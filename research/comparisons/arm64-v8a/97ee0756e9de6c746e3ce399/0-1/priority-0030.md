# v15.7.2 → v15.7.3 · 最優先の変更候補 (30)

[一覧の目次](README.md)

<a id="compare-49ea28f5489b7b49271151c32b6e9b57"></a>

### [`006aad48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006aa/006aad48.md) → [`006aad48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006aa/006aad48.md) FUN_006aad48

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008c2a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008c2/008c2a7c.md) [`00957f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) [`00a7888c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a78/00a7888c.md) · 呼出先 44件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md)
- 新版 呼出元 3件 [`008c2a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) · 呼出先 44件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ab7d8",
      "incomplete_value": true,
      "site": "006ab7d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ab7d8",
      "incomplete_value": true,
      "site": "006ab7d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 66,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ab7dc",
      "incomplete_value": true,
      "site": "006ab7dc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006ab7dc",
      "incomplete_value": true,
      "site": "006ab7dc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 67,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006ab95c",
      "incomplete_value": false,
      "site": "006ab964",
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
    "old": {
      "definition_site": "006ab95c",
      "incomplete_value": false,
      "site": "006ab964",
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
            "const:4eb:8"
          ]
        ]
      ]
    },
    "ordinal": 149,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ab7c8",
      "READ",
      [
        "storage",
        "002a6a79",
        null,
        "string"
      ]
    ],
    [
      "006ab7cc",
      "READ",
      [
        "storage",
        "002a6a7e",
        null,
        "string"
      ]
    ],
    [
      "006ab904",
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
      "006ab7c8",
      "READ",
      [
        "storage",
        "002a6a72",
        null,
        "string"
      ]
    ],
    [
      "006ab7cc",
      "READ",
      [
        "storage",
        "002a6a77",
        null,
        "string"
      ]
    ],
    [
      "006ab904",
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

- 旧版 [`006ab7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006aa/006aad48.md#insn-006ab7c0) · [`006ab8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006aa/006aad48.md#insn-006ab8a8) · [`006ab95c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006aa/006aad48.md#insn-006ab95c)
- 新版 [`006ab7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006aa/006aad48.md#insn-006ab7c0) · [`006ab8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006aa/006aad48.md#insn-006ab8a8) · [`006ab95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006aa/006aad48.md#insn-006ab95c)

~~~diff
- 006ab7c0 ["COPY", "tmp:0:8", ["const:a79:8"]]
- 006ab7c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ab7c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ab7c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006ab7c0 ["COPY", "tmp:0:8", ["const:a72:8"]]
+ 006ab7c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006ab7c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006ab7c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ab7c0 bytes 29e52991
+ 006ab7c0 bytes 29c92991
- 006ab8a8 ["COPY", "tmp:0:8", ["const:855:8"]]
- 006ab8a8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 006ab8a8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 006ab8a8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 006ab8a8 ["COPY", "tmp:0:8", ["const:85b:8"]]
+ 006ab8a8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 006ab8a8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 006ab8a8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 006ab8a8 bytes 94562191
+ 006ab8a8 bytes 946e2191
- 006ab95c ["COPY", "tmp:0:8", ["const:4eb:8"]]
- 006ab95c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006ab95c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006ab95c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006ab95c ["COPY", "tmp:0:8", ["const:457:8"]]
+ 006ab95c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006ab95c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006ab95c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006ab95c bytes 21ac1391
+ 006ab95c bytes 215c1191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc6f560e6858fb48d71cf321b738b94e"></a>

### [`006ad28c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad28c.md) → [`006ad28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad28c.md) FUN_006ad28c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006a6d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006a6/006a6d68.md) · 呼出先 10件 [`006ad590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad590.md) [`006ad854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad854.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`006ad8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8e8.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md)
- 新版 呼出元 1件 [`006a6d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a6/006a6d68.md) · 呼出先 10件 [`006ad590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad590.md) [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`006ad8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8e8.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.48% / 新版 99.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006ad54c",
      "incomplete_value": false,
      "site": "006ad550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:23:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ad54c",
      "incomplete_value": false,
      "site": "006ad550",
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
            "const:f96:8"
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
      "006ad54c",
      "PARAM",
      [
        "storage",
        "00299f96",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006ad54c",
      "PARAM",
      [
        "storage",
        "0029a023",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ad548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad28c.md#insn-006ad548) · [`006ad54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad28c.md#insn-006ad54c)
- 新版 [`006ad548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad28c.md#insn-006ad548) · [`006ad54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad28c.md#insn-006ad54c)

~~~diff
- 006ad548 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 006ad548 ["COPY", "register:4000:8", ["const:29a000:8"]]
- 006ad548 bytes 60dfff90
+ 006ad548 bytes 60dfffb0
- 006ad54c ["COPY", "tmp:0:8", ["const:f96:8"]]
- 006ad54c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006ad54c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006ad54c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006ad54c ["COPY", "tmp:0:8", ["const:23:8"]]
+ 006ad54c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006ad54c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006ad54c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006ad54c bytes 00583e91
+ 006ad54c bytes 008c0091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80f8bd2dce25b90e4aedd04df35a812d"></a>

### [`006ad854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad854.md) → [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) FUN_006ad854

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`006ad28c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad28c.md) [`006ad980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad980.md) [`007c1c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1c70.md) [`007c1f74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1f74.md) · 呼出先 4件 [`006ad8b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8b8.md) [`00bbade0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbade0.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 4件 [`006ad28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad28c.md) [`006ad980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad980.md) [`007c1c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1c70.md) [`007c1f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1f74.md) · 呼出先 4件 [`006ad8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8b8.md) [`00bbaea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

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
      "definition_site": "006ad884",
      "incomplete_value": true,
      "site": "006ad88c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:700:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ad884",
      "incomplete_value": true,
      "site": "006ad88c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:650:8"
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
      "definition_site": "006ad888",
      "incomplete_value": true,
      "site": "006ad88c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:708:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ad888",
      "incomplete_value": true,
      "site": "006ad88c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:658:8"
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
      "006ad884",
      "READ",
      [
        "storage",
        "00c1b650",
        null,
        "pointer"
      ]
    ],
    [
      "006ad884",
      "PARAM",
      [
        "storage",
        "00c169c8",
        "_ZTISt11range_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006ad888",
      "READ",
      [
        "storage",
        "00c1b658",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006ad884",
      "READ",
      [
        "storage",
        "00c1b700",
        null,
        "pointer"
      ]
    ],
    [
      "006ad884",
      "PARAM",
      [
        "storage",
        "00c16a78",
        "_ZTISt11range_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006ad888",
      "READ",
      [
        "storage",
        "00c1b708",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ad884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad854.md#insn-006ad884) · [`006ad888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad854.md#insn-006ad888)
- 新版 [`006ad884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md#insn-006ad884) · [`006ad888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md#insn-006ad888)

~~~diff
- 006ad884 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:650:8"]]
- 006ad884 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 006ad884 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:700:8"]]
+ 006ad884 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 006ad884 bytes 212843f9
+ 006ad884 bytes 218043f9
- 006ad888 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:658:8"]]
- 006ad888 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 006ad888 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:708:8"]]
+ 006ad888 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 006ad888 bytes 422c43f9
+ 006ad888 bytes 428443f9
~~~


<a id="compare-a0c41b5a5cd723de673532c5054f58ed"></a>

### [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) → [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) FUN_006ad8a4

採用 · 移動量 `+0x0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 25件 [`006a6d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006a6/006a6d68.md) [`006ad28c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad28c.md) [`006ad590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad590.md) [`006ad8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8e8.md) [`007c1c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c1/007c1c70.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 25件 [`006a6d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a6/006a6d68.md) [`006ad28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad28c.md) [`006ad590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad590.md) [`006ad8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8e8.md) [`007c1c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c1/007c1c70.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "006ad8b0",
      "incomplete_value": false,
      "site": "006ad8b4",
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
      "definition_site": "006ad8b0",
      "incomplete_value": false,
      "site": "006ad8b4",
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
      "006ad8b0",
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
      "006ad8b0",
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

- 旧版 [`006ad8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md#insn-006ad8b0)
- 新版 [`006ad8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md#insn-006ad8b0)

~~~diff
- 006ad8b0 ["COPY", "tmp:0:8", ["const:246:8"]]
- 006ad8b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006ad8b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006ad8b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006ad8b0 ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 006ad8b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006ad8b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006ad8b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006ad8b0 bytes 00180991
+ 006ad8b0 bytes 00c80691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-217c21d8319e888f54c97b4dcfd9ce5d"></a>

### [`006ad8b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8b8.md) → [`006ad8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8b8.md) FUN_006ad8b8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006ad854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad854.md) · 呼出先 1件 [`00bdd980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd980.md)
- 新版 呼出元 1件 [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) · 呼出先 1件 [`00bdda30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda30.md)

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
      "definition_site": "006ad8d4",
      "incomplete_value": true,
      "site": "006ad8d8",
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
      "definition_site": "006ad8d4",
      "incomplete_value": true,
      "site": "006ad8d8",
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
      "006ad8d0",
      "READ",
      [
        "storage",
        "00c1b660",
        null,
        "pointer"
      ]
    ],
    [
      "006ad8d8",
      "DATA",
      [
        "storage",
        "00c16998",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "006ad8d0",
      "READ",
      [
        "storage",
        "00c1b710",
        null,
        "pointer"
      ]
    ],
    [
      "006ad8d8",
      "DATA",
      [
        "storage",
        "00c16a48",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ad8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8b8.md#insn-006ad8d0)
- 新版 [`006ad8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8b8.md#insn-006ad8d0)

~~~diff
- 006ad8d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:660:8"]]
- 006ad8d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006ad8d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:710:8"]]
+ 006ad8d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006ad8d0 bytes 083143f9
+ 006ad8d0 bytes 088943f9
~~~


<a id="compare-09d6d4dcf0714771ae9356676551be7b"></a>

### [`006ad980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad980.md) → [`006ad980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad980.md) FUN_006ad980

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006a6d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006a6/006a6d68.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`006ad854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad854.md) [`006add94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006add94.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`006a6d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a6/006a6d68.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) [`006add94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006add94.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.59% / 新版 99.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006add28",
      "incomplete_value": false,
      "site": "006add2c",
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
            "const:f2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006add28",
      "incomplete_value": false,
      "site": "006add2c",
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
            "const:ea2:8"
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
      "006add28",
      "PARAM",
      [
        "storage",
        "00297ea2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006add28",
      "PARAM",
      [
        "storage",
        "00297f2f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006add28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad980.md#insn-006add28)
- 新版 [`006add28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad980.md#insn-006add28)

~~~diff
- 006add28 ["COPY", "tmp:0:8", ["const:ea2:8"]]
- 006add28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006add28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006add28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006add28 ["COPY", "tmp:0:8", ["const:f2f:8"]]
+ 006add28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006add28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006add28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006add28 bytes 00883a91
+ 006add28 bytes 00bc3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daae220bc3ececd66f7e0466a49255b8"></a>

### [`006ae060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae060.md) → [`006ae060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae060.md) FUN_006ae060

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
      "definition_site": "006ae06c",
      "incomplete_value": false,
      "site": "006ae06c",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae06c",
      "incomplete_value": false,
      "site": "006ae06c",
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
            "const:cf0:8"
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
      "006ae06c",
      "DATA",
      [
        "storage",
        "00bf8cf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae06c",
      "DATA",
      [
        "storage",
        "00bf8da0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae060.md#insn-006ae068)
- 新版 [`006ae068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae060.md#insn-006ae068)

~~~diff
- 006ae068 ["COPY", "tmp:0:8", ["const:cf0:8"]]
- 006ae068 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ae068 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ae068 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006ae068 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 006ae068 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae068 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae068 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ae068 bytes 29c13391
+ 006ae068 bytes 29813691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7e6adf12aad2bde2211313e8a304a18"></a>

### [`006ae40c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae40c.md) → [`006ae40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae40c.md) FUN_006ae40c

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
      "definition_site": "006ae430",
      "incomplete_value": false,
      "site": "006ae430",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae430",
      "incomplete_value": false,
      "site": "006ae430",
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
            "const:d70:8"
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
      "006ae430",
      "DATA",
      [
        "storage",
        "00bf8d70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae430",
      "DATA",
      [
        "storage",
        "00bf8e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae42c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae40c.md#insn-006ae42c)
- 新版 [`006ae42c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae40c.md#insn-006ae42c)

~~~diff
- 006ae42c ["COPY", "tmp:0:8", ["const:d70:8"]]
- 006ae42c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ae42c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ae42c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ae42c ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 006ae42c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ae42c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ae42c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ae42c bytes 08c13591
+ 006ae42c bytes 08813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15b0677c21af51c15a5b931d42a904b1"></a>

### [`006ae440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae440.md) → [`006ae440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae440.md) FUN_006ae440

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
      "definition_site": "006ae44c",
      "incomplete_value": false,
      "site": "006ae44c",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae44c",
      "incomplete_value": false,
      "site": "006ae44c",
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
            "const:d70:8"
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
      "006ae44c",
      "DATA",
      [
        "storage",
        "00bf8d70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae44c",
      "DATA",
      [
        "storage",
        "00bf8e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae440.md#insn-006ae448)
- 新版 [`006ae448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae440.md#insn-006ae448)

~~~diff
- 006ae448 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 006ae448 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ae448 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ae448 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006ae448 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 006ae448 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae448 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae448 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ae448 bytes 29c13591
+ 006ae448 bytes 29813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b78aa32cfbf6a62fae190bf4703043b"></a>

### [`006ae59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae59c.md) → [`006ae59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae59c.md) FUN_006ae59c

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
      "definition_site": "006ae5c0",
      "incomplete_value": false,
      "site": "006ae5c0",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae5c0",
      "incomplete_value": false,
      "site": "006ae5c0",
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
            "const:df0:8"
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
      "006ae5c0",
      "DATA",
      [
        "storage",
        "00bf8df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae5c0",
      "DATA",
      [
        "storage",
        "00bf8ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae59c.md#insn-006ae5bc)
- 新版 [`006ae5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae59c.md#insn-006ae5bc)

~~~diff
- 006ae5bc ["COPY", "tmp:0:8", ["const:df0:8"]]
- 006ae5bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ae5bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ae5bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ae5bc ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 006ae5bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ae5bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ae5bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ae5bc bytes 08c13791
+ 006ae5bc bytes 08813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93bcc7869241528cd0a789b4a1dabfdd"></a>

### [`006ae5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae5d0.md) → [`006ae5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae5d0.md) FUN_006ae5d0

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
      "definition_site": "006ae5dc",
      "incomplete_value": false,
      "site": "006ae5dc",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae5dc",
      "incomplete_value": false,
      "site": "006ae5dc",
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
            "const:df0:8"
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
      "006ae5dc",
      "DATA",
      [
        "storage",
        "00bf8df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae5dc",
      "DATA",
      [
        "storage",
        "00bf8ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae5d0.md#insn-006ae5d8)
- 新版 [`006ae5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae5d0.md#insn-006ae5d8)

~~~diff
- 006ae5d8 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 006ae5d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ae5d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ae5d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006ae5d8 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 006ae5d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae5d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae5d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ae5d8 bytes 29c13791
+ 006ae5d8 bytes 29813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-650802f6afd8a41db98b1293498e54b7"></a>

### [`006ae91c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae91c.md) → [`006ae91c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae91c.md) FUN_006ae91c

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
      "definition_site": "006ae940",
      "incomplete_value": false,
      "site": "006ae940",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae940",
      "incomplete_value": false,
      "site": "006ae940",
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
            "const:e70:8"
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
      "006ae940",
      "DATA",
      [
        "storage",
        "00bf8e70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae940",
      "DATA",
      [
        "storage",
        "00bf8f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae93c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae91c.md#insn-006ae93c)
- 新版 [`006ae93c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae91c.md#insn-006ae93c)

~~~diff
- 006ae93c ["COPY", "tmp:0:8", ["const:e70:8"]]
- 006ae93c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ae93c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ae93c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ae93c ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 006ae93c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ae93c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ae93c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ae93c bytes 08c13991
+ 006ae93c bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92ec63be168b5bcd7d7275d2ccd35437"></a>

### [`006ae950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae950.md) → [`006ae950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae950.md) FUN_006ae950

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
      "definition_site": "006ae95c",
      "incomplete_value": false,
      "site": "006ae95c",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae95c",
      "incomplete_value": false,
      "site": "006ae95c",
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
            "const:e70:8"
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
      "006ae95c",
      "DATA",
      [
        "storage",
        "00bf8e70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ae95c",
      "DATA",
      [
        "storage",
        "00bf8f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006ae950.md#insn-006ae958)
- 新版 [`006ae958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae950.md#insn-006ae958)

~~~diff
- 006ae958 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 006ae958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ae958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ae958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006ae958 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 006ae958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006ae958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ae958 bytes 29c13991
+ 006ae958 bytes 29813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7c27c04f7a8fe0c31956f42d5df13cc"></a>

### [`006aeeb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006aeeb4.md) → [`006aeeb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006aeeb4.md) FUN_006aeeb4

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
      "definition_site": "006aeed8",
      "incomplete_value": false,
      "site": "006aeed8",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006aeed8",
      "incomplete_value": false,
      "site": "006aeed8",
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
            "const:ef0:8"
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
      "006aeed8",
      "DATA",
      [
        "storage",
        "00bf8ef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006aeed8",
      "DATA",
      [
        "storage",
        "00bf8fa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006aeed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006aeeb4.md#insn-006aeed4)
- 新版 [`006aeed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006aeeb4.md#insn-006aeed4)

~~~diff
- 006aeed4 ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 006aeed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006aeed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006aeed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006aeed4 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 006aeed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006aeed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006aeed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006aeed4 bytes 08c13b91
+ 006aeed4 bytes 08813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c922c68c35706cc5f7724726063ca3b"></a>

### [`006aeee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006aeee8.md) → [`006aeee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006aeee8.md) FUN_006aeee8

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
      "definition_site": "006aeef4",
      "incomplete_value": false,
      "site": "006aeef4",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006aeef4",
      "incomplete_value": false,
      "site": "006aeef4",
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
            "const:ef0:8"
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
      "006aeef4",
      "DATA",
      [
        "storage",
        "00bf8ef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006aeef4",
      "DATA",
      [
        "storage",
        "00bf8fa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006aeef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ae/006aeee8.md#insn-006aeef0)
- 新版 [`006aeef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006aeee8.md#insn-006aeef0)

~~~diff
- 006aeef0 ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 006aeef0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006aeef0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006aeef0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006aeef0 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 006aeef0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006aeef0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006aeef0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006aeef0 bytes 29c13b91
+ 006aeef0 bytes 29813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb3932d9b6af0584749fd58c1f278c49"></a>

### [`006afa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afa38.md) → [`006afa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afa38.md) FUN_006afa38

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
      "definition_site": "006afa5c",
      "incomplete_value": false,
      "site": "006afa5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afa5c",
      "incomplete_value": false,
      "site": "006afa5c",
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
            "const:f70:8"
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
      "006afa5c",
      "DATA",
      [
        "storage",
        "00bf8f70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afa5c",
      "DATA",
      [
        "storage",
        "00bf9020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afa54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afa38.md#insn-006afa54) · [`006afa58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afa38.md#insn-006afa58)
- 新版 [`006afa54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afa38.md#insn-006afa54) · [`006afa58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afa38.md#insn-006afa58)

~~~diff
- 006afa54 ["COPY", "register:4040:8", ["const:bf8000:8"]]
+ 006afa54 ["COPY", "register:4040:8", ["const:bf9000:8"]]
- 006afa54 bytes 482a00b0
+ 006afa54 bytes 482a00d0
- 006afa58 ["COPY", "tmp:0:8", ["const:f70:8"]]
- 006afa58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006afa58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006afa58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006afa58 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 006afa58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006afa58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006afa58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006afa58 bytes 08c13d91
+ 006afa58 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-512f6c42d64fe289ce82c6cb5e71d743"></a>

### [`006afa6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afa6c.md) → [`006afa6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afa6c.md) FUN_006afa6c

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
      "definition_site": "006afa78",
      "incomplete_value": false,
      "site": "006afa78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afa78",
      "incomplete_value": false,
      "site": "006afa78",
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
            "const:f70:8"
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
      "006afa78",
      "DATA",
      [
        "storage",
        "00bf8f70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afa78",
      "DATA",
      [
        "storage",
        "00bf9020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afa70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afa6c.md#insn-006afa70) · [`006afa74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afa6c.md#insn-006afa74)
- 新版 [`006afa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afa6c.md#insn-006afa70) · [`006afa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afa6c.md#insn-006afa74)

~~~diff
- 006afa70 ["COPY", "register:4048:8", ["const:bf8000:8"]]
+ 006afa70 ["COPY", "register:4048:8", ["const:bf9000:8"]]
- 006afa70 bytes 492a00b0
+ 006afa70 bytes 492a00d0
- 006afa74 ["COPY", "tmp:0:8", ["const:f70:8"]]
- 006afa74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006afa74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006afa74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006afa74 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 006afa74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006afa74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006afa74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006afa74 bytes 29c13d91
+ 006afa74 bytes 29810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a6fb159b213624c8eb04a847db8a282"></a>

### [`006afb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afb70.md) → [`006afb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afb70.md) FUN_006afb70

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
      "definition_site": "006afb94",
      "incomplete_value": false,
      "site": "006afb94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afb94",
      "incomplete_value": false,
      "site": "006afb94",
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
            "const:ff0:8"
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
      "006afb94",
      "DATA",
      [
        "storage",
        "00bf8ff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afb94",
      "DATA",
      [
        "storage",
        "00bf90a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afb8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afb70.md#insn-006afb8c) · [`006afb90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afb70.md#insn-006afb90)
- 新版 [`006afb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afb70.md#insn-006afb8c) · [`006afb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afb70.md#insn-006afb90)

~~~diff
- 006afb8c ["COPY", "register:4040:8", ["const:bf8000:8"]]
+ 006afb8c ["COPY", "register:4040:8", ["const:bf9000:8"]]
- 006afb8c bytes 482a00b0
+ 006afb8c bytes 482a00d0
- 006afb90 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 006afb90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006afb90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006afb90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006afb90 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 006afb90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006afb90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006afb90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006afb90 bytes 08c13f91
+ 006afb90 bytes 08810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e50cb0bae20d19c4e23f5d3ef38de07c"></a>

### [`006afba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afba4.md) → [`006afba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afba4.md) FUN_006afba4

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
      "definition_site": "006afbb0",
      "incomplete_value": false,
      "site": "006afbb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afbb0",
      "incomplete_value": false,
      "site": "006afbb0",
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
            "const:ff0:8"
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
      "006afbb0",
      "DATA",
      [
        "storage",
        "00bf8ff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afbb0",
      "DATA",
      [
        "storage",
        "00bf90a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afba4.md#insn-006afba8) · [`006afbac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afba4.md#insn-006afbac)
- 新版 [`006afba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afba4.md#insn-006afba8) · [`006afbac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afba4.md#insn-006afbac)

~~~diff
- 006afba8 ["COPY", "register:4048:8", ["const:bf8000:8"]]
+ 006afba8 ["COPY", "register:4048:8", ["const:bf9000:8"]]
- 006afba8 bytes 492a00b0
+ 006afba8 bytes 492a00d0
- 006afbac ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 006afbac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006afbac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006afbac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006afbac ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 006afbac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006afbac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006afbac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006afbac bytes 29c13f91
+ 006afbac bytes 29810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0a8d64648dd9c5d8dbf8816cc324f32"></a>

### [`006afc9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afc9c.md) → [`006afc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afc9c.md) FUN_006afc9c

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
      "definition_site": "006afcc0",
      "incomplete_value": false,
      "site": "006afcc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afcc0",
      "incomplete_value": false,
      "site": "006afcc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:70:8"
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
      "006afcc0",
      "DATA",
      [
        "storage",
        "00bf9070",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afcc0",
      "DATA",
      [
        "storage",
        "00bf9120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afcbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afc9c.md#insn-006afcbc)
- 新版 [`006afcbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afc9c.md#insn-006afcbc)

~~~diff
- 006afcbc ["COPY", "tmp:0:8", ["const:70:8"]]
- 006afcbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006afcbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006afcbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006afcbc ["COPY", "tmp:0:8", ["const:120:8"]]
+ 006afcbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006afcbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006afcbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006afcbc bytes 08c10191
+ 006afcbc bytes 08810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a25a8a05560bcb785fe36a0cf8bd2db"></a>

### [`006afcd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afcd0.md) → [`006afcd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afcd0.md) FUN_006afcd0

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
      "definition_site": "006afcdc",
      "incomplete_value": false,
      "site": "006afcdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afcdc",
      "incomplete_value": false,
      "site": "006afcdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:70:8"
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
      "006afcdc",
      "DATA",
      [
        "storage",
        "00bf9070",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afcdc",
      "DATA",
      [
        "storage",
        "00bf9120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afcd0.md#insn-006afcd8)
- 新版 [`006afcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afcd0.md#insn-006afcd8)

~~~diff
- 006afcd8 ["COPY", "tmp:0:8", ["const:70:8"]]
- 006afcd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006afcd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006afcd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006afcd8 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 006afcd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006afcd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006afcd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006afcd8 bytes 29c10191
+ 006afcd8 bytes 29810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-215fb66e3a96cb6f19d35c716222fe5f"></a>

### [`006afe68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afe68.md) → [`006afe68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afe68.md) FUN_006afe68

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
      "definition_site": "006afe88",
      "incomplete_value": false,
      "site": "006afe8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afe88",
      "incomplete_value": false,
      "site": "006afe8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      "006afe8c",
      "DATA",
      [
        "storage",
        "00bf90f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afe8c",
      "DATA",
      [
        "storage",
        "00bf91a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afe88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afe68.md#insn-006afe88)
- 新版 [`006afe88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afe68.md#insn-006afe88)

~~~diff
- 006afe88 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 006afe88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006afe88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006afe88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006afe88 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 006afe88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006afe88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006afe88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006afe88 bytes 08c10391
+ 006afe88 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddf83e5842ed8ec372b684256f321775"></a>

### [`006afea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afea0.md) → [`006afea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afea0.md) FUN_006afea0

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
      "definition_site": "006afea4",
      "incomplete_value": false,
      "site": "006afea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afea4",
      "incomplete_value": false,
      "site": "006afea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      "006afea8",
      "DATA",
      [
        "storage",
        "00bf90f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afea8",
      "DATA",
      [
        "storage",
        "00bf91a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006af/006afea0.md#insn-006afea4)
- 新版 [`006afea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afea0.md#insn-006afea4)

~~~diff
- 006afea4 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 006afea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006afea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006afea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006afea4 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 006afea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006afea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006afea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006afea4 bytes 08c10391
+ 006afea4 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93e1bc5c3a84abc83ee48269bedc6f4f"></a>

### [`006b0184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0184.md) → [`006b0184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0184.md) FUN_006b0184

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
      "definition_site": "006b01a4",
      "incomplete_value": false,
      "site": "006b01a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b01a4",
      "incomplete_value": false,
      "site": "006b01a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "006b01a8",
      "DATA",
      [
        "storage",
        "00bf9170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b01a8",
      "DATA",
      [
        "storage",
        "00bf9220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b01a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0184.md#insn-006b01a4)
- 新版 [`006b01a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0184.md#insn-006b01a4)

~~~diff
- 006b01a4 ["COPY", "tmp:0:8", ["const:170:8"]]
- 006b01a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b01a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b01a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b01a4 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 006b01a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b01a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b01a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b01a4 bytes 08c10591
+ 006b01a4 bytes 08810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d7e16dc1084ea48c82f4bb5b1c66ec4"></a>

### [`006b01bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b01bc.md) → [`006b01bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b01bc.md) FUN_006b01bc

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
      "definition_site": "006b01c0",
      "incomplete_value": false,
      "site": "006b01c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b01c0",
      "incomplete_value": false,
      "site": "006b01c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "006b01c4",
      "DATA",
      [
        "storage",
        "00bf9170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b01c4",
      "DATA",
      [
        "storage",
        "00bf9220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b01c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b01bc.md#insn-006b01c0)
- 新版 [`006b01c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b01bc.md#insn-006b01c0)

~~~diff
- 006b01c0 ["COPY", "tmp:0:8", ["const:170:8"]]
- 006b01c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b01c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b01c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b01c0 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 006b01c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b01c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b01c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b01c0 bytes 08c10591
+ 006b01c0 bytes 08810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a092d35cbd7a03f64c807d173c435753"></a>

### [`006b04cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b04cc.md) → [`006b04cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b04cc.md) FUN_006b04cc

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
      "definition_site": "006b04ec",
      "incomplete_value": false,
      "site": "006b04f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b04ec",
      "incomplete_value": false,
      "site": "006b04f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "006b04f0",
      "DATA",
      [
        "storage",
        "00bf91f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b04f0",
      "DATA",
      [
        "storage",
        "00bf92a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b04ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b04cc.md#insn-006b04ec)
- 新版 [`006b04ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b04cc.md#insn-006b04ec)

~~~diff
- 006b04ec ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 006b04ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b04ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b04ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b04ec ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 006b04ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b04ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b04ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b04ec bytes 08c10791
+ 006b04ec bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d56a6b5b327f403d545704806a98be6a"></a>

### [`006b0504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0504.md) → [`006b0504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0504.md) FUN_006b0504

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
      "definition_site": "006b0508",
      "incomplete_value": false,
      "site": "006b050c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b0508",
      "incomplete_value": false,
      "site": "006b050c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
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
      "006b050c",
      "DATA",
      [
        "storage",
        "00bf91f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b050c",
      "DATA",
      [
        "storage",
        "00bf92a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b0508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0504.md#insn-006b0508)
- 新版 [`006b0508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0504.md#insn-006b0508)

~~~diff
- 006b0508 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 006b0508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b0508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b0508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b0508 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 006b0508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b0508 bytes 08c10791
+ 006b0508 bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb8eeb952c62e97617d0929555d27fe1"></a>

### [`006b0824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0824.md) → [`006b0824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0824.md) FUN_006b0824

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
      "definition_site": "006b0848",
      "incomplete_value": false,
      "site": "006b0848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b0848",
      "incomplete_value": false,
      "site": "006b0848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "006b0848",
      "DATA",
      [
        "storage",
        "00bf9270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b0848",
      "DATA",
      [
        "storage",
        "00bf9320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b0844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0824.md#insn-006b0844)
- 新版 [`006b0844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0824.md#insn-006b0844)

~~~diff
- 006b0844 ["COPY", "tmp:0:8", ["const:270:8"]]
- 006b0844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b0844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b0844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b0844 ["COPY", "tmp:0:8", ["const:320:8"]]
+ 006b0844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b0844 bytes 08c10991
+ 006b0844 bytes 08810c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e774330b3fb55b03535fdafdf80d2212"></a>

### [`006b0858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0858.md) → [`006b0858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0858.md) FUN_006b0858

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
      "definition_site": "006b0864",
      "incomplete_value": false,
      "site": "006b0864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b0864",
      "incomplete_value": false,
      "site": "006b0864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "006b0864",
      "DATA",
      [
        "storage",
        "00bf9270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b0864",
      "DATA",
      [
        "storage",
        "00bf9320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b0860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0858.md#insn-006b0860)
- 新版 [`006b0860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0858.md#insn-006b0860)

~~~diff
- 006b0860 ["COPY", "tmp:0:8", ["const:270:8"]]
- 006b0860 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006b0860 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006b0860 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006b0860 ["COPY", "tmp:0:8", ["const:320:8"]]
+ 006b0860 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006b0860 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006b0860 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006b0860 bytes 29c10991
+ 006b0860 bytes 29810c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2e4ebe79cd49fc24e7d16512e06782f"></a>

### [`006b0a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0a20.md) → [`006b0a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0a20.md) _INIT_106

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
      "definition_site": "006b0a5c",
      "incomplete_value": true,
      "site": "006b0a78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b0a5c",
      "incomplete_value": true,
      "site": "006b0a78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b0a80",
      "incomplete_value": true,
      "site": "006b0a9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b0a80",
      "incomplete_value": true,
      "site": "006b0a9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b0aa0",
      "incomplete_value": true,
      "site": "006b0abc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006b0aa0",
      "incomplete_value": true,
      "site": "006b0abc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006b0a5c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "006b0a80",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "006b0aa0",
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
      "006b0a5c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006b0a80",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006b0aa0",
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

- 旧版 [`006b0a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0a20.md#insn-006b0a4c) · [`006b0a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0a20.md#insn-006b0a54)
- 新版 [`006b0a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0a20.md#insn-006b0a4c) · [`006b0a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0a20.md#insn-006b0a54)

~~~diff
- 006b0a4c ["COPY", "tmp:0:8", ["const:778:8"]]
- 006b0a4c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006b0a4c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006b0a4c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006b0a4c ["COPY", "tmp:0:8", ["const:838:8"]]
+ 006b0a4c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006b0a4c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006b0a4c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006b0a4c bytes 73e21d91
+ 006b0a4c bytes 73e22091
- 006b0a54 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006b0a54 bytes a9dffff0
+ 006b0a54 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006b0a54 bytes a9dffff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98d64b1d52e92597a7110148e334c2b4"></a>

### [`006b0f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0f78.md) → [`006b0f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0f78.md) FUN_006b0f78

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ab1dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab1/00ab1dc0.md) · 呼出先 9件 [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md) [`006b0db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0db0.md) [`00ab1128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab1/00ab1128.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00ab1e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md) · 呼出先 9件 [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`006b0db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0db0.md) [`00ab11f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab11f0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.00% / 新版 86.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006b0fac",
      "incomplete_value": false,
      "site": "006b0fb4",
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
      "definition_site": "006b0fac",
      "incomplete_value": false,
      "site": "006b0fb4",
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
      "definition_site": "006b0fc8",
      "incomplete_value": true,
      "site": "006b0fd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ab0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b0fc8",
      "incomplete_value": true,
      "site": "006b0fd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ab7:8"
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
      "definition_site": "006b1068",
      "incomplete_value": true,
      "site": "006b106c",
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
      "definition_site": "006b1068",
      "incomplete_value": true,
      "site": "006b106c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b0fb4",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "006b0fc8",
      "READ",
      [
        "storage",
        "002a6ab7",
        null,
        "string"
      ]
    ],
    [
      "006b1058",
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
      "006b0fb4",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006b0fc8",
      "READ",
      [
        "storage",
        "002a6ab0",
        null,
        "string"
      ]
    ],
    [
      "006b1058",
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

- 旧版 [`006b0fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0f78.md#insn-006b0fac) · [`006b0fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0f78.md#insn-006b0fc4) · [`006b1058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0f78.md#insn-006b1058)
- 新版 [`006b0fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0f78.md#insn-006b0fac) · [`006b0fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0f78.md#insn-006b0fc4) · [`006b1058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0f78.md#insn-006b1058)

~~~diff
- 006b0fac ["COPY", "tmp:0:8", ["const:c78:8"]]
- 006b0fac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b0fac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b0fac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b0fac ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 006b0fac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0fac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0fac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b0fac bytes 08e13191
+ 006b0fac bytes 08a13491
- 006b0fc4 ["COPY", "tmp:0:8", ["const:ab7:8"]]
- 006b0fc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b0fc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b0fc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b0fc4 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 006b0fc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0fc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b0fc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b0fc4 bytes 08dd2a91
+ 006b0fc4 bytes 08c12a91
- 006b1058 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 006b1058 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006b1058 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 006b1058 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006b1058 bytes 086146f9
+ 006b1058 bytes 08b946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b47724c6cca6cb3cf07cdb74db8e6df"></a>

### [`006b12cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b1/006b12cc.md) → [`006b12cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b12cc.md) FUN_006b12cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ab1dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab1/00ab1dc0.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00ab1e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.45% / 新版 90.45%

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
      "definition_site": "006b130c",
      "incomplete_value": false,
      "site": "006b1310",
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
      "definition_site": "006b130c",
      "incomplete_value": false,
      "site": "006b1310",
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
      "definition_site": "006b1328",
      "incomplete_value": true,
      "site": "006b133c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b1328",
      "incomplete_value": true,
      "site": "006b133c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:621:8"
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
      "definition_site": "006b1328",
      "incomplete_value": true,
      "site": "006b133c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "006b1328",
      "incomplete_value": true,
      "site": "006b133c",
      "value": [
        "LOAD",
        "16",
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
      "006b1310",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "006b1328",
      "READ",
      [
        "storage",
        "0029d621",
        null,
        "string"
      ]
    ],
    [
      "006b1328",
      "READ",
      [
        "storage",
        "0029d631",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b1310",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006b1328",
      "READ",
      [
        "storage",
        "0029d6ae",
        null,
        "string"
      ]
    ],
    [
      "006b1328",
      "READ",
      [
        "storage",
        "0029d6be",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b130c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b1/006b12cc.md#insn-006b130c) · [`006b1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b1/006b12cc.md#insn-006b1320) · [`006b1324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b1/006b12cc.md#insn-006b1324)
- 新版 [`006b130c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b12cc.md#insn-006b130c) · [`006b1320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b12cc.md#insn-006b1320)

~~~diff
- 006b130c ["COPY", "tmp:0:8", ["const:c78:8"]]
- 006b130c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b130c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b130c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b130c ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 006b130c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b130c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b130c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b130c bytes 08e13191
+ 006b130c bytes 08a13491
- 006b1320 ["COPY", "tmp:0:8", ["const:621:8"]]
- 006b1320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b1320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b1320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b1320 ["COPY", "tmp:0:8", ["const:6ae:8"]]
+ 006b1320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b1320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b1320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b1320 bytes 08851891
+ 006b1320 bytes 08b91a91
- 006b1324 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 006b1324 bytes 09e0ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aba8427277174f79fcbe88a7067c201c"></a>

### [`006b15e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b1/006b15e4.md) → [`006b15e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b15e4.md) FUN_006b15e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0068d810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068d/0068d810.md) · 呼出先 27件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`0068d810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d810.md) · 呼出先 27件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.04% / 新版 92.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b177c",
      "incomplete_value": true,
      "site": "006b177c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "006b177c",
      "incomplete_value": true,
      "site": "006b177c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006b1824",
      "incomplete_value": false,
      "site": "006b1824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b1824",
      "incomplete_value": false,
      "site": "006b1824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "definition_site": "006b1a18",
      "incomplete_value": false,
      "site": "006b1a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b1a18",
      "incomplete_value": false,
      "site": "006b1a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "006b1660",
      "READ",
      [
        "storage",
        "00c27d14",
        null,
        "undefined4"
      ]
    ],
    [
      "006b167c",
      "READ",
      [
        "storage",
        "00c27d10",
        null,
        "undefined4"
      ]
    ],
    [
      "006b1760",
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
      "006b1660",
      "READ",
      [
        "storage",
        "00c27dd4",
        null,
        "undefined4"
      ]
    ],
    [
      "006b167c",
      "READ",
      [
        "storage",
        "00c27dd0",
        null,
        "undefined4"
      ]
    ],
    [
      "006b1760",
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

- 旧版 [`006b165c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b1/006b15e4.md#insn-006b165c) · [`006b1678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b1/006b15e4.md#insn-006b1678) · [`006b175c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b1/006b15e4.md#insn-006b175c)
- 新版 [`006b165c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b15e4.md#insn-006b165c) · [`006b1678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b15e4.md#insn-006b1678) · [`006b175c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b15e4.md#insn-006b175c)

~~~diff
- 006b165c ["COPY", "tmp:0:8", ["const:d14:8"]]
- 006b165c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b165c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b165c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b165c ["COPY", "tmp:0:8", ["const:dd4:8"]]
+ 006b165c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b165c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b165c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b165c bytes 08513491
+ 006b165c bytes 08513791
- 006b1678 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 006b1678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b1678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b1678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b1678 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 006b1678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b1678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b1678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b1678 bytes 08413491
+ 006b1678 bytes 08413791
- 006b175c ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 006b175c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006b175c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006b175c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006b175c ["COPY", "tmp:0:8", ["const:6d9:8"]]
+ 006b175c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006b175c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006b175c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006b175c bytes 29811b91
+ 006b175c bytes 29651b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86bdccc9997b34ca71bae5f569b65360"></a>

### [`006b2b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b2/006b2b44.md) → [`006b2b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b2/006b2b44.md) FUN_006b2b44

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c6850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c6/006c6850.md) · 呼出先 18件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c1dc.md) [`0044c794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c794.md) [`0044c80c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c80c.md)
- 新版 呼出元 1件 [`006c6850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c6/006c6850.md) · 呼出先 18件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md) [`0044c794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c794.md) [`0044c80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c80c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.40% / 新版 88.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 7件, `store_value` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b2b88",
      "incomplete_value": true,
      "site": "006b2b98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b2b88",
      "incomplete_value": true,
      "site": "006b2b98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b82:8"
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
      "definition_site": "006b2b88",
      "incomplete_value": true,
      "site": "006b2b9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b2b88",
      "incomplete_value": true,
      "site": "006b2b9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b82:8"
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
      "definition_site": "006b2bc0",
      "incomplete_value": true,
      "site": "006b2bd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6f7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b2bc0",
      "incomplete_value": true,
      "site": "006b2bd4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6fe:8"
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
      "006b2b74",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "006b2b88",
      "READ",
      [
        "storage",
        "00292b82",
        null,
        "string"
      ]
    ],
    [
      "006b2bc0",
      "READ",
      [
        "storage",
        "002a26fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b2b74",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006b2b88",
      "READ",
      [
        "storage",
        "00292c0f",
        null,
        "string"
      ]
    ],
    [
      "006b2bc0",
      "READ",
      [
        "storage",
        "002a26f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b2b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b2/006b2b44.md#insn-006b2b60) · [`006b2b64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b2/006b2b44.md#insn-006b2b64) · [`006b2b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b2/006b2b44.md#insn-006b2b7c)
- 新版 [`006b2b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b2/006b2b44.md#insn-006b2b60) · [`006b2b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b2/006b2b44.md#insn-006b2b64)

~~~diff
- 006b2b60 ["COPY", "register:40b8:8", ["const:c24000:8"]]
+ 006b2b60 ["COPY", "register:40b8:8", ["const:c25000:8"]]
- 006b2b60 bytes 972b00d0
+ 006b2b60 bytes 972b00f0
- 006b2b64 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 006b2b64 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 006b2b64 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 006b2b64 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 006b2b64 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 006b2b64 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 006b2b64 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 006b2b64 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 006b2b64 bytes f7e23d91
+ 006b2b64 bytes f7e20091
- 006b2b7c ["COPY", "register:4048:8", ["const:292000:8"]]
- 006b2b7c bytes 09dfff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a1dcf1ee92b065fbcb046ab454237ef"></a>

### [`006b3674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b3/006b3674.md) → [`006b3674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b3/006b3674.md) FUN_006b3674

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c8/006c86d0.md) · 呼出先 10件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) · 呼出先 10件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.96% / 新版 82.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b36b8",
      "incomplete_value": true,
      "site": "006b36c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c0f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b36b8",
      "incomplete_value": true,
      "site": "006b36c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b82:8"
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
      "definition_site": "006b36e8",
      "incomplete_value": true,
      "site": "006b36fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6f7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b36e8",
      "incomplete_value": true,
      "site": "006b36fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6fe:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "006b385c",
      "incomplete_value": false,
      "site": "006b385c",
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
      "definition_site": "006b385c",
      "incomplete_value": false,
      "site": "006b385c",
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
      "006b36a4",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "006b36b8",
      "READ",
      [
        "storage",
        "00292b82",
        null,
        "string"
      ]
    ],
    [
      "006b36e8",
      "READ",
      [
        "storage",
        "002a26fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b36a4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006b36b8",
      "READ",
      [
        "storage",
        "00292c0f",
        null,
        "string"
      ]
    ],
    [
      "006b36e8",
      "READ",
      [
        "storage",
        "002a26f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b369c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b3/006b3674.md#insn-006b369c) · [`006b36a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b3/006b3674.md#insn-006b36a0) · [`006b36ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b3/006b3674.md#insn-006b36ac)
- 新版 [`006b369c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b3/006b3674.md#insn-006b369c) · [`006b36a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b3/006b3674.md#insn-006b36a0)

~~~diff
- 006b369c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 006b369c ["COPY", "register:4040:8", ["const:c25000:8"]]
- 006b369c bytes 882b00b0
+ 006b369c bytes 882b00d0
- 006b36a0 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 006b36a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b36a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b36a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b36a0 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 006b36a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b36a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b36a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b36a0 bytes 08e13d91
+ 006b36a0 bytes 08e10091
- 006b36ac ["COPY", "register:4048:8", ["const:292000:8"]]
- 006b36ac bytes e9defff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68fc68cd35f27df60fa41c3ace5e76a1"></a>

### [`006b408c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b4/006b408c.md) → [`006b408c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b4/006b408c.md) FUN_006b408c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006c0060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0060.md) [`006ce8d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ce/006ce8d4.md) · 呼出先 14件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00446074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446074.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md)
- 新版 呼出元 2件 [`006c0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0060.md) [`006ce8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006ce8d4.md) · 呼出先 14件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446074.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.63% / 新版 99.63%

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
      "definition_site": "006b40cc",
      "incomplete_value": true,
      "site": "006b40cc",
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
      "definition_site": "006b40cc",
      "incomplete_value": true,
      "site": "006b40cc",
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
      "definition_site": "006b40d4",
      "incomplete_value": false,
      "site": "006b40e8",
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
      "definition_site": "006b40d4",
      "incomplete_value": false,
      "site": "006b40e8",
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
      "definition_site": "006b40dc",
      "incomplete_value": false,
      "site": "006b40e8",
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
    "old": {
      "definition_site": "006b40dc",
      "incomplete_value": false,
      "site": "006b40e8",
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
            "const:1e8:8"
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
      "006b40c8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "006b40d4",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006b40dc",
      "PARAM",
      [
        "storage",
        "00bf61e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006b40c8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006b40d4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006b40dc",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b40c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b4/006b408c.md#insn-006b40c8) · [`006b40d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b4/006b408c.md#insn-006b40d4) · [`006b40dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b4/006b408c.md#insn-006b40dc)
- 新版 [`006b40c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b4/006b408c.md#insn-006b40c8) · [`006b40d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b4/006b408c.md#insn-006b40d4) · [`006b40dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b4/006b408c.md#insn-006b40dc)

~~~diff
- 006b40c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 006b40c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006b40c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006b40c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006b40c8 bytes 08dd44f9
+ 006b40c8 bytes 083d45f9
- 006b40d4 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 006b40d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006b40d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006b40d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006b40d4 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006b40d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006b40d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006b40d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006b40d4 bytes 21603691
+ 006b40d4 bytes 21203991
- 006b40dc ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 006b40dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006b40dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006b40dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006b40dc ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006b40dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006b40dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006b40dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006b40dc bytes 42a00791
+ 006b40dc bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6910fee3f457f90f247d9f44b6a5a3c2"></a>

### [`006b5fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b5/006b5fcc.md) → [`006b5fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b5/006b5fcc.md) FUN_006b5fcc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ab1dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab1/00ab1dc0.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00464a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`00ab1e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)

変更の種類 comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 96.56% / 新版 96.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b642c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b6430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b643c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b6028",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "006b6108",
      "READ",
      [
        "storage",
        "00299fce",
        null,
        "string"
      ]
    ],
    [
      "unmatched:006b641c",
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
      "006b6028",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006b6108",
      "READ",
      [
        "storage",
        "0029a05b",
        null,
        "string"
      ]
    ],
    [
      "006b641c",
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

- 旧版 [`006b642c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b5/006b5fcc.md#insn-006b642c) · [`006b6430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b5/006b5fcc.md#insn-006b6430)
- 新版 [`006b642c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b5/006b5fcc.md#insn-006b642c)

~~~diff
- 006b642c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:100:8"]]
- 006b642c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006b642c bytes e88300f9
+ 006b642c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:100:8"]]
+ 006b642c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 006b642c bytes e88300f9
- 006b6430 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:148:8"]]
- 006b6430 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 006b6430 bytes e9a700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5c8f10d188f8e4fadc15b9f7c504c55"></a>

### [`006b6b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b6/006b6b68.md) → [`006b6b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b6/006b6b68.md) FUN_006b6b68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006b6c84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b6/006b6c84.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`006b6c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b6/006b6c84.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006b6b80",
      "incomplete_value": true,
      "site": "006b6b84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c27000:8"
              ],
              [
                "leaf",
                "const:c90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b6b80",
      "incomplete_value": true,
      "site": "006b6b84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c27000:8"
              ],
              [
                "leaf",
                "const:bd0:8"
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
      "definition_site": "006b6b98",
      "incomplete_value": true,
      "site": "006b6b9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c27000:8"
              ],
              [
                "leaf",
                "const:c78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b6b98",
      "incomplete_value": true,
      "site": "006b6b9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c27000:8"
              ],
              [
                "leaf",
                "const:bb8:8"
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
      "definition_site": "006b6bb0",
      "incomplete_value": true,
      "site": "006b6bb4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b6bb0",
      "incomplete_value": true,
      "site": "006b6bb4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ba0:8"
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
      "006b6b74",
      "READ",
      [
        "storage",
        "00c27bc0",
        null,
        "undefined1"
      ]
    ],
    [
      "006b6b80",
      "READ",
      [
        "storage",
        "00c27bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "006b6b8c",
      "READ",
      [
        "storage",
        "00c27ba8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "006b6b74",
      "READ",
      [
        "storage",
        "00c27c80",
        null,
        "undefined1"
      ]
    ],
    [
      "006b6b80",
      "READ",
      [
        "storage",
        "00c27c90",
        null,
        "undefined8"
      ]
    ],
    [
      "006b6b8c",
      "READ",
      [
        "storage",
        "00c27c68",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b6b74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b6/006b6b68.md#insn-006b6b74) · [`006b6b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b6/006b6b68.md#insn-006b6b80) · [`006b6b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b6/006b6b68.md#insn-006b6b8c)
- 新版 [`006b6b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b6/006b6b68.md#insn-006b6b74) · [`006b6b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b6/006b6b68.md#insn-006b6b80) · [`006b6b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b6/006b6b68.md#insn-006b6b8c)

~~~diff
- 006b6b74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bc0:8"]]
- 006b6b74 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 006b6b74 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 006b6b74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c80:8"]]
+ 006b6b74 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 006b6b74 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 006b6b74 bytes 08016f39
+ 006b6b74 bytes 08017239
- 006b6b80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd0:8"]]
- 006b6b80 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006b6b80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c90:8"]]
+ 006b6b80 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006b6b80 bytes 00e945f9
+ 006b6b80 bytes 004946f9
- 006b6b8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ba8:8"]]
- 006b6b8c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 006b6b8c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 006b6b8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c68:8"]]
+ 006b6b8c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 006b6b8c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 006b6b8c bytes 08a16e39
+ 006b6b8c bytes 08a17139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e4a6501b1ae13253bdd91854d01d4ac"></a>

### [`006b77e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b7/006b77e4.md) → [`006b77e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b7/006b77e4.md) FUN_006b77e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006c0784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0784.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`0044b898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8a8.md)
- 新版 呼出元 1件 [`006c0784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.21% / 新版 96.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b7a20",
      "incomplete_value": true,
      "site": "006b7a20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:16c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b7a20",
      "incomplete_value": true,
      "site": "006b7a20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df:8"
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
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006b7954",
      "incomplete_value": false,
      "site": "006b7968",
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
      "definition_site": "006b7954",
      "incomplete_value": false,
      "site": "006b7968",
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006b7c80",
      "incomplete_value": true,
      "site": "006b7c84",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b7c80",
      "incomplete_value": true,
      "site": "006b7c84",
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
            "const:f78:8"
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b7898",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "006b7954",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      "006b7a08",
      "READ",
      [
        "storage",
        "002990df",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b7898",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006b7954",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "006b7a08",
      "READ",
      [
        "storage",
        "0029916c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b7/006b77e4.md#insn-006b7890) · [`006b7894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b7/006b77e4.md#insn-006b7894) · [`006b7950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b7/006b77e4.md#insn-006b7950)
- 新版 [`006b7890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b7/006b77e4.md#insn-006b7890) · [`006b7894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b7/006b77e4.md#insn-006b7894) · [`006b7950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b7/006b77e4.md#insn-006b7950)

~~~diff
- 006b7890 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 006b7890 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 006b7890 bytes 682b00b0
+ 006b7890 bytes 682b00d0
- 006b7894 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 006b7894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b7894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b7894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b7894 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 006b7894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b7894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b7894 bytes 08e13d91
+ 006b7894 bytes 08e10091
- 006b7950 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 006b7950 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 006b7950 bytes 602b00b0
+ 006b7950 bytes 602b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c05bcd5638ee760312e9c5aa0dc51052"></a>

### [`006b8bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b8/006b8bf4.md) → [`006b8bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8bf4.md) FUN_006b8bf4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006b8e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b8/006b8e78.md) · 呼出先 11件 [`00464a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a54.md) [`00464ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464ac4.md) [`00464b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`006b8e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8e78.md) · 呼出先 11件 [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ac4.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006b8c30",
      "incomplete_value": false,
      "site": "006b8c3c",
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
      "definition_site": "006b8c30",
      "incomplete_value": false,
      "site": "006b8c3c",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b8c34",
      "incomplete_value": true,
      "site": "006b8c48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c21:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b8c34",
      "incomplete_value": true,
      "site": "006b8c48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b94:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b8d88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006b8c34",
      "READ",
      [
        "storage",
        "00292b94",
        null,
        "string"
      ]
    ],
    [
      "006b8c3c",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006b8d78",
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
      "006b8c34",
      "READ",
      [
        "storage",
        "00292c21",
        null,
        "string"
      ]
    ],
    [
      "006b8c3c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006b8d78",
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

- 旧版 [`006b8d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b8/006b8bf4.md#insn-006b8d88) · [`006b8d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b8/006b8bf4.md#insn-006b8d8c)
- 新版 [`006b8d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8bf4.md#insn-006b8d88)

~~~diff
- 006b8d88 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 006b8d88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006b8d88 bytes e81300f9
+ 006b8d88 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
+ 006b8d88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 006b8d88 bytes e81300f9
- 006b8d8c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:68:8"]]
- 006b8d8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 006b8d8c bytes e93700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b41539037aef3ed60d7bf4cfcc1989d0"></a>

### [`006b8e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b8/006b8e78.md) → [`006b8e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8e78.md) FUN_006b8e78

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006c0784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0784.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0044b898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md)
- 新版 呼出元 1件 [`006c0784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.53% / 新版 93.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006b9060",
      "incomplete_value": true,
      "site": "006b9060",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:16c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b9060",
      "incomplete_value": true,
      "site": "006b9060",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df:8"
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
      "definition_site": "006b92a0",
      "incomplete_value": false,
      "site": "006b92a0",
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
      "definition_site": "006b92a0",
      "incomplete_value": false,
      "site": "006b92a0",
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
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006b92a4",
      "incomplete_value": false,
      "site": "006b92a4",
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
      "definition_site": "006b92a4",
      "incomplete_value": false,
      "site": "006b92a4",
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
      "006b8ecc",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "006b8f94",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      "006b9048",
      "READ",
      [
        "storage",
        "002990df",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006b8ecc",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006b8f94",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "006b9048",
      "READ",
      [
        "storage",
        "0029916c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b8ec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b8/006b8e78.md#insn-006b8ec0) · [`006b8ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b8/006b8e78.md#insn-006b8ec4) · [`006b8f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b8/006b8e78.md#insn-006b8f90)
- 新版 [`006b8ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8e78.md#insn-006b8ec0) · [`006b8ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8e78.md#insn-006b8ec4) · [`006b8f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b8/006b8e78.md#insn-006b8f90)

~~~diff
- 006b8ec0 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 006b8ec0 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 006b8ec0 bytes 682b0090
+ 006b8ec0 bytes 682b00b0
- 006b8ec4 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 006b8ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b8ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b8ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006b8ec4 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 006b8ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006b8ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006b8ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b8ec4 bytes 08e13d91
+ 006b8ec4 bytes 08e10091
- 006b8f90 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 006b8f90 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 006b8f90 bytes 602b0090
+ 006b8f90 bytes 602b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1737d75a23c3df99606e646151b0f42"></a>

### [`006ba6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ba/006ba6e4.md) → [`006ba6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006ba6e4.md) FUN_006ba6e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006baf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ba/006baf70.md) [`006bbf6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bb/006bbf6c.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 2件 [`006baf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006baf70.md) [`006bbf6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bbf6c.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.58% / 新版 85.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 14件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ba7c8",
      "incomplete_value": true,
      "site": "006ba7d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ba7c8",
      "incomplete_value": true,
      "site": "006ba7d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ff2:8"
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
      "definition_site": "006ba7d8",
      "incomplete_value": true,
      "site": "006ba7d8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006ba7d8",
      "incomplete_value": true,
      "site": "006ba7d8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006ba828",
      "incomplete_value": true,
      "site": "006ba838",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:633:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ba828",
      "incomplete_value": true,
      "site": "006ba838",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:63a:8"
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
      "006ba7a4",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "006ba7c8",
      "READ",
      [
        "storage",
        "00299ff2",
        null,
        "string"
      ]
    ],
    [
      "006ba7cc",
      "READ",
      [
        "storage",
        "0029a001",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006ba7a4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006ba7c8",
      "READ",
      [
        "storage",
        "0029a07f",
        null,
        "string"
      ]
    ],
    [
      "006ba7cc",
      "READ",
      [
        "storage",
        "0029a08e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ba79c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ba/006ba6e4.md#insn-006ba79c) · [`006ba7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ba/006ba6e4.md#insn-006ba7a0) · [`006ba7b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ba/006ba6e4.md#insn-006ba7b8)
- 新版 [`006ba79c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006ba6e4.md#insn-006ba79c) · [`006ba7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006ba6e4.md#insn-006ba7a0) · [`006ba7b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006ba6e4.md#insn-006ba7b8)

~~~diff
- 006ba79c ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 006ba79c ["COPY", "register:4040:8", ["const:c25000:8"]]
- 006ba79c bytes 482b00d0
+ 006ba79c bytes 482b00f0
- 006ba7a0 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 006ba7a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ba7a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ba7a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ba7a0 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 006ba7a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ba7a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ba7a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ba7a0 bytes 08e13d91
+ 006ba7a0 bytes 08e10091
- 006ba7b8 ["COPY", "register:4040:8", ["const:299000:8"]]
+ 006ba7b8 ["COPY", "register:4040:8", ["const:29a000:8"]]
- 006ba7b8 bytes e8defff0
+ 006ba7b8 bytes 08dfff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-518816b6dc11dda9e303fc3c0ab39039"></a>

### [`006baf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ba/006baf70.md) → [`006baf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006baf70.md) FUN_006baf70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c8/006c86d0.md) · 呼出先 16件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0068c0a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068c/0068c0a8.md) [`0069a970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069a/0069a970.md) [`0069a9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069a/0069a9cc.md) [`0069ab88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069a/0069ab88.md)
- 新版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) · 呼出先 16件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0068c0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c0a8.md) [`0069a970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a970.md) [`0069a9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a9cc.md) [`0069ab88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069ab88.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.97% / 新版 98.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006bb4e0",
      "incomplete_value": false,
      "site": "006bb4e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bb4e0",
      "incomplete_value": false,
      "site": "006bb4e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006bafb4",
      "incomplete_value": true,
      "site": "006bafb4",
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
      "definition_site": "006bafb4",
      "incomplete_value": true,
      "site": "006bafb4",
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
      "006bafb0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "006bafbc",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bafc4",
      "PARAM",
      [
        "storage",
        "00bf61e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006bafb0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006bafbc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bafc4",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bafb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ba/006baf70.md#insn-006bafb0) · [`006bafbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ba/006baf70.md#insn-006bafbc) · [`006bafc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ba/006baf70.md#insn-006bafc4)
- 新版 [`006bafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006baf70.md#insn-006bafb0) · [`006bafbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006baf70.md#insn-006bafbc) · [`006bafc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006baf70.md#insn-006bafc4)

~~~diff
- 006bafb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 006bafb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006bafb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006bafb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006bafb0 bytes 08dd44f9
+ 006bafb0 bytes 083d45f9
- 006bafbc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 006bafbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006bafbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006bafbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006bafbc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006bafbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006bafbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006bafbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006bafbc bytes 21603691
+ 006bafbc bytes 21203991
- 006bafc4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 006bafc4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006bafc4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006bafc4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006bafc4 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006bafc4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006bafc4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006bafc4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006bafc4 bytes 42a00791
+ 006bafc4 bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5314d936e574856e6a4aa6ab99a3377a"></a>

### [`006bbf6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bb/006bbf6c.md) → [`006bbf6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bbf6c.md) FUN_006bbf6c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c8/006c86d0.md) · 呼出先 59件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041d/0041dfc0.md) [`0042cde4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042cde4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) · 呼出先 59件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.91% / 新版 96.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 17件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006bc844",
      "incomplete_value": false,
      "site": "006bc844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bc844",
      "incomplete_value": false,
      "site": "006bc844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "definition_site": "006bc918",
      "incomplete_value": false,
      "site": "006bc918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bc918",
      "incomplete_value": false,
      "site": "006bc918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "definition_site": "006bca78",
      "incomplete_value": false,
      "site": "006bca80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bca78",
      "incomplete_value": false,
      "site": "006bca80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "006bbfa8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "006bbfb4",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bbfbc",
      "PARAM",
      [
        "storage",
        "00bf61e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006bbfa8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006bbfb4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bbfbc",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bbfa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bb/006bbf6c.md#insn-006bbfa8) · [`006bbfb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bb/006bbf6c.md#insn-006bbfb4) · [`006bbfbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bb/006bbf6c.md#insn-006bbfbc)
- 新版 [`006bbfa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bbf6c.md#insn-006bbfa8) · [`006bbfb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bbf6c.md#insn-006bbfb4) · [`006bbfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bbf6c.md#insn-006bbfbc)

~~~diff
- 006bbfa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 006bbfa8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006bbfa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006bbfa8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006bbfa8 bytes 00dd44f9
+ 006bbfa8 bytes 003d45f9
- 006bbfb4 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 006bbfb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006bbfb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006bbfb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006bbfb4 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006bbfb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006bbfb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006bbfb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006bbfb4 bytes 21603691
+ 006bbfb4 bytes 21203991
- 006bbfbc ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 006bbfbc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006bbfbc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006bbfbc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006bbfbc ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006bbfbc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006bbfbc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006bbfbc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006bbfbc bytes 42a00791
+ 006bbfbc bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-587e9111e5f73864a6eadcfd58e24e47"></a>

### [`006bdb8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bd/006bdb8c.md) → [`006bdb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bdb8c.md) FUN_006bdb8c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006cec14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ce/006cec14.md) · 呼出先 12件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449bac.md)
- 新版 呼出元 1件 [`006cec14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006cec14.md) · 呼出先 12件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006bdbbc",
      "incomplete_value": true,
      "site": "006bdbbc",
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
      "definition_site": "006bdbbc",
      "incomplete_value": true,
      "site": "006bdbbc",
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
      "definition_site": "006bdbc4",
      "incomplete_value": false,
      "site": "006bdbd4",
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
      "definition_site": "006bdbc4",
      "incomplete_value": false,
      "site": "006bdbd4",
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
      "definition_site": "006bdbcc",
      "incomplete_value": false,
      "site": "006bdbd4",
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
    "old": {
      "definition_site": "006bdbcc",
      "incomplete_value": false,
      "site": "006bdbd4",
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
            "const:1e8:8"
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
      "006bdbb8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "006bdbc4",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bdbcc",
      "PARAM",
      [
        "storage",
        "00bf61e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006bdbb8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006bdbc4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bdbcc",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bdbb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bd/006bdb8c.md#insn-006bdbb8) · [`006bdbc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bd/006bdb8c.md#insn-006bdbc4) · [`006bdbcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bd/006bdb8c.md#insn-006bdbcc)
- 新版 [`006bdbb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bdb8c.md#insn-006bdbb8) · [`006bdbc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bdb8c.md#insn-006bdbc4) · [`006bdbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bdb8c.md#insn-006bdbcc)

~~~diff
- 006bdbb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 006bdbb8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006bdbb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006bdbb8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006bdbb8 bytes 00dd44f9
+ 006bdbb8 bytes 003d45f9
- 006bdbc4 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 006bdbc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006bdbc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006bdbc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006bdbc4 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006bdbc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006bdbc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006bdbc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006bdbc4 bytes 21603691
+ 006bdbc4 bytes 21203991
- 006bdbcc ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 006bdbcc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006bdbcc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006bdbcc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006bdbcc ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006bdbcc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006bdbcc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006bdbcc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006bdbcc bytes 42a00791
+ 006bdbcc bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afba66a5bde5d4290f4d6208be649517"></a>

### [`006bde3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bd/006bde3c.md) → [`006bde3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bde3c.md) FUN_006bde3c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006bdb8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bd/006bdb8c.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00447378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447378.md) [`00448040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448040.md)
- 新版 呼出元 1件 [`006bdb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bdb8c.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00447378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447378.md) [`00448040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.79% / 新版 99.79%

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
      "definition_site": "006bde90",
      "incomplete_value": true,
      "site": "006bde90",
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
      "definition_site": "006bde90",
      "incomplete_value": true,
      "site": "006bde90",
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
      "definition_site": "006bde98",
      "incomplete_value": false,
      "site": "006bdeac",
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
      "definition_site": "006bde98",
      "incomplete_value": false,
      "site": "006bdeac",
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
      "definition_site": "006bdea0",
      "incomplete_value": false,
      "site": "006bdeac",
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
    "old": {
      "definition_site": "006bdea0",
      "incomplete_value": false,
      "site": "006bdeac",
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
            "const:1e8:8"
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
      "006bde8c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "006bde98",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bdea0",
      "PARAM",
      [
        "storage",
        "00bf61e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006bde8c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006bde98",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bdea0",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bde8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bd/006bde3c.md#insn-006bde8c) · [`006bde98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bd/006bde3c.md#insn-006bde98) · [`006bdea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bd/006bde3c.md#insn-006bdea0)
- 新版 [`006bde8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bde3c.md#insn-006bde8c) · [`006bde98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bde3c.md#insn-006bde98) · [`006bdea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bd/006bde3c.md#insn-006bdea0)

~~~diff
- 006bde8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 006bde8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006bde8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006bde8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006bde8c bytes 08dd44f9
+ 006bde8c bytes 083d45f9
- 006bde98 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 006bde98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006bde98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006bde98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006bde98 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006bde98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006bde98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006bde98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006bde98 bytes 21603691
+ 006bde98 bytes 21203991
- 006bdea0 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 006bdea0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006bdea0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006bdea0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006bdea0 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006bdea0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006bdea0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006bdea0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006bdea0 bytes 42a00791
+ 006bdea0 bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a84edccda7f45213bc9f94209ad437b7"></a>

### [`006bee18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006be/006bee18.md) → [`006bee18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006be/006bee18.md) FUN_006bee18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c0784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0784.md) · 呼出先 19件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`006c0784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md) · 呼出先 19件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.93% / 新版 90.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 14件, `store_value` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006bf180",
      "incomplete_value": true,
      "site": "006bf194",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:633:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bf180",
      "incomplete_value": true,
      "site": "006bf194",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:63a:8"
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
      "definition_site": "006bf1dc",
      "incomplete_value": true,
      "site": "006bf1ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:70c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006bf1dc",
      "incomplete_value": true,
      "site": "006bf1ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:713:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 51,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006bf448",
      "incomplete_value": false,
      "site": "006bf448",
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
      "definition_site": "006bf448",
      "incomplete_value": false,
      "site": "006bf448",
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
    "ordinal": 62,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006bee54",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "006bee60",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bee68",
      "PARAM",
      [
        "storage",
        "00bf61e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006bee54",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006bee60",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bee68",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bee54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006be/006bee18.md#insn-006bee54) · [`006bee60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006be/006bee18.md#insn-006bee60) · [`006bee68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006be/006bee18.md#insn-006bee68)
- 新版 [`006bee54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006be/006bee18.md#insn-006bee54) · [`006bee60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006be/006bee18.md#insn-006bee60) · [`006bee68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006be/006bee18.md#insn-006bee68)

~~~diff
- 006bee54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 006bee54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006bee54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006bee54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006bee54 bytes 08dd44f9
+ 006bee54 bytes 083d45f9
- 006bee60 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 006bee60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006bee60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006bee60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006bee60 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006bee60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006bee60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006bee60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006bee60 bytes 21603691
+ 006bee60 bytes 21203991
- 006bee68 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 006bee68 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006bee68 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006bee68 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006bee68 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006bee68 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006bee68 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006bee68 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006bee68 bytes 42a00791
+ 006bee68 bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e4fbcc4c6e2da4358e323cbc576dde7"></a>

### [`006bf5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bf/006bf5a0.md) → [`006bf5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bf/006bf5a0.md) FUN_006bf5a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c8/006c86d0.md) · 呼出先 30件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041d/0041dfc0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0042cde4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042cde4.md)
- 新版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) · 呼出先 30件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.78% / 新版 98.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006bf5d4",
      "incomplete_value": true,
      "site": "006bf5d4",
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
      "definition_site": "006bf5d4",
      "incomplete_value": true,
      "site": "006bf5d4",
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
      "definition_site": "006bf5dc",
      "incomplete_value": false,
      "site": "006bf5f0",
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
      "definition_site": "006bf5dc",
      "incomplete_value": false,
      "site": "006bf5f0",
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
      "definition_site": "006bf5e4",
      "incomplete_value": false,
      "site": "006bf5f0",
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
    "old": {
      "definition_site": "006bf5e4",
      "incomplete_value": false,
      "site": "006bf5f0",
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
            "const:1e8:8"
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
      "006bf5d0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "006bf5dc",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bf5e4",
      "PARAM",
      [
        "storage",
        "00bf61e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006bf5d0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006bf5dc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006bf5e4",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bf5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bf/006bf5a0.md#insn-006bf5d0) · [`006bf5dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bf/006bf5a0.md#insn-006bf5dc) · [`006bf5e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bf/006bf5a0.md#insn-006bf5e4)
- 新版 [`006bf5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bf/006bf5a0.md#insn-006bf5d0) · [`006bf5dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bf/006bf5a0.md#insn-006bf5dc) · [`006bf5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bf/006bf5a0.md#insn-006bf5e4)

~~~diff
- 006bf5d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 006bf5d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006bf5d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006bf5d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006bf5d0 bytes 08dd44f9
+ 006bf5d0 bytes 083d45f9
- 006bf5dc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 006bf5dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006bf5dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006bf5dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006bf5dc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006bf5dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006bf5dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006bf5dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006bf5dc bytes 21603691
+ 006bf5dc bytes 21203991
- 006bf5e4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 006bf5e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006bf5e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006bf5e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006bf5e4 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006bf5e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006bf5e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006bf5e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006bf5e4 bytes 42a00791
+ 006bf5e4 bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b37ea77212284e779258d0affa9b4aa9"></a>

### [`006c0060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0060.md) → [`006c0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0060.md) FUN_006c0060

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006cec14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ce/006cec14.md) · 呼出先 13件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00448034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448034.md)
- 新版 呼出元 1件 [`006cec14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006cec14.md) · 呼出先 13件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.29% / 新版 99.29%

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
      "definition_site": "006c00a0",
      "incomplete_value": true,
      "site": "006c00a0",
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
      "definition_site": "006c00a0",
      "incomplete_value": true,
      "site": "006c00a0",
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
      "definition_site": "006c00a8",
      "incomplete_value": false,
      "site": "006c00bc",
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
      "definition_site": "006c00a8",
      "incomplete_value": false,
      "site": "006c00bc",
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
      "definition_site": "006c00b0",
      "incomplete_value": false,
      "site": "006c00bc",
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
    "old": {
      "definition_site": "006c00b0",
      "incomplete_value": false,
      "site": "006c00bc",
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
            "const:1e8:8"
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
      "006c009c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "006c00a8",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c00b0",
      "PARAM",
      [
        "storage",
        "00bf61e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006c009c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006c00a8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c00b0",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c009c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0060.md#insn-006c009c) · [`006c00a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0060.md#insn-006c00a8) · [`006c00b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0060.md#insn-006c00b0)
- 新版 [`006c009c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0060.md#insn-006c009c) · [`006c00a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0060.md#insn-006c00a8) · [`006c00b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0060.md#insn-006c00b0)

~~~diff
- 006c009c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 006c009c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006c009c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006c009c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006c009c bytes 08dd44f9
+ 006c009c bytes 083d45f9
- 006c00a8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 006c00a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c00a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c00a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c00a8 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006c00a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c00a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c00a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c00a8 bytes 21603691
+ 006c00a8 bytes 21203991
- 006c00b0 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 006c00b0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006c00b0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006c00b0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006c00b0 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006c00b0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006c00b0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006c00b0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006c00b0 bytes 42a00791
+ 006c00b0 bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45df6f100a926628cf581a3d37844cdd"></a>

### [`006c0784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0784.md) → [`006c0784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md) FUN_006c0784

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 8件 [`0068d810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068d/0068d810.md) [`006c077c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c077c.md) [`006c7884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c7/006c7884.md) [`006c86d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c8/006c86d0.md) [`006d1b1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1b1c.md) · 呼出先 52件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md)
- 新版 呼出元 8件 [`0068d810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d810.md) [`006c077c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c077c.md) [`006c7884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c7884.md) [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) [`006d1b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1b1c.md) · 呼出先 52件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.43% / 新版 94.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 48件, `store_destination` 35件, `store_value` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c0da8",
      "incomplete_value": true,
      "site": "006c0db8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "006c0da8",
      "incomplete_value": true,
      "site": "006c0db8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:637:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 60,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c0dbc",
      "incomplete_value": true,
      "site": "006c0dbc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006c0dbc",
      "incomplete_value": true,
      "site": "006c0dbc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 61,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006c2540",
      "incomplete_value": false,
      "site": "006c2540",
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
      "definition_site": "006c2540",
      "incomplete_value": false,
      "site": "006c2540",
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
    "ordinal": 195,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c0958",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "006c09cc",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      "006c0ac8",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "006c0958",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006c09cc",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "006c0ac8",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c0950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0784.md#insn-006c0950) · [`006c0954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0784.md#insn-006c0954) · [`006c09c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0784.md#insn-006c09c8)
- 新版 [`006c0950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md#insn-006c0950) · [`006c0954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md#insn-006c0954) · [`006c09c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md#insn-006c09c8)

~~~diff
- 006c0950 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 006c0950 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 006c0950 bytes 282b0090
+ 006c0950 bytes 282b00b0
- 006c0954 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 006c0954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006c0954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006c0954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006c0954 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 006c0954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006c0954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006c0954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006c0954 bytes 08e13d91
+ 006c0954 bytes 08e10091
- 006c09c8 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 006c09c8 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 006c09c8 bytes 202b0090
+ 006c09c8 bytes 202b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f30a68ce4a531dd7bdbec3018484126d"></a>

### [`006c2f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c2/006c2f8c.md) → [`006c2f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c2/006c2f8c.md) FUN_006c2f8c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006c0784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c0/006c0784.md) [`006c86d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c8/006c86d0.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0044a8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a8d8.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00605f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00605/00605f28.md) [`006f4c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f4/006f4c58.md)
- 新版 呼出元 2件 [`006c0784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c0/006c0784.md) [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00605f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/00605f28.md) [`006f4c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f4/006f4c58.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.05% / 新版 98.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c34f8",
      "incomplete_value": true,
      "site": "006c34f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c34f8",
      "incomplete_value": true,
      "site": "006c34f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 65,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c34fc",
      "incomplete_value": true,
      "site": "006c34fc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006c34fc",
      "incomplete_value": true,
      "site": "006c34fc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 66,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006c304c",
      "incomplete_value": false,
      "site": "006c3054",
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
            "const:342:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c304c",
      "incomplete_value": false,
      "site": "006c3054",
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
            "const:2b5:8"
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
      "006c304c",
      "PARAM",
      [
        "storage",
        "002a02b5",
        null,
        null
      ]
    ],
    [
      "006c30e8",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        null
      ]
    ],
    [
      "006c31c0",
      "PARAM",
      [
        "storage",
        "002a02b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006c304c",
      "PARAM",
      [
        "storage",
        "002a0342",
        null,
        null
      ]
    ],
    [
      "006c30e8",
      "PARAM",
      [
        "storage",
        "0029196e",
        null,
        null
      ]
    ],
    [
      "006c31c0",
      "PARAM",
      [
        "storage",
        "002a0342",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c304c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c2/006c2f8c.md#insn-006c304c) · [`006c30e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c2/006c2f8c.md#insn-006c30e8) · [`006c31c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c2/006c2f8c.md#insn-006c31c0)
- 新版 [`006c304c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c2/006c2f8c.md#insn-006c304c) · [`006c30e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c2/006c2f8c.md#insn-006c30e8) · [`006c31c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c2/006c2f8c.md#insn-006c31c0)

~~~diff
- 006c304c ["COPY", "tmp:0:8", ["const:2b5:8"]]
- 006c304c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c304c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c304c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c304c ["COPY", "tmp:0:8", ["const:342:8"]]
+ 006c304c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c304c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c304c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c304c bytes 21d40a91
+ 006c304c bytes 21080d91
- 006c30e8 ["COPY", "tmp:0:8", ["const:8e1:8"]]
- 006c30e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c30e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c30e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c30e8 ["COPY", "tmp:0:8", ["const:96e:8"]]
+ 006c30e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c30e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c30e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c30e8 bytes 21842391
+ 006c30e8 bytes 21b82591
- 006c31c0 ["COPY", "tmp:0:8", ["const:2b5:8"]]
- 006c31c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c31c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c31c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c31c0 ["COPY", "tmp:0:8", ["const:342:8"]]
+ 006c31c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c31c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c31c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c31c0 bytes 21d40a91
+ 006c31c0 bytes 21080d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0dc4cf59cec9db151f307b62755dbc4"></a>

### [`006c3fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c3/006c3fe0.md) → [`006c3fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c3/006c3fe0.md) FUN_006c3fe0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`006c86d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c8/006c86d0.md) [`006d1400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1400.md) [`006d3c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3c38.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`0069ab88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069a/0069ab88.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) [`006d1400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1400.md) [`006d3c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c38.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0069ab88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069ab88.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006c48c4",
      "incomplete_value": false,
      "site": "006c48e0",
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
      "definition_site": "006c48c4",
      "incomplete_value": false,
      "site": "006c48e0",
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
    "ordinal": 26,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006c48e8",
      "incomplete_value": false,
      "site": "006c48ec",
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
    "old": {
      "definition_site": "006c48e8",
      "incomplete_value": false,
      "site": "006c48ec",
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
            "const:f78:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c4740",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "006c4784",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      "006c4788",
      "READ",
      [
        "storage",
        "00c1adb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006c4740",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006c4784",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "006c4788",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c4738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c3/006c3fe0.md#insn-006c4738) · [`006c473c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c3/006c3fe0.md#insn-006c473c) · [`006c4780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c3/006c3fe0.md#insn-006c4780)
- 新版 [`006c4738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c3/006c3fe0.md#insn-006c4738) · [`006c473c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c3/006c3fe0.md#insn-006c473c) · [`006c4780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c3/006c3fe0.md#insn-006c4780)

~~~diff
- 006c4738 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 006c4738 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 006c4738 bytes 082b0090
+ 006c4738 bytes 082b00b0
- 006c473c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 006c473c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006c473c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006c473c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006c473c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 006c473c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006c473c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006c473c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006c473c bytes 08e13d91
+ 006c473c bytes 08e10091
- 006c4780 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 006c4780 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 006c4780 bytes 002b0090
+ 006c4780 bytes 002b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71ee73767ac7030e035168b8869b7197"></a>

### [`006c4ea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c4/006c4ea8.md) → [`006c4ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c4/006c4ea8.md) FUN_006c4ea8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c8/006c86d0.md) · 呼出先 18件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`0044a8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a8d8.md) [`006b1fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b1/006b1fac.md) [`006ba5ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ba/006ba5ec.md) [`006bacc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ba/006bacc8.md)
- 新版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) · 呼出先 18件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`006b1fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b1fac.md) [`006ba5ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006ba5ec.md) [`006bacc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ba/006bacc8.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.05% / 新版 97.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c52ac",
      "incomplete_value": false,
      "site": "006c52b4",
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
            "const:e12:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c52ac",
      "incomplete_value": false,
      "site": "006c52b4",
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
            "const:d85:8"
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
      "definition_site": "006c52d0",
      "incomplete_value": false,
      "site": "006c52dc",
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
            "const:9a1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c52d0",
      "incomplete_value": false,
      "site": "006c52dc",
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
            "const:99b:8"
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
      "definition_site": "006c52f4",
      "incomplete_value": false,
      "site": "006c52fc",
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
            "const:742:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c52f4",
      "incomplete_value": false,
      "site": "006c52fc",
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
            "const:6b5:8"
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
      "006c4fcc",
      "DATA",
      [
        "storage",
        "00c23ee8",
        null,
        null
      ]
    ],
    [
      "006c5270",
      "DATA",
      [
        "storage",
        "00c23ed8",
        null,
        null
      ]
    ],
    [
      "006c52b4",
      "DATA",
      [
        "storage",
        "00297d85",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006c4fcc",
      "DATA",
      [
        "storage",
        "00c23f98",
        null,
        null
      ]
    ],
    [
      "006c5270",
      "DATA",
      [
        "storage",
        "00c23f88",
        null,
        null
      ]
    ],
    [
      "006c52b4",
      "DATA",
      [
        "storage",
        "00297e12",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c4fc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c4/006c4ea8.md#insn-006c4fc0) · [`006c5264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c4/006c4ea8.md#insn-006c5264) · [`006c52ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c4/006c4ea8.md#insn-006c52ac)
- 新版 [`006c4fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c4/006c4ea8.md#insn-006c4fc0) · [`006c5264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c4/006c4ea8.md#insn-006c5264) · [`006c52ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c4/006c4ea8.md#insn-006c52ac)

~~~diff
- 006c4fc0 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 006c4fc0 ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
- 006c4fc0 ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
- 006c4fc0 ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
+ 006c4fc0 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 006c4fc0 ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
+ 006c4fc0 ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
+ 006c4fc0 ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
- 006c4fc0 bytes 7ba33b91
+ 006c4fc0 bytes 7b633e91
- 006c5264 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 006c5264 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006c5264 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006c5264 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006c5264 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 006c5264 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006c5264 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006c5264 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006c5264 bytes 29013c91
+ 006c5264 bytes 29c13e91
- 006c52ac ["COPY", "tmp:0:8", ["const:d85:8"]]
- 006c52ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006c52ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006c52ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006c52ac ["COPY", "tmp:0:8", ["const:e12:8"]]
+ 006c52ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006c52ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006c52ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006c52ac bytes 08153691
+ 006c52ac bytes 08493891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-627a5b8c354183e6817e1cfcdb2dce81"></a>

### [`006c5940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c5/006c5940.md) → [`006c5940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c5/006c5940.md) FUN_006c5940

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006d4810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4810.md) · 呼出先 25件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a8/005a83e4.md)
- 新版 呼出元 1件 [`006d4810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4810.md) · 呼出先 25件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.53% / 新版 93.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c59d4",
      "incomplete_value": true,
      "site": "006c59e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:751:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c59d4",
      "incomplete_value": true,
      "site": "006c59e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c59ec",
      "incomplete_value": true,
      "site": "006c59ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006c59ec",
      "incomplete_value": true,
      "site": "006c59ec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c5a00",
      "incomplete_value": false,
      "site": "006c5a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c5a00",
      "incomplete_value": false,
      "site": "006c5a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "006c59d4",
      "READ",
      [
        "storage",
        "0029e6c4",
        null,
        "string"
      ]
    ],
    [
      "006c59dc",
      "READ",
      [
        "storage",
        "0029e6d1",
        null,
        "string"
      ]
    ],
    [
      "006c5a08",
      "DATA",
      [
        "storage",
        "00bf9670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006c59d4",
      "READ",
      [
        "storage",
        "0029e751",
        null,
        "string"
      ]
    ],
    [
      "006c59dc",
      "READ",
      [
        "storage",
        "0029e75e",
        null,
        "string"
      ]
    ],
    [
      "006c5a08",
      "DATA",
      [
        "storage",
        "00bf9720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c59d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c5/006c5940.md#insn-006c59d0) · [`006c5a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c5/006c5940.md#insn-006c5a00) · [`006c5a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c5/006c5940.md#insn-006c5a7c)
- 新版 [`006c59d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c5/006c5940.md#insn-006c59d0) · [`006c5a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c5/006c5940.md#insn-006c5a00) · [`006c5a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c5/006c5940.md#insn-006c5a7c)

~~~diff
- 006c59d0 ["COPY", "tmp:0:8", ["const:6c4:8"]]
- 006c59d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006c59d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006c59d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006c59d0 ["COPY", "tmp:0:8", ["const:751:8"]]
+ 006c59d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006c59d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006c59d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006c59d0 bytes 29111b91
+ 006c59d0 bytes 29451d91
- 006c5a00 ["COPY", "tmp:0:8", ["const:670:8"]]
- 006c5a00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006c5a00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006c5a00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006c5a00 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 006c5a00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006c5a00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006c5a00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006c5a00 bytes 08c11991
+ 006c5a00 bytes 08811c91
- 006c5a7c ["COPY", "tmp:0:8", ["const:cfb:8"]]
- 006c5a7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006c5a7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006c5a7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006c5a7c ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 006c5a7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006c5a7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006c5a7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006c5a7c bytes 29ed3391
+ 006c5a7c bytes 29213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af585d4a5def1b5ddac62be2c8faa480"></a>

### [`006c6850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c6/006c6850.md) → [`006c6850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c6/006c6850.md) FUN_006c6850

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c7884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c7/006c7884.md) · 呼出先 23件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044b898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c1dc.md)
- 新版 呼出元 1件 [`006c7884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c7884.md) · 呼出先 23件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 13件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c68e0",
      "incomplete_value": true,
      "site": "006c68ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:71e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c68e0",
      "incomplete_value": true,
      "site": "006c68ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:725:8"
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
      "definition_site": "006c68e0",
      "incomplete_value": true,
      "site": "006c68ec",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "006c68e0",
      "incomplete_value": true,
      "site": "006c68ec",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006c6f34",
      "incomplete_value": true,
      "site": "006c6f4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:776:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c6f34",
      "incomplete_value": true,
      "site": "006c6f4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 78,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c6888",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "006c6894",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c689c",
      "PARAM",
      [
        "storage",
        "00bf61e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006c6888",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006c6894",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c689c",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c6888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c6/006c6850.md#insn-006c6888) · [`006c6894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c6/006c6850.md#insn-006c6894) · [`006c689c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c6/006c6850.md#insn-006c689c)
- 新版 [`006c6888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c6/006c6850.md#insn-006c6888) · [`006c6894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c6/006c6850.md#insn-006c6894) · [`006c689c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c6/006c6850.md#insn-006c689c)

~~~diff
- 006c6888 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 006c6888 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006c6888 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006c6888 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006c6888 bytes 08dd44f9
+ 006c6888 bytes 083d45f9
- 006c6894 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 006c6894 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c6894 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c6894 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c6894 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006c6894 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c6894 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c6894 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c6894 bytes 21603691
+ 006c6894 bytes 21203991
- 006c689c ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 006c689c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006c689c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006c689c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006c689c ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006c689c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006c689c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006c689c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006c689c bytes 42a00791
+ 006c689c bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-358db9cc39133b70d060984b8895ddd8"></a>

### [`006c7884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c7/006c7884.md) → [`006c7884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c7884.md) FUN_006c7884

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0068c620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068c/0068c620.md) · 呼出先 37件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044d208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d208.md) [`00469fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469fac.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`0069a9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0069a/0069a9cc.md)
- 新版 呼出元 1件 [`0068c620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c620.md) · 呼出先 37件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d208.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0069a9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a9cc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c7e80",
      "incomplete_value": false,
      "site": "006c7e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c7e80",
      "incomplete_value": false,
      "site": "006c7e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "ordinal": 105,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c8424",
      "incomplete_value": false,
      "site": "006c8424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c8424",
      "incomplete_value": false,
      "site": "006c8424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "ordinal": 144,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006c78cc",
      "incomplete_value": true,
      "site": "006c78cc",
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
      "definition_site": "006c78cc",
      "incomplete_value": true,
      "site": "006c78cc",
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
      "006c78c0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "006c78d4",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c78dc",
      "PARAM",
      [
        "storage",
        "00bf61e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006c78c0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006c78d4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c78dc",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c78c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c7/006c7884.md#insn-006c78c0) · [`006c78d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c7/006c7884.md#insn-006c78d4) · [`006c78dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c7/006c7884.md#insn-006c78dc)
- 新版 [`006c78c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c7884.md#insn-006c78c0) · [`006c78d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c7884.md#insn-006c78d4) · [`006c78dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c7/006c7884.md#insn-006c78dc)

~~~diff
- 006c78c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 006c78c0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006c78c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006c78c0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006c78c0 bytes 00dd44f9
+ 006c78c0 bytes 003d45f9
- 006c78d4 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 006c78d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c78d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c78d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c78d4 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006c78d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c78d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c78d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c78d4 bytes 21603691
+ 006c78d4 bytes 21203991
- 006c78dc ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 006c78dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006c78dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006c78dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006c78dc ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006c78dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006c78dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006c78dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006c78dc bytes 42a00791
+ 006c78dc bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aad0f1418e06d3eac15a8cc1bca0b1bc"></a>

### [`006c86d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c8/006c86d0.md) → [`006c86d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md) FUN_006c86d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0068c7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068c/0068c7d4.md) · 呼出先 141件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041d/0041dfc0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0042cde4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042cde4.md)
- 新版 呼出元 1件 [`0068c7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c7d4.md) · 呼出先 141件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 63件, `store_value` 8件

アドレスに依存する影響 `branch_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006c88f0",
      "incomplete_value": false,
      "site": "006c88f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c88f0",
      "incomplete_value": false,
      "site": "006c88f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:af0:8"
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
      "definition_site": "006c99ac",
      "incomplete_value": false,
      "site": "006c99ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006c99ac",
      "incomplete_value": false,
      "site": "006c99ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "ordinal": 83,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006cb36c",
      "incomplete_value": false,
      "site": "006cb36c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006cb36c",
      "incomplete_value": false,
      "site": "006cb36c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "ordinal": 170,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c8764",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "006c8770",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c8778",
      "PARAM",
      [
        "storage",
        "00bf61e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006c8764",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006c8770",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006c8778",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c8764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c8/006c86d0.md#insn-006c8764) · [`006c8770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c8/006c86d0.md#insn-006c8770) · [`006c8778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c8/006c86d0.md#insn-006c8778)
- 新版 [`006c8764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md#insn-006c8764) · [`006c8770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md#insn-006c8770) · [`006c8778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c8/006c86d0.md#insn-006c8778)

~~~diff
- 006c8764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 006c8764 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006c8764 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006c8764 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006c8764 bytes 00dd44f9
+ 006c8764 bytes 003d45f9
- 006c8770 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 006c8770 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006c8770 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006c8770 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006c8770 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006c8770 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006c8770 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006c8770 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006c8770 bytes 21603691
+ 006c8770 bytes 21203991
- 006c8778 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 006c8778 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006c8778 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006c8778 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006c8778 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006c8778 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006c8778 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006c8778 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006c8778 bytes 42a00791
+ 006c8778 bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3364c940efbea8909506cb08bac4bfee"></a>

### [`006cec14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ce/006cec14.md) → [`006cec14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006cec14.md) FUN_006cec14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068d/0068d0f8.md) · 呼出先 30件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md)
- 新版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md) · 呼出先 30件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md)

変更の種類 branch_value, call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.97% / 新版 97.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006cec60",
      "incomplete_value": true,
      "site": "006cec60",
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
      "definition_site": "006cec60",
      "incomplete_value": true,
      "site": "006cec60",
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
      "definition_site": "006cec68",
      "incomplete_value": false,
      "site": "006cec78",
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
      "definition_site": "006cec68",
      "incomplete_value": false,
      "site": "006cec78",
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
      "definition_site": "006cec70",
      "incomplete_value": false,
      "site": "006cec78",
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
    "old": {
      "definition_site": "006cec70",
      "incomplete_value": false,
      "site": "006cec78",
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
            "const:1e8:8"
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
      "006cec4c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "006cec68",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006cec70",
      "PARAM",
      [
        "storage",
        "00bf61e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "006cec4c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006cec68",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006cec70",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006cec4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ce/006cec14.md#insn-006cec4c) · [`006cec68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ce/006cec14.md#insn-006cec68) · [`006cec70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ce/006cec14.md#insn-006cec70)
- 新版 [`006cec4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006cec14.md#insn-006cec4c) · [`006cec68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006cec14.md#insn-006cec68) · [`006cec70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ce/006cec14.md#insn-006cec70)

~~~diff
- 006cec4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 006cec4c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006cec4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006cec4c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006cec4c bytes 00dd44f9
+ 006cec4c bytes 003d45f9
- 006cec68 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 006cec68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006cec68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006cec68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006cec68 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006cec68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006cec68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006cec68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006cec68 bytes 21603691
+ 006cec68 bytes 21203991
- 006cec70 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 006cec70 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 006cec70 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 006cec70 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 006cec70 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006cec70 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 006cec70 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 006cec70 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 006cec70 bytes 42a00791
+ 006cec70 bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c7eb745d21b7aa14ec84115d82b0904"></a>

### [`006d00e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d0/006d00e4.md) → [`006d00e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d00e4.md) FUN_006d00e4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006b0db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0db0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`006b0db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0db0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "006d00f0",
      "incomplete_value": false,
      "site": "006d00f4",
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
      "definition_site": "006d00f0",
      "incomplete_value": false,
      "site": "006d00f4",
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
      "006d00f0",
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
      "006d00f0",
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

- 旧版 [`006d00f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d0/006d00e4.md#insn-006d00f0)
- 新版 [`006d00f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d00e4.md#insn-006d00f0)

~~~diff
- 006d00f0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 006d00f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006d00f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006d00f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006d00f0 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 006d00f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006d00f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006d00f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006d00f0 bytes 00280c91
+ 006d00f0 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddc72088899d4cfd8f03ef134750b1fc"></a>

### [`006d00fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d0/006d00fc.md) → [`006d00fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d00fc.md) FUN_006d00fc

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
      "definition_site": "006d0120",
      "incomplete_value": false,
      "site": "006d0120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d0120",
      "incomplete_value": false,
      "site": "006d0120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "006d0120",
      "DATA",
      [
        "storage",
        "00bf92f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d0120",
      "DATA",
      [
        "storage",
        "00bf93a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d011c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d0/006d00fc.md#insn-006d011c)
- 新版 [`006d011c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d00fc.md#insn-006d011c)

~~~diff
- 006d011c ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 006d011c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d011c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d011c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d011c ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 006d011c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d011c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d011c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d011c bytes 08c10b91
+ 006d011c bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45d341e6aba94d93cdd68203a68d8f00"></a>

### [`006d0130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d0/006d0130.md) → [`006d0130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d0130.md) FUN_006d0130

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
      "definition_site": "006d013c",
      "incomplete_value": false,
      "site": "006d013c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d013c",
      "incomplete_value": false,
      "site": "006d013c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "006d013c",
      "DATA",
      [
        "storage",
        "00bf92f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d013c",
      "DATA",
      [
        "storage",
        "00bf93a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d0/006d0130.md#insn-006d0138)
- 新版 [`006d0138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d0130.md#insn-006d0138)

~~~diff
- 006d0138 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 006d0138 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d0138 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d0138 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d0138 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 006d0138 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d0138 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d0138 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d0138 bytes 29c10b91
+ 006d0138 bytes 29810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26fe460b1a625f669721bad62bf79061"></a>

### [`006d01e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d0/006d01e8.md) → [`006d01e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d01e8.md) FUN_006d01e8

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
      "definition_site": "006d020c",
      "incomplete_value": false,
      "site": "006d020c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d020c",
      "incomplete_value": false,
      "site": "006d020c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "006d020c",
      "DATA",
      [
        "storage",
        "00bf9370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d020c",
      "DATA",
      [
        "storage",
        "00bf9420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d0/006d01e8.md#insn-006d0208)
- 新版 [`006d0208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d01e8.md#insn-006d0208)

~~~diff
- 006d0208 ["COPY", "tmp:0:8", ["const:370:8"]]
- 006d0208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d0208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d0208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d0208 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 006d0208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d0208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d0208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d0208 bytes 08c10d91
+ 006d0208 bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58e91737bc5df9738a4ad233c975fa8b"></a>

### [`006d021c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d0/006d021c.md) → [`006d021c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d021c.md) FUN_006d021c

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
      "definition_site": "006d0228",
      "incomplete_value": false,
      "site": "006d0228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d0228",
      "incomplete_value": false,
      "site": "006d0228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "006d0228",
      "DATA",
      [
        "storage",
        "00bf9370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d0228",
      "DATA",
      [
        "storage",
        "00bf9420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d0/006d021c.md#insn-006d0224)
- 新版 [`006d0224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d021c.md#insn-006d0224)

~~~diff
- 006d0224 ["COPY", "tmp:0:8", ["const:370:8"]]
- 006d0224 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d0224 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d0224 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d0224 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 006d0224 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d0224 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d0224 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d0224 bytes 29c10d91
+ 006d0224 bytes 29811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46e0e0f0499b6978f47831001df2f1dc"></a>

### [`006d02ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d0/006d02ec.md) → [`006d02ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d02ec.md) FUN_006d02ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006b1d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b1/006b1d70.md) [`006b1fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b1/006b1fac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`006b1d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b1d70.md) [`006b1fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b1fac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "006d02f8",
      "incomplete_value": false,
      "site": "006d02fc",
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
      "definition_site": "006d02f8",
      "incomplete_value": false,
      "site": "006d02fc",
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
      "006d02f8",
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
      "006d02f8",
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

- 旧版 [`006d02f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d0/006d02ec.md#insn-006d02f8)
- 新版 [`006d02f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d0/006d02ec.md#insn-006d02f8)

~~~diff
- 006d02f8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 006d02f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006d02f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006d02f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006d02f8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 006d02f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006d02f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006d02f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006d02f8 bytes 00280c91
+ 006d02f8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac7b2422a54f798e4a886b0f53139bc7"></a>

### [`006d12f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d12f4.md) → [`006d12f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d12f4.md) FUN_006d12f4

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
      "definition_site": "006d1308",
      "incomplete_value": false,
      "site": "006d130c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1308",
      "incomplete_value": false,
      "site": "006d130c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "006d130c",
      "DATA",
      [
        "storage",
        "00bf93f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d130c",
      "DATA",
      [
        "storage",
        "00bf94a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d12f4.md#insn-006d1308)
- 新版 [`006d1308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d12f4.md#insn-006d1308)

~~~diff
- 006d1308 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 006d1308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d1308 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 006d1308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1308 bytes 08c10f91
+ 006d1308 bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f95d3245f52378af5f50c75404d2e071"></a>

### [`006d1318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1318.md) → [`006d1318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1318.md) FUN_006d1318

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
      "definition_site": "006d131c",
      "incomplete_value": false,
      "site": "006d1320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d131c",
      "incomplete_value": false,
      "site": "006d1320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "006d1320",
      "DATA",
      [
        "storage",
        "00bf93f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1320",
      "DATA",
      [
        "storage",
        "00bf94a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d131c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1318.md#insn-006d131c)
- 新版 [`006d131c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1318.md#insn-006d131c)

~~~diff
- 006d131c ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 006d131c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d131c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d131c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d131c ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 006d131c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d131c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d131c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d131c bytes 08c10f91
+ 006d131c bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14ecb0f6431bf66ff25791aa74f933cb"></a>

### [`006d1398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1398.md) → [`006d1398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1398.md) FUN_006d1398

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
      "definition_site": "006d13bc",
      "incomplete_value": false,
      "site": "006d13c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d13bc",
      "incomplete_value": false,
      "site": "006d13c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "006d13c0",
      "DATA",
      [
        "storage",
        "00bf9470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d13c0",
      "DATA",
      [
        "storage",
        "00bf9520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d13bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1398.md#insn-006d13bc)
- 新版 [`006d13bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1398.md#insn-006d13bc)

~~~diff
- 006d13bc ["COPY", "tmp:0:8", ["const:470:8"]]
- 006d13bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d13bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d13bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d13bc ["COPY", "tmp:0:8", ["const:520:8"]]
+ 006d13bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d13bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d13bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d13bc bytes 08c11191
+ 006d13bc bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a610b44aa1ca156dbc84a35bb9c44d15"></a>

### [`006d13d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d13d8.md) → [`006d13d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d13d8.md) FUN_006d13d8

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
      "definition_site": "006d13dc",
      "incomplete_value": false,
      "site": "006d13e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d13dc",
      "incomplete_value": false,
      "site": "006d13e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "006d13e0",
      "DATA",
      [
        "storage",
        "00bf9470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d13e0",
      "DATA",
      [
        "storage",
        "00bf9520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d13dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d13d8.md#insn-006d13dc)
- 新版 [`006d13dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d13d8.md#insn-006d13dc)

~~~diff
- 006d13dc ["COPY", "tmp:0:8", ["const:470:8"]]
- 006d13dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d13dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d13dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d13dc ["COPY", "tmp:0:8", ["const:520:8"]]
+ 006d13dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d13dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d13dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d13dc bytes 08c11191
+ 006d13dc bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0762719cfc6b6181fa8731e29aa1afda"></a>

### [`006d1400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1400.md) → [`006d1400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1400.md) FUN_006d1400

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.56% / 新版 96.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d1524",
      "incomplete_value": true,
      "site": "006d1538",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:73a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1524",
      "incomplete_value": true,
      "site": "006d1538",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:741:8"
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
      "definition_site": "006d1584",
      "incomplete_value": true,
      "site": "006d1584",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1584",
      "incomplete_value": true,
      "site": "006d1584",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bdc:8"
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
      "definition_site": "006d1588",
      "incomplete_value": true,
      "site": "006d1588",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006d1588",
      "incomplete_value": true,
      "site": "006d1588",
      "value": [
        "LOAD",
        "8",
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
      "006d1524",
      "READ",
      [
        "storage",
        "002a3741",
        null,
        "string"
      ]
    ],
    [
      "006d1570",
      "READ",
      [
        "storage",
        "002acbdc",
        null,
        "string"
      ]
    ],
    [
      "006d1578",
      "READ",
      [
        "storage",
        "002acbe1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006d1524",
      "READ",
      [
        "storage",
        "002a373a",
        null,
        "string"
      ]
    ],
    [
      "006d1570",
      "READ",
      [
        "storage",
        "002acbd3",
        null,
        "string"
      ]
    ],
    [
      "006d1578",
      "READ",
      [
        "storage",
        "002acbd8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d151c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1400.md#insn-006d151c) · [`006d156c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1400.md#insn-006d156c) · [`006d1740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1400.md#insn-006d1740)
- 新版 [`006d151c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1400.md#insn-006d151c) · [`006d156c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1400.md#insn-006d156c) · [`006d1740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1400.md#insn-006d1740)

~~~diff
- 006d151c ["COPY", "tmp:0:8", ["const:741:8"]]
- 006d151c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d151c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d151c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d151c ["COPY", "tmp:0:8", ["const:73a:8"]]
+ 006d151c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d151c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d151c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d151c bytes 29051d91
+ 006d151c bytes 29e91c91
- 006d156c ["COPY", "tmp:0:8", ["const:bdc:8"]]
- 006d156c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d156c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d156c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d156c ["COPY", "tmp:0:8", ["const:bd3:8"]]
+ 006d156c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d156c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d156c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d156c bytes 29712f91
+ 006d156c bytes 294d2f91
- 006d1740 ["COPY", "tmp:0:8", ["const:855:8"]]
- 006d1740 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006d1740 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006d1740 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006d1740 ["COPY", "tmp:0:8", ["const:85b:8"]]
+ 006d1740 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006d1740 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006d1740 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006d1740 bytes 21542191
+ 006d1740 bytes 216c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d72444d19f58f9ffe7bd07f4c3de368d"></a>

### [`006d1acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1acc.md) → [`006d1acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1acc.md) FUN_006d1acc

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
      "definition_site": "006d1af0",
      "incomplete_value": false,
      "site": "006d1af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:590:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1af0",
      "incomplete_value": false,
      "site": "006d1af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "006d1af0",
      "DATA",
      [
        "storage",
        "00bf94e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1af0",
      "DATA",
      [
        "storage",
        "00bf9590",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1acc.md#insn-006d1aec)
- 新版 [`006d1aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1acc.md#insn-006d1aec)

~~~diff
- 006d1aec ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 006d1aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d1aec ["COPY", "tmp:0:8", ["const:590:8"]]
+ 006d1aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1aec bytes 08811391
+ 006d1aec bytes 08411691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99b762366ab144e099420e7c12e55935"></a>

### [`006d1b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1b00.md) → [`006d1b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1b00.md) FUN_006d1b00

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
      "definition_site": "006d1b0c",
      "incomplete_value": false,
      "site": "006d1b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:590:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1b0c",
      "incomplete_value": false,
      "site": "006d1b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
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
      "006d1b0c",
      "DATA",
      [
        "storage",
        "00bf94e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1b0c",
      "DATA",
      [
        "storage",
        "00bf9590",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1b00.md#insn-006d1b08)
- 新版 [`006d1b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1b00.md#insn-006d1b08)

~~~diff
- 006d1b08 ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 006d1b08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d1b08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d1b08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d1b08 ["COPY", "tmp:0:8", ["const:590:8"]]
+ 006d1b08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d1b08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d1b08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d1b08 bytes 29811391
+ 006d1b08 bytes 29411691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5a9658433cb986b246d5ea8d70b26d8"></a>

### [`006d1c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1c44.md) → [`006d1c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1c44.md) FUN_006d1c44

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
      "definition_site": "006d1c64",
      "incomplete_value": false,
      "site": "006d1c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1c64",
      "incomplete_value": false,
      "site": "006d1c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "006d1c68",
      "DATA",
      [
        "storage",
        "00bf9570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1c68",
      "DATA",
      [
        "storage",
        "00bf9620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1c64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1c44.md#insn-006d1c64)
- 新版 [`006d1c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1c44.md#insn-006d1c64)

~~~diff
- 006d1c64 ["COPY", "tmp:0:8", ["const:570:8"]]
- 006d1c64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1c64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1c64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d1c64 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 006d1c64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1c64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1c64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1c64 bytes 08c11591
+ 006d1c64 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5353021848d5e00e4aaf1300b4c62777"></a>

### [`006d1c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1c7c.md) → [`006d1c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1c7c.md) FUN_006d1c7c

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
      "definition_site": "006d1c80",
      "incomplete_value": false,
      "site": "006d1c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1c80",
      "incomplete_value": false,
      "site": "006d1c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "006d1c84",
      "DATA",
      [
        "storage",
        "00bf9570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1c84",
      "DATA",
      [
        "storage",
        "00bf9620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1c7c.md#insn-006d1c80)
- 新版 [`006d1c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1c7c.md#insn-006d1c80)

~~~diff
- 006d1c80 ["COPY", "tmp:0:8", ["const:570:8"]]
- 006d1c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d1c80 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 006d1c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1c80 bytes 08c11591
+ 006d1c80 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0be1d4558f7cc736652837383211a3e0"></a>

### [`006d1e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1e68.md) → [`006d1e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1e68.md) FUN_006d1e68

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
      "definition_site": "006d1e8c",
      "incomplete_value": false,
      "site": "006d1e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1e8c",
      "incomplete_value": false,
      "site": "006d1e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "006d1e8c",
      "DATA",
      [
        "storage",
        "00bf95f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1e8c",
      "DATA",
      [
        "storage",
        "00bf96a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1e68.md#insn-006d1e88)
- 新版 [`006d1e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1e68.md#insn-006d1e88)

~~~diff
- 006d1e88 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 006d1e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d1e88 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 006d1e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d1e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1e88 bytes 08c11791
+ 006d1e88 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a16a59f397211ab21cd6f5897973f12b"></a>

### [`006d1e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1e9c.md) → [`006d1e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1e9c.md) FUN_006d1e9c

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
      "definition_site": "006d1ea8",
      "incomplete_value": false,
      "site": "006d1ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1ea8",
      "incomplete_value": false,
      "site": "006d1ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "006d1ea8",
      "DATA",
      [
        "storage",
        "00bf95f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d1ea8",
      "DATA",
      [
        "storage",
        "00bf96a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d1/006d1e9c.md#insn-006d1ea4)
- 新版 [`006d1ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d1/006d1e9c.md#insn-006d1ea4)

~~~diff
- 006d1ea4 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 006d1ea4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d1ea4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d1ea4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d1ea4 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 006d1ea4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d1ea4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d1ea4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d1ea4 bytes 29c11791
+ 006d1ea4 bytes 29811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32d2054c4a66f96ed74abdb2cc4cf5c2"></a>

### [`006d3b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3b28.md) → [`006d3b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3b28.md) FUN_006d3b28

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
      "definition_site": "006d3b3c",
      "incomplete_value": false,
      "site": "006d3b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3b3c",
      "incomplete_value": false,
      "site": "006d3b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "006d3b40",
      "DATA",
      [
        "storage",
        "00bf9670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d3b40",
      "DATA",
      [
        "storage",
        "00bf9720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3b28.md#insn-006d3b3c)
- 新版 [`006d3b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3b28.md#insn-006d3b3c)

~~~diff
- 006d3b3c ["COPY", "tmp:0:8", ["const:670:8"]]
- 006d3b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d3b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d3b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d3b3c ["COPY", "tmp:0:8", ["const:720:8"]]
+ 006d3b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d3b3c bytes 08c11991
+ 006d3b3c bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52f13ba40774a61d1500f424f8c4dc4b"></a>

### [`006d3b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3b4c.md) → [`006d3b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3b4c.md) FUN_006d3b4c

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
      "definition_site": "006d3b50",
      "incomplete_value": false,
      "site": "006d3b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3b50",
      "incomplete_value": false,
      "site": "006d3b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "006d3b54",
      "DATA",
      [
        "storage",
        "00bf9670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d3b54",
      "DATA",
      [
        "storage",
        "00bf9720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3b50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3b4c.md#insn-006d3b50)
- 新版 [`006d3b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3b4c.md#insn-006d3b50)

~~~diff
- 006d3b50 ["COPY", "tmp:0:8", ["const:670:8"]]
- 006d3b50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d3b50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d3b50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d3b50 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 006d3b50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3b50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3b50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d3b50 bytes 08c11991
+ 006d3b50 bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9409e82d5c650f0082c37e926d52c3b"></a>

### [`006d3bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3bd0.md) → [`006d3bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3bd0.md) FUN_006d3bd0

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
      "definition_site": "006d3bf4",
      "incomplete_value": false,
      "site": "006d3bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3bf4",
      "incomplete_value": false,
      "site": "006d3bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "006d3bf8",
      "DATA",
      [
        "storage",
        "00bf96f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d3bf8",
      "DATA",
      [
        "storage",
        "00bf97a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3bd0.md#insn-006d3bf4)
- 新版 [`006d3bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3bd0.md#insn-006d3bf4)

~~~diff
- 006d3bf4 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 006d3bf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d3bf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d3bf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d3bf4 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 006d3bf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3bf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3bf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d3bf4 bytes 08c11b91
+ 006d3bf4 bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcabc6a7a66e61fc5643fab79671b802"></a>

### [`006d3c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3c10.md) → [`006d3c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c10.md) FUN_006d3c10

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
      "definition_site": "006d3c14",
      "incomplete_value": false,
      "site": "006d3c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3c14",
      "incomplete_value": false,
      "site": "006d3c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "006d3c18",
      "DATA",
      [
        "storage",
        "00bf96f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d3c18",
      "DATA",
      [
        "storage",
        "00bf97a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3c10.md#insn-006d3c14)
- 新版 [`006d3c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c10.md#insn-006d3c14)

~~~diff
- 006d3c14 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 006d3c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d3c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d3c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d3c14 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 006d3c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d3c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d3c14 bytes 08c11b91
+ 006d3c14 bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78e92820935e2b1f9384523fb594b16c"></a>

### [`006d3c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3c38.md) → [`006d3c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c38.md) FUN_006d3c38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.53% / 新版 94.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d3d3c",
      "incomplete_value": true,
      "site": "006d3d50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:73a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3d3c",
      "incomplete_value": true,
      "site": "006d3d50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:741:8"
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
      "definition_site": "006d3d90",
      "incomplete_value": true,
      "site": "006d3d90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3d90",
      "incomplete_value": true,
      "site": "006d3d90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bdc:8"
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
      "definition_site": "006d3d94",
      "incomplete_value": true,
      "site": "006d3d94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006d3d94",
      "incomplete_value": true,
      "site": "006d3d94",
      "value": [
        "LOAD",
        "8",
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
      "006d3d3c",
      "READ",
      [
        "storage",
        "002a3741",
        null,
        "string"
      ]
    ],
    [
      "006d3d7c",
      "READ",
      [
        "storage",
        "002acbdc",
        null,
        "string"
      ]
    ],
    [
      "006d3d84",
      "READ",
      [
        "storage",
        "002acbe1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006d3d3c",
      "READ",
      [
        "storage",
        "002a373a",
        null,
        "string"
      ]
    ],
    [
      "006d3d7c",
      "READ",
      [
        "storage",
        "002acbd3",
        null,
        "string"
      ]
    ],
    [
      "006d3d84",
      "READ",
      [
        "storage",
        "002acbd8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3d34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3c38.md#insn-006d3d34) · [`006d3d78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3c38.md#insn-006d3d78) · [`006d3e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d3/006d3c38.md#insn-006d3e60)
- 新版 [`006d3d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c38.md#insn-006d3d34) · [`006d3d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c38.md#insn-006d3d78) · [`006d3e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d3/006d3c38.md#insn-006d3e60)

~~~diff
- 006d3d34 ["COPY", "tmp:0:8", ["const:741:8"]]
- 006d3d34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d3d34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d3d34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d3d34 ["COPY", "tmp:0:8", ["const:73a:8"]]
+ 006d3d34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d3d34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d3d34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d3d34 bytes 29051d91
+ 006d3d34 bytes 29e91c91
- 006d3d78 ["COPY", "tmp:0:8", ["const:bdc:8"]]
- 006d3d78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d3d78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d3d78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d3d78 ["COPY", "tmp:0:8", ["const:bd3:8"]]
+ 006d3d78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d3d78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d3d78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d3d78 bytes 29712f91
+ 006d3d78 bytes 294d2f91
- 006d3e60 ["COPY", "tmp:0:8", ["const:b86:8"]]
- 006d3e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d3e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d3e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d3e60 ["COPY", "tmp:0:8", ["const:c13:8"]]
+ 006d3e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d3e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d3e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d3e60 bytes 29192e91
+ 006d3e60 bytes 294d3091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f53eedc5e10438054a47c1f9cc1deae0"></a>

### [`006d4344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4344.md) → [`006d4344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4344.md) FUN_006d4344

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
      "definition_site": "006d4364",
      "incomplete_value": false,
      "site": "006d4368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4364",
      "incomplete_value": false,
      "site": "006d4368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "006d4368",
      "DATA",
      [
        "storage",
        "00bf9760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4368",
      "DATA",
      [
        "storage",
        "00bf9810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4344.md#insn-006d4364)
- 新版 [`006d4364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4344.md#insn-006d4364)

~~~diff
- 006d4364 ["COPY", "tmp:0:8", ["const:760:8"]]
- 006d4364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4364 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 006d4364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4364 bytes 08811d91
+ 006d4364 bytes 08412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abfa5129c617190b2d75a28032dcf097"></a>

### [`006d437c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d437c.md) → [`006d437c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d437c.md) FUN_006d437c

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
      "definition_site": "006d4380",
      "incomplete_value": false,
      "site": "006d4384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4380",
      "incomplete_value": false,
      "site": "006d4384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "006d4384",
      "DATA",
      [
        "storage",
        "00bf9760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4384",
      "DATA",
      [
        "storage",
        "00bf9810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d437c.md#insn-006d4380)
- 新版 [`006d4380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d437c.md#insn-006d4380)

~~~diff
- 006d4380 ["COPY", "tmp:0:8", ["const:760:8"]]
- 006d4380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4380 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 006d4380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4380 bytes 08811d91
+ 006d4380 bytes 08412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33630248569fd1cf0bcff4d7b836e243"></a>

### [`006d447c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d447c.md) → [`006d447c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d447c.md) FUN_006d447c

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
      "definition_site": "006d449c",
      "incomplete_value": false,
      "site": "006d44a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d449c",
      "incomplete_value": false,
      "site": "006d44a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
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
      "006d44a0",
      "DATA",
      [
        "storage",
        "00bf97f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d44a0",
      "DATA",
      [
        "storage",
        "00bf98a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d449c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d447c.md#insn-006d449c)
- 新版 [`006d449c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d447c.md#insn-006d449c)

~~~diff
- 006d449c ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 006d449c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d449c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d449c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d449c ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 006d449c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d449c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d449c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d449c bytes 08c11f91
+ 006d449c bytes 08812291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-869389bd50b5d253c4f75f555293e9ed"></a>

### [`006d44b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d44b4.md) → [`006d44b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d44b4.md) FUN_006d44b4

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
      "definition_site": "006d44b8",
      "incomplete_value": false,
      "site": "006d44bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d44b8",
      "incomplete_value": false,
      "site": "006d44bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
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
      "006d44bc",
      "DATA",
      [
        "storage",
        "00bf97f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d44bc",
      "DATA",
      [
        "storage",
        "00bf98a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d44b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d44b4.md#insn-006d44b8)
- 新版 [`006d44b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d44b4.md#insn-006d44b8)

~~~diff
- 006d44b8 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 006d44b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d44b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d44b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d44b8 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 006d44b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d44b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d44b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d44b8 bytes 08c11f91
+ 006d44b8 bytes 08812291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab2b51ab8bc7685522fe50ce210d0c8f"></a>

### [`006d46a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d46a0.md) → [`006d46a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d46a0.md) FUN_006d46a0

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
      "definition_site": "006d46c0",
      "incomplete_value": false,
      "site": "006d46c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d46c0",
      "incomplete_value": false,
      "site": "006d46c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "006d46c4",
      "DATA",
      [
        "storage",
        "00bf9870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d46c4",
      "DATA",
      [
        "storage",
        "00bf9920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d46c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d46a0.md#insn-006d46c0)
- 新版 [`006d46c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d46a0.md#insn-006d46c0)

~~~diff
- 006d46c0 ["COPY", "tmp:0:8", ["const:870:8"]]
- 006d46c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d46c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d46c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d46c0 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 006d46c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d46c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d46c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d46c0 bytes 08c12191
+ 006d46c0 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-376f07df16dc771fdb7834ca8667170c"></a>

### [`006d46d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d46d8.md) → [`006d46d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d46d8.md) FUN_006d46d8

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
      "definition_site": "006d46dc",
      "incomplete_value": false,
      "site": "006d46e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d46dc",
      "incomplete_value": false,
      "site": "006d46e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "006d46e0",
      "DATA",
      [
        "storage",
        "00bf9870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d46e0",
      "DATA",
      [
        "storage",
        "00bf9920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d46dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d46d8.md#insn-006d46dc)
- 新版 [`006d46dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d46d8.md#insn-006d46dc)

~~~diff
- 006d46dc ["COPY", "tmp:0:8", ["const:870:8"]]
- 006d46dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d46dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d46dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d46dc ["COPY", "tmp:0:8", ["const:920:8"]]
+ 006d46dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d46dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d46dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d46dc bytes 08c12191
+ 006d46dc bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ba7040c757c6fbce4a3e39ea4c0d265"></a>

### [`006d47b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d47b8.md) → [`006d47b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d47b8.md) FUN_006d47b8

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
      "definition_site": "006d47d8",
      "incomplete_value": false,
      "site": "006d47dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d47d8",
      "incomplete_value": false,
      "site": "006d47dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "006d47dc",
      "DATA",
      [
        "storage",
        "00bf98f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d47dc",
      "DATA",
      [
        "storage",
        "00bf99a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d47d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d47b8.md#insn-006d47d8)
- 新版 [`006d47d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d47b8.md#insn-006d47d8)

~~~diff
- 006d47d8 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 006d47d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d47d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d47d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d47d8 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 006d47d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d47d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d47d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d47d8 bytes 08c12391
+ 006d47d8 bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-179fa241ae68a634b8335ea85e838cb2"></a>

### [`006d47f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d47f0.md) → [`006d47f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d47f0.md) FUN_006d47f0

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
      "definition_site": "006d47f4",
      "incomplete_value": false,
      "site": "006d47f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d47f4",
      "incomplete_value": false,
      "site": "006d47f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "006d47f8",
      "DATA",
      [
        "storage",
        "00bf98f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d47f8",
      "DATA",
      [
        "storage",
        "00bf99a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d47f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d47f0.md#insn-006d47f4)
- 新版 [`006d47f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d47f0.md#insn-006d47f4)

~~~diff
- 006d47f4 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 006d47f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d47f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d47f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d47f4 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 006d47f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d47f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d47f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d47f4 bytes 08c12391
+ 006d47f4 bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8615cd6e898afc2c445f3ac847bb9cc7"></a>

### [`006d4810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4810.md) → [`006d4810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4810.md) FUN_006d4810

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`006bb5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006bb/006bb5d0.md) [`006c5940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006c5/006c5940.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006bb5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006bb/006bb5d0.md) [`006c5940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006c5/006c5940.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.02% / 新版 94.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006d4914",
      "incomplete_value": true,
      "site": "006d4924",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9b7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4914",
      "incomplete_value": true,
      "site": "006d4924",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9b1:8"
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
      "definition_site": "006d4928",
      "incomplete_value": true,
      "site": "006d4928",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006d4928",
      "incomplete_value": true,
      "site": "006d4928",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006d4940",
      "incomplete_value": false,
      "site": "006d4948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4940",
      "incomplete_value": false,
      "site": "006d4948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "006d4914",
      "READ",
      [
        "storage",
        "002aa9b1",
        null,
        "string"
      ]
    ],
    [
      "006d4918",
      "READ",
      [
        "storage",
        "002aa9be",
        null,
        "string"
      ]
    ],
    [
      "006d4948",
      "DATA",
      [
        "storage",
        "00bf9960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4914",
      "READ",
      [
        "storage",
        "002aa9b7",
        null,
        "string"
      ]
    ],
    [
      "006d4918",
      "READ",
      [
        "storage",
        "002aa9c4",
        null,
        "string"
      ]
    ],
    [
      "006d4948",
      "DATA",
      [
        "storage",
        "00bf9a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d490c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4810.md#insn-006d490c) · [`006d4940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4810.md#insn-006d4940)
- 新版 [`006d490c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4810.md#insn-006d490c) · [`006d4940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4810.md#insn-006d4940)

~~~diff
- 006d490c ["COPY", "tmp:0:8", ["const:9b1:8"]]
- 006d490c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d490c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d490c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d490c ["COPY", "tmp:0:8", ["const:9b7:8"]]
+ 006d490c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d490c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d490c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d490c bytes 29c52691
+ 006d490c bytes 29dd2691
- 006d4940 ["COPY", "tmp:0:8", ["const:960:8"]]
- 006d4940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4940 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 006d4940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4940 bytes 08812591
+ 006d4940 bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f227c3728ffddb3894d62b75a6c2b0b5"></a>

### [`006d4aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4aa0.md) → [`006d4aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4aa0.md) FUN_006d4aa0

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
      "definition_site": "006d4ab4",
      "incomplete_value": false,
      "site": "006d4ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4ab4",
      "incomplete_value": false,
      "site": "006d4ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "006d4ab8",
      "DATA",
      [
        "storage",
        "00bf9960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4ab8",
      "DATA",
      [
        "storage",
        "00bf9a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4ab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4aa0.md#insn-006d4ab4)
- 新版 [`006d4ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4aa0.md#insn-006d4ab4)

~~~diff
- 006d4ab4 ["COPY", "tmp:0:8", ["const:960:8"]]
- 006d4ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4ab4 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 006d4ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4ab4 bytes 08812591
+ 006d4ab4 bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfc81fcd35fd5b14c47a002552f639bf"></a>

### [`006d4ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4ac4.md) → [`006d4ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4ac4.md) FUN_006d4ac4

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
      "definition_site": "006d4ac8",
      "incomplete_value": false,
      "site": "006d4acc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4ac8",
      "incomplete_value": false,
      "site": "006d4acc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "006d4acc",
      "DATA",
      [
        "storage",
        "00bf9960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4acc",
      "DATA",
      [
        "storage",
        "00bf9a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4ac4.md#insn-006d4ac8)
- 新版 [`006d4ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4ac4.md#insn-006d4ac8)

~~~diff
- 006d4ac8 ["COPY", "tmp:0:8", ["const:960:8"]]
- 006d4ac8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ac8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ac8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4ac8 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 006d4ac8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4ac8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4ac8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4ac8 bytes 08812591
+ 006d4ac8 bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d8f6c36eb438dd0eeffa77af49d7629"></a>

### [`006d4b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4b48.md) → [`006d4b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4b48.md) FUN_006d4b48

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
      "definition_site": "006d4b68",
      "incomplete_value": false,
      "site": "006d4b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4b68",
      "incomplete_value": false,
      "site": "006d4b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "006d4b6c",
      "DATA",
      [
        "storage",
        "00bf99f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4b6c",
      "DATA",
      [
        "storage",
        "00bf9aa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4b48.md#insn-006d4b68)
- 新版 [`006d4b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4b48.md#insn-006d4b68)

~~~diff
- 006d4b68 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 006d4b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4b68 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 006d4b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4b68 bytes 08c12791
+ 006d4b68 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41f841f54b44dd61b9cf1d8733abfb2d"></a>

### [`006d4b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4b80.md) → [`006d4b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4b80.md) FUN_006d4b80

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
      "definition_site": "006d4b84",
      "incomplete_value": false,
      "site": "006d4b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4b84",
      "incomplete_value": false,
      "site": "006d4b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "006d4b88",
      "DATA",
      [
        "storage",
        "00bf99f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4b88",
      "DATA",
      [
        "storage",
        "00bf9aa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4b84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4b80.md#insn-006d4b84)
- 新版 [`006d4b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4b80.md#insn-006d4b84)

~~~diff
- 006d4b84 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 006d4b84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4b84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4b84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4b84 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 006d4b84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4b84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4b84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4b84 bytes 08c12791
+ 006d4b84 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e487e73537b25dba6c0c9f4aa711642"></a>

### [`006d4f18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4f18.md) → [`006d4f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4f18.md) FUN_006d4f18

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
      "definition_site": "006d4f3c",
      "incomplete_value": false,
      "site": "006d4f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:b10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4f3c",
      "incomplete_value": false,
      "site": "006d4f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "006d4f3c",
      "DATA",
      [
        "storage",
        "00bf9a60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4f3c",
      "DATA",
      [
        "storage",
        "00bf9b10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4f18.md#insn-006d4f38)
- 新版 [`006d4f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4f18.md#insn-006d4f38)

~~~diff
- 006d4f38 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 006d4f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4f38 ["COPY", "tmp:0:8", ["const:b10:8"]]
+ 006d4f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4f38 bytes 08812991
+ 006d4f38 bytes 08412c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d829d35590e33e22470061676de21498"></a>

### [`006d4fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4fd4.md) → [`006d4fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4fd4.md) FUN_006d4fd4

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
      "definition_site": "006d4fe8",
      "incomplete_value": false,
      "site": "006d4fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4fe8",
      "incomplete_value": false,
      "site": "006d4fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:af0:8"
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
      "006d4fec",
      "DATA",
      [
        "storage",
        "00bf9af0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d4fec",
      "DATA",
      [
        "storage",
        "00bf9ba0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4fd4.md#insn-006d4fe8)
- 新版 [`006d4fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4fd4.md#insn-006d4fe8)

~~~diff
- 006d4fe8 ["COPY", "tmp:0:8", ["const:af0:8"]]
- 006d4fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4fe8 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 006d4fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4fe8 bytes 08c12b91
+ 006d4fe8 bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8b346d2eeaf4b0a9bc36e493d16273f"></a>

### [`006d4ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4ff8.md) → [`006d4ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4ff8.md) FUN_006d4ff8

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
      "definition_site": "006d4ffc",
      "incomplete_value": false,
      "site": "006d5000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4ffc",
      "incomplete_value": false,
      "site": "006d5000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:af0:8"
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
      "006d5000",
      "DATA",
      [
        "storage",
        "00bf9af0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d5000",
      "DATA",
      [
        "storage",
        "00bf9ba0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d4/006d4ff8.md#insn-006d4ffc)
- 新版 [`006d4ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d4/006d4ff8.md#insn-006d4ffc)

~~~diff
- 006d4ffc ["COPY", "tmp:0:8", ["const:af0:8"]]
- 006d4ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d4ffc ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 006d4ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d4ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4ffc bytes 08c12b91
+ 006d4ffc bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-942731dc44bc59a6a4c7f00b1793b1e5"></a>

### [`006d507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d5/006d507c.md) → [`006d507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d507c.md) FUN_006d507c

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
      "definition_site": "006d5090",
      "incomplete_value": false,
      "site": "006d5094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d5090",
      "incomplete_value": false,
      "site": "006d5094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "006d5094",
      "DATA",
      [
        "storage",
        "00bf9b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d5094",
      "DATA",
      [
        "storage",
        "00bf9c20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d5090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d5/006d507c.md#insn-006d5090)
- 新版 [`006d5090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d507c.md#insn-006d5090)

~~~diff
- 006d5090 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 006d5090 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d5090 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d5090 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d5090 ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 006d5090 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d5090 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d5090 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d5090 bytes 08c12d91
+ 006d5090 bytes 08813091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54aa8ac8b4c421d81d4d79b374f8dfd3"></a>

### [`006d50a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d5/006d50a0.md) → [`006d50a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d50a0.md) FUN_006d50a0

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
      "definition_site": "006d50a4",
      "incomplete_value": false,
      "site": "006d50a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d50a4",
      "incomplete_value": false,
      "site": "006d50a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "006d50a8",
      "DATA",
      [
        "storage",
        "00bf9b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d50a8",
      "DATA",
      [
        "storage",
        "00bf9c20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d50a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d5/006d50a0.md#insn-006d50a4)
- 新版 [`006d50a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d50a0.md#insn-006d50a4)

~~~diff
- 006d50a4 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 006d50a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d50a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d50a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d50a4 ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 006d50a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d50a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d50a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d50a4 bytes 08c12d91
+ 006d50a4 bytes 08813091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e3866f6eb3f2d3068379633f8010232"></a>

### [`006d51a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d5/006d51a4.md) → [`006d51a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d51a4.md) FUN_006d51a4

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
      "definition_site": "006d51c8",
      "incomplete_value": false,
      "site": "006d51c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d51c8",
      "incomplete_value": false,
      "site": "006d51c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "006d51c8",
      "DATA",
      [
        "storage",
        "00bf9bf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d51c8",
      "DATA",
      [
        "storage",
        "00bf9ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d51c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d5/006d51a4.md#insn-006d51c4)
- 新版 [`006d51c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d51a4.md#insn-006d51c4)

~~~diff
- 006d51c4 ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 006d51c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d51c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d51c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d51c4 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 006d51c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d51c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d51c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d51c4 bytes 08c12f91
+ 006d51c4 bytes 08813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8166a6f65c0d5902d400533a5b98173"></a>

### [`006d51d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d5/006d51d8.md) → [`006d51d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d51d8.md) FUN_006d51d8

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
      "definition_site": "006d51e4",
      "incomplete_value": false,
      "site": "006d51e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d51e4",
      "incomplete_value": false,
      "site": "006d51e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "006d51e4",
      "DATA",
      [
        "storage",
        "00bf9bf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d51e4",
      "DATA",
      [
        "storage",
        "00bf9ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d51e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d5/006d51d8.md#insn-006d51e0)
- 新版 [`006d51e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d51d8.md#insn-006d51e0)

~~~diff
- 006d51e0 ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 006d51e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d51e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d51e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d51e0 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 006d51e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d51e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d51e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d51e0 bytes 29c12f91
+ 006d51e0 bytes 29813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

