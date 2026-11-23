# v15.7.2 → v15.7.3 · 最優先の変更候補 (23)

[一覧の目次](README.md)

<a id="compare-a27c8fedd49bcca1100811e076df9438"></a>

### [`00593d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593d0c.md) → [`00593d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593d0c.md) FUN_00593d0c

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00593d28",
      "incomplete_value": false,
      "site": "00593d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593d28",
      "incomplete_value": false,
      "site": "00593d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00593d28",
      "DATA",
      [
        "storage",
        "00bf3278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593d28",
      "DATA",
      [
        "storage",
        "00bf3328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593d0c.md#insn-00593d24)
- 新版 `00593d24`（命令位置の公開資料なし）

~~~diff
- 00593d24 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00593d24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00593d24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00593d24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00593d24 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00593d24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00593d24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00593d24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00593d24 bytes 29e10991
+ 00593d24 bytes 29a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4bc6b909de7a865c88c87fa3586ed40"></a>

### [`00593e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593e50.md) → [`00593e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593e50.md) FUN_00593e50

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058f9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058f9b0.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0058f9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058f9b0.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00593e88",
      "incomplete_value": false,
      "site": "00593e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593e88",
      "incomplete_value": false,
      "site": "00593e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "00593e90",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00593f48",
      "READ",
      [
        "storage",
        "00bf30a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593e90",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00593f48",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593e50.md#insn-00593e88) · [`00593e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593e50.md#insn-00593e8c)
- 新版 `00593e88`（命令位置の公開資料なし） · `00593e8c`（命令位置の公開資料なし）

~~~diff
- 00593e88 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00593e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00593e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00593e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00593e88 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00593e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00593e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00593e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00593e88 bytes 08610291
+ 00593e88 bytes 08210591
- 00593e8c ["COPY", "register:4098:8", ["register:4000:8"]]
- 00593e8c bytes f30300aa
+ 00593e8c ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00593e8c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fe8777f0e0e98feea28d5396840d65f"></a>

### [`00593fc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593fc8.md) → [`00593fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00593/00593fc8.md) FUN_00593fc8

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
      "definition_site": "00593fd4",
      "incomplete_value": false,
      "site": "00593fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00593fd4",
      "incomplete_value": false,
      "site": "00593fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00593fe0",
      "DATA",
      [
        "storage",
        "00bf32f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00593fe0",
      "DATA",
      [
        "storage",
        "00bf33a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00593fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00593/00593fc8.md#insn-00593fd4)
- 新版 `00593fd4`（命令位置の公開資料なし）

~~~diff
- 00593fd4 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 00593fd4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00593fd4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00593fd4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00593fd4 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 00593fd4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00593fd4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00593fd4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00593fd4 bytes 4ae10b91
+ 00593fd4 bytes 4aa10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c405d2ef0c199640d55519b70364791"></a>

### [`0059400c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/0059400c.md) → [`0059400c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/0059400c.md) FUN_0059400c

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
      "definition_site": "00594024",
      "incomplete_value": false,
      "site": "00594030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594024",
      "incomplete_value": false,
      "site": "00594030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "00594030",
      "DATA",
      [
        "storage",
        "00bf32f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594030",
      "DATA",
      [
        "storage",
        "00bf33a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/0059400c.md#insn-00594024)
- 新版 `00594024`（命令位置の公開資料なし）

~~~diff
- 00594024 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 00594024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594024 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 00594024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594024 bytes 08e10b91
+ 00594024 bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-345d676b37e5664d04cd556ead22b91a"></a>

### [`00594068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594068.md) → [`00594068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594068.md) FUN_00594068

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00594094",
      "incomplete_value": false,
      "site": "00594094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594094",
      "incomplete_value": false,
      "site": "00594094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "00594094",
      "DATA",
      [
        "storage",
        "00bf32f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594094",
      "DATA",
      [
        "storage",
        "00bf33a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059408c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594068.md#insn-0059408c)
- 新版 `0059408c`（命令位置の公開資料なし）

~~~diff
- 0059408c ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 0059408c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059408c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059408c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059408c ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0059408c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059408c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059408c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059408c bytes 08e10b91
+ 0059408c bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b6c1a9c44efa7f73d3b106b6768fb62"></a>

### [`005940f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/005940f0.md) → [`005940f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/005940f0.md) FUN_005940f0

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059410c",
      "incomplete_value": false,
      "site": "0059410c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059410c",
      "incomplete_value": false,
      "site": "0059410c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "0059410c",
      "DATA",
      [
        "storage",
        "00bf32f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0059410c",
      "DATA",
      [
        "storage",
        "00bf33a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/005940f0.md#insn-00594108)
- 新版 `00594108`（命令位置の公開資料なし）

~~~diff
- 00594108 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 00594108 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00594108 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00594108 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00594108 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 00594108 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00594108 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00594108 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00594108 bytes 29e10b91
+ 00594108 bytes 29a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-514db4e8faddf31b8505671843aa6397"></a>

### [`005943f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/005943f4.md) → [`005943f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/005943f4.md) FUN_005943f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0058ff20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058f/0058ff20.md) · 呼出先 7件 [`00588310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00588/00588310.md) [`005945ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/005945ac.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0058ff20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058f/0058ff20.md) · 呼出先 7件 [`00588310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00588/00588310.md) [`005945ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/005945ac.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059442c",
      "incomplete_value": false,
      "site": "00594434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059442c",
      "incomplete_value": false,
      "site": "00594434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "00594434",
      "DATA",
      [
        "storage",
        "00bf3378",
        null,
        "pointer"
      ]
    ],
    [
      "005944ec",
      "READ",
      [
        "storage",
        "00bf3388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594434",
      "DATA",
      [
        "storage",
        "00bf3428",
        null,
        "pointer"
      ]
    ],
    [
      "005944ec",
      "READ",
      [
        "storage",
        "00bf3438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059442c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/005943f4.md#insn-0059442c) · [`00594430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/005943f4.md#insn-00594430)
- 新版 `0059442c`（命令位置の公開資料なし） · `00594430`（命令位置の公開資料なし）

~~~diff
- 0059442c ["COPY", "tmp:0:8", ["const:378:8"]]
- 0059442c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059442c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059442c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059442c ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0059442c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059442c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059442c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059442c bytes 08e10d91
+ 0059442c bytes 08a11091
- 00594430 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00594430 bytes f30300aa
+ 00594430 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00594430 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56d56f5be6121e10b8e2fc1977a388d7"></a>

### [`0059457c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/0059457c.md) → [`0059457c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/0059457c.md) FUN_0059457c

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
      "definition_site": "0059458c",
      "incomplete_value": false,
      "site": "00594594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059458c",
      "incomplete_value": false,
      "site": "00594594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "00594594",
      "DATA",
      [
        "storage",
        "00bf3378",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00594594",
      "DATA",
      [
        "storage",
        "00bf3428",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059458c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/0059457c.md#insn-0059458c)
- 新版 `0059458c`（命令位置の公開資料なし）

~~~diff
- 0059458c ["COPY", "tmp:0:8", ["const:378:8"]]
- 0059458c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059458c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059458c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059458c ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0059458c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059458c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059458c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059458c bytes 08e10d91
+ 0059458c bytes 08a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4a9b4699a668fe346d809d8641be54c"></a>

### [`0059465c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/0059465c.md) → [`0059465c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/0059465c.md) FUN_0059465c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00594688",
      "incomplete_value": false,
      "site": "00594688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594688",
      "incomplete_value": false,
      "site": "00594688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
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
      "00594688",
      "DATA",
      [
        "storage",
        "00bf33c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594688",
      "DATA",
      [
        "storage",
        "00bf3478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/0059465c.md#insn-00594680)
- 新版 `00594680`（命令位置の公開資料なし）

~~~diff
- 00594680 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 00594680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594680 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00594680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594680 bytes 08210f91
+ 00594680 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b8d978ee375c6b2618e1f47cf0b867f"></a>

### [`005946e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/005946e4.md) → [`005946e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/005946e4.md) FUN_005946e4

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00594700",
      "incomplete_value": false,
      "site": "00594700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594700",
      "incomplete_value": false,
      "site": "00594700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00594700",
      "DATA",
      [
        "storage",
        "00bf33c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594700",
      "DATA",
      [
        "storage",
        "00bf3478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005946fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/005946e4.md#insn-005946fc)
- 新版 `005946fc`（命令位置の公開資料なし）

~~~diff
- 005946fc ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 005946fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005946fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005946fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005946fc ["COPY", "tmp:0:8", ["const:478:8"]]
+ 005946fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005946fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005946fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005946fc bytes 29210f91
+ 005946fc bytes 29e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb7ba4b44665e4f42a26aa45137b490"></a>

### [`00594944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594944.md) → [`00594944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594944.md) FUN_00594944

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00590428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00590/00590428.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`00590428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00590/00590428.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059497c",
      "incomplete_value": false,
      "site": "00594984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059497c",
      "incomplete_value": false,
      "site": "00594984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "00594984",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00594a3c",
      "READ",
      [
        "storage",
        "00bf30a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594984",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00594a3c",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059497c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594944.md#insn-0059497c) · [`00594980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594944.md#insn-00594980)
- 新版 `0059497c`（命令位置の公開資料なし） · `00594980`（命令位置の公開資料なし）

~~~diff
- 0059497c ["COPY", "tmp:0:8", ["const:98:8"]]
- 0059497c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059497c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059497c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059497c ["COPY", "tmp:0:8", ["const:148:8"]]
+ 0059497c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059497c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059497c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059497c bytes 08610291
+ 0059497c bytes 08210591
- 00594980 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00594980 bytes f30300aa
+ 00594980 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00594980 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99eab3279d49ed9f7d358e7b4f590fda"></a>

### [`00594abc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594abc.md) → [`00594abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594abc.md) FUN_00594abc

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
      "definition_site": "00594ac8",
      "incomplete_value": false,
      "site": "00594ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594ac8",
      "incomplete_value": false,
      "site": "00594ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00594ad4",
      "DATA",
      [
        "storage",
        "00bf3448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594ad4",
      "DATA",
      [
        "storage",
        "00bf34f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594abc.md#insn-00594ac8)
- 新版 `00594ac8`（命令位置の公開資料なし）

~~~diff
- 00594ac8 ["COPY", "tmp:0:8", ["const:448:8"]]
- 00594ac8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00594ac8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00594ac8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00594ac8 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00594ac8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00594ac8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00594ac8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00594ac8 bytes 4a211191
+ 00594ac8 bytes 4ae11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-710acf0bfc340e71e1a98e2e340a9f2d"></a>

### [`00594b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594b00.md) → [`00594b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594b00.md) FUN_00594b00

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
      "definition_site": "00594b18",
      "incomplete_value": false,
      "site": "00594b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594b18",
      "incomplete_value": false,
      "site": "00594b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00594b24",
      "DATA",
      [
        "storage",
        "00bf3448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594b24",
      "DATA",
      [
        "storage",
        "00bf34f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594b00.md#insn-00594b18)
- 新版 `00594b18`（命令位置の公開資料なし）

~~~diff
- 00594b18 ["COPY", "tmp:0:8", ["const:448:8"]]
- 00594b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594b18 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00594b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594b18 bytes 08211191
+ 00594b18 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec52fe15f9da52fb693def658ea2a337"></a>

### [`00594b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594b5c.md) → [`00594b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594b5c.md) FUN_00594b5c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00594b88",
      "incomplete_value": false,
      "site": "00594b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594b88",
      "incomplete_value": false,
      "site": "00594b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:448:8"
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
      "00594b88",
      "DATA",
      [
        "storage",
        "00bf3448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594b88",
      "DATA",
      [
        "storage",
        "00bf34f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594b5c.md#insn-00594b80)
- 新版 `00594b80`（命令位置の公開資料なし）

~~~diff
- 00594b80 ["COPY", "tmp:0:8", ["const:448:8"]]
- 00594b80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00594b80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00594b80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00594b80 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00594b80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00594b80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00594b80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00594b80 bytes 08211191
+ 00594b80 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce22d2f90cea20554b46e9af9c312a27"></a>

### [`00594be4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594be4.md) → [`00594be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594be4.md) FUN_00594be4

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00594c00",
      "incomplete_value": false,
      "site": "00594c00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00594c00",
      "incomplete_value": false,
      "site": "00594c00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
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
      "00594c00",
      "DATA",
      [
        "storage",
        "00bf3448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00594c00",
      "DATA",
      [
        "storage",
        "00bf34f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00594bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594be4.md#insn-00594bfc)
- 新版 `00594bfc`（命令位置の公開資料なし）

~~~diff
- 00594bfc ["COPY", "tmp:0:8", ["const:448:8"]]
- 00594bfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00594bfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00594bfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00594bfc ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00594bfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00594bfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00594bfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00594bfc bytes 29211191
+ 00594bfc bytes 29e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-741e4adf567a23510d02bcd9fb8d9aac"></a>

### [`00594ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594ff8.md) → [`00594ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00594/00594ff8.md) _INIT_58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.22% / 新版 93.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00595220",
      "incomplete_value": false,
      "site": "0059522c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595220",
      "incomplete_value": false,
      "site": "0059522c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:838:8"
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
      "definition_site": "00595228",
      "incomplete_value": false,
      "site": "0059522c",
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
      "definition_site": "00595228",
      "incomplete_value": false,
      "site": "0059522c",
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
      "00595034",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00595058",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00595078",
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
      "00595034",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00595058",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00595078",
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

- 旧版 [`00595024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594ff8.md#insn-00595024) · [`00595030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594ff8.md#insn-00595030) · [`0059504c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00594/00594ff8.md#insn-0059504c)
- 新版 `00595024`（命令位置の公開資料なし） · `00595030`（命令位置の公開資料なし） · `0059504c`（命令位置の公開資料なし）

~~~diff
- 00595024 ["COPY", "tmp:0:8", ["const:838:8"]]
- 00595024 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00595024 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00595024 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00595024 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 00595024 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00595024 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00595024 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00595024 bytes 73e22091
+ 00595024 bytes 73e22391
- 00595030 ["COPY", "tmp:0:8", ["const:2e4:8"]]
- 00595030 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00595030 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00595030 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00595030 ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 00595030 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00595030 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00595030 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00595030 bytes 29910b91
+ 00595030 bytes 29750b91
- 0059504c ["COPY", "tmp:0:8", ["const:2f7:8"]]
- 0059504c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059504c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059504c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059504c ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 0059504c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059504c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059504c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059504c bytes 4add0b91
+ 0059504c bytes 4ac10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee65a625975bdedd8f809ac2a1ce1ec2"></a>

### [`005954e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00595/005954e4.md) → [`005954e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/005954e4.md) FUN_005954e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00595470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00595/00595470.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00595470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/00595470.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.65% / 新版 93.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595534",
      "incomplete_value": false,
      "site": "0059553c",
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
      "definition_site": "00595534",
      "incomplete_value": false,
      "site": "0059553c",
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
      "definition_site": "00595724",
      "incomplete_value": true,
      "site": "00595728",
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
      "definition_site": "00595724",
      "incomplete_value": true,
      "site": "00595728",
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
      "definition_site": "00595720",
      "incomplete_value": true,
      "site": "0059572c",
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
      "definition_site": "00595720",
      "incomplete_value": true,
      "site": "0059572c",
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
      "0059553c",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00595564",
      "PARAM",
      [
        "storage",
        "00c26870",
        null,
        null
      ]
    ],
    [
      "00595714",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0059553c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00595564",
      "PARAM",
      [
        "storage",
        "00c26930",
        null,
        null
      ]
    ],
    [
      "00595714",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00595/005954e4.md#insn-00595534) · [`00595564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00595/005954e4.md#insn-00595564) · [`00595714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00595/005954e4.md#insn-00595714)
- 新版 `00595534`（命令位置の公開資料なし） · `00595564`（命令位置の公開資料なし） · `00595714`（命令位置の公開資料なし）

~~~diff
- 00595534 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00595534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00595534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00595534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595534 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00595534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00595534 bytes 08e13191
+ 00595534 bytes 08a13491
- 00595564 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00595564 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00595564 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00595564 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00595564 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 00595564 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00595564 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00595564 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00595564 bytes 00c02191
+ 00595564 bytes 00c02491
- 00595714 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 00595714 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00595714 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 00595714 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00595714 bytes 086146f9
+ 00595714 bytes 08b946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-387803ec145ee7975070296c503d02c7"></a>

### [`005958c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00595/005958c4.md) → [`005958c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/005958c4.md) _INIT_59

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00b55550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55550.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.69% / 新版 84.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 2件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00595900",
      "incomplete_value": true,
      "site": "0059591c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00595900",
      "incomplete_value": true,
      "site": "0059591c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00595924",
      "incomplete_value": true,
      "site": "00595940",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00595924",
      "incomplete_value": true,
      "site": "00595940",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00595944",
      "incomplete_value": true,
      "site": "00595960",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00595944",
      "incomplete_value": true,
      "site": "00595960",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00595900",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00595924",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00595944",
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
      "00595900",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00595924",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00595944",
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

- 旧版 [`005958f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00595/005958c4.md#insn-005958f0) · [`005958f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00595/005958c4.md#insn-005958f8)
- 新版 `005958f0`（命令位置の公開資料なし） · `005958f8`（命令位置の公開資料なし）

~~~diff
- 005958f0 ["COPY", "tmp:0:8", ["const:850:8"]]
- 005958f0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005958f0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005958f0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005958f0 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 005958f0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005958f0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005958f0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005958f0 bytes 73422191
+ 005958f0 bytes 73422491
- 005958f8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 005958f8 bytes 89e8ffd0
+ 005958f8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 005958f8 bytes 89e8ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89502dd2cbfb156355c199049ecbce98"></a>

### [`00595ca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00595/00595ca0.md) → [`00595ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00595/00595ca0.md) FUN_00595ca0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0081fa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081fa64.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff0.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.40% / 新版 84.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00595cdc",
      "incomplete_value": false,
      "site": "00595ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595cdc",
      "incomplete_value": false,
      "site": "00595ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "definition_site": "00595d48",
      "incomplete_value": true,
      "site": "00595d48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:315:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595d48",
      "incomplete_value": true,
      "site": "00595d48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:288:8"
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
      "definition_site": "00595d60",
      "incomplete_value": true,
      "site": "00595d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00595d60",
      "incomplete_value": true,
      "site": "00595d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ea:8"
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
      "00595ce0",
      "DATA",
      [
        "storage",
        "00bf34c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00595d14",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00595d34",
      "READ",
      [
        "storage",
        "002a0288",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00595ce0",
      "DATA",
      [
        "storage",
        "00bf3578",
        null,
        "undefined *"
      ]
    ],
    [
      "00595d14",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00595d34",
      "READ",
      [
        "storage",
        "002a0315",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00595/00595ca0.md#insn-00595cdc) · [`00595d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00595/00595ca0.md#insn-00595d0c) · [`00595d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00595/00595ca0.md#insn-00595d10)
- 新版 `00595cdc`（命令位置の公開資料なし） · `00595d0c`（命令位置の公開資料なし） · `00595d10`（命令位置の公開資料なし）

~~~diff
- 00595cdc ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 00595cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00595cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00595cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00595cdc ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00595cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00595cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00595cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00595cdc bytes 08211391
+ 00595cdc bytes 08e11591
- 00595d0c ["COPY", "register:40c8:8", ["const:c24000:8"]]
+ 00595d0c ["COPY", "register:40c8:8", ["const:c25000:8"]]
- 00595d0c bytes 793400f0
+ 00595d0c bytes 99340090
- 00595d10 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00595d10 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00595d10 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00595d10 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00595d10 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00595d10 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00595d10 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00595d10 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00595d10 bytes 39e33d91
+ 00595d10 bytes 39e30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63d82063d75e46c60bdcc95c37a598c0"></a>

### [`005962e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/005962e8.md) → [`005962e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/005962e8.md) FUN_005962e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`0059675c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/0059675c.md) [`0059682c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/0059682c.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0059675c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/0059675c.md) [`0059682c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/0059682c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00596328",
      "incomplete_value": false,
      "site": "00596330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596328",
      "incomplete_value": false,
      "site": "00596330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "definition_site": "00596438",
      "incomplete_value": false,
      "site": "0059643c",
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
      "definition_site": "00596438",
      "incomplete_value": false,
      "site": "0059643c",
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
      "00596330",
      "DATA",
      [
        "storage",
        "00bf3528",
        null,
        "pointer"
      ]
    ],
    [
      "005963d4",
      "READ",
      [
        "storage",
        "00bf3538",
        null,
        "undefined *"
      ]
    ],
    [
      "00596438",
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
      "00596330",
      "DATA",
      [
        "storage",
        "00bf35d8",
        null,
        "pointer"
      ]
    ],
    [
      "005963d4",
      "READ",
      [
        "storage",
        "00bf35e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00596438",
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

- 旧版 [`00596328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/005962e8.md#insn-00596328) · [`00596438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/005962e8.md#insn-00596438)
- 新版 `00596328`（命令位置の公開資料なし） · `00596438`（命令位置の公開資料なし）

~~~diff
- 00596328 ["COPY", "tmp:0:8", ["const:528:8"]]
- 00596328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00596328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00596328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00596328 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00596328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00596328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00596328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00596328 bytes 08a11491
+ 00596328 bytes 08611791
- 00596438 ["COPY", "tmp:0:8", ["const:544:8"]]
- 00596438 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00596438 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00596438 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00596438 ["COPY", "tmp:0:8", ["const:5d1:8"]]
+ 00596438 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00596438 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00596438 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00596438 bytes 21101591
+ 00596438 bytes 21441791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5adf260c95d25fe12fdb61fa46d509c"></a>

### [`005964f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/005964f4.md) → [`005964f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/005964f4.md) FUN_005964f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb590.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb640.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0059650c",
      "incomplete_value": false,
      "site": "00596510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059650c",
      "incomplete_value": false,
      "site": "00596510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "00596510",
      "DATA",
      [
        "storage",
        "00bf34c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00596510",
      "DATA",
      [
        "storage",
        "00bf3578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059650c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/005964f4.md#insn-0059650c)
- 新版 `0059650c`（命令位置の公開資料なし）

~~~diff
- 0059650c ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 0059650c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059650c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059650c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059650c ["COPY", "tmp:0:8", ["const:578:8"]]
+ 0059650c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059650c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059650c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059650c bytes 29211391
+ 0059650c bytes 29e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-382b6dbe41d3db53f3e4f4046ee69812"></a>

### [`005965a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/005965a8.md) → [`005965a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/005965a8.md) FUN_005965a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb590.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb640.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005965c0",
      "incomplete_value": false,
      "site": "005965c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005965c0",
      "incomplete_value": false,
      "site": "005965c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "005965c4",
      "DATA",
      [
        "storage",
        "00bf34c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005965c4",
      "DATA",
      [
        "storage",
        "00bf3578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005965c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/005965a8.md#insn-005965c0)
- 新版 `005965c0`（命令位置の公開資料なし）

~~~diff
- 005965c0 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 005965c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005965c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005965c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005965c0 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 005965c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005965c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005965c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005965c0 bytes 29211391
+ 005965c0 bytes 29e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8db891cf6078cd6ffe24a92b3030a581"></a>

### [`00596708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596708.md) → [`00596708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596708.md) FUN_00596708

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdaf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf10.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb180.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)

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
      "definition_site": "0059672c",
      "incomplete_value": true,
      "site": "0059672c",
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
      "definition_site": "0059672c",
      "incomplete_value": true,
      "site": "0059672c",
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
      "00596720",
      "READ",
      [
        "storage",
        "00c1ad60",
        null,
        "pointer"
      ]
    ],
    [
      "0059672c",
      "DATA",
      [
        "storage",
        "00c12e30",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00596720",
      "READ",
      [
        "storage",
        "00c1ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0059672c",
      "DATA",
      [
        "storage",
        "00c12ee0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596708.md#insn-00596720)
- 新版 `00596720`（命令位置の公開資料なし）

~~~diff
- 00596720 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d60:8"]]
- 00596720 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00596720 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 00596720 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00596720 bytes 08b146f9
+ 00596720 bytes 080947f9
~~~


<a id="compare-21049a84271d3644fef2c62b8533c19c"></a>

### [`00596948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596948.md) → [`00596948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596948.md) _INIT_60

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.40% / 新版 90.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00596a04",
      "incomplete_value": true,
      "site": "00596a20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00596a04",
      "incomplete_value": true,
      "site": "00596a20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_value",
    "new": {
      "definition_site": "00596a44",
      "incomplete_value": true,
      "site": "00596a88",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:5b3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596a44",
      "incomplete_value": true,
      "site": "00596a88",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:294000:8"
              ],
              [
                "leaf",
                "const:526:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00596b70",
      "incomplete_value": false,
      "site": "00596b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596b70",
      "incomplete_value": false,
      "site": "00596b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:888:8"
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
      "00596984",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "005969a8",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "005969c8",
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
      "00596984",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "005969a8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "005969c8",
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

- 旧版 [`00596974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596948.md#insn-00596974) · [`0059697c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596948.md#insn-0059697c)
- 新版 `00596974`（命令位置の公開資料なし） · `0059697c`（命令位置の公開資料なし）

~~~diff
- 00596974 ["COPY", "tmp:0:8", ["const:888:8"]]
- 00596974 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00596974 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00596974 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00596974 ["COPY", "tmp:0:8", ["const:948:8"]]
+ 00596974 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00596974 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00596974 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00596974 bytes 73222291
+ 00596974 bytes 73222591
- 0059697c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0059697c bytes 89e8ffb0
+ 0059697c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0059697c bytes 89e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7ce5fe10d769be2542bab0f5af1af57"></a>

### [`00596d14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596d14.md) → [`00596d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596d14.md) FUN_00596d14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596cd8.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596cd8.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.54% / 新版 91.54%

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
      "definition_site": "00596d54",
      "incomplete_value": false,
      "site": "00596d60",
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
      "definition_site": "00596d54",
      "incomplete_value": false,
      "site": "00596d60",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00596d88",
      "incomplete_value": true,
      "site": "00596d98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cc3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00596d88",
      "incomplete_value": true,
      "site": "00596d98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c36:8"
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
      "definition_site": "00596d8c",
      "incomplete_value": true,
      "site": "00596d9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00596d8c",
      "incomplete_value": true,
      "site": "00596d9c",
      "value": [
        "LOAD",
        "8",
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
      "00596d60",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00596d88",
      "READ",
      [
        "storage",
        "00291c36",
        null,
        "string"
      ]
    ],
    [
      "00596d8c",
      "READ",
      [
        "storage",
        "00291c46",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00596d60",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00596d88",
      "READ",
      [
        "storage",
        "00291cc3",
        null,
        "string"
      ]
    ],
    [
      "00596d8c",
      "READ",
      [
        "storage",
        "00291cd3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00596d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596d14.md#insn-00596d54) · [`00596d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596d14.md#insn-00596d80) · [`00596d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596d14.md#insn-00596d84)
- 新版 `00596d54`（命令位置の公開資料なし） · `00596d80`（命令位置の公開資料なし）

~~~diff
- 00596d54 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00596d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00596d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00596d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00596d54 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00596d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00596d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00596d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00596d54 bytes 08e13191
+ 00596d54 bytes 08a13491
- 00596d80 ["COPY", "tmp:0:8", ["const:c36:8"]]
- 00596d80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00596d80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00596d80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00596d80 ["COPY", "tmp:0:8", ["const:cc3:8"]]
+ 00596d80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00596d80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00596d80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00596d80 bytes 08d93091
+ 00596d80 bytes 080d3391
- 00596d84 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00596d84 bytes c9e8ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6196ea19381eeea4606deddfaab7baa7"></a>

### [`00597088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/00597088.md) → [`00597088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597088.md) FUN_00597088

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596cd8.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596cd8.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.57% / 新版 96.57%

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
      "definition_site": "005970c8",
      "incomplete_value": false,
      "site": "005970cc",
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
      "definition_site": "005970c8",
      "incomplete_value": false,
      "site": "005970cc",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005970e4",
      "incomplete_value": true,
      "site": "005970f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005970e4",
      "incomplete_value": true,
      "site": "005970f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:55c:8"
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
      "definition_site": "005970e8",
      "incomplete_value": true,
      "site": "005970f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005970e8",
      "incomplete_value": true,
      "site": "005970f8",
      "value": [
        "LOAD",
        "8",
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
      "005970cc",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "005970e4",
      "READ",
      [
        "storage",
        "0029d55c",
        null,
        "string"
      ]
    ],
    [
      "005970e8",
      "READ",
      [
        "storage",
        "0029d56c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005970cc",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "005970e4",
      "READ",
      [
        "storage",
        "0029d5e9",
        null,
        "string"
      ]
    ],
    [
      "005970e8",
      "READ",
      [
        "storage",
        "0029d5f9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005970c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/00597088.md#insn-005970c8) · [`005970dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/00597088.md#insn-005970dc) · [`005970e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/00597088.md#insn-005970e0)
- 新版 `005970c8`（命令位置の公開資料なし） · `005970dc`（命令位置の公開資料なし）

~~~diff
- 005970c8 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 005970c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005970c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005970c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005970c8 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 005970c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005970c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005970c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005970c8 bytes 08e13191
+ 005970c8 bytes 08a13491
- 005970dc ["COPY", "tmp:0:8", ["const:55c:8"]]
- 005970dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005970dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005970dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005970dc ["COPY", "tmp:0:8", ["const:5e9:8"]]
+ 005970dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005970dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005970dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005970dc bytes 08711591
+ 005970dc bytes 08a51791
- 005970e0 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 005970e0 bytes c9e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78c65d96f0f5b97f0231505d01ec67d5"></a>

### [`005978a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/005978a4.md) → [`005978a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/005978a4.md) FUN_005978a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596cd8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596cd8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005978e4",
      "incomplete_value": false,
      "site": "005978ec",
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
      "definition_site": "005978e4",
      "incomplete_value": false,
      "site": "005978ec",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00597908",
      "incomplete_value": true,
      "site": "00597918",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a47:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597908",
      "incomplete_value": true,
      "site": "00597918",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9ba:8"
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
      "definition_site": "0059790c",
      "incomplete_value": true,
      "site": "0059791c",
      "value": [
        "LOAD",
        "16",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059790c",
      "incomplete_value": true,
      "site": "0059791c",
      "value": [
        "LOAD",
        "16",
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
                "const:9:8"
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
      "005978ec",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00597908",
      "READ",
      [
        "storage",
        "002929ba",
        null,
        "string"
      ]
    ],
    [
      "0059790c",
      "READ",
      [
        "storage",
        "002929c3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005978ec",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00597908",
      "READ",
      [
        "storage",
        "00292a47",
        null,
        "string"
      ]
    ],
    [
      "0059790c",
      "READ",
      [
        "storage",
        "00292a50",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005978e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/005978a4.md#insn-005978e4) · [`00597900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/005978a4.md#insn-00597900) · [`00597904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/005978a4.md#insn-00597904)
- 新版 `005978e4`（命令位置の公開資料なし） · `00597900`（命令位置の公開資料なし）

~~~diff
- 005978e4 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 005978e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005978e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005978e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005978e4 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 005978e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005978e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005978e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005978e4 bytes 29e13191
+ 005978e4 bytes 29a13491
- 00597900 ["COPY", "tmp:0:8", ["const:9ba:8"]]
- 00597900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00597900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00597900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00597900 ["COPY", "tmp:0:8", ["const:a47:8"]]
+ 00597900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00597900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00597900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00597900 bytes 08e92691
+ 00597900 bytes 081d2991
- 00597904 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00597904 bytes c9e8ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-770f3014a370898e73f4648ceb329cdb"></a>

### [`00597bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/00597bc8.md) → [`00597bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597bc8.md) FUN_00597bc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596cd8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464ca8.md)
- 新版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596cd8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.63% / 新版 89.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00597c0c",
      "incomplete_value": false,
      "site": "00597c14",
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
      "definition_site": "00597c0c",
      "incomplete_value": false,
      "site": "00597c14",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00597c30",
      "incomplete_value": true,
      "site": "00597c40",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:841:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597c30",
      "incomplete_value": true,
      "site": "00597c40",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:83b:8"
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
      "definition_site": "00597c34",
      "incomplete_value": true,
      "site": "00597c44",
      "value": [
        "LOAD",
        "16",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597c34",
      "incomplete_value": true,
      "site": "00597c44",
      "value": [
        "LOAD",
        "16",
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
                "const:9:8"
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
      "00597c14",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00597c30",
      "READ",
      [
        "storage",
        "002ab83b",
        null,
        "string"
      ]
    ],
    [
      "00597c34",
      "READ",
      [
        "storage",
        "002ab844",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00597c14",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00597c30",
      "READ",
      [
        "storage",
        "002ab841",
        null,
        "string"
      ]
    ],
    [
      "00597c34",
      "READ",
      [
        "storage",
        "002ab84a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00597c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/00597bc8.md#insn-00597c0c) · [`00597c28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/00597bc8.md#insn-00597c28) · [`00597c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/00597bc8.md#insn-00597c2c)
- 新版 `00597c0c`（命令位置の公開資料なし） · `00597c28`（命令位置の公開資料なし）

~~~diff
- 00597c0c ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00597c0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00597c0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00597c0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00597c0c ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00597c0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00597c0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00597c0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00597c0c bytes 29e13191
+ 00597c0c bytes 29a13491
- 00597c28 ["COPY", "tmp:0:8", ["const:83b:8"]]
- 00597c28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00597c28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00597c28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00597c28 ["COPY", "tmp:0:8", ["const:841:8"]]
+ 00597c28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00597c28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00597c28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00597c28 bytes 08ed2091
+ 00597c28 bytes 08052191
- 00597c2c ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00597c2c bytes c9e8ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16208536c35d0d2d2da3061a3f9fa1b8"></a>

### [`00597ea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/00597ea8.md) → [`00597ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/00597ea8.md) FUN_00597ea8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/00596cd8.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00596cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/00596cd8.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.03% / 新版 89.03%

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
      "definition_site": "00597ee8",
      "incomplete_value": false,
      "site": "00597ef8",
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
      "definition_site": "00597ee8",
      "incomplete_value": false,
      "site": "00597ef8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00597f1c",
      "incomplete_value": true,
      "site": "00597f2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ba:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00597f1c",
      "incomplete_value": true,
      "site": "00597f2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6c1:8"
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
      "definition_site": "00597f20",
      "incomplete_value": true,
      "site": "00597f30",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00597f20",
      "incomplete_value": true,
      "site": "00597f30",
      "value": [
        "LOAD",
        "16",
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
      "00597ef8",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00597f1c",
      "READ",
      [
        "storage",
        "002a46c1",
        null,
        "string"
      ]
    ],
    [
      "00597f20",
      "READ",
      [
        "storage",
        "002a46cf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00597ef8",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00597f1c",
      "READ",
      [
        "storage",
        "002a46ba",
        null,
        "string"
      ]
    ],
    [
      "00597f20",
      "READ",
      [
        "storage",
        "002a46c8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00597ee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/00597ea8.md#insn-00597ee8) · [`00597f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/00597ea8.md#insn-00597f14) · [`00597f18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/00597ea8.md#insn-00597f18)
- 新版 `00597ee8`（命令位置の公開資料なし） · `00597f14`（命令位置の公開資料なし）

~~~diff
- 00597ee8 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00597ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00597ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00597ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00597ee8 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00597ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00597ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00597ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00597ee8 bytes 08e13191
+ 00597ee8 bytes 08a13491
- 00597f14 ["COPY", "tmp:0:8", ["const:6c1:8"]]
- 00597f14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00597f14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00597f14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00597f14 ["COPY", "tmp:0:8", ["const:6ba:8"]]
+ 00597f14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00597f14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00597f14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00597f14 bytes 08051b91
+ 00597f14 bytes 08e91a91
- 00597f18 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00597f18 bytes c9e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5369969b01547768f2f6da47f980210"></a>

### [`0059815c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00598/0059815c.md) → [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) FUN_0059815c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00a90870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90870.md) [`00a90e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90e28.md) · 呼出先 59件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a8d8.md) [`0044abe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044abe4.md) [`0044abfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044abfc.md)
- 新版 呼出元 2件 [`00a90870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90870.md) [`00a90e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90e28.md) · 呼出先 59件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`0044abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abfc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.49% / 新版 99.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005984b8",
      "incomplete_value": true,
      "site": "005984b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "005984b8",
      "incomplete_value": true,
      "site": "005984b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:135:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00599cc0",
      "incomplete_value": true,
      "site": "00599cd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:58f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00599cc0",
      "incomplete_value": true,
      "site": "00599cd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:596:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 271,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059a060",
      "incomplete_value": true,
      "site": "0059a070",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:602:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059a060",
      "incomplete_value": true,
      "site": "0059a070",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:575:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 311,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005984a0",
      "READ",
      [
        "storage",
        "002a8135",
        null,
        "string"
      ]
    ],
    [
      "00599cc0",
      "READ",
      [
        "storage",
        "002a3596",
        null,
        "string"
      ]
    ],
    [
      "0059a060",
      "READ",
      [
        "storage",
        "0029d575",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005984a0",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ],
    [
      "00599cc0",
      "READ",
      [
        "storage",
        "002a358f",
        null,
        "string"
      ]
    ],
    [
      "0059a060",
      "READ",
      [
        "storage",
        "0029d602",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00598494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00598/0059815c.md#insn-00598494) · [`00599cbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00598/0059815c.md#insn-00599cbc) · [`0059a05c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00598/0059815c.md#insn-0059a05c)
- 新版 `00598494`（命令位置の公開資料なし） · `00599cbc`（命令位置の公開資料なし） · `0059a05c`（命令位置の公開資料なし）

~~~diff
- 00598494 ["COPY", "tmp:0:8", ["const:135:8"]]
- 00598494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00598494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00598494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00598494 ["COPY", "tmp:0:8", ["const:a1:8"]]
+ 00598494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00598494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00598494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00598494 bytes 29d50491
+ 00598494 bytes 29850291
- 00599cbc ["COPY", "tmp:0:8", ["const:596:8"]]
- 00599cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00599cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00599cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00599cbc ["COPY", "tmp:0:8", ["const:58f:8"]]
+ 00599cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00599cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00599cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00599cbc bytes 08591691
+ 00599cbc bytes 083d1691
- 0059a05c ["COPY", "tmp:0:8", ["const:575:8"]]
- 0059a05c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059a05c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059a05c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059a05c ["COPY", "tmp:0:8", ["const:602:8"]]
+ 0059a05c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a05c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059a05c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059a05c bytes 08d51591
+ 0059a05c bytes 08091891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35fa797033902d7f2d817413c4d4f71e"></a>

### [`0059d1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059d/0059d1c0.md) → [`0059d1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d1c0.md) FUN_0059d1c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005978a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00597/005978a4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005978a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00597/005978a4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0059d1cc",
      "incomplete_value": false,
      "site": "0059d1d0",
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
      "definition_site": "0059d1cc",
      "incomplete_value": false,
      "site": "0059d1d0",
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
      "0059d1cc",
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
      "0059d1cc",
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

- 旧版 [`0059d1cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059d/0059d1c0.md#insn-0059d1cc)
- 新版 `0059d1cc`（命令位置の公開資料なし）

~~~diff
- 0059d1cc ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0059d1cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0059d1cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0059d1cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0059d1cc ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0059d1cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0059d1cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0059d1cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0059d1cc bytes 00280c91
+ 0059d1cc bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b4118085b83a1e40cd2ba133e9c479"></a>

### [`0059d658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059d/0059d658.md) → [`0059d658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d658.md) FUN_0059d658

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0059815c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00598/0059815c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0059d664",
      "incomplete_value": true,
      "site": "0059d668",
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
            "const:303:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059d664",
      "incomplete_value": true,
      "site": "0059d668",
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
      "0059d664",
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
      "0059d664",
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

- 旧版 [`0059d664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059d/0059d658.md#insn-0059d664)
- 新版 `0059d664`（命令位置の公開資料なし）

~~~diff
- 0059d664 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0059d664 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0059d664 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0059d664 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0059d664 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0059d664 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0059d664 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0059d664 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0059d664 bytes 00280c91
+ 0059d664 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39e7f824093ccdd8e9d13557f44da0a9"></a>

### [`0059d66c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059d/0059d66c.md) → [`0059d66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d66c.md) FUN_0059d66c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`0059815c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00598/0059815c.md) [`0067417c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00674/0067417c.md) [`00678d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00678/00678d74.md) [`0067c708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0067c/0067c708.md) [`0086b704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 8件 [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) [`0067417c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00674/0067417c.md) [`00678d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678d74.md) [`0067c708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c708.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0059d678",
      "incomplete_value": false,
      "site": "0059d67c",
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
      "definition_site": "0059d678",
      "incomplete_value": false,
      "site": "0059d67c",
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
      "0059d678",
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
      "0059d678",
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

- 旧版 [`0059d678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059d/0059d66c.md#insn-0059d678)
- 新版 `0059d678`（命令位置の公開資料なし）

~~~diff
- 0059d678 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0059d678 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0059d678 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0059d678 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0059d678 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0059d678 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0059d678 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0059d678 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0059d678 bytes 00280c91
+ 0059d678 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1972e11457f03e30394548fa16ea19e"></a>

### [`0059f85c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059f85c.md) → [`0059f85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059f85c.md) _INIT_61

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059fa84",
      "incomplete_value": false,
      "site": "0059fa90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fa84",
      "incomplete_value": false,
      "site": "0059fa90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c26000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "definition_site": "0059fa8c",
      "incomplete_value": false,
      "site": "0059fa90",
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
      "definition_site": "0059fa8c",
      "incomplete_value": false,
      "site": "0059fa90",
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
      "0059f898",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0059f8bc",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0059f8dc",
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
      "0059f898",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0059f8bc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0059f8dc",
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

- 旧版 [`0059f888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059f85c.md#insn-0059f888) · [`0059f894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059f85c.md#insn-0059f894) · [`0059f8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059f85c.md#insn-0059f8b0)
- 新版 `0059f888`（命令位置の公開資料なし） · `0059f894`（命令位置の公開資料なし） · `0059f8b0`（命令位置の公開資料なし）

~~~diff
- 0059f888 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 0059f888 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0059f888 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0059f888 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0059f888 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 0059f888 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0059f888 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0059f888 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0059f888 bytes 73822291
+ 0059f888 bytes 73822591
- 0059f894 ["COPY", "tmp:0:8", ["const:2e4:8"]]
- 0059f894 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0059f894 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0059f894 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0059f894 ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 0059f894 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0059f894 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0059f894 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0059f894 bytes 29910b91
+ 0059f894 bytes 29750b91
- 0059f8b0 ["COPY", "tmp:0:8", ["const:2f7:8"]]
- 0059f8b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0059f8b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0059f8b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0059f8b0 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 0059f8b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0059f8b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0059f8b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0059f8b0 bytes 4add0b91
+ 0059f8b0 bytes 4ac10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2efc6b3ff6a1934824dccbc7979ed06"></a>

### [`0059fbec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059fbec.md) → [`0059fbec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059fbec.md) FUN_0059fbec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005a45f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a4/005a45f4.md) · 呼出先 16件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`0059ff30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059ff30.md) [`006612f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00661/006612f8.md)
- 新版 呼出元 1件 [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) · 呼出先 16件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0059ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059ff30.md) [`006612f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.59% / 新版 86.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 7件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0059fcb0",
      "incomplete_value": true,
      "site": "0059fcc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:717:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059fcb0",
      "incomplete_value": true,
      "site": "0059fcc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:68a:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0059fe4c",
      "incomplete_value": false,
      "site": "0059fe4c",
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
      "definition_site": "0059fe4c",
      "incomplete_value": false,
      "site": "0059fe4c",
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
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0059fe50",
      "incomplete_value": false,
      "site": "0059fe50",
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
      "definition_site": "0059fe50",
      "incomplete_value": false,
      "site": "0059fe50",
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
      "0059fc94",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "0059fcb0",
      "READ",
      [
        "storage",
        "002a068a",
        null,
        "string"
      ]
    ],
    [
      "0059fcb4",
      "READ",
      [
        "storage",
        "002a0699",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0059fc94",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0059fcb0",
      "READ",
      [
        "storage",
        "002a0717",
        null,
        "string"
      ]
    ],
    [
      "0059fcb4",
      "READ",
      [
        "storage",
        "002a0726",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059fc8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059fbec.md#insn-0059fc8c) · [`0059fc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059fbec.md#insn-0059fc90) · [`0059fca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059fbec.md#insn-0059fca8)
- 新版 `0059fc8c`（命令位置の公開資料なし） · `0059fc90`（命令位置の公開資料なし） · `0059fca8`（命令位置の公開資料なし）

~~~diff
- 0059fc8c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0059fc8c ["COPY", "register:4040:8", ["const:c25000:8"]]
- 0059fc8c bytes 283400b0
+ 0059fc8c bytes 283400d0
- 0059fc90 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0059fc90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059fc90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059fc90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059fc90 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0059fc90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059fc90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059fc90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059fc90 bytes 08e13d91
+ 0059fc90 bytes 08e10091
- 0059fca8 ["COPY", "tmp:0:8", ["const:68a:8"]]
- 0059fca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0059fca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0059fca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0059fca8 ["COPY", "tmp:0:8", ["const:717:8"]]
+ 0059fca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0059fca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0059fca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0059fca8 bytes 08291a91
+ 0059fca8 bytes 085d1c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbf45ea04726d4c391aacb3a2a35701c"></a>

### [`0059ff30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059ff30.md) → [`0059ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059ff30.md) FUN_0059ff30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0059fbec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059fbec.md) [`005a2308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a2/005a2308.md) · 呼出先 12件 [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0065ec80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065e/0065ec80.md) [`0065f044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065f/0065f044.md) [`0065f258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065f/0065f258.md) [`006612f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00661/006612f8.md)
- 新版 呼出元 2件 [`0059fbec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059fbec.md) [`005a2308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a2/005a2308.md) · 呼出先 12件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0065ec80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ec80.md) [`0065f044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f044.md) [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`006612f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.22% / 新版 96.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a00b8",
      "incomplete_value": true,
      "site": "005a00b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a83:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a00b8",
      "incomplete_value": true,
      "site": "005a00b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a8c:8"
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
      "definition_site": "005a00ac",
      "incomplete_value": true,
      "site": "005a00bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005a00ac",
      "incomplete_value": true,
      "site": "005a00bc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0059ffa8",
      "incomplete_value": false,
      "site": "0059ffb0",
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
            "const:85b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0059ffa8",
      "incomplete_value": false,
      "site": "0059ffb0",
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
            "const:855:8"
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
      "0059ffa8",
      "PARAM",
      [
        "storage",
        "002ab855",
        null,
        null
      ]
    ],
    [
      "005a00a8",
      "READ",
      [
        "storage",
        "002aca8c",
        null,
        "string"
      ]
    ],
    [
      "005a00ac",
      "READ",
      [
        "storage",
        "002aca93",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0059ffa8",
      "PARAM",
      [
        "storage",
        "002ab85b",
        null,
        null
      ]
    ],
    [
      "005a00a8",
      "READ",
      [
        "storage",
        "002aca83",
        null,
        "string"
      ]
    ],
    [
      "005a00ac",
      "READ",
      [
        "storage",
        "002aca8a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059ffa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059ff30.md#insn-0059ffa8) · [`005a00a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059ff30.md#insn-005a00a0) · [`005a00d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059ff30.md#insn-005a00d0)
- 新版 `0059ffa8`（命令位置の公開資料なし） · `005a00a0`（命令位置の公開資料なし） · `005a00d0`（命令位置の公開資料なし）

~~~diff
- 0059ffa8 ["COPY", "tmp:0:8", ["const:855:8"]]
- 0059ffa8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0059ffa8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0059ffa8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0059ffa8 ["COPY", "tmp:0:8", ["const:85b:8"]]
+ 0059ffa8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0059ffa8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0059ffa8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0059ffa8 bytes 21542191
+ 0059ffa8 bytes 216c2191
- 005a00a0 ["COPY", "tmp:0:8", ["const:a8c:8"]]
- 005a00a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a00a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a00a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a00a0 ["COPY", "tmp:0:8", ["const:a83:8"]]
+ 005a00a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a00a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a00a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a00a0 bytes 29312a91
+ 005a00a0 bytes 290d2a91
- 005a00d0 ["COPY", "tmp:0:8", ["const:855:8"]]
- 005a00d0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005a00d0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005a00d0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005a00d0 ["COPY", "tmp:0:8", ["const:85b:8"]]
+ 005a00d0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005a00d0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005a00d0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005a00d0 bytes 42542191
+ 005a00d0 bytes 426c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3635ce702a635e5a19de3f963784a632"></a>

### [`005a02e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a0/005a02e8.md) → [`005a02e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a0/005a02e8.md) FUN_005a02e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005a33f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a3/005a33f8.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00446df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446df4.md) [`00447378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447378.md)
- 新版 呼出元 1件 [`005a33f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a33f8.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446df4.md) [`00447378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447378.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a05c8",
      "incomplete_value": true,
      "site": "005a05e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "005a05c8",
      "incomplete_value": true,
      "site": "005a05e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9b8:8"
              ]
            ]
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
      "definition_site": "005a05d0",
      "incomplete_value": false,
      "site": "005a05e0",
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
      "definition_site": "005a05d0",
      "incomplete_value": false,
      "site": "005a05e0",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a05d8",
      "incomplete_value": false,
      "site": "005a05e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a05d8",
      "incomplete_value": false,
      "site": "005a05e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a05c8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "005a05d0",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005a05d8",
      "PARAM",
      [
        "storage",
        "00bf3c98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005a05c8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "005a05d0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005a05d8",
      "PARAM",
      [
        "storage",
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a05c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a0/005a02e8.md#insn-005a05c8) · [`005a05d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a0/005a02e8.md#insn-005a05d0) · [`005a05d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a0/005a02e8.md#insn-005a05d4)
- 新版 `005a05c8`（命令位置の公開資料なし） · `005a05d0`（命令位置の公開資料なし）

~~~diff
- 005a05c8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:9b8:8"]]
- 005a05c8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a05c8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:a78:8"]]
+ 005a05c8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005a05c8 bytes 60df44f9
+ 005a05c8 bytes 603f45f9
- 005a05d0 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 005a05d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005a05d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005a05d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005a05d0 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 005a05d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005a05d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005a05d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005a05d0 bytes 21603691
+ 005a05d0 bytes 21203991
- 005a05d4 ["COPY", "register:4010:8", ["const:bf3000:8"]]
- 005a05d4 bytes 823200f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36d81a0de633d869040238c3da930d17"></a>

### [`005a1ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a1/005a1ae4.md) → [`005a1ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a1/005a1ae4.md) FUN_005a1ae4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`005d996c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005eb/005eb040.md) [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) [`009e9518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009e9/009e9518.md) · 呼出先 2件 [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 8件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005eb/005eb040.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`009e9518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009e9/009e9518.md) · 呼出先 2件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "005a1b0c",
      "incomplete_value": true,
      "site": "005a1b0c",
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
      "definition_site": "005a1b0c",
      "incomplete_value": true,
      "site": "005a1b0c",
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
      "005a1b04",
      "READ",
      [
        "storage",
        "00c1b470",
        null,
        "pointer"
      ]
    ],
    [
      "005a1b0c",
      "DATA",
      [
        "storage",
        "00c0bc38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1b04",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "005a1b0c",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1b04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a1/005a1ae4.md#insn-005a1b04)
- 新版 `005a1b04`（命令位置の公開資料なし）

~~~diff
- 005a1b04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
- 005a1b04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a1b04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
+ 005a1b04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a1b04 bytes 083942f9
+ 005a1b04 bytes 089142f9
~~~


<a id="compare-4300e6f933b3236700cc5f50751516d1"></a>

### [`005a1b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a1/005a1b30.md) → [`005a1b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a1/005a1b30.md) FUN_005a1b30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005d996c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005eb/005eb040.md) [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 4件 [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 4件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`005eb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005eb/005eb040.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 4件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a1b98",
      "incomplete_value": true,
      "site": "005a1b98",
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
      "definition_site": "005a1b98",
      "incomplete_value": true,
      "site": "005a1b98",
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
      "005a1b58",
      "DATA",
      [
        "storage",
        "00c0bc90",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1b90",
      "READ",
      [
        "storage",
        "00c1b470",
        null,
        "pointer"
      ]
    ],
    [
      "005a1b98",
      "DATA",
      [
        "storage",
        "00c0bc38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1b58",
      "DATA",
      [
        "storage",
        "00c0bd40",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1b90",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "005a1b98",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a1/005a1b30.md#insn-005a1b4c) · [`005a1b90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a1/005a1b30.md#insn-005a1b90)
- 新版 `005a1b4c`（命令位置の公開資料なし） · `005a1b90`（命令位置の公開資料なし）

~~~diff
- 005a1b4c ["COPY", "tmp:0:8", ["const:c80:8"]]
- 005a1b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1b4c ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 005a1b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1b4c bytes 08013291
+ 005a1b4c bytes 08c13491
- 005a1b90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
- 005a1b90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a1b90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
+ 005a1b90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a1b90 bytes 083942f9
+ 005a1b90 bytes 089142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d637e452dfb52ac7bd4f72f54e81838f"></a>

### [`005a1c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a1/005a1c90.md) → [`005a1c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a1/005a1c90.md) FUN_005a1c90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0094f7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094f/0094f7d0.md) · 呼出先 23件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) · 呼出先 23件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a1e20",
      "incomplete_value": false,
      "site": "005a1e28",
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
      "definition_site": "005a1e20",
      "incomplete_value": false,
      "site": "005a1e28",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a1e50",
      "incomplete_value": true,
      "site": "005a1e50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1e50",
      "incomplete_value": true,
      "site": "005a1e50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:666:8"
              ]
            ]
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
      "definition_site": "005a1e54",
      "incomplete_value": true,
      "site": "005a1e54",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005a1e54",
      "incomplete_value": true,
      "site": "005a1e54",
      "value": [
        "LOAD",
        "8",
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
      "005a1e28",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1e3c",
      "READ",
      [
        "storage",
        "0029f666",
        null,
        "string"
      ]
    ],
    [
      "005a1e44",
      "READ",
      [
        "storage",
        "0029f66c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a1e28",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1e3c",
      "READ",
      [
        "storage",
        "0029f6f3",
        null,
        "string"
      ]
    ],
    [
      "005a1e44",
      "READ",
      [
        "storage",
        "0029f6f9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a1/005a1c90.md#insn-005a1e20) · [`005a1e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a1/005a1c90.md#insn-005a1e38) · [`005a2044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a1/005a1c90.md#insn-005a2044)
- 新版 `005a1e20`（命令位置の公開資料なし） · `005a1e38`（命令位置の公開資料なし） · `005a2044`（命令位置の公開資料なし）

~~~diff
- 005a1e20 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 005a1e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1e20 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 005a1e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1e20 bytes 08e13191
+ 005a1e20 bytes 08a13491
- 005a1e38 ["COPY", "tmp:0:8", ["const:666:8"]]
- 005a1e38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a1e38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a1e38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a1e38 ["COPY", "tmp:0:8", ["const:6f3:8"]]
+ 005a1e38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1e38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1e38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a1e38 bytes 29991991
+ 005a1e38 bytes 29cd1b91
- 005a2044 ["COPY", "tmp:0:8", ["const:591:8"]]
- 005a2044 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a2044 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a2044 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a2044 ["COPY", "tmp:0:8", ["const:58a:8"]]
+ 005a2044 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a2044 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a2044 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a2044 bytes 29451691
+ 005a2044 bytes 29291691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57552de31aa74592dda3decea3ccb25b"></a>

### [`005a33f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a3/005a33f8.md) → [`005a33f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a3/005a33f8.md) FUN_005a33f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00963004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00963/00963004.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444edc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444edc.md) [`00445044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445044.md)
- 新版 呼出元 1件 [`00963004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00963/00963004.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444edc.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.39% / 新版 99.39%

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
      "definition_site": "005a3a3c",
      "incomplete_value": true,
      "site": "005a3a3c",
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
      "definition_site": "005a3a3c",
      "incomplete_value": true,
      "site": "005a3a3c",
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
    "ordinal": 21,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a3a44",
      "incomplete_value": false,
      "site": "005a3a54",
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
      "definition_site": "005a3a44",
      "incomplete_value": false,
      "site": "005a3a54",
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
    "ordinal": 70,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a3a4c",
      "incomplete_value": false,
      "site": "005a3a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a3a4c",
      "incomplete_value": false,
      "site": "005a3a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 70,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a38e8",
      "READ",
      [
        "storage",
        "00c1ac78",
        null,
        "pointer"
      ]
    ],
    [
      "005a39c4",
      "PARAM",
      [
        "storage",
        "00c24cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "005a3a38",
      "READ",
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
      "005a38e8",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "005a39c4",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "005a3a38",
      "READ",
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

- 旧版 [`005a38e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a3/005a33f8.md#insn-005a38e8) · [`005a3a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a3/005a33f8.md#insn-005a3a38) · [`005a3a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a3/005a33f8.md#insn-005a3a44)
- 新版 `005a38e8`（命令位置の公開資料なし） · `005a3a38`（命令位置の公開資料なし） · `005a3a44`（命令位置の公開資料なし）

~~~diff
- 005a38e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c78:8"]]
- 005a38e8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a38e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d28:8"]]
+ 005a38e8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 005a38e8 bytes b53e46f9
+ 005a38e8 bytes b59646f9
- 005a3a38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 005a3a38 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a3a38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 005a3a38 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005a3a38 bytes 00dd44f9
+ 005a3a38 bytes 003d45f9
- 005a3a44 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 005a3a44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005a3a44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005a3a44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005a3a44 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 005a3a44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005a3a44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005a3a44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005a3a44 bytes 21603691
+ 005a3a44 bytes 21203991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c98b389e71e3acb3867ac10c6fccbb0b"></a>

### [`005a45f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a4/005a45f4.md) → [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) FUN_005a45f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0094f7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) · 呼出先 68件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044abfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044abfc.md)
- 新版 呼出元 2件 [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 68件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abfc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 9件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5050",
      "incomplete_value": true,
      "site": "005a5060",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a93:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5050",
      "incomplete_value": true,
      "site": "005a5060",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a9c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 113,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5054",
      "incomplete_value": true,
      "site": "005a5064",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005a5054",
      "incomplete_value": true,
      "site": "005a5064",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 114,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5a38",
      "incomplete_value": false,
      "site": "005a5a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5a38",
      "incomplete_value": false,
      "site": "005a5a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "ordinal": 211,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a5050",
      "READ",
      [
        "storage",
        "002aca9c",
        null,
        "string"
      ]
    ],
    [
      "005a5054",
      "READ",
      [
        "storage",
        "002acaac",
        null,
        "string"
      ]
    ],
    [
      "005a5150",
      "PARAM",
      [
        "storage",
        "002ab855",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a5050",
      "READ",
      [
        "storage",
        "002aca93",
        null,
        "string"
      ]
    ],
    [
      "005a5054",
      "READ",
      [
        "storage",
        "002acaa3",
        null,
        "string"
      ]
    ],
    [
      "005a5150",
      "PARAM",
      [
        "storage",
        "002ab85b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a4/005a45f4.md#insn-005a5048) · [`005a5150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a4/005a45f4.md#insn-005a5150) · [`005a570c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a4/005a45f4.md#insn-005a570c)
- 新版 `005a5048`（命令位置の公開資料なし） · `005a5150`（命令位置の公開資料なし） · `005a570c`（命令位置の公開資料なし）

~~~diff
- 005a5048 ["COPY", "tmp:0:8", ["const:a9c:8"]]
- 005a5048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5048 ["COPY", "tmp:0:8", ["const:a93:8"]]
+ 005a5048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5048 bytes 08712a91
+ 005a5048 bytes 084d2a91
- 005a5150 ["COPY", "tmp:0:8", ["const:855:8"]]
- 005a5150 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 005a5150 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 005a5150 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 005a5150 ["COPY", "tmp:0:8", ["const:85b:8"]]
+ 005a5150 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 005a5150 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 005a5150 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 005a5150 bytes 42542191
+ 005a5150 bytes 426c2191
- 005a570c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:470:8"]]
- 005a570c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a570c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:520:8"]]
+ 005a570c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 005a570c bytes 183b42f9
+ 005a570c bytes 189342f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd8fe29dd1ed94450e734ed568fe82ef"></a>

### [`005a74e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a74e4.md) → [`005a74e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a74e4.md) FUN_005a74e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005a45f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a4/005a45f4.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 1件 [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.71% / 新版 86.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a7610",
      "incomplete_value": true,
      "site": "005a7620",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a61:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7610",
      "incomplete_value": true,
      "site": "005a7620",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9d4:8"
              ]
            ]
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
      "definition_site": "005a7624",
      "incomplete_value": true,
      "site": "005a7624",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005a7624",
      "incomplete_value": true,
      "site": "005a7624",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005a7764",
      "incomplete_value": false,
      "site": "005a7764",
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
      "definition_site": "005a7764",
      "incomplete_value": false,
      "site": "005a7764",
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
    "ordinal": 40,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a75c4",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "005a75d8",
      "READ",
      [
        "storage",
        "002ab85a",
        null,
        "string"
      ]
    ],
    [
      "005a7610",
      "READ",
      [
        "storage",
        "002929d4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a75c4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "005a75d8",
      "READ",
      [
        "storage",
        "002ab860",
        null,
        "string"
      ]
    ],
    [
      "005a7610",
      "READ",
      [
        "storage",
        "00292a61",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a75bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a74e4.md#insn-005a75bc) · [`005a75c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a74e4.md#insn-005a75c0) · [`005a75d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a74e4.md#insn-005a75d0)
- 新版 `005a75bc`（命令位置の公開資料なし） · `005a75c0`（命令位置の公開資料なし） · `005a75d0`（命令位置の公開資料なし）

~~~diff
- 005a75bc ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 005a75bc ["COPY", "register:4040:8", ["const:c25000:8"]]
- 005a75bc bytes e83300b0
+ 005a75bc bytes e83300d0
- 005a75c0 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 005a75c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a75c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a75c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a75c0 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 005a75c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a75c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a75c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a75c0 bytes 08e13d91
+ 005a75c0 bytes 08e10091
- 005a75d0 ["COPY", "tmp:0:8", ["const:85a:8"]]
- 005a75d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a75d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a75d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a75d0 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 005a75d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a75d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a75d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a75d0 bytes 29692191
+ 005a75d0 bytes 29812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b19234b88bbeb8d4cae0d083d370aee3"></a>

### [`005a7844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a7844.md) → [`005a7844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7844.md) FUN_005a7844

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005d996c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d9/005d996c.md) [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 4件 [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 2件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 4件 [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a78ac",
      "incomplete_value": true,
      "site": "005a78ac",
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
      "definition_site": "005a78ac",
      "incomplete_value": true,
      "site": "005a78ac",
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
      "005a786c",
      "DATA",
      [
        "storage",
        "00c0bc90",
        null,
        "undefined *"
      ]
    ],
    [
      "005a78a4",
      "READ",
      [
        "storage",
        "00c1b470",
        null,
        "pointer"
      ]
    ],
    [
      "005a78ac",
      "DATA",
      [
        "storage",
        "00c0bc38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a786c",
      "DATA",
      [
        "storage",
        "00c0bd40",
        null,
        "undefined *"
      ]
    ],
    [
      "005a78a4",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "005a78ac",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a7844.md#insn-005a7860) · [`005a78a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a7844.md#insn-005a78a4)
- 新版 `005a7860`（命令位置の公開資料なし） · `005a78a4`（命令位置の公開資料なし）

~~~diff
- 005a7860 ["COPY", "tmp:0:8", ["const:c80:8"]]
- 005a7860 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7860 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7860 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7860 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 005a7860 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7860 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7860 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7860 bytes 08013291
+ 005a7860 bytes 08c13491
- 005a78a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
- 005a78a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a78a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:520:8"]]
+ 005a78a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a78a4 bytes 083942f9
+ 005a78a4 bytes 089142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dd6ee916bbd4c43245760c91a5ebf6d"></a>

### [`005a7ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a7ff8.md) → [`005a7ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7ff8.md) FUN_005a7ff8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`006525c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00652/006525c0.md) [`00686590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00686/00686590.md) [`00695904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00695/00695904.md) [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) [`008f06a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f0/008f06a0.md) · 呼出先 16件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 7件 [`006525c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00652/006525c0.md) [`00686590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00686/00686590.md) [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) [`008f06a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f0/008f06a0.md) · 呼出先 16件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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
      "definition_site": "005a80e8",
      "incomplete_value": true,
      "site": "005a80e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "005a80e8",
      "incomplete_value": true,
      "site": "005a80e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e0:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a814c",
      "incomplete_value": false,
      "site": "005a814c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a814c",
      "incomplete_value": false,
      "site": "005a814c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf4000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a8104",
      "incomplete_value": false,
      "site": "005a8114",
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
            "const:ac6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8104",
      "incomplete_value": false,
      "site": "005a8114",
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
            "const:a39:8"
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
      "005a8070",
      "READ",
      [
        "storage",
        "002a9796",
        null,
        "string"
      ]
    ],
    [
      "005a8074",
      "READ",
      [
        "storage",
        "002a97a0",
        null,
        "string"
      ]
    ],
    [
      "005a80d8",
      "READ",
      [
        "storage",
        "002a46e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a8070",
      "READ",
      [
        "storage",
        "002a978d",
        null,
        "string"
      ]
    ],
    [
      "005a8074",
      "READ",
      [
        "storage",
        "002a9797",
        null,
        "string"
      ]
    ],
    [
      "005a80d8",
      "READ",
      [
        "storage",
        "002a46d9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a7ff8.md#insn-005a8068) · [`005a80d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a7ff8.md#insn-005a80d4) · [`005a8104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a7ff8.md#insn-005a8104)
- 新版 `005a8068`（命令位置の公開資料なし） · `005a80d4`（命令位置の公開資料なし） · `005a8104`（命令位置の公開資料なし）

~~~diff
- 005a8068 ["COPY", "tmp:0:8", ["const:796:8"]]
- 005a8068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a8068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a8068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a8068 ["COPY", "tmp:0:8", ["const:78d:8"]]
+ 005a8068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a8068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a8068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a8068 bytes 08591e91
+ 005a8068 bytes 08351e91
- 005a80d4 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 005a80d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a80d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a80d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a80d4 ["COPY", "tmp:0:8", ["const:6d9:8"]]
+ 005a80d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a80d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a80d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a80d4 bytes 08811b91
+ 005a80d4 bytes 08651b91
- 005a8104 ["COPY", "tmp:0:8", ["const:a39:8"]]
- 005a8104 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005a8104 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005a8104 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005a8104 ["COPY", "tmp:0:8", ["const:ac6:8"]]
+ 005a8104 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005a8104 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005a8104 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005a8104 bytes 21e42891
+ 005a8104 bytes 21182b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fa1edf3e99fc8867b1ba4d98a093351"></a>

### [`005a83e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a83e4.md) → [`005a83e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md) FUN_005a83e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 48件 [`005a7ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a7ff8.md) [`005b6778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b6/005b6778.md) [`005e1a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e1/005e1a5c.md) [`005e53dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e5/005e53dc.md) [`005e8d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e8/005e8d4c.md) · 呼出先 14件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00470ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470ef0.md) [`005a8954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8954.md) [`005b0f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0f54.md)
- 新版 呼出元 48件 [`005a7ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7ff8.md) [`005b6778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b6/005b6778.md) [`005e1a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e1/005e1a5c.md) [`005e53dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e5/005e53dc.md) [`005e8d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e8/005e8d4c.md) · 呼出先 14件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00470ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470ef0.md) [`005a8954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8954.md) [`005b0f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0f54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.57% / 新版 99.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a841c",
      "incomplete_value": false,
      "site": "005a8430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:dcb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a841c",
      "incomplete_value": false,
      "site": "005a8430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:297000:8"
          ],
          [
            "leaf",
            "const:d3e:8"
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
      "005a841c",
      "PARAM",
      [
        "storage",
        "00297d3e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a841c",
      "PARAM",
      [
        "storage",
        "00297dcb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a841c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a83e4.md#insn-005a841c)
- 新版 `005a841c`（命令位置の公開資料なし）

~~~diff
- 005a841c ["COPY", "tmp:0:8", ["const:d3e:8"]]
- 005a841c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005a841c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005a841c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005a841c ["COPY", "tmp:0:8", ["const:dcb:8"]]
+ 005a841c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005a841c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005a841c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005a841c bytes 21f83491
+ 005a841c bytes 212c3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cde090d7dd5d60e4bafa319a1a86d4d"></a>

### [`005a8954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8954.md) → [`005a8954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8954.md) FUN_005a8954

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a83e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a83e4.md) [`00859898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859898.md) · 呼出先 8件 [`005a8a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8a5c.md) [`005a8aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8aac.md) [`005a8df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8df0.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`005a83e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md) [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) · 呼出先 8件 [`005a8a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8a5c.md) [`005a8aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8aac.md) [`005a8df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8df0.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a897c",
      "incomplete_value": true,
      "site": "005a8980",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "005a897c",
      "incomplete_value": true,
      "site": "005a8980",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d40:8"
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
      "definition_site": "005a8990",
      "incomplete_value": true,
      "site": "005a8994",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:530:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8990",
      "incomplete_value": true,
      "site": "005a8994",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:480:8"
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
      "005a897c",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "005a897c",
      "PARAM",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005a8990",
      "READ",
      [
        "storage",
        "00c1b480",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a897c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "005a897c",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005a8990",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a897c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8954.md#insn-005a897c) · [`005a8990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8954.md#insn-005a8990)
- 新版 `005a897c`（命令位置の公開資料なし） · `005a8990`（命令位置の公開資料なし）

~~~diff
- 005a897c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d40:8"]]
- 005a897c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a897c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
+ 005a897c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005a897c bytes 21a046f9
+ 005a897c bytes 21f846f9
- 005a8990 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:480:8"]]
- 005a8990 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8990 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:530:8"]]
+ 005a8990 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005a8990 bytes 214042f9
+ 005a8990 bytes 219842f9
~~~


<a id="compare-96b650a0dfa4836d925a276a0250e5ce"></a>

### [`005a8aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8aac.md) → [`005a8aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8aac.md) FUN_005a8aac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005a8954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8954.md) [`005a98f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a98f4.md) · 呼出先 11件 [`005a8ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8ff4.md) [`005a9180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9180.md) [`005a92f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a92f4.md) [`005a94a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a94a8.md) [`005a965c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a965c.md)
- 新版 呼出元 2件 [`005a8954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8954.md) [`005a98f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a98f4.md) · 呼出先 11件 [`005a8ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8ff4.md) [`005a9180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9180.md) [`005a92f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a92f4.md) [`005a94a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a94a8.md) [`005a965c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a965c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a8ae8",
      "incomplete_value": true,
      "site": "005a8aec",
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
      "definition_site": "005a8ae8",
      "incomplete_value": true,
      "site": "005a8aec",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a8b08",
      "incomplete_value": true,
      "site": "005a8b08",
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
      "definition_site": "005a8b08",
      "incomplete_value": true,
      "site": "005a8b08",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a8dbc",
      "incomplete_value": true,
      "site": "005a8dc0",
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
      "definition_site": "005a8dbc",
      "incomplete_value": true,
      "site": "005a8dc0",
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
    "ordinal": 43,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a8ae4",
      "READ",
      [
        "storage",
        "00c1b488",
        null,
        "pointer"
      ]
    ],
    [
      "005a8aec",
      "DATA",
      [
        "storage",
        "00bf3570",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005a8b00",
      "READ",
      [
        "storage",
        "00c1b490",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a8ae4",
      "READ",
      [
        "storage",
        "00c1b538",
        null,
        "pointer"
      ]
    ],
    [
      "005a8aec",
      "DATA",
      [
        "storage",
        "00bf3620",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005a8b00",
      "READ",
      [
        "storage",
        "00c1b540",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8aac.md#insn-005a8ae4) · [`005a8b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8aac.md#insn-005a8b00) · [`005a8b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8aac.md#insn-005a8b18)
- 新版 `005a8ae4`（命令位置の公開資料なし） · `005a8b00`（命令位置の公開資料なし） · `005a8b18`（命令位置の公開資料なし）

~~~diff
- 005a8ae4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:488:8"]]
- 005a8ae4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8ae4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:538:8"]]
+ 005a8ae4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a8ae4 bytes 084542f9
+ 005a8ae4 bytes 089d42f9
- 005a8b00 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:490:8"]]
- 005a8b00 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8b00 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:540:8"]]
+ 005a8b00 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 005a8b00 bytes 184b42f9
+ 005a8b00 bytes 18a342f9
- 005a8b18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:498:8"]]
- 005a8b18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8b18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:548:8"]]
+ 005a8b18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a8b18 bytes 084d42f9
+ 005a8b18 bytes 08a542f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81d57f69c376a9aa78910542162654a6"></a>

### [`005a8df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8df0.md) → [`005a8df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8df0.md) FUN_005a8df0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005a8954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8954.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 1件 [`005a8954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8954.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005a8e1c",
      "incomplete_value": true,
      "site": "005a8e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8e1c",
      "incomplete_value": true,
      "site": "005a8e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "005a8e20",
      "incomplete_value": true,
      "site": "005a8e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8e20",
      "incomplete_value": true,
      "site": "005a8e24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005a8e1c",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005a8e1c",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005a8e20",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a8e1c",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005a8e1c",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005a8e20",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8df0.md#insn-005a8e1c) · [`005a8e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8df0.md#insn-005a8e20)
- 新版 `005a8e1c`（命令位置の公開資料なし） · `005a8e20`（命令位置の公開資料なし）

~~~diff
- 005a8e1c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005a8e1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8e1c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005a8e1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005a8e1c bytes 215c42f9
+ 005a8e1c bytes 21b442f9
- 005a8e20 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005a8e20 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8e20 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005a8e20 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005a8e20 bytes 426042f9
+ 005a8e20 bytes 42b842f9
~~~


<a id="compare-9c4fc85b331b0c4e50adf369f017021c"></a>

### [`005a965c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a965c.md) → [`005a965c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a965c.md) FUN_005a965c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005a8aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8aac.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 1件 [`005a8aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8aac.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005a9688",
      "incomplete_value": true,
      "site": "005a9690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9688",
      "incomplete_value": true,
      "site": "005a9690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "005a968c",
      "incomplete_value": true,
      "site": "005a9690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a968c",
      "incomplete_value": true,
      "site": "005a9690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005a9688",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005a9688",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005a968c",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a9688",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005a9688",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005a968c",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a965c.md#insn-005a9688) · [`005a968c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a965c.md#insn-005a968c)
- 新版 `005a9688`（命令位置の公開資料なし） · `005a968c`（命令位置の公開資料なし）

~~~diff
- 005a9688 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005a9688 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9688 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005a9688 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9688 bytes 215c42f9
+ 005a9688 bytes 21b442f9
- 005a968c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005a968c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a968c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005a968c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005a968c bytes 426042f9
+ 005a968c bytes 42b842f9
~~~


<a id="compare-97c78e98146dbae0ec341eb208d54873"></a>

### [`005a98f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a98f4.md) → [`005a98f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a98f4.md) FUN_005a98f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005a97c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a97c0.md) [`005a9860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9860.md) · 呼出先 8件 [`005a8a0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8a0c.md) [`005a8aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8aac.md) [`005aa270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa270.md) [`005aa2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa2dc.md) [`005aa390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa390.md)
- 新版 呼出元 2件 [`005a97c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a97c0.md) [`005a9860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9860.md) · 呼出先 8件 [`005a8a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8a0c.md) [`005a8aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8aac.md) [`005aa270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa270.md) [`005aa2dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa2dc.md) [`005aa390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa390.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.59% / 新版 96.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a9b04",
      "incomplete_value": true,
      "site": "005a9b04",
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
      "definition_site": "005a9b04",
      "incomplete_value": true,
      "site": "005a9b04",
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
      "005a9a24",
      "READ",
      [
        "storage",
        "00c1b4c8",
        null,
        "pointer"
      ]
    ],
    [
      "005a9a50",
      "READ",
      [
        "storage",
        "00c1b4d0",
        null,
        "pointer"
      ]
    ],
    [
      "005a9a74",
      "DATA",
      [
        "storage",
        "00bf3708",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005a9a24",
      "READ",
      [
        "storage",
        "00c1b578",
        null,
        "pointer"
      ]
    ],
    [
      "005a9a50",
      "READ",
      [
        "storage",
        "00c1b580",
        null,
        "pointer"
      ]
    ],
    [
      "005a9a74",
      "DATA",
      [
        "storage",
        "00bf37b8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a98f4.md#insn-005a9a24) · [`005a9a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a98f4.md#insn-005a9a50) · [`005a9af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a98f4.md#insn-005a9af4)
- 新版 `005a9a24`（命令位置の公開資料なし） · `005a9a50`（命令位置の公開資料なし） · `005a9af4`（命令位置の公開資料なし）

~~~diff
- 005a9a24 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:4c8:8"]]
- 005a9a24 ["LOAD", "register:4058:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9a24 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:578:8"]]
+ 005a9a24 ["LOAD", "register:4058:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9a24 bytes 6b6542f9
+ 005a9a24 bytes 6bbd42f9
- 005a9a50 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:4d0:8"]]
- 005a9a50 ["LOAD", "register:4058:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9a50 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:580:8"]]
+ 005a9a50 ["LOAD", "register:4058:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9a50 bytes 6b6942f9
+ 005a9a50 bytes 6bc142f9
- 005a9af4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4e0:8"]]
- 005a9af4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9af4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:590:8"]]
+ 005a9af4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9af4 bytes 297142f9
+ 005a9af4 bytes 29c942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95342e6e5afe33b732592985d3d123de"></a>

### [`005a9c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9c58.md) → [`005a9c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9c58.md) FUN_005a9c58

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a97c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a97c0.md) [`005a9860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9860.md) · 呼出先 10件 [`005a8e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8e3c.md) [`005aa390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa390.md) [`005ab944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab944.md) [`005aba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005aba98.md) [`005abae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005abae4.md)
- 新版 呼出元 2件 [`005a97c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a97c0.md) [`005a9860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9860.md) · 呼出先 10件 [`005a8e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8e3c.md) [`005aa390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa390.md) [`005ab944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab944.md) [`005aba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005aba98.md) [`005abae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abae4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a9cb0",
      "incomplete_value": true,
      "site": "005a9cc0",
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
      "definition_site": "005a9cb0",
      "incomplete_value": true,
      "site": "005a9cc0",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a9e04",
      "incomplete_value": true,
      "site": "005a9e1c",
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
      "definition_site": "005a9e04",
      "incomplete_value": true,
      "site": "005a9e1c",
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
      "definition_site": "005a9eb0",
      "incomplete_value": true,
      "site": "005a9ec0",
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
      "definition_site": "005a9eb0",
      "incomplete_value": true,
      "site": "005a9ec0",
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
      "005a9ca8",
      "READ",
      [
        "storage",
        "00c1b4e8",
        null,
        "pointer"
      ]
    ],
    [
      "005a9cc0",
      "DATA",
      [
        "storage",
        "00bf37e0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005a9df0",
      "READ",
      [
        "storage",
        "00c1b4f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a9ca8",
      "READ",
      [
        "storage",
        "00c1b598",
        null,
        "pointer"
      ]
    ],
    [
      "005a9cc0",
      "DATA",
      [
        "storage",
        "00bf3890",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005a9df0",
      "READ",
      [
        "storage",
        "00c1b5a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9c58.md#insn-005a9ca8) · [`005a9df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9c58.md#insn-005a9df0) · [`005a9ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9c58.md#insn-005a9ea4)
- 新版 `005a9ca8`（命令位置の公開資料なし） · `005a9df0`（命令位置の公開資料なし） · `005a9ea4`（命令位置の公開資料なし）

~~~diff
- 005a9ca8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4e8:8"]]
- 005a9ca8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9ca8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:598:8"]]
+ 005a9ca8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9ca8 bytes 297542f9
+ 005a9ca8 bytes 29cd42f9
- 005a9df0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:4f0:8"]]
- 005a9df0 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9df0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:5a0:8"]]
+ 005a9df0 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9df0 bytes 4a7942f9
+ 005a9df0 bytes 4ad142f9
- 005a9ea4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4f8:8"]]
- 005a9ea4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a9ea4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5a8:8"]]
+ 005a9ea4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005a9ea4 bytes 297d42f9
+ 005a9ea4 bytes 29d542f9
~~~


<a id="compare-676dfad1d99f6e2ec8aaeaf33daf5efd"></a>

### [`005aa270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa270.md) → [`005aa270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa270.md) FUN_005aa270

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005a98f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a98f4.md) · 呼出先 2件 [`00bdb330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb330.md) [`00bdd850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd850.md)
- 新版 呼出元 1件 [`005a98f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a98f4.md) · 呼出先 2件 [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdd900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd900.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005aa28c",
      "incomplete_value": true,
      "site": "005aa290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "005aa28c",
      "incomplete_value": true,
      "site": "005aa290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d40:8"
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
      "definition_site": "005aa2a0",
      "incomplete_value": true,
      "site": "005aa2a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa2a0",
      "incomplete_value": true,
      "site": "005aa2a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "005aa28c",
      "READ",
      [
        "storage",
        "00c1ad40",
        null,
        "pointer"
      ]
    ],
    [
      "005aa28c",
      "PARAM",
      [
        "storage",
        "010a2a10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005aa2a0",
      "READ",
      [
        "storage",
        "00c1b480",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa28c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "005aa28c",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005aa2a0",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa28c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa270.md#insn-005aa28c) · [`005aa2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa270.md#insn-005aa2a0)
- 新版 `005aa28c`（命令位置の公開資料なし） · `005aa2a0`（命令位置の公開資料なし）

~~~diff
- 005aa28c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d40:8"]]
- 005aa28c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa28c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
+ 005aa28c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa28c bytes 21a046f9
+ 005aa28c bytes 21f846f9
- 005aa2a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:480:8"]]
- 005aa2a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa2a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:530:8"]]
+ 005aa2a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa2a0 bytes 214042f9
+ 005aa2a0 bytes 219842f9
~~~


<a id="compare-442b45874f988b743b42361a86b0fece"></a>

### [`005aa390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa390.md) → [`005aa390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa390.md) FUN_005aa390

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005a98f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a98f4.md) [`005a9c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9c58.md) [`005b04f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b04f0.md) [`005b0b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0b60.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 4件 [`005a98f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a98f4.md) [`005a9c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9c58.md) [`005b04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04f0.md) [`005b0b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0b60.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005aa3bc",
      "incomplete_value": true,
      "site": "005aa3c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa3bc",
      "incomplete_value": true,
      "site": "005aa3c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:4b8:8"
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
      "definition_site": "005aa3c0",
      "incomplete_value": true,
      "site": "005aa3c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa3c0",
      "incomplete_value": true,
      "site": "005aa3c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005aa3bc",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005aa3bc",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005aa3c0",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa3bc",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005aa3bc",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005aa3c0",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa3bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa390.md#insn-005aa3bc) · [`005aa3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa390.md#insn-005aa3c0)
- 新版 `005aa3bc`（命令位置の公開資料なし） · `005aa3c0`（命令位置の公開資料なし）

~~~diff
- 005aa3bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005aa3bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa3bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005aa3bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa3bc bytes 215c42f9
+ 005aa3bc bytes 21b442f9
- 005aa3c0 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005aa3c0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa3c0 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005aa3c0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa3c0 bytes 426042f9
+ 005aa3c0 bytes 42b842f9
~~~


<a id="compare-20c4ff64ce7d99669718d8c3195ee754"></a>

### [`005aa51c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa51c.md) → [`005aa51c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa51c.md) FUN_005aa51c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

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
      "definition_site": "005aa538",
      "incomplete_value": true,
      "site": "005aa538",
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
      "definition_site": "005aa538",
      "incomplete_value": true,
      "site": "005aa538",
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
      "005aa530",
      "READ",
      [
        "storage",
        "00c1b4e0",
        null,
        "pointer"
      ]
    ],
    [
      "005aa538",
      "DATA",
      [
        "storage",
        "00bf3750",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa544",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa530",
      "READ",
      [
        "storage",
        "00c1b590",
        null,
        "pointer"
      ]
    ],
    [
      "005aa538",
      "DATA",
      [
        "storage",
        "00bf3800",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa544",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa51c.md#insn-005aa530) · [`005aa544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa51c.md#insn-005aa544)
- 新版 `005aa530`（命令位置の公開資料なし） · `005aa544`（命令位置の公開資料なし）

~~~diff
- 005aa530 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
- 005aa530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa530 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:590:8"]]
+ 005aa530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa530 bytes 087142f9
+ 005aa530 bytes 08c942f9
- 005aa544 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005aa544 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa544 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005aa544 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa544 bytes 085942f9
+ 005aa544 bytes 08b142f9
~~~


<a id="compare-be93b90f7c601ef042be6a64055f1218"></a>

### [`005aa578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa578.md) → [`005aa578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa578.md) FUN_005aa578

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005aa594",
      "incomplete_value": true,
      "site": "005aa594",
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
      "definition_site": "005aa594",
      "incomplete_value": true,
      "site": "005aa594",
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
      "definition_site": "005aa5a8",
      "incomplete_value": true,
      "site": "005aa5ac",
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
      "definition_site": "005aa5a8",
      "incomplete_value": true,
      "site": "005aa5ac",
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
      "005aa58c",
      "READ",
      [
        "storage",
        "00c1b4e0",
        null,
        "pointer"
      ]
    ],
    [
      "005aa594",
      "DATA",
      [
        "storage",
        "00bf3750",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa5a0",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa58c",
      "READ",
      [
        "storage",
        "00c1b590",
        null,
        "pointer"
      ]
    ],
    [
      "005aa594",
      "DATA",
      [
        "storage",
        "00bf3800",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa5a0",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa58c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa578.md#insn-005aa58c) · [`005aa5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa578.md#insn-005aa5a0)
- 新版 `005aa58c`（命令位置の公開資料なし） · `005aa5a0`（命令位置の公開資料なし）

~~~diff
- 005aa58c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
- 005aa58c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa58c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:590:8"]]
+ 005aa58c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa58c bytes 087142f9
+ 005aa58c bytes 08c942f9
- 005aa5a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005aa5a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa5a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005aa5a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa5a0 bytes 085942f9
+ 005aa5a0 bytes 08b142f9
~~~


<a id="compare-7c9edd41b9898e0ac672d5df56915965"></a>

### [`005aa6e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa6e0.md) → [`005aa6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa6e0.md) FUN_005aa6e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "definition_site": "005aa6fc",
      "incomplete_value": true,
      "site": "005aa700",
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
      "definition_site": "005aa6fc",
      "incomplete_value": true,
      "site": "005aa700",
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
      "definition_site": "005aa744",
      "incomplete_value": true,
      "site": "005aa748",
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
      "definition_site": "005aa744",
      "incomplete_value": true,
      "site": "005aa748",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005aa6f4",
      "READ",
      [
        "storage",
        "00c1b500",
        null,
        "pointer"
      ]
    ],
    [
      "005aa700",
      "DATA",
      [
        "storage",
        "00bf3798",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa73c",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa6f4",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "005aa700",
      "DATA",
      [
        "storage",
        "00bf3848",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa73c",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa6f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa6e0.md#insn-005aa6f4) · [`005aa73c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa6e0.md#insn-005aa73c)
- 新版 `005aa6f4`（命令位置の公開資料なし） · `005aa73c`（命令位置の公開資料なし）

~~~diff
- 005aa6f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
- 005aa6f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa6f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005aa6f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa6f4 bytes 088142f9
+ 005aa6f4 bytes 08d942f9
- 005aa73c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005aa73c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa73c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005aa73c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa73c bytes 085942f9
+ 005aa73c bytes 08b142f9
~~~


<a id="compare-9abbfa8e066335e992dbf597a2a6154f"></a>

### [`005aa770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa770.md) → [`005aa770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa770.md) FUN_005aa770

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

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
      "definition_site": "005aa78c",
      "incomplete_value": true,
      "site": "005aa790",
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
      "definition_site": "005aa78c",
      "incomplete_value": true,
      "site": "005aa790",
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
      "definition_site": "005aa7d4",
      "incomplete_value": true,
      "site": "005aa7d8",
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
      "definition_site": "005aa7d4",
      "incomplete_value": true,
      "site": "005aa7d8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005aa784",
      "READ",
      [
        "storage",
        "00c1b500",
        null,
        "pointer"
      ]
    ],
    [
      "005aa790",
      "DATA",
      [
        "storage",
        "00bf3798",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa7cc",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aa784",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "005aa790",
      "DATA",
      [
        "storage",
        "00bf3848",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005aa7cc",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa770.md#insn-005aa784) · [`005aa7cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa770.md#insn-005aa7cc)
- 新版 `005aa784`（命令位置の公開資料なし） · `005aa7cc`（命令位置の公開資料なし）

~~~diff
- 005aa784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
- 005aa784 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5b0:8"]]
+ 005aa784 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa784 bytes 088142f9
+ 005aa784 bytes 08d942f9
- 005aa7cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005aa7cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aa7cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005aa7cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005aa7cc bytes 085942f9
+ 005aa7cc bytes 08b142f9
~~~


<a id="compare-c426bc2771c6032bc8f2d4d61138666c"></a>

### [`005aaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aaff0.md) → [`005aaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aaff0.md) FUN_005aaff0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005aae28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aae28.md) [`005ab094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab094.md) [`005ab678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab678.md) [`005b3380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3380.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 4件 [`005aae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aae28.md) [`005ab094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab094.md) [`005ab678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab678.md) [`005b3380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3380.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "005aaffc",
      "incomplete_value": false,
      "site": "005ab000",
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
      "definition_site": "005aaffc",
      "incomplete_value": false,
      "site": "005ab000",
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
      "005aaffc",
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
      "005aaffc",
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

- 旧版 [`005aaffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aaff0.md#insn-005aaffc)
- 新版 `005aaffc`（命令位置の公開資料なし）

~~~diff
- 005aaffc ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005aaffc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005aaffc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005aaffc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005aaffc ["COPY", "tmp:0:8", ["const:303:8"]]
+ 005aaffc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005aaffc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005aaffc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005aaffc bytes 00280c91
+ 005aaffc bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ecc7868bec4fc5ceecaf82ed4881cd0"></a>

### [`005ab048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab048.md) → [`005ab048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab048.md) FUN_005ab048

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005aa9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa9b4.md) [`005b1404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b1/005b1404.md) [`005b1ce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b1/005b1ce4.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 3件 [`005aa9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa9b4.md) [`005b1404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b1/005b1404.md) [`005b1ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b1/005b1ce4.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005ab074",
      "incomplete_value": true,
      "site": "005ab07c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab074",
      "incomplete_value": true,
      "site": "005ab07c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:4b8:8"
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
      "definition_site": "005ab078",
      "incomplete_value": true,
      "site": "005ab07c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab078",
      "incomplete_value": true,
      "site": "005ab07c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:4c0:8"
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
      "005ab074",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005ab074",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ab078",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ab074",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005ab074",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ab078",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab048.md#insn-005ab074) · [`005ab078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab048.md#insn-005ab078)
- 新版 `005ab074`（命令位置の公開資料なし） · `005ab078`（命令位置の公開資料なし）

~~~diff
- 005ab074 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005ab074 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ab074 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005ab074 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005ab074 bytes 215c42f9
+ 005ab074 bytes 21b442f9
- 005ab078 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005ab078 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ab078 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005ab078 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005ab078 bytes 426042f9
+ 005ab078 bytes 42b842f9
~~~


<a id="compare-98280595939b17b00dd15192c1eb61c3"></a>

### [`005ab20c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab20c.md) → [`005ab20c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab20c.md) FUN_005ab20c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005aa9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa9b4.md) [`005b1404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b1/005b1404.md) [`005b1ce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b1/005b1ce4.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 3件 [`005aa9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa9b4.md) [`005b1404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b1/005b1404.md) [`005b1ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b1/005b1ce4.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005ab23c",
      "incomplete_value": true,
      "site": "005ab240",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab23c",
      "incomplete_value": true,
      "site": "005ab240",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:4c0:8"
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
      "005ab238",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005ab238",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ab23c",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ab238",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005ab238",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ab23c",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab20c.md#insn-005ab238) · [`005ab23c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab20c.md#insn-005ab23c)
- 新版 `005ab238`（命令位置の公開資料なし） · `005ab23c`（命令位置の公開資料なし）

~~~diff
- 005ab238 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005ab238 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ab238 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005ab238 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005ab238 bytes 215c42f9
+ 005ab238 bytes 21b442f9
- 005ab23c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005ab23c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ab23c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005ab23c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005ab23c bytes 426042f9
+ 005ab23c bytes 42b842f9
~~~


<a id="compare-82f391aec5cf4b20868f63bb2e696351"></a>

### [`005ab664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab664.md) → [`005ab664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab664.md) FUN_005ab664

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005ab2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab2e0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005ab2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab2e0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "005ab670",
      "incomplete_value": false,
      "site": "005ab674",
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
      "definition_site": "005ab670",
      "incomplete_value": false,
      "site": "005ab674",
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
      "005ab670",
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
      "005ab670",
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

- 旧版 [`005ab670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab664.md#insn-005ab670)
- 新版 `005ab670`（命令位置の公開資料なし）

~~~diff
- 005ab670 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005ab670 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005ab670 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005ab670 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005ab670 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 005ab670 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005ab670 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005ab670 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005ab670 bytes 00280c91
+ 005ab670 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83072b0a505b9f3b647d489da3a679b4"></a>

### [`005ab930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab930.md) → [`005ab930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab930.md) FUN_005ab930

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005ab094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab094.md) [`005ab804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab804.md) [`005b356c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b356c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`005ab094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab094.md) [`005ab804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab804.md) [`005b356c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b356c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "005ab93c",
      "incomplete_value": false,
      "site": "005ab940",
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
      "definition_site": "005ab93c",
      "incomplete_value": false,
      "site": "005ab940",
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
      "005ab93c",
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
      "005ab93c",
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

- 旧版 [`005ab93c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab930.md#insn-005ab93c)
- 新版 `005ab93c`（命令位置の公開資料なし）

~~~diff
- 005ab93c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005ab93c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005ab93c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005ab93c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005ab93c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 005ab93c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005ab93c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005ab93c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005ab93c bytes 00280c91
+ 005ab93c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6d7ff050a6d5f5e218051ae676b03b4"></a>

### [`005aba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005aba98.md) → [`005aba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005aba98.md) FUN_005aba98

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005a9c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9c58.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 1件 [`005a9c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9c58.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005abac4",
      "incomplete_value": true,
      "site": "005abacc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005abac4",
      "incomplete_value": true,
      "site": "005abacc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:4b8:8"
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
      "definition_site": "005abac8",
      "incomplete_value": true,
      "site": "005abacc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005abac8",
      "incomplete_value": true,
      "site": "005abacc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005abac4",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005abac4",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005abac8",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005abac4",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005abac4",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005abac8",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005abac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005aba98.md#insn-005abac4) · [`005abac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005aba98.md#insn-005abac8)
- 新版 `005abac4`（命令位置の公開資料なし） · `005abac8`（命令位置の公開資料なし）

~~~diff
- 005abac4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005abac4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005abac4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005abac4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005abac4 bytes 215c42f9
+ 005abac4 bytes 21b442f9
- 005abac8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005abac8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005abac8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005abac8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005abac8 bytes 426042f9
+ 005abac8 bytes 42b842f9
~~~


<a id="compare-e6bcd1edee78d600d28355ba6ed6c3ee"></a>

### [`005abb94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005abb94.md) → [`005abb94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abb94.md) FUN_005abb94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005a9c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9c58.md) [`005abeac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005abeac.md) [`005ae770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ae/005ae770.md) [`005ae894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ae/005ae894.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 4件 [`005a9c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9c58.md) [`005abeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abeac.md) [`005ae770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae770.md) [`005ae894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae894.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005abbc0",
      "incomplete_value": true,
      "site": "005abbc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005abbc0",
      "incomplete_value": true,
      "site": "005abbc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "005abbc4",
      "incomplete_value": true,
      "site": "005abbc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005abbc4",
      "incomplete_value": true,
      "site": "005abbc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005abbc0",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005abbc0",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005abbc4",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005abbc0",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005abbc0",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005abbc4",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005abbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005abb94.md#insn-005abbc0) · [`005abbc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005abb94.md#insn-005abbc4)
- 新版 `005abbc0`（命令位置の公開資料なし） · `005abbc4`（命令位置の公開資料なし）

~~~diff
- 005abbc0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005abbc0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005abbc0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005abbc0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005abbc0 bytes 215c42f9
+ 005abbc0 bytes 21b442f9
- 005abbc4 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005abbc4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005abbc4 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005abbc4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005abbc4 bytes 426042f9
+ 005abbc4 bytes 42b842f9
~~~


<a id="compare-834b618c013254e4d010d4933edf4672"></a>

### [`005ac1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac1ac.md) → [`005ac1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac1ac.md) FUN_005ac1ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`005abae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005abae4.md) [`005abbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005abbe0.md) [`005abeac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005abeac.md) [`005ae894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ae/005ae894.md) [`005b093c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b093c.md) · 呼出先 2件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md)
- 新版 呼出元 7件 [`005abae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abae4.md) [`005abbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abbe0.md) [`005abeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abeac.md) [`005ae894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae894.md) [`005b093c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b093c.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ac1f0",
      "incomplete_value": true,
      "site": "005ac1f0",
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
      "definition_site": "005ac1f0",
      "incomplete_value": true,
      "site": "005ac1f0",
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
      "definition_site": "005ac220",
      "incomplete_value": true,
      "site": "005ac220",
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
      "definition_site": "005ac220",
      "incomplete_value": true,
      "site": "005ac220",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ac274",
      "incomplete_value": true,
      "site": "005ac274",
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
      "definition_site": "005ac274",
      "incomplete_value": true,
      "site": "005ac274",
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
      "005ac1e0",
      "READ",
      [
        "storage",
        "00c1b508",
        null,
        "pointer"
      ]
    ],
    [
      "005ac1f0",
      "DATA",
      [
        "storage",
        "00bf38b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac210",
      "READ",
      [
        "storage",
        "00c1b510",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac1e0",
      "READ",
      [
        "storage",
        "00c1b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "005ac1f0",
      "DATA",
      [
        "storage",
        "00bf3968",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac210",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac1ac.md#insn-005ac1e0) · [`005ac210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac1ac.md#insn-005ac210) · [`005ac264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac1ac.md#insn-005ac264)
- 新版 `005ac1e0`（命令位置の公開資料なし） · `005ac210`（命令位置の公開資料なし） · `005ac264`（命令位置の公開資料なし）

~~~diff
- 005ac1e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:508:8"]]
- 005ac1e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac1e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5b8:8"]]
+ 005ac1e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac1e0 bytes 298542f9
+ 005ac1e0 bytes 29dd42f9
- 005ac210 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:510:8"]]
- 005ac210 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac210 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5c0:8"]]
+ 005ac210 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac210 bytes 298942f9
+ 005ac210 bytes 29e142f9
- 005ac264 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:518:8"]]
- 005ac264 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac264 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5c8:8"]]
+ 005ac264 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac264 bytes 298d42f9
+ 005ac264 bytes 29e542f9
~~~


<a id="compare-364e9dd85ca59be6232e6f278fe2ad35"></a>

### [`005ac2ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac2ec.md) → [`005ac2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac2ec.md) FUN_005ac2ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005abbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005abbe0.md) [`005ac9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac9d8.md) [`005b04f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b04f0.md) [`005b0b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0b00.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 4件 [`005abbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abbe0.md) [`005ac9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac9d8.md) [`005b04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04f0.md) [`005b0b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0b00.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005ac318",
      "incomplete_value": true,
      "site": "005ac320",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac318",
      "incomplete_value": true,
      "site": "005ac320",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "005ac31c",
      "incomplete_value": true,
      "site": "005ac320",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac31c",
      "incomplete_value": true,
      "site": "005ac320",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005ac318",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005ac318",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ac31c",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac318",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005ac318",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ac31c",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac2ec.md#insn-005ac318) · [`005ac31c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac2ec.md#insn-005ac31c)
- 新版 `005ac318`（命令位置の公開資料なし） · `005ac31c`（命令位置の公開資料なし）

~~~diff
- 005ac318 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005ac318 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac318 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005ac318 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac318 bytes 215c42f9
+ 005ac318 bytes 21b442f9
- 005ac31c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005ac31c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac31c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005ac31c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac31c bytes 426042f9
+ 005ac31c bytes 42b842f9
~~~


<a id="compare-cda925c759f5240c2158b10239ecb127"></a>

### [`005ac400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac400.md) → [`005ac400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac400.md) FUN_005ac400

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005ac41c",
      "incomplete_value": true,
      "site": "005ac41c",
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
      "definition_site": "005ac41c",
      "incomplete_value": true,
      "site": "005ac41c",
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
      "definition_site": "005ac430",
      "incomplete_value": true,
      "site": "005ac434",
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
      "definition_site": "005ac430",
      "incomplete_value": true,
      "site": "005ac434",
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
      "005ac414",
      "READ",
      [
        "storage",
        "00c1b510",
        null,
        "pointer"
      ]
    ],
    [
      "005ac41c",
      "DATA",
      [
        "storage",
        "00bf3828",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac428",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac414",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ],
    [
      "005ac41c",
      "DATA",
      [
        "storage",
        "00bf38d8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac428",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac400.md#insn-005ac414) · [`005ac428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac400.md#insn-005ac428)
- 新版 `005ac414`（命令位置の公開資料なし） · `005ac428`（命令位置の公開資料なし）

~~~diff
- 005ac414 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:510:8"]]
- 005ac414 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac414 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c0:8"]]
+ 005ac414 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac414 bytes 088942f9
+ 005ac414 bytes 08e142f9
- 005ac428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005ac428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005ac428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac428 bytes 085942f9
+ 005ac428 bytes 08b142f9
~~~


<a id="compare-038ab3bef6552e2e5a40e1add76e38eb"></a>

### [`005ac45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac45c.md) → [`005ac45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac45c.md) FUN_005ac45c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005ac478",
      "incomplete_value": true,
      "site": "005ac478",
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
      "definition_site": "005ac478",
      "incomplete_value": true,
      "site": "005ac478",
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
      "definition_site": "005ac48c",
      "incomplete_value": true,
      "site": "005ac490",
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
      "definition_site": "005ac48c",
      "incomplete_value": true,
      "site": "005ac490",
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
      "005ac470",
      "READ",
      [
        "storage",
        "00c1b510",
        null,
        "pointer"
      ]
    ],
    [
      "005ac478",
      "DATA",
      [
        "storage",
        "00bf3828",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac484",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac470",
      "READ",
      [
        "storage",
        "00c1b5c0",
        null,
        "pointer"
      ]
    ],
    [
      "005ac478",
      "DATA",
      [
        "storage",
        "00bf38d8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac484",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac45c.md#insn-005ac470) · [`005ac484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac45c.md#insn-005ac484)
- 新版 `005ac470`（命令位置の公開資料なし） · `005ac484`（命令位置の公開資料なし）

~~~diff
- 005ac470 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:510:8"]]
- 005ac470 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac470 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c0:8"]]
+ 005ac470 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac470 bytes 088942f9
+ 005ac470 bytes 08e142f9
- 005ac484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005ac484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac484 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005ac484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac484 bytes 085942f9
+ 005ac484 bytes 08b142f9
~~~


<a id="compare-86f0ebbd61c0965af92620c274684500"></a>

### [`005ac52c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac52c.md) → [`005ac52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac52c.md) FUN_005ac52c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005ac548",
      "incomplete_value": true,
      "site": "005ac548",
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
      "definition_site": "005ac548",
      "incomplete_value": true,
      "site": "005ac548",
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
      "definition_site": "005ac55c",
      "incomplete_value": true,
      "site": "005ac560",
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
      "definition_site": "005ac55c",
      "incomplete_value": true,
      "site": "005ac560",
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
      "005ac540",
      "READ",
      [
        "storage",
        "00c1b518",
        null,
        "pointer"
      ]
    ],
    [
      "005ac548",
      "DATA",
      [
        "storage",
        "00bf3870",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac554",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac540",
      "READ",
      [
        "storage",
        "00c1b5c8",
        null,
        "pointer"
      ]
    ],
    [
      "005ac548",
      "DATA",
      [
        "storage",
        "00bf3920",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac554",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac52c.md#insn-005ac540) · [`005ac554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac52c.md#insn-005ac554)
- 新版 `005ac540`（命令位置の公開資料なし） · `005ac554`（命令位置の公開資料なし）

~~~diff
- 005ac540 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:518:8"]]
- 005ac540 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac540 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c8:8"]]
+ 005ac540 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac540 bytes 088d42f9
+ 005ac540 bytes 08e542f9
- 005ac554 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005ac554 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac554 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005ac554 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac554 bytes 085942f9
+ 005ac554 bytes 08b142f9
~~~


<a id="compare-f98e5c512ee20bc6c5880eb7cddd483d"></a>

### [`005ac588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac588.md) → [`005ac588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac588.md) FUN_005ac588

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005ac5a4",
      "incomplete_value": true,
      "site": "005ac5a4",
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
      "definition_site": "005ac5a4",
      "incomplete_value": true,
      "site": "005ac5a4",
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
      "definition_site": "005ac5b8",
      "incomplete_value": true,
      "site": "005ac5bc",
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
      "definition_site": "005ac5b8",
      "incomplete_value": true,
      "site": "005ac5bc",
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
      "005ac59c",
      "READ",
      [
        "storage",
        "00c1b518",
        null,
        "pointer"
      ]
    ],
    [
      "005ac5a4",
      "DATA",
      [
        "storage",
        "00bf3870",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac5b0",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac59c",
      "READ",
      [
        "storage",
        "00c1b5c8",
        null,
        "pointer"
      ]
    ],
    [
      "005ac5a4",
      "DATA",
      [
        "storage",
        "00bf3920",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac5b0",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac588.md#insn-005ac59c) · [`005ac5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac588.md#insn-005ac5b0)
- 新版 `005ac59c`（命令位置の公開資料なし） · `005ac5b0`（命令位置の公開資料なし）

~~~diff
- 005ac59c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:518:8"]]
- 005ac59c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac59c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5c8:8"]]
+ 005ac59c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac59c bytes 088d42f9
+ 005ac59c bytes 08e542f9
- 005ac5b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005ac5b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac5b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005ac5b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac5b0 bytes 085942f9
+ 005ac5b0 bytes 08b142f9
~~~


<a id="compare-63718329b6badad99b515d524e5cae52"></a>

### [`005ac6b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac6b8.md) → [`005ac6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac6b8.md) FUN_005ac6b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005ac6d4",
      "incomplete_value": true,
      "site": "005ac6d4",
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
      "definition_site": "005ac6d4",
      "incomplete_value": true,
      "site": "005ac6d4",
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
      "definition_site": "005ac6e8",
      "incomplete_value": true,
      "site": "005ac6ec",
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
      "definition_site": "005ac6e8",
      "incomplete_value": true,
      "site": "005ac6ec",
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
      "005ac6cc",
      "READ",
      [
        "storage",
        "00c1b528",
        null,
        "pointer"
      ]
    ],
    [
      "005ac6d4",
      "DATA",
      [
        "storage",
        "00bf3900",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac6e0",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac6cc",
      "READ",
      [
        "storage",
        "00c1b5d8",
        null,
        "pointer"
      ]
    ],
    [
      "005ac6d4",
      "DATA",
      [
        "storage",
        "00bf39b0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac6e0",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac6cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac6b8.md#insn-005ac6cc) · [`005ac6e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac6b8.md#insn-005ac6e0)
- 新版 `005ac6cc`（命令位置の公開資料なし） · `005ac6e0`（命令位置の公開資料なし）

~~~diff
- 005ac6cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:528:8"]]
- 005ac6cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac6cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5d8:8"]]
+ 005ac6cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac6cc bytes 089542f9
+ 005ac6cc bytes 08ed42f9
- 005ac6e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005ac6e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac6e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005ac6e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac6e0 bytes 085942f9
+ 005ac6e0 bytes 08b142f9
~~~


<a id="compare-77d32b18a5c9f2db38ed690affa61521"></a>

### [`005ac714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac714.md) → [`005ac714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac714.md) FUN_005ac714

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005ac730",
      "incomplete_value": true,
      "site": "005ac730",
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
      "definition_site": "005ac730",
      "incomplete_value": true,
      "site": "005ac730",
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
      "definition_site": "005ac744",
      "incomplete_value": true,
      "site": "005ac748",
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
      "definition_site": "005ac744",
      "incomplete_value": true,
      "site": "005ac748",
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
      "005ac728",
      "READ",
      [
        "storage",
        "00c1b528",
        null,
        "pointer"
      ]
    ],
    [
      "005ac730",
      "DATA",
      [
        "storage",
        "00bf3900",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac73c",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac728",
      "READ",
      [
        "storage",
        "00c1b5d8",
        null,
        "pointer"
      ]
    ],
    [
      "005ac730",
      "DATA",
      [
        "storage",
        "00bf39b0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac73c",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac714.md#insn-005ac728) · [`005ac73c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac714.md#insn-005ac73c)
- 新版 `005ac728`（命令位置の公開資料なし） · `005ac73c`（命令位置の公開資料なし）

~~~diff
- 005ac728 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:528:8"]]
- 005ac728 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac728 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5d8:8"]]
+ 005ac728 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac728 bytes 089542f9
+ 005ac728 bytes 08ed42f9
- 005ac73c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005ac73c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac73c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005ac73c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac73c bytes 085942f9
+ 005ac73c bytes 08b142f9
~~~


<a id="compare-a83e353d2e81df0006a64570f57db196"></a>

### [`005ac854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac854.md) → [`005ac854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac854.md) FUN_005ac854

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005ac870",
      "incomplete_value": true,
      "site": "005ac870",
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
      "definition_site": "005ac870",
      "incomplete_value": true,
      "site": "005ac870",
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
      "definition_site": "005ac884",
      "incomplete_value": true,
      "site": "005ac888",
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
      "definition_site": "005ac884",
      "incomplete_value": true,
      "site": "005ac888",
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
      "005ac868",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ],
    [
      "005ac870",
      "DATA",
      [
        "storage",
        "00bf3948",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac87c",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac868",
      "READ",
      [
        "storage",
        "00c1b5e0",
        null,
        "pointer"
      ]
    ],
    [
      "005ac870",
      "DATA",
      [
        "storage",
        "00bf39f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac87c",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac854.md#insn-005ac868) · [`005ac87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac854.md#insn-005ac87c)
- 新版 `005ac868`（命令位置の公開資料なし） · `005ac87c`（命令位置の公開資料なし）

~~~diff
- 005ac868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
- 005ac868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5e0:8"]]
+ 005ac868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac868 bytes 089942f9
+ 005ac868 bytes 08f142f9
- 005ac87c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005ac87c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac87c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005ac87c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac87c bytes 085942f9
+ 005ac87c bytes 08b142f9
~~~


<a id="compare-64329165a92a44840fe65f03cac82253"></a>

### [`005ac8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac8b0.md) → [`005ac8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac8b0.md) FUN_005ac8b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005ac8cc",
      "incomplete_value": true,
      "site": "005ac8cc",
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
      "definition_site": "005ac8cc",
      "incomplete_value": true,
      "site": "005ac8cc",
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
      "definition_site": "005ac8e0",
      "incomplete_value": true,
      "site": "005ac8e4",
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
      "definition_site": "005ac8e0",
      "incomplete_value": true,
      "site": "005ac8e4",
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
      "005ac8c4",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ],
    [
      "005ac8cc",
      "DATA",
      [
        "storage",
        "00bf3948",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac8d8",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ac8c4",
      "READ",
      [
        "storage",
        "00c1b5e0",
        null,
        "pointer"
      ]
    ],
    [
      "005ac8cc",
      "DATA",
      [
        "storage",
        "00bf39f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ac8d8",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac8b0.md#insn-005ac8c4) · [`005ac8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac8b0.md#insn-005ac8d8)
- 新版 `005ac8c4`（命令位置の公開資料なし） · `005ac8d8`（命令位置の公開資料なし）

~~~diff
- 005ac8c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
- 005ac8c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac8c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5e0:8"]]
+ 005ac8c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac8c4 bytes 089942f9
+ 005ac8c4 bytes 08f142f9
- 005ac8d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005ac8d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ac8d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005ac8d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ac8d8 bytes 085942f9
+ 005ac8d8 bytes 08b142f9
~~~


<a id="compare-c1bd7de05302794760e3ecaa1d6c7d60"></a>

### [`005acbf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005acbf4.md) → [`005acbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005acbf4.md) FUN_005acbf4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005ab944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab944.md) [`005abca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005abca8.md) · 呼出先 5件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) [`00bdd8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8a0.md)
- 新版 呼出元 2件 [`005ab944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab944.md) [`005abca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005abca8.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00bdd950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd950.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005acc3c",
      "incomplete_value": true,
      "site": "005acc3c",
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
      "definition_site": "005acc3c",
      "incomplete_value": true,
      "site": "005acc3c",
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
      "005acc20",
      "READ",
      [
        "storage",
        "00c1b538",
        null,
        "pointer"
      ]
    ],
    [
      "005acc3c",
      "DATA",
      [
        "storage",
        "00bf39d8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005acc20",
      "READ",
      [
        "storage",
        "00c1b5e8",
        null,
        "pointer"
      ]
    ],
    [
      "005acc3c",
      "DATA",
      [
        "storage",
        "00bf3a88",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005acc20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005acbf4.md#insn-005acc20)
- 新版 `005acc20`（命令位置の公開資料なし）

~~~diff
- 005acc20 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:538:8"]]
- 005acc20 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005acc20 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5e8:8"]]
+ 005acc20 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005acc20 bytes 299d42f9
+ 005acc20 bytes 29f542f9
~~~


<a id="compare-84059cd7207897bbd6a8cd5418fc2941"></a>

### [`005ace3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ace3c.md) → [`005ace3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ace3c.md) FUN_005ace3c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005acf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005acf80.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 1件 [`005acf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005acf80.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

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
      "definition_site": "005ace5c",
      "incomplete_value": true,
      "site": "005ace60",
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
      "definition_site": "005ace5c",
      "incomplete_value": true,
      "site": "005ace60",
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
      "definition_site": "005acf4c",
      "incomplete_value": true,
      "site": "005acf50",
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
      "definition_site": "005acf4c",
      "incomplete_value": true,
      "site": "005acf50",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005ace54",
      "READ",
      [
        "storage",
        "00c1b538",
        null,
        "pointer"
      ]
    ],
    [
      "005ace60",
      "DATA",
      [
        "storage",
        "00bf39d8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005acf44",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ace54",
      "READ",
      [
        "storage",
        "00c1b5e8",
        null,
        "pointer"
      ]
    ],
    [
      "005ace60",
      "DATA",
      [
        "storage",
        "00bf3a88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005acf44",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ace54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ace3c.md#insn-005ace54) · [`005acf44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ace3c.md#insn-005acf44)
- 新版 `005ace54`（命令位置の公開資料なし） · `005acf44`（命令位置の公開資料なし）

~~~diff
- 005ace54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:538:8"]]
- 005ace54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005ace54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5e8:8"]]
+ 005ace54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005ace54 bytes 089d42f9
+ 005ace54 bytes 08f542f9
- 005acf44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005acf44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005acf44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005acf44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005acf44 bytes 085942f9
+ 005acf44 bytes 08b142f9
~~~


<a id="compare-82eb90c0e13e42660eb62c67d8928cc3"></a>

### [`005adeac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ad/005adeac.md) → [`005adeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ad/005adeac.md) FUN_005adeac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005ab944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005ab944.md) [`005adef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ad/005adef8.md) [`005ae3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ae/005ae3c8.md) [`005ae654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ae/005ae654.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 4件 [`005ab944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ab/005ab944.md) [`005adef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ad/005adef8.md) [`005ae3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae3c8.md) [`005ae654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae654.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005aded8",
      "incomplete_value": true,
      "site": "005adee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aded8",
      "incomplete_value": true,
      "site": "005adee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "005adedc",
      "incomplete_value": true,
      "site": "005adee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005adedc",
      "incomplete_value": true,
      "site": "005adee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005aded8",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005aded8",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005adedc",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005aded8",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005aded8",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005adedc",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aded8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ad/005adeac.md#insn-005aded8) · [`005adedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ad/005adeac.md#insn-005adedc)
- 新版 `005aded8`（命令位置の公開資料なし） · `005adedc`（命令位置の公開資料なし）

~~~diff
- 005aded8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005aded8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005aded8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005aded8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005aded8 bytes 215c42f9
+ 005aded8 bytes 21b442f9
- 005adedc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005adedc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005adedc ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005adedc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005adedc bytes 426042f9
+ 005adedc bytes 42b842f9
~~~


<a id="compare-a525db51734adc602caa12fdd3f819e5"></a>

### [`005af158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005af158.md) → [`005af158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005af158.md) FUN_005af158

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005ae3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ae/005ae3c8.md) [`005ae654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ae/005ae654.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 2件 [`005ae3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae3c8.md) [`005ae654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005ae654.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005af184",
      "incomplete_value": true,
      "site": "005af18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005af184",
      "incomplete_value": true,
      "site": "005af18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "005af188",
      "incomplete_value": true,
      "site": "005af18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005af188",
      "incomplete_value": true,
      "site": "005af18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005af184",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005af184",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005af188",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005af184",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005af184",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005af188",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005af184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005af158.md#insn-005af184) · [`005af188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005af158.md#insn-005af188)
- 新版 `005af184`（命令位置の公開資料なし） · `005af188`（命令位置の公開資料なし）

~~~diff
- 005af184 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005af184 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005af184 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005af184 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005af184 bytes 215c42f9
+ 005af184 bytes 21b442f9
- 005af188 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005af188 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005af188 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005af188 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005af188 bytes 426042f9
+ 005af188 bytes 42b842f9
~~~


<a id="compare-2f1a67210fcc139bc925223f7d4c766f"></a>

### [`005af630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005af630.md) → [`005af630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005af630.md) FUN_005af630

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005adef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ad/005adef8.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 1件 [`005adef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ad/005adef8.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005af65c",
      "incomplete_value": true,
      "site": "005af664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005af65c",
      "incomplete_value": true,
      "site": "005af664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "005af660",
      "incomplete_value": true,
      "site": "005af664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005af660",
      "incomplete_value": true,
      "site": "005af664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005af65c",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005af65c",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005af660",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005af65c",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005af65c",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005af660",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005af65c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005af630.md#insn-005af65c) · [`005af660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005af630.md#insn-005af660)
- 新版 `005af65c`（命令位置の公開資料なし） · `005af660`（命令位置の公開資料なし）

~~~diff
- 005af65c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005af65c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005af65c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005af65c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005af65c bytes 215c42f9
+ 005af65c bytes 21b442f9
- 005af660 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005af660 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005af660 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005af660 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005af660 bytes 426042f9
+ 005af660 bytes 42b842f9
~~~


<a id="compare-e7619fad880ba8bd887711787e999898"></a>

### [`005afb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afb30.md) → [`005afb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afb30.md) FUN_005afb30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005aea7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ae/005aea7c.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 1件 [`005aea7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005aea7c.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005afb5c",
      "incomplete_value": true,
      "site": "005afb64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afb5c",
      "incomplete_value": true,
      "site": "005afb64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "005afb60",
      "incomplete_value": true,
      "site": "005afb64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afb60",
      "incomplete_value": true,
      "site": "005afb64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005afb5c",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005afb5c",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005afb60",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005afb5c",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005afb5c",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005afb60",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005afb5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afb30.md#insn-005afb5c) · [`005afb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afb30.md#insn-005afb60)
- 新版 `005afb5c`（命令位置の公開資料なし） · `005afb60`（命令位置の公開資料なし）

~~~diff
- 005afb5c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005afb5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afb5c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005afb5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005afb5c bytes 215c42f9
+ 005afb5c bytes 21b442f9
- 005afb60 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005afb60 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afb60 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005afb60 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005afb60 bytes 426042f9
+ 005afb60 bytes 42b842f9
~~~


<a id="compare-2140f3d13aa9bc7cf080e2cac44768b2"></a>

### [`005afd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afd1c.md) → [`005afd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afd1c.md) FUN_005afd1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005afb7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afb7c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005afb7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afb7c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "005afd28",
      "incomplete_value": false,
      "site": "005afd2c",
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
      "definition_site": "005afd28",
      "incomplete_value": false,
      "site": "005afd2c",
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
      "005afd28",
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
      "005afd28",
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

- 旧版 [`005afd28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afd1c.md#insn-005afd28)
- 新版 `005afd28`（命令位置の公開資料なし）

~~~diff
- 005afd28 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005afd28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005afd28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005afd28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005afd28 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 005afd28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005afd28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005afd28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005afd28 bytes 00280c91
+ 005afd28 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce0b23035f4c4c57b809abf468ebd57a"></a>

### [`005afd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afd30.md) → [`005afd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afd30.md) FUN_005afd30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005aef4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ae/005aef4c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005aef4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ae/005aef4c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "005afd3c",
      "incomplete_value": false,
      "site": "005afd40",
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
      "definition_site": "005afd3c",
      "incomplete_value": false,
      "site": "005afd40",
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
      "005afd3c",
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
      "005afd3c",
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

- 旧版 [`005afd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afd30.md#insn-005afd3c)
- 新版 `005afd3c`（命令位置の公開資料なし）

~~~diff
- 005afd3c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005afd3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005afd3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005afd3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005afd3c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 005afd3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005afd3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005afd3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005afd3c bytes 00280c91
+ 005afd3c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62b97b427e60508221c8910885ce67c1"></a>

### [`005afe3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afe3c.md) → [`005afe3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005afe3c.md) FUN_005afe3c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b06fc.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b06fc.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.16% / 新版 90.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005afe94",
      "incomplete_value": true,
      "site": "005afe94",
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
      "definition_site": "005afe94",
      "incomplete_value": true,
      "site": "005afe94",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005afec8",
      "incomplete_value": true,
      "site": "005afec8",
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
      "definition_site": "005afec8",
      "incomplete_value": true,
      "site": "005afec8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005afef8",
      "incomplete_value": true,
      "site": "005aff00",
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
      "definition_site": "005afef8",
      "incomplete_value": true,
      "site": "005aff00",
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
      "005afe88",
      "READ",
      [
        "storage",
        "00c1b490",
        null,
        "pointer"
      ]
    ],
    [
      "005afe94",
      "DATA",
      [
        "storage",
        "00bf3618",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005afeb0",
      "READ",
      [
        "storage",
        "00c1b540",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005afe88",
      "READ",
      [
        "storage",
        "00c1b540",
        null,
        "pointer"
      ]
    ],
    [
      "005afe94",
      "DATA",
      [
        "storage",
        "00bf36c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005afeb0",
      "READ",
      [
        "storage",
        "00c1b5f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005afe88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afe3c.md#insn-005afe88) · [`005afeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afe3c.md#insn-005afeb0) · [`005afee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005afe3c.md#insn-005afee8)
- 新版 `005afe88`（命令位置の公開資料なし） · `005afeb0`（命令位置の公開資料なし） · `005afee8`（命令位置の公開資料なし）

~~~diff
- 005afe88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:490:8"]]
- 005afe88 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afe88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:540:8"]]
+ 005afe88 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005afe88 bytes 294942f9
+ 005afe88 bytes 29a142f9
- 005afeb0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:540:8"]]
- 005afeb0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afeb0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5f0:8"]]
+ 005afeb0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005afeb0 bytes 29a142f9
+ 005afeb0 bytes 29f942f9
- 005afee8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:548:8"]]
- 005afee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afee8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5f8:8"]]
+ 005afee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005afee8 bytes 08a542f9
+ 005afee8 bytes 08fd42f9
~~~


<a id="compare-b63d9db1971d0fdf1f307dfc4deb9c5c"></a>

### [`005aff7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005aff7c.md) → [`005aff7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005aff7c.md) FUN_005aff7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b06fc.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b06fc.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005affa8",
      "incomplete_value": true,
      "site": "005affb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005affa8",
      "incomplete_value": true,
      "site": "005affb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "005affac",
      "incomplete_value": true,
      "site": "005affb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005affac",
      "incomplete_value": true,
      "site": "005affb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005affa8",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005affa8",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005affac",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005affa8",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005affa8",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005affac",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005affa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005aff7c.md#insn-005affa8) · [`005affac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005aff7c.md#insn-005affac)
- 新版 `005affa8`（命令位置の公開資料なし） · `005affac`（命令位置の公開資料なし）

~~~diff
- 005affa8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005affa8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005affa8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005affa8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005affa8 bytes 215c42f9
+ 005affa8 bytes 21b442f9
- 005affac ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005affac ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005affac ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005affac ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005affac bytes 426042f9
+ 005affac bytes 42b842f9
~~~


<a id="compare-ba8809309a636b3137cd5deb770a8969"></a>

### [`005affc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005affc8.md) → [`005affc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005affc8.md) FUN_005affc8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b06fc.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 2件 [`005a9f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9f10.md) [`005b06fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b06fc.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005afff4",
      "incomplete_value": true,
      "site": "005afffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afff4",
      "incomplete_value": true,
      "site": "005afffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "005afff8",
      "incomplete_value": true,
      "site": "005afffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005afff8",
      "incomplete_value": true,
      "site": "005afffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005afff4",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005afff4",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005afff8",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005afff4",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005afff4",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005afff8",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005afff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005affc8.md#insn-005afff4) · [`005afff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005affc8.md#insn-005afff8)
- 新版 `005afff4`（命令位置の公開資料なし） · `005afff8`（命令位置の公開資料なし）

~~~diff
- 005afff4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005afff4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afff4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005afff4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005afff4 bytes 215c42f9
+ 005afff4 bytes 21b442f9
- 005afff8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005afff8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005afff8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005afff8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005afff8 bytes 426042f9
+ 005afff8 bytes 42b842f9
~~~


<a id="compare-ec7b82e8eed46f43cf521c1d78adb454"></a>

### [`005b0014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0014.md) → [`005b0014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0014.md) FUN_005b0014

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

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
      "definition_site": "005b0030",
      "incomplete_value": true,
      "site": "005b0034",
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
      "definition_site": "005b0030",
      "incomplete_value": true,
      "site": "005b0034",
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
      "definition_site": "005b0054",
      "incomplete_value": true,
      "site": "005b0058",
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
      "definition_site": "005b0054",
      "incomplete_value": true,
      "site": "005b0058",
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
      "005b0028",
      "READ",
      [
        "storage",
        "00c1b550",
        null,
        "pointer"
      ]
    ],
    [
      "005b0034",
      "DATA",
      [
        "storage",
        "00bf3b10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b004c",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b0028",
      "READ",
      [
        "storage",
        "00c1b600",
        null,
        "pointer"
      ]
    ],
    [
      "005b0034",
      "DATA",
      [
        "storage",
        "00bf3bc0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b004c",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0014.md#insn-005b0028) · [`005b004c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0014.md#insn-005b004c)
- 新版 `005b0028`（命令位置の公開資料なし） · `005b004c`（命令位置の公開資料なし）

~~~diff
- 005b0028 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:550:8"]]
- 005b0028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0028 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
+ 005b0028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0028 bytes 08a942f9
+ 005b0028 bytes 080143f9
- 005b004c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005b004c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b004c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005b004c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b004c bytes 085942f9
+ 005b004c bytes 08b142f9
~~~


<a id="compare-85c9b9aece45a3278278e65e86f180c6"></a>

### [`005b0304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0304.md) → [`005b0304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0304.md) FUN_005b0304

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

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
      "definition_site": "005b0320",
      "incomplete_value": true,
      "site": "005b0324",
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
      "definition_site": "005b0320",
      "incomplete_value": true,
      "site": "005b0324",
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
      "definition_site": "005b0344",
      "incomplete_value": true,
      "site": "005b0348",
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
      "definition_site": "005b0344",
      "incomplete_value": true,
      "site": "005b0348",
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
      "005b0318",
      "READ",
      [
        "storage",
        "00c1b550",
        null,
        "pointer"
      ]
    ],
    [
      "005b0324",
      "DATA",
      [
        "storage",
        "00bf3b10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b033c",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b0318",
      "READ",
      [
        "storage",
        "00c1b600",
        null,
        "pointer"
      ]
    ],
    [
      "005b0324",
      "DATA",
      [
        "storage",
        "00bf3bc0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b033c",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0304.md#insn-005b0318) · [`005b033c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0304.md#insn-005b033c)
- 新版 `005b0318`（命令位置の公開資料なし） · `005b033c`（命令位置の公開資料なし）

~~~diff
- 005b0318 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:550:8"]]
- 005b0318 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0318 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
+ 005b0318 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0318 bytes 08a942f9
+ 005b0318 bytes 080143f9
- 005b033c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005b033c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b033c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005b033c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b033c bytes 085942f9
+ 005b033c bytes 08b142f9
~~~


<a id="compare-eb9210c6c20cb7921dca0f603d41e78e"></a>

### [`005b0384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0384.md) → [`005b0384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0384.md) FUN_005b0384

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "005b03a0",
      "incomplete_value": true,
      "site": "005b03a4",
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
      "definition_site": "005b03a0",
      "incomplete_value": true,
      "site": "005b03a4",
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
      "definition_site": "005b03c4",
      "incomplete_value": true,
      "site": "005b03c8",
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
      "definition_site": "005b03c4",
      "incomplete_value": true,
      "site": "005b03c8",
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
      "005b0398",
      "READ",
      [
        "storage",
        "00c1b550",
        null,
        "pointer"
      ]
    ],
    [
      "005b03a4",
      "DATA",
      [
        "storage",
        "00bf3b10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b03bc",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b0398",
      "READ",
      [
        "storage",
        "00c1b600",
        null,
        "pointer"
      ]
    ],
    [
      "005b03a4",
      "DATA",
      [
        "storage",
        "00bf3bc0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b03bc",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0384.md#insn-005b0398) · [`005b03bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0384.md#insn-005b03bc)
- 新版 `005b0398`（命令位置の公開資料なし） · `005b03bc`（命令位置の公開資料なし）

~~~diff
- 005b0398 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:550:8"]]
- 005b0398 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0398 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
+ 005b0398 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0398 bytes 08a942f9
+ 005b0398 bytes 080143f9
- 005b03bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005b03bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b03bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005b03bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b03bc bytes 085942f9
+ 005b03bc bytes 08b142f9
~~~


<a id="compare-4b1e66c7466429508773f93e4f8a52ba"></a>

### [`005b03f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b03f0.md) → [`005b03f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b03f0.md) FUN_005b03f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

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
      "definition_site": "005b040c",
      "incomplete_value": true,
      "site": "005b0410",
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
      "definition_site": "005b040c",
      "incomplete_value": true,
      "site": "005b0410",
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
      "definition_site": "005b0430",
      "incomplete_value": true,
      "site": "005b0434",
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
      "definition_site": "005b0430",
      "incomplete_value": true,
      "site": "005b0434",
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
      "005b0404",
      "READ",
      [
        "storage",
        "00c1b550",
        null,
        "pointer"
      ]
    ],
    [
      "005b0410",
      "DATA",
      [
        "storage",
        "00bf3b10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b0428",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b0404",
      "READ",
      [
        "storage",
        "00c1b600",
        null,
        "pointer"
      ]
    ],
    [
      "005b0410",
      "DATA",
      [
        "storage",
        "00bf3bc0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b0428",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b03f0.md#insn-005b0404) · [`005b0428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b03f0.md#insn-005b0428)
- 新版 `005b0404`（命令位置の公開資料なし） · `005b0428`（命令位置の公開資料なし）

~~~diff
- 005b0404 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:550:8"]]
- 005b0404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0404 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
+ 005b0404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0404 bytes 08a942f9
+ 005b0404 bytes 080143f9
- 005b0428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
- 005b0428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 005b0428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0428 bytes 085942f9
+ 005b0428 bytes 08b142f9
~~~


<a id="compare-b2306ea63f1343560be1e65ed313a5c9"></a>

### [`005b04a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b04a4.md) → [`005b04a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04a4.md) FUN_005b04a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a8ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8ff4.md) [`005a9180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a9/005a9180.md) · 呼出先 4件 [`00bba30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba30c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdd860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd860.md)
- 新版 呼出元 2件 [`005a8ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8ff4.md) [`005a9180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a9/005a9180.md) · 呼出先 4件 [`00bba3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba3d4.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdd910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd910.md)

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
      "definition_site": "005b04d0",
      "incomplete_value": true,
      "site": "005b04d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:568:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b04d0",
      "incomplete_value": true,
      "site": "005b04d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "005b04d4",
      "incomplete_value": true,
      "site": "005b04d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b04d4",
      "incomplete_value": true,
      "site": "005b04d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c0:8"
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
      "005b04d0",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005b04d0",
      "PARAM",
      [
        "storage",
        "00c16710",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005b04d4",
      "READ",
      [
        "storage",
        "00c1b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b04d0",
      "READ",
      [
        "storage",
        "00c1b568",
        null,
        "pointer"
      ]
    ],
    [
      "005b04d0",
      "PARAM",
      [
        "storage",
        "00c167c0",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005b04d4",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b04d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b04a4.md#insn-005b04d0) · [`005b04d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b04a4.md#insn-005b04d4)
- 新版 `005b04d0`（命令位置の公開資料なし） · `005b04d4`（命令位置の公開資料なし）

~~~diff
- 005b04d0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
- 005b04d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b04d0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:568:8"]]
+ 005b04d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 005b04d0 bytes 215c42f9
+ 005b04d0 bytes 21b442f9
- 005b04d4 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4c0:8"]]
- 005b04d4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b04d4 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:570:8"]]
+ 005b04d4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 005b04d4 bytes 426042f9
+ 005b04d4 bytes 42b842f9
~~~


<a id="compare-12ecee744aff7ebfa58cfe51e69ea950"></a>

### [`005b04f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b04f0.md) → [`005b04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04f0.md) FUN_005b04f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a8ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a8ff4.md) [`005b04f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b04f0.md) · 呼出先 7件 [`005aa390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005aa/005aa390.md) [`005ac2ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac2ec.md) [`005ac338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005ac338.md) [`005b04f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b04f0.md) [`005b06fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b06fc.md)
- 新版 呼出元 2件 [`005a8ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a8ff4.md) [`005b04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04f0.md) · 呼出先 7件 [`005aa390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005aa/005aa390.md) [`005ac2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac2ec.md) [`005ac338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005ac338.md) [`005b04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b04f0.md) [`005b06fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b06fc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.42% / 新版 95.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b0580",
      "incomplete_value": true,
      "site": "005b0598",
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
      "definition_site": "005b0580",
      "incomplete_value": true,
      "site": "005b0598",
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
      "definition_site": "005b06d4",
      "incomplete_value": true,
      "site": "005b06e4",
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
      "definition_site": "005b06d4",
      "incomplete_value": true,
      "site": "005b06e4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b0570",
      "READ",
      [
        "storage",
        "00c1b4f0",
        null,
        "pointer"
      ]
    ],
    [
      "005b0598",
      "DATA",
      [
        "storage",
        "00bf3a20",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b06c4",
      "READ",
      [
        "storage",
        "00c1b4f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b0570",
      "READ",
      [
        "storage",
        "00c1b5a0",
        null,
        "pointer"
      ]
    ],
    [
      "005b0598",
      "DATA",
      [
        "storage",
        "00bf3ad0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005b06c4",
      "READ",
      [
        "storage",
        "00c1b5a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b04f0.md#insn-005b0570) · [`005b06c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b04f0.md#insn-005b06c4)
- 新版 `005b0570`（命令位置の公開資料なし） · `005b06c4`（命令位置の公開資料なし）

~~~diff
- 005b0570 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:4f0:8"]]
- 005b0570 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0570 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:5a0:8"]]
+ 005b0570 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0570 bytes 4a7942f9
+ 005b0570 bytes 4ad142f9
- 005b06c4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:4f8:8"]]
- 005b06c4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b06c4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:5a8:8"]]
+ 005b06c4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 005b06c4 bytes 4a7d42f9
+ 005b06c4 bytes 4ad542f9
~~~


<a id="compare-807998fe8e406cb3989d775e60c52481"></a>

### [`005b0a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0a4c.md) → [`005b0a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b0/005b0a4c.md) FUN_005b0a4c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "005b0a5c",
      "incomplete_value": true,
      "site": "005b0a60",
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
      "definition_site": "005b0a5c",
      "incomplete_value": true,
      "site": "005b0a60",
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
      "005b0a54",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ],
    [
      "005b0a60",
      "DATA",
      [
        "storage",
        "00bf3690",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005b0a54",
      "READ",
      [
        "storage",
        "00c1b560",
        null,
        "pointer"
      ]
    ],
    [
      "005b0a60",
      "DATA",
      [
        "storage",
        "00bf3740",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b0/005b0a4c.md#insn-005b0a54)
- 新版 `005b0a54`（命令位置の公開資料なし）

~~~diff
- 005b0a54 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4b0:8"]]
- 005b0a54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005b0a54 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:560:8"]]
+ 005b0a54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005b0a54 bytes 295942f9
+ 005b0a54 bytes 29b142f9
~~~


<a id="compare-d37bce21b4b215a9fad2ba4ba47d993c"></a>

### [`005b39cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b39cc.md) → [`005b39cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b39cc.md) FUN_005b39cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005b3850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3850.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005b3850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3850.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "005b39d8",
      "incomplete_value": false,
      "site": "005b39dc",
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
      "definition_site": "005b39d8",
      "incomplete_value": false,
      "site": "005b39dc",
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
      "005b39d8",
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
      "005b39d8",
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

- 旧版 [`005b39d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b39cc.md#insn-005b39d8)
- 新版 `005b39d8`（命令位置の公開資料なし）

~~~diff
- 005b39d8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005b39d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005b39d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005b39d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005b39d8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 005b39d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005b39d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005b39d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005b39d8 bytes 00280c91
+ 005b39d8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fec0c79b92b42931a8d01b059b440615"></a>

### [`005b4210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4210.md) → [`005b4210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4210.md) FUN_005b4210

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005b4028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4028.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005b4028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4028.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "005b421c",
      "incomplete_value": false,
      "site": "005b4220",
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
      "definition_site": "005b421c",
      "incomplete_value": false,
      "site": "005b4220",
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
      "005b421c",
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
      "005b421c",
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

- 旧版 [`005b421c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4210.md#insn-005b421c)
- 新版 `005b421c`（命令位置の公開資料なし）

~~~diff
- 005b421c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 005b421c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005b421c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005b421c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005b421c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 005b421c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005b421c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005b421c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005b421c bytes 00280c91
+ 005b421c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06b5f7a83fa32f4d720158163caa20ef"></a>

### [`005b4228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4228.md) → [`005b4228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4228.md) FUN_005b4228

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
      "definition_site": "005b424c",
      "incomplete_value": false,
      "site": "005b424c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b424c",
      "incomplete_value": false,
      "site": "005b424c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "005b424c",
      "DATA",
      [
        "storage",
        "00bf3cc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b424c",
      "DATA",
      [
        "storage",
        "00bf3d70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4228.md#insn-005b4248)
- 新版 `005b4248`（命令位置の公開資料なし）

~~~diff
- 005b4248 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 005b4248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4248 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 005b4248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4248 bytes 08013391
+ 005b4248 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1ea5b80c0198f0f1a79b4f1f5cb7db2"></a>

### [`005b425c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b425c.md) → [`005b425c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b425c.md) FUN_005b425c

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
      "definition_site": "005b4268",
      "incomplete_value": false,
      "site": "005b4268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4268",
      "incomplete_value": false,
      "site": "005b4268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "005b4268",
      "DATA",
      [
        "storage",
        "00bf3cc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4268",
      "DATA",
      [
        "storage",
        "00bf3d70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b425c.md#insn-005b4264)
- 新版 `005b4264`（命令位置の公開資料なし）

~~~diff
- 005b4264 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 005b4264 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b4264 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b4264 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b4264 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 005b4264 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b4264 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b4264 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b4264 bytes 29013391
+ 005b4264 bytes 29c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d403f0bc1b9cef6c8925795fa977a20e"></a>

### [`005b4278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4278.md) → [`005b4278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4278.md) FUN_005b4278

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 32件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md)
- 新版 呼出元 0件  · 呼出先 32件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4480",
      "incomplete_value": false,
      "site": "005b4488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4480",
      "incomplete_value": false,
      "site": "005b4488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d40:8"
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
      "definition_site": "005b48b4",
      "incomplete_value": false,
      "site": "005b48b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b48b4",
      "incomplete_value": false,
      "site": "005b48b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
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
      "definition_site": "005b4990",
      "incomplete_value": false,
      "site": "005b4998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4990",
      "incomplete_value": false,
      "site": "005b4998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "ordinal": 61,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b4434",
      "PARAM",
      [
        "storage",
        "0029c68b",
        null,
        "string"
      ]
    ],
    [
      "005b4488",
      "DATA",
      [
        "storage",
        "00bf3d40",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4670",
      "PARAM",
      [
        "storage",
        "00299e3e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005b4434",
      "PARAM",
      [
        "storage",
        "0029c718",
        null,
        "string"
      ]
    ],
    [
      "005b4488",
      "DATA",
      [
        "storage",
        "00bf3df0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4670",
      "PARAM",
      [
        "storage",
        "00299ecb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4278.md#insn-005b4434) · [`005b4480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4278.md#insn-005b4480) · [`005b4484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4278.md#insn-005b4484)
- 新版 `005b4434`（命令位置の公開資料なし） · `005b4480`（命令位置の公開資料なし）

~~~diff
- 005b4434 ["COPY", "tmp:0:8", ["const:68b:8"]]
- 005b4434 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005b4434 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005b4434 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005b4434 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 005b4434 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005b4434 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005b4434 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005b4434 bytes 212c1a91
+ 005b4434 bytes 21601c91
- 005b4480 ["COPY", "tmp:0:8", ["const:d40:8"]]
- 005b4480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4480 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 005b4480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4480 bytes 08013591
+ 005b4480 bytes 08c13791
- 005b4484 ["INT_SUB", "register:40a0:8", ["register:40e8:8", "const:50:8"]]
- 005b4484 bytes b44301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74386353e4db03bf1c20ff8505afe5b6"></a>

### [`005b4f4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4f4c.md) → [`005b4f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4f4c.md) FUN_005b4f4c

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
      "definition_site": "005b4f60",
      "incomplete_value": false,
      "site": "005b4f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4f60",
      "incomplete_value": false,
      "site": "005b4f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d40:8"
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
      "005b4f64",
      "DATA",
      [
        "storage",
        "00bf3d40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4f64",
      "DATA",
      [
        "storage",
        "00bf3df0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4f4c.md#insn-005b4f60)
- 新版 `005b4f60`（命令位置の公開資料なし）

~~~diff
- 005b4f60 ["COPY", "tmp:0:8", ["const:d40:8"]]
- 005b4f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4f60 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 005b4f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4f60 bytes 08013591
+ 005b4f60 bytes 08c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-febf300dc8e10294964097b5ff74677f"></a>

### [`005b4f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4f70.md) → [`005b4f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b4/005b4f70.md) FUN_005b4f70

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
      "definition_site": "005b4f74",
      "incomplete_value": false,
      "site": "005b4f78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4f74",
      "incomplete_value": false,
      "site": "005b4f78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d40:8"
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
      "005b4f78",
      "DATA",
      [
        "storage",
        "00bf3d40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4f78",
      "DATA",
      [
        "storage",
        "00bf3df0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4f74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b4/005b4f70.md#insn-005b4f74)
- 新版 `005b4f74`（命令位置の公開資料なし）

~~~diff
- 005b4f74 ["COPY", "tmp:0:8", ["const:d40:8"]]
- 005b4f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4f74 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 005b4f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4f74 bytes 08013591
+ 005b4f74 bytes 08c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

