# v15.7.2 → v15.7.3 · 最優先の変更候補 (17)

[一覧の目次](README.md)

<a id="compare-94de76b0b93f6478a2e66feb11cf7d61"></a>

### [`00558b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558b10.md) → [`00558b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558b10.md) Java_jp_co_ponos_battlecats_MyActivity_onWebViewEvalResult

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566a7c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00558b40",
      "incomplete_value": true,
      "site": "00558b40",
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
      "definition_site": "00558b40",
      "incomplete_value": true,
      "site": "00558b40",
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
      "00558b3c",
      "READ",
      [
        "storage",
        "00c26298",
        null,
        "undefined8"
      ]
    ],
    [
      "00558bd8",
      "READ",
      [
        "storage",
        "00c262e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00558b3c",
      "READ",
      [
        "storage",
        "00c26358",
        null,
        "undefined8"
      ]
    ],
    [
      "00558bd8",
      "READ",
      [
        "storage",
        "00c263a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00558b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558b10.md#insn-00558b38) · [`00558b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558b10.md#insn-00558b48) · [`00558ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558b10.md#insn-00558ba8)
- 新版 `00558b38`（命令位置の公開資料なし） · `00558b48`（命令位置の公開資料なし） · `00558ba8`（命令位置の公開資料なし）

~~~diff
- 00558b38 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00558b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00558b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00558b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00558b38 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00558b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00558b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00558b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00558b38 bytes 08610a91
+ 00558b38 bytes 08610d91
- 00558b48 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00558b48 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00558b48 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00558b48 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00558b48 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00558b48 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00558b48 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00558b48 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00558b48 bytes b5620a91
+ 00558b48 bytes b5620d91
- 00558ba8 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00558ba8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00558ba8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00558ba8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00558ba8 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 00558ba8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00558ba8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00558ba8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00558ba8 bytes 4a610a91
+ 00558ba8 bytes 4a610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53a8dc87c979a049c39634e702c87a6c"></a>

### [`00558ca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558ca4.md) → [`00558ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558ca4.md) FUN_00558ca4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00558cbc",
      "incomplete_value": false,
      "site": "00558cc0",
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
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00558cbc",
      "incomplete_value": false,
      "site": "00558cc0",
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
            "const:b28:8"
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
      "00558cc0",
      "DATA",
      [
        "storage",
        "00beeb28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00558cc0",
      "DATA",
      [
        "storage",
        "00beebd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00558cbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558ca4.md#insn-00558cbc)
- 新版 `00558cbc`（命令位置の公開資料なし）

~~~diff
- 00558cbc ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00558cbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00558cbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00558cbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00558cbc ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 00558cbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00558cbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00558cbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00558cbc bytes 29a12c91
+ 00558cbc bytes 29612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f34f030e0a1ed2430289e76dc400d15"></a>

### [`00559138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559138.md) → [`00559138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559138.md) FUN_00559138

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
      "definition_site": "0055913c",
      "incomplete_value": false,
      "site": "00559140",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055913c",
      "incomplete_value": false,
      "site": "00559140",
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
            "const:dc0:8"
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
      "00559140",
      "DATA",
      [
        "storage",
        "00beedc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00559140",
      "DATA",
      [
        "storage",
        "00beee70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055913c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559138.md#insn-0055913c)
- 新版 `0055913c`（命令位置の公開資料なし）

~~~diff
- 0055913c ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 0055913c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055913c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055913c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055913c ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 0055913c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055913c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055913c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055913c bytes 08013791
+ 0055913c bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd05d6de8699639a3f79a6d282ba2fc3"></a>

### [`00559148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559148.md) → [`00559148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559148.md) FUN_00559148

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
      "definition_site": "00559158",
      "incomplete_value": false,
      "site": "00559160",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559158",
      "incomplete_value": false,
      "site": "00559160",
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
            "const:dc0:8"
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
      "00559160",
      "DATA",
      [
        "storage",
        "00beedc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00559160",
      "DATA",
      [
        "storage",
        "00beee70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00559158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559148.md#insn-00559158)
- 新版 `00559158`（命令位置の公開資料なし）

~~~diff
- 00559158 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 00559158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00559158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00559158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00559158 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00559158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00559158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00559158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00559158 bytes 08013791
+ 00559158 bytes 08c13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eed81e5d217cd1410e2f79bafe287fcf"></a>

### [`00559188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559188.md) → [`00559188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559188.md) FUN_00559188

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
      "definition_site": "0055918c",
      "incomplete_value": false,
      "site": "00559190",
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
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055918c",
      "incomplete_value": false,
      "site": "00559190",
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
            "const:e10:8"
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
      "00559190",
      "DATA",
      [
        "storage",
        "00beee10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00559190",
      "DATA",
      [
        "storage",
        "00beeec0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055918c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559188.md#insn-0055918c)
- 新版 `0055918c`（命令位置の公開資料なし）

~~~diff
- 0055918c ["COPY", "tmp:0:8", ["const:e10:8"]]
- 0055918c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055918c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055918c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055918c ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 0055918c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055918c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055918c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055918c bytes 08413891
+ 0055918c bytes 08013b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cc33b5379df6726db66267672697091"></a>

### [`00559198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559198.md) → [`00559198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559198.md) FUN_00559198

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
      "definition_site": "005591a8",
      "incomplete_value": false,
      "site": "005591b0",
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
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005591a8",
      "incomplete_value": false,
      "site": "005591b0",
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
            "const:e10:8"
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
      "005591b0",
      "DATA",
      [
        "storage",
        "00beee10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005591b0",
      "DATA",
      [
        "storage",
        "00beeec0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005591a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559198.md#insn-005591a8)
- 新版 `005591a8`（命令位置の公開資料なし）

~~~diff
- 005591a8 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 005591a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005591a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005591a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005591a8 ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 005591a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005591a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005591a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005591a8 bytes 08413891
+ 005591a8 bytes 08013b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bf0f677e7c4adbc57ad1da72fbff41a"></a>

### [`00559334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559334.md) → [`00559334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559334.md) FUN_00559334

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005591d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/005591d8.md) [`00559458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559458.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`005591d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005591d8.md) [`00559458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559458.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00559340",
      "incomplete_value": false,
      "site": "00559344",
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
      "definition_site": "00559340",
      "incomplete_value": false,
      "site": "00559344",
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
      "00559340",
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
      "00559340",
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

- 旧版 [`00559340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559334.md#insn-00559340)
- 新版 `00559340`（命令位置の公開資料なし）

~~~diff
- 00559340 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00559340 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00559340 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00559340 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00559340 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00559340 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00559340 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00559340 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00559340 bytes 00280c91
+ 00559340 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78cb60d7e8ad49ab6aeda1e36dc94a11"></a>

### [`00559444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559444.md) → [`00559444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559444.md) FUN_00559444

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005573cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/005573cc.md) [`00557424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557424.md) [`0055746c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/0055746c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`005573cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/005573cc.md) [`00557424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557424.md) [`0055746c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/0055746c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "00559450",
      "incomplete_value": false,
      "site": "00559454",
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
      "definition_site": "00559450",
      "incomplete_value": false,
      "site": "00559454",
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
      "00559450",
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
      "00559450",
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

- 旧版 [`00559450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559444.md#insn-00559450)
- 新版 `00559450`（命令位置の公開資料なし）

~~~diff
- 00559450 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00559450 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00559450 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00559450 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00559450 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00559450 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00559450 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00559450 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00559450 bytes 00280c91
+ 00559450 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9e5efaa8a2caedbffa8aaa927513cdd"></a>

### [`005595b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/005595b4.md) → [`005595b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005595b4.md) FUN_005595b4

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
      "definition_site": "005595b8",
      "incomplete_value": false,
      "site": "005595bc",
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
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005595b8",
      "incomplete_value": false,
      "site": "005595bc",
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
            "const:e60:8"
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
      "005595bc",
      "DATA",
      [
        "storage",
        "00beee60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005595bc",
      "DATA",
      [
        "storage",
        "00beef10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005595b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/005595b4.md#insn-005595b8)
- 新版 `005595b8`（命令位置の公開資料なし）

~~~diff
- 005595b8 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 005595b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005595b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005595b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005595b8 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 005595b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005595b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005595b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005595b8 bytes 08813991
+ 005595b8 bytes 08413c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86eb7715b47ef8821acdf1c142a1fe5d"></a>

### [`005595c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/005595c4.md) → [`005595c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005595c4.md) FUN_005595c4

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
      "definition_site": "005595d4",
      "incomplete_value": false,
      "site": "005595dc",
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
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005595d4",
      "incomplete_value": false,
      "site": "005595dc",
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
            "const:e60:8"
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
      "005595dc",
      "DATA",
      [
        "storage",
        "00beee60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005595dc",
      "DATA",
      [
        "storage",
        "00beef10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005595d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/005595c4.md#insn-005595d4)
- 新版 `005595d4`（命令位置の公開資料なし）

~~~diff
- 005595d4 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 005595d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005595d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005595d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005595d4 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 005595d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005595d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005595d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005595d4 bytes 08813991
+ 005595d4 bytes 08413c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b8d8a58054c647739e5f19a15501c92"></a>

### [`00559604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559604.md) → [`00559604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559604.md) FUN_00559604

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
      "definition_site": "00559608",
      "incomplete_value": false,
      "site": "0055960c",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559608",
      "incomplete_value": false,
      "site": "0055960c",
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
            "const:eb0:8"
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
      "0055960c",
      "DATA",
      [
        "storage",
        "00beeeb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055960c",
      "DATA",
      [
        "storage",
        "00beef60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00559608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559604.md#insn-00559608)
- 新版 `00559608`（命令位置の公開資料なし）

~~~diff
- 00559608 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 00559608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00559608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00559608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00559608 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00559608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00559608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00559608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00559608 bytes 08c13a91
+ 00559608 bytes 08813d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e33ab94ea7f6a6fad7457a9743b056b"></a>

### [`00559614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559614.md) → [`00559614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559614.md) FUN_00559614

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
      "definition_site": "00559624",
      "incomplete_value": false,
      "site": "0055962c",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559624",
      "incomplete_value": false,
      "site": "0055962c",
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
            "const:eb0:8"
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
      "0055962c",
      "DATA",
      [
        "storage",
        "00beeeb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055962c",
      "DATA",
      [
        "storage",
        "00beef60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00559624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559614.md#insn-00559624)
- 新版 `00559624`（命令位置の公開資料なし）

~~~diff
- 00559624 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 00559624 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00559624 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00559624 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00559624 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00559624 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00559624 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00559624 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00559624 bytes 08c13a91
+ 00559624 bytes 08813d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d225f5b14eb4ae95b2add226d5f13963"></a>

### [`00559734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559734.md) → [`00559734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559734.md) FUN_00559734

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
      "definition_site": "00559738",
      "incomplete_value": false,
      "site": "0055973c",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559738",
      "incomplete_value": false,
      "site": "0055973c",
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
            "const:f00:8"
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
      "0055973c",
      "DATA",
      [
        "storage",
        "00beef00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055973c",
      "DATA",
      [
        "storage",
        "00beefb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00559738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559734.md#insn-00559738)
- 新版 `00559738`（命令位置の公開資料なし）

~~~diff
- 00559738 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 00559738 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00559738 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00559738 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00559738 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 00559738 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00559738 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00559738 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00559738 bytes 08013c91
+ 00559738 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfce3e2f0f3e3f5908c029c30770a1a5"></a>

### [`00559744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559744.md) → [`00559744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559744.md) FUN_00559744

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
      "definition_site": "00559754",
      "incomplete_value": false,
      "site": "0055975c",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559754",
      "incomplete_value": false,
      "site": "0055975c",
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
            "const:f00:8"
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
      "0055975c",
      "DATA",
      [
        "storage",
        "00beef00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055975c",
      "DATA",
      [
        "storage",
        "00beefb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00559754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559744.md#insn-00559754)
- 新版 `00559754`（命令位置の公開資料なし）

~~~diff
- 00559754 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 00559754 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00559754 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00559754 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00559754 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 00559754 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00559754 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00559754 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00559754 bytes 08013c91
+ 00559754 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-327d51679c25db50315e11f8eba4944e"></a>

### [`005598e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/005598e4.md) → [`005598e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005598e4.md) _INIT_31

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`005536d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005536d4.md) [`005536dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005536dc.md) [`00553820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/00553820.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`005536d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005536d4.md) [`005536dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005536dc.md) [`00553820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/00553820.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 76.32% / 新版 76.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 12件, `store_value` 7件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00559920",
      "incomplete_value": true,
      "site": "0055993c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00559920",
      "incomplete_value": true,
      "site": "0055993c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00559944",
      "incomplete_value": true,
      "site": "00559960",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00559944",
      "incomplete_value": true,
      "site": "00559960",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00559964",
      "incomplete_value": true,
      "site": "00559980",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00559964",
      "incomplete_value": true,
      "site": "00559980",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00559920",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00559944",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00559964",
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
      "00559920",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00559944",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00559964",
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

- 旧版 [`00559b94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/005598e4.md#insn-00559b94) · [`00559bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/005598e4.md#insn-00559bbc)
- 新版 `00559b94`（命令位置の公開資料なし）

~~~diff
- 00559b94 ["INT_ADD", "register:40f0:8", ["const:559b94:8", "const:4:8"]]
- 00559b94 ["CALL", null, ["callee:00bdaf90:8"]]
- 00559b94 bytes d3041a94
+ 00559b94 ["INT_ADD", "register:40f0:8", ["const:559b94:8", "const:4:8"]]
+ 00559b94 ["CALL", null, ["callee:00bdaf90:8"]]
+ 00559b94 bytes ff041a94
- 00559bbc ["INT_ADD", "register:40f0:8", ["const:559bbc:8", "const:4:8"]]
- 00559bbc ["CALL", null, ["callee:00bdaf90:8"]]
- 00559bbc bytes c9041a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93d7f118ebca1161a1cd435638d2b970"></a>

### [`00559d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559d40.md) → [`00559d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559d40.md) FUN_00559d40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdd1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00559d60",
      "incomplete_value": false,
      "site": "00559d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559d60",
      "incomplete_value": false,
      "site": "00559d60",
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
            "const:f50:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00559d60",
      "incomplete_value": false,
      "site": "00559d60",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559d60",
      "incomplete_value": false,
      "site": "00559d60",
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
                "const:bee000:8"
              ],
              [
                "leaf",
                "const:f50:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "00559d60",
      "DATA",
      [
        "storage",
        "00beef50",
        null,
        "undefined *"
      ]
    ],
    [
      "00559d60",
      "DATA",
      [
        "storage",
        "00bef018",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00559d60",
      "DATA",
      [
        "storage",
        "00bef000",
        null,
        "undefined *"
      ]
    ],
    [
      "00559d60",
      "DATA",
      [
        "storage",
        "00bef0c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00559d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559d40.md#insn-00559d50) · [`00559d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559d40.md#insn-00559d54)
- 新版 `00559d50`（命令位置の公開資料なし） · `00559d54`（命令位置の公開資料なし）

~~~diff
- 00559d50 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00559d50 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 00559d50 bytes a83400b0
+ 00559d50 bytes a83400d0
- 00559d54 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00559d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00559d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00559d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00559d54 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00559d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00559d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00559d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00559d54 bytes 08413d91
+ 00559d54 bytes 08010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dc996c08eab49f8d6c7bd0a969f9e55"></a>

### [`00559da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559da0.md) → [`00559da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559da0.md) FUN_00559da0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdd1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdd2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00559dc0",
      "incomplete_value": false,
      "site": "00559dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559dc0",
      "incomplete_value": false,
      "site": "00559dc0",
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
            "const:f50:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00559dc0",
      "incomplete_value": false,
      "site": "00559dc0",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00559dc0",
      "incomplete_value": false,
      "site": "00559dc0",
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
                "const:bee000:8"
              ],
              [
                "leaf",
                "const:f50:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "00559dc0",
      "DATA",
      [
        "storage",
        "00beef50",
        null,
        "undefined *"
      ]
    ],
    [
      "00559dc0",
      "DATA",
      [
        "storage",
        "00bef018",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00559dc0",
      "DATA",
      [
        "storage",
        "00bef000",
        null,
        "undefined *"
      ]
    ],
    [
      "00559dc0",
      "DATA",
      [
        "storage",
        "00bef0c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00559db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559da0.md#insn-00559db0) · [`00559db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559da0.md#insn-00559db4)
- 新版 `00559db0`（命令位置の公開資料なし） · `00559db4`（命令位置の公開資料なし）

~~~diff
- 00559db0 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00559db0 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 00559db0 bytes a83400b0
+ 00559db0 bytes a83400d0
- 00559db4 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00559db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00559db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00559db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00559db4 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00559db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00559db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00559db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00559db4 bytes 08413d91
+ 00559db4 bytes 08010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3145d5d9d5fb977d0090ae5084d39a1e"></a>

### [`00559fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559fe0.md) → [`00559fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559fe0.md) FUN_00559fe0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00567d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567d4c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00567d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d4c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "0055a150",
      "incomplete_value": false,
      "site": "0055a15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055a150",
      "incomplete_value": false,
      "site": "0055a15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
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
      "0055a15c",
      "DATA",
      [
        "storage",
        "00bef1a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055a15c",
      "DATA",
      [
        "storage",
        "00bef250",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559fe0.md#insn-0055a150)
- 新版 `0055a150`（命令位置の公開資料なし）

~~~diff
- 0055a150 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 0055a150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055a150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055a150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055a150 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 0055a150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055a150 bytes 08810691
+ 0055a150 bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85cc5fd04938c8ca2fe486b0d2d02c5e"></a>

### [`0055a5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055a5bc.md) → [`0055a5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055a5bc.md) FUN_0055a5bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00567d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567d4c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00567d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d4c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055a734",
      "incomplete_value": false,
      "site": "0055a740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055a734",
      "incomplete_value": false,
      "site": "0055a740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
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
      "0055a740",
      "DATA",
      [
        "storage",
        "00bef1a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055a740",
      "DATA",
      [
        "storage",
        "00bef250",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055a734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055a5bc.md#insn-0055a734)
- 新版 `0055a734`（命令位置の公開資料なし）

~~~diff
- 0055a734 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 0055a734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055a734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055a734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055a734 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 0055a734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055a734 bytes 08810691
+ 0055a734 bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f19c36fc29d7f4e9310b4ae72abf65d"></a>

### [`0055aad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055aad0.md) → [`0055aad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055aad0.md) FUN_0055aad0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052dccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dccc.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdd140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd140.md) [`00bdd210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd210.md)
- 新版 呼出元 1件 [`0052dccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dccc.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md) [`00bdd2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2c0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.17% / 新版 86.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ab28",
      "incomplete_value": false,
      "site": "0055ab34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ab28",
      "incomplete_value": false,
      "site": "0055ab34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "definition_site": "0055ab48",
      "incomplete_value": false,
      "site": "0055ab48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ab48",
      "incomplete_value": false,
      "site": "0055ab48",
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
            "const:f50:8"
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
      "definition_site": "0055ab4c",
      "incomplete_value": false,
      "site": "0055ab50",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ab4c",
      "incomplete_value": false,
      "site": "0055ab50",
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
                "const:bee000:8"
              ],
              [
                "leaf",
                "const:f50:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0055aaf0",
      "READ",
      [
        "storage",
        "00c1b3e0",
        null,
        "pointer"
      ]
    ],
    [
      "0055ab04",
      "READ",
      [
        "storage",
        "00c262f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0055ab34",
      "DATA",
      [
        "storage",
        "00bef1f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055aaf0",
      "READ",
      [
        "storage",
        "00c1b490",
        null,
        "pointer"
      ]
    ],
    [
      "0055ab04",
      "READ",
      [
        "storage",
        "00c263b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0055ab34",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055aaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055aad0.md#insn-0055aaf0) · [`0055ab28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055aad0.md#insn-0055ab28) · [`0055ab2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055aad0.md#insn-0055ab2c)
- 新版 `0055aaf0`（命令位置の公開資料なし） · `0055ab28`（命令位置の公開資料なし）

~~~diff
- 0055aaf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3e0:8"]]
- 0055aaf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0055aaf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:490:8"]]
+ 0055aaf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0055aaf0 bytes 08f141f9
+ 0055aaf0 bytes 084942f9
- 0055ab28 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 0055ab28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ab28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ab28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ab28 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 0055ab28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ab28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ab28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ab28 bytes 08c10791
+ 0055ab28 bytes 08810a91
- 0055ab2c ["COPY", "register:4048:8", ["const:bee000:8"]]
- 0055ab2c bytes a9340090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-610663855c4ea724ea7c9676f5d5a5eb"></a>

### [`0055ac68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055ac68.md) → [`0055ac68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ac68.md) FUN_0055ac68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ac78",
      "incomplete_value": false,
      "site": "0055ac78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ac78",
      "incomplete_value": false,
      "site": "0055ac78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ac78",
      "incomplete_value": false,
      "site": "0055ac78",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ac78",
      "incomplete_value": false,
      "site": "0055ac78",
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
                "const:bef000:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0055ac78",
      "DATA",
      [
        "storage",
        "00bef030",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ac78",
      "DATA",
      [
        "storage",
        "00bef0f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0055ac78",
      "DATA",
      [
        "storage",
        "00bef0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ac78",
      "DATA",
      [
        "storage",
        "00bef1a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ac6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055ac68.md#insn-0055ac6c)
- 新版 `0055ac6c`（命令位置の公開資料なし）

~~~diff
- 0055ac6c ["COPY", "tmp:0:8", ["const:30:8"]]
- 0055ac6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ac6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ac6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ac6c ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 0055ac6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ac6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ac6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ac6c bytes 08c10091
+ 0055ac6c bytes 08810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5c1d8c3d2fccbe859346c0c232c505c"></a>

### [`0055ac8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055ac8c.md) → [`0055ac8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ac8c.md) FUN_0055ac8c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ac9c",
      "incomplete_value": true,
      "site": "0055ac9c",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ac9c",
      "incomplete_value": true,
      "site": "0055ac9c",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ac9c",
      "incomplete_value": true,
      "site": "0055ac9c",
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
                "const:e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ac9c",
      "incomplete_value": true,
      "site": "0055ac9c",
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
                "const:30:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0055ac9c",
      "DATA",
      [
        "storage",
        "00bef030",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ac9c",
      "DATA",
      [
        "storage",
        "00bef0f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0055ac9c",
      "DATA",
      [
        "storage",
        "00bef0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ac9c",
      "DATA",
      [
        "storage",
        "00bef1a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ac90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055ac8c.md#insn-0055ac90)
- 新版 `0055ac90`（命令位置の公開資料なし）

~~~diff
- 0055ac90 ["COPY", "tmp:0:8", ["const:30:8"]]
- 0055ac90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ac90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ac90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ac90 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 0055ac90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ac90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ac90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ac90 bytes 08c10091
+ 0055ac90 bytes 08810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4897119cd1d538f2793ddce5082f36a7"></a>

### [`0055acd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055acd0.md) → [`0055acd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055acd0.md) FUN_0055acd0

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
      "definition_site": "0055acd4",
      "incomplete_value": false,
      "site": "0055acd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055acd4",
      "incomplete_value": false,
      "site": "0055acd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
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
      "0055acd8",
      "DATA",
      [
        "storage",
        "00bef1a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055acd8",
      "DATA",
      [
        "storage",
        "00bef250",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055acd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055acd0.md#insn-0055acd4)
- 新版 `0055acd4`（命令位置の公開資料なし）

~~~diff
- 0055acd4 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 0055acd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055acd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055acd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055acd4 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 0055acd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055acd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055acd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055acd4 bytes 08810691
+ 0055acd4 bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-692a0689c6f13e2a60ed8dfacb17582d"></a>

### [`0055ad20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055ad20.md) → [`0055ad20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ad20.md) FUN_0055ad20

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
      "definition_site": "0055ad24",
      "incomplete_value": false,
      "site": "0055ad28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ad24",
      "incomplete_value": false,
      "site": "0055ad28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "0055ad28",
      "DATA",
      [
        "storage",
        "00bef1f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ad28",
      "DATA",
      [
        "storage",
        "00bef2a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ad24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055ad20.md#insn-0055ad24)
- 新版 `0055ad24`（命令位置の公開資料なし）

~~~diff
- 0055ad24 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 0055ad24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ad24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ad24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ad24 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 0055ad24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ad24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ad24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ad24 bytes 08c10791
+ 0055ad24 bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-438a0ed90662a41cab3cd6c2636b3e9c"></a>

### [`0055ad70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055ad70.md) → [`0055ad70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ad70.md) FUN_0055ad70

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
      "definition_site": "0055ad74",
      "incomplete_value": false,
      "site": "0055ad78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ad74",
      "incomplete_value": false,
      "site": "0055ad78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "0055ad78",
      "DATA",
      [
        "storage",
        "00bef240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ad78",
      "DATA",
      [
        "storage",
        "00bef2f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ad74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055ad70.md#insn-0055ad74)
- 新版 `0055ad74`（命令位置の公開資料なし）

~~~diff
- 0055ad74 ["COPY", "tmp:0:8", ["const:240:8"]]
- 0055ad74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ad74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ad74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ad74 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 0055ad74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ad74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ad74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ad74 bytes 08010991
+ 0055ad74 bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b7ac5d8532e574d705d26950b530016"></a>

### [`0055ad80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055ad80.md) → [`0055ad80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055ad80.md) FUN_0055ad80

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
      "definition_site": "0055ad90",
      "incomplete_value": false,
      "site": "0055ad98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ad90",
      "incomplete_value": false,
      "site": "0055ad98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:240:8"
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
      "0055ad98",
      "DATA",
      [
        "storage",
        "00bef240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ad98",
      "DATA",
      [
        "storage",
        "00bef2f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ad90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055ad80.md#insn-0055ad90)
- 新版 `0055ad90`（命令位置の公開資料なし）

~~~diff
- 0055ad90 ["COPY", "tmp:0:8", ["const:240:8"]]
- 0055ad90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ad90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ad90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ad90 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 0055ad90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ad90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ad90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ad90 bytes 08010991
+ 0055ad90 bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4a57a099bfa9ba02c2f9dc79db009de"></a>

### [`0055b1b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b1b8.md) → [`0055b1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b1b8.md) FUN_0055b1b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0052dd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dd30.md) [`005627f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005627f4.md) [`0056340c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/0056340c.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 3件 [`0052dd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd30.md) [`005627f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005627f4.md) [`0056340c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/0056340c.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055b1ec",
      "incomplete_value": false,
      "site": "0055b1f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b1ec",
      "incomplete_value": false,
      "site": "0055b1f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:308:8"
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
      "0055b1f4",
      "DATA",
      [
        "storage",
        "00bef308",
        null,
        "undefined *"
      ]
    ],
    [
      "0055b20c",
      "DATA",
      [
        "storage",
        "00bef290",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b1f4",
      "DATA",
      [
        "storage",
        "00bef3b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0055b20c",
      "DATA",
      [
        "storage",
        "00bef340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b1ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b1b8.md#insn-0055b1ec) · [`0055b200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b1b8.md#insn-0055b200)
- 新版 `0055b1ec`（命令位置の公開資料なし） · `0055b200`（命令位置の公開資料なし）

~~~diff
- 0055b1ec ["COPY", "tmp:0:8", ["const:308:8"]]
- 0055b1ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b1ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b1ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b1ec ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 0055b1ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b1ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b1ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b1ec bytes 08210c91
+ 0055b1ec bytes 08e10e91
- 0055b200 ["COPY", "tmp:0:8", ["const:290:8"]]
- 0055b200 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055b200 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055b200 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055b200 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 0055b200 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055b200 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055b200 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055b200 bytes 29410a91
+ 0055b200 bytes 29010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-936e3ebe722d0fb3a23b8d77d621cfc8"></a>

### [`0055b28c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b28c.md) → [`0055b28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b28c.md) FUN_0055b28c

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055b2a4",
      "incomplete_value": true,
      "site": "0055b2a8",
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
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b2a4",
      "incomplete_value": true,
      "site": "0055b2a8",
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
            "const:290:8"
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
      "0055b2a8",
      "DATA",
      [
        "storage",
        "00bef290",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b2a8",
      "DATA",
      [
        "storage",
        "00bef340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b2a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b28c.md#insn-0055b2a4)
- 新版 `0055b2a4`（命令位置の公開資料なし）

~~~diff
- 0055b2a4 ["COPY", "tmp:0:8", ["const:290:8"]]
- 0055b2a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b2a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b2a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b2a4 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 0055b2a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b2a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b2a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b2a4 bytes 08410a91
+ 0055b2a4 bytes 08010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85666041728dd6bf88154c23ac03300d"></a>

### [`0055b304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b304.md) → [`0055b304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b304.md) FUN_0055b304

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
      "definition_site": "0055b31c",
      "incomplete_value": false,
      "site": "0055b320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b31c",
      "incomplete_value": false,
      "site": "0055b320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "0055b320",
      "DATA",
      [
        "storage",
        "00bef290",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b320",
      "DATA",
      [
        "storage",
        "00bef340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b31c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b304.md#insn-0055b31c)
- 新版 `0055b31c`（命令位置の公開資料なし）

~~~diff
- 0055b31c ["COPY", "tmp:0:8", ["const:290:8"]]
- 0055b31c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b31c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b31c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b31c ["COPY", "tmp:0:8", ["const:340:8"]]
+ 0055b31c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b31c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b31c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b31c bytes 08410a91
+ 0055b31c bytes 08010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98ae00cfe62c92a0c1673a058b1f1a11"></a>

### [`0055b37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b37c.md) → [`0055b37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b37c.md) FUN_0055b37c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0055af38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055af38.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`0055af38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055af38.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055b3a8",
      "incomplete_value": false,
      "site": "0055b3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b3a8",
      "incomplete_value": false,
      "site": "0055b3ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:308:8"
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
      "definition_site": "0055b3b4",
      "incomplete_value": false,
      "site": "0055b3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b3b4",
      "incomplete_value": false,
      "site": "0055b3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "0055b3ac",
      "DATA",
      [
        "storage",
        "00bef308",
        null,
        "undefined *"
      ]
    ],
    [
      "0055b3c4",
      "DATA",
      [
        "storage",
        "00bef290",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b3ac",
      "DATA",
      [
        "storage",
        "00bef3b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0055b3c4",
      "DATA",
      [
        "storage",
        "00bef340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b37c.md#insn-0055b3a8) · [`0055b3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b37c.md#insn-0055b3b0)
- 新版 `0055b3a8`（命令位置の公開資料なし） · `0055b3b0`（命令位置の公開資料なし）

~~~diff
- 0055b3a8 ["COPY", "tmp:0:8", ["const:308:8"]]
- 0055b3a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b3a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b3a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b3a8 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 0055b3a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b3a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b3a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b3a8 bytes 08210c91
+ 0055b3a8 bytes 08e10e91
- 0055b3b0 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 0055b3b0 bytes a8340090
+ 0055b3b0 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 0055b3b0 bytes a8340090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67f6935efd723f5d21c5ec95f049be70"></a>

### [`0055b4a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b4a4.md) → [`0055b4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b4a4.md) FUN_0055b4a4

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
      "definition_site": "0055b4a8",
      "incomplete_value": false,
      "site": "0055b4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b4a8",
      "incomplete_value": false,
      "site": "0055b4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:308:8"
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
      "0055b4ac",
      "DATA",
      [
        "storage",
        "00bef308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b4ac",
      "DATA",
      [
        "storage",
        "00bef3b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b4a4.md#insn-0055b4a8)
- 新版 `0055b4a8`（命令位置の公開資料なし）

~~~diff
- 0055b4a8 ["COPY", "tmp:0:8", ["const:308:8"]]
- 0055b4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b4a8 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 0055b4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b4a8 bytes 08210c91
+ 0055b4a8 bytes 08e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f82b01f32d61ae494e846f9a519b1da"></a>

### [`0055b4b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b4b4.md) → [`0055b4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b4b4.md) FUN_0055b4b4

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
      "definition_site": "0055b4c4",
      "incomplete_value": false,
      "site": "0055b4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b4c4",
      "incomplete_value": false,
      "site": "0055b4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:308:8"
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
      "0055b4cc",
      "DATA",
      [
        "storage",
        "00bef308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055b4cc",
      "DATA",
      [
        "storage",
        "00bef3b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b4c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b4b4.md#insn-0055b4c4)
- 新版 `0055b4c4`（命令位置の公開資料なし）

~~~diff
- 0055b4c4 ["COPY", "tmp:0:8", ["const:308:8"]]
- 0055b4c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b4c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b4c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b4c4 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 0055b4c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b4c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b4c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b4c4 bytes 08210c91
+ 0055b4c4 bytes 08e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-229072a5f8e7e4fb563cb610171a470f"></a>

### [`0055b604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b604.md) → [`0055b604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b604.md) FUN_0055b604

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0052dd54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dd54.md) [`0055bd18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055bd18.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056627c.md)
- 新版 呼出元 2件 [`0052dd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd54.md) [`0055bd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055bd18.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056627c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.22% / 新版 93.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055b664",
      "incomplete_value": true,
      "site": "0055b664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b664",
      "incomplete_value": true,
      "site": "0055b664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc9:8"
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
      "definition_site": "0055b670",
      "incomplete_value": true,
      "site": "0055b67c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a0d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b670",
      "incomplete_value": true,
      "site": "0055b67c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a16:8"
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
      "definition_site": "0055b71c",
      "incomplete_value": true,
      "site": "0055b71c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:70d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b71c",
      "incomplete_value": true,
      "site": "0055b71c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:714:8"
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
      "0055b654",
      "READ",
      [
        "storage",
        "00296bc9",
        null,
        "string"
      ]
    ],
    [
      "0055b670",
      "READ",
      [
        "storage",
        "002aca16",
        null,
        "string"
      ]
    ],
    [
      "0055b704",
      "READ",
      [
        "storage",
        "002a5714",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055b654",
      "READ",
      [
        "storage",
        "00296c56",
        null,
        "string"
      ]
    ],
    [
      "0055b670",
      "READ",
      [
        "storage",
        "002aca0d",
        null,
        "string"
      ]
    ],
    [
      "0055b704",
      "READ",
      [
        "storage",
        "002a570d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b604.md#insn-0055b650) · [`0055b668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b604.md#insn-0055b668)
- 新版 `0055b650`（命令位置の公開資料なし） · `0055b668`（命令位置の公開資料なし）

~~~diff
- 0055b650 ["COPY", "tmp:0:8", ["const:bc9:8"]]
- 0055b650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b650 ["COPY", "tmp:0:8", ["const:c56:8"]]
+ 0055b650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b650 bytes 08252f91
+ 0055b650 bytes 08593191
- 0055b668 ["COPY", "register:4040:8", ["const:2ac000:8"]]
- 0055b668 bytes 88eaffb0
+ 0055b668 ["COPY", "register:4040:8", ["const:2ac000:8"]]
+ 0055b668 bytes 88eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f43c5553ca7a79ab84bdfb2aaf0403d8"></a>

### [`0055b95c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b95c.md) → [`0055b95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b95c.md) FUN_0055b95c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052dd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dd50.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056627c.md)
- 新版 呼出元 1件 [`0052dd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd50.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056627c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.48% / 新版 95.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055b9c8",
      "incomplete_value": true,
      "site": "0055b9d4",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:a0d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055b9c8",
      "incomplete_value": true,
      "site": "0055b9d4",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:a16:8"
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
      "definition_site": "0055ba74",
      "incomplete_value": true,
      "site": "0055ba74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:70d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ba74",
      "incomplete_value": true,
      "site": "0055ba74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:714:8"
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
      "definition_site": "0055ba7c",
      "incomplete_value": true,
      "site": "0055ba7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0055ba7c",
      "incomplete_value": true,
      "site": "0055ba7c",
      "value": [
        "LOAD",
        "8",
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
      "0055b9c8",
      "READ",
      [
        "storage",
        "002aca16",
        null,
        "string"
      ]
    ],
    [
      "0055ba5c",
      "READ",
      [
        "storage",
        "002a5714",
        null,
        "string"
      ]
    ],
    [
      "0055ba64",
      "READ",
      [
        "storage",
        "002a571b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055b9c8",
      "READ",
      [
        "storage",
        "002aca0d",
        null,
        "string"
      ]
    ],
    [
      "0055ba5c",
      "READ",
      [
        "storage",
        "002a570d",
        null,
        "string"
      ]
    ],
    [
      "0055ba64",
      "READ",
      [
        "storage",
        "002a5714",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055b9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b95c.md#insn-0055b9c4) · [`0055ba58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b95c.md#insn-0055ba58)
- 新版 `0055b9c4`（命令位置の公開資料なし） · `0055ba58`（命令位置の公開資料なし）

~~~diff
- 0055b9c4 ["COPY", "tmp:0:8", ["const:a16:8"]]
- 0055b9c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055b9c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055b9c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055b9c4 ["COPY", "tmp:0:8", ["const:a0d:8"]]
+ 0055b9c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b9c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055b9c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055b9c4 bytes 08592891
+ 0055b9c4 bytes 08352891
- 0055ba58 ["COPY", "tmp:0:8", ["const:714:8"]]
- 0055ba58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055ba58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055ba58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055ba58 ["COPY", "tmp:0:8", ["const:70d:8"]]
+ 0055ba58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055ba58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055ba58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055ba58 bytes 29511c91
+ 0055ba58 bytes 29351c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7f78c80a49b9fffe2dd9e0a4d67ff77"></a>

### [`0055c104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c104.md) → [`0055c104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c104.md) FUN_0055c104

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00558f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00558f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

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
      "definition_site": "0055c150",
      "incomplete_value": true,
      "site": "0055c16c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c150",
      "incomplete_value": true,
      "site": "0055c16c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b9f:8"
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
      "0055c150",
      "READ",
      [
        "storage",
        "00295b9f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055c150",
      "READ",
      [
        "storage",
        "00295c2c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c104.md#insn-0055c140)
- 新版 `0055c140`（命令位置の公開資料なし）

~~~diff
- 0055c140 ["COPY", "tmp:0:8", ["const:b9f:8"]]
- 0055c140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055c140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055c140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055c140 ["COPY", "tmp:0:8", ["const:c2c:8"]]
+ 0055c140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055c140 bytes 297d2e91
+ 0055c140 bytes 29b13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d482f446a3e7ec2e19200347cefa6c5"></a>

### [`0055c3fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c3fc.md) → [`0055c3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c3fc.md) FUN_0055c3fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00558f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00558f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.94% / 新版 92.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c448",
      "incomplete_value": true,
      "site": "0055c458",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ba:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c448",
      "incomplete_value": true,
      "site": "0055c458",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:62d:8"
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
      "definition_site": "0055c460",
      "incomplete_value": true,
      "site": "0055c460",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0055c460",
      "incomplete_value": true,
      "site": "0055c460",
      "value": [
        "LOAD",
        "8",
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
      "0055c448",
      "READ",
      [
        "storage",
        "0029c62d",
        null,
        "string"
      ]
    ],
    [
      "0055c44c",
      "READ",
      [
        "storage",
        "0029c63c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055c448",
      "READ",
      [
        "storage",
        "0029c6ba",
        null,
        "string"
      ]
    ],
    [
      "0055c44c",
      "READ",
      [
        "storage",
        "0029c6c9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c3fc.md#insn-0055c440) · [`0055c444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c3fc.md#insn-0055c444)
- 新版 `0055c440`（命令位置の公開資料なし） · `0055c444`（命令位置の公開資料なし）

~~~diff
- 0055c440 ["COPY", "tmp:0:8", ["const:62d:8"]]
- 0055c440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c440 ["COPY", "tmp:0:8", ["const:6ba:8"]]
+ 0055c440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c440 bytes 08b51891
+ 0055c440 bytes 08e91a91
- 0055c444 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0055c444 bytes a9eaff90
+ 0055c444 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0055c444 bytes a9eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6f14e90fbc3705dabcf252b1e85d668"></a>

### [`0055c58c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c58c.md) → [`0055c58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c58c.md) FUN_0055c58c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00558f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00558f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.58% / 新版 91.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c5dc",
      "incomplete_value": true,
      "site": "0055c5f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b21:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c5dc",
      "incomplete_value": true,
      "site": "0055c5f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bb5:8"
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
      "definition_site": "0055c5f8",
      "incomplete_value": true,
      "site": "0055c604",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c5f8",
      "incomplete_value": true,
      "site": "0055c604",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5ec:8"
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
      "definition_site": "0055c608",
      "incomplete_value": true,
      "site": "0055c608",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0055c608",
      "incomplete_value": true,
      "site": "0055c608",
      "value": [
        "LOAD",
        "8",
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
      "0055c5dc",
      "READ",
      [
        "storage",
        "002adbb5",
        null,
        "string"
      ]
    ],
    [
      "0055c5f8",
      "READ",
      [
        "storage",
        "002a45ec",
        null,
        "string"
      ]
    ],
    [
      "0055c5fc",
      "READ",
      [
        "storage",
        "002a45fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055c5dc",
      "READ",
      [
        "storage",
        "002adb21",
        null,
        "string"
      ]
    ],
    [
      "0055c5f8",
      "READ",
      [
        "storage",
        "002a45e5",
        null,
        "string"
      ]
    ],
    [
      "0055c5fc",
      "READ",
      [
        "storage",
        "002a45f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c58c.md#insn-0055c5d0) · [`0055c5f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c58c.md#insn-0055c5f0)
- 新版 `0055c5d0`（命令位置の公開資料なし） · `0055c5f0`（命令位置の公開資料なし）

~~~diff
- 0055c5d0 ["COPY", "tmp:0:8", ["const:bb5:8"]]
- 0055c5d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055c5d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055c5d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055c5d0 ["COPY", "tmp:0:8", ["const:b21:8"]]
+ 0055c5d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c5d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c5d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055c5d0 bytes 29d52e91
+ 0055c5d0 bytes 29852c91
- 0055c5f0 ["COPY", "tmp:0:8", ["const:5ec:8"]]
- 0055c5f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055c5f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055c5f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c5f0 ["COPY", "tmp:0:8", ["const:5e5:8"]]
+ 0055c5f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c5f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c5f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055c5f0 bytes 08b11791
+ 0055c5f0 bytes 08951791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e20cd9b954897d499e7e1dc24198fd5"></a>

### [`0055c754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c754.md) → [`0055c754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c754.md) FUN_0055c754

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056627c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`0056627c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056627c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c79c",
      "incomplete_value": true,
      "site": "0055c7ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:71d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055c79c",
      "incomplete_value": true,
      "site": "0055c7ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:724:8"
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
      "0055c79c",
      "READ",
      [
        "storage",
        "002a5724",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055c79c",
      "READ",
      [
        "storage",
        "002a571d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c754.md#insn-0055c794)
- 新版 `0055c794`（命令位置の公開資料なし）

~~~diff
- 0055c794 ["COPY", "tmp:0:8", ["const:724:8"]]
- 0055c794 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055c794 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055c794 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055c794 ["COPY", "tmp:0:8", ["const:71d:8"]]
+ 0055c794 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c794 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c794 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055c794 bytes 29911c91
+ 0055c794 bytes 29751c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec79c20c6dd6f5a479efc003a284a6fe"></a>

### [`0055c994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c994.md) → [`0055c994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c994.md) FUN_0055c994

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`005398ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/005398ec.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005398ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005398ec.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "0055ca04",
      "incomplete_value": true,
      "site": "0055ca04",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:e16:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ca04",
      "incomplete_value": true,
      "site": "0055ca04",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:299000:8"
              ],
              [
                "leaf",
                "const:d89:8"
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
      "0055c9f0",
      "READ",
      [
        "storage",
        "00299d89",
        null,
        "string"
      ]
    ],
    [
      "0055c9f8",
      "READ",
      [
        "storage",
        "00299d8e",
        null,
        "string"
      ]
    ],
    [
      "0055ca24",
      "READ",
      [
        "storage",
        "0029b4b3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055c9f0",
      "READ",
      [
        "storage",
        "00299e16",
        null,
        "string"
      ]
    ],
    [
      "0055c9f8",
      "READ",
      [
        "storage",
        "00299e1b",
        null,
        "string"
      ]
    ],
    [
      "0055ca24",
      "READ",
      [
        "storage",
        "0029b540",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055c9ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c994.md#insn-0055c9ec) · [`0055c9fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c994.md#insn-0055c9fc)
- 新版 `0055c9ec`（命令位置の公開資料なし） · `0055c9fc`（命令位置の公開資料なし）

~~~diff
- 0055c9ec ["COPY", "tmp:0:8", ["const:d89:8"]]
- 0055c9ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055c9ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055c9ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055c9ec ["COPY", "tmp:0:8", ["const:e16:8"]]
+ 0055c9ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c9ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c9ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055c9ec bytes 29253691
+ 0055c9ec bytes 29593891
- 0055c9fc ["COPY", "register:40c8:8", ["register:4000:8"]]
- 0055c9fc bytes f90300aa
+ 0055c9fc ["COPY", "register:40c8:8", ["register:4000:8"]]
+ 0055c9fc bytes f90300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f6eecb52c5563d5ba93ac0d4b05af41"></a>

### [`0055cc34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055cc34.md) → [`0055cc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cc34.md) FUN_0055cc34

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`005323c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005323c0.md) [`0055ce48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055ce48.md) [`0055ced0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055ced0.md) [`0055cf7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055cf7c.md) [`0055d024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d024.md) · 呼出先 11件 [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 6件 [`005323c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323c0.md) [`0055ce48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055ce48.md) [`0055ced0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055ced0.md) [`0055cf7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cf7c.md) [`0055d024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d024.md) · 呼出先 11件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.73% / 新版 86.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055cc98",
      "incomplete_value": true,
      "site": "0055cc98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:552:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cc98",
      "incomplete_value": true,
      "site": "0055cc98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:559:8"
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
      "definition_site": "0055cca0",
      "incomplete_value": true,
      "site": "0055cca0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0055cca0",
      "incomplete_value": true,
      "site": "0055cca0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055cc9c",
      "incomplete_value": true,
      "site": "0055ccb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c69:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cc9c",
      "incomplete_value": true,
      "site": "0055ccb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bdc:8"
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
      "0055cc80",
      "READ",
      [
        "storage",
        "002a2559",
        null,
        "string"
      ]
    ],
    [
      "0055cc88",
      "READ",
      [
        "storage",
        "002a255e",
        null,
        "string"
      ]
    ],
    [
      "0055cc9c",
      "READ",
      [
        "storage",
        "00291bdc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055cc80",
      "READ",
      [
        "storage",
        "002a2552",
        null,
        "string"
      ]
    ],
    [
      "0055cc88",
      "READ",
      [
        "storage",
        "002a2557",
        null,
        "string"
      ]
    ],
    [
      "0055cc9c",
      "READ",
      [
        "storage",
        "00291c69",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055cc7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055cc34.md#insn-0055cc7c) · [`0055cc8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055cc34.md#insn-0055cc8c)
- 新版 `0055cc7c`（命令位置の公開資料なし） · `0055cc8c`（命令位置の公開資料なし）

~~~diff
- 0055cc7c ["COPY", "tmp:0:8", ["const:559:8"]]
- 0055cc7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055cc7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055cc7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055cc7c ["COPY", "tmp:0:8", ["const:552:8"]]
+ 0055cc7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055cc7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055cc7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055cc7c bytes 29651591
+ 0055cc7c bytes 29491591
- 0055cc8c ["COPY", "register:4048:8", ["const:291000:8"]]
- 0055cc8c bytes a9e9ffb0
+ 0055cc8c ["COPY", "register:4048:8", ["const:291000:8"]]
+ 0055cc8c bytes a9e9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3387cfb10b0cea260d1c787c3078a42"></a>

### [`0055ced0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055ced0.md) → [`0055ced0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055ced0.md) FUN_0055ced0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005323c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005323c8.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055cc34.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`005323c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323c8.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cc34.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055cf0c",
      "incomplete_value": true,
      "site": "0055cf0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cf0c",
      "incomplete_value": true,
      "site": "0055cf0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:645:8"
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
      "0055cef0",
      "READ",
      [
        "storage",
        "0029c645",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055cef0",
      "READ",
      [
        "storage",
        "0029c6d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055cee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055ced0.md#insn-0055cee8)
- 新版 `0055cee8`（命令位置の公開資料なし）

~~~diff
- 0055cee8 ["COPY", "tmp:0:8", ["const:645:8"]]
- 0055cee8 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 0055cee8 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 0055cee8 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0055cee8 ["COPY", "tmp:0:8", ["const:6d2:8"]]
+ 0055cee8 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0055cee8 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0055cee8 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 0055cee8 bytes 6b151991
+ 0055cee8 bytes 6b491b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-650db2a1d6a9260122b5fded2519771a"></a>

### [`0055cf7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055cf7c.md) → [`0055cf7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cf7c.md) FUN_0055cf7c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005323cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005323cc.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055cc34.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`005323cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323cc.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cc34.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055cfb0",
      "incomplete_value": true,
      "site": "0055cfb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:75e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055cfb0",
      "incomplete_value": true,
      "site": "0055cfb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:767:8"
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
      "definition_site": "0055cfb4",
      "incomplete_value": true,
      "site": "0055cfb4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0055cfb4",
      "incomplete_value": true,
      "site": "0055cfb4",
      "value": [
        "LOAD",
        "8",
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
      "0055cf9c",
      "READ",
      [
        "storage",
        "002a9767",
        null,
        "string"
      ]
    ],
    [
      "0055cfa8",
      "READ",
      [
        "storage",
        "002a976d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055cf9c",
      "READ",
      [
        "storage",
        "002a975e",
        null,
        "string"
      ]
    ],
    [
      "0055cfa8",
      "READ",
      [
        "storage",
        "002a9764",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055cf94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055cf7c.md#insn-0055cf94)
- 新版 `0055cf94`（命令位置の公開資料なし）

~~~diff
- 0055cf94 ["COPY", "tmp:0:8", ["const:767:8"]]
- 0055cf94 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0055cf94 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0055cf94 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0055cf94 ["COPY", "tmp:0:8", ["const:75e:8"]]
+ 0055cf94 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0055cf94 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0055cf94 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0055cf94 bytes 4a9d1d91
+ 0055cf94 bytes 4a791d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0604a95daadafe24a94743c59e4e4e2"></a>

### [`0055d0c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d0c8.md) → [`0055d0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d0c8.md) FUN_0055d0c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005323d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005323d4.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055cc34.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`005323d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323d4.md) · 呼出先 3件 [`0055cc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055cc34.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055d0fc",
      "incomplete_value": true,
      "site": "0055d0fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:643:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d0fc",
      "incomplete_value": true,
      "site": "0055d0fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b6:8"
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
      "definition_site": "0055d100",
      "incomplete_value": true,
      "site": "0055d100",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0055d100",
      "incomplete_value": true,
      "site": "0055d100",
      "value": [
        "LOAD",
        "8",
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
      "0055d0e8",
      "READ",
      [
        "storage",
        "0029f5b6",
        null,
        "string"
      ]
    ],
    [
      "0055d0f4",
      "READ",
      [
        "storage",
        "0029f5bb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055d0e8",
      "READ",
      [
        "storage",
        "0029f643",
        null,
        "string"
      ]
    ],
    [
      "0055d0f4",
      "READ",
      [
        "storage",
        "0029f648",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d0c8.md#insn-0055d0e0)
- 新版 `0055d0e0`（命令位置の公開資料なし）

~~~diff
- 0055d0e0 ["COPY", "tmp:0:8", ["const:5b6:8"]]
- 0055d0e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0055d0e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0055d0e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0055d0e0 ["COPY", "tmp:0:8", ["const:643:8"]]
+ 0055d0e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0055d0e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0055d0e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0055d0e0 bytes 4ad91691
+ 0055d0e0 bytes 4a0d1991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bd90c7817b9ce2c0378f656cc10c39d"></a>

### [`0055d170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d170.md) → [`0055d170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d170.md) FUN_0055d170

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
      "definition_site": "0055d174",
      "incomplete_value": false,
      "site": "0055d178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d174",
      "incomplete_value": false,
      "site": "0055d178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "0055d178",
      "DATA",
      [
        "storage",
        "00bef400",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055d178",
      "DATA",
      [
        "storage",
        "00bef4b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d170.md#insn-0055d174)
- 新版 `0055d174`（命令位置の公開資料なし）

~~~diff
- 0055d174 ["COPY", "tmp:0:8", ["const:400:8"]]
- 0055d174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055d174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055d174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d174 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 0055d174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055d174 bytes 08011091
+ 0055d174 bytes 08c11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-619761d23d397c8582e100f2ba391336"></a>

### [`0055d180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d180.md) → [`0055d180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d180.md) FUN_0055d180

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
      "definition_site": "0055d190",
      "incomplete_value": false,
      "site": "0055d198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d190",
      "incomplete_value": false,
      "site": "0055d198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:400:8"
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
      "0055d198",
      "DATA",
      [
        "storage",
        "00bef400",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055d198",
      "DATA",
      [
        "storage",
        "00bef4b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d180.md#insn-0055d190)
- 新版 `0055d190`（命令位置の公開資料なし）

~~~diff
- 0055d190 ["COPY", "tmp:0:8", ["const:400:8"]]
- 0055d190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055d190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055d190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d190 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 0055d190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055d190 bytes 08011091
+ 0055d190 bytes 08c11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab798e6c4c6533699db0010c672f29a2"></a>

### [`0055d1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d1c0.md) → [`0055d1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d1c0.md) FUN_0055d1c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005397f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/005397f8.md) · 呼出先 17件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`005397fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/005397fc.md) [`00539804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539804.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md)
- 新版 呼出元 1件 [`005397f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397f8.md) · 呼出先 17件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`005397fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397fc.md) [`00539804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539804.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055d228",
      "incomplete_value": true,
      "site": "0055d228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:560:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d228",
      "incomplete_value": true,
      "site": "0055d228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:567:8"
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
      "definition_site": "0055d240",
      "incomplete_value": true,
      "site": "0055d250",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:57b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d240",
      "incomplete_value": true,
      "site": "0055d250",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4ee:8"
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
      "definition_site": "0055d240",
      "incomplete_value": true,
      "site": "0055d250",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0055d240",
      "incomplete_value": true,
      "site": "0055d250",
      "value": [
        "LOAD",
        "16",
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
      "0055d214",
      "READ",
      [
        "storage",
        "002a2567",
        null,
        "string"
      ]
    ],
    [
      "0055d240",
      "READ",
      [
        "storage",
        "0029d4ee",
        null,
        "string"
      ]
    ],
    [
      "0055d240",
      "READ",
      [
        "storage",
        "0029d4fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055d214",
      "READ",
      [
        "storage",
        "002a2560",
        null,
        "string"
      ]
    ],
    [
      "0055d240",
      "READ",
      [
        "storage",
        "0029d57b",
        null,
        "string"
      ]
    ],
    [
      "0055d240",
      "READ",
      [
        "storage",
        "0029d58b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d1c0.md#insn-0055d208) · [`0055d238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d1c0.md#insn-0055d238) · [`0055d23c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d1c0.md#insn-0055d23c)
- 新版 `0055d208`（命令位置の公開資料なし） · `0055d238`（命令位置の公開資料なし）

~~~diff
- 0055d208 ["COPY", "tmp:0:8", ["const:567:8"]]
- 0055d208 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055d208 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055d208 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055d208 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 0055d208 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055d208 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055d208 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055d208 bytes 299d1591
+ 0055d208 bytes 29811591
- 0055d238 ["COPY", "tmp:0:8", ["const:4ee:8"]]
- 0055d238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055d238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055d238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d238 ["COPY", "tmp:0:8", ["const:57b:8"]]
+ 0055d238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055d238 bytes 08b91391
+ 0055d238 bytes 08ed1591
- 0055d23c ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0055d23c bytes a9eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d7e6970dda66ee01078c4b4c4841727"></a>

### [`0055d5cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d5cc.md) → [`0055d5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d5cc.md) FUN_0055d5cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00539948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/00539948.md) · 呼出先 20件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`005398ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00539/005398ec.md) [`0055af10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055af10.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 1件 [`00539948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539948.md) · 呼出先 20件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005398ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005398ec.md) [`0055af10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055af10.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.68% / 新版 93.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055d620",
      "incomplete_value": true,
      "site": "0055d620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d620",
      "incomplete_value": true,
      "site": "0055d620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a27:8"
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
      "definition_site": "0055d63c",
      "incomplete_value": true,
      "site": "0055d64c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cda:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055d63c",
      "incomplete_value": true,
      "site": "0055d64c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c4d:8"
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
      "definition_site": "0055d63c",
      "incomplete_value": true,
      "site": "0055d64c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0055d63c",
      "incomplete_value": true,
      "site": "0055d64c",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055d610",
      "READ",
      [
        "storage",
        "002aca27",
        null,
        "string"
      ]
    ],
    [
      "0055d63c",
      "READ",
      [
        "storage",
        "00297c4d",
        null,
        "string"
      ]
    ],
    [
      "0055d63c",
      "READ",
      [
        "storage",
        "00297c5d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055d610",
      "READ",
      [
        "storage",
        "002aca1e",
        null,
        "string"
      ]
    ],
    [
      "0055d63c",
      "READ",
      [
        "storage",
        "00297cda",
        null,
        "string"
      ]
    ],
    [
      "0055d63c",
      "READ",
      [
        "storage",
        "00297cea",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055d608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d5cc.md#insn-0055d608) · [`0055d634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d5cc.md#insn-0055d634) · [`0055d638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d5cc.md#insn-0055d638)
- 新版 `0055d608`（命令位置の公開資料なし） · `0055d634`（命令位置の公開資料なし）

~~~diff
- 0055d608 ["COPY", "tmp:0:8", ["const:a27:8"]]
- 0055d608 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055d608 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055d608 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055d608 ["COPY", "tmp:0:8", ["const:a1e:8"]]
+ 0055d608 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055d608 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055d608 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055d608 bytes 299d2891
+ 0055d608 bytes 29792891
- 0055d634 ["COPY", "tmp:0:8", ["const:c4d:8"]]
- 0055d634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055d634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055d634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d634 ["COPY", "tmp:0:8", ["const:cda:8"]]
+ 0055d634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055d634 bytes 08353191
+ 0055d634 bytes 08693391
- 0055d638 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0055d638 bytes a9eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee64811e3dfbbb03cdf41f3c89237204"></a>

### [`0055d9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d9b0.md) → [`0055d9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d9b0.md) FUN_0055d9b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053d57c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d57c.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0053d57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d57c.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055daf8",
      "incomplete_value": false,
      "site": "0055db04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055daf8",
      "incomplete_value": false,
      "site": "0055db04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "0055db04",
      "DATA",
      [
        "storage",
        "00bef450",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055db04",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055daf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d9b0.md#insn-0055daf8)
- 新版 `0055daf8`（命令位置の公開資料なし）

~~~diff
- 0055daf8 ["COPY", "tmp:0:8", ["const:450:8"]]
- 0055daf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055daf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055daf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055daf8 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0055daf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055daf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055daf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055daf8 bytes 08411191
+ 0055daf8 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-475698d1277975246a65d217a613db1d"></a>

### [`0055dc58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055dc58.md) → [`0055dc58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055dc58.md) FUN_0055dc58

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0053d584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d584.md) · 呼出先 8件 [`00567d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567d4c.md) [`00574734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574734.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`0053d584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d584.md) · 呼出先 8件 [`00567d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d4c.md) [`00574734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574734.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055dcbc",
      "incomplete_value": false,
      "site": "0055dcc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055dcbc",
      "incomplete_value": false,
      "site": "0055dcc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
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
      "0055dcc8",
      "DATA",
      [
        "storage",
        "00bef1a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055dcc8",
      "DATA",
      [
        "storage",
        "00bef250",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055dcbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055dc58.md#insn-0055dcbc)
- 新版 `0055dcbc`（命令位置の公開資料なし）

~~~diff
- 0055dcbc ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 0055dcbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055dcbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055dcbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055dcbc ["COPY", "tmp:0:8", ["const:250:8"]]
+ 0055dcbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055dcbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055dcbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055dcbc bytes 08810691
+ 0055dcbc bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc3eafe08bc2263bc374cac434485623"></a>

### [`0055ddc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055ddc8.md) → [`0055ddc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055ddc8.md) FUN_0055ddc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053bda8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053bda8.md) · 呼出先 9件 [`0041e0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e0fc.md) [`00513fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/00513fb0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`0053bda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bda8.md) · 呼出先 9件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00513fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513fb0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.59% / 新版 90.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055de88",
      "incomplete_value": true,
      "site": "0055de88",
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
      "definition_site": "0055de88",
      "incomplete_value": true,
      "site": "0055de88",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055dedc",
      "incomplete_value": false,
      "site": "0055dee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055dedc",
      "incomplete_value": false,
      "site": "0055dee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "definition_site": "0055def4",
      "incomplete_value": false,
      "site": "0055def4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055def4",
      "incomplete_value": false,
      "site": "0055def4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "0055de70",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "0055de88",
      "DATA",
      [
        "storage",
        "00bea2c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0055dee4",
      "DATA",
      [
        "storage",
        "00bef4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055de70",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "0055de88",
      "DATA",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0055dee4",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055de70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055ddc8.md#insn-0055de70) · [`0055dedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055ddc8.md#insn-0055dedc) · [`0055dee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055ddc8.md#insn-0055dee8)
- 新版 `0055de70`（命令位置の公開資料なし） · `0055dedc`（命令位置の公開資料なし）

~~~diff
- 0055de70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef0:8"]]
- 0055de70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0055de70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
+ 0055de70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0055de70 bytes 087947f9
+ 0055de70 bytes 08d147f9
- 0055dedc ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 0055dedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055dedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055dedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055dedc ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0055dedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055dedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055dedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055dedc bytes 08811291
+ 0055dedc bytes 08411591
- 0055dee8 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 0055dee8 bytes 883400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2418bcc1226a696f289df4ae108e4ed"></a>

### [`0055e170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e170.md) → [`0055e170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e170.md) FUN_0055e170

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053bdac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053bdac.md) · 呼出先 12件 [`00574734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574734.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`0053bdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bdac.md) · 呼出先 12件 [`00574734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574734.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.50% / 新版 95.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055e210",
      "incomplete_value": true,
      "site": "0055e210",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:643:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e210",
      "incomplete_value": true,
      "site": "0055e210",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5b6:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055e1ac",
      "incomplete_value": false,
      "site": "0055e1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e1ac",
      "incomplete_value": false,
      "site": "0055e1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "definition_site": "0055e1b4",
      "incomplete_value": false,
      "site": "0055e1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e1b4",
      "incomplete_value": false,
      "site": "0055e1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
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
      "0055e1ac",
      "PARAM",
      [
        "storage",
        "00bef508",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e1b4",
      "PARAM",
      [
        "storage",
        "00bef5a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e1f0",
      "READ",
      [
        "storage",
        "0029e5b6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055e1ac",
      "PARAM",
      [
        "storage",
        "00bef5b8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e1b4",
      "PARAM",
      [
        "storage",
        "00bef658",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e1f0",
      "READ",
      [
        "storage",
        "0029e643",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e170.md#insn-0055e1ac) · [`0055e1b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e170.md#insn-0055e1b4) · [`0055e1e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e170.md#insn-0055e1e8)
- 新版 `0055e1ac`（命令位置の公開資料なし） · `0055e1b4`（命令位置の公開資料なし） · `0055e1e8`（命令位置の公開資料なし）

~~~diff
- 0055e1ac ["COPY", "tmp:0:8", ["const:508:8"]]
- 0055e1ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0055e1ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0055e1ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0055e1ac ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 0055e1ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0055e1ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0055e1ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0055e1ac bytes 21201491
+ 0055e1ac bytes 21e01691
- 0055e1b4 ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 0055e1b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0055e1b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0055e1b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0055e1b4 ["COPY", "tmp:0:8", ["const:658:8"]]
+ 0055e1b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0055e1b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0055e1b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0055e1b4 bytes 42a01691
+ 0055e1b4 bytes 42601991
- 0055e1e8 ["COPY", "tmp:0:8", ["const:5b6:8"]]
- 0055e1e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055e1e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055e1e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055e1e8 ["COPY", "tmp:0:8", ["const:643:8"]]
+ 0055e1e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055e1e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055e1e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055e1e8 bytes 29d91691
+ 0055e1e8 bytes 290d1991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-644dc8a38c86385f0385dfb6def20e66"></a>

### [`0055e3a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e3a4.md) → [`0055e3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e3a4.md) FUN_0055e3a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053bdb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053bdb0.md) · 呼出先 10件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`0053bdb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bdb0.md) · 呼出先 10件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.79% / 新版 92.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055e430",
      "incomplete_value": true,
      "site": "0055e440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:651:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e430",
      "incomplete_value": true,
      "site": "0055e440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5c4:8"
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
      "definition_site": "0055e434",
      "incomplete_value": true,
      "site": "0055e444",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0055e434",
      "incomplete_value": true,
      "site": "0055e444",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055e3e0",
      "incomplete_value": false,
      "site": "0055e3f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e3e0",
      "incomplete_value": false,
      "site": "0055e3f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:508:8"
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
      "0055e3e0",
      "PARAM",
      [
        "storage",
        "00bef508",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e3e8",
      "PARAM",
      [
        "storage",
        "00bef518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e430",
      "READ",
      [
        "storage",
        "0029f5c4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055e3e0",
      "PARAM",
      [
        "storage",
        "00bef5b8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e3e8",
      "PARAM",
      [
        "storage",
        "00bef5c8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0055e430",
      "READ",
      [
        "storage",
        "0029f651",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e3e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e3a4.md#insn-0055e3e0) · [`0055e3e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e3a4.md#insn-0055e3e8) · [`0055e428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e3a4.md#insn-0055e428)
- 新版 `0055e3e0`（命令位置の公開資料なし） · `0055e3e8`（命令位置の公開資料なし） · `0055e428`（命令位置の公開資料なし）

~~~diff
- 0055e3e0 ["COPY", "tmp:0:8", ["const:508:8"]]
- 0055e3e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0055e3e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0055e3e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0055e3e0 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 0055e3e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0055e3e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0055e3e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0055e3e0 bytes 21201491
+ 0055e3e0 bytes 21e01691
- 0055e3e8 ["COPY", "tmp:0:8", ["const:518:8"]]
- 0055e3e8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0055e3e8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0055e3e8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0055e3e8 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 0055e3e8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0055e3e8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0055e3e8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0055e3e8 bytes 42601491
+ 0055e3e8 bytes 42201791
- 0055e428 ["COPY", "tmp:0:8", ["const:5c4:8"]]
- 0055e428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055e428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055e428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e428 ["COPY", "tmp:0:8", ["const:651:8"]]
+ 0055e428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055e428 bytes 08111791
+ 0055e428 bytes 08451991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb3d13a648b1091cfe31df22537579e2"></a>

### [`0055e5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e5bc.md) → [`0055e5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e5bc.md) FUN_0055e5bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053be30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053be30.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0055f0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f0e4.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 1件 [`0053be30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053be30.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0055f0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0e4.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055e640",
      "incomplete_value": true,
      "site": "0055e654",
      "value": [
        "LOAD",
        "16",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055e640",
      "incomplete_value": true,
      "site": "0055e654",
      "value": [
        "LOAD",
        "16",
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
                "const:20:8"
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
      "definition_site": "0055e640",
      "incomplete_value": true,
      "site": "0055e654",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0055e640",
      "incomplete_value": true,
      "site": "0055e654",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055e64c",
      "incomplete_value": true,
      "site": "0055e658",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0055e64c",
      "incomplete_value": true,
      "site": "0055e658",
      "value": [
        "LOAD",
        "16",
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
      "0055e640",
      "READ",
      [
        "storage",
        "002a68d2",
        null,
        "string"
      ]
    ],
    [
      "0055e640",
      "READ",
      [
        "storage",
        "002a68e2",
        null,
        "string"
      ]
    ],
    [
      "0055e64c",
      "READ",
      [
        "storage",
        "002a68f2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055e640",
      "READ",
      [
        "storage",
        "002a68cb",
        null,
        "string"
      ]
    ],
    [
      "0055e640",
      "READ",
      [
        "storage",
        "002a68db",
        null,
        "string"
      ]
    ],
    [
      "0055e64c",
      "READ",
      [
        "storage",
        "002a68eb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e63c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e5bc.md#insn-0055e63c) · [`0055e778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e5bc.md#insn-0055e778)
- 新版 `0055e63c`（命令位置の公開資料なし） · `0055e778`（命令位置の公開資料なし）

~~~diff
- 0055e63c ["COPY", "tmp:0:8", ["const:8b2:8"]]
- 0055e63c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055e63c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055e63c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e63c ["COPY", "tmp:0:8", ["const:8ab:8"]]
+ 0055e63c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e63c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e63c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055e63c bytes 08c92291
+ 0055e63c bytes 08ad2291
- 0055e778 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 0055e778 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055e778 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055e778 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e778 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 0055e778 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e778 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e778 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055e778 bytes 08411791
+ 0055e778 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed8afabd9417550ffde15b79fd2f774e"></a>

### [`0055e88c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e88c.md) → [`0055e88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e88c.md) FUN_0055e88c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0053c1bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c1bc.md) [`0053c1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c1c0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0055f0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f0e4.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 2件 [`0053c1bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c1bc.md) [`0053c1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c1c0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0055f0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0e4.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.53% / 新版 96.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ea48",
      "incomplete_value": false,
      "site": "0055ea54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ea48",
      "incomplete_value": false,
      "site": "0055ea54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      "0055e910",
      "READ",
      [
        "storage",
        "002a68d2",
        null,
        "string"
      ]
    ],
    [
      "0055e910",
      "READ",
      [
        "storage",
        "002a68e2",
        null,
        "string"
      ]
    ],
    [
      "0055e91c",
      "READ",
      [
        "storage",
        "002a68f2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055e910",
      "READ",
      [
        "storage",
        "002a68cb",
        null,
        "string"
      ]
    ],
    [
      "0055e910",
      "READ",
      [
        "storage",
        "002a68db",
        null,
        "string"
      ]
    ],
    [
      "0055e91c",
      "READ",
      [
        "storage",
        "002a68eb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055e90c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e88c.md#insn-0055e90c) · [`0055ea48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e88c.md#insn-0055ea48)
- 新版 `0055e90c`（命令位置の公開資料なし） · `0055ea48`（命令位置の公開資料なし）

~~~diff
- 0055e90c ["COPY", "tmp:0:8", ["const:8b2:8"]]
- 0055e90c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055e90c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055e90c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e90c ["COPY", "tmp:0:8", ["const:8ab:8"]]
+ 0055e90c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e90c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e90c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055e90c bytes 08c92291
+ 0055e90c bytes 08ad2291
- 0055ea48 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 0055ea48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ea48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ea48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ea48 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 0055ea48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ea48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ea48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ea48 bytes 08411791
+ 0055ea48 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb38bd64e352cc799a66624a4ad2bef6"></a>

### [`0055eb5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055eb5c.md) → [`0055eb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055eb5c.md) FUN_0055eb5c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0053b878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b878.md) [`0053b998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b998.md) [`0053b99c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053b99c.md) · 呼出先 2件 [`0055f8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f8e0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 3件 [`0053b878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b878.md) [`0053b998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b998.md) [`0053b99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b99c.md) · 呼出先 2件 [`0055f8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f8e0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055eb84",
      "incomplete_value": false,
      "site": "0055eb90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055eb84",
      "incomplete_value": false,
      "site": "0055eb90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:688:8"
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
      "0055eb90",
      "DATA",
      [
        "storage",
        "00bef688",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055eb90",
      "DATA",
      [
        "storage",
        "00bef738",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055eb84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055eb5c.md#insn-0055eb84)
- 新版 `0055eb84`（命令位置の公開資料なし）

~~~diff
- 0055eb84 ["COPY", "tmp:0:8", ["const:688:8"]]
- 0055eb84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055eb84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055eb84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055eb84 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 0055eb84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055eb84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055eb84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055eb84 bytes 08211a91
+ 0055eb84 bytes 08e11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23778dd38c16ee2b48c007bbddc06e68"></a>

### [`0055ebd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055ebd0.md) → [`0055ebd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ebd0.md) FUN_0055ebd0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`0053baf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053baf0.md) [`0053bc44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053b/0053bc44.md) · 呼出先 2件 [`0055fe08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fe08.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 2件 [`0053baf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053baf0.md) [`0053bc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053bc44.md) · 呼出先 2件 [`0055fe08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fe08.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0055ec00",
      "incomplete_value": false,
      "site": "0055ec0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ec00",
      "incomplete_value": false,
      "site": "0055ec0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "0055ec0c",
      "DATA",
      [
        "storage",
        "00bef730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ec0c",
      "DATA",
      [
        "storage",
        "00bef7e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ec00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055ebd0.md#insn-0055ec00)
- 新版 `0055ec00`（命令位置の公開資料なし）

~~~diff
- 0055ec00 ["COPY", "tmp:0:8", ["const:730:8"]]
- 0055ec00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ec00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ec00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ec00 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 0055ec00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ec00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ec00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ec00 bytes 08c11c91
+ 0055ec00 bytes 08811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1501c73d0b294c5e706e1a8d348ef4c3"></a>

### [`0055eef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055eef8.md) → [`0055eef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055eef8.md) FUN_0055eef8

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
      "definition_site": "0055eefc",
      "incomplete_value": false,
      "site": "0055ef00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055eefc",
      "incomplete_value": false,
      "site": "0055ef00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "0055ef00",
      "DATA",
      [
        "storage",
        "00bef450",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055ef00",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055eefc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055eef8.md#insn-0055eefc)
- 新版 `0055eefc`（命令位置の公開資料なし）

~~~diff
- 0055eefc ["COPY", "tmp:0:8", ["const:450:8"]]
- 0055eefc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055eefc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055eefc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055eefc ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0055eefc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055eefc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055eefc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055eefc bytes 08411191
+ 0055eefc bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fe7ddf0ce4f45369d388bf6fdde4adc"></a>

### [`0055ef48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055ef48.md) → [`0055ef48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ef48.md) FUN_0055ef48

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
      "definition_site": "0055ef4c",
      "incomplete_value": false,
      "site": "0055ef50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ef4c",
      "incomplete_value": false,
      "site": "0055ef50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "0055ef50",
      "DATA",
      [
        "storage",
        "00bef4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ef50",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ef4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055ef48.md#insn-0055ef4c)
- 新版 `0055ef4c`（命令位置の公開資料なし）

~~~diff
- 0055ef4c ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 0055ef4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ef4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ef4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ef4c ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0055ef4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ef4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ef4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ef4c bytes 08811291
+ 0055ef4c bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9be2373c6203089e8fc205cfb50bcd82"></a>

### [`0055ef58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055ef58.md) → [`0055ef58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ef58.md) FUN_0055ef58

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
      "definition_site": "0055ef68",
      "incomplete_value": false,
      "site": "0055ef70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ef68",
      "incomplete_value": false,
      "site": "0055ef70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      "0055ef70",
      "DATA",
      [
        "storage",
        "00bef4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ef70",
      "DATA",
      [
        "storage",
        "00bef550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055ef68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055ef58.md#insn-0055ef68)
- 新版 `0055ef68`（命令位置の公開資料なし）

~~~diff
- 0055ef68 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 0055ef68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055ef68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055ef68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055ef68 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 0055ef68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ef68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055ef68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055ef68 bytes 08811291
+ 0055ef68 bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7f9314b8373878833dd662395e7b8c4"></a>

### [`0055efe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055efe8.md) → [`0055efe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055efe8.md) FUN_0055efe8

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
      "definition_site": "0055efec",
      "incomplete_value": false,
      "site": "0055eff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055efec",
      "incomplete_value": false,
      "site": "0055eff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "0055eff0",
      "DATA",
      [
        "storage",
        "00bef540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055eff0",
      "DATA",
      [
        "storage",
        "00bef5f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055efec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055efe8.md#insn-0055efec)
- 新版 `0055efec`（命令位置の公開資料なし）

~~~diff
- 0055efec ["COPY", "tmp:0:8", ["const:540:8"]]
- 0055efec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055efec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055efec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055efec ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 0055efec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055efec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055efec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055efec bytes 08011591
+ 0055efec bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3f1e8e07a2077d8c1a41eea00f9bb87"></a>

### [`0055eff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055eff8.md) → [`0055eff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055eff8.md) FUN_0055eff8

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
      "definition_site": "0055f008",
      "incomplete_value": false,
      "site": "0055f010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f008",
      "incomplete_value": false,
      "site": "0055f010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "0055f010",
      "DATA",
      [
        "storage",
        "00bef540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f010",
      "DATA",
      [
        "storage",
        "00bef5f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055eff8.md#insn-0055f008)
- 新版 `0055f008`（命令位置の公開資料なし）

~~~diff
- 0055f008 ["COPY", "tmp:0:8", ["const:540:8"]]
- 0055f008 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f008 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f008 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f008 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 0055f008 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f008 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f008 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f008 bytes 08011591
+ 0055f008 bytes 08c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-149421b8f3943968c97bf30068c5fd4a"></a>

### [`0055f094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f094.md) → [`0055f094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f094.md) FUN_0055f094

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
      "definition_site": "0055f098",
      "incomplete_value": false,
      "site": "0055f09c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f098",
      "incomplete_value": false,
      "site": "0055f09c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      "0055f09c",
      "DATA",
      [
        "storage",
        "00bef5d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f09c",
      "DATA",
      [
        "storage",
        "00bef680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f094.md#insn-0055f098)
- 新版 `0055f098`（命令位置の公開資料なし）

~~~diff
- 0055f098 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 0055f098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f098 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 0055f098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f098 bytes 08411791
+ 0055f098 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32162fff14fe41ac217a6665ef23586b"></a>

### [`0055f0a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f0a4.md) → [`0055f0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0a4.md) FUN_0055f0a4

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
      "definition_site": "0055f0b4",
      "incomplete_value": false,
      "site": "0055f0bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f0b4",
      "incomplete_value": false,
      "site": "0055f0bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      "0055f0bc",
      "DATA",
      [
        "storage",
        "00bef5d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f0bc",
      "DATA",
      [
        "storage",
        "00bef680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f0b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f0a4.md#insn-0055f0b4)
- 新版 `0055f0b4`（命令位置の公開資料なし）

~~~diff
- 0055f0b4 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 0055f0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f0b4 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 0055f0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f0b4 bytes 08411791
+ 0055f0b4 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62414e164d6c90e75d5d2b762405ab8b"></a>

### [`0055f0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f0e4.md) → [`0055f0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0e4.md) FUN_0055f0e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0055e5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e5bc.md) [`0055e88c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e88c.md) · 呼出先 5件 [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`005668b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/005668b8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 2件 [`0055e5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e5bc.md) [`0055e88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e88c.md) · 呼出先 5件 [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`005668b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/005668b8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f120",
      "incomplete_value": false,
      "site": "0055f120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f120",
      "incomplete_value": false,
      "site": "0055f120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "0055f160",
      "incomplete_value": true,
      "site": "0055f170",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5fc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f160",
      "incomplete_value": true,
      "site": "0055f170",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:603:8"
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
      "definition_site": "0055f160",
      "incomplete_value": true,
      "site": "0055f170",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0055f160",
      "incomplete_value": true,
      "site": "0055f170",
      "value": [
        "LOAD",
        "16",
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
      "0055f120",
      "DATA",
      [
        "storage",
        "00bef620",
        null,
        "undefined *"
      ]
    ],
    [
      "0055f160",
      "READ",
      [
        "storage",
        "002a4603",
        null,
        "string"
      ]
    ],
    [
      "0055f160",
      "READ",
      [
        "storage",
        "002a4613",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055f120",
      "DATA",
      [
        "storage",
        "00bef6d0",
        null,
        "undefined *"
      ]
    ],
    [
      "0055f160",
      "READ",
      [
        "storage",
        "002a45fc",
        null,
        "string"
      ]
    ],
    [
      "0055f160",
      "READ",
      [
        "storage",
        "002a460c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f0e4.md#insn-0055f100) · [`0055f158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f0e4.md#insn-0055f158) · [`0055f15c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f0e4.md#insn-0055f15c)
- 新版 `0055f100`（命令位置の公開資料なし） · `0055f158`（命令位置の公開資料なし）

~~~diff
- 0055f100 ["COPY", "tmp:0:8", ["const:620:8"]]
- 0055f100 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055f100 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055f100 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055f100 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 0055f100 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055f100 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055f100 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055f100 bytes 29811891
+ 0055f100 bytes 29411b91
- 0055f158 ["COPY", "tmp:0:8", ["const:603:8"]]
- 0055f158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f158 ["COPY", "tmp:0:8", ["const:5fc:8"]]
+ 0055f158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f158 bytes 080d1891
+ 0055f158 bytes 08f11791
- 0055f15c ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0055f15c bytes 89eaffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9f0cddc90d1a8de93ce291d54427649"></a>

### [`0055f2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f2c0.md) → [`0055f2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f2c0.md) FUN_0055f2c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`005679e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/005679e4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005679e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005679e4.md)

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
      "definition_site": "0055f2c8",
      "incomplete_value": false,
      "site": "0055f2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f2c8",
      "incomplete_value": false,
      "site": "0055f2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "0055f2c8",
      "DATA",
      [
        "storage",
        "00bef620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f2c8",
      "DATA",
      [
        "storage",
        "00bef6d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f2c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f2c0.md#insn-0055f2c4)
- 新版 `0055f2c4`（命令位置の公開資料なし）

~~~diff
- 0055f2c4 ["COPY", "tmp:0:8", ["const:620:8"]]
- 0055f2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f2c4 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 0055f2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f2c4 bytes 08811891
+ 0055f2c4 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b545fa15792ec1d5aca20f09ea7bab22"></a>

### [`0055f2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f2d0.md) → [`0055f2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f2d0.md) FUN_0055f2d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005679e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/005679e4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005679e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005679e4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0055f2e8",
      "incomplete_value": false,
      "site": "0055f2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f2e8",
      "incomplete_value": false,
      "site": "0055f2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "0055f2e8",
      "DATA",
      [
        "storage",
        "00bef620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f2e8",
      "DATA",
      [
        "storage",
        "00bef6d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f2d0.md#insn-0055f2e0)
- 新版 `0055f2e0`（命令位置の公開資料なし）

~~~diff
- 0055f2e0 ["COPY", "tmp:0:8", ["const:620:8"]]
- 0055f2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f2e0 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 0055f2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f2e0 bytes 08811891
+ 0055f2e0 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36e200d007fbb72419e86f1372048368"></a>

### [`0055f300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f300.md) → [`0055f300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f300.md) FUN_0055f300

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566d10.md) [`00566df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566df0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566d10.md) [`00566df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566df0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f3dc",
      "incomplete_value": false,
      "site": "0055f3e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f3dc",
      "incomplete_value": false,
      "site": "0055f3e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "0055f3e8",
      "DATA",
      [
        "storage",
        "00bef450",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055f3e8",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f3dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f300.md#insn-0055f3dc)
- 新版 `0055f3dc`（命令位置の公開資料なし）

~~~diff
- 0055f3dc ["COPY", "tmp:0:8", ["const:450:8"]]
- 0055f3dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f3dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f3dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f3dc ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0055f3dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f3dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f3dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f3dc bytes 08411191
+ 0055f3dc bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3513bc2f72900efd79e4d4e2e0aa63f5"></a>

### [`0055f488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f488.md) → [`0055f488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f488.md) FUN_0055f488

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566d10.md) [`00566e98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566e98.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566d10.md) [`00566e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566e98.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f56c",
      "incomplete_value": false,
      "site": "0055f578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f56c",
      "incomplete_value": false,
      "site": "0055f578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "0055f578",
      "DATA",
      [
        "storage",
        "00bef450",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055f578",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f56c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f488.md#insn-0055f56c)
- 新版 `0055f56c`（命令位置の公開資料なし）

~~~diff
- 0055f56c ["COPY", "tmp:0:8", ["const:450:8"]]
- 0055f56c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f56c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f56c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f56c ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0055f56c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f56c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f56c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f56c bytes 08411191
+ 0055f56c bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caeec836fd49b2c3e383c2d7ff18da2d"></a>

### [`0055f61c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f61c.md) → [`0055f61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f61c.md) FUN_0055f61c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566d10.md) [`00566e98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566e98.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566d10.md) [`00566e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566e98.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.47% / 新版 97.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f6ec",
      "incomplete_value": false,
      "site": "0055f6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f6ec",
      "incomplete_value": false,
      "site": "0055f6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "0055f6f8",
      "DATA",
      [
        "storage",
        "00bef450",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055f6f8",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f6ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f61c.md#insn-0055f6ec)
- 新版 `0055f6ec`（命令位置の公開資料なし）

~~~diff
- 0055f6ec ["COPY", "tmp:0:8", ["const:450:8"]]
- 0055f6ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f6ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f6ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f6ec ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0055f6ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f6ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f6ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f6ec bytes 08411191
+ 0055f6ec bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4875b02ef683dbda7f8fe1aef25a3b03"></a>

### [`0055f798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f798.md) → [`0055f798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f798.md) FUN_0055f798

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566d10.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566980.md) [`00566d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566d10.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f828",
      "incomplete_value": false,
      "site": "0055f834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f828",
      "incomplete_value": false,
      "site": "0055f834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "0055f834",
      "DATA",
      [
        "storage",
        "00bef450",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055f834",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f798.md#insn-0055f828)
- 新版 `0055f828`（命令位置の公開資料なし）

~~~diff
- 0055f828 ["COPY", "tmp:0:8", ["const:450:8"]]
- 0055f828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f828 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 0055f828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f828 bytes 08411191
+ 0055f828 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-569aa005cc34bac7cd0468fb66d0e6c7"></a>

### [`0055f8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f8a0.md) → [`0055f8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f8a0.md) FUN_0055f8a0

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
      "definition_site": "0055f8b0",
      "incomplete_value": false,
      "site": "0055f8b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f8b0",
      "incomplete_value": false,
      "site": "0055f8b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:688:8"
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
      "0055f8b8",
      "DATA",
      [
        "storage",
        "00bef688",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f8b8",
      "DATA",
      [
        "storage",
        "00bef738",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f8a0.md#insn-0055f8b0)
- 新版 `0055f8b0`（命令位置の公開資料なし）

~~~diff
- 0055f8b0 ["COPY", "tmp:0:8", ["const:688:8"]]
- 0055f8b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055f8b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055f8b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f8b0 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 0055f8b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f8b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f8b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055f8b0 bytes 08211a91
+ 0055f8b0 bytes 08e11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5f4aeb548f9de16b619e1a684f60960"></a>

### [`0055f8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f8e0.md) → [`0055f8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f8e0.md) FUN_0055f8e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055eb5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055eb5c.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdbea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbea0.md)
- 新版 呼出元 1件 [`0055eb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055eb5c.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbf50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f910",
      "incomplete_value": false,
      "site": "0055f910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055f910",
      "incomplete_value": false,
      "site": "0055f910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
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
      "0055f910",
      "DATA",
      [
        "storage",
        "00bef6d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f910",
      "DATA",
      [
        "storage",
        "00bef788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055f900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f8e0.md#insn-0055f900)
- 新版 `0055f900`（命令位置の公開資料なし）

~~~diff
- 0055f900 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 0055f900 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055f900 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055f900 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055f900 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 0055f900 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055f900 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055f900 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055f900 bytes 29611b91
+ 0055f900 bytes 29211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12fbbf54b4acd8cd0d15384cb5c96944"></a>

### [`0055fa98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fa98.md) → [`0055fa98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fa98.md) FUN_0055fa98

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0055faa8",
      "incomplete_value": false,
      "site": "0055faa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055faa8",
      "incomplete_value": false,
      "site": "0055faa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
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
      "0055faa8",
      "DATA",
      [
        "storage",
        "00bef6d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055faa8",
      "DATA",
      [
        "storage",
        "00bef788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055faa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fa98.md#insn-0055faa4)
- 新版 `0055faa4`（命令位置の公開資料なし）

~~~diff
- 0055faa4 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 0055faa4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055faa4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055faa4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055faa4 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 0055faa4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055faa4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055faa4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055faa4 bytes 29611b91
+ 0055faa4 bytes 29211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38972bc3e4ee112b7ca75162594b1697"></a>

### [`0055fac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fac0.md) → [`0055fac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fac0.md) FUN_0055fac0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0055facc",
      "incomplete_value": false,
      "site": "0055facc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055facc",
      "incomplete_value": false,
      "site": "0055facc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
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
      "0055facc",
      "DATA",
      [
        "storage",
        "00bef6d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055facc",
      "DATA",
      [
        "storage",
        "00bef788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055fac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fac0.md#insn-0055fac8)
- 新版 `0055fac8`（命令位置の公開資料なし）

~~~diff
- 0055fac8 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 0055fac8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055fac8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055fac8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055fac8 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 0055fac8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055fac8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055fac8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055fac8 bytes 29611b91
+ 0055fac8 bytes 29211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74df9f3d83643539f52bb1e1dcfd7fbd"></a>

### [`0055fdb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fdb8.md) → [`0055fdb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fdb8.md) FUN_0055fdb8

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
      "definition_site": "0055fdbc",
      "incomplete_value": false,
      "site": "0055fdc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055fdbc",
      "incomplete_value": false,
      "site": "0055fdc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "0055fdc0",
      "DATA",
      [
        "storage",
        "00bef730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055fdc0",
      "DATA",
      [
        "storage",
        "00bef7e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055fdbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fdb8.md#insn-0055fdbc)
- 新版 `0055fdbc`（命令位置の公開資料なし）

~~~diff
- 0055fdbc ["COPY", "tmp:0:8", ["const:730:8"]]
- 0055fdbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055fdbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055fdbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055fdbc ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 0055fdbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055fdbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055fdbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055fdbc bytes 08c11c91
+ 0055fdbc bytes 08811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55aa6db5f32ce72cac404e12001b74a7"></a>

### [`0055fdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fdc8.md) → [`0055fdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fdc8.md) FUN_0055fdc8

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
      "definition_site": "0055fdd8",
      "incomplete_value": false,
      "site": "0055fde0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055fdd8",
      "incomplete_value": false,
      "site": "0055fde0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:730:8"
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
      "0055fde0",
      "DATA",
      [
        "storage",
        "00bef730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055fde0",
      "DATA",
      [
        "storage",
        "00bef7e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055fdd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fdc8.md#insn-0055fdd8)
- 新版 `0055fdd8`（命令位置の公開資料なし）

~~~diff
- 0055fdd8 ["COPY", "tmp:0:8", ["const:730:8"]]
- 0055fdd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0055fdd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0055fdd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055fdd8 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 0055fdd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055fdd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055fdd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0055fdd8 bytes 08c11c91
+ 0055fdd8 bytes 08811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11bdd039bb700d193049a62ad0cbe6a5"></a>

### [`0055fe08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fe08.md) → [`0055fe08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055fe08.md) FUN_0055fe08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055ebd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055ebd0.md) · 呼出先 4件 [`00499b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00499/00499b28.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdbf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbf40.md)
- 新版 呼出元 1件 [`0055ebd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ebd0.md) · 呼出先 4件 [`00499b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499b28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.53% / 新版 92.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055fe40",
      "incomplete_value": false,
      "site": "0055fe40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055fe40",
      "incomplete_value": false,
      "site": "0055fe40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "definition_site": "0055fe70",
      "incomplete_value": true,
      "site": "0055fe70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055fe70",
      "incomplete_value": true,
      "site": "0055fe70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c7e:8"
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
      "definition_site": "0055ff2c",
      "incomplete_value": true,
      "site": "0055ff2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0055ff2c",
      "incomplete_value": true,
      "site": "0055ff2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:95c:8"
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
      "0055fe40",
      "DATA",
      [
        "storage",
        "00bef780",
        null,
        "undefined *"
      ]
    ],
    [
      "0055fe60",
      "READ",
      [
        "storage",
        "00297c7e",
        null,
        "string"
      ]
    ],
    [
      "0055ff18",
      "READ",
      [
        "storage",
        "0029295c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0055fe40",
      "DATA",
      [
        "storage",
        "00bef830",
        null,
        "undefined *"
      ]
    ],
    [
      "0055fe60",
      "READ",
      [
        "storage",
        "00297d0b",
        null,
        "string"
      ]
    ],
    [
      "0055ff18",
      "READ",
      [
        "storage",
        "002929e9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0055fe34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fe08.md#insn-0055fe34) · [`0055fe58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fe08.md#insn-0055fe58) · [`0055ff10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055fe08.md#insn-0055ff10)
- 新版 `0055fe34`（命令位置の公開資料なし） · `0055fe58`（命令位置の公開資料なし） · `0055ff10`（命令位置の公開資料なし）

~~~diff
- 0055fe34 ["COPY", "tmp:0:8", ["const:780:8"]]
- 0055fe34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055fe34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055fe34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055fe34 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 0055fe34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055fe34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055fe34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055fe34 bytes 29011e91
+ 0055fe34 bytes 29c12091
- 0055fe58 ["COPY", "tmp:0:8", ["const:c7e:8"]]
- 0055fe58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055fe58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055fe58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055fe58 ["COPY", "tmp:0:8", ["const:d0b:8"]]
+ 0055fe58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055fe58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055fe58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055fe58 bytes 29f93191
+ 0055fe58 bytes 292d3491
- 0055ff10 ["COPY", "tmp:0:8", ["const:95c:8"]]
- 0055ff10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0055ff10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0055ff10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055ff10 ["COPY", "tmp:0:8", ["const:9e9:8"]]
+ 0055ff10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055ff10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055ff10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0055ff10 bytes 29712591
+ 0055ff10 bytes 29a52791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c71c8a1e2911f0fa1b3aa3e36ab2a4e"></a>

### [`00560124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/00560124.md) → [`00560124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560124.md) FUN_00560124

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00560134",
      "incomplete_value": false,
      "site": "00560134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560134",
      "incomplete_value": false,
      "site": "00560134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "00560134",
      "DATA",
      [
        "storage",
        "00bef780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560134",
      "DATA",
      [
        "storage",
        "00bef830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/00560124.md#insn-00560130)
- 新版 `00560130`（命令位置の公開資料なし）

~~~diff
- 00560130 ["COPY", "tmp:0:8", ["const:780:8"]]
- 00560130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560130 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00560130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560130 bytes 29011e91
+ 00560130 bytes 29c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-280f89243e19ac2c77857dc5597c99b5"></a>

### [`0056014c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/0056014c.md) → [`0056014c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/0056014c.md) FUN_0056014c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00560158",
      "incomplete_value": false,
      "site": "00560158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560158",
      "incomplete_value": false,
      "site": "00560158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "00560158",
      "DATA",
      [
        "storage",
        "00bef780",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560158",
      "DATA",
      [
        "storage",
        "00bef830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/0056014c.md#insn-00560154)
- 新版 `00560154`（命令位置の公開資料なし）

~~~diff
- 00560154 ["COPY", "tmp:0:8", ["const:780:8"]]
- 00560154 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560154 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560154 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560154 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00560154 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560154 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560154 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560154 bytes 29011e91
+ 00560154 bytes 29c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82477d0409ba852a53ee390966418947"></a>

### [`005605e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005605e0.md) → [`005605e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005605e0.md) FUN_005605e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00560748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/00560748.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00560748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560748.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

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
      "definition_site": "00560600",
      "incomplete_value": false,
      "site": "00560600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560600",
      "incomplete_value": false,
      "site": "00560600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:808:8"
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
      "00560600",
      "DATA",
      [
        "storage",
        "00bef808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00560600",
      "DATA",
      [
        "storage",
        "00bef8b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005605f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005605e0.md#insn-005605f8)
- 新版 `005605f8`（命令位置の公開資料なし）

~~~diff
- 005605f8 ["COPY", "tmp:0:8", ["const:808:8"]]
- 005605f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005605f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005605f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005605f8 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 005605f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005605f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005605f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005605f8 bytes 08212091
+ 005605f8 bytes 08e12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdcc57ec40b23349614b82c61d90a9b0"></a>

### [`00560748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/00560748.md) → [`00560748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560748.md) FUN_00560748

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0053ee58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee58.md) · 呼出先 2件 [`005605e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005605e0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`0053ee58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee58.md) · 呼出先 2件 [`005605e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005605e0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00560784",
      "incomplete_value": false,
      "site": "00560790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560784",
      "incomplete_value": false,
      "site": "00560790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "00560790",
      "DATA",
      [
        "storage",
        "00bef948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560790",
      "DATA",
      [
        "storage",
        "00bef9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/00560748.md#insn-00560784)
- 新版 `00560784`（命令位置の公開資料なし）

~~~diff
- 00560784 ["COPY", "tmp:0:8", ["const:948:8"]]
- 00560784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560784 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00560784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560784 bytes 08212591
+ 00560784 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3ea94d90b4bd4d74b1f9676b4dcb15c"></a>

### [`005609d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005609d4.md) → [`005609d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609d4.md) FUN_005609d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005609cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005609cc.md) [`00561a60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/00561a60.md) · 呼出先 25件 [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00560f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/00560f00.md) [`00564250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564250.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 2件 [`005609cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609cc.md) [`00561a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/00561a60.md) · 呼出先 25件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00560f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560f00.md) [`00564250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564250.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.13% / 新版 95.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00560a68",
      "incomplete_value": true,
      "site": "00560a78",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00560a68",
      "incomplete_value": true,
      "site": "00560a78",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00560a68",
      "incomplete_value": true,
      "site": "00560a78",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00560a68",
      "incomplete_value": true,
      "site": "00560a78",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00560a80",
      "incomplete_value": true,
      "site": "00560a80",
      "value": [
        "LOAD",
        "8",
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
                "const:5d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00560a80",
      "incomplete_value": true,
      "site": "00560a80",
      "value": [
        "LOAD",
        "8",
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
                "const:5d:8"
              ]
            ]
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
      "00560a2c",
      "READ",
      [
        "storage",
        "0029d52d",
        null,
        "string"
      ]
    ],
    [
      "00560a34",
      "READ",
      [
        "storage",
        "0029d533",
        null,
        "string"
      ]
    ],
    [
      "00560a68",
      "READ",
      [
        "storage",
        "002949f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00560a2c",
      "READ",
      [
        "storage",
        "0029d5ba",
        null,
        "string"
      ]
    ],
    [
      "00560a34",
      "READ",
      [
        "storage",
        "0029d5c0",
        null,
        "string"
      ]
    ],
    [
      "00560a68",
      "READ",
      [
        "storage",
        "00294a86",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00560a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005609d4.md#insn-00560a28) · [`00560a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005609d4.md#insn-00560a64) · [`00560b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005609d4.md#insn-00560b48)
- 新版 `00560a28`（命令位置の公開資料なし） · `00560a64`（命令位置の公開資料なし） · `00560b48`（命令位置の公開資料なし）

~~~diff
- 00560a28 ["COPY", "tmp:0:8", ["const:52d:8"]]
- 00560a28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00560a28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00560a28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560a28 ["COPY", "tmp:0:8", ["const:5ba:8"]]
+ 00560a28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560a28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560a28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00560a28 bytes 29b51491
+ 00560a28 bytes 29e91691
- 00560a64 ["COPY", "tmp:0:8", ["const:9b9:8"]]
- 00560a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00560a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00560a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560a64 ["COPY", "tmp:0:8", ["const:a46:8"]]
+ 00560a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00560a64 bytes 08e52691
+ 00560a64 bytes 08192991
- 00560b48 ["COPY", "tmp:0:8", ["const:910:8"]]
- 00560b48 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00560b48 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00560b48 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00560b48 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00560b48 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00560b48 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00560b48 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00560b48 bytes 39432491
+ 00560b48 bytes 39032791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49420b82de5de7271ce3fbdfa8fc2db1"></a>

### [`00560f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/00560f00.md) → [`00560f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560f00.md) FUN_00560f00

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005609d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/005612d4.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`005609d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/005612d4.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00561074",
      "incomplete_value": false,
      "site": "0056107c",
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
            "const:6e9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561074",
      "incomplete_value": false,
      "site": "0056107c",
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
            "const:65c:8"
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
      "definition_site": "005610d8",
      "incomplete_value": false,
      "site": "005610e0",
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
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005610d8",
      "incomplete_value": false,
      "site": "005610e0",
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
            "const:62b:8"
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
      "00561074",
      "PARAM",
      [
        "storage",
        "002a065c",
        null,
        "string"
      ]
    ],
    [
      "005610d8",
      "PARAM",
      [
        "storage",
        "0029c62b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00561074",
      "PARAM",
      [
        "storage",
        "002a06e9",
        null,
        "string"
      ]
    ],
    [
      "005610d8",
      "PARAM",
      [
        "storage",
        "0029c6b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/00560f00.md#insn-00561074) · [`005610d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/00560f00.md#insn-005610d8)
- 新版 `00561074`（命令位置の公開資料なし） · `005610d8`（命令位置の公開資料なし）

~~~diff
- 00561074 ["COPY", "tmp:0:8", ["const:65c:8"]]
- 00561074 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00561074 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00561074 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00561074 ["COPY", "tmp:0:8", ["const:6e9:8"]]
+ 00561074 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00561074 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00561074 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00561074 bytes 21701991
+ 00561074 bytes 21a41b91
- 005610d8 ["COPY", "tmp:0:8", ["const:62b:8"]]
- 005610d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005610d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005610d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005610d8 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 005610d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005610d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005610d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005610d8 bytes 21ac1891
+ 005610d8 bytes 21e01a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb926f124c44b99b0d8d80ff8882bd6f"></a>

### [`005612d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/005612d4.md) → [`005612d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/005612d4.md) FUN_005612d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005612cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/005612cc.md) · 呼出先 27件 [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00560f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/00560f00.md) [`00563938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563938.md) [`00563a9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563a9c.md) [`00564374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564374.md)
- 新版 呼出元 1件 [`005612cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/005612cc.md) · 呼出先 27件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00560f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560f00.md) [`00563938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563938.md) [`00563a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563a9c.md) [`00564374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564374.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.61% / 新版 97.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00561648",
      "incomplete_value": false,
      "site": "00561658",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561648",
      "incomplete_value": false,
      "site": "00561658",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00561338",
      "READ",
      [
        "storage",
        "0029d52d",
        null,
        "string"
      ]
    ],
    [
      "00561340",
      "READ",
      [
        "storage",
        "0029d533",
        null,
        "string"
      ]
    ],
    [
      "00561368",
      "READ",
      [
        "storage",
        "002949f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00561338",
      "READ",
      [
        "storage",
        "0029d5ba",
        null,
        "string"
      ]
    ],
    [
      "00561340",
      "READ",
      [
        "storage",
        "0029d5c0",
        null,
        "string"
      ]
    ],
    [
      "00561368",
      "READ",
      [
        "storage",
        "00294a86",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/005612d4.md#insn-00561334) · [`00561360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/005612d4.md#insn-00561360) · [`00561364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/005612d4.md#insn-00561364)
- 新版 `00561334`（命令位置の公開資料なし） · `00561360`（命令位置の公開資料なし）

~~~diff
- 00561334 ["COPY", "tmp:0:8", ["const:52d:8"]]
- 00561334 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00561334 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00561334 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00561334 ["COPY", "tmp:0:8", ["const:5ba:8"]]
+ 00561334 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00561334 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00561334 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00561334 bytes 29b51491
+ 00561334 bytes 29e91691
- 00561360 ["COPY", "tmp:0:8", ["const:9b9:8"]]
- 00561360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561360 ["COPY", "tmp:0:8", ["const:a46:8"]]
+ 00561360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561360 bytes 08e52691
+ 00561360 bytes 08192991
- 00561364 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00561364 bytes 89eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28ba9c74df96a537dd2afcdd7359fa46"></a>

### [`00561a60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/00561a60.md) → [`00561a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/00561a60.md) FUN_00561a60

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) [`005609d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005609d4.md) [`00564590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564590.md) [`005645f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/005645f0.md) [`00564974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564974.md)
- 新版 呼出元 0件  · 呼出先 14件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`005609d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609d4.md) [`00564590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564590.md) [`005645f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/005645f0.md) [`00564974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564974.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00561aa4",
      "incomplete_value": false,
      "site": "00561aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561aa4",
      "incomplete_value": false,
      "site": "00561aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "definition_site": "00561ad0",
      "incomplete_value": false,
      "site": "00561ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561ad0",
      "incomplete_value": false,
      "site": "00561ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00561b40",
      "incomplete_value": false,
      "site": "00561b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00561b40",
      "incomplete_value": false,
      "site": "00561b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "00561aac",
      "DATA",
      [
        "storage",
        "00bef998",
        null,
        "pointer"
      ]
    ],
    [
      "00561ad8",
      "DATA",
      [
        "storage",
        "00bef9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00561b40",
      "DATA",
      [
        "storage",
        "00befa30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00561aac",
      "DATA",
      [
        "storage",
        "00befa48",
        null,
        "pointer"
      ]
    ],
    [
      "00561ad8",
      "DATA",
      [
        "storage",
        "00befa98",
        null,
        "pointer"
      ]
    ],
    [
      "00561b40",
      "DATA",
      [
        "storage",
        "00befae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00561aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/00561a60.md#insn-00561aa4) · [`00561ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/00561a60.md#insn-00561ad0) · [`00561b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/00561a60.md#insn-00561b38)
- 新版 `00561aa4`（命令位置の公開資料なし） · `00561ad0`（命令位置の公開資料なし） · `00561b38`（命令位置の公開資料なし）

~~~diff
- 00561aa4 ["COPY", "tmp:0:8", ["const:998:8"]]
- 00561aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561aa4 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 00561aa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561aa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561aa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561aa4 bytes 08612691
+ 00561aa4 bytes 08212991
- 00561ad0 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00561ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561ad0 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 00561ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561ad0 bytes 08a12791
+ 00561ad0 bytes 08612a91
- 00561b38 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 00561b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00561b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00561b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561b38 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 00561b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00561b38 bytes 08c12891
+ 00561b38 bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc298ec161ea96474a3221efd1b002cf"></a>

### [`005624f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005624f4.md) → [`005624f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005624f4.md) FUN_005624f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005627f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005627f4.md) [`005636f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/005636f4.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00471738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471738.md) [`0056503c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056503c.md) [`0056508c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056508c.md) [`0056521c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056521c.md)
- 新版 呼出元 2件 [`005627f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005627f4.md) [`005636f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/005636f4.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00471738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471738.md) [`0056503c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056503c.md) [`0056508c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056508c.md) [`0056521c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056521c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00562720",
      "incomplete_value": true,
      "site": "00562720",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00562720",
      "incomplete_value": true,
      "site": "00562720",
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
    "ordinal": 19,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00562524",
      "incomplete_value": true,
      "site": "00562524",
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
      "definition_site": "00562524",
      "incomplete_value": true,
      "site": "00562524",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "005625b4",
      "incomplete_value": true,
      "site": "005625b4",
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
      "definition_site": "005625b4",
      "incomplete_value": true,
      "site": "005625b4",
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
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00562520",
      "READ",
      [
        "storage",
        "00c26380",
        null,
        "undefined8"
      ]
    ],
    [
      "00562568",
      "READ",
      [
        "storage",
        "00c26430",
        null,
        "undefined8"
      ]
    ],
    [
      "0056258c",
      "PARAM",
      [
        "storage",
        "00c26378",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00562520",
      "READ",
      [
        "storage",
        "00c26440",
        null,
        "undefined8"
      ]
    ],
    [
      "00562568",
      "READ",
      [
        "storage",
        "00c264f0",
        null,
        "undefined8"
      ]
    ],
    [
      "0056258c",
      "PARAM",
      [
        "storage",
        "00c26438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00562720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005624f4.md#insn-00562720) · [`0056251c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005624f4.md#insn-0056251c) · [`0056252c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005624f4.md#insn-0056252c)
- 新版 `00562720`（命令位置の公開資料なし） · `0056251c`（命令位置の公開資料なし） · `0056252c`（命令位置の公開資料なし）

~~~diff
- 00562720 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:360:8"]]
- 00562720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00562720 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:420:8"]]
+ 00562720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00562720 bytes 28b101f9
+ 00562720 bytes 281102f9
- 0056251c ["COPY", "tmp:0:8", ["const:380:8"]]
- 0056251c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056251c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056251c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056251c ["COPY", "tmp:0:8", ["const:440:8"]]
+ 0056251c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056251c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056251c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056251c bytes 08010e91
+ 0056251c bytes 08011191
- 0056252c ["COPY", "tmp:0:8", ["const:380:8"]]
- 0056252c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0056252c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0056252c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0056252c ["COPY", "tmp:0:8", ["const:440:8"]]
+ 0056252c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0056252c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0056252c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0056252c bytes 73020e91
+ 0056252c bytes 73021191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d2eae9380728eef84584491649ad027"></a>

### [`005627f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005627f4.md) → [`005627f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005627f4.md) Java_jp_co_ponos_battlecats_MyActivity_newResponse

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00471738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471738.md) [`0055b1b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b1b8.md) [`0055ef38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055ef38.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00471738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471738.md) [`0055b1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b1b8.md) [`0055ef38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ef38.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 3件, `store_condition` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00562950",
      "incomplete_value": false,
      "site": "0056295c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00562950",
      "incomplete_value": false,
      "site": "0056295c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:450:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00562cf0",
      "incomplete_value": true,
      "site": "00562cf0",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00562cf0",
      "incomplete_value": true,
      "site": "00562cf0",
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
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056283c",
      "incomplete_value": true,
      "site": "0056283c",
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
      "definition_site": "0056283c",
      "incomplete_value": true,
      "site": "0056283c",
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
      "00562834",
      "READ",
      [
        "storage",
        "00c26368",
        null,
        "undefined8"
      ]
    ],
    [
      "00562880",
      "READ",
      [
        "storage",
        "00c263b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0056295c",
      "DATA",
      [
        "storage",
        "00bef450",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00562834",
      "READ",
      [
        "storage",
        "00c26428",
        null,
        "undefined8"
      ]
    ],
    [
      "00562880",
      "READ",
      [
        "storage",
        "00c26478",
        null,
        "undefined8"
      ]
    ],
    [
      "0056295c",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00562cf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005627f4.md#insn-00562cf0) · [`00562818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005627f4.md#insn-00562818) · [`00562844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005627f4.md#insn-00562844)
- 新版 `00562cf0`（命令位置の公開資料なし） · `00562818`（命令位置の公開資料なし） · `00562844`（命令位置の公開資料なし）

~~~diff
- 00562cf0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:360:8"]]
- 00562cf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00562cf0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:420:8"]]
+ 00562cf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00562cf0 bytes 28b101f9
+ 00562cf0 bytes 281102f9
- 00562818 ["COPY", "tmp:0:8", ["const:368:8"]]
- 00562818 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 00562818 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 00562818 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 00562818 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 00562818 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 00562818 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 00562818 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 00562818 bytes 5aa30d91
+ 00562818 bytes 5aa31091
- 00562844 ["COPY", "tmp:0:8", ["const:368:8"]]
- 00562844 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00562844 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00562844 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00562844 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 00562844 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00562844 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00562844 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00562844 bytes 73a20d91
+ 00562844 bytes 73a21091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba7a8da118b41a41581aefcdb1848db5"></a>

### [`00563038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563038.md) → [`00563038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563038.md) Java_jp_co_ponos_battlecats_MyActivity_onResponseCodeHeaders

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00562e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/00562e78.md) [`0056547c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056547c.md) [`00566a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566a7c.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00562e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/00562e78.md) [`0056547c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056547c.md) [`00566a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566a7c.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056306c",
      "incomplete_value": true,
      "site": "0056306c",
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
      "definition_site": "0056306c",
      "incomplete_value": true,
      "site": "0056306c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00563184",
      "incomplete_value": true,
      "site": "00563184",
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
      "definition_site": "00563184",
      "incomplete_value": true,
      "site": "00563184",
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
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00563184"
      ],
      [
        "FALL_THROUGH",
        "00563184"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00563184",
      "incomplete_value": true,
      "site": "005631a4",
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
      "definition_site": "00563184",
      "incomplete_value": true,
      "site": "005631a4",
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
      "00563064",
      "READ",
      [
        "storage",
        "00c26380",
        null,
        "undefined8"
      ]
    ],
    [
      "005630c0",
      "READ",
      [
        "storage",
        "00c263d0",
        null,
        "undefined4"
      ]
    ],
    [
      "0056317c",
      "READ",
      [
        "storage",
        "00c26320",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00563064",
      "READ",
      [
        "storage",
        "00c26440",
        null,
        "undefined8"
      ]
    ],
    [
      "005630c0",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined4"
      ]
    ],
    [
      "0056317c",
      "READ",
      [
        "storage",
        "00c263e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563038.md#insn-00563060) · [`00563074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563038.md#insn-00563074) · [`0056317c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563038.md#insn-0056317c)
- 新版 `00563060`（命令位置の公開資料なし） · `00563074`（命令位置の公開資料なし） · `0056317c`（命令位置の公開資料なし）

~~~diff
- 00563060 ["COPY", "tmp:0:8", ["const:380:8"]]
- 00563060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563060 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00563060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563060 bytes 08010e91
+ 00563060 bytes 08011191
- 00563074 ["COPY", "tmp:0:8", ["const:380:8"]]
- 00563074 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00563074 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00563074 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00563074 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00563074 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00563074 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00563074 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00563074 bytes d6020e91
+ 00563074 bytes d6021191
- 0056317c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
- 0056317c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056317c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3e0:8"]]
+ 0056317c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0056317c bytes 009141f9
+ 0056317c bytes 00f141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6e9361beeec52d8b947969e2c92b08d"></a>

### [`0056340c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/0056340c.md) → [`0056340c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/0056340c.md) Java_jp_co_ponos_battlecats_MyActivity_onResponseData

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0055b1b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b1b8.md) [`0055ef38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055ef38.md) [`00566d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566d10.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0055b1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b1b8.md) [`0055ef38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055ef38.md) [`00566d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566d10.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056343c",
      "incomplete_value": true,
      "site": "0056343c",
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
      "definition_site": "0056343c",
      "incomplete_value": true,
      "site": "0056343c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0056357c",
      "incomplete_value": true,
      "site": "0056357c",
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
      "definition_site": "0056357c",
      "incomplete_value": true,
      "site": "0056357c",
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
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "0056357c"
      ],
      [
        "FALL_THROUGH",
        "0056357c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0056357c",
      "incomplete_value": true,
      "site": "0056359c",
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
      "definition_site": "0056357c",
      "incomplete_value": true,
      "site": "0056359c",
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
    "ordinal": 17,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00563438",
      "READ",
      [
        "storage",
        "00c26380",
        null,
        "undefined8"
      ]
    ],
    [
      "00563490",
      "READ",
      [
        "storage",
        "00c26400",
        null,
        "undefined8"
      ]
    ],
    [
      "005634c0",
      "DATA",
      [
        "storage",
        "00bef450",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00563438",
      "READ",
      [
        "storage",
        "00c26440",
        null,
        "undefined8"
      ]
    ],
    [
      "00563490",
      "READ",
      [
        "storage",
        "00c264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "005634c0",
      "DATA",
      [
        "storage",
        "00bef500",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/0056340c.md#insn-00563434) · [`00563444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/0056340c.md#insn-00563444) · [`005634b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/0056340c.md#insn-005634b4)
- 新版 `00563434`（命令位置の公開資料なし） · `00563444`（命令位置の公開資料なし） · `005634b4`（命令位置の公開資料なし）

~~~diff
- 00563434 ["COPY", "tmp:0:8", ["const:380:8"]]
- 00563434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563434 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00563434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563434 bytes 08010e91
+ 00563434 bytes 08011191
- 00563444 ["COPY", "tmp:0:8", ["const:380:8"]]
- 00563444 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 00563444 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 00563444 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 00563444 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00563444 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 00563444 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 00563444 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 00563444 bytes 18030e91
+ 00563444 bytes 18031191
- 005634b4 ["COPY", "tmp:0:8", ["const:450:8"]]
- 005634b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005634b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005634b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005634b4 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 005634b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005634b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005634b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005634b4 bytes 08411191
+ 005634b4 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c063f35f9afa1f43b0146d3ec9038aa"></a>

### [`00563704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563704.md) → [`00563704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563704.md) FUN_00563704

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00563804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563804.md) · 呼出先 4件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00563804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563804.md) · 呼出先 4件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00563720",
      "incomplete_value": false,
      "site": "00563724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563720",
      "incomplete_value": false,
      "site": "00563724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "00563724",
      "DATA",
      [
        "storage",
        "00bef828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563724",
      "DATA",
      [
        "storage",
        "00bef8d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563704.md#insn-00563720)
- 新版 `00563720`（命令位置の公開資料なし）

~~~diff
- 00563720 ["COPY", "tmp:0:8", ["const:828:8"]]
- 00563720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00563720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00563720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00563720 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00563720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00563720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00563720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00563720 bytes 08a12091
+ 00563720 bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1bbcefbf961b033e8c891a921759e31"></a>

### [`00563828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563828.md) → [`00563828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563828.md) FUN_00563828

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00563840",
      "incomplete_value": false,
      "site": "00563844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00563840",
      "incomplete_value": false,
      "site": "00563844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:808:8"
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
      "00563844",
      "DATA",
      [
        "storage",
        "00bef808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00563844",
      "DATA",
      [
        "storage",
        "00bef8b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00563840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563828.md#insn-00563840)
- 新版 `00563840`（命令位置の公開資料なし）

~~~diff
- 00563840 ["COPY", "tmp:0:8", ["const:808:8"]]
- 00563840 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00563840 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00563840 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00563840 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 00563840 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00563840 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00563840 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00563840 bytes 29212091
+ 00563840 bytes 29e12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dde9f53041298a9872d057e75bc15f0f"></a>

### [`005638b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/005638b0.md) → [`005638b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/005638b0.md) FUN_005638b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005638c8",
      "incomplete_value": false,
      "site": "005638cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005638c8",
      "incomplete_value": false,
      "site": "005638cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:808:8"
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
      "005638cc",
      "DATA",
      [
        "storage",
        "00bef808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005638cc",
      "DATA",
      [
        "storage",
        "00bef8b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005638c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/005638b0.md#insn-005638c8)
- 新版 `005638c8`（命令位置の公開資料なし）

~~~diff
- 005638c8 ["COPY", "tmp:0:8", ["const:808:8"]]
- 005638c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005638c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005638c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005638c8 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 005638c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005638c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005638c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005638c8 bytes 29212091
+ 005638c8 bytes 29e12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-708f69017ae1fc491f3468ac649adad4"></a>

### [`00564200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564200.md) → [`00564200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564200.md) FUN_00564200

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
      "definition_site": "00564204",
      "incomplete_value": false,
      "site": "00564208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564204",
      "incomplete_value": false,
      "site": "00564208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:948:8"
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
      "00564208",
      "DATA",
      [
        "storage",
        "00bef948",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564208",
      "DATA",
      [
        "storage",
        "00bef9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564200.md#insn-00564204)
- 新版 `00564204`（命令位置の公開資料なし）

~~~diff
- 00564204 ["COPY", "tmp:0:8", ["const:948:8"]]
- 00564204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564204 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00564204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564204 bytes 08212591
+ 00564204 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa046be0220e376b2b92fb1dc69aa50a"></a>

### [`00564550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564550.md) → [`00564550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564550.md) FUN_00564550

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
      "definition_site": "00564554",
      "incomplete_value": false,
      "site": "00564558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564554",
      "incomplete_value": false,
      "site": "00564558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "00564558",
      "DATA",
      [
        "storage",
        "00bef998",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00564558",
      "DATA",
      [
        "storage",
        "00befa48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564550.md#insn-00564554)
- 新版 `00564554`（命令位置の公開資料なし）

~~~diff
- 00564554 ["COPY", "tmp:0:8", ["const:998:8"]]
- 00564554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564554 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 00564554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564554 bytes 08612691
+ 00564554 bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18040cac8e917f1bee2826c476d24fbb"></a>

### [`00564560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564560.md) → [`00564560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564560.md) FUN_00564560

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
      "definition_site": "00564570",
      "incomplete_value": false,
      "site": "00564578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564570",
      "incomplete_value": false,
      "site": "00564578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "00564578",
      "DATA",
      [
        "storage",
        "00bef998",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00564578",
      "DATA",
      [
        "storage",
        "00befa48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564560.md#insn-00564570)
- 新版 `00564570`（命令位置の公開資料なし）

~~~diff
- 00564570 ["COPY", "tmp:0:8", ["const:998:8"]]
- 00564570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564570 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 00564570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564570 bytes 08612691
+ 00564570 bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e7f807257eab39f14ce26811294772b"></a>

### [`0056459c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/0056459c.md) → [`0056459c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/0056459c.md) FUN_0056459c

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
      "definition_site": "005645c0",
      "incomplete_value": true,
      "site": "005645c0",
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
      "definition_site": "005645c0",
      "incomplete_value": true,
      "site": "005645c0",
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
      "005645b4",
      "READ",
      [
        "storage",
        "00c1ad60",
        null,
        "pointer"
      ]
    ],
    [
      "005645c0",
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
      "005645b4",
      "READ",
      [
        "storage",
        "00c1ae10",
        null,
        "pointer"
      ]
    ],
    [
      "005645c0",
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

- 旧版 [`005645b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/0056459c.md#insn-005645b4)
- 新版 `005645b4`（命令位置の公開資料なし）

~~~diff
- 005645b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d60:8"]]
- 005645b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005645b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 005645b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005645b4 bytes 08b146f9
+ 005645b4 bytes 080947f9
~~~


<a id="compare-1d855e96c8ef4a540874bd1e5cc79866"></a>

### [`00564710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564710.md) → [`00564710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564710.md) FUN_00564710

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00564590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564590.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377f0.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md)
- 新版 呼出元 1件 [`00564590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564590.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377f0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)

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
      "definition_site": "005647b4",
      "incomplete_value": true,
      "site": "005647b8",
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
      "definition_site": "005647b4",
      "incomplete_value": true,
      "site": "005647b8",
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
      "definition_site": "00564790",
      "incomplete_value": true,
      "site": "00564798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00564790",
      "incomplete_value": true,
      "site": "00564798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d68:8"
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
      "00564790",
      "READ",
      [
        "storage",
        "00c1ad68",
        null,
        "pointer"
      ]
    ],
    [
      "00564790",
      "PARAM",
      [
        "storage",
        "00c12e08",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005647b0",
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
      "00564790",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "00564790",
      "PARAM",
      [
        "storage",
        "00c12eb8",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005647b0",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564710.md#insn-00564790) · [`005647b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564710.md#insn-005647b0)
- 新版 `00564790`（命令位置の公開資料なし） · `005647b0`（命令位置の公開資料なし）

~~~diff
- 00564790 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d68:8"]]
- 00564790 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00564790 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
+ 00564790 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00564790 bytes 21b446f9
+ 00564790 bytes 210c47f9
- 005647b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 005647b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005647b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e20:8"]]
+ 005647b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005647b0 bytes 08b946f9
+ 005647b0 bytes 081147f9
~~~


<a id="compare-dd44515193e8a936b4d2a40ba4612a53"></a>

### [`00564838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564838.md) → [`00564838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564838.md) FUN_00564838

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "0056484c",
      "incomplete_value": false,
      "site": "00564850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056484c",
      "incomplete_value": false,
      "site": "00564850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "00564850",
      "DATA",
      [
        "storage",
        "00befa30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564850",
      "DATA",
      [
        "storage",
        "00befae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056484c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564838.md#insn-0056484c)
- 新版 `0056484c`（命令位置の公開資料なし）

~~~diff
- 0056484c ["COPY", "tmp:0:8", ["const:a30:8"]]
- 0056484c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056484c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056484c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056484c ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0056484c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056484c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056484c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056484c bytes 08c12891
+ 0056484c bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f25512d7fd8e927d984d7ad86cdc5ff7"></a>

### [`00564894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564894.md) → [`00564894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564894.md) FUN_00564894

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "005648ac",
      "incomplete_value": false,
      "site": "005648b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005648ac",
      "incomplete_value": false,
      "site": "005648b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "005648b0",
      "DATA",
      [
        "storage",
        "00befa30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005648b0",
      "DATA",
      [
        "storage",
        "00befae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005648ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564894.md#insn-005648ac)
- 新版 `005648ac`（命令位置の公開資料なし）

~~~diff
- 005648ac ["COPY", "tmp:0:8", ["const:a30:8"]]
- 005648ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005648ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005648ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005648ac ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005648ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005648ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005648ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005648ac bytes 08c12891
+ 005648ac bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-756b2ad45e0cc6818adeeda2caea6583"></a>

### [`005648f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/005648f0.md) → [`005648f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/005648f0.md) FUN_005648f0

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
      "definition_site": "00564914",
      "incomplete_value": false,
      "site": "00564914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564914",
      "incomplete_value": false,
      "site": "00564914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bef000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "00564914",
      "DATA",
      [
        "storage",
        "00befa30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564914",
      "DATA",
      [
        "storage",
        "00befae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/005648f0.md#insn-00564910)
- 新版 `00564910`（命令位置の公開資料なし）

~~~diff
- 00564910 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 00564910 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00564910 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00564910 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00564910 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 00564910 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00564910 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00564910 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00564910 bytes 29c12891
+ 00564910 bytes 29812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

