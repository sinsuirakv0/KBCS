# v15.7.2 → v15.7.3 · 最優先の変更候補 (79)

[一覧の目次](README.md)

<a id="compare-eafdc5f5b5b15ce2911fc89e8ca8abd9"></a>

### [`00bc0b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0b18.md) → [`00bc0be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0be0.md) FUN_00bc0be0

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
      "definition_site": "00bc0c44",
      "incomplete_value": false,
      "site": "00bc0c44",
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
      "definition_site": "00bc0b7c",
      "incomplete_value": false,
      "site": "00bc0b7c",
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
      "00bc0c44",
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
      "00bc0c44",
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

- 旧版 [`00bc0b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0b18.md#insn-00bc0b4c) · [`00bc0b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0b18.md#insn-00bc0b70) · [`00bc0bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0b18.md#insn-00bc0bc4)
- 新版 `00bc0c14`（命令位置の公開資料なし） · `00bc0c38`（命令位置の公開資料なし） · `00bc0c8c`（命令位置の公開資料なし）

~~~diff
- 00bc0b4c ["INT_ADD", "register:40f0:8", ["const:bc0b4c:8", "const:4:8"]]
- 00bc0b4c ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc0c14 ["INT_ADD", "register:40f0:8", ["const:bc0c14:8", "const:4:8"]]
+ 00bc0c14 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc0b4c bytes 61710094
+ 00bc0c14 bytes 5b710094
- 00bc0b70 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00bc0b70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0b70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0b70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0c38 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00bc0c38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0c38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0c38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0b70 bytes 08a11a91
+ 00bc0c38 bytes 08611d91
- 00bc0bc4 ["INT_ADD", "register:40f0:8", ["const:bc0bc4:8", "const:4:8"]]
- 00bc0bc4 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc0c8c ["INT_ADD", "register:40f0:8", ["const:bc0c8c:8", "const:4:8"]]
+ 00bc0c8c ["CALL", null, ["callee:00bdb180:8"]]
- 00bc0bc4 bytes 43690094
+ 00bc0c8c bytes 3d690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9e1519ab25e2d781597c907553f6f7a"></a>

### [`00bc0eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0eb4.md) → [`00bc0f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0f7c.md) FUN_00bc0f7c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.68% / 新版 94.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0fe4",
      "incomplete_value": true,
      "site": "00bc0ff0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0f1c",
      "incomplete_value": true,
      "site": "00bc0f28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:39a:8"
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
      "definition_site": "00bc0fe8",
      "incomplete_value": true,
      "site": "00bc0ff4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bc0f20",
      "incomplete_value": true,
      "site": "00bc0f2c",
      "value": [
        "LOAD",
        "8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc0fe4",
      "READ",
      [
        "storage",
        "002aa39a",
        null,
        "string"
      ]
    ],
    [
      "00bc0fe8",
      "READ",
      [
        "storage",
        "002aa3aa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0fe4",
      "READ",
      [
        "storage",
        "002aa3a0",
        null,
        "string"
      ]
    ],
    [
      "00bc0fe8",
      "READ",
      [
        "storage",
        "002aa3b0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0eb4.md#insn-00bc0efc) · [`00bc0f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0eb4.md#insn-00bc0f14) · [`00bc0f4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0eb4.md#insn-00bc0f4c)
- 新版 `00bc0fc4`（命令位置の公開資料なし） · `00bc0fdc`（命令位置の公開資料なし） · `00bc1014`（命令位置の公開資料なし）

~~~diff
- 00bc0efc ["INT_ADD", "register:40f0:8", ["const:bc0efc:8", "const:4:8"]]
- 00bc0efc ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc0fc4 ["INT_ADD", "register:40f0:8", ["const:bc0fc4:8", "const:4:8"]]
+ 00bc0fc4 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc0efc bytes 95700094
+ 00bc0fc4 bytes 8f700094
- 00bc0f14 ["COPY", "tmp:0:8", ["const:39a:8"]]
- 00bc0f14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bc0f14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bc0f14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bc0fdc ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 00bc0fdc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc0fdc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc0fdc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bc0f14 bytes 4a690e91
+ 00bc0fdc bytes 4a810e91
- 00bc0f4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc0f4c ["INT_ADD", "register:40f0:8", ["const:bc0f4c:8", "const:4:8"]]
- 00bc0f4c ["CALLIND", null, ["register:0:8"]]
+ 00bc1014 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc1014 ["INT_ADD", "register:40f0:8", ["const:bc1014:8", "const:4:8"]]
+ 00bc1014 ["CALLIND", null, ["register:0:8"]]
- 00bc0f4c bytes 00013fd6
+ 00bc1014 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5451b33cf5d026adbc6e4a9208bc8b3e"></a>

### [`00bc1034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1034.md) → [`00bc10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md) FUN_00bc10fc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 7件 [`00bc0bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0bc8.md) [`00bc2394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2394.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) [`00bc5510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5510.md) [`00bc66f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc66f0.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 7件 [`00bc0c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0c90.md) [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bc55d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc55d8.md) [`00bc67b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.26% / 新版 96.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc121c",
      "incomplete_value": false,
      "site": "00bc121c",
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
      "definition_site": "00bc1154",
      "incomplete_value": false,
      "site": "00bc1154",
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
      "00bc121c",
      "DATA",
      [
        "storage",
        "00c17798",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc1228",
      "DATA",
      [
        "storage",
        "0029f1f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc121c",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc1228",
      "DATA",
      [
        "storage",
        "0029f286",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1034.md#insn-00bc1124) · [`00bc1148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1034.md#insn-00bc1148) · [`00bc11ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1034.md#insn-00bc11ac)
- 新版 `00bc11ec`（命令位置の公開資料なし） · `00bc1210`（命令位置の公開資料なし） · `00bc1274`（命令位置の公開資料なし）

~~~diff
- 00bc1124 ["INT_ADD", "register:40f0:8", ["const:bc1124:8", "const:4:8"]]
- 00bc1124 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc11ec ["INT_ADD", "register:40f0:8", ["const:bc11ec:8", "const:4:8"]]
+ 00bc11ec ["CALL", null, ["callee:00bdd180:8"]]
- 00bc1124 bytes eb6f0094
+ 00bc11ec bytes e56f0094
- 00bc1148 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bc1148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc1210 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bc1210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc1148 bytes 08611e91
+ 00bc1210 bytes 08212191
- 00bc11ac ["INT_ADD", "register:40f0:8", ["const:bc11ac:8", "const:4:8"]]
- 00bc11ac ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc1274 ["INT_ADD", "register:40f0:8", ["const:bc1274:8", "const:4:8"]]
+ 00bc1274 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc11ac bytes c96f0094
+ 00bc1274 bytes c36f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bedb5602d47bfd1d04cfb4c064f23b4"></a>

### [`00bc1260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1260.md) → [`00bc1328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1328.md) FUN_00bc1328

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc138c",
      "incomplete_value": false,
      "site": "00bc138c",
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
      "definition_site": "00bc12c4",
      "incomplete_value": false,
      "site": "00bc12c4",
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
      "00bc138c",
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
      "00bc138c",
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

- 旧版 [`00bc1294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1260.md#insn-00bc1294) · [`00bc12b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1260.md#insn-00bc12b8) · [`00bc12fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1260.md#insn-00bc12fc)
- 新版 `00bc135c`（命令位置の公開資料なし） · `00bc1380`（命令位置の公開資料なし） · `00bc13c4`（命令位置の公開資料なし）

~~~diff
- 00bc1294 ["INT_ADD", "register:40f0:8", ["const:bc1294:8", "const:4:8"]]
- 00bc1294 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc135c ["INT_ADD", "register:40f0:8", ["const:bc135c:8", "const:4:8"]]
+ 00bc135c ["CALL", null, ["callee:00bdd180:8"]]
- 00bc1294 bytes 8f6f0094
+ 00bc135c bytes 896f0094
- 00bc12b8 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bc12b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc12b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc12b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc1380 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bc1380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc12b8 bytes 08611e91
+ 00bc1380 bytes 08212191
- 00bc12fc ["INT_ADD", "register:40f0:8", ["const:bc12fc:8", "const:4:8"]]
- 00bc12fc ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc13c4 ["INT_ADD", "register:40f0:8", ["const:bc13c4:8", "const:4:8"]]
+ 00bc13c4 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc12fc bytes 75670094
+ 00bc13c4 bytes 6f670094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e3d95b56304db389a55dca687ece5a2"></a>

### [`00bc14d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc14d8.md) → [`00bc15a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc15a0.md) FUN_00bc15a0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) · 呼出先 4件 [`00bc20b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc20b8.md) [`00bc2394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2394.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) · 呼出先 4件 [`00bc2180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2180.md) [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc1688",
      "incomplete_value": false,
      "site": "00bc1688",
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
      "definition_site": "00bc15c0",
      "incomplete_value": false,
      "site": "00bc15c0",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc16a4",
      "incomplete_value": false,
      "site": "00bc16b0",
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
      "definition_site": "00bc15dc",
      "incomplete_value": false,
      "site": "00bc15e8",
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
      "00bc1688",
      "DATA",
      [
        "storage",
        "00c17798",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc16b0",
      "DATA",
      [
        "storage",
        "002a809c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc1688",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc16b0",
      "DATA",
      [
        "storage",
        "002a8008",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc14d8.md#insn-00bc1530) · [`00bc1580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc14d8.md#insn-00bc1580) · [`00bc15b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc14d8.md#insn-00bc15b4)
- 新版 `00bc15f8`（命令位置の公開資料なし） · `00bc1648`（命令位置の公開資料なし） · `00bc167c`（命令位置の公開資料なし）

~~~diff
- 00bc1530 ["INT_ADD", "register:40f0:8", ["const:bc1530:8", "const:4:8"]]
- 00bc1530 ["CALL", null, ["callee:00bc2180:8"]]
+ 00bc15f8 ["INT_ADD", "register:40f0:8", ["const:bc15f8:8", "const:4:8"]]
+ 00bc15f8 ["CALL", null, ["callee:00bc2180:8"]]
- 00bc1530 bytes e2020094
+ 00bc15f8 bytes e2020094
- 00bc1580 ["INT_ADD", "register:40f0:8", ["const:bc1580:8", "const:4:8"]]
- 00bc1580 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc1648 ["INT_ADD", "register:40f0:8", ["const:bc1648:8", "const:4:8"]]
+ 00bc1648 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc1580 bytes d46e0094
+ 00bc1648 bytes ce6e0094
- 00bc15b4 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bc15b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc15b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc15b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc167c ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bc167c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc167c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc167c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc15b4 bytes 29611e91
+ 00bc167c bytes 29212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3322336b4232e6336b9ede9c29ae364"></a>

### [`00bc1648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1648.md) → [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) FUN_00bc1710

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bc66f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc66f0.md) [`00bce830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce830.md) [`00bd166c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd166c.md) · 呼出先 8件 [`00bbf9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) [`00bbfe64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 5件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bc67b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md) [`00bce8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md) [`00bd1734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1734.md) · 呼出先 8件 [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc1924",
      "incomplete_value": false,
      "site": "00bc1924",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc185c",
      "incomplete_value": false,
      "site": "00bc185c",
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
            "const:5b8:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc1b90",
      "incomplete_value": false,
      "site": "00bc1b90",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1ac8",
      "incomplete_value": false,
      "site": "00bc1ac8",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc1924",
      "DATA",
      [
        "storage",
        "00c195b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc1b90",
      "DATA",
      [
        "storage",
        "00c19628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc1924",
      "DATA",
      [
        "storage",
        "00c19668",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc1b90",
      "DATA",
      [
        "storage",
        "00c196d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc16bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1648.md#insn-00bc16bc) · [`00bc16c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1648.md#insn-00bc16c8) · [`00bc16d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1648.md#insn-00bc16d0)
- 新版 `00bc1784`（命令位置の公開資料なし） · `00bc1790`（命令位置の公開資料なし） · `00bc1798`（命令位置の公開資料なし）

~~~diff
- 00bc16bc ["INT_ADD", "register:40f0:8", ["const:bc16bc:8", "const:4:8"]]
- 00bc16bc ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc1784 ["INT_ADD", "register:40f0:8", ["const:bc1784:8", "const:4:8"]]
+ 00bc1784 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc16bc bytes a56e0094
+ 00bc1784 bytes 9f6e0094
- 00bc16c8 ["INT_ADD", "register:40f0:8", ["const:bc16c8:8", "const:4:8"]]
- 00bc16c8 ["CALL", null, ["callee:00bde270:8"]]
+ 00bc1790 ["INT_ADD", "register:40f0:8", ["const:bc1790:8", "const:4:8"]]
+ 00bc1790 ["CALL", null, ["callee:00bde270:8"]]
- 00bc16c8 bytes be720094
+ 00bc1790 bytes b8720094
- 00bc16d0 ["INT_ADD", "register:40f0:8", ["const:bc16d0:8", "const:4:8"]]
- 00bc16d0 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc1798 ["INT_ADD", "register:40f0:8", ["const:bc1798:8", "const:4:8"]]
+ 00bc1798 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc16d0 bytes 806e0094
+ 00bc1798 bytes 7a6e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34ebf0a247b4bc1bae0e9e3b6edde6e0"></a>

### [`00bc1b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1b18.md) → [`00bc1be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1be0.md) FUN_00bc1be0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bc66f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc66f0.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc67b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc1c48",
      "incomplete_value": false,
      "site": "00bc1c48",
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
      "definition_site": "00bc1b80",
      "incomplete_value": false,
      "site": "00bc1b80",
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
      "00bc1c48",
      "DATA",
      [
        "storage",
        "00c19698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc1c48",
      "DATA",
      [
        "storage",
        "00c19748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1b50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1b18.md#insn-00bc1b50) · [`00bc1b74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1b18.md#insn-00bc1b74) · [`00bc1bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1b18.md#insn-00bc1bbc)
- 新版 `00bc1c18`（命令位置の公開資料なし） · `00bc1c3c`（命令位置の公開資料なし） · `00bc1c84`（命令位置の公開資料なし）

~~~diff
- 00bc1b50 ["INT_ADD", "register:40f0:8", ["const:bc1b50:8", "const:4:8"]]
- 00bc1b50 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc1c18 ["INT_ADD", "register:40f0:8", ["const:bc1c18:8", "const:4:8"]]
+ 00bc1c18 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc1b50 bytes 606d0094
+ 00bc1c18 bytes 5a6d0094
- 00bc1b74 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00bc1b74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1b74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1b74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc1c3c ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00bc1c3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1c3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1c3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc1b74 bytes 08611a91
+ 00bc1c3c bytes 08211d91
- 00bc1bbc ["INT_ADD", "register:40f0:8", ["const:bc1bbc:8", "const:4:8"]]
- 00bc1bbc ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc1c84 ["INT_ADD", "register:40f0:8", ["const:bc1c84:8", "const:4:8"]]
+ 00bc1c84 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc1bbc bytes 45650094
+ 00bc1c84 bytes 3f650094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eeb24efff1b4677688b552090ba8e58"></a>

### [`00bc1bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1bc0.md) → [`00bc1c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1c88.md) FUN_00bc1c88

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) [`00bce6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce6ac.md) · 呼出先 7件 [`00bc29f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc29f4.md) [`00bc2acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2acc.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 4件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bce774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) · 呼出先 7件 [`00bc2abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2abc.md) [`00bc2b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2b94.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.93% / 新版 97.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc1ddc",
      "incomplete_value": false,
      "site": "00bc1ddc",
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
      "definition_site": "00bc1d14",
      "incomplete_value": false,
      "site": "00bc1d14",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc1ef4",
      "incomplete_value": false,
      "site": "00bc1ef4",
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
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1e2c",
      "incomplete_value": false,
      "site": "00bc1e2c",
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
            "const:878:8"
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
      "00bc1ddc",
      "DATA",
      [
        "storage",
        "00c17798",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc1ef4",
      "DATA",
      [
        "storage",
        "00c17878",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc1fd4",
      "PARAM",
      [
        "storage",
        "002925bc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc1ddc",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc1ef4",
      "DATA",
      [
        "storage",
        "00c17928",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc1fd4",
      "PARAM",
      [
        "storage",
        "00292649",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1ce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1bc0.md#insn-00bc1ce4) · [`00bc1d08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1bc0.md#insn-00bc1d08) · [`00bc1df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1bc0.md#insn-00bc1df4)
- 新版 `00bc1dac`（命令位置の公開資料なし） · `00bc1dd0`（命令位置の公開資料なし） · `00bc1ebc`（命令位置の公開資料なし）

~~~diff
- 00bc1ce4 ["INT_ADD", "register:40f0:8", ["const:bc1ce4:8", "const:4:8"]]
- 00bc1ce4 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc1dac ["INT_ADD", "register:40f0:8", ["const:bc1dac:8", "const:4:8"]]
+ 00bc1dac ["CALL", null, ["callee:00bdd180:8"]]
- 00bc1ce4 bytes fb6c0094
+ 00bc1dac bytes f56c0094
- 00bc1d08 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bc1d08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1d08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc1d08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc1dd0 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bc1dd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1dd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc1dd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc1d08 bytes 08611e91
+ 00bc1dd0 bytes 08212191
- 00bc1df4 ["INT_ADD", "register:40f0:8", ["const:bc1df4:8", "const:4:8"]]
- 00bc1df4 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc1ebc ["INT_ADD", "register:40f0:8", ["const:bc1ebc:8", "const:4:8"]]
+ 00bc1ebc ["CALL", null, ["callee:00bdd180:8"]]
- 00bc1df4 bytes b76c0094
+ 00bc1ebc bytes b16c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fad51db22cf3fc7557fc23f95b758f3"></a>

### [`00bc1f84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1f84.md) → [`00bc204c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc204c.md) FUN_00bc204c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bce6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce6ac.md) · 呼出先 3件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 3件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bce774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) · 呼出先 3件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc2128",
      "incomplete_value": false,
      "site": "00bc2128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2060",
      "incomplete_value": false,
      "site": "00bc2060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "definition_site": "00bc2148",
      "incomplete_value": false,
      "site": "00bc2148",
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
            "const:13c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2080",
      "incomplete_value": false,
      "site": "00bc2080",
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
            "const:af:8"
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
      "00bc2128",
      "DATA",
      [
        "storage",
        "00c18198",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc2148",
      "DATA",
      [
        "storage",
        "0029e0af",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2128",
      "DATA",
      [
        "storage",
        "00c18248",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc2148",
      "DATA",
      [
        "storage",
        "0029e13c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1f84.md#insn-00bc1fe4) · [`00bc202c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1f84.md#insn-00bc202c) · [`00bc2054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1f84.md#insn-00bc2054)
- 新版 `00bc20ac`（命令位置の公開資料なし） · `00bc20f4`（命令位置の公開資料なし） · `00bc211c`（命令位置の公開資料なし）

~~~diff
- 00bc1fe4 ["INT_ADD", "register:40f0:8", ["const:bc1fe4:8", "const:4:8"]]
- 00bc1fe4 ["CALL", null, ["callee:00bc2ec8:8"]]
+ 00bc20ac ["INT_ADD", "register:40f0:8", ["const:bc20ac:8", "const:4:8"]]
+ 00bc20ac ["CALL", null, ["callee:00bc2ec8:8"]]
- 00bc1fe4 bytes 87030094
+ 00bc20ac bytes 87030094
- 00bc202c ["INT_ADD", "register:40f0:8", ["const:bc202c:8", "const:4:8"]]
- 00bc202c ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc20f4 ["INT_ADD", "register:40f0:8", ["const:bc20f4:8", "const:4:8"]]
+ 00bc20f4 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc202c bytes 296c0094
+ 00bc20f4 bytes 236c0094
- 00bc2054 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00bc2054 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bc2054 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bc2054 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bc211c ["COPY", "tmp:0:8", ["const:248:8"]]
+ 00bc211c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc211c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc211c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bc2054 bytes 4a610691
+ 00bc211c bytes 4a210991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5525276ea74d896b6defcdd9caa2eed"></a>

### [`00bc20b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc20b8.md) → [`00bc2180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2180.md) FUN_00bc2180

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bc14d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc14d8.md) [`00bce6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce6ac.md) · 呼出先 6件 [`00bcf2ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf2ac.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md)
- 新版 呼出元 3件 [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bc15a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc15a0.md) [`00bce774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) · 呼出先 6件 [`00bcf374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf374.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "00bc23a4",
      "incomplete_value": false,
      "site": "00bc23a8",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc22dc",
      "incomplete_value": false,
      "site": "00bc22e0",
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
            "const:1c8:8"
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
      "00bc23a8",
      "DATA",
      [
        "storage",
        "00c191c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc23a8",
      "DATA",
      [
        "storage",
        "00c19278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc20b8.md#insn-00bc2284) · [`00bc22dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc20b8.md#insn-00bc22dc) · [`00bc22e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc20b8.md#insn-00bc22e4)
- 新版 `00bc234c`（命令位置の公開資料なし） · `00bc23a4`（命令位置の公開資料なし） · `00bc23ac`（命令位置の公開資料なし）

~~~diff
- 00bc2284 ["INT_ADD", "register:40f0:8", ["const:bc2284:8", "const:4:8"]]
- 00bc2284 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc234c ["INT_ADD", "register:40f0:8", ["const:bc234c:8", "const:4:8"]]
+ 00bc234c ["CALL", null, ["callee:00bdd180:8"]]
- 00bc2284 bytes 936b0094
+ 00bc234c bytes 8d6b0094
- 00bc22dc ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 00bc22dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc22dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc22dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc23a4 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 00bc23a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc23a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc23a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc22dc bytes 08210791
+ 00bc23a4 bytes 08e10991
- 00bc22e4 ["INT_ADD", "register:40f0:8", ["const:bc22e4:8", "const:4:8"]]
- 00bc22e4 ["CALL", null, ["callee:00bcf374:8"]]
+ 00bc23ac ["INT_ADD", "register:40f0:8", ["const:bc23ac:8", "const:4:8"]]
+ 00bc23ac ["CALL", null, ["callee:00bcf374:8"]]
- 00bc22e4 bytes f2330094
+ 00bc23ac bytes f2330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f93ada6e4467f454f3868ba0a983d3d"></a>

### [`00bc2394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2394.md) → [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) FUN_00bc245c

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bc14d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc14d8.md) · 呼出先 13件 [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bbfe64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md) [`00bc0bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0bc8.md) [`00bc1034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1034.md) [`00bc95a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc95a4.md)
- 新版 呼出元 2件 [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bc15a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc15a0.md) · 呼出先 13件 [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc0c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0c90.md) [`00bc10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md) [`00bc966c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc966c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc25dc",
      "incomplete_value": false,
      "site": "00bc25e8",
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
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2514",
      "incomplete_value": false,
      "site": "00bc2520",
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
            "const:250:8"
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
      "definition_site": "00bc26a4",
      "incomplete_value": false,
      "site": "00bc26a4",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc25dc",
      "incomplete_value": false,
      "site": "00bc25dc",
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
            "const:3f8:8"
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
      "definition_site": "00bc290c",
      "incomplete_value": false,
      "site": "00bc290c",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc2844",
      "incomplete_value": false,
      "site": "00bc2844",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc25e8",
      "DATA",
      [
        "storage",
        "00c19250",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc26a4",
      "DATA",
      [
        "storage",
        "00c193f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc2794",
      "DATA",
      [
        "storage",
        "00c194d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc25e8",
      "DATA",
      [
        "storage",
        "00c19300",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc26a4",
      "DATA",
      [
        "storage",
        "00c194a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc2794",
      "DATA",
      [
        "storage",
        "00c19588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc2514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2394.md#insn-00bc2514) · [`00bc23c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2394.md#insn-00bc23c8) · [`00bc244c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2394.md#insn-00bc244c)
- 新版 `00bc25dc`（命令位置の公開資料なし） · `00bc2490`（命令位置の公開資料なし） · `00bc2514`（命令位置の公開資料なし）

~~~diff
- 00bc2514 ["COPY", "tmp:0:8", ["const:250:8"]]
- 00bc2514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc2514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc25dc ["COPY", "tmp:0:8", ["const:300:8"]]
+ 00bc25dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc25dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc25dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc2514 bytes 08410991
+ 00bc25dc bytes 08010c91
- 00bc23c8 ["INT_ADD", "register:40f0:8", ["const:bc23c8:8", "const:4:8"]]
- 00bc23c8 ["CALL", null, ["callee:00bc0c90:8"]]
+ 00bc2490 ["INT_ADD", "register:40f0:8", ["const:bc2490:8", "const:4:8"]]
+ 00bc2490 ["CALL", null, ["callee:00bc0c90:8"]]
- 00bc23c8 bytes 00faff97
+ 00bc2490 bytes 00faff97
- 00bc244c ["INT_ADD", "register:40f0:8", ["const:bc244c:8", "const:4:8"]]
- 00bc244c ["CALL", null, ["callee:00bc10fc:8"]]
+ 00bc2514 ["INT_ADD", "register:40f0:8", ["const:bc2514:8", "const:4:8"]]
+ 00bc2514 ["CALL", null, ["callee:00bc10fc:8"]]
- 00bc244c bytes fafaff97
+ 00bc2514 bytes fafaff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be6d90e983555c1f9711a3453022803a"></a>

### [`00bc2954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2954.md) → [`00bc2a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2a1c.md) FUN_00bc2a1c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc2a80",
      "incomplete_value": false,
      "site": "00bc2a80",
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
      "definition_site": "00bc29b8",
      "incomplete_value": false,
      "site": "00bc29b8",
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
      "00bc2a80",
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
      "00bc2a80",
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

- 旧版 [`00bc2988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2954.md#insn-00bc2988) · [`00bc29ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2954.md#insn-00bc29ac) · [`00bc29f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2954.md#insn-00bc29f0)
- 新版 `00bc2a50`（命令位置の公開資料なし） · `00bc2a74`（命令位置の公開資料なし） · `00bc2ab8`（命令位置の公開資料なし）

~~~diff
- 00bc2988 ["INT_ADD", "register:40f0:8", ["const:bc2988:8", "const:4:8"]]
- 00bc2988 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc2a50 ["INT_ADD", "register:40f0:8", ["const:bc2a50:8", "const:4:8"]]
+ 00bc2a50 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc2988 bytes d2690094
+ 00bc2a50 bytes cc690094
- 00bc29ac ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bc29ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc29ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc29ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc2a74 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bc2a74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2a74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc2a74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc29ac bytes 08611e91
+ 00bc2a74 bytes 08212191
- 00bc29f0 ["INT_ADD", "register:40f0:8", ["const:bc29f0:8", "const:4:8"]]
- 00bc29f0 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc2ab8 ["INT_ADD", "register:40f0:8", ["const:bc2ab8:8", "const:4:8"]]
+ 00bc2ab8 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc29f0 bytes b8610094
+ 00bc2ab8 bytes b2610094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29c510e6612c7b61d5bc23e5bb162b79"></a>

### [`00bc2acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2acc.md) → [`00bc2b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2b94.md) FUN_00bc2b94

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bc1bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1bc0.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc1c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1c88.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc2c00",
      "incomplete_value": false,
      "site": "00bc2c00",
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
      "definition_site": "00bc2b38",
      "incomplete_value": false,
      "site": "00bc2b38",
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
      "00bc2c00",
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
      "00bc2c00",
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

- 旧版 [`00bc2b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2acc.md#insn-00bc2b00) · [`00bc2b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2acc.md#insn-00bc2b28) · [`00bc2b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2acc.md#insn-00bc2b30)
- 新版 `00bc2bc8`（命令位置の公開資料なし） · `00bc2bf0`（命令位置の公開資料なし） · `00bc2bf8`（命令位置の公開資料なし）

~~~diff
- 00bc2b00 ["INT_ADD", "register:40f0:8", ["const:bc2b00:8", "const:4:8"]]
- 00bc2b00 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc2bc8 ["INT_ADD", "register:40f0:8", ["const:bc2bc8:8", "const:4:8"]]
+ 00bc2bc8 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc2b00 bytes 74690094
+ 00bc2bc8 bytes 6e690094
- 00bc2b28 ["INT_ADD", "register:40f0:8", ["const:bc2b28:8", "const:4:8"]]
- 00bc2b28 ["CALL", null, ["callee:00bdb140:8"]]
+ 00bc2bf0 ["INT_ADD", "register:40f0:8", ["const:bc2bf0:8", "const:4:8"]]
+ 00bc2bf0 ["CALL", null, ["callee:00bdb140:8"]]
- 00bc2b28 bytes 5a610094
+ 00bc2bf0 bytes 54610094
- 00bc2b30 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bc2b30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc2b30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc2b30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc2bf8 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bc2bf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc2bf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc2bf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc2b30 bytes 29611e91
+ 00bc2bf8 bytes 29212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8025895d0ad0747b529e0bf067bbc93"></a>

### [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) → [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) FUN_00bc2ec8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 14件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) [`00bc1648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1648.md) [`00bc1f84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1f84.md) · 呼出先 42件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bbd19c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd19c.md) [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) [`00bbfcec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfcec.md)
- 新版 呼出元 14件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) [`00bc204c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc204c.md) · 呼出先 42件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bbd264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd264.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bbfdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.56% / 新版 98.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc3218",
      "incomplete_value": false,
      "site": "00bc3218",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3150",
      "incomplete_value": false,
      "site": "00bc3150",
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
            "const:d38:8"
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
      "definition_site": "00bc365c",
      "incomplete_value": false,
      "site": "00bc365c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc3594",
      "incomplete_value": false,
      "site": "00bc3594",
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
            "const:f68:8"
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
      "definition_site": "00bc3a9c",
      "incomplete_value": false,
      "site": "00bc3a9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc39d4",
      "incomplete_value": false,
      "site": "00bc39d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 105,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2f9c",
      "READ",
      [
        "storage",
        "00c17ab8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2fac",
      "READ",
      [
        "storage",
        "00c17ab9",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2fd8",
      "READ",
      [
        "storage",
        "00c17ac8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2f9c",
      "READ",
      [
        "storage",
        "00c17b68",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2fac",
      "READ",
      [
        "storage",
        "00c17b69",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2fd8",
      "READ",
      [
        "storage",
        "00c17b78",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc32b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md#insn-00bc32b8) · [`00bc3318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md#insn-00bc3318) · [`00bc38bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md#insn-00bc38bc)
- 新版 `00bc3380`（命令位置の公開資料なし） · `00bc33e0`（命令位置の公開資料なし） · `00bc3984`（命令位置の公開資料なし）

~~~diff
- 00bc32b8 ["INT_ADD", "register:40f0:8", ["const:bc32b8:8", "const:4:8"]]
- 00bc32b8 ["CALL", null, ["callee:00bbd264:8"]]
+ 00bc3380 ["INT_ADD", "register:40f0:8", ["const:bc3380:8", "const:4:8"]]
+ 00bc3380 ["CALL", null, ["callee:00bbd264:8"]]
- 00bc32b8 bytes b9e7ff97
+ 00bc3380 bytes b9e7ff97
- 00bc3318 ["INT_ADD", "register:40f0:8", ["const:bc3318:8", "const:4:8"]]
- 00bc3318 ["CALL", null, ["callee:00bbd264:8"]]
+ 00bc33e0 ["INT_ADD", "register:40f0:8", ["const:bc33e0:8", "const:4:8"]]
+ 00bc33e0 ["CALL", null, ["callee:00bbd264:8"]]
- 00bc3318 bytes a1e7ff97
+ 00bc33e0 bytes a1e7ff97
- 00bc38bc ["INT_ADD", "register:40f0:8", ["const:bc38bc:8", "const:4:8"]]
- 00bc38bc ["CALL", null, ["callee:00bbd264:8"]]
+ 00bc3984 ["INT_ADD", "register:40f0:8", ["const:bc3984:8", "const:4:8"]]
+ 00bc3984 ["CALL", null, ["callee:00bbd264:8"]]
- 00bc38bc bytes 38e6ff97
+ 00bc3984 bytes 38e6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d0be82c401420fb378f3bb1966353d5"></a>

### [`00bc4250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc4250.md) → [`00bc4318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc4318.md) FUN_00bc4318

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc4388",
      "incomplete_value": false,
      "site": "00bc4388",
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
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc42c0",
      "incomplete_value": false,
      "site": "00bc42c0",
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
            "const:e18:8"
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
      "00bc4388",
      "DATA",
      [
        "storage",
        "00c17e18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc4388",
      "DATA",
      [
        "storage",
        "00c17ec8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc4250.md#insn-00bc4290) · [`00bc42b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc4250.md#insn-00bc42b4) · [`00bc4308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc4250.md#insn-00bc4308)
- 新版 `00bc4358`（命令位置の公開資料なし） · `00bc437c`（命令位置の公開資料なし） · `00bc43d0`（命令位置の公開資料なし）

~~~diff
- 00bc4290 ["INT_ADD", "register:40f0:8", ["const:bc4290:8", "const:4:8"]]
- 00bc4290 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc4358 ["INT_ADD", "register:40f0:8", ["const:bc4358:8", "const:4:8"]]
+ 00bc4358 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc4290 bytes 90630094
+ 00bc4358 bytes 8a630094
- 00bc42b4 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 00bc42b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc42b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc42b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc437c ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00bc437c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc437c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc437c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc42b4 bytes 08613891
+ 00bc437c bytes 08213b91
- 00bc4308 ["INT_ADD", "register:40f0:8", ["const:bc4308:8", "const:4:8"]]
- 00bc4308 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc43d0 ["INT_ADD", "register:40f0:8", ["const:bc43d0:8", "const:4:8"]]
+ 00bc43d0 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc4308 bytes 725b0094
+ 00bc43d0 bytes 6c5b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-054249ef3ed430bc7b5a305c6194c6bc"></a>

### [`00bc430c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc430c.md) → [`00bc43d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc43d4.md) FUN_00bc43d4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc4448",
      "incomplete_value": false,
      "site": "00bc4448",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4380",
      "incomplete_value": false,
      "site": "00bc4380",
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
            "const:e88:8"
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
      "00bc4448",
      "DATA",
      [
        "storage",
        "00c17e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc4448",
      "DATA",
      [
        "storage",
        "00c17f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc430c.md#insn-00bc4350) · [`00bc4374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc430c.md#insn-00bc4374) · [`00bc43d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc430c.md#insn-00bc43d4)
- 新版 `00bc4418`（命令位置の公開資料なし） · `00bc443c`（命令位置の公開資料なし） · `00bc449c`（命令位置の公開資料なし）

~~~diff
- 00bc4350 ["INT_ADD", "register:40f0:8", ["const:bc4350:8", "const:4:8"]]
- 00bc4350 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc4418 ["INT_ADD", "register:40f0:8", ["const:bc4418:8", "const:4:8"]]
+ 00bc4418 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc4350 bytes 60630094
+ 00bc4418 bytes 5a630094
- 00bc4374 ["COPY", "tmp:0:8", ["const:e88:8"]]
- 00bc4374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc4374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc4374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc443c ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00bc443c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc443c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc443c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc4374 bytes 08213a91
+ 00bc443c bytes 08e13c91
- 00bc43d4 ["INT_ADD", "register:40f0:8", ["const:bc43d4:8", "const:4:8"]]
- 00bc43d4 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc449c ["INT_ADD", "register:40f0:8", ["const:bc449c:8", "const:4:8"]]
+ 00bc449c ["CALL", null, ["callee:00bdb180:8"]]
- 00bc43d4 bytes 3f5b0094
+ 00bc449c bytes 395b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b171ee36ae4894dd78448115aa09628"></a>

### [`00bc43d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc43d8.md) → [`00bc44a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc44a0.md) FUN_00bc44a0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc4520",
      "incomplete_value": false,
      "site": "00bc4520",
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
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4458",
      "incomplete_value": false,
      "site": "00bc4458",
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
            "const:ef8:8"
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
      "00bc4520",
      "DATA",
      [
        "storage",
        "00c17ef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc4520",
      "DATA",
      [
        "storage",
        "00c17fa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc43d8.md#insn-00bc4428) · [`00bc444c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc43d8.md#insn-00bc444c) · [`00bc44c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc43d8.md#insn-00bc44c0)
- 新版 `00bc44f0`（命令位置の公開資料なし） · `00bc4514`（命令位置の公開資料なし） · `00bc4588`（命令位置の公開資料なし）

~~~diff
- 00bc4428 ["INT_ADD", "register:40f0:8", ["const:bc4428:8", "const:4:8"]]
- 00bc4428 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc44f0 ["INT_ADD", "register:40f0:8", ["const:bc44f0:8", "const:4:8"]]
+ 00bc44f0 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc4428 bytes 2a630094
+ 00bc44f0 bytes 24630094
- 00bc444c ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 00bc444c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc444c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc444c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc4514 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 00bc4514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc4514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc4514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc444c bytes 08e13b91
+ 00bc4514 bytes 08a13e91
- 00bc44c0 ["INT_ADD", "register:40f0:8", ["const:bc44c0:8", "const:4:8"]]
- 00bc44c0 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc4588 ["INT_ADD", "register:40f0:8", ["const:bc4588:8", "const:4:8"]]
+ 00bc4588 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc44c0 bytes 045b0094
+ 00bc4588 bytes fe5a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-793f768f7a4fc91fb79ed163c377cc45"></a>

### [`00bc44c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc44c4.md) → [`00bc458c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc458c.md) FUN_00bc458c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc45fc",
      "incomplete_value": false,
      "site": "00bc45fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4534",
      "incomplete_value": false,
      "site": "00bc4534",
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
            "const:fd8:8"
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
      "00bc45fc",
      "DATA",
      [
        "storage",
        "00c17fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc45fc",
      "DATA",
      [
        "storage",
        "00c18088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc44c4.md#insn-00bc4504) · [`00bc4524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc44c4.md#insn-00bc4524) · [`00bc4528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc44c4.md#insn-00bc4528)
- 新版 `00bc45cc`（命令位置の公開資料なし） · `00bc45ec`（命令位置の公開資料なし） · `00bc45f0`（命令位置の公開資料なし）

~~~diff
- 00bc4504 ["INT_ADD", "register:40f0:8", ["const:bc4504:8", "const:4:8"]]
- 00bc4504 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc45cc ["INT_ADD", "register:40f0:8", ["const:bc45cc:8", "const:4:8"]]
+ 00bc45cc ["CALL", null, ["callee:00bdd180:8"]]
- 00bc4504 bytes f3620094
+ 00bc45cc bytes ed620094
- 00bc4524 ["COPY", "register:4040:8", ["const:c17000:8"]]
+ 00bc45ec ["COPY", "register:4040:8", ["const:c18000:8"]]
- 00bc4524 bytes 880200f0
+ 00bc45ec bytes a8020090
- 00bc4528 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00bc4528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc4528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc4528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc45f0 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 00bc45f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc45f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc45f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc4528 bytes 08613f91
+ 00bc45f0 bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-013a4f8769fab43798c0f71c8481150f"></a>

### [`00bc4584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc4584.md) → [`00bc464c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc464c.md) FUN_00bc464c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc46bc",
      "incomplete_value": false,
      "site": "00bc46bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc45f4",
      "incomplete_value": false,
      "site": "00bc45f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:48:8"
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
      "00bc46bc",
      "DATA",
      [
        "storage",
        "00c18048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc46bc",
      "DATA",
      [
        "storage",
        "00c180f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc45c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc4584.md#insn-00bc45c4) · [`00bc45e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc4584.md#insn-00bc45e8) · [`00bc4640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc4584.md#insn-00bc4640)
- 新版 `00bc468c`（命令位置の公開資料なし） · `00bc46b0`（命令位置の公開資料なし） · `00bc4708`（命令位置の公開資料なし）

~~~diff
- 00bc45c4 ["INT_ADD", "register:40f0:8", ["const:bc45c4:8", "const:4:8"]]
- 00bc45c4 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc468c ["INT_ADD", "register:40f0:8", ["const:bc468c:8", "const:4:8"]]
+ 00bc468c ["CALL", null, ["callee:00bdd180:8"]]
- 00bc45c4 bytes c3620094
+ 00bc468c bytes bd620094
- 00bc45e8 ["COPY", "tmp:0:8", ["const:48:8"]]
- 00bc45e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc45e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc45e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc46b0 ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 00bc46b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc46b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc46b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc45e8 bytes 08210191
+ 00bc46b0 bytes 08e10391
- 00bc4640 ["INT_ADD", "register:40f0:8", ["const:bc4640:8", "const:4:8"]]
- 00bc4640 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc4708 ["INT_ADD", "register:40f0:8", ["const:bc4708:8", "const:4:8"]]
+ 00bc4708 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc4640 bytes a45a0094
+ 00bc4708 bytes 9e5a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecb57c5ae7e820c21f07abac2a64ad98"></a>

### [`00bc4644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc4644.md) → [`00bc470c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc470c.md) FUN_00bc470c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc4780",
      "incomplete_value": false,
      "site": "00bc4780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc46b8",
      "incomplete_value": false,
      "site": "00bc46b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:b8:8"
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
      "00bc4780",
      "DATA",
      [
        "storage",
        "00c180b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc4780",
      "DATA",
      [
        "storage",
        "00c18168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc4644.md#insn-00bc4688) · [`00bc46ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc4644.md#insn-00bc46ac) · [`00bc4708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc4644.md#insn-00bc4708)
- 新版 `00bc4750`（命令位置の公開資料なし） · `00bc4774`（命令位置の公開資料なし） · `00bc47d0`（命令位置の公開資料なし）

~~~diff
- 00bc4688 ["INT_ADD", "register:40f0:8", ["const:bc4688:8", "const:4:8"]]
- 00bc4688 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc4750 ["INT_ADD", "register:40f0:8", ["const:bc4750:8", "const:4:8"]]
+ 00bc4750 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc4688 bytes 92620094
+ 00bc4750 bytes 8c620094
- 00bc46ac ["COPY", "tmp:0:8", ["const:b8:8"]]
- 00bc46ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc46ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc46ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc4774 ["COPY", "tmp:0:8", ["const:168:8"]]
+ 00bc4774 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc4774 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc4774 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc46ac bytes 08e10291
+ 00bc4774 bytes 08a10591
- 00bc4708 ["INT_ADD", "register:40f0:8", ["const:bc4708:8", "const:4:8"]]
- 00bc4708 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc47d0 ["INT_ADD", "register:40f0:8", ["const:bc47d0:8", "const:4:8"]]
+ 00bc47d0 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc4708 bytes 725a0094
+ 00bc47d0 bytes 6c5a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe0b816124b982a7262de3d48b2f1aeb"></a>

### [`00bc47d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc47d4.md) → [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) FUN_00bc489c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbf9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 12件 [`00bbd19c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd19c.md) [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bc92bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc92bc.md) [`00bc93b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc93b0.md)
- 新版 呼出元 2件 [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 12件 [`00bbd264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd264.md) [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc9384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9384.md) [`00bc9478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9478.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.04% / 新版 97.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc4efc",
      "incomplete_value": false,
      "site": "00bc4efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc4e34",
      "incomplete_value": false,
      "site": "00bc4e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
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
      "definition_site": "00bc5178",
      "incomplete_value": false,
      "site": "00bc5178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc50b0",
      "incomplete_value": false,
      "site": "00bc50b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc48fc",
      "DATA",
      [
        "storage",
        "002fcc64",
        "switchD_00bc483c::switchdataD_002fcc64",
        "ushort"
      ]
    ],
    [
      "00bc4a34",
      "PARAM",
      [
        "storage",
        "0029ce31",
        null,
        "string"
      ]
    ],
    [
      "00bc4a4c",
      "PARAM",
      [
        "storage",
        "0029c1d7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bc48fc",
      "DATA",
      [
        "storage",
        "002fcc64",
        "switchD_00bc4904::switchdataD_002fcc64",
        "ushort"
      ]
    ],
    [
      "00bc4a34",
      "PARAM",
      [
        "storage",
        "0029cebe",
        null,
        "string"
      ]
    ],
    [
      "00bc4a4c",
      "PARAM",
      [
        "storage",
        "0029c264",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc4830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc47d4.md#insn-00bc4830) · [`00bc4848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc47d4.md#insn-00bc4848) · [`00bc487c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc47d4.md#insn-00bc487c)
- 新版 `00bc48f8`（命令位置の公開資料なし） · `00bc4910`（命令位置の公開資料なし） · `00bc4944`（命令位置の公開資料なし）

~~~diff
- 00bc4830 ["COPY", "register:4078:8", ["const:bc4840:8"]]
+ 00bc48f8 ["COPY", "register:4078:8", ["const:bc4908:8"]]
- 00bc4830 bytes 8f000010
+ 00bc48f8 bytes 8f000010
- 00bc4848 ["INT_ADD", "register:40f0:8", ["const:bc4848:8", "const:4:8"]]
- 00bc4848 ["CALL", null, ["callee:00bbde18:8"]]
+ 00bc4910 ["INT_ADD", "register:40f0:8", ["const:bc4910:8", "const:4:8"]]
+ 00bc4910 ["CALL", null, ["callee:00bbde18:8"]]
- 00bc4848 bytes 42e5ff97
+ 00bc4910 bytes 42e5ff97
- 00bc487c ["INT_ADD", "register:40f0:8", ["const:bc487c:8", "const:4:8"]]
- 00bc487c ["CALL", null, ["callee:00bc9520:8"]]
+ 00bc4944 ["INT_ADD", "register:40f0:8", ["const:bc4944:8", "const:4:8"]]
+ 00bc4944 ["CALL", null, ["callee:00bc9520:8"]]
- 00bc487c bytes f7120094
+ 00bc4944 bytes f7120094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05ff19265677b31ced8e42c377a05b39"></a>

### [`00bc5154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5154.md) → [`00bc521c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc521c.md) FUN_00bc521c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 3件 [`00bcc5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc5e0.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 3件 [`00bcc6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc6a8.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.33% / 新版 98.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc5448",
      "incomplete_value": false,
      "site": "00bc5448",
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
      "definition_site": "00bc5380",
      "incomplete_value": false,
      "site": "00bc5380",
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
      "definition_site": "00bc5520",
      "incomplete_value": false,
      "site": "00bc5520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5458",
      "incomplete_value": false,
      "site": "00bc5458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "00bc5448",
      "DATA",
      [
        "storage",
        "00c17798",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5520",
      "DATA",
      [
        "storage",
        "00c18908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc5448",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5520",
      "DATA",
      [
        "storage",
        "00c189b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5154.md#insn-00bc5350) · [`00bc5374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5154.md#insn-00bc5374) · [`00bc5428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5154.md#insn-00bc5428)
- 新版 `00bc5418`（命令位置の公開資料なし） · `00bc543c`（命令位置の公開資料なし） · `00bc54f0`（命令位置の公開資料なし）

~~~diff
- 00bc5350 ["INT_ADD", "register:40f0:8", ["const:bc5350:8", "const:4:8"]]
- 00bc5350 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc5418 ["INT_ADD", "register:40f0:8", ["const:bc5418:8", "const:4:8"]]
+ 00bc5418 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc5350 bytes 605f0094
+ 00bc5418 bytes 5a5f0094
- 00bc5374 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bc5374 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bc5374 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bc5374 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bc543c ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bc543c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc543c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc543c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bc5374 bytes 4a611e91
+ 00bc543c bytes 4a212191
- 00bc5428 ["INT_ADD", "register:40f0:8", ["const:bc5428:8", "const:4:8"]]
- 00bc5428 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc54f0 ["INT_ADD", "register:40f0:8", ["const:bc54f0:8", "const:4:8"]]
+ 00bc54f0 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc5428 bytes 2a5f0094
+ 00bc54f0 bytes 245f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8323dfc4f0442102121141a394a26572"></a>

### [`00bc5510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5510.md) → [`00bc55d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc55d8.md) FUN_00bc55d8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) [`00bc5510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5510.md) · 呼出先 5件 [`00bc1034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1034.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) [`00bc5510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5510.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 2件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bc55d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc55d8.md) · 呼出先 5件 [`00bc10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bc55d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc55d8.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc56a0",
      "incomplete_value": false,
      "site": "00bc56a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc55d8",
      "incomplete_value": false,
      "site": "00bc55d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "00bc5750",
      "incomplete_value": true,
      "site": "00bc5750",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5688",
      "incomplete_value": true,
      "site": "00bc5688",
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
            "const:a58:8"
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
      "definition_site": "00bc5800",
      "incomplete_value": false,
      "site": "00bc5800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5738",
      "incomplete_value": false,
      "site": "00bc5738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "00bc56a0",
      "DATA",
      [
        "storage",
        "00c18a58",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5750",
      "DATA",
      [
        "storage",
        "00c18a58",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5800",
      "DATA",
      [
        "storage",
        "00c18ac8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc56a0",
      "DATA",
      [
        "storage",
        "00c18b08",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5750",
      "DATA",
      [
        "storage",
        "00c18b08",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5800",
      "DATA",
      [
        "storage",
        "00c18b78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5510.md#insn-00bc5570) · [`00bc5580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5510.md#insn-00bc5580) · [`00bc55a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5510.md#insn-00bc55a8)
- 新版 `00bc5638`（命令位置の公開資料なし） · `00bc5648`（命令位置の公開資料なし） · `00bc5670`（命令位置の公開資料なし）

~~~diff
- 00bc5570 ["INT_ADD", "register:40f0:8", ["const:bc5570:8", "const:4:8"]]
- 00bc5570 ["CALL", null, ["callee:00bc10fc:8"]]
+ 00bc5638 ["INT_ADD", "register:40f0:8", ["const:bc5638:8", "const:4:8"]]
+ 00bc5638 ["CALL", null, ["callee:00bc10fc:8"]]
- 00bc5570 bytes b1eeff97
+ 00bc5638 bytes b1eeff97
- 00bc5580 ["INT_ADD", "register:40f0:8", ["const:bc5580:8", "const:4:8"]]
- 00bc5580 ["CALL", null, ["local:b0:8"]]
+ 00bc5648 ["INT_ADD", "register:40f0:8", ["const:bc5648:8", "const:4:8"]]
+ 00bc5648 ["CALL", null, ["local:b0:8"]]
- 00bc5580 bytes e4ffff97
+ 00bc5648 bytes e4ffff97
- 00bc55a8 ["INT_ADD", "register:40f0:8", ["const:bc55a8:8", "const:4:8"]]
- 00bc55a8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc5670 ["INT_ADD", "register:40f0:8", ["const:bc5670:8", "const:4:8"]]
+ 00bc5670 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc55a8 bytes ca5e0094
+ 00bc5670 bytes c45e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23b7752d21ce8ebe65ca2c57ea4a500e"></a>

### [`00bc5778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5778.md) → [`00bc5840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5840.md) FUN_00bc5840

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc58a4",
      "incomplete_value": false,
      "site": "00bc58a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc57dc",
      "incomplete_value": false,
      "site": "00bc57dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:b38:8"
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
      "00bc58a4",
      "DATA",
      [
        "storage",
        "00c18b38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc58a4",
      "DATA",
      [
        "storage",
        "00c18be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc57ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5778.md#insn-00bc57ac) · [`00bc57d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5778.md#insn-00bc57d0) · [`00bc5818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5778.md#insn-00bc5818)
- 新版 `00bc5874`（命令位置の公開資料なし） · `00bc5898`（命令位置の公開資料なし） · `00bc58e0`（命令位置の公開資料なし）

~~~diff
- 00bc57ac ["INT_ADD", "register:40f0:8", ["const:bc57ac:8", "const:4:8"]]
- 00bc57ac ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc5874 ["INT_ADD", "register:40f0:8", ["const:bc5874:8", "const:4:8"]]
+ 00bc5874 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc57ac bytes 495e0094
+ 00bc5874 bytes 435e0094
- 00bc57d0 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 00bc57d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc57d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc57d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc5898 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00bc5898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc5898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc5898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc57d0 bytes 08e12c91
+ 00bc5898 bytes 08a12f91
- 00bc5818 ["INT_ADD", "register:40f0:8", ["const:bc5818:8", "const:4:8"]]
- 00bc5818 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc58e0 ["INT_ADD", "register:40f0:8", ["const:bc58e0:8", "const:4:8"]]
+ 00bc58e0 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc5818 bytes 2e560094
+ 00bc58e0 bytes 28560094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87789defe86b7d77f5fb939e843a4ec5"></a>

### [`00bc581c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc581c.md) → [`00bc58e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc58e4.md) FUN_00bc58e4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 4件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 4件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc5a00",
      "incomplete_value": false,
      "site": "00bc5a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5938",
      "incomplete_value": false,
      "site": "00bc5938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "00bc5a00",
      "DATA",
      [
        "storage",
        "00c18ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc5a00",
      "DATA",
      [
        "storage",
        "00c18c58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc581c.md#insn-00bc5838) · [`00bc5848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc581c.md#insn-00bc5848) · [`00bc5904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc581c.md#insn-00bc5904)
- 新版 `00bc5900`（命令位置の公開資料なし） · `00bc5910`（命令位置の公開資料なし） · `00bc59cc`（命令位置の公開資料なし）

~~~diff
- 00bc5838 ["INT_ADD", "register:40f0:8", ["const:bc5838:8", "const:4:8"]]
- 00bc5838 ["CALL", null, ["callee:00bbde18:8"]]
+ 00bc5900 ["INT_ADD", "register:40f0:8", ["const:bc5900:8", "const:4:8"]]
+ 00bc5900 ["CALL", null, ["callee:00bbde18:8"]]
- 00bc5838 bytes 46e1ff97
+ 00bc5900 bytes 46e1ff97
- 00bc5848 ["INT_ADD", "register:40f0:8", ["const:bc5848:8", "const:4:8"]]
- 00bc5848 ["CALL", null, ["callee:00bc2ec8:8"]]
+ 00bc5910 ["INT_ADD", "register:40f0:8", ["const:bc5910:8", "const:4:8"]]
+ 00bc5910 ["CALL", null, ["callee:00bc2ec8:8"]]
- 00bc5848 bytes 6ef5ff97
+ 00bc5910 bytes 6ef5ff97
- 00bc5904 ["INT_ADD", "register:40f0:8", ["const:bc5904:8", "const:4:8"]]
- 00bc5904 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc59cc ["INT_ADD", "register:40f0:8", ["const:bc59cc:8", "const:4:8"]]
+ 00bc59cc ["CALL", null, ["callee:00bdd180:8"]]
- 00bc5904 bytes f35d0094
+ 00bc59cc bytes ed5d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9e448c56856022ac6f1df51ebf59d65"></a>

### [`00bc5984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5984.md) → [`00bc5a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5a4c.md) FUN_00bc5a4c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc5ab4",
      "incomplete_value": false,
      "site": "00bc5ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc59ec",
      "incomplete_value": false,
      "site": "00bc59ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "definition_site": "00bc5ae0",
      "incomplete_value": false,
      "site": "00bc5ae0",
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
            "const:241:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5a18",
      "incomplete_value": false,
      "site": "00bc5a18",
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
            "const:248:8"
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
      "00bc5ab4",
      "DATA",
      [
        "storage",
        "00c18198",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5ae0",
      "DATA",
      [
        "storage",
        "002a7248",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc5ab4",
      "DATA",
      [
        "storage",
        "00c18248",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5ae0",
      "DATA",
      [
        "storage",
        "002a7241",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc59bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5984.md#insn-00bc59bc) · [`00bc59e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5984.md#insn-00bc59e0) · [`00bc5a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5984.md#insn-00bc5a00)
- 新版 `00bc5a84`（命令位置の公開資料なし） · `00bc5aa8`（命令位置の公開資料なし） · `00bc5ac8`（命令位置の公開資料なし）

~~~diff
- 00bc59bc ["INT_ADD", "register:40f0:8", ["const:bc59bc:8", "const:4:8"]]
- 00bc59bc ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc5a84 ["INT_ADD", "register:40f0:8", ["const:bc5a84:8", "const:4:8"]]
+ 00bc5a84 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc59bc bytes c55d0094
+ 00bc5a84 bytes bf5d0094
- 00bc59e0 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00bc59e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc59e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc59e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc5aa8 ["COPY", "tmp:0:8", ["const:248:8"]]
+ 00bc5aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc5aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc5aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc59e0 bytes 08610691
+ 00bc5aa8 bytes 08210991
- 00bc5a00 ["COPY", "tmp:0:8", ["const:248:8"]]
- 00bc5a00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc5a00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc5a00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc5ac8 ["COPY", "tmp:0:8", ["const:241:8"]]
+ 00bc5ac8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc5ac8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc5ac8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc5a00 bytes 29210991
+ 00bc5ac8 bytes 29050991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8db5dd27a2ba462ffebf9aae0d022d65"></a>

### [`00bc5a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5a44.md) → [`00bc5b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5b0c.md) FUN_00bc5b0c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 9件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bbfe64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 9件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc5f9c",
      "incomplete_value": false,
      "site": "00bc5f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc5ed4",
      "incomplete_value": false,
      "site": "00bc5ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "00bc5df8",
      "DATA",
      [
        "storage",
        "00c18c18",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5e8c",
      "DATA",
      [
        "storage",
        "00c18c88",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5e8c",
      "DATA",
      [
        "storage",
        "00c18cf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc5df8",
      "DATA",
      [
        "storage",
        "00c18cc8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5e8c",
      "DATA",
      [
        "storage",
        "00c18d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc5e8c",
      "DATA",
      [
        "storage",
        "00c18da8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc5ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5a44.md#insn-00bc5ae0) · [`00bc5b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5a44.md#insn-00bc5b28) · [`00bc5b58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5a44.md#insn-00bc5b58)
- 新版 `00bc5ba8`（命令位置の公開資料なし） · `00bc5bf0`（命令位置の公開資料なし） · `00bc5c20`（命令位置の公開資料なし）

~~~diff
- 00bc5ae0 ["INT_ADD", "register:40f0:8", ["const:bc5ae0:8", "const:4:8"]]
- 00bc5ae0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bc5ba8 ["INT_ADD", "register:40f0:8", ["const:bc5ba8:8", "const:4:8"]]
+ 00bc5ba8 ["CALL", null, ["callee:00bdd200:8"]]
- 00bc5ae0 bytes 9c5d0094
+ 00bc5ba8 bytes 965d0094
- 00bc5b28 ["INT_ADD", "register:40f0:8", ["const:bc5b28:8", "const:4:8"]]
- 00bc5b28 ["CALL", null, ["callee:00bbde18:8"]]
+ 00bc5bf0 ["INT_ADD", "register:40f0:8", ["const:bc5bf0:8", "const:4:8"]]
+ 00bc5bf0 ["CALL", null, ["callee:00bbde18:8"]]
- 00bc5b28 bytes 8ae0ff97
+ 00bc5bf0 bytes 8ae0ff97
- 00bc5b58 ["INT_ADD", "register:40f0:8", ["const:bc5b58:8", "const:4:8"]]
- 00bc5b58 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc5c20 ["INT_ADD", "register:40f0:8", ["const:bc5c20:8", "const:4:8"]]
+ 00bc5c20 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc5b58 bytes 5e5d0094
+ 00bc5c20 bytes 585d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc41b07ef895fcee90f73e79313a30cd"></a>

### [`00bc5f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5f14.md) → [`00bc5fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5fdc.md) FUN_00bc5fdc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 8件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbfe64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 8件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc62c0",
      "incomplete_value": false,
      "site": "00bc62c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc61f8",
      "incomplete_value": false,
      "site": "00bc61f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc60e8",
      "DATA",
      [
        "storage",
        "00c17798",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc62c0",
      "DATA",
      [
        "storage",
        "00c18dd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc60e8",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc62c0",
      "DATA",
      [
        "storage",
        "00c18e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5f14.md#insn-00bc6130) · [`00bc5f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5f14.md#insn-00bc5f3c) · [`00bc5f4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5f14.md#insn-00bc5f4c)
- 新版 `00bc61f8`（命令位置の公開資料なし） · `00bc6004`（命令位置の公開資料なし） · `00bc6014`（命令位置の公開資料なし）

~~~diff
- 00bc6130 ["INT_ADD", "register:40f0:8", ["const:bc6130:8", "const:4:8"]]
- 00bc6130 ["CALL", null, ["callee:00bdb160:8"]]
+ 00bc61f8 ["INT_ADD", "register:40f0:8", ["const:bc61f8:8", "const:4:8"]]
+ 00bc61f8 ["CALL", null, ["callee:00bdb160:8"]]
- 00bc6130 bytes e0530094
+ 00bc61f8 bytes da530094
- 00bc5f3c ["INT_ADD", "register:40f0:8", ["const:bc5f3c:8", "const:4:8"]]
- 00bc5f3c ["CALL", null, ["callee:00bbde18:8"]]
+ 00bc6004 ["INT_ADD", "register:40f0:8", ["const:bc6004:8", "const:4:8"]]
+ 00bc6004 ["CALL", null, ["callee:00bbde18:8"]]
- 00bc5f3c bytes 85dfff97
+ 00bc6004 bytes 85dfff97
- 00bc5f4c ["INT_ADD", "register:40f0:8", ["const:bc5f4c:8", "const:4:8"]]
- 00bc5f4c ["CALL", null, ["callee:00bc2ec8:8"]]
+ 00bc6014 ["INT_ADD", "register:40f0:8", ["const:bc6014:8", "const:4:8"]]
+ 00bc6014 ["CALL", null, ["callee:00bc2ec8:8"]]
- 00bc5f4c bytes adf3ff97
+ 00bc6014 bytes adf3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3fed087d5b103207d1decb7cce546e1"></a>

### [`00bc6308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6308.md) → [`00bc63d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc63d0.md) FUN_00bc63d0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc6434",
      "incomplete_value": false,
      "site": "00bc6434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc636c",
      "incomplete_value": false,
      "site": "00bc636c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "00bc6434",
      "DATA",
      [
        "storage",
        "00c18e48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc6434",
      "DATA",
      [
        "storage",
        "00c18ef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc633c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6308.md#insn-00bc633c) · [`00bc6360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6308.md#insn-00bc6360) · [`00bc63a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6308.md#insn-00bc63a4)
- 新版 `00bc6404`（命令位置の公開資料なし） · `00bc6428`（命令位置の公開資料なし） · `00bc646c`（命令位置の公開資料なし）

~~~diff
- 00bc633c ["INT_ADD", "register:40f0:8", ["const:bc633c:8", "const:4:8"]]
- 00bc633c ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc6404 ["INT_ADD", "register:40f0:8", ["const:bc6404:8", "const:4:8"]]
+ 00bc6404 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc633c bytes 655b0094
+ 00bc6404 bytes 5f5b0094
- 00bc6360 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00bc6360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc6428 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 00bc6428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc6428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc6428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc6360 bytes 08213991
+ 00bc6428 bytes 08e13b91
- 00bc63a4 ["INT_ADD", "register:40f0:8", ["const:bc63a4:8", "const:4:8"]]
- 00bc63a4 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc646c ["INT_ADD", "register:40f0:8", ["const:bc646c:8", "const:4:8"]]
+ 00bc646c ["CALL", null, ["callee:00bdb180:8"]]
- 00bc63a4 bytes 4b530094
+ 00bc646c bytes 45530094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5318e0a51e89ab6674b7b496d967d04b"></a>

### [`00bc63a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc63a8.md) → [`00bc6470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6470.md) FUN_00bc6470

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc64d8",
      "incomplete_value": false,
      "site": "00bc64d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6410",
      "incomplete_value": false,
      "site": "00bc6410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "definition_site": "00bc64f0",
      "incomplete_value": false,
      "site": "00bc64f0",
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
            "const:1eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6428",
      "incomplete_value": false,
      "site": "00bc6428",
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
            "const:15e:8"
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
      "00bc64d8",
      "DATA",
      [
        "storage",
        "00c18198",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc64f0",
      "DATA",
      [
        "storage",
        "0029d15e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc64d8",
      "DATA",
      [
        "storage",
        "00c18248",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc64f0",
      "DATA",
      [
        "storage",
        "0029d1eb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc63dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc63a8.md#insn-00bc63dc) · [`00bc6400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc63a8.md#insn-00bc6400) · [`00bc6408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc63a8.md#insn-00bc6408)
- 新版 `00bc64a4`（命令位置の公開資料なし） · `00bc64c8`（命令位置の公開資料なし）

~~~diff
- 00bc63dc ["INT_ADD", "register:40f0:8", ["const:bc63dc:8", "const:4:8"]]
- 00bc63dc ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc64a4 ["INT_ADD", "register:40f0:8", ["const:bc64a4:8", "const:4:8"]]
+ 00bc64a4 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc63dc bytes 3d5b0094
+ 00bc64a4 bytes 375b0094
- 00bc6400 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00bc6400 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6400 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6400 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc64c8 ["COPY", "tmp:0:8", ["const:248:8"]]
+ 00bc64c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc64c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc64c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc6400 bytes 08610691
+ 00bc64c8 bytes 08210991
- 00bc6408 ["COPY", "register:4048:8", ["const:29d000:8"]]
- 00bc6408 bytes a9b6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5494936bd6d5ac163b7e532626393c9f"></a>

### [`00bc64f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc64f8.md) → [`00bc65c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc65c0.md) FUN_00bc65c0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc6628",
      "incomplete_value": false,
      "site": "00bc6628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6560",
      "incomplete_value": false,
      "site": "00bc6560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:b38:8"
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
      "00bc6628",
      "DATA",
      [
        "storage",
        "00c18b38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc6628",
      "DATA",
      [
        "storage",
        "00c18be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc64f8.md#insn-00bc6530) · [`00bc6554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc64f8.md#insn-00bc6554) · [`00bc65a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc64f8.md#insn-00bc65a0)
- 新版 `00bc65f8`（命令位置の公開資料なし） · `00bc661c`（命令位置の公開資料なし） · `00bc6668`（命令位置の公開資料なし）

~~~diff
- 00bc6530 ["INT_ADD", "register:40f0:8", ["const:bc6530:8", "const:4:8"]]
- 00bc6530 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc65f8 ["INT_ADD", "register:40f0:8", ["const:bc65f8:8", "const:4:8"]]
+ 00bc65f8 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc6530 bytes e85a0094
+ 00bc65f8 bytes e25a0094
- 00bc6554 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 00bc6554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc661c ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00bc661c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc661c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc661c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc6554 bytes 08e12c91
+ 00bc661c bytes 08a12f91
- 00bc65a0 ["INT_ADD", "register:40f0:8", ["const:bc65a0:8", "const:4:8"]]
- 00bc65a0 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc6668 ["INT_ADD", "register:40f0:8", ["const:bc6668:8", "const:4:8"]]
+ 00bc6668 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc65a0 bytes cc520094
+ 00bc6668 bytes c6520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3fa5e81c3097e106a0d2913c14e0456"></a>

### [`00bc65a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc65a4.md) → [`00bc666c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc666c.md) FUN_00bc666c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc66d8",
      "incomplete_value": false,
      "site": "00bc66d8",
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
      "definition_site": "00bc6610",
      "incomplete_value": false,
      "site": "00bc6610",
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
      "00bc66d8",
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
      "00bc66d8",
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

- 旧版 [`00bc65d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc65a4.md#insn-00bc65d8) · [`00bc6600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc65a4.md#insn-00bc6600) · [`00bc6608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc65a4.md#insn-00bc6608)
- 新版 `00bc66a0`（命令位置の公開資料なし） · `00bc66c8`（命令位置の公開資料なし） · `00bc66d0`（命令位置の公開資料なし）

~~~diff
- 00bc65d8 ["INT_ADD", "register:40f0:8", ["const:bc65d8:8", "const:4:8"]]
- 00bc65d8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc66a0 ["INT_ADD", "register:40f0:8", ["const:bc66a0:8", "const:4:8"]]
+ 00bc66a0 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc65d8 bytes be5a0094
+ 00bc66a0 bytes b85a0094
- 00bc6600 ["INT_ADD", "register:40f0:8", ["const:bc6600:8", "const:4:8"]]
- 00bc6600 ["CALL", null, ["callee:00bdb140:8"]]
+ 00bc66c8 ["INT_ADD", "register:40f0:8", ["const:bc66c8:8", "const:4:8"]]
+ 00bc66c8 ["CALL", null, ["callee:00bdb140:8"]]
- 00bc6600 bytes a4520094
+ 00bc66c8 bytes 9e520094
- 00bc6608 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bc6608 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc6608 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc6608 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc66d0 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bc66d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc66d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc66d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc6608 bytes 29611e91
+ 00bc66d0 bytes 29212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24aae07e8c7790585335abf42f3ff6c5"></a>

### [`00bc6650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6650.md) → [`00bc6718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6718.md) FUN_00bc6718

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc677c",
      "incomplete_value": true,
      "site": "00bc677c",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc66b4",
      "incomplete_value": true,
      "site": "00bc66b4",
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
      "00bc677c",
      "DATA",
      [
        "storage",
        "00c18f28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc677c",
      "DATA",
      [
        "storage",
        "00c18fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6650.md#insn-00bc6684) · [`00bc66a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6650.md#insn-00bc66a8) · [`00bc66ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6650.md#insn-00bc66ec)
- 新版 `00bc674c`（命令位置の公開資料なし） · `00bc6770`（命令位置の公開資料なし） · `00bc67b4`（命令位置の公開資料なし）

~~~diff
- 00bc6684 ["INT_ADD", "register:40f0:8", ["const:bc6684:8", "const:4:8"]]
- 00bc6684 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc674c ["INT_ADD", "register:40f0:8", ["const:bc674c:8", "const:4:8"]]
+ 00bc674c ["CALL", null, ["callee:00bdd180:8"]]
- 00bc6684 bytes 935a0094
+ 00bc674c bytes 8d5a0094
- 00bc66a8 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 00bc66a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc66a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc66a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc6770 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 00bc6770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc6770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc6770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc66a8 bytes 08a13c91
+ 00bc6770 bytes 08613f91
- 00bc66ec ["INT_ADD", "register:40f0:8", ["const:bc66ec:8", "const:4:8"]]
- 00bc66ec ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc67b4 ["INT_ADD", "register:40f0:8", ["const:bc67b4:8", "const:4:8"]]
+ 00bc67b4 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc66ec bytes 79520094
+ 00bc67b4 bytes 73520094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b11ae546da5a48c739ddc14bb052c04"></a>

### [`00bc66f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc66f0.md) → [`00bc67b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md) FUN_00bc67b8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 7件 [`00bc1034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1034.md) [`00bc1648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1648.md) [`00bc1b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1b18.md) [`00bce6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce6ac.md) [`00bce830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce830.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 7件 [`00bc10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md) [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) [`00bc1be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1be0.md) [`00bce774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) [`00bce8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc688c",
      "incomplete_value": false,
      "site": "00bc688c",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc67c4",
      "incomplete_value": false,
      "site": "00bc67c4",
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
            "const:158:8"
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
      "definition_site": "00bc6b8c",
      "incomplete_value": false,
      "site": "00bc6b8c",
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
      "definition_site": "00bc6ac4",
      "incomplete_value": false,
      "site": "00bc6ac4",
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
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc6c5c",
      "incomplete_value": false,
      "site": "00bc6c5c",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6b94",
      "incomplete_value": false,
      "site": "00bc6b94",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "ordinal": 71,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc688c",
      "DATA",
      [
        "storage",
        "00c19158",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc69c0",
      "DATA",
      [
        "storage",
        "00c19698",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc6a04",
      "DATA",
      [
        "storage",
        "00c18f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc688c",
      "DATA",
      [
        "storage",
        "00c19208",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc69c0",
      "DATA",
      [
        "storage",
        "00c19748",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc6a04",
      "DATA",
      [
        "storage",
        "00c19048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc66f0.md#insn-00bc6768) · [`00bc6790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc66f0.md#insn-00bc6790) · [`00bc67b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc66f0.md#insn-00bc67b8)
- 新版 `00bc6830`（命令位置の公開資料なし） · `00bc6858`（命令位置の公開資料なし） · `00bc6880`（命令位置の公開資料なし）

~~~diff
- 00bc6768 ["INT_ADD", "register:40f0:8", ["const:bc6768:8", "const:4:8"]]
- 00bc6768 ["CALL", null, ["callee:00bce8f8:8"]]
+ 00bc6830 ["INT_ADD", "register:40f0:8", ["const:bc6830:8", "const:4:8"]]
+ 00bc6830 ["CALL", null, ["callee:00bce8f8:8"]]
- 00bc6768 bytes 32200094
+ 00bc6830 bytes 32200094
- 00bc6790 ["INT_ADD", "register:40f0:8", ["const:bc6790:8", "const:4:8"]]
- 00bc6790 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc6858 ["INT_ADD", "register:40f0:8", ["const:bc6858:8", "const:4:8"]]
+ 00bc6858 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc6790 bytes 505a0094
+ 00bc6858 bytes 4a5a0094
- 00bc67b8 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00bc67b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bc67b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bc67b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bc6880 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 00bc6880 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc6880 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bc6880 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bc67b8 bytes 4a610591
+ 00bc6880 bytes 4a210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a66b3e32535b0458056782ee5197cfa"></a>

### [`00bc6d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6d64.md) → [`00bc6e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc6e2c.md) FUN_00bc6e2c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc6ea0",
      "incomplete_value": false,
      "site": "00bc6ea0",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc6dd8",
      "incomplete_value": false,
      "site": "00bc6dd8",
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
            "const:cc8:8"
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
      "00bc6ea0",
      "DATA",
      [
        "storage",
        "00c17cc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc6ea0",
      "DATA",
      [
        "storage",
        "00c17d78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc6da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6d64.md#insn-00bc6da8) · [`00bc6dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6d64.md#insn-00bc6dcc) · [`00bc6e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc6d64.md#insn-00bc6e2c)
- 新版 `00bc6e70`（命令位置の公開資料なし） · `00bc6e94`（命令位置の公開資料なし） · `00bc6ef4`（命令位置の公開資料なし）

~~~diff
- 00bc6da8 ["INT_ADD", "register:40f0:8", ["const:bc6da8:8", "const:4:8"]]
- 00bc6da8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc6e70 ["INT_ADD", "register:40f0:8", ["const:bc6e70:8", "const:4:8"]]
+ 00bc6e70 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc6da8 bytes ca580094
+ 00bc6e70 bytes c4580094
- 00bc6dcc ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00bc6dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc6dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc6e94 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00bc6e94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc6e94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc6e94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc6dcc bytes 08213391
+ 00bc6e94 bytes 08e13591
- 00bc6e2c ["INT_ADD", "register:40f0:8", ["const:bc6e2c:8", "const:4:8"]]
- 00bc6e2c ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc6ef4 ["INT_ADD", "register:40f0:8", ["const:bc6ef4:8", "const:4:8"]]
+ 00bc6ef4 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc6e2c bytes a9500094
+ 00bc6ef4 bytes a3500094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-563e8cc8eec843d1113898287d8d1c85"></a>

### [`00bc7344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7344.md) → [`00bc740c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc7/00bc740c.md) FUN_00bc740c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc747c",
      "incomplete_value": false,
      "site": "00bc747c",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc73b4",
      "incomplete_value": false,
      "site": "00bc73b4",
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
            "const:d38:8"
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
      "00bc747c",
      "DATA",
      [
        "storage",
        "00c17d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc747c",
      "DATA",
      [
        "storage",
        "00c17de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc7384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7344.md#insn-00bc7384) · [`00bc73a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7344.md#insn-00bc73a8) · [`00bc7400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc7/00bc7344.md#insn-00bc7400)
- 新版 `00bc744c`（命令位置の公開資料なし） · `00bc7470`（命令位置の公開資料なし） · `00bc74c8`（命令位置の公開資料なし）

~~~diff
- 00bc7384 ["INT_ADD", "register:40f0:8", ["const:bc7384:8", "const:4:8"]]
- 00bc7384 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc744c ["INT_ADD", "register:40f0:8", ["const:bc744c:8", "const:4:8"]]
+ 00bc744c ["CALL", null, ["callee:00bdd180:8"]]
- 00bc7384 bytes 53570094
+ 00bc744c bytes 4d570094
- 00bc73a8 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00bc73a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc73a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc73a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc7470 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00bc7470 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc7470 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc7470 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc73a8 bytes 08e13491
+ 00bc7470 bytes 08a13791
- 00bc7400 ["INT_ADD", "register:40f0:8", ["const:bc7400:8", "const:4:8"]]
- 00bc7400 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc74c8 ["INT_ADD", "register:40f0:8", ["const:bc74c8:8", "const:4:8"]]
+ 00bc74c8 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc7400 bytes 344f0094
+ 00bc74c8 bytes 2e4f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3f3d8bf704c7246697b61b1b87dcad4"></a>

### [`00bc92bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc92bc.md) → [`00bc9384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9384.md) FUN_00bc9384

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc47d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc47d4.md) · 呼出先 3件 [`00bbdc10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdc10.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 3件 [`00bbdcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdcd8.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc942c",
      "incomplete_value": false,
      "site": "00bc942c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9364",
      "incomplete_value": false,
      "site": "00bc9364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "00bc942c",
      "DATA",
      [
        "storage",
        "00c18208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc942c",
      "DATA",
      [
        "storage",
        "00c182b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc92e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc92bc.md#insn-00bc92e4) · [`00bc932c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc92bc.md#insn-00bc932c) · [`00bc9360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc92bc.md#insn-00bc9360)
- 新版 `00bc93ac`（命令位置の公開資料なし） · `00bc93f4`（命令位置の公開資料なし） · `00bc9428`（命令位置の公開資料なし）

~~~diff
- 00bc92e4 ["INT_ADD", "register:40f0:8", ["const:bc92e4:8", "const:4:8"]]
- 00bc92e4 ["CALL", null, ["callee:00bbdcd8:8"]]
+ 00bc93ac ["INT_ADD", "register:40f0:8", ["const:bc93ac:8", "const:4:8"]]
+ 00bc93ac ["CALL", null, ["callee:00bbdcd8:8"]]
- 00bc92e4 bytes 4bd2ff97
+ 00bc93ac bytes 4bd2ff97
- 00bc932c ["INT_ADD", "register:40f0:8", ["const:bc932c:8", "const:4:8"]]
- 00bc932c ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc93f4 ["INT_ADD", "register:40f0:8", ["const:bc93f4:8", "const:4:8"]]
+ 00bc93f4 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc932c bytes 694f0094
+ 00bc93f4 bytes 634f0094
- 00bc9360 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00bc9360 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc9360 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc9360 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc9428 ["COPY", "tmp:0:8", ["const:2b8:8"]]
+ 00bc9428 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc9428 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc9428 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc9360 bytes 29210891
+ 00bc9428 bytes 29e10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0760e210c6457b309ef8e37b23e9a045"></a>

### [`00bc93b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc93b0.md) → [`00bc9478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9478.md) FUN_00bc9478

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc47d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc47d4.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc94e8",
      "incomplete_value": false,
      "site": "00bc94f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9420",
      "incomplete_value": false,
      "site": "00bc942c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "00bc94f4",
      "DATA",
      [
        "storage",
        "00c18278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc94f4",
      "DATA",
      [
        "storage",
        "00c18328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc93e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc93b0.md#insn-00bc93e4) · [`00bc9420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc93b0.md#insn-00bc9420) · [`00bc9454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc93b0.md#insn-00bc9454)
- 新版 `00bc94ac`（命令位置の公開資料なし） · `00bc94e8`（命令位置の公開資料なし） · `00bc951c`（命令位置の公開資料なし）

~~~diff
- 00bc93e4 ["INT_ADD", "register:40f0:8", ["const:bc93e4:8", "const:4:8"]]
- 00bc93e4 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc94ac ["INT_ADD", "register:40f0:8", ["const:bc94ac:8", "const:4:8"]]
+ 00bc94ac ["CALL", null, ["callee:00bdd180:8"]]
- 00bc93e4 bytes 3b4f0094
+ 00bc94ac bytes 354f0094
- 00bc9420 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00bc9420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc94e8 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00bc94e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc94e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc94e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc9420 bytes 08e10991
+ 00bc94e8 bytes 08a10c91
- 00bc9454 ["INT_ADD", "register:40f0:8", ["const:bc9454:8", "const:4:8"]]
- 00bc9454 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc951c ["INT_ADD", "register:40f0:8", ["const:bc951c:8", "const:4:8"]]
+ 00bc951c ["CALL", null, ["callee:00bdb180:8"]]
- 00bc9454 bytes 1f470094
+ 00bc951c bytes 19470094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48af9074895e5d4628ccf44b4c13db59"></a>

### [`00bc9458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9458.md) → [`00bc9520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9520.md) FUN_00bc9520

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc47d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc47d4.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc9584",
      "incomplete_value": false,
      "site": "00bc9584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc94bc",
      "incomplete_value": false,
      "site": "00bc94bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "00bc9584",
      "DATA",
      [
        "storage",
        "00c18438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc9584",
      "DATA",
      [
        "storage",
        "00c184e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc948c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9458.md#insn-00bc948c) · [`00bc94b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9458.md#insn-00bc94b0) · [`00bc94f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9458.md#insn-00bc94f4)
- 新版 `00bc9554`（命令位置の公開資料なし） · `00bc9578`（命令位置の公開資料なし） · `00bc95bc`（命令位置の公開資料なし）

~~~diff
- 00bc948c ["INT_ADD", "register:40f0:8", ["const:bc948c:8", "const:4:8"]]
- 00bc948c ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc9554 ["INT_ADD", "register:40f0:8", ["const:bc9554:8", "const:4:8"]]
+ 00bc9554 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc948c bytes 114f0094
+ 00bc9554 bytes 0b4f0094
- 00bc94b0 ["COPY", "tmp:0:8", ["const:438:8"]]
- 00bc94b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc94b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc94b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc9578 ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 00bc9578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc94b0 bytes 08e11091
+ 00bc9578 bytes 08a11391
- 00bc94f4 ["INT_ADD", "register:40f0:8", ["const:bc94f4:8", "const:4:8"]]
- 00bc94f4 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc95bc ["INT_ADD", "register:40f0:8", ["const:bc95bc:8", "const:4:8"]]
+ 00bc95bc ["CALL", null, ["callee:00bdb180:8"]]
- 00bc94f4 bytes f7460094
+ 00bc95bc bytes f1460094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae3f1f0988df87a439acfb7c0724cdfd"></a>

### [`00bc94f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc94f8.md) → [`00bc95c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc95c0.md) FUN_00bc95c0

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bc47d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc47d4.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc962c",
      "incomplete_value": false,
      "site": "00bc962c",
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
      "definition_site": "00bc9564",
      "incomplete_value": false,
      "site": "00bc9564",
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
      "00bc962c",
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
      "00bc962c",
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

- 旧版 [`00bc952c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc94f8.md#insn-00bc952c) · [`00bc9554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc94f8.md#insn-00bc9554) · [`00bc955c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc94f8.md#insn-00bc955c)
- 新版 `00bc95f4`（命令位置の公開資料なし） · `00bc961c`（命令位置の公開資料なし） · `00bc9624`（命令位置の公開資料なし）

~~~diff
- 00bc952c ["INT_ADD", "register:40f0:8", ["const:bc952c:8", "const:4:8"]]
- 00bc952c ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc95f4 ["INT_ADD", "register:40f0:8", ["const:bc95f4:8", "const:4:8"]]
+ 00bc95f4 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc952c bytes e94e0094
+ 00bc95f4 bytes e34e0094
- 00bc9554 ["INT_ADD", "register:40f0:8", ["const:bc9554:8", "const:4:8"]]
- 00bc9554 ["CALL", null, ["callee:00bdb140:8"]]
+ 00bc961c ["INT_ADD", "register:40f0:8", ["const:bc961c:8", "const:4:8"]]
+ 00bc961c ["CALL", null, ["callee:00bdb140:8"]]
- 00bc9554 bytes cf460094
+ 00bc961c bytes c9460094
- 00bc955c ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bc955c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bc955c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bc955c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bc9624 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bc9624 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc9624 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bc9624 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bc955c bytes 29611e91
+ 00bc9624 bytes 29212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd317eeec15b17e90ece553a01473c4e"></a>

### [`00bc95a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc95a4.md) → [`00bc966c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc966c.md) FUN_00bc966c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bc2394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2394.md) [`00bc47d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc47d4.md) · 呼出先 14件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbfe64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) [`00bca8b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca8b8.md)
- 新版 呼出元 2件 [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 14件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bca980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca980.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.63% / 新版 97.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc978c",
      "incomplete_value": false,
      "site": "00bc978c",
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
      "definition_site": "00bc96c4",
      "incomplete_value": false,
      "site": "00bc96c4",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc97b4",
      "incomplete_value": false,
      "site": "00bc97b4",
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
            "const:c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc96ec",
      "incomplete_value": false,
      "site": "00bc96ec",
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
            "const:a0:8"
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
      "definition_site": "00bc9940",
      "incomplete_value": false,
      "site": "00bc9940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9878",
      "incomplete_value": false,
      "site": "00bc9878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc978c",
      "DATA",
      [
        "storage",
        "00c17798",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc97b4",
      "DATA",
      [
        "storage",
        "002a80a0",
        null,
        "string"
      ]
    ],
    [
      "00bc9940",
      "DATA",
      [
        "storage",
        "00c184a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc978c",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc97b4",
      "DATA",
      [
        "storage",
        "002a800c",
        null,
        "string"
      ]
    ],
    [
      "00bc9940",
      "DATA",
      [
        "storage",
        "00c18558",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc95a4.md#insn-00bc9cb8) · [`00bc9cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc95a4.md#insn-00bc9cdc) · [`00bc9694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc95a4.md#insn-00bc9694)
- 新版 `00bc9d80`（命令位置の公開資料なし） · `00bc9da4`（命令位置の公開資料なし） · `00bc975c`（命令位置の公開資料なし）

~~~diff
- 00bc9cb8 ["INT_ADD", "register:40f0:8", ["const:bc9cb8:8", "const:4:8"]]
- 00bc9cb8 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bc9d80 ["INT_ADD", "register:40f0:8", ["const:bc9d80:8", "const:4:8"]]
+ 00bc9d80 ["CALL", null, ["callee:00bbb158:8"]]
- 00bc9cb8 bytes f6c4ff97
+ 00bc9d80 bytes f6c4ff97
- 00bc9cdc ["INT_ADD", "register:40f0:8", ["const:bc9cdc:8", "const:4:8"]]
- 00bc9cdc ["CALL", null, ["callee:00bbb158:8"]]
+ 00bc9da4 ["INT_ADD", "register:40f0:8", ["const:bc9da4:8", "const:4:8"]]
+ 00bc9da4 ["CALL", null, ["callee:00bbb158:8"]]
- 00bc9cdc bytes edc4ff97
+ 00bc9da4 bytes edc4ff97
- 00bc9694 ["INT_ADD", "register:40f0:8", ["const:bc9694:8", "const:4:8"]]
- 00bc9694 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc975c ["INT_ADD", "register:40f0:8", ["const:bc975c:8", "const:4:8"]]
+ 00bc975c ["CALL", null, ["callee:00bdd180:8"]]
- 00bc9694 bytes 8f4e0094
+ 00bc975c bytes 894e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16966cbd2bc8066e9a711a59722d9af4"></a>

### [`00bc9d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9d24.md) → [`00bc9dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9dec.md) FUN_00bc9dec

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc47d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc47d4.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc9e50",
      "incomplete_value": false,
      "site": "00bc9e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9d88",
      "incomplete_value": false,
      "site": "00bc9d88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "00bc9e50",
      "DATA",
      [
        "storage",
        "00c18828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc9e50",
      "DATA",
      [
        "storage",
        "00c188d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9d24.md#insn-00bc9d58) · [`00bc9d7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9d24.md#insn-00bc9d7c) · [`00bc9dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9d24.md#insn-00bc9dc0)
- 新版 `00bc9e20`（命令位置の公開資料なし） · `00bc9e44`（命令位置の公開資料なし） · `00bc9e88`（命令位置の公開資料なし）

~~~diff
- 00bc9d58 ["INT_ADD", "register:40f0:8", ["const:bc9d58:8", "const:4:8"]]
- 00bc9d58 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc9e20 ["INT_ADD", "register:40f0:8", ["const:bc9e20:8", "const:4:8"]]
+ 00bc9e20 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc9d58 bytes de4c0094
+ 00bc9e20 bytes d84c0094
- 00bc9d7c ["COPY", "tmp:0:8", ["const:828:8"]]
- 00bc9d7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9d7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9d7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc9e44 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00bc9e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc9d7c bytes 08a12091
+ 00bc9e44 bytes 08612391
- 00bc9dc0 ["INT_ADD", "register:40f0:8", ["const:bc9dc0:8", "const:4:8"]]
- 00bc9dc0 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc9e88 ["INT_ADD", "register:40f0:8", ["const:bc9e88:8", "const:4:8"]]
+ 00bc9e88 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc9dc0 bytes c4440094
+ 00bc9e88 bytes be440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc945594012aad9cfca2dbb86a6cdc12"></a>

### [`00bc9dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9dc4.md) → [`00bc9e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc9e8c.md) FUN_00bc9e8c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc47d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc47d4.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc9ef4",
      "incomplete_value": false,
      "site": "00bc9ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9e2c",
      "incomplete_value": false,
      "site": "00bc9e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00bc9ef4",
      "DATA",
      [
        "storage",
        "00c18898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc9ef4",
      "DATA",
      [
        "storage",
        "00c18948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9dfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9dc4.md#insn-00bc9dfc) · [`00bc9e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9dc4.md#insn-00bc9e20) · [`00bc9e6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9dc4.md#insn-00bc9e6c)
- 新版 `00bc9ec4`（命令位置の公開資料なし） · `00bc9ee8`（命令位置の公開資料なし） · `00bc9f34`（命令位置の公開資料なし）

~~~diff
- 00bc9dfc ["INT_ADD", "register:40f0:8", ["const:bc9dfc:8", "const:4:8"]]
- 00bc9dfc ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc9ec4 ["INT_ADD", "register:40f0:8", ["const:bc9ec4:8", "const:4:8"]]
+ 00bc9ec4 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc9dfc bytes b54c0094
+ 00bc9ec4 bytes af4c0094
- 00bc9e20 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00bc9e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc9ee8 ["COPY", "tmp:0:8", ["const:948:8"]]
+ 00bc9ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc9ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc9e20 bytes 08612291
+ 00bc9ee8 bytes 08212591
- 00bc9e6c ["INT_ADD", "register:40f0:8", ["const:bc9e6c:8", "const:4:8"]]
- 00bc9e6c ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc9f34 ["INT_ADD", "register:40f0:8", ["const:bc9f34:8", "const:4:8"]]
+ 00bc9f34 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc9e6c bytes 99440094
+ 00bc9f34 bytes 93440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a94f2dbf85b3040bc3b5ab8349d76bf3"></a>

### [`00bca214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca214.md) → [`00bca2dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca2dc.md) FUN_00bca2dc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1000.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be10b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca400",
      "incomplete_value": false,
      "site": "00bca418",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca338",
      "incomplete_value": false,
      "site": "00bca350",
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
            "const:98:8"
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
      "00bca400",
      "PARAM",
      [
        "storage",
        "002a8098",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bca400",
      "PARAM",
      [
        "storage",
        "002a8004",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca214.md#insn-00bca350) · [`00bca338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca214.md#insn-00bca338) · [`00bca384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca214.md#insn-00bca384)
- 新版 `00bca418`（命令位置の公開資料なし） · `00bca400`（命令位置の公開資料なし） · `00bca44c`（命令位置の公開資料なし）

~~~diff
- 00bca350 ["INT_ADD", "register:40f0:8", ["const:bca350:8", "const:4:8"]]
- 00bca350 ["CALL", null, ["callee:00be10b0:8"]]
+ 00bca418 ["INT_ADD", "register:40f0:8", ["const:bca418:8", "const:4:8"]]
+ 00bca418 ["CALL", null, ["callee:00be10b0:8"]]
- 00bca350 bytes 2c5b0094
+ 00bca418 bytes 265b0094
- 00bca338 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00bca338 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00bca338 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00bca338 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00bca400 ["COPY", "tmp:0:8", ["const:4:8"]]
+ 00bca400 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00bca400 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00bca400 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00bca338 bytes 42600291
+ 00bca400 bytes 42100091
- 00bca384 ["INT_ADD", "register:40f0:8", ["const:bca384:8", "const:4:8"]]
- 00bca384 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bca44c ["INT_ADD", "register:40f0:8", ["const:bca44c:8", "const:4:8"]]
+ 00bca44c ["CALL", null, ["callee:00bdd200:8"]]
- 00bca384 bytes 734b0094
+ 00bca44c bytes 6d4b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87a776680b28e4a56d96d8b6d8e4a30e"></a>

### [`00bca3d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca3d0.md) → [`00bca498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca498.md) FUN_00bca498

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1000.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be10b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca5d4",
      "incomplete_value": false,
      "site": "00bca5e4",
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
      "definition_site": "00bca50c",
      "incomplete_value": false,
      "site": "00bca51c",
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
      "00bca5d4",
      "PARAM",
      [
        "storage",
        "0029c22c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bca5d4",
      "PARAM",
      [
        "storage",
        "0029c2b9",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca51c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca3d0.md#insn-00bca51c) · [`00bca50c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca3d0.md#insn-00bca50c) · [`00bca550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca3d0.md#insn-00bca550)
- 新版 `00bca5e4`（命令位置の公開資料なし） · `00bca5d4`（命令位置の公開資料なし） · `00bca618`（命令位置の公開資料なし）

~~~diff
- 00bca51c ["INT_ADD", "register:40f0:8", ["const:bca51c:8", "const:4:8"]]
- 00bca51c ["CALL", null, ["callee:00be10b0:8"]]
+ 00bca5e4 ["INT_ADD", "register:40f0:8", ["const:bca5e4:8", "const:4:8"]]
+ 00bca5e4 ["CALL", null, ["callee:00be10b0:8"]]
- 00bca51c bytes b95a0094
+ 00bca5e4 bytes b35a0094
- 00bca50c ["COPY", "tmp:0:8", ["const:22c:8"]]
- 00bca50c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00bca50c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00bca50c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00bca5d4 ["COPY", "tmp:0:8", ["const:2b9:8"]]
+ 00bca5d4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00bca5d4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00bca5d4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00bca50c bytes 42b00891
+ 00bca5d4 bytes 42e40a91
- 00bca550 ["INT_ADD", "register:40f0:8", ["const:bca550:8", "const:4:8"]]
- 00bca550 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bca618 ["INT_ADD", "register:40f0:8", ["const:bca618:8", "const:4:8"]]
+ 00bca618 ["CALL", null, ["callee:00bdd200:8"]]
- 00bca550 bytes 004b0094
+ 00bca618 bytes fa4a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65e89379be954595553cada155914db4"></a>

### [`00bca59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca59c.md) → [`00bca664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca664.md) FUN_00bca664

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1000.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be10b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be10b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bca7d8",
      "incomplete_value": false,
      "site": "00bca7ec",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca710",
      "incomplete_value": false,
      "site": "00bca724",
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
            "const:171:8"
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
      "00bca7d8",
      "PARAM",
      [
        "storage",
        "002a9171",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bca7d8",
      "PARAM",
      [
        "storage",
        "002a90dd",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca59c.md#insn-00bca724) · [`00bca710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca59c.md#insn-00bca710) · [`00bca758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca59c.md#insn-00bca758)
- 新版 `00bca7ec`（命令位置の公開資料なし） · `00bca7d8`（命令位置の公開資料なし） · `00bca820`（命令位置の公開資料なし）

~~~diff
- 00bca724 ["INT_ADD", "register:40f0:8", ["const:bca724:8", "const:4:8"]]
- 00bca724 ["CALL", null, ["callee:00be10b0:8"]]
+ 00bca7ec ["INT_ADD", "register:40f0:8", ["const:bca7ec:8", "const:4:8"]]
+ 00bca7ec ["CALL", null, ["callee:00be10b0:8"]]
- 00bca724 bytes 375a0094
+ 00bca7ec bytes 315a0094
- 00bca710 ["COPY", "tmp:0:8", ["const:171:8"]]
- 00bca710 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00bca710 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00bca710 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00bca7d8 ["COPY", "tmp:0:8", ["const:dd:8"]]
+ 00bca7d8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00bca7d8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00bca7d8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00bca710 bytes 42c40591
+ 00bca7d8 bytes 42740391
- 00bca758 ["INT_ADD", "register:40f0:8", ["const:bca758:8", "const:4:8"]]
- 00bca758 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bca820 ["INT_ADD", "register:40f0:8", ["const:bca820:8", "const:4:8"]]
+ 00bca820 ["CALL", null, ["callee:00bdd200:8"]]
- 00bca758 bytes 7e4a0094
+ 00bca820 bytes 784a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0357e0a90bbaa501a0e648c7e9a64338"></a>

### [`00bca8b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca8b8.md) → [`00bca980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca980.md) FUN_00bca980

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00bbf9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) [`00bc95a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc95a4.md) [`00bca8b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca8b8.md) · 呼出先 14件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bbfe64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md)
- 新版 呼出元 3件 [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc966c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc966c.md) [`00bca980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca980.md) · 呼出先 14件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.96% / 新版 96.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcaa9c",
      "incomplete_value": false,
      "site": "00bcaa9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca9d4",
      "incomplete_value": false,
      "site": "00bca9d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "definition_site": "00bcab74",
      "incomplete_value": false,
      "site": "00bcab74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcaaac",
      "incomplete_value": false,
      "site": "00bcaaac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "definition_site": "00bcac34",
      "incomplete_value": false,
      "site": "00bcac34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcab6c",
      "incomplete_value": false,
      "site": "00bcab6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "00bcaa9c",
      "DATA",
      [
        "storage",
        "00c18518",
        null,
        "undefined *"
      ]
    ],
    [
      "00bcab74",
      "DATA",
      [
        "storage",
        "00c18518",
        null,
        "undefined *"
      ]
    ],
    [
      "00bcac34",
      "DATA",
      [
        "storage",
        "00c18518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcaa9c",
      "DATA",
      [
        "storage",
        "00c185c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bcab74",
      "DATA",
      [
        "storage",
        "00c185c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bcac34",
      "DATA",
      [
        "storage",
        "00c185c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcacfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca8b8.md#insn-00bcacfc) · [`00bcadc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca8b8.md#insn-00bcadc8) · [`00bcb1e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca8b8.md#insn-00bcb1e4)
- 新版 `00bcadc4`（命令位置の公開資料なし） · `00bcae90`（命令位置の公開資料なし） · `00bcb2ac`（命令位置の公開資料なし）

~~~diff
- 00bcacfc ["INT_ADD", "register:40f0:8", ["const:bcacfc:8", "const:4:8"]]
- 00bcacfc ["CALL", null, ["callee:00bdd180:8"]]
+ 00bcadc4 ["INT_ADD", "register:40f0:8", ["const:bcadc4:8", "const:4:8"]]
+ 00bcadc4 ["CALL", null, ["callee:00bdd180:8"]]
- 00bcacfc bytes f5480094
+ 00bcadc4 bytes ef480094
- 00bcadc8 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00bcadc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcadc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcadc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcae90 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 00bcae90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcae90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcae90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcadc8 bytes 08e11791
+ 00bcae90 bytes 08a11a91
- 00bcb1e4 ["INT_ADD", "register:40f0:8", ["const:bcb1e4:8", "const:4:8"]]
- 00bcb1e4 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bcb2ac ["INT_ADD", "register:40f0:8", ["const:bcb2ac:8", "const:4:8"]]
+ 00bcb2ac ["CALL", null, ["callee:00bbb158:8"]]
- 00bcb1e4 bytes abbfff97
+ 00bcb2ac bytes abbfff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e68d0db7620a0c915e89cfaf6c8e7197"></a>

### [`00bcb224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb224.md) → [`00bcb2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb2ec.md) FUN_00bcb2ec

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc95a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc95a4.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc966c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc9/00bc966c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bcb368",
      "incomplete_value": false,
      "site": "00bcb368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb2a0",
      "incomplete_value": false,
      "site": "00bcb2a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
      "00bcb368",
      "DATA",
      [
        "storage",
        "00c187b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcb368",
      "DATA",
      [
        "storage",
        "00c18868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb224.md#insn-00bcb270) · [`00bcb294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb224.md#insn-00bcb294) · [`00bcb300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb224.md#insn-00bcb300)
- 新版 `00bcb338`（命令位置の公開資料なし） · `00bcb35c`（命令位置の公開資料なし） · `00bcb3c8`（命令位置の公開資料なし）

~~~diff
- 00bcb270 ["INT_ADD", "register:40f0:8", ["const:bcb270:8", "const:4:8"]]
- 00bcb270 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bcb338 ["INT_ADD", "register:40f0:8", ["const:bcb338:8", "const:4:8"]]
+ 00bcb338 ["CALL", null, ["callee:00bdd180:8"]]
- 00bcb270 bytes 98470094
+ 00bcb338 bytes 92470094
- 00bcb294 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 00bcb294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcb294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcb294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcb35c ["COPY", "tmp:0:8", ["const:868:8"]]
+ 00bcb35c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcb35c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcb35c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcb294 bytes 08e11e91
+ 00bcb35c bytes 08a12191
- 00bcb300 ["INT_ADD", "register:40f0:8", ["const:bcb300:8", "const:4:8"]]
- 00bcb300 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bcb3c8 ["INT_ADD", "register:40f0:8", ["const:bcb3c8:8", "const:4:8"]]
+ 00bcb3c8 ["CALL", null, ["callee:00bdb180:8"]]
- 00bcb300 bytes 743f0094
+ 00bcb3c8 bytes 6e3f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ff9a4ada5d036486218962e08dfbe60"></a>

### [`00bcb304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb304.md) → [`00bcb3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb3cc.md) FUN_00bcb3cc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcb430",
      "incomplete_value": false,
      "site": "00bcb440",
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
      "definition_site": "00bcb368",
      "incomplete_value": false,
      "site": "00bcb378",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcb438",
      "incomplete_value": false,
      "site": "00bcb440",
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
      "definition_site": "00bcb370",
      "incomplete_value": false,
      "site": "00bcb378",
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
      "00bcb430",
      "PARAM",
      [
        "storage",
        "002a207d",
        null,
        "string"
      ]
    ],
    [
      "00bcb438",
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
      "00bcb430",
      "PARAM",
      [
        "storage",
        "002a210a",
        null,
        "string"
      ]
    ],
    [
      "00bcb438",
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

- 旧版 [`00bcb378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb304.md#insn-00bcb378) · [`00bcb368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb304.md#insn-00bcb368) · [`00bcb370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb304.md#insn-00bcb370)
- 新版 `00bcb440`（命令位置の公開資料なし） · `00bcb430`（命令位置の公開資料なし） · `00bcb438`（命令位置の公開資料なし）

~~~diff
- 00bcb378 ["INT_ADD", "register:40f0:8", ["const:bcb378:8", "const:4:8"]]
- 00bcb378 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bcb440 ["INT_ADD", "register:40f0:8", ["const:bcb440:8", "const:4:8"]]
+ 00bcb440 ["CALL", null, ["callee:00bbb158:8"]]
- 00bcb378 bytes 46bfff97
+ 00bcb440 bytes 46bfff97
- 00bcb368 ["COPY", "tmp:0:8", ["const:7d:8"]]
- 00bcb368 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bcb368 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bcb368 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bcb430 ["COPY", "tmp:0:8", ["const:10a:8"]]
+ 00bcb430 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bcb430 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bcb430 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bcb368 bytes 21f40191
+ 00bcb430 bytes 21280491
- 00bcb370 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 00bcb370 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00bcb370 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00bcb370 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00bcb438 ["COPY", "tmp:0:8", ["const:866:8"]]
+ 00bcb438 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00bcb438 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00bcb438 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00bcb370 bytes 63641f91
+ 00bcb438 bytes 63982191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f37a94e6dd28198baff7784e0b771ffe"></a>

### [`00bcb4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb4d0.md) → [`00bcb598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb598.md) FUN_00bcb598

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bca8b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bca/00bca8b8.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bca980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bca/00bca980.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bcb5fc",
      "incomplete_value": false,
      "site": "00bcb5fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb534",
      "incomplete_value": false,
      "site": "00bcb534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:748:8"
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
      "00bcb5fc",
      "DATA",
      [
        "storage",
        "00c18748",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcb5fc",
      "DATA",
      [
        "storage",
        "00c187f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb4d0.md#insn-00bcb504) · [`00bcb528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb4d0.md#insn-00bcb528) · [`00bcb56c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb4d0.md#insn-00bcb56c)
- 新版 `00bcb5cc`（命令位置の公開資料なし） · `00bcb5f0`（命令位置の公開資料なし） · `00bcb634`（命令位置の公開資料なし）

~~~diff
- 00bcb504 ["INT_ADD", "register:40f0:8", ["const:bcb504:8", "const:4:8"]]
- 00bcb504 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bcb5cc ["INT_ADD", "register:40f0:8", ["const:bcb5cc:8", "const:4:8"]]
+ 00bcb5cc ["CALL", null, ["callee:00bdd180:8"]]
- 00bcb504 bytes f3460094
+ 00bcb5cc bytes ed460094
- 00bcb528 ["COPY", "tmp:0:8", ["const:748:8"]]
- 00bcb528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcb528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcb528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcb5f0 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 00bcb5f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcb5f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcb5f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcb528 bytes 08211d91
+ 00bcb5f0 bytes 08e11f91
- 00bcb56c ["INT_ADD", "register:40f0:8", ["const:bcb56c:8", "const:4:8"]]
- 00bcb56c ["CALL", null, ["callee:00bdb180:8"]]
+ 00bcb634 ["INT_ADD", "register:40f0:8", ["const:bcb634:8", "const:4:8"]]
+ 00bcb634 ["CALL", null, ["callee:00bdb180:8"]]
- 00bcb56c bytes d93e0094
+ 00bcb634 bytes d33e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c07f1eaaa253bcadbb78700aaa0899f"></a>

### [`00bcb7a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb7a4.md) → [`00bcb86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb86c.md) FUN_00bcb86c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcb8c4",
      "incomplete_value": true,
      "site": "00bcb8d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:64e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb7fc",
      "incomplete_value": true,
      "site": "00bcb808",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c1:8"
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
      "00bcb8c4",
      "READ",
      [
        "storage",
        "002925c1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcb8c4",
      "READ",
      [
        "storage",
        "0029264e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb7e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb7a4.md#insn-00bcb7e0) · [`00bcb7f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb7a4.md#insn-00bcb7f4) · [`00bcb828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcb7a4.md#insn-00bcb828)
- 新版 `00bcb8a8`（命令位置の公開資料なし） · `00bcb8bc`（命令位置の公開資料なし） · `00bcb8f0`（命令位置の公開資料なし）

~~~diff
- 00bcb7e0 ["INT_ADD", "register:40f0:8", ["const:bcb7e0:8", "const:4:8"]]
- 00bcb7e0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcb8a8 ["INT_ADD", "register:40f0:8", ["const:bcb8a8:8", "const:4:8"]]
+ 00bcb8a8 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcb7e0 bytes 5c460094
+ 00bcb8a8 bytes 56460094
- 00bcb7f4 ["COPY", "tmp:0:8", ["const:5c1:8"]]
- 00bcb7f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bcb7f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bcb7f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bcb8bc ["COPY", "tmp:0:8", ["const:64e:8"]]
+ 00bcb8bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bcb8bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bcb8bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bcb7f4 bytes 29051791
+ 00bcb8bc bytes 29391991
- 00bcb828 ["INT_ADD", "register:40f0:8", ["const:bcb828:8", "const:4:8"]]
- 00bcb828 ["CALL", null, ["callee:00bde270:8"]]
+ 00bcb8f0 ["INT_ADD", "register:40f0:8", ["const:bcb8f0:8", "const:4:8"]]
+ 00bcb8f0 ["CALL", null, ["callee:00bde270:8"]]
- 00bcb828 bytes 664a0094
+ 00bcb8f0 bytes 604a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ead316249c4ff943142e91a70242bdd"></a>

### [`00bcbaf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbaf4.md) → [`00bcbbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcbbbc.md) FUN_00bcbbbc

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcbc24",
      "incomplete_value": true,
      "site": "00bcbc30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:62c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbb5c",
      "incomplete_value": true,
      "site": "00bcbb68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c0:8"
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
      "definition_site": "00bcbc90",
      "incomplete_value": true,
      "site": "00bcbc9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbbc8",
      "incomplete_value": true,
      "site": "00bcbbd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:244:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcbc24",
      "READ",
      [
        "storage",
        "002ae6c0",
        null,
        "string"
      ]
    ],
    [
      "00bcbc90",
      "READ",
      [
        "storage",
        "002a0244",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcbc24",
      "READ",
      [
        "storage",
        "002ae62c",
        null,
        "string"
      ]
    ],
    [
      "00bcbc90",
      "READ",
      [
        "storage",
        "002a02d1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbaf4.md#insn-00bcbb40) · [`00bcbb54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbaf4.md#insn-00bcbb54) · [`00bcbb80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbaf4.md#insn-00bcbb80)
- 新版 `00bcbc08`（命令位置の公開資料なし） · `00bcbc1c`（命令位置の公開資料なし） · `00bcbc48`（命令位置の公開資料なし）

~~~diff
- 00bcbb40 ["INT_ADD", "register:40f0:8", ["const:bcbb40:8", "const:4:8"]]
- 00bcbb40 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcbc08 ["INT_ADD", "register:40f0:8", ["const:bcbc08:8", "const:4:8"]]
+ 00bcbc08 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcbb40 bytes 84450094
+ 00bcbc08 bytes 7e450094
- 00bcbb54 ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 00bcbb54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bcbb54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bcbb54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bcbc1c ["COPY", "tmp:0:8", ["const:62c:8"]]
+ 00bcbc1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bcbc1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bcbc1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bcbb54 bytes 29011b91
+ 00bcbc1c bytes 29b11891
- 00bcbb80 ["INT_ADD", "register:40f0:8", ["const:bcbb80:8", "const:4:8"]]
- 00bcbb80 ["CALL", null, ["callee:00bc8290:8"]]
+ 00bcbc48 ["INT_ADD", "register:40f0:8", ["const:bcbc48:8", "const:4:8"]]
+ 00bcbc48 ["CALL", null, ["callee:00bc8290:8"]]
- 00bcbb80 bytes 92f1ff97
+ 00bcbc48 bytes 92f1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a07d9f8a8d2efe9ec1ed69ae5d7ec0bd"></a>

### [`00bcc5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc5e0.md) → [`00bcc6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc6a8.md) FUN_00bcc6a8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc5154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5154.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc521c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc521c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bcc70c",
      "incomplete_value": false,
      "site": "00bcc70c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc644",
      "incomplete_value": false,
      "site": "00bcc644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "00bcc70c",
      "DATA",
      [
        "storage",
        "00c18908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcc70c",
      "DATA",
      [
        "storage",
        "00c189b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc5e0.md#insn-00bcc614) · [`00bcc638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc5e0.md#insn-00bcc638) · [`00bcc67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc5e0.md#insn-00bcc67c)
- 新版 `00bcc6dc`（命令位置の公開資料なし） · `00bcc700`（命令位置の公開資料なし） · `00bcc744`（命令位置の公開資料なし）

~~~diff
- 00bcc614 ["INT_ADD", "register:40f0:8", ["const:bcc614:8", "const:4:8"]]
- 00bcc614 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bcc6dc ["INT_ADD", "register:40f0:8", ["const:bcc6dc:8", "const:4:8"]]
+ 00bcc6dc ["CALL", null, ["callee:00bdd180:8"]]
- 00bcc614 bytes af420094
+ 00bcc6dc bytes a9420094
- 00bcc638 ["COPY", "tmp:0:8", ["const:908:8"]]
- 00bcc638 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc638 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcc638 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcc700 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00bcc700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcc700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcc700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcc638 bytes 08212491
+ 00bcc700 bytes 08e12691
- 00bcc67c ["INT_ADD", "register:40f0:8", ["const:bcc67c:8", "const:4:8"]]
- 00bcc67c ["CALL", null, ["callee:00bdb180:8"]]
+ 00bcc744 ["INT_ADD", "register:40f0:8", ["const:bcc744:8", "const:4:8"]]
+ 00bcc744 ["CALL", null, ["callee:00bdb180:8"]]
- 00bcc67c bytes 953a0094
+ 00bcc744 bytes 8f3a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b6cead7ece2b60e8f1f9a554dbfb089"></a>

### [`00bcc774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc774.md) → [`00bcc83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bcc83c.md) FUN_00bcc83c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bccef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bccef8.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bccfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcca1c",
      "incomplete_value": false,
      "site": "00bcca20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcc954",
      "incomplete_value": false,
      "site": "00bcc958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "definition_site": "00bccd54",
      "incomplete_value": false,
      "site": "00bccd58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bccc8c",
      "incomplete_value": false,
      "site": "00bccc90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcca20",
      "DATA",
      [
        "storage",
        "00c189e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bccd58",
      "DATA",
      [
        "storage",
        "00c189e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcca20",
      "DATA",
      [
        "storage",
        "00c18a98",
        null,
        "undefined *"
      ]
    ],
    [
      "00bccd58",
      "DATA",
      [
        "storage",
        "00c18a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc7c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc774.md#insn-00bcc7c8) · [`00bcc844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc774.md#insn-00bcc844) · [`00bcc874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bcc774.md#insn-00bcc874)
- 新版 `00bcc890`（命令位置の公開資料なし） · `00bcc90c`（命令位置の公開資料なし） · `00bcc93c`（命令位置の公開資料なし）

~~~diff
- 00bcc7c8 ["INT_ADD", "register:40f0:8", ["const:bcc7c8:8", "const:4:8"]]
- 00bcc7c8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcc890 ["INT_ADD", "register:40f0:8", ["const:bcc890:8", "const:4:8"]]
+ 00bcc890 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcc7c8 bytes 62420094
+ 00bcc890 bytes 5c420094
- 00bcc844 ["INT_ADD", "register:40f0:8", ["const:bcc844:8", "const:4:8"]]
- 00bcc844 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcc90c ["INT_ADD", "register:40f0:8", ["const:bcc90c:8", "const:4:8"]]
+ 00bcc90c ["CALL", null, ["callee:00bdd200:8"]]
- 00bcc844 bytes 43420094
+ 00bcc90c bytes 3d420094
- 00bcc874 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcc874 ["INT_ADD", "register:40f0:8", ["const:bcc874:8", "const:4:8"]]
- 00bcc874 ["CALLIND", null, ["register:0:8"]]
+ 00bcc93c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcc93c ["INT_ADD", "register:40f0:8", ["const:bcc93c:8", "const:4:8"]]
+ 00bcc93c ["CALLIND", null, ["register:0:8"]]
- 00bcc874 bytes 00013fd6
+ 00bcc93c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fba787918874622bd9e7e085eb87080b"></a>

### [`00bcd89c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd89c.md) → [`00bcd964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcd964.md) FUN_00bcd964

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.38% / 新版 98.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcdb24",
      "incomplete_value": true,
      "site": "00bcdb30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1d9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcda5c",
      "incomplete_value": true,
      "site": "00bcda68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:14c:8"
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
      "00bcdb24",
      "READ",
      [
        "storage",
        "002a114c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcdb24",
      "READ",
      [
        "storage",
        "002a11d9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcd8e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd89c.md#insn-00bcd8e4) · [`00bcd950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd89c.md#insn-00bcd950) · [`00bcd984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd89c.md#insn-00bcd984)
- 新版 `00bcd9ac`（命令位置の公開資料なし） · `00bcda18`（命令位置の公開資料なし） · `00bcda4c`（命令位置の公開資料なし）

~~~diff
- 00bcd8e4 ["INT_ADD", "register:40f0:8", ["const:bcd8e4:8", "const:4:8"]]
- 00bcd8e4 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcd9ac ["INT_ADD", "register:40f0:8", ["const:bcd9ac:8", "const:4:8"]]
+ 00bcd9ac ["CALL", null, ["callee:00bdd200:8"]]
- 00bcd8e4 bytes 1b3e0094
+ 00bcd9ac bytes 153e0094
- 00bcd950 ["INT_ADD", "register:40f0:8", ["const:bcd950:8", "const:4:8"]]
- 00bcd950 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcda18 ["INT_ADD", "register:40f0:8", ["const:bcda18:8", "const:4:8"]]
+ 00bcda18 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcd950 bytes 003e0094
+ 00bcda18 bytes fa3d0094
- 00bcd984 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcd984 ["INT_ADD", "register:40f0:8", ["const:bcd984:8", "const:4:8"]]
- 00bcd984 ["CALLIND", null, ["register:0:8"]]
+ 00bcda4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcda4c ["INT_ADD", "register:40f0:8", ["const:bcda4c:8", "const:4:8"]]
+ 00bcda4c ["CALLIND", null, ["register:0:8"]]
- 00bcd984 bytes 00013fd6
+ 00bcda4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-626ba406765da8600cbb7e842ab6619b"></a>

### [`00bcdb88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcdb88.md) → [`00bcdc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdc50.md) FUN_00bcdc50

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcdcb4",
      "incomplete_value": true,
      "site": "00bcdcc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:39f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdbec",
      "incomplete_value": true,
      "site": "00bcdbfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:399:8"
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
      "00bcdcb4",
      "READ",
      [
        "storage",
        "002ab399",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcdcb4",
      "READ",
      [
        "storage",
        "002ab39f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcdbcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcdb88.md#insn-00bcdbcc) · [`00bcdbe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcdb88.md#insn-00bcdbe4) · [`00bcdc1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcdb88.md#insn-00bcdc1c)
- 新版 `00bcdc94`（命令位置の公開資料なし） · `00bcdcac`（命令位置の公開資料なし） · `00bcdce4`（命令位置の公開資料なし）

~~~diff
- 00bcdbcc ["INT_ADD", "register:40f0:8", ["const:bcdbcc:8", "const:4:8"]]
- 00bcdbcc ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcdc94 ["INT_ADD", "register:40f0:8", ["const:bcdc94:8", "const:4:8"]]
+ 00bcdc94 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcdbcc bytes 613d0094
+ 00bcdc94 bytes 5b3d0094
- 00bcdbe4 ["COPY", "tmp:0:8", ["const:399:8"]]
- 00bcdbe4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bcdbe4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bcdbe4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bcdcac ["COPY", "tmp:0:8", ["const:39f:8"]]
+ 00bcdcac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bcdcac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bcdcac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bcdbe4 bytes 4a650e91
+ 00bcdcac bytes 4a7d0e91
- 00bcdc1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcdc1c ["INT_ADD", "register:40f0:8", ["const:bcdc1c:8", "const:4:8"]]
- 00bcdc1c ["CALLIND", null, ["register:0:8"]]
+ 00bcdce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcdce4 ["INT_ADD", "register:40f0:8", ["const:bcdce4:8", "const:4:8"]]
+ 00bcdce4 ["CALLIND", null, ["register:0:8"]]
- 00bcdc1c bytes 00013fd6
+ 00bcdce4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8934029225140595efc8ad007557acce"></a>

### [`00bce128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce128.md) → [`00bce1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce1f0.md) FUN_00bce1f0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.45% / 新版 98.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bce310",
      "incomplete_value": true,
      "site": "00bce31c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:25b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bce248",
      "incomplete_value": true,
      "site": "00bce254",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:262:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bce310",
      "READ",
      [
        "storage",
        "002a7262",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bce310",
      "READ",
      [
        "storage",
        "002a725b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bce154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce128.md#insn-00bce154) · [`00bce178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce128.md#insn-00bce178) · [`00bce1a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce128.md#insn-00bce1a4)
- 新版 `00bce21c`（命令位置の公開資料なし） · `00bce240`（命令位置の公開資料なし） · `00bce26c`（命令位置の公開資料なし）

~~~diff
- 00bce154 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bce154 ["INT_ADD", "register:40f0:8", ["const:bce154:8", "const:4:8"]]
- 00bce154 ["CALLIND", null, ["register:0:8"]]
+ 00bce21c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bce21c ["INT_ADD", "register:40f0:8", ["const:bce21c:8", "const:4:8"]]
+ 00bce21c ["CALLIND", null, ["register:0:8"]]
- 00bce154 bytes 00013fd6
+ 00bce21c bytes 00013fd6
- 00bce178 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bce178 ["INT_ADD", "register:40f0:8", ["const:bce178:8", "const:4:8"]]
- 00bce178 ["CALLIND", null, ["register:0:8"]]
+ 00bce240 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bce240 ["INT_ADD", "register:40f0:8", ["const:bce240:8", "const:4:8"]]
+ 00bce240 ["CALLIND", null, ["register:0:8"]]
- 00bce178 bytes 00013fd6
+ 00bce240 bytes 00013fd6
- 00bce1a4 ["INT_ADD", "register:40f0:8", ["const:bce1a4:8", "const:4:8"]]
- 00bce1a4 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bce26c ["INT_ADD", "register:40f0:8", ["const:bce26c:8", "const:4:8"]]
+ 00bce26c ["CALL", null, ["callee:00bdd200:8"]]
- 00bce1a4 bytes eb3b0094
+ 00bce26c bytes e53b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c33cc6715d85377f3c6805c3a9035086"></a>

### [`00bce438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce438.md) → [`00bce500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce500.md) FUN_00bce500

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bccef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bccef8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bccfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.68% / 新版 94.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bce568",
      "incomplete_value": true,
      "site": "00bce574",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:31c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bce4a0",
      "incomplete_value": true,
      "site": "00bce4ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:28f:8"
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
      "definition_site": "00bce5f4",
      "incomplete_value": false,
      "site": "00bce5f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bce52c",
      "incomplete_value": false,
      "site": "00bce530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c18000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "00bce568",
      "READ",
      [
        "storage",
        "0029c28f",
        null,
        "string"
      ]
    ],
    [
      "00bce5f8",
      "DATA",
      [
        "storage",
        "00c189e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bce568",
      "READ",
      [
        "storage",
        "0029c31c",
        null,
        "string"
      ]
    ],
    [
      "00bce5f8",
      "DATA",
      [
        "storage",
        "00c18a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bce480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce438.md#insn-00bce480) · [`00bce498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce438.md#insn-00bce498) · [`00bce4ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce438.md#insn-00bce4ec)
- 新版 `00bce548`（命令位置の公開資料なし） · `00bce560`（命令位置の公開資料なし） · `00bce5b4`（命令位置の公開資料なし）

~~~diff
- 00bce480 ["INT_ADD", "register:40f0:8", ["const:bce480:8", "const:4:8"]]
- 00bce480 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bce548 ["INT_ADD", "register:40f0:8", ["const:bce548:8", "const:4:8"]]
+ 00bce548 ["CALL", null, ["callee:00bdd200:8"]]
- 00bce480 bytes 343b0094
+ 00bce548 bytes 2e3b0094
- 00bce498 ["COPY", "tmp:0:8", ["const:28f:8"]]
- 00bce498 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bce498 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bce498 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bce560 ["COPY", "tmp:0:8", ["const:31c:8"]]
+ 00bce560 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bce560 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bce560 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bce498 bytes 4a3d0a91
+ 00bce560 bytes 4a710c91
- 00bce4ec ["INT_ADD", "register:40f0:8", ["const:bce4ec:8", "const:4:8"]]
- 00bce4ec ["CALL", null, ["callee:00bdd200:8"]]
+ 00bce5b4 ["INT_ADD", "register:40f0:8", ["const:bce5b4:8", "const:4:8"]]
+ 00bce5b4 ["CALL", null, ["callee:00bdd200:8"]]
- 00bce4ec bytes 193b0094
+ 00bce5b4 bytes 133b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fe372e1f72b410d01e69c33c63db867"></a>

### [`00bce830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce830.md) → [`00bce8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md) FUN_00bce8f8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc66f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc6/00bc66f0.md) · 呼出先 6件 [`00bc1034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1034.md) [`00bc1648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1648.md) [`00bce6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce6ac.md) [`00bcebe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcebe0.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 1件 [`00bc67b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc6/00bc67b8.md) · 呼出先 6件 [`00bc10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md) [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) [`00bce774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce774.md) [`00bceca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceca8.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.95% / 新版 96.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bceaa0",
      "incomplete_value": false,
      "site": "00bceaa0",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bce9d8",
      "incomplete_value": false,
      "site": "00bce9d8",
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
            "const:8:8"
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
      "definition_site": "00bceb60",
      "incomplete_value": false,
      "site": "00bceb60",
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
      "definition_site": "00bcea98",
      "incomplete_value": false,
      "site": "00bcea98",
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
      "00bce9f8",
      "DATA",
      [
        "storage",
        "00c19698",
        null,
        "undefined *"
      ]
    ],
    [
      "00bceaa0",
      "DATA",
      [
        "storage",
        "00c19008",
        null,
        "undefined *"
      ]
    ],
    [
      "00bceb60",
      "DATA",
      [
        "storage",
        "00c19698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bce9f8",
      "DATA",
      [
        "storage",
        "00c19748",
        null,
        "undefined *"
      ]
    ],
    [
      "00bceaa0",
      "DATA",
      [
        "storage",
        "00c190b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bceb60",
      "DATA",
      [
        "storage",
        "00c19748",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bce89c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce830.md#insn-00bce89c) · [`00bce8ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce830.md#insn-00bce8ac) · [`00bce8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce830.md#insn-00bce8d8)
- 新版 `00bce964`（命令位置の公開資料なし） · `00bce974`（命令位置の公開資料なし） · `00bce9a0`（命令位置の公開資料なし）

~~~diff
- 00bce89c ["INT_ADD", "register:40f0:8", ["const:bce89c:8", "const:4:8"]]
- 00bce89c ["CALL", null, ["callee:00bceca8:8"]]
+ 00bce964 ["INT_ADD", "register:40f0:8", ["const:bce964:8", "const:4:8"]]
+ 00bce964 ["CALL", null, ["callee:00bceca8:8"]]
- 00bce89c bytes d1000094
+ 00bce964 bytes d1000094
- 00bce8ac ["INT_ADD", "register:40f0:8", ["const:bce8ac:8", "const:4:8"]]
- 00bce8ac ["CALL", null, ["callee:00bc10fc:8"]]
+ 00bce974 ["INT_ADD", "register:40f0:8", ["const:bce974:8", "const:4:8"]]
+ 00bce974 ["CALL", null, ["callee:00bc10fc:8"]]
- 00bce8ac bytes e2c9ff97
+ 00bce974 bytes e2c9ff97
- 00bce8d8 ["INT_ADD", "register:40f0:8", ["const:bce8d8:8", "const:4:8"]]
- 00bce8d8 ["CALL", null, ["callee:00bc1710:8"]]
+ 00bce9a0 ["INT_ADD", "register:40f0:8", ["const:bce9a0:8", "const:4:8"]]
+ 00bce9a0 ["CALL", null, ["callee:00bc1710:8"]]
- 00bce8d8 bytes 5ccbff97
+ 00bce9a0 bytes 5ccbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb9deee7dd31c5e95ea23debebd46841"></a>

### [`00bcebe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcebe0.md) → [`00bceca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bceca8.md) FUN_00bceca8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bc2394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2394.md) [`00bce830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bce830.md) · 呼出先 5件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bc1034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1034.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 2件 [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) [`00bce8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce8f8.md) · 呼出先 5件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc10fc.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.74% / 新版 97.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcedf4",
      "incomplete_value": false,
      "site": "00bcedf4",
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
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bced2c",
      "incomplete_value": false,
      "site": "00bced2c",
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
            "const:78:8"
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
      "00bced00",
      "READ",
      [
        "storage",
        "00c17ab8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bced10",
      "READ",
      [
        "storage",
        "00c17ab9",
        null,
        "undefined1"
      ]
    ],
    [
      "00bced3c",
      "READ",
      [
        "storage",
        "00c17ac8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bced00",
      "READ",
      [
        "storage",
        "00c17b68",
        null,
        "undefined1"
      ]
    ],
    [
      "00bced10",
      "READ",
      [
        "storage",
        "00c17b69",
        null,
        "undefined1"
      ]
    ],
    [
      "00bced3c",
      "READ",
      [
        "storage",
        "00c17b78",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcec18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcebe0.md#insn-00bcec18) · [`00bcecc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcebe0.md#insn-00bcecc4) · [`00bcecf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcebe0.md#insn-00bcecf8)
- 新版 `00bcece0`（命令位置の公開資料なし） · `00bced8c`（命令位置の公開資料なし） · `00bcedc0`（命令位置の公開資料なし）

~~~diff
- 00bcec18 ["COPY", "register:4060:8", ["const:c178d8:8"]]
+ 00bcece0 ["COPY", "register:4060:8", ["const:c17988:8"]]
- 00bcec18 bytes 0c662410
+ 00bcece0 bytes 4c652410
- 00bcecc4 ["INT_ADD", "register:40f0:8", ["const:bcecc4:8", "const:4:8"]]
- 00bcecc4 ["CALL", null, ["callee:00bbde18:8"]]
+ 00bced8c ["INT_ADD", "register:40f0:8", ["const:bced8c:8", "const:4:8"]]
+ 00bced8c ["CALL", null, ["callee:00bbde18:8"]]
- 00bcecc4 bytes 23bcff97
+ 00bced8c bytes 23bcff97
- 00bcecf8 ["INT_ADD", "register:40f0:8", ["const:bcecf8:8", "const:4:8"]]
- 00bcecf8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bcedc0 ["INT_ADD", "register:40f0:8", ["const:bcedc0:8", "const:4:8"]]
+ 00bcedc0 ["CALL", null, ["callee:00bdd180:8"]]
- 00bcecf8 bytes f6380094
+ 00bcedc0 bytes f0380094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e29ee8b497615417d3c9ae027e6db34"></a>

### [`00bceffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bceffc.md) → [`00bcf0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf0c4.md) FUN_00bcf0c4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcf128",
      "incomplete_value": true,
      "site": "00bcf138",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf060",
      "incomplete_value": true,
      "site": "00bcf070",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5e6:8"
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
      "00bcf128",
      "READ",
      [
        "storage",
        "002ac5e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcf128",
      "READ",
      [
        "storage",
        "002ac5dd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bceffc.md#insn-00bcf040) · [`00bcf058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bceffc.md#insn-00bcf058) · [`00bcf090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bceffc.md#insn-00bcf090)
- 新版 `00bcf108`（命令位置の公開資料なし） · `00bcf120`（命令位置の公開資料なし） · `00bcf158`（命令位置の公開資料なし）

~~~diff
- 00bcf040 ["INT_ADD", "register:40f0:8", ["const:bcf040:8", "const:4:8"]]
- 00bcf040 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcf108 ["INT_ADD", "register:40f0:8", ["const:bcf108:8", "const:4:8"]]
+ 00bcf108 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcf040 bytes 44380094
+ 00bcf108 bytes 3e380094
- 00bcf058 ["COPY", "tmp:0:8", ["const:5e6:8"]]
- 00bcf058 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bcf058 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bcf058 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bcf120 ["COPY", "tmp:0:8", ["const:5dd:8"]]
+ 00bcf120 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bcf120 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bcf120 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bcf058 bytes 4a991791
+ 00bcf120 bytes 4a751791
- 00bcf090 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcf090 ["INT_ADD", "register:40f0:8", ["const:bcf090:8", "const:4:8"]]
- 00bcf090 ["CALLIND", null, ["register:0:8"]]
+ 00bcf158 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcf158 ["INT_ADD", "register:40f0:8", ["const:bcf158:8", "const:4:8"]]
+ 00bcf158 ["CALLIND", null, ["register:0:8"]]
- 00bcf090 bytes 00013fd6
+ 00bcf158 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73d03f3f143e462d561a5c561bcc206a"></a>

### [`00bcf3bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf3bc.md) → [`00bcf484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf484.md) FUN_00bcf484

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf620",
      "incomplete_value": false,
      "site": "00bcf630",
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
      "definition_site": "00bcf558",
      "incomplete_value": false,
      "site": "00bcf568",
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
      "definition_site": "00bcf628",
      "incomplete_value": false,
      "site": "00bcf630",
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
      "definition_site": "00bcf560",
      "incomplete_value": false,
      "site": "00bcf568",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcf588",
      "READ",
      [
        "storage",
        "002a9246",
        null,
        "string"
      ]
    ],
    [
      "00bcf588",
      "READ",
      [
        "storage",
        "002ac5f0",
        null,
        "string"
      ]
    ],
    [
      "00bcf588",
      "READ",
      [
        "storage",
        "002a80b0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcf588",
      "READ",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ],
    [
      "00bcf588",
      "READ",
      [
        "storage",
        "002ac5e7",
        null,
        "string"
      ]
    ],
    [
      "00bcf588",
      "READ",
      [
        "storage",
        "002a801c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf3bc.md#insn-00bcf568) · [`00bcf404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf3bc.md#insn-00bcf404) · [`00bcf458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf3bc.md#insn-00bcf458)
- 新版 `00bcf630`（命令位置の公開資料なし） · `00bcf4cc`（命令位置の公開資料なし） · `00bcf520`（命令位置の公開資料なし）

~~~diff
- 00bcf568 ["INT_ADD", "register:40f0:8", ["const:bcf568:8", "const:4:8"]]
- 00bcf568 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bcf630 ["INT_ADD", "register:40f0:8", ["const:bcf630:8", "const:4:8"]]
+ 00bcf630 ["CALL", null, ["callee:00bbb158:8"]]
- 00bcf568 bytes caaeff97
+ 00bcf630 bytes caaeff97
- 00bcf404 ["INT_ADD", "register:40f0:8", ["const:bcf404:8", "const:4:8"]]
- 00bcf404 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcf4cc ["INT_ADD", "register:40f0:8", ["const:bcf4cc:8", "const:4:8"]]
+ 00bcf4cc ["CALL", null, ["callee:00bdd200:8"]]
- 00bcf404 bytes 53370094
+ 00bcf4cc bytes 4d370094
- 00bcf458 ["COPY", "tmp:0:8", ["const:246:8"]]
- 00bcf458 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00bcf458 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00bcf458 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00bcf520 ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 00bcf520 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00bcf520 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00bcf520 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00bcf458 bytes b51a0991
+ 00bcf520 bytes b5ca0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73ac294261e296323b3bf95de6abe960"></a>

### [`00bcf574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf574.md) → [`00bcf63c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf63c.md) FUN_00bcf63c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 85.45% / 新版 85.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf704",
      "incomplete_value": false,
      "site": "00bcf714",
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
      "definition_site": "00bcf63c",
      "incomplete_value": false,
      "site": "00bcf64c",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf70c",
      "incomplete_value": false,
      "site": "00bcf714",
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
      "definition_site": "00bcf644",
      "incomplete_value": false,
      "site": "00bcf64c",
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
    "ordinal": 0,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bcf65c",
      "incomplete_value": false,
      "site": "00bcf664",
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
      "definition_site": "00bcf594",
      "incomplete_value": false,
      "site": "00bcf59c",
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcf65c",
      "DATA",
      [
        "storage",
        "002a9246",
        null,
        "string"
      ]
    ],
    [
      "00bcf68c",
      "DATA",
      [
        "storage",
        "002a726e",
        null,
        "string"
      ]
    ],
    [
      "00bcf6c4",
      "READ",
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
      "00bcf65c",
      "DATA",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ],
    [
      "00bcf68c",
      "DATA",
      [
        "storage",
        "002a7267",
        null,
        "string"
      ]
    ],
    [
      "00bcf6c4",
      "READ",
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

- 旧版 [`00bcf64c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf574.md#insn-00bcf64c) · [`00bcf594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf574.md#insn-00bcf594) · [`00bcf5b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf574.md#insn-00bcf5b4)
- 新版 `00bcf714`（命令位置の公開資料なし） · `00bcf65c`（命令位置の公開資料なし） · `00bcf67c`（命令位置の公開資料なし）

~~~diff
- 00bcf64c ["INT_ADD", "register:40f0:8", ["const:bcf64c:8", "const:4:8"]]
- 00bcf64c ["CALL", null, ["callee:00bbb158:8"]]
+ 00bcf714 ["INT_ADD", "register:40f0:8", ["const:bcf714:8", "const:4:8"]]
+ 00bcf714 ["CALL", null, ["callee:00bbb158:8"]]
- 00bcf64c bytes 91aeff97
+ 00bcf714 bytes 91aeff97
- 00bcf594 ["COPY", "tmp:0:8", ["const:246:8"]]
- 00bcf594 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcf594 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcf594 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bcf65c ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 00bcf65c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcf65c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bcf65c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcf594 bytes 00180991
+ 00bcf65c bytes 00c80691
- 00bcf5b4 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00bcf5b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcf5b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcf5b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bcf67c ["COPY", "tmp:0:8", ["const:5e7:8"]]
+ 00bcf67c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcf67c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bcf67c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcf5b4 bytes 08c11791
+ 00bcf67c bytes 089d1791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-589c2a109db6e55d82e8dcd3d9d19c1b"></a>

### [`00bcf658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf658.md) → [`00bcf720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf720.md) FUN_00bcf720

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.01% / 新版 93.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bcf860",
      "incomplete_value": true,
      "site": "00bcf868",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:178:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf798",
      "incomplete_value": true,
      "site": "00bcf7a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:17f:8"
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
      "definition_site": "00bcf864",
      "incomplete_value": true,
      "site": "00bcf86c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00bcf79c",
      "incomplete_value": true,
      "site": "00bcf7a4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00bcf8cc",
      "incomplete_value": true,
      "site": "00bcf8d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3da:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf804",
      "incomplete_value": true,
      "site": "00bcf80c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3d4:8"
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
      "00bcf860",
      "READ",
      [
        "storage",
        "002a417f",
        null,
        "string"
      ]
    ],
    [
      "00bcf864",
      "READ",
      [
        "storage",
        "002a418c",
        null,
        "string"
      ]
    ],
    [
      "00bcf8cc",
      "READ",
      [
        "storage",
        "002aa3d4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcf860",
      "READ",
      [
        "storage",
        "002a4178",
        null,
        "string"
      ]
    ],
    [
      "00bcf864",
      "READ",
      [
        "storage",
        "002a4185",
        null,
        "string"
      ]
    ],
    [
      "00bcf8cc",
      "READ",
      [
        "storage",
        "002aa3da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf658.md#insn-00bcf6a0) · [`00bcf6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf658.md#insn-00bcf6e4) · [`00bcf71c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcf658.md#insn-00bcf71c)
- 新版 `00bcf768`（命令位置の公開資料なし） · `00bcf7ac`（命令位置の公開資料なし） · `00bcf7e4`（命令位置の公開資料なし）

~~~diff
- 00bcf6a0 ["INT_ADD", "register:40f0:8", ["const:bcf6a0:8", "const:4:8"]]
- 00bcf6a0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcf768 ["INT_ADD", "register:40f0:8", ["const:bcf768:8", "const:4:8"]]
+ 00bcf768 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcf6a0 bytes ac360094
+ 00bcf768 bytes a6360094
- 00bcf6e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcf6e4 ["INT_ADD", "register:40f0:8", ["const:bcf6e4:8", "const:4:8"]]
- 00bcf6e4 ["CALLIND", null, ["register:0:8"]]
+ 00bcf7ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcf7ac ["INT_ADD", "register:40f0:8", ["const:bcf7ac:8", "const:4:8"]]
+ 00bcf7ac ["CALLIND", null, ["register:0:8"]]
- 00bcf6e4 bytes 00013fd6
+ 00bcf7ac bytes 00013fd6
- 00bcf71c ["INT_ADD", "register:40f0:8", ["const:bcf71c:8", "const:4:8"]]
- 00bcf71c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bcf7e4 ["INT_ADD", "register:40f0:8", ["const:bcf7e4:8", "const:4:8"]]
+ 00bcf7e4 ["CALL", null, ["callee:00bdd200:8"]]
- 00bcf71c bytes 8d360094
+ 00bcf7e4 bytes 87360094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ed0c34a77c94701cd79d7114875293e"></a>

### [`00bcfb88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfb88.md) → [`00bcfc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcfc50.md) FUN_00bcfc50

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc2394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2394.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bcfcc0",
      "incomplete_value": false,
      "site": "00bcfcc0",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcfbf8",
      "incomplete_value": false,
      "site": "00bcfbf8",
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
            "const:388:8"
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
      "00bcfcc0",
      "DATA",
      [
        "storage",
        "00c19388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bcfcc0",
      "DATA",
      [
        "storage",
        "00c19438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcfbc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfb88.md#insn-00bcfbc8) · [`00bcfbf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfb88.md#insn-00bcfbf4) · [`00bcfc44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcf/00bcfb88.md#insn-00bcfc44)
- 新版 `00bcfc90`（命令位置の公開資料なし） · `00bcfcbc`（命令位置の公開資料なし） · `00bcfd0c`（命令位置の公開資料なし）

~~~diff
- 00bcfbc8 ["INT_ADD", "register:40f0:8", ["const:bcfbc8:8", "const:4:8"]]
- 00bcfbc8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bcfc90 ["INT_ADD", "register:40f0:8", ["const:bcfc90:8", "const:4:8"]]
+ 00bcfc90 ["CALL", null, ["callee:00bdd180:8"]]
- 00bcfbc8 bytes 42350094
+ 00bcfc90 bytes 3c350094
- 00bcfbf4 ["COPY", "tmp:0:8", ["const:388:8"]]
- 00bcfbf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bcfbf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bcfbf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bcfcbc ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00bcfcbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bcfcbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bcfcbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bcfbf4 bytes 29210e91
+ 00bcfcbc bytes 29e11091
- 00bcfc44 ["INT_ADD", "register:40f0:8", ["const:bcfc44:8", "const:4:8"]]
- 00bcfc44 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bcfd0c ["INT_ADD", "register:40f0:8", ["const:bcfd0c:8", "const:4:8"]]
+ 00bcfd0c ["CALL", null, ["callee:00bdb180:8"]]
- 00bcfc44 bytes 232d0094
+ 00bcfd0c bytes 1d2d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e44e57b31a9f658fb02ff36cc8930f9b"></a>

### [`00bd0174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0174.md) → [`00bd023c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd023c.md) FUN_00bd023c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd02a8",
      "incomplete_value": true,
      "site": "00bd02a8",
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
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd01e0",
      "incomplete_value": true,
      "site": "00bd01e0",
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
            "const:798:8"
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
      "00bd02a8",
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
      "00bd02a8",
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

- 旧版 [`00bd01a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0174.md#insn-00bd01a8) · [`00bd01d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0174.md#insn-00bd01d0) · [`00bd01d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0174.md#insn-00bd01d8)
- 新版 `00bd0270`（命令位置の公開資料なし） · `00bd0298`（命令位置の公開資料なし） · `00bd02a0`（命令位置の公開資料なし）

~~~diff
- 00bd01a8 ["INT_ADD", "register:40f0:8", ["const:bd01a8:8", "const:4:8"]]
- 00bd01a8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd0270 ["INT_ADD", "register:40f0:8", ["const:bd0270:8", "const:4:8"]]
+ 00bd0270 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd01a8 bytes ca330094
+ 00bd0270 bytes c4330094
- 00bd01d0 ["INT_ADD", "register:40f0:8", ["const:bd01d0:8", "const:4:8"]]
- 00bd01d0 ["CALL", null, ["callee:00bdb140:8"]]
+ 00bd0298 ["INT_ADD", "register:40f0:8", ["const:bd0298:8", "const:4:8"]]
+ 00bd0298 ["CALL", null, ["callee:00bdb140:8"]]
- 00bd01d0 bytes b02b0094
+ 00bd0298 bytes aa2b0094
- 00bd01d8 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bd01d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd01d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd01d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd02a0 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bd02a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd02a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd02a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd01d8 bytes 29611e91
+ 00bd02a0 bytes 29212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c4dc8e18ace918c2a44f277c3e625bf"></a>

### [`00bd0220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0220.md) → [`00bd02e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd02e8.md) FUN_00bd02e8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bd0350",
      "incomplete_value": false,
      "site": "00bd0350",
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
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0288",
      "incomplete_value": false,
      "site": "00bd0288",
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
            "const:548:8"
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
      "00bd0350",
      "DATA",
      [
        "storage",
        "00c19548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd0350",
      "DATA",
      [
        "storage",
        "00c195f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0220.md#insn-00bd0258) · [`00bd027c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0220.md#insn-00bd027c) · [`00bd02c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0220.md#insn-00bd02c4)
- 新版 `00bd0320`（命令位置の公開資料なし） · `00bd0344`（命令位置の公開資料なし） · `00bd038c`（命令位置の公開資料なし）

~~~diff
- 00bd0258 ["INT_ADD", "register:40f0:8", ["const:bd0258:8", "const:4:8"]]
- 00bd0258 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd0320 ["INT_ADD", "register:40f0:8", ["const:bd0320:8", "const:4:8"]]
+ 00bd0320 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd0258 bytes 9e330094
+ 00bd0320 bytes 98330094
- 00bd027c ["COPY", "tmp:0:8", ["const:548:8"]]
- 00bd027c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd027c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd027c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd0344 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00bd0344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd0344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd0344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd027c bytes 08211591
+ 00bd0344 bytes 08e11791
- 00bd02c4 ["INT_ADD", "register:40f0:8", ["const:bd02c4:8", "const:4:8"]]
- 00bd02c4 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd038c ["INT_ADD", "register:40f0:8", ["const:bd038c:8", "const:4:8"]]
+ 00bd038c ["CALL", null, ["callee:00bdb180:8"]]
- 00bd02c4 bytes 832b0094
+ 00bd038c bytes 7d2b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b38531bfa4e6f49303318c999c2eb76"></a>

### [`00bd0850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0850.md) → [`00bd0918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0918.md) FUN_00bd0918

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd097c",
      "incomplete_value": true,
      "site": "00bd0990",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00bd08b4",
      "incomplete_value": true,
      "site": "00bd08c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:499:8"
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
      "00bd097c",
      "READ",
      [
        "storage",
        "00294499",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd097c",
      "READ",
      [
        "storage",
        "00294526",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0850.md#insn-00bd0894) · [`00bd08ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0850.md#insn-00bd08ac) · [`00bd08dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0850.md#insn-00bd08dc)
- 新版 `00bd095c`（命令位置の公開資料なし） · `00bd0974`（命令位置の公開資料なし） · `00bd09a4`（命令位置の公開資料なし）

~~~diff
- 00bd0894 ["INT_ADD", "register:40f0:8", ["const:bd0894:8", "const:4:8"]]
- 00bd0894 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd095c ["INT_ADD", "register:40f0:8", ["const:bd095c:8", "const:4:8"]]
+ 00bd095c ["CALL", null, ["callee:00bdd200:8"]]
- 00bd0894 bytes 2f320094
+ 00bd095c bytes 29320094
- 00bd08ac ["COPY", "tmp:0:8", ["const:499:8"]]
- 00bd08ac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bd08ac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bd08ac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bd0974 ["COPY", "tmp:0:8", ["const:526:8"]]
+ 00bd0974 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bd0974 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bd0974 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bd08ac bytes 4a651291
+ 00bd0974 bytes 4a991491
- 00bd08dc ["INT_ADD", "register:40f0:8", ["const:bd08dc:8", "const:4:8"]]
- 00bd08dc ["CALL", null, ["callee:00bc8290:8"]]
+ 00bd09a4 ["INT_ADD", "register:40f0:8", ["const:bd09a4:8", "const:4:8"]]
+ 00bd09a4 ["CALL", null, ["callee:00bc8290:8"]]
- 00bd08dc bytes 3bdeff97
+ 00bd09a4 bytes 3bdeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fb434b6dd96def4cea4a07d1a13e1a0"></a>

### [`00bd0b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0b4c.md) → [`00bd0c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd0c14.md) FUN_00bd0c14

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd0dac",
      "incomplete_value": true,
      "site": "00bd0db8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5f5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0ce4",
      "incomplete_value": true,
      "site": "00bd0cf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5fe:8"
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
      "definition_site": "00bd0e14",
      "incomplete_value": true,
      "site": "00bd0e20",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:79d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd0d4c",
      "incomplete_value": true,
      "site": "00bd0d58",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:7a6:8"
              ]
            ]
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
      "00bd0dac",
      "READ",
      [
        "storage",
        "002ac5fe",
        null,
        "string"
      ]
    ],
    [
      "00bd0e14",
      "READ",
      [
        "storage",
        "002ad7a6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd0dac",
      "READ",
      [
        "storage",
        "002ac5f5",
        null,
        "string"
      ]
    ],
    [
      "00bd0e14",
      "READ",
      [
        "storage",
        "002ad79d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0b4c.md#insn-00bd0b9c) · [`00bd0bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0b4c.md#insn-00bd0bc4) · [`00bd0bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd0/00bd0b4c.md#insn-00bd0bfc)
- 新版 `00bd0c64`（命令位置の公開資料なし） · `00bd0c8c`（命令位置の公開資料なし） · `00bd0cc4`（命令位置の公開資料なし）

~~~diff
- 00bd0b9c ["INT_ADD", "register:40f0:8", ["const:bd0b9c:8", "const:4:8"]]
- 00bd0b9c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd0c64 ["INT_ADD", "register:40f0:8", ["const:bd0c64:8", "const:4:8"]]
+ 00bd0c64 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd0b9c bytes 6d310094
+ 00bd0c64 bytes 67310094
- 00bd0bc4 ["INT_ADD", "register:40f0:8", ["const:bd0bc4:8", "const:4:8"]]
- 00bd0bc4 ["CALL", null, ["callee:00bc8290:8"]]
+ 00bd0c8c ["INT_ADD", "register:40f0:8", ["const:bd0c8c:8", "const:4:8"]]
+ 00bd0c8c ["CALL", null, ["callee:00bc8290:8"]]
- 00bd0bc4 bytes 81ddff97
+ 00bd0c8c bytes 81ddff97
- 00bd0bfc ["INT_ADD", "register:40f0:8", ["const:bd0bfc:8", "const:4:8"]]
- 00bd0bfc ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd0cc4 ["INT_ADD", "register:40f0:8", ["const:bd0cc4:8", "const:4:8"]]
+ 00bd0cc4 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd0bfc bytes 55310094
+ 00bd0cc4 bytes 4f310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f1a531f3246b877f24a8069bd63ee50"></a>

### [`00bd10c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd10c4.md) → [`00bd118c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd118c.md) FUN_00bd118c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 8件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbfe64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 8件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.24% / 新版 97.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd1384",
      "incomplete_value": false,
      "site": "00bd1384",
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
      "definition_site": "00bd12bc",
      "incomplete_value": false,
      "site": "00bd12bc",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd13a8",
      "incomplete_value": false,
      "site": "00bd13a8",
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
            "const:bf1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd12e0",
      "incomplete_value": false,
      "site": "00bd12e0",
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
            "const:b64:8"
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
      "definition_site": "00bd1434",
      "incomplete_value": false,
      "site": "00bd1434",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd136c",
      "incomplete_value": false,
      "site": "00bd136c",
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
            "const:9a8:8"
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
      "00bd1384",
      "DATA",
      [
        "storage",
        "00c17798",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd13a8",
      "DATA",
      [
        "storage",
        "00298b64",
        null,
        "string"
      ]
    ],
    [
      "00bd1434",
      "DATA",
      [
        "storage",
        "00c199a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1384",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd13a8",
      "DATA",
      [
        "storage",
        "00298bf1",
        null,
        "string"
      ]
    ],
    [
      "00bd1434",
      "DATA",
      [
        "storage",
        "00c19a58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd155c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd10c4.md#insn-00bd155c) · [`00bd11c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd10c4.md#insn-00bd11c8) · [`00bd1210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd10c4.md#insn-00bd1210)
- 新版 `00bd1624`（命令位置の公開資料なし） · `00bd1290`（命令位置の公開資料なし） · `00bd12d8`（命令位置の公開資料なし）

~~~diff
- 00bd155c ["INT_ADD", "register:40f0:8", ["const:bd155c:8", "const:4:8"]]
- 00bd155c ["CALL", null, ["callee:00bdb160:8"]]
+ 00bd1624 ["INT_ADD", "register:40f0:8", ["const:bd1624:8", "const:4:8"]]
+ 00bd1624 ["CALL", null, ["callee:00bdb160:8"]]
- 00bd155c bytes d5260094
+ 00bd1624 bytes cf260094
- 00bd11c8 ["INT_ADD", "register:40f0:8", ["const:bd11c8:8", "const:4:8"]]
- 00bd11c8 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd1290 ["INT_ADD", "register:40f0:8", ["const:bd1290:8", "const:4:8"]]
+ 00bd1290 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd11c8 bytes e22f0094
+ 00bd1290 bytes dc2f0094
- 00bd1210 ["INT_ADD", "register:40f0:8", ["const:bd1210:8", "const:4:8"]]
- 00bd1210 ["CALL", null, ["callee:00bbde18:8"]]
+ 00bd12d8 ["INT_ADD", "register:40f0:8", ["const:bd12d8:8", "const:4:8"]]
+ 00bd12d8 ["CALL", null, ["callee:00bbde18:8"]]
- 00bd1210 bytes d0b2ff97
+ 00bd12d8 bytes d0b2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c69e539bdfffdc80e8283c61250e446"></a>

### [`00bd166c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd166c.md) → [`00bd1734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1734.md) FUN_00bd1734

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bd166c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd166c.md) · 呼出先 5件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bc1648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1648.md) [`00bd166c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd166c.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 2件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bd1734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1734.md) · 呼出先 5件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) [`00bd1734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1734.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.97% / 新版 97.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd19b4",
      "incomplete_value": false,
      "site": "00bd19b4",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd18ec",
      "incomplete_value": false,
      "site": "00bd18ec",
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
            "const:b68:8"
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
      "definition_site": "00bd1ac4",
      "incomplete_value": false,
      "site": "00bd1ac4",
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
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd19fc",
      "incomplete_value": false,
      "site": "00bd19fc",
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
            "const:af8:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd192c",
      "DATA",
      [
        "storage",
        "00c19bd8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd19b4",
      "DATA",
      [
        "storage",
        "00c19b68",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd1ac4",
      "DATA",
      [
        "storage",
        "00c19af8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd192c",
      "DATA",
      [
        "storage",
        "00c19c88",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd19b4",
      "DATA",
      [
        "storage",
        "00c19c18",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd1ac4",
      "DATA",
      [
        "storage",
        "00c19ba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd166c.md#insn-00bd1788) · [`00bd1804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd166c.md#insn-00bd1804) · [`00bd182c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd166c.md#insn-00bd182c)
- 新版 `00bd1850`（命令位置の公開資料なし） · `00bd18cc`（命令位置の公開資料なし） · `00bd18f4`（命令位置の公開資料なし）

~~~diff
- 00bd1788 ["INT_ADD", "register:40f0:8", ["const:bd1788:8", "const:4:8"]]
- 00bd1788 ["CALL", null, ["callee:00bc1710:8"]]
+ 00bd1850 ["INT_ADD", "register:40f0:8", ["const:bd1850:8", "const:4:8"]]
+ 00bd1850 ["CALL", null, ["callee:00bc1710:8"]]
- 00bd1788 bytes b0bfff97
+ 00bd1850 bytes b0bfff97
- 00bd1804 ["INT_ADD", "register:40f0:8", ["const:bd1804:8", "const:4:8"]]
- 00bd1804 ["CALL", null, ["callee:00bbde18:8"]]
+ 00bd18cc ["INT_ADD", "register:40f0:8", ["const:bd18cc:8", "const:4:8"]]
+ 00bd18cc ["CALL", null, ["callee:00bbde18:8"]]
- 00bd1804 bytes 53b1ff97
+ 00bd18cc bytes 53b1ff97
- 00bd182c ["INT_ADD", "register:40f0:8", ["const:bd182c:8", "const:4:8"]]
- 00bd182c ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd18f4 ["INT_ADD", "register:40f0:8", ["const:bd18f4:8", "const:4:8"]]
+ 00bd18f4 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd182c bytes 292e0094
+ 00bd18f4 bytes 232e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86a4f8c78bb2053166b29d8f1e8895cc"></a>

### [`00bd1a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1a44.md) → [`00bd1b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1b0c.md) FUN_00bd1b0c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd1b78",
      "incomplete_value": false,
      "site": "00bd1b78",
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
      "definition_site": "00bd1ab0",
      "incomplete_value": false,
      "site": "00bd1ab0",
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
      "00bd1b78",
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
      "00bd1b78",
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

- 旧版 [`00bd1a78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1a44.md#insn-00bd1a78) · [`00bd1aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1a44.md#insn-00bd1aa0) · [`00bd1aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1a44.md#insn-00bd1aa8)
- 新版 `00bd1b40`（命令位置の公開資料なし） · `00bd1b68`（命令位置の公開資料なし） · `00bd1b70`（命令位置の公開資料なし）

~~~diff
- 00bd1a78 ["INT_ADD", "register:40f0:8", ["const:bd1a78:8", "const:4:8"]]
- 00bd1a78 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd1b40 ["INT_ADD", "register:40f0:8", ["const:bd1b40:8", "const:4:8"]]
+ 00bd1b40 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd1a78 bytes 962d0094
+ 00bd1b40 bytes 902d0094
- 00bd1aa0 ["INT_ADD", "register:40f0:8", ["const:bd1aa0:8", "const:4:8"]]
- 00bd1aa0 ["CALL", null, ["callee:00bdb140:8"]]
+ 00bd1b68 ["INT_ADD", "register:40f0:8", ["const:bd1b68:8", "const:4:8"]]
+ 00bd1b68 ["CALL", null, ["callee:00bdb140:8"]]
- 00bd1aa0 bytes 7c250094
+ 00bd1b68 bytes 76250094
- 00bd1aa8 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bd1aa8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd1aa8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd1aa8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd1b70 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bd1b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd1b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd1b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd1aa8 bytes 29611e91
+ 00bd1b70 bytes 29212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc9abd8e70d8faad0dad8f6d5370d92c"></a>

### [`00bd1af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1af0.md) → [`00bd1bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1bb8.md) FUN_00bd1bb8

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd1c24",
      "incomplete_value": false,
      "site": "00bd1c24",
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
      "definition_site": "00bd1b5c",
      "incomplete_value": false,
      "site": "00bd1b5c",
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
      "00bd1c24",
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
      "00bd1c24",
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

- 旧版 [`00bd1b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1af0.md#insn-00bd1b24) · [`00bd1b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1af0.md#insn-00bd1b4c) · [`00bd1b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1af0.md#insn-00bd1b54)
- 新版 `00bd1bec`（命令位置の公開資料なし） · `00bd1c14`（命令位置の公開資料なし） · `00bd1c1c`（命令位置の公開資料なし）

~~~diff
- 00bd1b24 ["INT_ADD", "register:40f0:8", ["const:bd1b24:8", "const:4:8"]]
- 00bd1b24 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd1bec ["INT_ADD", "register:40f0:8", ["const:bd1bec:8", "const:4:8"]]
+ 00bd1bec ["CALL", null, ["callee:00bdd180:8"]]
- 00bd1b24 bytes 6b2d0094
+ 00bd1bec bytes 652d0094
- 00bd1b4c ["INT_ADD", "register:40f0:8", ["const:bd1b4c:8", "const:4:8"]]
- 00bd1b4c ["CALL", null, ["callee:00bdb140:8"]]
+ 00bd1c14 ["INT_ADD", "register:40f0:8", ["const:bd1c14:8", "const:4:8"]]
+ 00bd1c14 ["CALL", null, ["callee:00bdb140:8"]]
- 00bd1b4c bytes 51250094
+ 00bd1c14 bytes 4b250094
- 00bd1b54 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bd1b54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd1b54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd1b54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd1c1c ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bd1c1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd1c1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd1c1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd1b54 bytes 29611e91
+ 00bd1c1c bytes 29212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc527407e5c09b8e10d6be07dd49bc59"></a>

### [`00bd1b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1b9c.md) → [`00bd1c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1c64.md) FUN_00bd1c64

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd1cd0",
      "incomplete_value": false,
      "site": "00bd1cd0",
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
      "definition_site": "00bd1c08",
      "incomplete_value": false,
      "site": "00bd1c08",
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
      "00bd1cd0",
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
      "00bd1cd0",
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

- 旧版 [`00bd1bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1b9c.md#insn-00bd1bd0) · [`00bd1bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1b9c.md#insn-00bd1bf8) · [`00bd1c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1b9c.md#insn-00bd1c00)
- 新版 `00bd1c98`（命令位置の公開資料なし） · `00bd1cc0`（命令位置の公開資料なし） · `00bd1cc8`（命令位置の公開資料なし）

~~~diff
- 00bd1bd0 ["INT_ADD", "register:40f0:8", ["const:bd1bd0:8", "const:4:8"]]
- 00bd1bd0 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd1c98 ["INT_ADD", "register:40f0:8", ["const:bd1c98:8", "const:4:8"]]
+ 00bd1c98 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd1bd0 bytes 402d0094
+ 00bd1c98 bytes 3a2d0094
- 00bd1bf8 ["INT_ADD", "register:40f0:8", ["const:bd1bf8:8", "const:4:8"]]
- 00bd1bf8 ["CALL", null, ["callee:00bdb140:8"]]
+ 00bd1cc0 ["INT_ADD", "register:40f0:8", ["const:bd1cc0:8", "const:4:8"]]
+ 00bd1cc0 ["CALL", null, ["callee:00bdb140:8"]]
- 00bd1bf8 bytes 26250094
+ 00bd1cc0 bytes 20250094
- 00bd1c00 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bd1c00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd1c00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd1c00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd1cc8 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bd1cc8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd1cc8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd1cc8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd1c00 bytes 29611e91
+ 00bd1cc8 bytes 29212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3bba126ce8467ceb1636add0d0a127f"></a>

### [`00bd1c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1c48.md) → [`00bd1d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1d10.md) FUN_00bd1d10

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd1d78",
      "incomplete_value": false,
      "site": "00bd1d78",
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
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1cb0",
      "incomplete_value": false,
      "site": "00bd1cb0",
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
            "const:c48:8"
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
      "00bd1d78",
      "DATA",
      [
        "storage",
        "00c19c48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1d78",
      "DATA",
      [
        "storage",
        "00c19cf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1c48.md#insn-00bd1c80) · [`00bd1ca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1c48.md#insn-00bd1ca4) · [`00bd1cf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1c48.md#insn-00bd1cf0)
- 新版 `00bd1d48`（命令位置の公開資料なし） · `00bd1d6c`（命令位置の公開資料なし） · `00bd1db8`（命令位置の公開資料なし）

~~~diff
- 00bd1c80 ["INT_ADD", "register:40f0:8", ["const:bd1c80:8", "const:4:8"]]
- 00bd1c80 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd1d48 ["INT_ADD", "register:40f0:8", ["const:bd1d48:8", "const:4:8"]]
+ 00bd1d48 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd1c80 bytes 142d0094
+ 00bd1d48 bytes 0e2d0094
- 00bd1ca4 ["COPY", "tmp:0:8", ["const:c48:8"]]
- 00bd1ca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1ca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1ca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd1d6c ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00bd1d6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1d6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1d6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd1ca4 bytes 08213191
+ 00bd1d6c bytes 08e13391
- 00bd1cf0 ["INT_ADD", "register:40f0:8", ["const:bd1cf0:8", "const:4:8"]]
- 00bd1cf0 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd1db8 ["INT_ADD", "register:40f0:8", ["const:bd1db8:8", "const:4:8"]]
+ 00bd1db8 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd1cf0 bytes f8240094
+ 00bd1db8 bytes f2240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29d96a49562b3d88a92a92860bc1939f"></a>

### [`00bd1cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1cf4.md) → [`00bd1dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1dbc.md) FUN_00bd1dbc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd1e20",
      "incomplete_value": true,
      "site": "00bd1e20",
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
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1d58",
      "incomplete_value": true,
      "site": "00bd1d58",
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
            "const:cb8:8"
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
      "00bd1e20",
      "DATA",
      [
        "storage",
        "00c19cb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1e20",
      "DATA",
      [
        "storage",
        "00c19d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1d28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1cf4.md#insn-00bd1d28) · [`00bd1d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1cf4.md#insn-00bd1d4c) · [`00bd1d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1cf4.md#insn-00bd1d90)
- 新版 `00bd1df0`（命令位置の公開資料なし） · `00bd1e14`（命令位置の公開資料なし） · `00bd1e58`（命令位置の公開資料なし）

~~~diff
- 00bd1d28 ["INT_ADD", "register:40f0:8", ["const:bd1d28:8", "const:4:8"]]
- 00bd1d28 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd1df0 ["INT_ADD", "register:40f0:8", ["const:bd1df0:8", "const:4:8"]]
+ 00bd1df0 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd1d28 bytes ea2c0094
+ 00bd1df0 bytes e42c0094
- 00bd1d4c ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 00bd1d4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1d4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1d4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd1e14 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00bd1e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd1d4c bytes 08e13291
+ 00bd1e14 bytes 08a13591
- 00bd1d90 ["INT_ADD", "register:40f0:8", ["const:bd1d90:8", "const:4:8"]]
- 00bd1d90 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd1e58 ["INT_ADD", "register:40f0:8", ["const:bd1e58:8", "const:4:8"]]
+ 00bd1e58 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd1d90 bytes d0240094
+ 00bd1e58 bytes ca240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9bc53a4bd2f4decf948a324c5249bb6"></a>

### [`00bd1d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1d94.md) → [`00bd1e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1e5c.md) FUN_00bd1e5c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd1ec4",
      "incomplete_value": false,
      "site": "00bd1ec4",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1dfc",
      "incomplete_value": false,
      "site": "00bd1dfc",
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
            "const:d28:8"
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
      "00bd1ec4",
      "DATA",
      [
        "storage",
        "00c19d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1ec4",
      "DATA",
      [
        "storage",
        "00c19dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1d94.md#insn-00bd1dcc) · [`00bd1df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1d94.md#insn-00bd1df0) · [`00bd1e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1d94.md#insn-00bd1e3c)
- 新版 `00bd1e94`（命令位置の公開資料なし） · `00bd1eb8`（命令位置の公開資料なし） · `00bd1f04`（命令位置の公開資料なし）

~~~diff
- 00bd1dcc ["INT_ADD", "register:40f0:8", ["const:bd1dcc:8", "const:4:8"]]
- 00bd1dcc ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd1e94 ["INT_ADD", "register:40f0:8", ["const:bd1e94:8", "const:4:8"]]
+ 00bd1e94 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd1dcc bytes c12c0094
+ 00bd1e94 bytes bb2c0094
- 00bd1df0 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00bd1df0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1df0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1df0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd1eb8 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00bd1eb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1eb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1eb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd1df0 bytes 08a13491
+ 00bd1eb8 bytes 08613791
- 00bd1e3c ["INT_ADD", "register:40f0:8", ["const:bd1e3c:8", "const:4:8"]]
- 00bd1e3c ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd1f04 ["INT_ADD", "register:40f0:8", ["const:bd1f04:8", "const:4:8"]]
+ 00bd1f04 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd1e3c bytes a5240094
+ 00bd1f04 bytes 9f240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f845975e987ded38c285a778ef2855a"></a>

### [`00bd1e40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1e40.md) → [`00bd1f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1f08.md) FUN_00bd1f08

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd1f70",
      "incomplete_value": true,
      "site": "00bd1f70",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd1ea8",
      "incomplete_value": true,
      "site": "00bd1ea8",
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
            "const:d98:8"
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
      "00bd1f70",
      "DATA",
      [
        "storage",
        "00c19d98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd1f70",
      "DATA",
      [
        "storage",
        "00c19e48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1e40.md#insn-00bd1e78) · [`00bd1e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1e40.md#insn-00bd1e9c) · [`00bd1ee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1e40.md#insn-00bd1ee8)
- 新版 `00bd1f40`（命令位置の公開資料なし） · `00bd1f64`（命令位置の公開資料なし） · `00bd1fb0`（命令位置の公開資料なし）

~~~diff
- 00bd1e78 ["INT_ADD", "register:40f0:8", ["const:bd1e78:8", "const:4:8"]]
- 00bd1e78 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd1f40 ["INT_ADD", "register:40f0:8", ["const:bd1f40:8", "const:4:8"]]
+ 00bd1f40 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd1e78 bytes 962c0094
+ 00bd1f40 bytes 902c0094
- 00bd1e9c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00bd1e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd1f64 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00bd1f64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1f64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd1f64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd1e9c bytes 08613691
+ 00bd1f64 bytes 08213991
- 00bd1ee8 ["INT_ADD", "register:40f0:8", ["const:bd1ee8:8", "const:4:8"]]
- 00bd1ee8 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd1fb0 ["INT_ADD", "register:40f0:8", ["const:bd1fb0:8", "const:4:8"]]
+ 00bd1fb0 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd1ee8 bytes 7a240094
+ 00bd1fb0 bytes 74240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-914a633a1bbfd443d383e5e7312afe95"></a>

### [`00bd1eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1eec.md) → [`00bd1fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1fb4.md) FUN_00bd1fb4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 6件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) [`00bd38b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd38b4.md) [`00bd3954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3954.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 6件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) [`00bd397c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd397c.md) [`00bd3a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3a1c.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.57% / 新版 96.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd20b0",
      "incomplete_value": false,
      "site": "00bd20b0",
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
      "definition_site": "00bd1fe8",
      "incomplete_value": false,
      "site": "00bd1fe8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd218c",
      "incomplete_value": false,
      "site": "00bd218c",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd20c4",
      "incomplete_value": false,
      "site": "00bd20c4",
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
            "const:e78:8"
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
      "definition_site": "00bd2228",
      "incomplete_value": false,
      "site": "00bd2228",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2160",
      "incomplete_value": false,
      "site": "00bd2160",
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
            "const:e78:8"
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
      "00bd20b0",
      "DATA",
      [
        "storage",
        "00c17798",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd218c",
      "DATA",
      [
        "storage",
        "00c19e78",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd2228",
      "DATA",
      [
        "storage",
        "00c19e78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd20b0",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd218c",
      "DATA",
      [
        "storage",
        "00c19f28",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd2228",
      "DATA",
      [
        "storage",
        "00c19f28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1eec.md#insn-00bd1fb0) · [`00bd1fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1eec.md#insn-00bd1fe4) · [`00bd2054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1eec.md#insn-00bd2054)
- 新版 `00bd2078`（命令位置の公開資料なし） · `00bd20ac`（命令位置の公開資料なし） · `00bd211c`（命令位置の公開資料なし）

~~~diff
- 00bd1fb0 ["INT_ADD", "register:40f0:8", ["const:bd1fb0:8", "const:4:8"]]
- 00bd1fb0 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd2078 ["INT_ADD", "register:40f0:8", ["const:bd2078:8", "const:4:8"]]
+ 00bd2078 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd1fb0 bytes 482c0094
+ 00bd2078 bytes 422c0094
- 00bd1fe4 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bd1fe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1fe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd1fe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd20ac ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bd20ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd20ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd20ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd1fe4 bytes 08611e91
+ 00bd20ac bytes 08212191
- 00bd2054 ["INT_ADD", "register:40f0:8", ["const:bd2054:8", "const:4:8"]]
- 00bd2054 ["CALL", null, ["callee:00bd397c:8"]]
+ 00bd211c ["INT_ADD", "register:40f0:8", ["const:bd211c:8", "const:4:8"]]
+ 00bd211c ["CALL", null, ["callee:00bd397c:8"]]
- 00bd2054 bytes 18060094
+ 00bd211c bytes 18060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33198302647e51c4990a559488dfec72"></a>

### [`00bd21a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd21a8.md) → [`00bd2270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2270.md) FUN_00bd2270

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 3件 [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 3件 [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bd237c",
      "incomplete_value": false,
      "site": "00bd237c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd22b4",
      "incomplete_value": false,
      "site": "00bd22b4",
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
            "const:fc8:8"
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
      "00bd237c",
      "DATA",
      [
        "storage",
        "00c19fc8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd239c",
      "DATA",
      [
        "storage",
        "002a3070",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd237c",
      "DATA",
      [
        "storage",
        "00c1a078",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd239c",
      "DATA",
      [
        "storage",
        "002a3069",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd21a8.md#insn-00bd2220) · [`00bd2240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd21a8.md#insn-00bd2240) · [`00bd2258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd21a8.md#insn-00bd2258)
- 新版 `00bd22e8`（命令位置の公開資料なし） · `00bd2308`（命令位置の公開資料なし） · `00bd2320`（命令位置の公開資料なし）

~~~diff
- 00bd2220 ["COPY", "tmp:0:8", ["const:70:8"]]
- 00bd2220 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00bd2220 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00bd2220 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00bd22e8 ["COPY", "tmp:0:8", ["const:69:8"]]
+ 00bd22e8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00bd22e8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00bd22e8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00bd2220 bytes 73c20191
+ 00bd22e8 bytes 73a60191
- 00bd2240 ["COPY", "tmp:0:8", ["const:75b:8"]]
- 00bd2240 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00bd2240 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00bd2240 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00bd2308 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00bd2308 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00bd2308 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00bd2308 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00bd2240 bytes 736e1d91
+ 00bd2308 bytes 73a21f91
- 00bd2258 ["INT_ADD", "register:40f0:8", ["const:bd2258:8", "const:4:8"]]
- 00bd2258 ["CALL", null, ["callee:00bbf358:8"]]
+ 00bd2320 ["INT_ADD", "register:40f0:8", ["const:bd2320:8", "const:4:8"]]
+ 00bd2320 ["CALL", null, ["callee:00bbf358:8"]]
- 00bd2258 bytes 0eb4ff97
+ 00bd2320 bytes 0eb4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea14e238c5a9eefb5da5a511a310267d"></a>

### [`00bd22f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd22f8.md) → [`00bd23c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd23c0.md) FUN_00bd23c0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd2428",
      "incomplete_value": false,
      "site": "00bd2428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2360",
      "incomplete_value": false,
      "site": "00bd2360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "00bd2428",
      "DATA",
      [
        "storage",
        "00c1a038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd2428",
      "DATA",
      [
        "storage",
        "00c1a0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd232c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd22f8.md#insn-00bd232c) · [`00bd2358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd22f8.md#insn-00bd2358) · [`00bd23a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd22f8.md#insn-00bd23a0)
- 新版 `00bd23f4`（命令位置の公開資料なし） · `00bd2420`（命令位置の公開資料なし） · `00bd2468`（命令位置の公開資料なし）

~~~diff
- 00bd232c ["INT_ADD", "register:40f0:8", ["const:bd232c:8", "const:4:8"]]
- 00bd232c ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd23f4 ["INT_ADD", "register:40f0:8", ["const:bd23f4:8", "const:4:8"]]
+ 00bd23f4 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd232c bytes 692b0094
+ 00bd23f4 bytes 632b0094
- 00bd2358 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00bd2358 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2358 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2358 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd2420 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00bd2420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd2358 bytes 08e10091
+ 00bd2420 bytes 08a10391
- 00bd23a0 ["INT_ADD", "register:40f0:8", ["const:bd23a0:8", "const:4:8"]]
- 00bd23a0 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd2468 ["INT_ADD", "register:40f0:8", ["const:bd2468:8", "const:4:8"]]
+ 00bd2468 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd23a0 bytes 4c230094
+ 00bd2468 bytes 46230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9654e83837bdc61eac746eee6d5be29d"></a>

### [`00bd23a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd23a4.md) → [`00bd246c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd246c.md) FUN_00bd246c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd24e0",
      "incomplete_value": false,
      "site": "00bd24e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2418",
      "incomplete_value": false,
      "site": "00bd2418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
      "00bd24e0",
      "DATA",
      [
        "storage",
        "00c1a0a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd24e0",
      "DATA",
      [
        "storage",
        "00c1a158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd23dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd23a4.md#insn-00bd23dc) · [`00bd2408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd23a4.md#insn-00bd2408) · [`00bd245c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd23a4.md#insn-00bd245c)
- 新版 `00bd24a4`（命令位置の公開資料なし） · `00bd24d0`（命令位置の公開資料なし） · `00bd2524`（命令位置の公開資料なし）

~~~diff
- 00bd23dc ["INT_ADD", "register:40f0:8", ["const:bd23dc:8", "const:4:8"]]
- 00bd23dc ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd24a4 ["INT_ADD", "register:40f0:8", ["const:bd24a4:8", "const:4:8"]]
+ 00bd24a4 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd23dc bytes 3d2b0094
+ 00bd24a4 bytes 372b0094
- 00bd2408 ["COPY", "tmp:0:8", ["const:a8:8"]]
- 00bd2408 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bd2408 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bd2408 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bd24d0 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 00bd24d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bd24d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bd24d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bd2408 bytes 4aa10291
+ 00bd24d0 bytes 4a610591
- 00bd245c ["INT_ADD", "register:40f0:8", ["const:bd245c:8", "const:4:8"]]
- 00bd245c ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd2524 ["INT_ADD", "register:40f0:8", ["const:bd2524:8", "const:4:8"]]
+ 00bd2524 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd245c bytes 1d230094
+ 00bd2524 bytes 17230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d3cb0fa507ef36c66a6077a311a11cd"></a>

### [`00bd2460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2460.md) → [`00bd2528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2528.md) FUN_00bd2528

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd25ac",
      "incomplete_value": false,
      "site": "00bd25ac",
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
            "const:8e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd24e4",
      "incomplete_value": false,
      "site": "00bd24e4",
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
            "const:854:8"
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
      "00bd258c",
      "DATA",
      [
        "storage",
        "00c19d98",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd25ac",
      "DATA",
      [
        "storage",
        "00297854",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd258c",
      "DATA",
      [
        "storage",
        "00c19e48",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd25ac",
      "DATA",
      [
        "storage",
        "002978e1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2460.md#insn-00bd2494) · [`00bd24b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2460.md#insn-00bd24b8) · [`00bd24dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2460.md#insn-00bd24dc)
- 新版 `00bd255c`（命令位置の公開資料なし） · `00bd2580`（命令位置の公開資料なし） · `00bd25a4`（命令位置の公開資料なし）

~~~diff
- 00bd2494 ["INT_ADD", "register:40f0:8", ["const:bd2494:8", "const:4:8"]]
- 00bd2494 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd255c ["INT_ADD", "register:40f0:8", ["const:bd255c:8", "const:4:8"]]
+ 00bd255c ["CALL", null, ["callee:00bdd180:8"]]
- 00bd2494 bytes 0f2b0094
+ 00bd255c bytes 092b0094
- 00bd24b8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00bd24b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd24b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd24b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd2580 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00bd2580 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2580 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2580 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd24b8 bytes 08613691
+ 00bd2580 bytes 08213991
- 00bd24dc ["COPY", "tmp:0:8", ["const:854:8"]]
- 00bd24dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd24dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd24dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd25a4 ["COPY", "tmp:0:8", ["const:8e1:8"]]
+ 00bd25a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd25a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd25a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd24dc bytes 29512191
+ 00bd25a4 bytes 29852391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-100ed774773628060b335108695447ce"></a>

### [`00bd2510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2510.md) → [`00bd25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd25d8.md) FUN_00bd25d8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bd263c",
      "incomplete_value": false,
      "site": "00bd263c",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2574",
      "incomplete_value": false,
      "site": "00bd2574",
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
            "const:d98:8"
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
      "00bd263c",
      "DATA",
      [
        "storage",
        "00c19d98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd263c",
      "DATA",
      [
        "storage",
        "00c19e48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2510.md#insn-00bd2544) · [`00bd2568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2510.md#insn-00bd2568) · [`00bd25bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2510.md#insn-00bd25bc)
- 新版 `00bd260c`（命令位置の公開資料なし） · `00bd2630`（命令位置の公開資料なし） · `00bd2684`（命令位置の公開資料なし）

~~~diff
- 00bd2544 ["INT_ADD", "register:40f0:8", ["const:bd2544:8", "const:4:8"]]
- 00bd2544 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd260c ["INT_ADD", "register:40f0:8", ["const:bd260c:8", "const:4:8"]]
+ 00bd260c ["CALL", null, ["callee:00bdd180:8"]]
- 00bd2544 bytes e32a0094
+ 00bd260c bytes dd2a0094
- 00bd2568 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00bd2568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd2568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd2630 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00bd2630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd2630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd2568 bytes 08613691
+ 00bd2630 bytes 08213991
- 00bd25bc ["INT_ADD", "register:40f0:8", ["const:bd25bc:8", "const:4:8"]]
- 00bd25bc ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd2684 ["INT_ADD", "register:40f0:8", ["const:bd2684:8", "const:4:8"]]
+ 00bd2684 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd25bc bytes c5220094
+ 00bd2684 bytes bf220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6735635ab1d6c367e7bc12b9c2a8abd"></a>

### [`00bd2a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2a24.md) → [`00bd2aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2aec.md) FUN_00bd2aec

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc8/00bc81c8.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc8/00bc8290.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.82% / 新版 97.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd2c7c",
      "incomplete_value": true,
      "site": "00bd2c88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5f5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd2bb4",
      "incomplete_value": true,
      "site": "00bd2bc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5fe:8"
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
      "00bd2c7c",
      "READ",
      [
        "storage",
        "002ac5fe",
        null,
        "string"
      ]
    ],
    [
      "00bd2ce4",
      "READ",
      [
        "storage",
        "002ad7a6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd2c7c",
      "READ",
      [
        "storage",
        "002ac5f5",
        null,
        "string"
      ]
    ],
    [
      "00bd2ce4",
      "READ",
      [
        "storage",
        "002ad79d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2a70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2a24.md#insn-00bd2a70) · [`00bd2a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2a24.md#insn-00bd2a98) · [`00bd2ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd2a24.md#insn-00bd2ad0)
- 新版 `00bd2b38`（命令位置の公開資料なし） · `00bd2b60`（命令位置の公開資料なし） · `00bd2b98`（命令位置の公開資料なし）

~~~diff
- 00bd2a70 ["INT_ADD", "register:40f0:8", ["const:bd2a70:8", "const:4:8"]]
- 00bd2a70 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd2b38 ["INT_ADD", "register:40f0:8", ["const:bd2b38:8", "const:4:8"]]
+ 00bd2b38 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd2a70 bytes b8290094
+ 00bd2b38 bytes b2290094
- 00bd2a98 ["INT_ADD", "register:40f0:8", ["const:bd2a98:8", "const:4:8"]]
- 00bd2a98 ["CALL", null, ["callee:00bc8290:8"]]
+ 00bd2b60 ["INT_ADD", "register:40f0:8", ["const:bd2b60:8", "const:4:8"]]
+ 00bd2b60 ["CALL", null, ["callee:00bc8290:8"]]
- 00bd2a98 bytes ccd5ff97
+ 00bd2b60 bytes ccd5ff97
- 00bd2ad0 ["INT_ADD", "register:40f0:8", ["const:bd2ad0:8", "const:4:8"]]
- 00bd2ad0 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd2b98 ["INT_ADD", "register:40f0:8", ["const:bd2b98:8", "const:4:8"]]
+ 00bd2b98 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd2ad0 bytes a0290094
+ 00bd2b98 bytes 9a290094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb391fec48934abb7e0d87778d8a5433"></a>

### [`00bd3138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3138.md) → [`00bd3200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3200.md) FUN_00bd3200

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd32d8",
      "incomplete_value": true,
      "site": "00bd32e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5f5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3210",
      "incomplete_value": true,
      "site": "00bd321c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5fe:8"
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
      "definition_site": "00bd3340",
      "incomplete_value": true,
      "site": "00bd334c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:79d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3278",
      "incomplete_value": true,
      "site": "00bd3284",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:7a6:8"
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
      "00bd32d8",
      "READ",
      [
        "storage",
        "002ac5fe",
        null,
        "string"
      ]
    ],
    [
      "00bd3340",
      "READ",
      [
        "storage",
        "002ad7a6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd32d8",
      "READ",
      [
        "storage",
        "002ac5f5",
        null,
        "string"
      ]
    ],
    [
      "00bd3340",
      "READ",
      [
        "storage",
        "002ad79d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd315c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3138.md#insn-00bd315c) · [`00bd3190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3138.md#insn-00bd3190) · [`00bd31f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3138.md#insn-00bd31f4)
- 新版 `00bd3224`（命令位置の公開資料なし） · `00bd3258`（命令位置の公開資料なし） · `00bd32bc`（命令位置の公開資料なし）

~~~diff
- 00bd315c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd315c ["INT_ADD", "register:40f0:8", ["const:bd315c:8", "const:4:8"]]
- 00bd315c ["CALLIND", null, ["register:0:8"]]
+ 00bd3224 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3224 ["INT_ADD", "register:40f0:8", ["const:bd3224:8", "const:4:8"]]
+ 00bd3224 ["CALLIND", null, ["register:0:8"]]
- 00bd315c bytes 00013fd6
+ 00bd3224 bytes 00013fd6
- 00bd3190 ["INT_ADD", "register:40f0:8", ["const:bd3190:8", "const:4:8"]]
- 00bd3190 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd3258 ["INT_ADD", "register:40f0:8", ["const:bd3258:8", "const:4:8"]]
+ 00bd3258 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd3190 bytes f0270094
+ 00bd3258 bytes ea270094
- 00bd31f4 ["INT_ADD", "register:40f0:8", ["const:bd31f4:8", "const:4:8"]]
- 00bd31f4 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd32bc ["INT_ADD", "register:40f0:8", ["const:bd32bc:8", "const:4:8"]]
+ 00bd32bc ["CALL", null, ["callee:00bdd200:8"]]
- 00bd31f4 bytes d7270094
+ 00bd32bc bytes d1270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f1831c0fb2bdcbe7f05d2b1daa4db34"></a>

### [`00bd3520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3520.md) → [`00bd35e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd35e8.md) FUN_00bd35e8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd3650",
      "incomplete_value": true,
      "site": "00bd365c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8ea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3588",
      "incomplete_value": true,
      "site": "00bd3594",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:85d:8"
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
      "00bd3650",
      "READ",
      [
        "storage",
        "0029785d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd3650",
      "READ",
      [
        "storage",
        "002978ea",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd356c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3520.md#insn-00bd356c) · [`00bd3580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3520.md#insn-00bd3580) · [`00bd35cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3520.md#insn-00bd35cc)
- 新版 `00bd3634`（命令位置の公開資料なし） · `00bd3648`（命令位置の公開資料なし） · `00bd3694`（命令位置の公開資料なし）

~~~diff
- 00bd356c ["INT_ADD", "register:40f0:8", ["const:bd356c:8", "const:4:8"]]
- 00bd356c ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd3634 ["INT_ADD", "register:40f0:8", ["const:bd3634:8", "const:4:8"]]
+ 00bd3634 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd356c bytes f9260094
+ 00bd3634 bytes f3260094
- 00bd3580 ["COPY", "tmp:0:8", ["const:85d:8"]]
- 00bd3580 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd3580 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd3580 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd3648 ["COPY", "tmp:0:8", ["const:8ea:8"]]
+ 00bd3648 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd3648 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd3648 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd3580 bytes 29752191
+ 00bd3648 bytes 29a92391
- 00bd35cc ["INT_ADD", "register:40f0:8", ["const:bd35cc:8", "const:4:8"]]
- 00bd35cc ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd3694 ["INT_ADD", "register:40f0:8", ["const:bd3694:8", "const:4:8"]]
+ 00bd3694 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd35cc bytes e1260094
+ 00bd3694 bytes db260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c240fd10dd8d2436fbc5ad0dd67d372e"></a>

### [`00bd38b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd38b4.md) → [`00bd397c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd397c.md) FUN_00bd397c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bd1eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1eec.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bd1fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1fb4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bd39e0",
      "incomplete_value": false,
      "site": "00bd39e0",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3918",
      "incomplete_value": false,
      "site": "00bd3918",
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
            "const:e08:8"
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
      "00bd39e0",
      "DATA",
      [
        "storage",
        "00c19e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd39e0",
      "DATA",
      [
        "storage",
        "00c19eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd38e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd38b4.md#insn-00bd38e8) · [`00bd390c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd38b4.md#insn-00bd390c) · [`00bd3950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd38b4.md#insn-00bd3950)
- 新版 `00bd39b0`（命令位置の公開資料なし） · `00bd39d4`（命令位置の公開資料なし） · `00bd3a18`（命令位置の公開資料なし）

~~~diff
- 00bd38e8 ["INT_ADD", "register:40f0:8", ["const:bd38e8:8", "const:4:8"]]
- 00bd38e8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd39b0 ["INT_ADD", "register:40f0:8", ["const:bd39b0:8", "const:4:8"]]
+ 00bd39b0 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd38e8 bytes fa250094
+ 00bd39b0 bytes f4250094
- 00bd390c ["COPY", "tmp:0:8", ["const:e08:8"]]
- 00bd390c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd390c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd390c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd39d4 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 00bd39d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd39d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd39d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd390c bytes 08213891
+ 00bd39d4 bytes 08e13a91
- 00bd3950 ["INT_ADD", "register:40f0:8", ["const:bd3950:8", "const:4:8"]]
- 00bd3950 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd3a18 ["INT_ADD", "register:40f0:8", ["const:bd3a18:8", "const:4:8"]]
+ 00bd3a18 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd3950 bytes e01d0094
+ 00bd3a18 bytes da1d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff4223ecab4b15f1849fa15dae6f0e3e"></a>

### [`00bd3954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3954.md) → [`00bd3a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3a1c.md) FUN_00bd3a1c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bd1eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1eec.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bd1fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1fb4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bd3a84",
      "incomplete_value": false,
      "site": "00bd3a84",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd39bc",
      "incomplete_value": false,
      "site": "00bd39bc",
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
            "const:e78:8"
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
      "00bd3a84",
      "DATA",
      [
        "storage",
        "00c19e78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd3a84",
      "DATA",
      [
        "storage",
        "00c19f28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd398c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3954.md#insn-00bd398c) · [`00bd39b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3954.md#insn-00bd39b0) · [`00bd39f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3954.md#insn-00bd39f8)
- 新版 `00bd3a54`（命令位置の公開資料なし） · `00bd3a78`（命令位置の公開資料なし） · `00bd3ac0`（命令位置の公開資料なし）

~~~diff
- 00bd398c ["INT_ADD", "register:40f0:8", ["const:bd398c:8", "const:4:8"]]
- 00bd398c ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd3a54 ["INT_ADD", "register:40f0:8", ["const:bd3a54:8", "const:4:8"]]
+ 00bd3a54 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd398c bytes d1250094
+ 00bd3a54 bytes cb250094
- 00bd39b0 ["COPY", "tmp:0:8", ["const:e78:8"]]
- 00bd39b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd39b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd39b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd3a78 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 00bd3a78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3a78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3a78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd39b0 bytes 08e13991
+ 00bd3a78 bytes 08a13c91
- 00bd39f8 ["INT_ADD", "register:40f0:8", ["const:bd39f8:8", "const:4:8"]]
- 00bd39f8 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd3ac0 ["INT_ADD", "register:40f0:8", ["const:bd3ac0:8", "const:4:8"]]
+ 00bd3ac0 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd39f8 bytes b61d0094
+ 00bd3ac0 bytes b01d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80e3337940756f3d6ee4b3ae3b1431f1"></a>

### [`00bd39fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd39fc.md) → [`00bd3ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3ac4.md) FUN_00bd3ac4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.06% / 新版 93.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd3b28",
      "incomplete_value": true,
      "site": "00bd3b34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:644:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3a60",
      "incomplete_value": true,
      "site": "00bd3a6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6d8:8"
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
      "definition_site": "00bd3b38",
      "incomplete_value": true,
      "site": "00bd3b38",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd3a70",
      "incomplete_value": true,
      "site": "00bd3a70",
      "value": [
        "LOAD",
        "8",
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
      "00bd3b28",
      "READ",
      [
        "storage",
        "002ae6d8",
        null,
        "string"
      ]
    ],
    [
      "00bd3b2c",
      "READ",
      [
        "storage",
        "002ae6dd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd3b28",
      "READ",
      [
        "storage",
        "002ae644",
        null,
        "string"
      ]
    ],
    [
      "00bd3b2c",
      "READ",
      [
        "storage",
        "002ae649",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd39fc.md#insn-00bd3a40) · [`00bd3a58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd39fc.md#insn-00bd3a58) · [`00bd3a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd39fc.md#insn-00bd3a90)
- 新版 `00bd3b08`（命令位置の公開資料なし） · `00bd3b20`（命令位置の公開資料なし） · `00bd3b58`（命令位置の公開資料なし）

~~~diff
- 00bd3a40 ["INT_ADD", "register:40f0:8", ["const:bd3a40:8", "const:4:8"]]
- 00bd3a40 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd3b08 ["INT_ADD", "register:40f0:8", ["const:bd3b08:8", "const:4:8"]]
+ 00bd3b08 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd3a40 bytes c4250094
+ 00bd3b08 bytes be250094
- 00bd3a58 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 00bd3a58 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bd3a58 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bd3a58 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bd3b20 ["COPY", "tmp:0:8", ["const:644:8"]]
+ 00bd3b20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bd3b20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bd3b20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bd3a58 bytes 4a611b91
+ 00bd3b20 bytes 4a111991
- 00bd3a90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd3a90 ["INT_ADD", "register:40f0:8", ["const:bd3a90:8", "const:4:8"]]
- 00bd3a90 ["CALLIND", null, ["register:0:8"]]
+ 00bd3b58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd3b58 ["INT_ADD", "register:40f0:8", ["const:bd3b58:8", "const:4:8"]]
+ 00bd3b58 ["CALLIND", null, ["register:0:8"]]
- 00bd3a90 bytes 00013fd6
+ 00bd3b58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a33032eb1c7497000c0c86d148011685"></a>

### [`00bd3c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3c80.md) → [`00bd3d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3d48.md) FUN_00bd3d48

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bd3db0",
      "incomplete_value": false,
      "site": "00bd3db0",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3ce8",
      "incomplete_value": false,
      "site": "00bd3ce8",
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
            "const:ee8:8"
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
      "00bd3db0",
      "DATA",
      [
        "storage",
        "00c19ee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd3db0",
      "DATA",
      [
        "storage",
        "00c19f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3c80.md#insn-00bd3cb8) · [`00bd3cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3c80.md#insn-00bd3cdc) · [`00bd3d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3c80.md#insn-00bd3d20)
- 新版 `00bd3d80`（命令位置の公開資料なし） · `00bd3da4`（命令位置の公開資料なし） · `00bd3de8`（命令位置の公開資料なし）

~~~diff
- 00bd3cb8 ["INT_ADD", "register:40f0:8", ["const:bd3cb8:8", "const:4:8"]]
- 00bd3cb8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd3d80 ["INT_ADD", "register:40f0:8", ["const:bd3d80:8", "const:4:8"]]
+ 00bd3d80 ["CALL", null, ["callee:00bdd180:8"]]
- 00bd3cb8 bytes 06250094
+ 00bd3d80 bytes 00250094
- 00bd3cdc ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 00bd3cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd3cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd3cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd3da4 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00bd3da4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3da4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd3da4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd3cdc bytes 08a13b91
+ 00bd3da4 bytes 08613e91
- 00bd3d20 ["INT_ADD", "register:40f0:8", ["const:bd3d20:8", "const:4:8"]]
- 00bd3d20 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bd3de8 ["INT_ADD", "register:40f0:8", ["const:bd3de8:8", "const:4:8"]]
+ 00bd3de8 ["CALL", null, ["callee:00bdb180:8"]]
- 00bd3d20 bytes ec1c0094
+ 00bd3de8 bytes e61c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0308f2f01ed6d3b548fa9bdc28014658"></a>

### [`00bd3d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d50.md) → [`00bd3e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3e18.md) FUN_00bd3e18

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd3f9c",
      "incomplete_value": false,
      "site": "00bd3fac",
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
            "const:326:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3ed4",
      "incomplete_value": false,
      "site": "00bd3ee4",
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
            "const:299:8"
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
      "definition_site": "00bd3fa4",
      "incomplete_value": false,
      "site": "00bd3fac",
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
      "definition_site": "00bd3edc",
      "incomplete_value": false,
      "site": "00bd3ee4",
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
    "ordinal": 5,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd3f9c",
      "PARAM",
      [
        "storage",
        "0029c299",
        null,
        "string"
      ]
    ],
    [
      "00bd3fa4",
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
      "00bd3f9c",
      "PARAM",
      [
        "storage",
        "0029c326",
        null,
        "string"
      ]
    ],
    [
      "00bd3fa4",
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

- 旧版 [`00bd3ee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d50.md#insn-00bd3ee4) · [`00bd3dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d50.md#insn-00bd3dac) · [`00bd3df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3d50.md#insn-00bd3df4)
- 新版 `00bd3fac`（命令位置の公開資料なし） · `00bd3e74`（命令位置の公開資料なし） · `00bd3ebc`（命令位置の公開資料なし）

~~~diff
- 00bd3ee4 ["INT_ADD", "register:40f0:8", ["const:bd3ee4:8", "const:4:8"]]
- 00bd3ee4 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bd3fac ["INT_ADD", "register:40f0:8", ["const:bd3fac:8", "const:4:8"]]
+ 00bd3fac ["CALL", null, ["callee:00bbb158:8"]]
- 00bd3ee4 bytes 6b9cff97
+ 00bd3fac bytes 6b9cff97
- 00bd3dac ["INT_ADD", "register:40f0:8", ["const:bd3dac:8", "const:4:8"]]
- 00bd3dac ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd3e74 ["INT_ADD", "register:40f0:8", ["const:bd3e74:8", "const:4:8"]]
+ 00bd3e74 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd3dac bytes e9240094
+ 00bd3e74 bytes e3240094
- 00bd3df4 ["INT_ADD", "register:40f0:8", ["const:bd3df4:8", "const:4:8"]]
- 00bd3df4 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd3ebc ["INT_ADD", "register:40f0:8", ["const:bd3ebc:8", "const:4:8"]]
+ 00bd3ebc ["CALL", null, ["callee:00bdd200:8"]]
- 00bd3df4 bytes d7240094
+ 00bd3ebc bytes d1240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0fb38db6fbdb4044bbf3f04c7c40664"></a>

### [`00bd3efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3efc.md) → [`00bd3fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd3/00bd3fc4.md) FUN_00bd3fc4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bd4030",
      "incomplete_value": false,
      "site": "00bd4030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3f68",
      "incomplete_value": false,
      "site": "00bd3f68",
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
            "const:f58:8"
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
      "00bd4030",
      "DATA",
      [
        "storage",
        "00c19f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bd4030",
      "DATA",
      [
        "storage",
        "00c1a008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3efc.md#insn-00bd3f34) · [`00bd3f5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3efc.md#insn-00bd3f5c) · [`00bd3f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd3/00bd3efc.md#insn-00bd3f60)
- 新版 `00bd3ffc`（命令位置の公開資料なし） · `00bd4024`（命令位置の公開資料なし） · `00bd4028`（命令位置の公開資料なし）

~~~diff
- 00bd3f34 ["INT_ADD", "register:40f0:8", ["const:bd3f34:8", "const:4:8"]]
- 00bd3f34 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bd3ffc ["INT_ADD", "register:40f0:8", ["const:bd3ffc:8", "const:4:8"]]
+ 00bd3ffc ["CALL", null, ["callee:00bdd180:8"]]
- 00bd3f34 bytes 67240094
+ 00bd3ffc bytes 61240094
- 00bd3f5c ["COPY", "register:4040:8", ["const:c19000:8"]]
+ 00bd4024 ["COPY", "register:4040:8", ["const:c1a000:8"]]
- 00bd3f5c bytes 280200d0
+ 00bd4024 bytes 280200d0
- 00bd3f60 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00bd3f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd3f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd3f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd4028 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 00bd4028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd4028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd4028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd3f60 bytes 08613d91
+ 00bd4028 bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89fd28ad6be397a5f38278a4788ca374"></a>

### [`00bd4bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4bf8.md) → [`00bd4cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4cc0.md) FUN_00bd4cc0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bd48c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd48c0.md) [`00bd4ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4ad0.md) · 呼出先 6件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md)
- 新版 呼出元 2件 [`00bd4988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4988.md) [`00bd4b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4b98.md) · 呼出先 6件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md)

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
      "definition_site": "00bd4e30",
      "incomplete_value": false,
      "site": "00bd4e40",
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
      "definition_site": "00bd4d68",
      "incomplete_value": false,
      "site": "00bd4d78",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd4e38",
      "incomplete_value": false,
      "site": "00bd4e40",
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
            "const:bb3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4d70",
      "incomplete_value": false,
      "site": "00bd4d78",
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
            "const:b26:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd4e30",
      "PARAM",
      [
        "storage",
        "002a207d",
        null,
        "string"
      ]
    ],
    [
      "00bd4e38",
      "PARAM",
      [
        "storage",
        "00298b26",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd4e30",
      "PARAM",
      [
        "storage",
        "002a210a",
        null,
        "string"
      ]
    ],
    [
      "00bd4e38",
      "PARAM",
      [
        "storage",
        "00298bb3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4d78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4bf8.md#insn-00bd4d78) · [`00bd4c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4bf8.md#insn-00bd4c50) · [`00bd4c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4bf8.md#insn-00bd4c90)
- 新版 `00bd4e40`（命令位置の公開資料なし） · `00bd4d18`（命令位置の公開資料なし） · `00bd4d58`（命令位置の公開資料なし）

~~~diff
- 00bd4d78 ["INT_ADD", "register:40f0:8", ["const:bd4d78:8", "const:4:8"]]
- 00bd4d78 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bd4e40 ["INT_ADD", "register:40f0:8", ["const:bd4e40:8", "const:4:8"]]
+ 00bd4e40 ["CALL", null, ["callee:00bbb158:8"]]
- 00bd4d78 bytes c698ff97
+ 00bd4e40 bytes c698ff97
- 00bd4c50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4c50 ["INT_ADD", "register:40f0:8", ["const:bd4c50:8", "const:4:8"]]
- 00bd4c50 ["CALLIND", null, ["register:0:8"]]
+ 00bd4d18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4d18 ["INT_ADD", "register:40f0:8", ["const:bd4d18:8", "const:4:8"]]
+ 00bd4d18 ["CALLIND", null, ["register:0:8"]]
- 00bd4c50 bytes 00013fd6
+ 00bd4d18 bytes 00013fd6
- 00bd4c90 ["INT_ADD", "register:40f0:8", ["const:bd4c90:8", "const:4:8"]]
- 00bd4c90 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd4d58 ["INT_ADD", "register:40f0:8", ["const:bd4d58:8", "const:4:8"]]
+ 00bd4d58 ["CALL", null, ["callee:00bdd200:8"]]
- 00bd4c90 bytes 30210094
+ 00bd4d58 bytes 2a210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9bb905d96d0f6068c2232b2e65ee184"></a>

### [`00bd5714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5714.md) → [`00bd57dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd57dc.md) FUN_00bd57dc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bd56c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd56c8.md) · 呼出先 3件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 1件 [`00bd5790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5790.md) · 呼出先 3件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 84.27% / 新版 84.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 6件, `store_destination` 3件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd582c",
      "incomplete_value": true,
      "site": "00bd582c",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5764",
      "incomplete_value": true,
      "site": "00bd5764",
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
            "const:688:8"
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
      "definition_site": "00bd5824",
      "incomplete_value": false,
      "site": "00bd582c",
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
            "const:75c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd575c",
      "incomplete_value": false,
      "site": "00bd5764",
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
            "const:69c:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5830",
      "incomplete_value": false,
      "site": "00bd5830",
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
            "const:75c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5768",
      "incomplete_value": false,
      "site": "00bd5768",
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
            "const:69c:8"
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
      "00bd57f4",
      "PARAM",
      [
        "storage",
        "010a3660",
        null,
        null
      ]
    ],
    [
      "00bd5800",
      "READ",
      [
        "storage",
        "010a3688",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd582c",
      "WRITE",
      [
        "storage",
        "010a3688",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd57f4",
      "PARAM",
      [
        "storage",
        "010a3720",
        null,
        null
      ]
    ],
    [
      "00bd5800",
      "READ",
      [
        "storage",
        "010a3748",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd582c",
      "WRITE",
      [
        "storage",
        "010a3748",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5714.md#insn-00bd5730) · [`00bd5764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5714.md#insn-00bd5764) · [`00bd5778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5714.md#insn-00bd5778)
- 新版 `00bd57f8`（命令位置の公開資料なし） · `00bd582c`（命令位置の公開資料なし） · `00bd5840`（命令位置の公開資料なし）

~~~diff
- 00bd5730 ["INT_ADD", "register:40f0:8", ["const:bd5730:8", "const:4:8"]]
- 00bd5730 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00bd57f8 ["INT_ADD", "register:40f0:8", ["const:bd57f8:8", "const:4:8"]]
+ 00bd57f8 ["CALL", null, ["callee:00bde7d0:8"]]
- 00bd5730 bytes fc230094
+ 00bd57f8 bytes f6230094
- 00bd5764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:688:8"]]
- 00bd5764 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:8"]]
+ 00bd582c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:748:8"]]
+ 00bd582c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:8"]]
- 00bd5764 bytes 0e4503f9
+ 00bd582c bytes 0ea503f9
- 00bd5778 ["COPY", "tmp:0:8", ["const:690:8"]]
- 00bd5778 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00bd5778 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00bd5778 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00bd5840 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00bd5840 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00bd5840 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00bd5840 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00bd5778 bytes 6b411a91
+ 00bd5840 bytes 6b411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4801e213c5c5118b3cb64257ddce506"></a>

### [`00bd589c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd589c.md) → [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md) FUN_00bd5964

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 6件 [`00bd4fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4fe8.md) [`00bd507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd507c.md) [`00bd5120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5120.md) [`00bd51b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd51b4.md) [`00bd52a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd52a0.md) · 呼出先 2件 [`00bd58c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd58c8.md) [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md)
- 新版 呼出元 6件 [`00bd50b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd50b0.md) [`00bd5144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5144.md) [`00bd51e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51e8.md) [`00bd527c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd527c.md) [`00bd5368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5368.md) · 呼出先 2件 [`00bd5990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5990.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd5974",
      "incomplete_value": true,
      "site": "00bd5974",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              "INT_ADD",
              [
                "live",
                "register:4000:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd58ac",
      "incomplete_value": true,
      "site": "00bd58ac",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              "INT_ADD",
              [
                "live",
                "register:4000:8"
              ]
            ]
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
      "definition_site": "00bd5980",
      "incomplete_value": true,
      "site": "00bd5984",
      "value": [
        "INT_LESSEQUAL",
        "1",
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
                "const:950:8"
              ]
            ]
          ],
          [
            "live",
            "register:4000:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd58b8",
      "incomplete_value": true,
      "site": "00bd58bc",
      "value": [
        "INT_LESSEQUAL",
        "1",
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
                "const:890:8"
              ]
            ]
          ],
          [
            "live",
            "register:4000:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bd58a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd589c.md#insn-00bd58a4) · [`00bd58b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd589c.md#insn-00bd58b4)
- 新版 `00bd596c`（命令位置の公開資料なし） · `00bd597c`（命令位置の公開資料なし）

~~~diff
- 00bd58a4 ["COPY", "tmp:0:8", ["const:690:8"]]
- 00bd58a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd58a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd58a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd596c ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00bd596c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd596c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd596c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd58a4 bytes 08411a91
+ 00bd596c bytes 08411d91
- 00bd58b4 ["COPY", "tmp:0:8", ["const:890:8"]]
- 00bd58b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd58b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd58b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd597c ["COPY", "tmp:0:8", ["const:950:8"]]
+ 00bd597c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd597c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd597c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd58b4 bytes 08412291
+ 00bd597c bytes 08412591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0e24e1d03a6d5af75ccf4ddbd809c18"></a>

### [`00bd58c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd58c8.md) → [`00bd5990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5990.md) FUN_00bd5990

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bd589c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd589c.md) · 呼出先 2件 [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 1件 [`00bd5964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5964.md) · 呼出先 2件 [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd5a20",
      "incomplete_value": true,
      "site": "00bd5a20",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5958",
      "incomplete_value": true,
      "site": "00bd5958",
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
            "const:688:8"
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
      "definition_site": "00bd5a6c",
      "incomplete_value": true,
      "site": "00bd5a6c",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd59a4",
      "incomplete_value": true,
      "site": "00bd59a4",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd59bc",
      "incomplete_value": true,
      "site": "00bd59bc",
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
      "definition_site": "00bd58f4",
      "incomplete_value": true,
      "site": "00bd58f4",
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
      "00bd59ac",
      "PARAM",
      [
        "storage",
        "010a3660",
        null,
        null
      ]
    ],
    [
      "00bd59b8",
      "READ",
      [
        "storage",
        "010a3688",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd59e0",
      "DATA",
      [
        "storage",
        "010a3692",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd59ac",
      "PARAM",
      [
        "storage",
        "010a3720",
        null,
        null
      ]
    ],
    [
      "00bd59b8",
      "READ",
      [
        "storage",
        "010a3748",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd59e0",
      "DATA",
      [
        "storage",
        "010a3752",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd58e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd58c8.md#insn-00bd58e8) · [`00bd5958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd58c8.md#insn-00bd5958) · [`00bd59a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd58c8.md#insn-00bd59a4)
- 新版 `00bd59b0`（命令位置の公開資料なし） · `00bd5a20`（命令位置の公開資料なし） · `00bd5a6c`（命令位置の公開資料なし）

~~~diff
- 00bd58e8 ["INT_ADD", "register:40f0:8", ["const:bd58e8:8", "const:4:8"]]
- 00bd58e8 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00bd59b0 ["INT_ADD", "register:40f0:8", ["const:bd59b0:8", "const:4:8"]]
+ 00bd59b0 ["CALL", null, ["callee:00bde7d0:8"]]
- 00bd58e8 bytes 8e230094
+ 00bd59b0 bytes 88230094
- 00bd5958 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:688:8"]]
- 00bd5958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00bd5a20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:748:8"]]
+ 00bd5a20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00bd5958 bytes 144503f9
+ 00bd5a20 bytes 14a503f9
- 00bd59a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:688:8"]]
- 00bd59a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00bd5a6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:748:8"]]
+ 00bd5a6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00bd59a4 bytes 144503f9
+ 00bd5a6c bytes 14a503f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33213a36cff1b160b90765cc66c7b799"></a>

### [`00bd5f68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5f68.md) → [`00bd6030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6030.md) __cxa_call_unexpected

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 18件 [`00bba918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba918.md) [`00bba964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md) [`00bbac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac28.md) [`00bd4ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4ecc.md) [`00bd4ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4ed8.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00bba9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9e0.md) [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bd4f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4f94.md) [`00bd4fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fa0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd6184",
      "incomplete_value": true,
      "site": "00bd6188",
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
      "definition_site": "00bd60bc",
      "incomplete_value": true,
      "site": "00bd60c0",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6198",
      "incomplete_value": true,
      "site": "00bd61ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd60d0",
      "incomplete_value": true,
      "site": "00bd60e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd61e4",
      "incomplete_value": true,
      "site": "00bd61ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd611c",
      "incomplete_value": true,
      "site": "00bd6124",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f30:8"
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
      "00bd6180",
      "READ",
      [
        "storage",
        "00c1bf28",
        null,
        "pointer"
      ]
    ],
    [
      "00bd6188",
      "DATA",
      [
        "storage",
        "00c167c0",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00bd6198",
      "READ",
      [
        "storage",
        "00c1bf30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bd6180",
      "READ",
      [
        "storage",
        "00c1bfd8",
        null,
        "pointer"
      ]
    ],
    [
      "00bd6188",
      "DATA",
      [
        "storage",
        "00c16870",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00bd6198",
      "READ",
      [
        "storage",
        "00c1bfe0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd60e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5f68.md#insn-00bd60e4) · [`00bd6124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5f68.md#insn-00bd6124) · [`00bd5f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5f68.md#insn-00bd5f90)
- 新版 `00bd61ac`（命令位置の公開資料なし） · `00bd61ec`（命令位置の公開資料なし） · `00bd6058`（命令位置の公開資料なし）

~~~diff
- 00bd60e4 ["INT_ADD", "register:40f0:8", ["const:bd60e4:8", "const:4:8"]]
- 00bd60e4 ["CALL", null, ["callee:00bd63f4:8"]]
+ 00bd61ac ["INT_ADD", "register:40f0:8", ["const:bd61ac:8", "const:4:8"]]
+ 00bd61ac ["CALL", null, ["callee:00bd63f4:8"]]
- 00bd60e4 bytes 92000094
+ 00bd61ac bytes 92000094
- 00bd6124 ["INT_ADD", "register:40f0:8", ["const:bd6124:8", "const:4:8"]]
- 00bd6124 ["CALL", null, ["callee:00bdb070:8"]]
+ 00bd61ec ["INT_ADD", "register:40f0:8", ["const:bd61ec:8", "const:4:8"]]
+ 00bd61ec ["CALL", null, ["callee:00bdb070:8"]]
- 00bd6124 bytes a7130094
+ 00bd61ec bytes a1130094
- 00bd5f90 ["INT_ADD", "register:40f0:8", ["const:bd5f90:8", "const:4:8"]]
- 00bd5f90 ["CALL", null, ["callee:00bdb170:8"]]
+ 00bd6058 ["INT_ADD", "register:40f0:8", ["const:bd6058:8", "const:4:8"]]
+ 00bd6058 ["CALL", null, ["callee:00bdb170:8"]]
- 00bd5f90 bytes 4c140094
+ 00bd6058 bytes 46140094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-809bc5c9ea92605e08d2fd422d385d31"></a>

### [`00bd6588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6588.md) → [`00bd6650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6650.md) __emutls_get_address

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3a0.md) · 呼出先 11件 [`00bd67b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd67b0.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md) [`00bdb1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1f0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bdd450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd450.md) · 呼出先 11件 [`00bd6878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6878.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd670c",
      "incomplete_value": true,
      "site": "00bd670c",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6644",
      "incomplete_value": true,
      "site": "00bd6644",
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd6704",
      "incomplete_value": true,
      "site": "00bd670c",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd663c",
      "incomplete_value": true,
      "site": "00bd6644",
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
            "const:1:8"
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
      "definition_site": "00bd6704",
      "incomplete_value": true,
      "site": "00bd6710",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd663c",
      "incomplete_value": true,
      "site": "00bd6648",
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
            "const:1:8"
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
      "00bd6678",
      "READ",
      [
        "storage",
        "010a3894",
        null,
        "undefined4"
      ]
    ],
    [
      "00bd66e0",
      "PARAM",
      [
        "storage",
        "00bd67b0",
        null,
        null
      ]
    ],
    [
      "00bd66e4",
      "PARAM",
      [
        "storage",
        "010a3898",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd6678",
      "READ",
      [
        "storage",
        "010a3954",
        null,
        "undefined4"
      ]
    ],
    [
      "00bd66e0",
      "PARAM",
      [
        "storage",
        "00bd6878",
        null,
        null
      ]
    ],
    [
      "00bd66e4",
      "PARAM",
      [
        "storage",
        "010a3958",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd65b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6588.md#insn-00bd65b4) · [`00bd65e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6588.md#insn-00bd65e4) · [`00bd6620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6588.md#insn-00bd6620)
- 新版 `00bd667c`（命令位置の公開資料なし） · `00bd66ac`（命令位置の公開資料なし） · `00bd66e8`（命令位置の公開資料なし）

~~~diff
- 00bd65b4 ["INT_ADD", "register:40f0:8", ["const:bd65b4:8", "const:4:8"]]
- 00bd65b4 ["CALL", null, ["callee:00be11a0:8"]]
+ 00bd667c ["INT_ADD", "register:40f0:8", ["const:bd667c:8", "const:4:8"]]
+ 00bd667c ["CALL", null, ["callee:00be11a0:8"]]
- 00bd65b4 bytes cf2a0094
+ 00bd667c bytes c92a0094
- 00bd65e4 ["INT_ADD", "register:40f0:8", ["const:bd65e4:8", "const:4:8"]]
- 00bd65e4 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bd66ac ["INT_ADD", "register:40f0:8", ["const:bd66ac:8", "const:4:8"]]
+ 00bd66ac ["CALL", null, ["callee:00bdd200:8"]]
- 00bd65e4 bytes db1a0094
+ 00bd66ac bytes d51a0094
- 00bd6620 ["INT_ADD", "register:40f0:8", ["const:bd6620:8", "const:4:8"]]
- 00bd6620 ["CALL", null, ["callee:00bde7f0:8"]]
+ 00bd66e8 ["INT_ADD", "register:40f0:8", ["const:bd66e8:8", "const:4:8"]]
+ 00bd66e8 ["CALL", null, ["callee:00bde7f0:8"]]
- 00bd6620 bytes 48200094
+ 00bd66e8 bytes 42200094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48679a6fb0802bee232d0cf870d2be12"></a>

### [`00bd6774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6774.md) → [`00bd683c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd683c.md) FUN_00bd683c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004182e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004182e8.md) · 呼出先 1件 [`00be1e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e50.md)
- 新版 呼出元 1件 [`004182e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004182e8.md) · 呼出先 1件 [`00be1f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd6860",
      "incomplete_value": true,
      "site": "00bd6864",
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
      "definition_site": "00bd6798",
      "incomplete_value": true,
      "site": "00bd679c",
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
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6844",
      "READ",
      [
        "storage",
        "010a3890",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6860",
      "READ",
      [
        "storage",
        "010a3894",
        null,
        "undefined4"
      ]
    ],
    [
      "00bd6868",
      "WRITE",
      [
        "storage",
        "010a3890",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6844",
      "READ",
      [
        "storage",
        "010a3950",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6860",
      "READ",
      [
        "storage",
        "010a3954",
        null,
        "undefined4"
      ]
    ],
    [
      "00bd6868",
      "WRITE",
      [
        "storage",
        "010a3950",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd679c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6774.md#insn-00bd679c) · [`00bd677c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6774.md#insn-00bd677c) · [`00bd6794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6774.md#insn-00bd6794)
- 新版 `00bd6864`（命令位置の公開資料なし） · `00bd6844`（命令位置の公開資料なし） · `00bd685c`（命令位置の公開資料なし）

~~~diff
- 00bd679c ["INT_ADD", "register:40f0:8", ["const:bd679c:8", "const:4:8"]]
- 00bd679c ["CALL", null, ["callee:00be1f00:8"]]
+ 00bd6864 ["INT_ADD", "register:40f0:8", ["const:bd6864:8", "const:4:8"]]
+ 00bd6864 ["CALL", null, ["callee:00be1f00:8"]]
- 00bd679c bytes ad2d0094
+ 00bd6864 bytes a72d0094
- 00bd677c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:890:8"]]
- 00bd677c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd677c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bd6844 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
+ 00bd6844 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6844 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd677c bytes 08416239
+ 00bd6844 bytes 08416539
- 00bd6794 ["COPY", "tmp:0:8", ["const:890:8"]]
- 00bd6794 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00bd6794 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00bd6794 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00bd685c ["COPY", "tmp:0:8", ["const:950:8"]]
+ 00bd685c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00bd685c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00bd685c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00bd6794 bytes 73422291
+ 00bd685c bytes 73422591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

