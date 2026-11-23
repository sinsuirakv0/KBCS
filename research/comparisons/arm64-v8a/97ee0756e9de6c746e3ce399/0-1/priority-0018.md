# v15.7.2 → v15.7.3 · 最優先の変更候補 (18)

[一覧の目次](README.md)

<a id="compare-39a022d01fa23de7bbdaaa82cede8dd1"></a>

### [`00564940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564940.md) → [`00564940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564940.md) FUN_00564940

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
      "definition_site": "0056494c",
      "incomplete_value": false,
      "site": "0056494c",
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
      "definition_site": "0056494c",
      "incomplete_value": false,
      "site": "0056494c",
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
      "0056494c",
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
      "0056494c",
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

- 旧版 [`00564948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564940.md#insn-00564948)
- 新版 [`00564948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564940.md#insn-00564948)

~~~diff
- 00564948 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 00564948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00564948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00564948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00564948 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 00564948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00564948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00564948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00564948 bytes 29c12891
+ 00564948 bytes 29812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91bf1fc772adca657b11996fc661c90f"></a>

### [`00564ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564ebc.md) → [`00564ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ebc.md) FUN_00564ebc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00564d7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564d7c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00564d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564d7c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00564ec8",
      "incomplete_value": false,
      "site": "00564ecc",
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
      "definition_site": "00564ec8",
      "incomplete_value": false,
      "site": "00564ecc",
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
      "00564ec8",
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
      "00564ec8",
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

- 旧版 [`00564ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564ebc.md#insn-00564ec8)
- 新版 [`00564ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ebc.md#insn-00564ec8)

~~~diff
- 00564ec8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00564ec8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00564ec8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00564ec8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00564ec8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00564ec8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00564ec8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00564ec8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00564ec8 bytes 00280c91
+ 00564ec8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f5f2c9518db186ba99067c4103bddbb"></a>

### [`00564ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564ed0.md) → [`00564ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ed0.md) FUN_00564ed0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0056244c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/0056244c.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`0056244c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/0056244c.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00564eec",
      "incomplete_value": false,
      "site": "00564eec",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564eec",
      "incomplete_value": false,
      "site": "00564eec",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00564ef8",
      "incomplete_value": false,
      "site": "00564ef8",
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
      "definition_site": "00564ef8",
      "incomplete_value": false,
      "site": "00564ef8",
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
      "00564eec",
      "DATA",
      [
        "storage",
        "00befab0",
        null,
        "undefined *"
      ]
    ],
    [
      "00564ef8",
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
      "00564eec",
      "DATA",
      [
        "storage",
        "00befb60",
        null,
        "undefined *"
      ]
    ],
    [
      "00564ef8",
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

- 旧版 [`00564ee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564ed0.md#insn-00564ee4) · [`00564ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564ed0.md#insn-00564ef0)
- 新版 [`00564ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ed0.md#insn-00564ee4) · [`00564ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ed0.md#insn-00564ef0)

~~~diff
- 00564ee4 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00564ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564ee4 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 00564ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564ee4 bytes 08c12a91
+ 00564ee4 bytes 08812d91
- 00564ef0 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 00564ef0 bytes 483400f0
+ 00564ef0 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 00564ef0 bytes 483400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dd65be7538c747a5e3974eb37eadd66"></a>

### [`00564fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564fac.md) → [`00564fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564fac.md) FUN_00564fac

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
      "definition_site": "00564fb0",
      "incomplete_value": false,
      "site": "00564fb4",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564fb0",
      "incomplete_value": false,
      "site": "00564fb4",
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
            "const:ab0:8"
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
      "00564fb4",
      "DATA",
      [
        "storage",
        "00befab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564fb4",
      "DATA",
      [
        "storage",
        "00befb60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564fac.md#insn-00564fb0)
- 新版 [`00564fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564fac.md#insn-00564fb0)

~~~diff
- 00564fb0 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00564fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564fb0 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 00564fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564fb0 bytes 08c12a91
+ 00564fb0 bytes 08812d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6ae1075aa8a6c46f80fc39bd10b3fba"></a>

### [`00564fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564fbc.md) → [`00564fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564fbc.md) FUN_00564fbc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00564fcc",
      "incomplete_value": true,
      "site": "00564fd4",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00564fcc",
      "incomplete_value": true,
      "site": "00564fd4",
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
            "const:ab0:8"
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
      "00564fd4",
      "DATA",
      [
        "storage",
        "00befab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00564fd4",
      "DATA",
      [
        "storage",
        "00befb60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00564fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564fbc.md#insn-00564fcc)
- 新版 [`00564fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564fbc.md#insn-00564fcc)

~~~diff
- 00564fcc ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00564fcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00564fcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00564fcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00564fcc ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 00564fcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00564fcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00564fcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00564fcc bytes 08c12a91
+ 00564fcc bytes 08812d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63b128429935cfb76a33eed5adf3ec2e"></a>

### [`00564ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564ffc.md) → [`00564ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ffc.md) FUN_00564ffc

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
      "definition_site": "00565000",
      "incomplete_value": false,
      "site": "00565004",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565000",
      "incomplete_value": false,
      "site": "00565004",
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
            "const:b00:8"
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
      "00565004",
      "DATA",
      [
        "storage",
        "00befb00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00565004",
      "DATA",
      [
        "storage",
        "00befbb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564ffc.md#insn-00565000)
- 新版 [`00565000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564ffc.md#insn-00565000)

~~~diff
- 00565000 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 00565000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565000 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 00565000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565000 bytes 08012c91
+ 00565000 bytes 08c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28773909eaaee1737e75c555bd0782bb"></a>

### [`0056500c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056500c.md) → [`0056500c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056500c.md) FUN_0056500c

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
      "definition_site": "0056501c",
      "incomplete_value": false,
      "site": "00565024",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056501c",
      "incomplete_value": false,
      "site": "00565024",
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
            "const:b00:8"
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
      "00565024",
      "DATA",
      [
        "storage",
        "00befb00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00565024",
      "DATA",
      [
        "storage",
        "00befbb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056501c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056500c.md#insn-0056501c)
- 新版 [`0056501c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056500c.md#insn-0056501c)

~~~diff
- 0056501c ["COPY", "tmp:0:8", ["const:b00:8"]]
- 0056501c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056501c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056501c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056501c ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 0056501c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056501c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056501c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056501c bytes 08012c91
+ 0056501c bytes 08c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94c421dd30f671b18e2235cac10e95d9"></a>

### [`0056503c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056503c.md) → [`0056503c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056503c.md) FUN_0056503c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005624f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005624f4.md) · 呼出先 2件 [`005641a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/005641a0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`005624f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005624f4.md) · 呼出先 2件 [`005641a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/005641a0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00565050",
      "incomplete_value": false,
      "site": "00565058",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565050",
      "incomplete_value": false,
      "site": "00565058",
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
      "00565058",
      "DATA",
      [
        "storage",
        "00bef7d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565058",
      "DATA",
      [
        "storage",
        "00bef888",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056503c.md#insn-00565050)
- 新版 [`00565050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056503c.md#insn-00565050)

~~~diff
- 00565050 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00565050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565050 ["COPY", "tmp:0:8", ["const:888:8"]]
+ 00565050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565050 bytes 08611f91
+ 00565050 bytes 08212291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69ebe8efad8703247fd78fff358f2f81"></a>

### [`0056508c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056508c.md) → [`0056508c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056508c.md) FUN_0056508c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005624f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005624f4.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`005624f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005624f4.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.80% / 新版 97.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056513c",
      "incomplete_value": false,
      "site": "00565144",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056513c",
      "incomplete_value": false,
      "site": "00565144",
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
            "const:7d8:8"
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
      "00565144",
      "DATA",
      [
        "storage",
        "00bef7d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565144",
      "DATA",
      [
        "storage",
        "00bef888",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056513c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056508c.md#insn-0056513c)
- 新版 [`0056513c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056508c.md#insn-0056513c)

~~~diff
- 0056513c ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0056513c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056513c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056513c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056513c ["COPY", "tmp:0:8", ["const:888:8"]]
+ 0056513c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056513c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056513c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056513c bytes 29611f91
+ 0056513c bytes 29212291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cde40d6ba899ddcc84eaafce4d4f9fc0"></a>

### [`0056547c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056547c.md) → [`0056547c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056547c.md) FUN_0056547c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005627f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00562/005627f4.md) [`00563038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563038.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00563d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00563/00563d44.md)
- 新版 呼出元 2件 [`005627f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/005627f4.md) [`00563038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563038.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00563d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00563/00563d44.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00565494",
      "incomplete_value": false,
      "site": "00565498",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565494",
      "incomplete_value": false,
      "site": "00565498",
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
            "const:b00:8"
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
      "definition_site": "005654a4",
      "incomplete_value": false,
      "site": "005654b0",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005654a4",
      "incomplete_value": false,
      "site": "005654b0",
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
            "const:7d8:8"
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
      "00565498",
      "DATA",
      [
        "storage",
        "00befb00",
        null,
        "pointer"
      ]
    ],
    [
      "005654b0",
      "DATA",
      [
        "storage",
        "00bef7d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565498",
      "DATA",
      [
        "storage",
        "00befbb0",
        null,
        "pointer"
      ]
    ],
    [
      "005654b0",
      "DATA",
      [
        "storage",
        "00bef888",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056547c.md#insn-00565494) · [`005654a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056547c.md#insn-005654a0)
- 新版 [`00565494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056547c.md#insn-00565494) · [`005654a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056547c.md#insn-005654a0)

~~~diff
- 00565494 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 00565494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00565494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00565494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00565494 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 00565494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00565494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00565494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00565494 bytes 29012c91
+ 00565494 bytes 29c12e91
- 005654a0 ["COPY", "register:4040:8", ["const:bef000:8"]]
- 005654a0 bytes 483400d0
+ 005654a0 ["COPY", "register:4040:8", ["const:bef000:8"]]
+ 005654a0 bytes 483400d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-067b6e938e3d97e1e7376248b2ea0684"></a>

### [`0056554c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056554c.md) → [`0056554c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056554c.md) _INIT_32

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00560444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/00560444.md) [`00560474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/00560474.md) [`005604a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005604a4.md) [`005604ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005604ac.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00560444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560444.md) [`00560474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/00560474.md) [`005604a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005604a4.md) [`005604ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005604ac.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 call, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 29.27% / 新版 29.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 8件, `store_value` 2件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00565574",
      "incomplete_value": false,
      "site": "00565574",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:3c0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565574",
      "incomplete_value": false,
      "site": "00565574",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:300:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "00565590",
      "incomplete_value": false,
      "site": "00565590",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:3f0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565590",
      "incomplete_value": false,
      "site": "00565590",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:330:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "005655b0",
      "incomplete_value": false,
      "site": "005655b0",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:420:8"
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
      "definition_site": "005655b0",
      "incomplete_value": false,
      "site": "005655b0",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:360:8"
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
      "00565564",
      "PARAM",
      [
        "storage",
        "00c26300",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:0056556c",
      "PARAM",
      [
        "storage",
        "00560444",
        null,
        null
      ]
    ],
    [
      "00565570",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00565564",
      "PARAM",
      [
        "storage",
        "00c263c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0056556c",
      "PARAM",
      [
        "storage",
        "00560444",
        null,
        null
      ]
    ],
    [
      "00565570",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056554c.md#insn-00565578) · [`00565594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/0056554c.md#insn-00565594)
- 新版 [`00565578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/0056554c.md#insn-00565578)

~~~diff
- 00565578 ["INT_ADD", "register:40f0:8", ["const:565578:8", "const:4:8"]]
- 00565578 ["CALL", null, ["callee:00bdaf90:8"]]
- 00565578 bytes 5ad61994
+ 00565578 ["INT_ADD", "register:40f0:8", ["const:565578:8", "const:4:8"]]
+ 00565578 ["CALL", null, ["callee:00bdaf90:8"]]
+ 00565578 bytes 86d61994
- 00565594 ["INT_ADD", "register:40f0:8", ["const:565594:8", "const:4:8"]]
- 00565594 ["CALL", null, ["callee:00bdaf90:8"]]
- 00565594 bytes 53d61994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-595aa18bb5df4651e83a20e05f88bbbd"></a>

### [`005655f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/005655f0.md) → [`005655f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/005655f0.md) FUN_005655f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00574724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574724.md) · 呼出先 2件 [`00571a60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00571/00571a60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00574724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574724.md) · 呼出先 2件 [`00571a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00571/00571a60.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00565628",
      "incomplete_value": false,
      "site": "00565634",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565628",
      "incomplete_value": false,
      "site": "00565634",
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
            "const:b50:8"
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
      "00565634",
      "DATA",
      [
        "storage",
        "00befb50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565634",
      "DATA",
      [
        "storage",
        "00befc00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/005655f0.md#insn-00565628)
- 新版 [`00565628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/005655f0.md#insn-00565628)

~~~diff
- 00565628 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 00565628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565628 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 00565628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565628 bytes 08412d91
+ 00565628 bytes 08013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86cd7320914f4850ea74253667c1fae1"></a>

### [`00565684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565684.md) → [`00565684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565684.md) FUN_00565684

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
      "definition_site": "00565688",
      "incomplete_value": false,
      "site": "0056568c",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565688",
      "incomplete_value": false,
      "site": "0056568c",
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
            "const:b50:8"
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
      "0056568c",
      "DATA",
      [
        "storage",
        "00befb50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056568c",
      "DATA",
      [
        "storage",
        "00befc00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565684.md#insn-00565688)
- 新版 [`00565688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565684.md#insn-00565688)

~~~diff
- 00565688 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 00565688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565688 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 00565688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565688 bytes 08412d91
+ 00565688 bytes 08013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20200d64e41778869d3893ccfb39bbbb"></a>

### [`00565694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565694.md) → [`00565694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565694.md) FUN_00565694

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
      "definition_site": "005656a4",
      "incomplete_value": false,
      "site": "005656ac",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005656a4",
      "incomplete_value": false,
      "site": "005656ac",
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
            "const:b50:8"
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
      "005656ac",
      "DATA",
      [
        "storage",
        "00befb50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005656ac",
      "DATA",
      [
        "storage",
        "00befc00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005656a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565694.md#insn-005656a4)
- 新版 [`005656a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565694.md#insn-005656a4)

~~~diff
- 005656a4 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 005656a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005656a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005656a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005656a4 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 005656a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005656a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005656a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005656a4 bytes 08412d91
+ 005656a4 bytes 08013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d25a8f3dd6b48db985ac07b6ad746314"></a>

### [`00565720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565720.md) → [`00565720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565720.md) FUN_00565720

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00565ce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ce8.md) · 呼出先 7件 [`00565e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565e14.md) [`00567d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567d4c.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00565ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ce8.md) · 呼出先 7件 [`00565e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565e14.md) [`00567d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d4c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00565750",
      "incomplete_value": false,
      "site": "00565764",
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
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565750",
      "incomplete_value": false,
      "site": "00565764",
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
            "const:ba0:8"
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
      "00565764",
      "DATA",
      [
        "storage",
        "00befba0",
        null,
        "undefined *"
      ]
    ],
    [
      "00565834",
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
      "00565764",
      "DATA",
      [
        "storage",
        "00befc50",
        null,
        "undefined *"
      ]
    ],
    [
      "00565834",
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

- 旧版 [`00565750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565720.md#insn-00565750) · [`00565828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565720.md#insn-00565828)
- 新版 [`00565750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565720.md#insn-00565750) · [`00565828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565720.md#insn-00565828)

~~~diff
- 00565750 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00565750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565750 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00565750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565750 bytes 08812e91
+ 00565750 bytes 08413191
- 00565828 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 00565828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565828 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 00565828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565828 bytes 08810691
+ 00565828 bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fa084db02c74a3c53778e6ac2dfdac6"></a>

### [`00565908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565908.md) → [`00565908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565908.md) FUN_00565908

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
      "definition_site": "0056591c",
      "incomplete_value": false,
      "site": "00565920",
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
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056591c",
      "incomplete_value": false,
      "site": "00565920",
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
            "const:ba0:8"
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
      "00565920",
      "DATA",
      [
        "storage",
        "00befba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565920",
      "DATA",
      [
        "storage",
        "00befc50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056591c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565908.md#insn-0056591c)
- 新版 [`0056591c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565908.md#insn-0056591c)

~~~diff
- 0056591c ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 0056591c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056591c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056591c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056591c ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 0056591c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056591c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056591c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056591c bytes 08812e91
+ 0056591c bytes 08413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0605208da2cd813857b785481c62b4be"></a>

### [`00565964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565964.md) → [`00565964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565964.md) FUN_00565964

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
      "definition_site": "0056597c",
      "incomplete_value": false,
      "site": "00565980",
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
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056597c",
      "incomplete_value": false,
      "site": "00565980",
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
            "const:ba0:8"
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
      "00565980",
      "DATA",
      [
        "storage",
        "00befba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565980",
      "DATA",
      [
        "storage",
        "00befc50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056597c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565964.md#insn-0056597c)
- 新版 [`0056597c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565964.md#insn-0056597c)

~~~diff
- 0056597c ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 0056597c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056597c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056597c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056597c ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 0056597c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056597c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056597c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056597c bytes 08812e91
+ 0056597c bytes 08413191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe0a3c9becac896a7b1112cca4438122"></a>

### [`00565ce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ce8.md) → [`00565ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ce8.md) FUN_00565ce8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00565c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565c20.md) [`0057472c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/0057472c.md) · 呼出先 6件 [`00565720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565720.md) [`00574724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574724.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 2件 [`00565c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565c20.md) [`0057472c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057472c.md) · 呼出先 6件 [`00565720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565720.md) [`00574724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574724.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00565d38",
      "incomplete_value": false,
      "site": "00565d44",
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
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565d38",
      "incomplete_value": false,
      "site": "00565d44",
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
            "const:880:8"
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
      "00565d44",
      "DATA",
      [
        "storage",
        "00bee880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00565d44",
      "DATA",
      [
        "storage",
        "00bee930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ce8.md#insn-00565d38)
- 新版 [`00565d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ce8.md#insn-00565d38)

~~~diff
- 00565d38 ["COPY", "tmp:0:8", ["const:880:8"]]
- 00565d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00565d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00565d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00565d38 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 00565d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00565d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00565d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00565d38 bytes 08012291
+ 00565d38 bytes 08c12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d603bfb18c1576dc8ca5e0a480b10c5"></a>

### [`00565f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f20.md) → [`00565f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f20.md) FUN_00565f20

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004183e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004183e4.md) · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md) [`00bdb1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1f0.md) [`00bdd3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3a0.md)
- 新版 呼出元 1件 [`004183e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183e4.md) · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md) [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00bdd450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd450.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 72.41% / 新版 72.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00565f34",
      "incomplete_value": false,
      "site": "00565f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565f34",
      "incomplete_value": false,
      "site": "00565f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00565f60",
      "incomplete_value": true,
      "site": "00565f60",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565f60",
      "incomplete_value": true,
      "site": "00565f60",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "00565f50",
      "incomplete_value": true,
      "site": "00565f60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565f50",
      "incomplete_value": true,
      "site": "00565f60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:390:8"
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
      "00565f34",
      "PARAM",
      [
        "storage",
        "00c23e18",
        null,
        null
      ]
    ],
    [
      "00565f50",
      "READ",
      [
        "storage",
        "00c26390",
        null,
        "undefined8"
      ]
    ],
    [
      "00565f6c",
      "READ",
      [
        "storage",
        "00c263d0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00565f34",
      "PARAM",
      [
        "storage",
        "00c23ec8",
        null,
        null
      ]
    ],
    [
      "00565f50",
      "READ",
      [
        "storage",
        "00c26450",
        null,
        "undefined8"
      ]
    ],
    [
      "00565f6c",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f20.md#insn-00565f34) · [`00565f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f20.md#insn-00565f50) · [`00565f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f20.md#insn-00565f64)
- 新版 [`00565f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f20.md#insn-00565f34) · [`00565f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f20.md#insn-00565f50)

~~~diff
- 00565f34 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 00565f34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00565f34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00565f34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00565f34 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00565f34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00565f34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00565f34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00565f34 bytes 00603891
+ 00565f34 bytes 00203b91
- 00565f50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
- 00565f50 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00565f50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 00565f50 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00565f50 bytes 00c941f9
+ 00565f50 bytes 002942f9
- 00565f64 ["COPY", "register:4040:8", ["const:c26000:8"]]
- 00565f64 bytes 083600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7951b69f5e0d1388187f9dc0075bb00d"></a>

### [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) → [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) FUN_00565f94

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 138件 [`004747cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004747cc.md) [`004749f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004749f8.md) [`004782e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004782e4.md) [`0054e928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e928.md) [`0054ea94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ea94.md) · 呼出先 2件 [`00bdb1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1f0.md) [`00bdd3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3a0.md)
- 新版 呼出元 138件 [`004747cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/004747cc.md) [`004749f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/004749f8.md) [`004782e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004782e4.md) [`0054e928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e928.md) [`0054ea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054ea94.md) · 呼出先 2件 [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00bdd450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd450.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 70.83% / 新版 70.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00565fa4",
      "incomplete_value": false,
      "site": "00565fa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565fa4",
      "incomplete_value": false,
      "site": "00565fa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00565fd0",
      "incomplete_value": true,
      "site": "00565fd0",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565fd0",
      "incomplete_value": true,
      "site": "00565fd0",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "00565fc4",
      "incomplete_value": true,
      "site": "00565fd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00565fc4",
      "incomplete_value": true,
      "site": "00565fd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:390:8"
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
      "00565fa4",
      "PARAM",
      [
        "storage",
        "00c23e18",
        null,
        null
      ]
    ],
    [
      "00565fc4",
      "READ",
      [
        "storage",
        "00c26390",
        null,
        "undefined8"
      ]
    ],
    [
      "00565fdc",
      "READ",
      [
        "storage",
        "00c263d0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00565fa4",
      "PARAM",
      [
        "storage",
        "00c23ec8",
        null,
        null
      ]
    ],
    [
      "00565fc4",
      "READ",
      [
        "storage",
        "00c26450",
        null,
        "undefined8"
      ]
    ],
    [
      "00565fdc",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00565fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md#insn-00565fa4) · [`00565fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md#insn-00565fc4) · [`00565fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md#insn-00565fd4)
- 新版 [`00565fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md#insn-00565fa4) · [`00565fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md#insn-00565fc4)

~~~diff
- 00565fa4 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 00565fa4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00565fa4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00565fa4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00565fa4 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00565fa4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00565fa4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00565fa4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00565fa4 bytes 00603891
+ 00565fa4 bytes 00203b91
- 00565fc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
- 00565fc4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00565fc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 00565fc4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00565fc4 bytes 00c941f9
+ 00565fc4 bytes 002942f9
- 00565fd4 ["COPY", "register:4040:8", ["const:c26000:8"]]
- 00565fd4 bytes 083600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83a9aecf427814be74bd70e0d851c25c"></a>

### [`00565ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md) → [`00565ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md) FUN_00565ff4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`00565f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f20.md) [`005668b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/005668b8.md) [`0056691c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056691c.md) [`00566988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566988.md) [`005673dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/005673dc.md) · 呼出先 3件 [`00567a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567a74.md) [`00bdb1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1f0.md) [`00bdd3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3a0.md)
- 新版 呼出元 11件 [`00565f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f20.md) [`005668b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/005668b8.md) [`0056691c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056691c.md) [`00566988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566988.md) [`005673dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005673dc.md) · 呼出先 3件 [`00567a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567a74.md) [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00bdd450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd450.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00566020",
      "incomplete_value": false,
      "site": "00566024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566020",
      "incomplete_value": false,
      "site": "00566024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0056604c",
      "incomplete_value": true,
      "site": "0056604c",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056604c",
      "incomplete_value": true,
      "site": "0056604c",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "0056603c",
      "incomplete_value": true,
      "site": "0056604c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056603c",
      "incomplete_value": true,
      "site": "0056604c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:390:8"
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
      "00566020",
      "PARAM",
      [
        "storage",
        "00c23e18",
        null,
        null
      ]
    ],
    [
      "0056603c",
      "READ",
      [
        "storage",
        "00c26390",
        null,
        "undefined8"
      ]
    ],
    [
      "00566058",
      "READ",
      [
        "storage",
        "00c263d0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00566020",
      "PARAM",
      [
        "storage",
        "00c23ec8",
        null,
        null
      ]
    ],
    [
      "0056603c",
      "READ",
      [
        "storage",
        "00c26450",
        null,
        "undefined8"
      ]
    ],
    [
      "00566058",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md#insn-00566020) · [`0056603c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md#insn-0056603c) · [`00566050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md#insn-00566050)
- 新版 [`00566020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md#insn-00566020) · [`0056603c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md#insn-0056603c)

~~~diff
- 00566020 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 00566020 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00566020 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00566020 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00566020 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00566020 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00566020 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00566020 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00566020 bytes 00603891
+ 00566020 bytes 00203b91
- 0056603c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
- 0056603c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056603c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 0056603c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0056603c bytes 00c941f9
+ 0056603c bytes 002942f9
- 00566050 ["COPY", "register:4040:8", ["const:c26000:8"]]
- 00566050 bytes 08360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae6b7362612cea5df42e8ef54246944f"></a>

### [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) → [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) FUN_00566284

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 122件 [`004747cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004747cc.md) [`004749f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004749f8.md) [`004782e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004782e4.md) [`0054e928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e928.md) [`0054ea94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ea94.md) · 呼出先 0件 
- 新版 呼出元 122件 [`004747cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/004747cc.md) [`004749f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/004749f8.md) [`004782e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004782e4.md) [`0054e928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e928.md) [`0054ea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054ea94.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00566288",
      "incomplete_value": false,
      "site": "0056628c",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566288",
      "incomplete_value": false,
      "site": "0056628c",
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
            "const:398:8"
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
      "00566288",
      "DATA",
      [
        "storage",
        "00c26398",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00566288",
      "DATA",
      [
        "storage",
        "00c26458",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md#insn-00566288)
- 新版 [`00566288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md#insn-00566288)

~~~diff
- 00566288 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00566288 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00566288 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00566288 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00566288 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 00566288 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00566288 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00566288 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00566288 bytes 00600e91
+ 00566288 bytes 00601191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f8c2c16df750b7bb7e589e6f6031094"></a>

### [`00566290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566290.md) → [`00566290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566290.md) FUN_00566290

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0056a298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056a298.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0056a298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056a298.md) · 呼出先 0件 

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
      "definition_site": "0056629c",
      "incomplete_value": false,
      "site": "0056629c",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056629c",
      "incomplete_value": false,
      "site": "0056629c",
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
            "const:c28:8"
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
      "0056629c",
      "DATA",
      [
        "storage",
        "00befc28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0056629c",
      "DATA",
      [
        "storage",
        "00befcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566290.md#insn-00566294)
- 新版 [`00566294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566290.md#insn-00566294)

~~~diff
- 00566294 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00566294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00566294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00566294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00566294 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00566294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00566294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00566294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00566294 bytes 08a13091
+ 00566294 bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6408fb90148daac4ba8a9396703df3f8"></a>

### [`005662b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/005662b8.md) → [`005662b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/005662b8.md) FUN_005662b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00567388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567388.md) · 呼出先 4件 [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00567388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567388.md) · 呼出先 4件 [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005662e8",
      "incomplete_value": false,
      "site": "005662e8",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005662e8",
      "incomplete_value": false,
      "site": "005662e8",
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
            "const:c28:8"
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
      "005662e8",
      "DATA",
      [
        "storage",
        "00befc28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005662e8",
      "DATA",
      [
        "storage",
        "00befcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005662e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/005662b8.md#insn-005662e4)
- 新版 [`005662e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/005662b8.md#insn-005662e4)

~~~diff
- 005662e4 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 005662e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005662e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005662e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005662e4 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 005662e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005662e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005662e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005662e4 bytes 08a13091
+ 005662e4 bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02b1a34ae4d971de9d3f9371239ce507"></a>

### [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) → [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) FUN_00566448

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 130件 [`004747cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004747cc.md) [`004749f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004749f8.md) [`004782e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004782e4.md) [`0054e928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054e928.md) [`0054ea94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ea94.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00567ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567ad4.md) [`00567bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567bfc.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 130件 [`004747cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/004747cc.md) [`004749f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/004749f8.md) [`004782e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004782e4.md) [`0054e928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054e928.md) [`0054ea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054ea94.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00567ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567ad4.md) [`00567bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567bfc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.58% / 新版 93.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00566538",
      "incomplete_value": false,
      "site": "0056653c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566538",
      "incomplete_value": false,
      "site": "0056653c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:e18:8"
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
      "definition_site": "0056655c",
      "incomplete_value": false,
      "site": "00566560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056655c",
      "incomplete_value": false,
      "site": "00566560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00566588",
      "incomplete_value": true,
      "site": "00566588",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566588",
      "incomplete_value": true,
      "site": "00566588",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00566538",
      "PARAM",
      [
        "storage",
        "00c23e18",
        null,
        null
      ]
    ],
    [
      "0056655c",
      "PARAM",
      [
        "storage",
        "00c23e18",
        null,
        null
      ]
    ],
    [
      "00566574",
      "READ",
      [
        "storage",
        "00c26390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00566538",
      "PARAM",
      [
        "storage",
        "00c23ec8",
        null,
        null
      ]
    ],
    [
      "0056655c",
      "PARAM",
      [
        "storage",
        "00c23ec8",
        null,
        null
      ]
    ],
    [
      "00566574",
      "READ",
      [
        "storage",
        "00c26450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md#insn-00566538) · [`0056655c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md#insn-0056655c) · [`00566574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md#insn-00566574)
- 新版 [`00566538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md#insn-00566538) · [`0056655c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md#insn-0056655c) · [`00566574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md#insn-00566574)

~~~diff
- 00566538 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 00566538 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00566538 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00566538 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00566538 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00566538 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00566538 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00566538 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00566538 bytes 00603891
+ 00566538 bytes 00203b91
- 0056655c ["COPY", "tmp:0:8", ["const:e18:8"]]
- 0056655c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0056655c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0056655c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0056655c ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 0056655c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0056655c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0056655c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0056655c bytes 00603891
+ 0056655c bytes 00203b91
- 00566574 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
- 00566574 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00566574 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 00566574 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00566574 bytes 00c941f9
+ 00566574 bytes 002942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bd7b28f3abb5b11b37b06fc7de1f4d1"></a>

### [`005668b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/005668b8.md) → [`005668b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/005668b8.md) FUN_005668b8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0055b604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b604.md) [`0055b95c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055b/0055b95c.md) [`0055f0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f0e4.md) · 呼出先 1件 [`00565ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md)
- 新版 呼出元 3件 [`0055b604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b604.md) [`0055b95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055b/0055b95c.md) [`0055f0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f0e4.md) · 呼出先 1件 [`00565ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005668d0",
      "incomplete_value": false,
      "site": "005668d0",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005668d0",
      "incomplete_value": false,
      "site": "005668d0",
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
            "const:c28:8"
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
      "005668d0",
      "DATA",
      [
        "storage",
        "00befc28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005668d0",
      "DATA",
      [
        "storage",
        "00befcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005668c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/005668b8.md#insn-005668c8) · [`005668cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/005668b8.md#insn-005668cc)
- 新版 [`005668c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/005668b8.md#insn-005668c8) · [`005668cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/005668b8.md#insn-005668cc)

~~~diff
- 005668c8 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 005668c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005668c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005668c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005668c8 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 005668c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005668c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005668c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005668c8 bytes 08a13091
+ 005668c8 bytes 08613391
- 005668cc ["COPY", "register:40a0:8", ["register:4000:8"]]
- 005668cc bytes f40300aa
+ 005668cc ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 005668cc bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-210f5ff0e946bbdfb61eb3b82e7bb4b4"></a>

### [`0056691c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056691c.md) → [`0056691c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056691c.md) FUN_0056691c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567a74.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567a74.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00566930",
      "incomplete_value": false,
      "site": "00566934",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566930",
      "incomplete_value": false,
      "site": "00566934",
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
            "const:c28:8"
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
      "00566934",
      "DATA",
      [
        "storage",
        "00befc28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00566934",
      "DATA",
      [
        "storage",
        "00befcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056691c.md#insn-00566930)
- 新版 [`00566930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056691c.md#insn-00566930)

~~~diff
- 00566930 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00566930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00566930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00566930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00566930 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00566930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00566930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00566930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00566930 bytes 08a13091
+ 00566930 bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2948f13a86cff2360b50024e46b136a0"></a>

### [`005669f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/005669f8.md) → [`005669f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/005669f8.md) FUN_005669f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 55件 [`004782e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004782e4.md) [`0054ec1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ec1c.md) [`0054ef40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ef40.md) [`0054f220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f220.md) [`0054f3d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f3d4.md) · 呼出先 0件 
- 新版 呼出元 55件 [`004782e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004782e4.md) [`0054ec1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054ec1c.md) [`0054ef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054ef40.md) [`0054f220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054f220.md) [`0054f3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054f3d4.md) · 呼出先 0件 

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
      "definition_site": "00566a2c",
      "incomplete_value": false,
      "site": "00566a2c",
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
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566a2c",
      "incomplete_value": false,
      "site": "00566a2c",
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
            "const:c48:8"
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
      "00566a2c",
      "DATA",
      [
        "storage",
        "00befc48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00566a2c",
      "DATA",
      [
        "storage",
        "00befcf8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/005669f8.md#insn-00566a28)
- 新版 [`00566a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/005669f8.md#insn-00566a28)

~~~diff
- 00566a28 ["COPY", "tmp:0:8", ["const:c48:8"]]
- 00566a28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00566a28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00566a28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00566a28 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00566a28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00566a28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00566a28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00566a28 bytes 29213191
+ 00566a28 bytes 29e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2976896e24c521da053407915cca4fcb"></a>

### [`00566d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566d10.md) → [`00566d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566d10.md) FUN_00566d10

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0055d9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d9b0.md) [`0055f300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f300.md) [`0055f488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f488.md) [`0055f61c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f61c.md) [`0055f798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f798.md) · 呼出先 0件 
- 新版 呼出元 7件 [`0055d9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d9b0.md) [`0055f300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f300.md) [`0055f488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f488.md) [`0055f61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f61c.md) [`0055f798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f798.md) · 呼出先 0件 

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
      "definition_site": "00566d30",
      "incomplete_value": false,
      "site": "00566d30",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566d30",
      "incomplete_value": false,
      "site": "00566d30",
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
            "const:c68:8"
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
      "00566d30",
      "DATA",
      [
        "storage",
        "00befc68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00566d30",
      "DATA",
      [
        "storage",
        "00befd18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566d10.md#insn-00566d2c)
- 新版 [`00566d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566d10.md#insn-00566d2c)

~~~diff
- 00566d2c ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00566d2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00566d2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00566d2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00566d2c ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00566d2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00566d2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00566d2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00566d2c bytes 08a13191
+ 00566d2c bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abc3248f37dcca692163da59c5d18b0d"></a>

### [`00566dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566dac.md) → [`00566dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566dac.md) FUN_00566dac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055d1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d1c0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0055d1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d1c0.md) · 呼出先 0件 

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
      "definition_site": "00566dc0",
      "incomplete_value": false,
      "site": "00566dc8",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566dc0",
      "incomplete_value": false,
      "site": "00566dc8",
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
            "const:c68:8"
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
      "00566dc8",
      "DATA",
      [
        "storage",
        "00befc68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00566dc8",
      "DATA",
      [
        "storage",
        "00befd18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566dac.md#insn-00566dc0)
- 新版 [`00566dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566dac.md#insn-00566dc0)

~~~diff
- 00566dc0 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00566dc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00566dc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00566dc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00566dc0 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00566dc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00566dc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00566dc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00566dc0 bytes 29a13191
+ 00566dc0 bytes 29613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-accaecb724bf2a104906808f9e56be24"></a>

### [`00566df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566df0.md) → [`00566df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566df0.md) FUN_00566df0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0055f300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f300.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0055f300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f300.md) · 呼出先 0件 

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
      "definition_site": "00566e0c",
      "incomplete_value": false,
      "site": "00566e0c",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00566e0c",
      "incomplete_value": false,
      "site": "00566e0c",
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
            "const:c68:8"
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
      "00566e0c",
      "DATA",
      [
        "storage",
        "00befc68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00566e0c",
      "DATA",
      [
        "storage",
        "00befd18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00566e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566df0.md#insn-00566e04)
- 新版 [`00566e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566df0.md#insn-00566e04)

~~~diff
- 00566e04 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00566e04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00566e04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00566e04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00566e04 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00566e04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00566e04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00566e04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00566e04 bytes 08a13191
+ 00566e04 bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-804a9e268c8d45e359435a02f3b2e7d0"></a>

### [`00567030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567030.md) → [`00567030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567030.md) FUN_00567030

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`0055d1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d1c0.md) [`0055d5cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d5cc.md) [`0055e5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e5bc.md) [`0055e88c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055e/0055e88c.md) [`0055f300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055f/0055f300.md) · 呼出先 2件 [`00bdb1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1f0.md) [`00bdd3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3a0.md)
- 新版 呼出元 10件 [`0055d1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d1c0.md) [`0055d5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d5cc.md) [`0055e5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e5bc.md) [`0055e88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e88c.md) [`0055f300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055f/0055f300.md) · 呼出先 2件 [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00bdd450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd450.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.08% / 新版 86.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00567040",
      "incomplete_value": false,
      "site": "00567048",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567040",
      "incomplete_value": false,
      "site": "00567048",
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
            "const:c68:8"
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
      "definition_site": "00567050",
      "incomplete_value": false,
      "site": "00567054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567050",
      "incomplete_value": false,
      "site": "00567054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00567088",
      "incomplete_value": true,
      "site": "00567088",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567088",
      "incomplete_value": true,
      "site": "00567088",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
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
      "00567048",
      "DATA",
      [
        "storage",
        "00befc68",
        null,
        "undefined *"
      ]
    ],
    [
      "00567050",
      "PARAM",
      [
        "storage",
        "00c23e18",
        null,
        null
      ]
    ],
    [
      "00567074",
      "READ",
      [
        "storage",
        "00c26390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00567048",
      "DATA",
      [
        "storage",
        "00befd18",
        null,
        "undefined *"
      ]
    ],
    [
      "00567050",
      "PARAM",
      [
        "storage",
        "00c23ec8",
        null,
        null
      ]
    ],
    [
      "00567074",
      "READ",
      [
        "storage",
        "00c26450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567030.md#insn-00567040) · [`00567044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567030.md#insn-00567044)
- 新版 [`00567040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567030.md#insn-00567040) · [`00567044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567030.md#insn-00567044)

~~~diff
- 00567040 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00567040 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00567040 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00567040 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00567040 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00567040 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00567040 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00567040 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00567040 bytes 08a13191
+ 00567040 bytes 08613491
- 00567044 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00567044 bytes f30300aa
+ 00567044 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00567044 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58a3e1cd289821146ccb8165cff38600"></a>

### [`00567194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567194.md) → [`00567194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567194.md) FUN_00567194

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1f0.md) [`00bdd3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00bdd450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd450.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005671a8",
      "incomplete_value": false,
      "site": "005671ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005671a8",
      "incomplete_value": false,
      "site": "005671ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005671d4",
      "incomplete_value": true,
      "site": "005671d4",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005671d4",
      "incomplete_value": true,
      "site": "005671d4",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "005671c8",
      "incomplete_value": true,
      "site": "005671d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005671c8",
      "incomplete_value": true,
      "site": "005671d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:390:8"
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
      "005671a8",
      "PARAM",
      [
        "storage",
        "00c23e18",
        null,
        null
      ]
    ],
    [
      "005671c8",
      "READ",
      [
        "storage",
        "00c26390",
        null,
        "undefined8"
      ]
    ],
    [
      "005671e0",
      "READ",
      [
        "storage",
        "00c263d0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005671a8",
      "PARAM",
      [
        "storage",
        "00c23ec8",
        null,
        null
      ]
    ],
    [
      "005671c8",
      "READ",
      [
        "storage",
        "00c26450",
        null,
        "undefined8"
      ]
    ],
    [
      "005671e0",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005671a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567194.md#insn-005671a8) · [`005671c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567194.md#insn-005671c8) · [`005671d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567194.md#insn-005671d8)
- 新版 [`005671a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567194.md#insn-005671a8) · [`005671c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567194.md#insn-005671c8)

~~~diff
- 005671a8 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 005671a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005671a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005671a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005671a8 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 005671a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005671a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005671a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005671a8 bytes 00603891
+ 005671a8 bytes 00203b91
- 005671c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
- 005671c8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005671c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 005671c8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005671c8 bytes 00c941f9
+ 005671c8 bytes 002942f9
- 005671d8 ["COPY", "register:4040:8", ["const:c26000:8"]]
- 005671d8 bytes e83500f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2ec57d8108cf53c9d72997bee3b78e5"></a>

### [`00567204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567204.md) → [`00567204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567204.md) FUN_00567204

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1f0.md) [`00bdd3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00bdd450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd450.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00567218",
      "incomplete_value": false,
      "site": "0056721c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567218",
      "incomplete_value": false,
      "site": "0056721c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00567244",
      "incomplete_value": true,
      "site": "00567244",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567244",
      "incomplete_value": true,
      "site": "00567244",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "00567238",
      "incomplete_value": true,
      "site": "00567244",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567238",
      "incomplete_value": true,
      "site": "00567244",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:390:8"
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
      "00567218",
      "PARAM",
      [
        "storage",
        "00c23e18",
        null,
        null
      ]
    ],
    [
      "00567238",
      "READ",
      [
        "storage",
        "00c26390",
        null,
        "undefined8"
      ]
    ],
    [
      "00567250",
      "READ",
      [
        "storage",
        "00c263d0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00567218",
      "PARAM",
      [
        "storage",
        "00c23ec8",
        null,
        null
      ]
    ],
    [
      "00567238",
      "READ",
      [
        "storage",
        "00c26450",
        null,
        "undefined8"
      ]
    ],
    [
      "00567250",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567204.md#insn-00567218) · [`00567238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567204.md#insn-00567238) · [`00567248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567204.md#insn-00567248)
- 新版 [`00567218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567204.md#insn-00567218) · [`00567238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567204.md#insn-00567238)

~~~diff
- 00567218 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 00567218 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00567218 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00567218 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00567218 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00567218 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00567218 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00567218 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00567218 bytes 00603891
+ 00567218 bytes 00203b91
- 00567238 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
- 00567238 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00567238 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 00567238 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00567238 bytes 00c941f9
+ 00567238 bytes 002942f9
- 00567248 ["COPY", "register:4040:8", ["const:c26000:8"]]
- 00567248 bytes e83500f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4617873fea364c1d93ab5609b21ced05"></a>

### [`00567274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567274.md) → [`00567274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567274.md) FUN_00567274

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1f0.md) [`00bdd3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3a0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00bdd450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd450.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.55% / 新版 89.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005672bc",
      "incomplete_value": true,
      "site": "005672bc",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005672bc",
      "incomplete_value": true,
      "site": "005672bc",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "005672ac",
      "incomplete_value": true,
      "site": "005672bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005672ac",
      "incomplete_value": true,
      "site": "005672bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:390:8"
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
      "definition_site": "005672c8",
      "incomplete_value": true,
      "site": "005672cc",
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
      "definition_site": "005672c8",
      "incomplete_value": true,
      "site": "005672cc",
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
      "0056728c",
      "PARAM",
      [
        "storage",
        "00c23e18",
        null,
        null
      ]
    ],
    [
      "005672ac",
      "READ",
      [
        "storage",
        "00c26390",
        null,
        "undefined8"
      ]
    ],
    [
      "005672c8",
      "READ",
      [
        "storage",
        "00c263d0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0056728c",
      "PARAM",
      [
        "storage",
        "00c23ec8",
        null,
        null
      ]
    ],
    [
      "005672ac",
      "READ",
      [
        "storage",
        "00c26450",
        null,
        "undefined8"
      ]
    ],
    [
      "005672c8",
      "READ",
      [
        "storage",
        "00c26490",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056728c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567274.md#insn-0056728c) · [`005672ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567274.md#insn-005672ac) · [`005672c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567274.md#insn-005672c0)
- 新版 [`0056728c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567274.md#insn-0056728c) · [`005672ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567274.md#insn-005672ac)

~~~diff
- 0056728c ["COPY", "tmp:0:8", ["const:e18:8"]]
- 0056728c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0056728c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0056728c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0056728c ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 0056728c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0056728c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0056728c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0056728c bytes 00603891
+ 0056728c bytes 00203b91
- 005672ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
- 005672ac ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 005672ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 005672ac ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 005672ac bytes 00c941f9
+ 005672ac bytes 002942f9
- 005672c0 ["COPY", "register:4040:8", ["const:c26000:8"]]
- 005672c0 bytes e83500f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69cb716f00ba02148a763cb63944da9b"></a>

### [`00567388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567388.md) → [`00567388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567388.md) FUN_00567388

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005609d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/005612d4.md) · 呼出先 1件 [`005662b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/005662b8.md)
- 新版 呼出元 2件 [`005609d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/005612d4.md) · 呼出先 1件 [`005662b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/005662b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005673c8",
      "incomplete_value": false,
      "site": "005673cc",
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
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005673c8",
      "incomplete_value": false,
      "site": "005673cc",
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
            "const:ca0:8"
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
      "definition_site": "005673a4",
      "incomplete_value": false,
      "site": "005673b0",
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
            "const:c62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005673a4",
      "incomplete_value": false,
      "site": "005673b0",
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
            "const:bd5:8"
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
      "005673a4",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "005673cc",
      "DATA",
      [
        "storage",
        "00befca0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005673a4",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ],
    [
      "005673cc",
      "DATA",
      [
        "storage",
        "00befd50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005673a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567388.md#insn-005673a4) · [`005673c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567388.md#insn-005673c8)
- 新版 [`005673a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567388.md#insn-005673a4) · [`005673c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567388.md#insn-005673c8)

~~~diff
- 005673a4 ["COPY", "tmp:0:8", ["const:bd5:8"]]
- 005673a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005673a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005673a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005673a4 ["COPY", "tmp:0:8", ["const:c62:8"]]
+ 005673a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005673a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005673a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005673a4 bytes 21542f91
+ 005673a4 bytes 21883191
- 005673c8 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 005673c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005673c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005673c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005673c8 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 005673c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005673c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005673c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005673c8 bytes 08813291
+ 005673c8 bytes 08413591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfd9089e14af2c76e85a42e7d0ceb714"></a>

### [`005673dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/005673dc.md) → [`005673dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005673dc.md) FUN_005673dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005609d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/005612d4.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00567a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567a74.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 2件 [`005609d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/005612d4.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00567a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567a74.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00567440",
      "incomplete_value": true,
      "site": "00567450",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567440",
      "incomplete_value": true,
      "site": "00567450",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a31:8"
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
      "definition_site": "00567440",
      "incomplete_value": true,
      "site": "00567450",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00567440",
      "incomplete_value": true,
      "site": "00567450",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00567454",
      "incomplete_value": true,
      "site": "00567460",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00567454",
      "incomplete_value": true,
      "site": "00567460",
      "value": [
        "LOAD",
        "16",
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
      "00567440",
      "READ",
      [
        "storage",
        "002aca31",
        null,
        "string"
      ]
    ],
    [
      "00567440",
      "READ",
      [
        "storage",
        "002aca41",
        null,
        "string"
      ]
    ],
    [
      "00567454",
      "READ",
      [
        "storage",
        "002aca51",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00567440",
      "READ",
      [
        "storage",
        "002aca28",
        null,
        "string"
      ]
    ],
    [
      "00567440",
      "READ",
      [
        "storage",
        "002aca38",
        null,
        "string"
      ]
    ],
    [
      "00567454",
      "READ",
      [
        "storage",
        "002aca48",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/005673dc.md#insn-00567438) · [`0056743c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/005673dc.md#insn-0056743c)
- 新版 [`00567438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005673dc.md#insn-00567438) · [`0056743c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005673dc.md#insn-0056743c)

~~~diff
- 00567438 ["COPY", "tmp:0:8", ["const:a31:8"]]
- 00567438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00567438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00567438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00567438 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 00567438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00567438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00567438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00567438 bytes 08c52891
+ 00567438 bytes 08a12891
- 0056743c ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0056743c bytes 49eaffd0
+ 0056743c ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0056743c bytes 49eaffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65e8ea6860b17e22f9b58347f37006be"></a>

### [`0056766c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/0056766c.md) → [`0056766c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/0056766c.md) FUN_0056766c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0054f588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f588.md) [`00555fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00555/00555fe4.md) [`0055828c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/0055828c.md) [`005609d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00561/005612d4.md) · 呼出先 1件 [`00565ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md)
- 新版 呼出元 5件 [`0054f588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054f588.md) [`00555fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00555/00555fe4.md) [`0055828c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/0055828c.md) [`005609d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00560/005609d4.md) [`005612d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00561/005612d4.md) · 呼出先 1件 [`00565ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005676e4",
      "incomplete_value": false,
      "site": "005676e4",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005676e4",
      "incomplete_value": false,
      "site": "005676e4",
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
            "const:c28:8"
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
      "definition_site": "0056771c",
      "incomplete_value": false,
      "site": "00567720",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056771c",
      "incomplete_value": false,
      "site": "00567720",
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
            "const:cc0:8"
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
      "definition_site": "0056768c",
      "incomplete_value": true,
      "site": "0056769c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056768c",
      "incomplete_value": true,
      "site": "0056769c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:5c3:8"
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
      "0056768c",
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      "005676ac",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "005676e4",
      "DATA",
      [
        "storage",
        "00befc28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0056768c",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "005676ac",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "005676e4",
      "DATA",
      [
        "storage",
        "00befcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056768c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/0056766c.md#insn-0056768c) · [`005676ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/0056766c.md#insn-005676ac) · [`005676dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/0056766c.md#insn-005676dc)
- 新版 [`0056768c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/0056766c.md#insn-0056768c) · [`005676ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/0056766c.md#insn-005676ac) · [`005676dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/0056766c.md#insn-005676dc)

~~~diff
- 0056768c ["COPY", "tmp:0:8", ["const:5c3:8"]]
- 0056768c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056768c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056768c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056768c ["COPY", "tmp:0:8", ["const:650:8"]]
+ 0056768c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056768c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056768c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056768c bytes 210c1791
+ 0056768c bytes 21401991
- 005676ac ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 005676ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005676ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005676ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005676ac ["COPY", "tmp:0:8", ["const:866:8"]]
+ 005676ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005676ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005676ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005676ac bytes 21641f91
+ 005676ac bytes 21982191
- 005676dc ["COPY", "tmp:0:8", ["const:c28:8"]]
- 005676dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005676dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005676dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005676dc ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 005676dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005676dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005676dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005676dc bytes 08a13091
+ 005676dc bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9802f583f44545e9db56d117e1d15120"></a>

### [`0056774c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/0056774c.md) → [`0056774c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/0056774c.md) FUN_0056774c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0054fd90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054fd90.md) [`00550fa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00550/00550fa8.md) [`00551208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551208.md) · 呼出先 1件 [`00565ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md)
- 新版 呼出元 3件 [`0054fd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054fd90.md) [`00550fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00550/00550fa8.md) [`00551208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551208.md) · 呼出先 1件 [`00565ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00567774",
      "incomplete_value": true,
      "site": "00567774",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567774",
      "incomplete_value": true,
      "site": "00567774",
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
            "const:c28:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056779c",
      "incomplete_value": false,
      "site": "005677a0",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056779c",
      "incomplete_value": false,
      "site": "005677a0",
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
            "const:cc0:8"
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
      "00567774",
      "DATA",
      [
        "storage",
        "00befc28",
        null,
        "pointer"
      ]
    ],
    [
      "005677a0",
      "DATA",
      [
        "storage",
        "00befcc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00567774",
      "DATA",
      [
        "storage",
        "00befcd8",
        null,
        "pointer"
      ]
    ],
    [
      "005677a0",
      "DATA",
      [
        "storage",
        "00befd70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/0056774c.md#insn-00567768) · [`0056776c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/0056774c.md#insn-0056776c)
- 新版 [`00567768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/0056774c.md#insn-00567768) · [`0056776c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/0056774c.md#insn-0056776c)

~~~diff
- 00567768 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00567768 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00567768 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00567768 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00567768 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00567768 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00567768 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00567768 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00567768 bytes 29a13091
+ 00567768 bytes 29613391
- 0056776c ["COPY", "register:40a8:8", ["register:4000:8"]]
- 0056776c bytes f50300aa
+ 0056776c ["COPY", "register:40a8:8", ["register:4000:8"]]
+ 0056776c bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a11ba30fe4e01f7af1911e3683dcd6f6"></a>

### [`00567918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567918.md) → [`00567918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567918.md) JNI_OnLoad

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00566234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566234.md) [`00bdd3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00566234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566234.md) [`00bdd460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd460.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056792c",
      "incomplete_value": false,
      "site": "0056792c",
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
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056792c",
      "incomplete_value": false,
      "site": "0056792c",
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
            "const:390:8"
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
      "definition_site": "00567934",
      "incomplete_value": false,
      "site": "00567938",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567934",
      "incomplete_value": false,
      "site": "00567938",
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
            "const:3d0:8"
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
      "0056792c",
      "WRITE",
      [
        "storage",
        "00c26390",
        null,
        "undefined8"
      ]
    ],
    [
      "00567934",
      "PARAM",
      [
        "storage",
        "00c263d0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0056792c",
      "WRITE",
      [
        "storage",
        "00c26450",
        null,
        "undefined8"
      ]
    ],
    [
      "00567934",
      "PARAM",
      [
        "storage",
        "00c26490",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056792c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567918.md#insn-0056792c) · [`00567934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567918.md#insn-00567934)
- 新版 [`0056792c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567918.md#insn-0056792c) · [`00567934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567918.md#insn-00567934)

~~~diff
- 0056792c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:390:8"]]
- 0056792c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 0056792c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 0056792c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0056792c bytes 00c901f9
+ 0056792c bytes 002902f9
- 00567934 ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 00567934 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00567934 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00567934 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00567934 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 00567934 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00567934 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00567934 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00567934 bytes 00400f91
+ 00567934 bytes 00401291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43a0778ee97df6e393ca3e9fd9f36f4e"></a>

### [`0056794c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/0056794c.md) → [`0056794c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/0056794c.md) FUN_0056794c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567a74.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567a74.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00567960",
      "incomplete_value": false,
      "site": "00567964",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567960",
      "incomplete_value": false,
      "site": "00567964",
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
            "const:c28:8"
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
      "00567964",
      "DATA",
      [
        "storage",
        "00befc28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00567964",
      "DATA",
      [
        "storage",
        "00befcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/0056794c.md#insn-00567960)
- 新版 [`00567960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/0056794c.md#insn-00567960)

~~~diff
- 00567960 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00567960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00567960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00567960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00567960 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00567960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00567960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00567960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00567960 bytes 08a13091
+ 00567960 bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ba258a7d6ed24afc54225e6a983060d"></a>

### [`00567998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567998.md) → [`00567998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567998.md) FUN_00567998

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567a74.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567a74.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "005679ac",
      "incomplete_value": false,
      "site": "005679b0",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005679ac",
      "incomplete_value": false,
      "site": "005679b0",
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
            "const:c28:8"
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
      "005679b0",
      "DATA",
      [
        "storage",
        "00befc28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005679b0",
      "DATA",
      [
        "storage",
        "00befcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005679ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567998.md#insn-005679ac)
- 新版 [`005679ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567998.md#insn-005679ac)

~~~diff
- 005679ac ["COPY", "tmp:0:8", ["const:c28:8"]]
- 005679ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005679ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005679ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005679ac ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 005679ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005679ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005679ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005679ac bytes 08a13091
+ 005679ac bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-988ca95c3c1c7e299e62ae8dfaf74087"></a>

### [`005679e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/005679e4.md) → [`005679e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005679e4.md) FUN_005679e4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 65件 [`004782e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004782e4.md) [`0054ec1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ec1c.md) [`0054ef40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054e/0054ef40.md) [`0054f220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f220.md) [`0054f3d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054f/0054f3d4.md) · 呼出先 2件 [`00565ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567a74.md)
- 新版 呼出元 65件 [`004782e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004782e4.md) [`0054ec1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054ec1c.md) [`0054ef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054e/0054ef40.md) [`0054f220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054f220.md) [`0054f3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054f/0054f3d4.md) · 呼出先 2件 [`00565ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567a74.md)

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
      "definition_site": "005679f8",
      "incomplete_value": false,
      "site": "005679fc",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005679f8",
      "incomplete_value": false,
      "site": "005679fc",
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
            "const:c28:8"
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
      "005679fc",
      "DATA",
      [
        "storage",
        "00befc28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005679fc",
      "DATA",
      [
        "storage",
        "00befcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005679f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/005679e4.md#insn-005679f8)
- 新版 [`005679f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005679e4.md#insn-005679f8)

~~~diff
- 005679f8 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 005679f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005679f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005679f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005679f8 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 005679f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005679f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005679f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005679f8 bytes 08a13091
+ 005679f8 bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4986f0d3e3f138daf6a25bb4281b859d"></a>

### [`00567a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567a28.md) → [`00567a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567a28.md) FUN_00567a28

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567a74.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00565ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565ff4.md) [`00567a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567a74.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00567a3c",
      "incomplete_value": false,
      "site": "00567a40",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567a3c",
      "incomplete_value": false,
      "site": "00567a40",
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
            "const:c28:8"
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
      "00567a40",
      "DATA",
      [
        "storage",
        "00befc28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00567a40",
      "DATA",
      [
        "storage",
        "00befcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567a28.md#insn-00567a3c)
- 新版 [`00567a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567a28.md#insn-00567a3c)

~~~diff
- 00567a3c ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00567a3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00567a3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00567a3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00567a3c ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00567a3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00567a3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00567a3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00567a3c bytes 08a13091
+ 00567a3c bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-817a3b942ab8c0ed1d335497a27563bd"></a>

### [`00567d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567d0c.md) → [`00567d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d0c.md) _INIT_33

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005679e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/005679e4.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005679e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005679e4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00567d24",
      "incomplete_value": false,
      "site": "00567d24",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567d24",
      "incomplete_value": false,
      "site": "00567d24",
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
            "const:398:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00567d24",
      "incomplete_value": false,
      "site": "00567d24",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567d24",
      "incomplete_value": false,
      "site": "00567d24",
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
            "const:c28:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00567d24",
      "incomplete_value": false,
      "site": "00567d24",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:458:8"
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
      "definition_site": "00567d24",
      "incomplete_value": false,
      "site": "00567d24",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:398:8"
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
      "00567d10",
      "PARAM",
      [
        "storage",
        "00c26398",
        null,
        "undefined8"
      ]
    ],
    [
      "00567d24",
      "WRITE",
      [
        "storage",
        "00c26398",
        null,
        "undefined8"
      ]
    ],
    [
      "00567d24",
      "DATA",
      [
        "storage",
        "00befc28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00567d10",
      "PARAM",
      [
        "storage",
        "00c26458",
        null,
        "undefined8"
      ]
    ],
    [
      "00567d24",
      "WRITE",
      [
        "storage",
        "00c26458",
        null,
        "undefined8"
      ]
    ],
    [
      "00567d24",
      "DATA",
      [
        "storage",
        "00befcd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567d0c.md#insn-00567d10) · [`00567d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567d0c.md#insn-00567d18) · [`00567d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567d0c.md#insn-00567d30)
- 新版 [`00567d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d0c.md#insn-00567d10) · [`00567d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d0c.md#insn-00567d18) · [`00567d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d0c.md#insn-00567d30)

~~~diff
- 00567d10 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00567d10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00567d10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00567d10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00567d10 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 00567d10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00567d10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00567d10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00567d10 bytes 21600e91
+ 00567d10 bytes 21601191
- 00567d18 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00567d18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00567d18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00567d18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00567d18 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00567d18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00567d18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00567d18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00567d18 bytes 08a13091
+ 00567d18 bytes 08613391
- 00567d30 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 00567d30 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00567d30 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00567d30 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00567d30 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 00567d30 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00567d30 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00567d30 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00567d30 bytes 42403b91
+ 00567d30 bytes 42003e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2826283bb43e7b939ab7be47cae2b4ed"></a>

### [`00567d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567d4c.md) → [`00567d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d4c.md) FUN_00567d4c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00559fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559fe0.md) [`0055a5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055a5bc.md) [`0055af38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055af38.md) [`0055dc58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055dc58.md) [`00565720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565720.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 5件 [`00559fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559fe0.md) [`0055a5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055a5bc.md) [`0055af38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055af38.md) [`0055dc58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055dc58.md) [`00565720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565720.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

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
      "definition_site": "00567d74",
      "incomplete_value": false,
      "site": "00567d78",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00567d74",
      "incomplete_value": false,
      "site": "00567d78",
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
            "const:d50:8"
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
      "00567d78",
      "DATA",
      [
        "storage",
        "00befd50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00567d78",
      "DATA",
      [
        "storage",
        "00befe00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00567d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567d4c.md#insn-00567d74)
- 新版 [`00567d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567d4c.md#insn-00567d74)

~~~diff
- 00567d74 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 00567d74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00567d74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00567d74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00567d74 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00567d74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00567d74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00567d74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00567d74 bytes 08413591
+ 00567d74 bytes 08013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2c62791c8bcdb300fd2c39d5a661031"></a>

### [`00568674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568674.md) → [`00568674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568674.md) FUN_00568674

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00568680",
      "incomplete_value": false,
      "site": "00568684",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568680",
      "incomplete_value": false,
      "site": "00568684",
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
            "const:d50:8"
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
      "00568684",
      "DATA",
      [
        "storage",
        "00befd50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00568684",
      "DATA",
      [
        "storage",
        "00befe00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568674.md#insn-00568680)
- 新版 [`00568680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568674.md#insn-00568680)

~~~diff
- 00568680 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 00568680 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00568680 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00568680 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00568680 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00568680 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00568680 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00568680 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00568680 bytes 29413591
+ 00568680 bytes 29013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fd692df2e750ae5fe2a27355645f402"></a>

### [`00568698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568698.md) → [`00568698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568698.md) FUN_00568698

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "005686a0",
      "incomplete_value": false,
      "site": "005686a4",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005686a0",
      "incomplete_value": false,
      "site": "005686a4",
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
            "const:d50:8"
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
      "005686a4",
      "DATA",
      [
        "storage",
        "00befd50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005686a4",
      "DATA",
      [
        "storage",
        "00befe00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005686a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568698.md#insn-005686a0)
- 新版 [`005686a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568698.md#insn-005686a0)

~~~diff
- 005686a0 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 005686a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005686a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005686a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005686a0 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 005686a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005686a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005686a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005686a0 bytes 29413591
+ 005686a0 bytes 29013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6602d22bfdc312079eb56f6bb904443"></a>

### [`005686d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/005686d8.md) → [`005686d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/005686d8.md) FUN_005686d8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "005686e4",
      "incomplete_value": false,
      "site": "005686e8",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005686e4",
      "incomplete_value": false,
      "site": "005686e8",
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
      "005686e8",
      "DATA",
      [
        "storage",
        "00befd88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005686e8",
      "DATA",
      [
        "storage",
        "00befe38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005686e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/005686d8.md#insn-005686e4)
- 新版 [`005686e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/005686d8.md#insn-005686e4)

~~~diff
- 005686e4 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 005686e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005686e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005686e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005686e4 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 005686e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005686e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005686e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005686e4 bytes 29213691
+ 005686e4 bytes 29e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9221a9ea4a60dffbd6fa8c1201af1d93"></a>

### [`005686fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/005686fc.md) → [`005686fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/005686fc.md) FUN_005686fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00568704",
      "incomplete_value": false,
      "site": "00568708",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568704",
      "incomplete_value": false,
      "site": "00568708",
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
      "00568708",
      "DATA",
      [
        "storage",
        "00befd88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00568708",
      "DATA",
      [
        "storage",
        "00befe38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/005686fc.md#insn-00568704)
- 新版 [`00568704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/005686fc.md#insn-00568704)

~~~diff
- 00568704 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 00568704 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00568704 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00568704 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00568704 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 00568704 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00568704 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00568704 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00568704 bytes 29213691
+ 00568704 bytes 29e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f26449a76af2192098e1d66c6ba86c24"></a>

### [`0056873c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/0056873c.md) → [`0056873c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/0056873c.md) FUN_0056873c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00567e94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567e94.md) [`00567ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/00567ef0.md) [`00568064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568064.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 3件 [`00567e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567e94.md) [`00567ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/00567ef0.md) [`00568064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568064.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00568764",
      "incomplete_value": false,
      "site": "0056876c",
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
      "definition_site": "00568764",
      "incomplete_value": false,
      "site": "0056876c",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00568778",
      "incomplete_value": false,
      "site": "00568778",
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
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568778",
      "incomplete_value": false,
      "site": "00568778",
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
            "const:d50:8"
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
      "0056876c",
      "DATA",
      [
        "storage",
        "00bef1a0",
        null,
        "pointer"
      ]
    ],
    [
      "00568778",
      "DATA",
      [
        "storage",
        "00befd50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056876c",
      "DATA",
      [
        "storage",
        "00bef250",
        null,
        "pointer"
      ]
    ],
    [
      "00568778",
      "DATA",
      [
        "storage",
        "00befe00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/0056873c.md#insn-00568764) · [`00568768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/0056873c.md#insn-00568768)
- 新版 [`00568764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/0056873c.md#insn-00568764) · [`00568768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/0056873c.md#insn-00568768)

~~~diff
- 00568764 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 00568764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00568764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00568764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00568764 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 00568764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00568764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00568764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00568764 bytes 08810691
+ 00568764 bytes 08410991
- 00568768 ["COPY", "register:40c0:8", ["register:4000:8"]]
- 00568768 bytes f80300aa
+ 00568768 ["COPY", "register:40c0:8", ["register:4000:8"]]
+ 00568768 bytes f80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-643bf9212e527ef3653885269a44080d"></a>

### [`0056891c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/0056891c.md) → [`0056891c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/0056891c.md) FUN_0056891c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`005682f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/005682f8.md) [`0056839c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/0056839c.md) [`00568510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568510.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 3件 [`005682f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/005682f8.md) [`0056839c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/0056839c.md) [`00568510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568510.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00568944",
      "incomplete_value": false,
      "site": "0056894c",
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
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568944",
      "incomplete_value": false,
      "site": "0056894c",
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
            "const:e28:8"
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
      "definition_site": "00568958",
      "incomplete_value": false,
      "site": "00568958",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568958",
      "incomplete_value": false,
      "site": "00568958",
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
            "const:d88:8"
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
      "0056894c",
      "DATA",
      [
        "storage",
        "00befe28",
        null,
        "undefined *"
      ]
    ],
    [
      "00568958",
      "DATA",
      [
        "storage",
        "00befd88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056894c",
      "DATA",
      [
        "storage",
        "00befed8",
        null,
        "undefined *"
      ]
    ],
    [
      "00568958",
      "DATA",
      [
        "storage",
        "00befe38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/0056891c.md#insn-00568944) · [`00568948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/0056891c.md#insn-00568948)
- 新版 [`00568944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/0056891c.md#insn-00568944) · [`00568948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/0056891c.md#insn-00568948)

~~~diff
- 00568944 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00568944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00568944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00568944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00568944 ["COPY", "tmp:0:8", ["const:ed8:8"]]
+ 00568944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00568944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00568944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00568944 bytes 08a13891
+ 00568944 bytes 08613b91
- 00568948 ["COPY", "register:40c0:8", ["register:4000:8"]]
- 00568948 bytes f80300aa
+ 00568948 ["COPY", "register:40c0:8", ["register:4000:8"]]
+ 00568948 bytes f80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebbe520406672aabd6e7877d0797313a"></a>

### [`005689f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/005689f4.md) → [`005689f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/005689f4.md) FUN_005689f4

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
      "definition_site": "005689f8",
      "incomplete_value": false,
      "site": "005689fc",
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
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005689f8",
      "incomplete_value": false,
      "site": "005689fc",
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
            "const:e28:8"
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
      "005689fc",
      "DATA",
      [
        "storage",
        "00befe28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005689fc",
      "DATA",
      [
        "storage",
        "00befed8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005689f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/005689f4.md#insn-005689f8)
- 新版 [`005689f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/005689f4.md#insn-005689f8)

~~~diff
- 005689f8 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 005689f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005689f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005689f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005689f8 ["COPY", "tmp:0:8", ["const:ed8:8"]]
+ 005689f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005689f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005689f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005689f8 bytes 08a13891
+ 005689f8 bytes 08613b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-465bf95c89a6ae72c931ba34c046be1c"></a>

### [`00568a04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568a04.md) → [`00568a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568a04.md) FUN_00568a04

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
      "definition_site": "00568a14",
      "incomplete_value": false,
      "site": "00568a1c",
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
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568a14",
      "incomplete_value": false,
      "site": "00568a1c",
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
            "const:e28:8"
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
      "00568a1c",
      "DATA",
      [
        "storage",
        "00befe28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00568a1c",
      "DATA",
      [
        "storage",
        "00befed8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568a04.md#insn-00568a14)
- 新版 [`00568a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568a04.md#insn-00568a14)

~~~diff
- 00568a14 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00568a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00568a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00568a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00568a14 ["COPY", "tmp:0:8", ["const:ed8:8"]]
+ 00568a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00568a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00568a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00568a14 bytes 08a13891
+ 00568a14 bytes 08613b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6628f96994070b055b7a8c09cb1942e"></a>

### [`00568a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568a6c.md) → [`00568a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568a6c.md) FUN_00568a6c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574748.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00574748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574748.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.25% / 新版 94.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00568ac0",
      "incomplete_value": true,
      "site": "00568ac0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:326:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568ac0",
      "incomplete_value": true,
      "site": "00568ac0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ba:8"
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
      "definition_site": "00568ac8",
      "incomplete_value": true,
      "site": "00568ac8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00568ac8",
      "incomplete_value": true,
      "site": "00568ac8",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00568aa8",
      "READ",
      [
        "storage",
        "002a83ba",
        null,
        "string"
      ]
    ],
    [
      "00568ab0",
      "READ",
      [
        "storage",
        "002a83c0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00568aa8",
      "READ",
      [
        "storage",
        "002a8326",
        null,
        "string"
      ]
    ],
    [
      "00568ab0",
      "READ",
      [
        "storage",
        "002a832c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568a6c.md#insn-00568aa4)
- 新版 [`00568aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568a6c.md#insn-00568aa4)

~~~diff
- 00568aa4 ["COPY", "tmp:0:8", ["const:3ba:8"]]
- 00568aa4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00568aa4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00568aa4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00568aa4 ["COPY", "tmp:0:8", ["const:326:8"]]
+ 00568aa4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00568aa4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00568aa4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00568aa4 bytes 29e90e91
+ 00568aa4 bytes 29990c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a0346f579ba44c141eb51c406f247f9"></a>

### [`00568c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568c04.md) → [`00568c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568c04.md) FUN_00568c04

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0057474c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/0057474c.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0057474c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057474c.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "00568c5c",
      "incomplete_value": true,
      "site": "00568c5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b34:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568c5c",
      "incomplete_value": true,
      "site": "00568c5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
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
      "00568c4c",
      "READ",
      [
        "storage",
        "002adbc8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00568c4c",
      "READ",
      [
        "storage",
        "002adb34",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568c04.md#insn-00568c48)
- 新版 [`00568c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568c04.md#insn-00568c48)

~~~diff
- 00568c48 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 00568c48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00568c48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00568c48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00568c48 ["COPY", "tmp:0:8", ["const:b34:8"]]
+ 00568c48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00568c48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00568c48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00568c48 bytes 08212f91
+ 00568c48 bytes 08d12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76ba66c1df90279d9ee0925ca5a4e4a3"></a>

### [`00568da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568da0.md) → [`00568da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568da0.md) FUN_00568da0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574750.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00574750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574750.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00568df4",
      "incomplete_value": true,
      "site": "00568df4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aac:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568df4",
      "incomplete_value": true,
      "site": "00568df4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1f:8"
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
      "definition_site": "00568e08",
      "incomplete_value": true,
      "site": "00568e10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568e08",
      "incomplete_value": true,
      "site": "00568e10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4f6:8"
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
      "definition_site": "00568e14",
      "incomplete_value": true,
      "site": "00568e14",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00568e14",
      "incomplete_value": true,
      "site": "00568e14",
      "value": [
        "LOAD",
        "8",
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
      "00568de8",
      "READ",
      [
        "storage",
        "00294a1f",
        null,
        "string"
      ]
    ],
    [
      "00568e08",
      "READ",
      [
        "storage",
        "002a34f6",
        null,
        "string"
      ]
    ],
    [
      "00568e0c",
      "READ",
      [
        "storage",
        "002a3503",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00568de8",
      "READ",
      [
        "storage",
        "00294aac",
        null,
        "string"
      ]
    ],
    [
      "00568e08",
      "READ",
      [
        "storage",
        "002a34ef",
        null,
        "string"
      ]
    ],
    [
      "00568e0c",
      "READ",
      [
        "storage",
        "002a34fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568da0.md#insn-00568de4) · [`00568e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568da0.md#insn-00568e04)
- 新版 [`00568de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568da0.md#insn-00568de4) · [`00568e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568da0.md#insn-00568e04)

~~~diff
- 00568de4 ["COPY", "tmp:0:8", ["const:a1f:8"]]
- 00568de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00568de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00568de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00568de4 ["COPY", "tmp:0:8", ["const:aac:8"]]
+ 00568de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00568de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00568de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00568de4 bytes 087d2891
+ 00568de4 bytes 08b12a91
- 00568e04 ["COPY", "tmp:0:8", ["const:4f6:8"]]
- 00568e04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00568e04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00568e04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00568e04 ["COPY", "tmp:0:8", ["const:4ef:8"]]
+ 00568e04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00568e04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00568e04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00568e04 bytes 08d91391
+ 00568e04 bytes 08bd1391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02b253d84820c0760388d2fc8f8b6f41"></a>

### [`00568f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568f64.md) → [`00568f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568f64.md) FUN_00568f64

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00574758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574758.md) · 呼出先 9件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00574758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574758.md) · 呼出先 9件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.77% / 新版 92.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00568fac",
      "incomplete_value": true,
      "site": "00568fb8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00568fac",
      "incomplete_value": true,
      "site": "00568fb8",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00568fa8",
      "incomplete_value": true,
      "site": "00568fc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9f5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00568fa8",
      "incomplete_value": true,
      "site": "00568fc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:968:8"
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
      "00568fa8",
      "READ",
      [
        "storage",
        "00292968",
        null,
        "string"
      ]
    ],
    [
      "00568fac",
      "READ",
      [
        "storage",
        "00292978",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00568fa8",
      "READ",
      [
        "storage",
        "002929f5",
        null,
        "string"
      ]
    ],
    [
      "00568fac",
      "READ",
      [
        "storage",
        "00292a05",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00568fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568f64.md#insn-00568fa0) · [`00568fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00568/00568f64.md#insn-00568fa4)
- 新版 [`00568fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568f64.md#insn-00568fa0) · [`00568fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00568/00568f64.md#insn-00568fa4)

~~~diff
- 00568fa0 ["COPY", "tmp:0:8", ["const:968:8"]]
- 00568fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00568fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00568fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00568fa0 ["COPY", "tmp:0:8", ["const:9f5:8"]]
+ 00568fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00568fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00568fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00568fa0 bytes 08a12591
+ 00568fa0 bytes 08d52791
- 00568fa4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00568fa4 bytes 49eaff90
+ 00568fa4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 00568fa4 bytes 49eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-398c768fb4ea4586e70e9f5ab6b05f19"></a>

### [`005690ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/005690ec.md) → [`005690ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/005690ec.md) FUN_005690ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574754.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00574754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574754.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

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
      "definition_site": "00569154",
      "incomplete_value": true,
      "site": "0056915c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569154",
      "incomplete_value": true,
      "site": "0056915c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4f6:8"
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
      "definition_site": "00569160",
      "incomplete_value": true,
      "site": "00569160",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00569160",
      "incomplete_value": true,
      "site": "00569160",
      "value": [
        "LOAD",
        "8",
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
      "00569154",
      "READ",
      [
        "storage",
        "002a34f6",
        null,
        "string"
      ]
    ],
    [
      "00569158",
      "READ",
      [
        "storage",
        "002a3503",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00569154",
      "READ",
      [
        "storage",
        "002a34ef",
        null,
        "string"
      ]
    ],
    [
      "00569158",
      "READ",
      [
        "storage",
        "002a34fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00569150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/005690ec.md#insn-00569150)
- 新版 [`00569150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/005690ec.md#insn-00569150)

~~~diff
- 00569150 ["COPY", "tmp:0:8", ["const:4f6:8"]]
- 00569150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00569150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00569150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00569150 ["COPY", "tmp:0:8", ["const:4ef:8"]]
+ 00569150 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00569150 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00569150 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00569150 bytes 08d91391
+ 00569150 bytes 08bd1391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1f251c6ba0aedaad367ee83e1b0180c"></a>

### [`005692b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/005692b0.md) → [`005692b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/005692b0.md) FUN_005692b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0057475c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/0057475c.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0057475c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057475c.md) · 呼出先 11件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005692ec",
      "incomplete_value": true,
      "site": "00569304",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005692ec",
      "incomplete_value": true,
      "site": "00569304",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:663:8"
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
      "definition_site": "00569308",
      "incomplete_value": true,
      "site": "00569314",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:725:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569308",
      "incomplete_value": true,
      "site": "00569314",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:71f:8"
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
      "definition_site": "00569318",
      "incomplete_value": true,
      "site": "00569318",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00569318",
      "incomplete_value": true,
      "site": "00569318",
      "value": [
        "LOAD",
        "8",
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
      "005692ec",
      "READ",
      [
        "storage",
        "002a0663",
        null,
        "string"
      ]
    ],
    [
      "00569308",
      "READ",
      [
        "storage",
        "002aa71f",
        null,
        "string"
      ]
    ],
    [
      "0056930c",
      "READ",
      [
        "storage",
        "002aa72c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005692ec",
      "READ",
      [
        "storage",
        "002a06f0",
        null,
        "string"
      ]
    ],
    [
      "00569308",
      "READ",
      [
        "storage",
        "002aa725",
        null,
        "string"
      ]
    ],
    [
      "0056930c",
      "READ",
      [
        "storage",
        "002aa732",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005692e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/005692b0.md#insn-005692e8) · [`00569300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/005692b0.md#insn-00569300)
- 新版 [`005692e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/005692b0.md#insn-005692e8) · [`00569300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/005692b0.md#insn-00569300)

~~~diff
- 005692e8 ["COPY", "tmp:0:8", ["const:663:8"]]
- 005692e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005692e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005692e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005692e8 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 005692e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005692e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005692e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005692e8 bytes 298d1991
+ 005692e8 bytes 29c11b91
- 00569300 ["COPY", "tmp:0:8", ["const:71f:8"]]
- 00569300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00569300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00569300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00569300 ["COPY", "tmp:0:8", ["const:725:8"]]
+ 00569300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00569300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00569300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00569300 bytes 087d1c91
+ 00569300 bytes 08951c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6be729c71bef30c6c8c624afe71cc64a"></a>

### [`00569418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/00569418.md) → [`00569418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569418.md) FUN_00569418

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00574760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574760.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00574760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574760.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00569468",
      "incomplete_value": true,
      "site": "00569468",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569468",
      "incomplete_value": true,
      "site": "00569468",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
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
      "00569458",
      "READ",
      [
        "storage",
        "00297c88",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00569458",
      "READ",
      [
        "storage",
        "00297d15",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00569450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/00569418.md#insn-00569450)
- 新版 [`00569450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569418.md#insn-00569450)

~~~diff
- 00569450 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00569450 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00569450 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00569450 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00569450 ["COPY", "tmp:0:8", ["const:d15:8"]]
+ 00569450 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00569450 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00569450 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00569450 bytes 29213291
+ 00569450 bytes 29553491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47a91674b1bb9a833863903a4e4001b0"></a>

### [`00569550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/00569550.md) → [`00569550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569550.md) FUN_00569550

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00574768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574768.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`005596c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/005596c4.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 1件 [`00574768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574768.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`005596c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/005596c4.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00569578",
      "incomplete_value": false,
      "site": "00569584",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569578",
      "incomplete_value": false,
      "site": "00569584",
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
            "const:3d8:8"
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
      "definition_site": "00569580",
      "incomplete_value": true,
      "site": "00569584",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569580",
      "incomplete_value": true,
      "site": "00569584",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
      "00569578",
      "PARAM",
      [
        "storage",
        "00c263d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00569580",
      "READ",
      [
        "storage",
        "00c263e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00569588",
      "WRITE",
      [
        "storage",
        "00c263d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00569578",
      "PARAM",
      [
        "storage",
        "00c26498",
        null,
        "undefined8"
      ]
    ],
    [
      "00569580",
      "READ",
      [
        "storage",
        "00c264a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00569588",
      "WRITE",
      [
        "storage",
        "00c26498",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056956c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/00569550.md#insn-0056956c)
- 新版 [`0056956c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569550.md#insn-0056956c)

~~~diff
- 0056956c ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 0056956c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0056956c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0056956c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0056956c ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0056956c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0056956c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0056956c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0056956c bytes 73620f91
+ 0056956c bytes 73621291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2181e0f20b63d242e79c2385658ba50"></a>

### [`0056968c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/0056968c.md) → [`0056968c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/0056968c.md) FUN_0056968c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0057476c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/0057476c.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0057476c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057476c.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005696dc",
      "incomplete_value": true,
      "site": "005696dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:76d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005696dc",
      "incomplete_value": true,
      "site": "005696dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:776:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00569758",
      "incomplete_value": true,
      "site": "00569758",
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
      "definition_site": "00569758",
      "incomplete_value": true,
      "site": "00569758",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00569824",
      "incomplete_value": false,
      "site": "00569828",
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
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569824",
      "incomplete_value": false,
      "site": "00569828",
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
            "const:3f0:8"
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
      "005696d0",
      "READ",
      [
        "storage",
        "002a9776",
        null,
        "string"
      ]
    ],
    [
      "00569740",
      "PARAM",
      [
        "storage",
        "00c263f0",
        null,
        null
      ]
    ],
    [
      "00569750",
      "READ",
      [
        "storage",
        "00c263e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005696d0",
      "READ",
      [
        "storage",
        "002a976d",
        null,
        "string"
      ]
    ],
    [
      "00569740",
      "PARAM",
      [
        "storage",
        "00c264b0",
        null,
        null
      ]
    ],
    [
      "00569750",
      "READ",
      [
        "storage",
        "00c264a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005696c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/0056968c.md#insn-005696c8) · [`00569740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/0056968c.md#insn-00569740) · [`00569750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/0056968c.md#insn-00569750)
- 新版 [`005696c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/0056968c.md#insn-005696c8) · [`00569740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/0056968c.md#insn-00569740) · [`00569750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/0056968c.md#insn-00569750)

~~~diff
- 005696c8 ["COPY", "tmp:0:8", ["const:776:8"]]
- 005696c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005696c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005696c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005696c8 ["COPY", "tmp:0:8", ["const:76d:8"]]
+ 005696c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005696c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005696c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005696c8 bytes 29d91d91
+ 005696c8 bytes 29b51d91
- 00569740 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00569740 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00569740 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00569740 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00569740 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 00569740 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00569740 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00569740 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00569740 bytes 00c00f91
+ 00569740 bytes 00c01291
- 00569750 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:3e0:8"]]
- 00569750 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00569750 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:4a0:8"]]
+ 00569750 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00569750 bytes c8f241f9
+ 00569750 bytes c85242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecb8c9e4a230b9daaaac994c78bca40c"></a>

### [`005698ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/005698ec.md) → [`005698ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/005698ec.md) FUN_005698ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574770.md) · 呼出先 6件 [`00471738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471738.md) [`00558fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558fd0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb190.md)
- 新版 呼出元 1件 [`00574770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574770.md) · 呼出先 6件 [`00471738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471738.md) [`00558fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558fd0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.16% / 新版 94.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00569a44",
      "incomplete_value": true,
      "site": "00569a44",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569a44",
      "incomplete_value": true,
      "site": "00569a44",
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
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00569930",
      "incomplete_value": true,
      "site": "00569930",
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
      "definition_site": "00569930",
      "incomplete_value": true,
      "site": "00569930",
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
      "definition_site": "00569a40",
      "incomplete_value": true,
      "site": "00569a40",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "00569a40",
      "incomplete_value": true,
      "site": "00569a40",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056991c",
      "PARAM",
      [
        "storage",
        "00c263f0",
        null,
        null
      ]
    ],
    [
      "0056992c",
      "READ",
      [
        "storage",
        "00c263e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00569984",
      "READ",
      [
        "storage",
        "00c26430",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056991c",
      "PARAM",
      [
        "storage",
        "00c264b0",
        null,
        null
      ]
    ],
    [
      "0056992c",
      "READ",
      [
        "storage",
        "00c264a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00569984",
      "READ",
      [
        "storage",
        "00c264f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00569a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/005698ec.md#insn-00569a44) · [`0056991c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/005698ec.md#insn-0056991c) · [`00569928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/005698ec.md#insn-00569928)
- 新版 [`00569a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/005698ec.md#insn-00569a44) · [`0056991c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/005698ec.md#insn-0056991c) · [`00569928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/005698ec.md#insn-00569928)

~~~diff
- 00569a44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:3d8:8"]]
- 00569a44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00569a44 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:498:8"]]
+ 00569a44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00569a44 bytes 28ed01f9
+ 00569a44 bytes 284d02f9
- 0056991c ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 0056991c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0056991c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0056991c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0056991c ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 0056991c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0056991c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0056991c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0056991c bytes 00c00f91
+ 0056991c bytes 00c01291
- 00569928 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 00569928 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00569928 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00569928 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00569928 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 00569928 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00569928 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00569928 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00569928 bytes d6820f91
+ 00569928 bytes d6821291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47a9f51a10b4e74379850600a9a3bd87"></a>

### [`00569b74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/00569b74.md) → [`00569b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569b74.md) FUN_00569b74

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574774.md) · 呼出先 13件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md)
- 新版 呼出元 1件 [`00574774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574774.md) · 呼出先 13件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00569bc8",
      "incomplete_value": true,
      "site": "00569bc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c74:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569bc8",
      "incomplete_value": true,
      "site": "00569bc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be7:8"
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
      "00569bbc",
      "READ",
      [
        "storage",
        "00296be7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00569bbc",
      "READ",
      [
        "storage",
        "00296c74",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00569bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/00569b74.md#insn-00569bb8)
- 新版 [`00569bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569b74.md#insn-00569bb8)

~~~diff
- 00569bb8 ["COPY", "tmp:0:8", ["const:be7:8"]]
- 00569bb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00569bb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00569bb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00569bb8 ["COPY", "tmp:0:8", ["const:c74:8"]]
+ 00569bb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00569bb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00569bb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00569bb8 bytes 089d2f91
+ 00569bb8 bytes 08d13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81c0ad5ef179f38974fdc330f692baee"></a>

### [`00569dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/00569dd8.md) → [`00569dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569dd8.md) FUN_00569dd8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0057477c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/0057477c.md) · 呼出先 13件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`0057477c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057477c.md) · 呼出先 13件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.17% / 新版 95.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00569e60",
      "incomplete_value": true,
      "site": "00569e70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:572:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569e60",
      "incomplete_value": true,
      "site": "00569e70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e5:8"
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
      "definition_site": "00569e60",
      "incomplete_value": true,
      "site": "00569e70",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00569e60",
      "incomplete_value": true,
      "site": "00569e70",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00569e74",
      "incomplete_value": true,
      "site": "00569e7c",
      "value": [
        "LOAD",
        "16",
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
                "const:1b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00569e74",
      "incomplete_value": true,
      "site": "00569e7c",
      "value": [
        "LOAD",
        "16",
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
                "const:1b:8"
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
      "00569e60",
      "READ",
      [
        "storage",
        "0029b4e5",
        null,
        "string"
      ]
    ],
    [
      "00569e60",
      "READ",
      [
        "storage",
        "0029b4f5",
        null,
        "string"
      ]
    ],
    [
      "00569e74",
      "READ",
      [
        "storage",
        "0029b500",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00569e60",
      "READ",
      [
        "storage",
        "0029b572",
        null,
        "string"
      ]
    ],
    [
      "00569e60",
      "READ",
      [
        "storage",
        "0029b582",
        null,
        "string"
      ]
    ],
    [
      "00569e74",
      "READ",
      [
        "storage",
        "0029b58d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00569e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/00569dd8.md#insn-00569e58) · [`00569e5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/00569dd8.md#insn-00569e5c)
- 新版 [`00569e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569dd8.md#insn-00569e58) · [`00569e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569dd8.md#insn-00569e5c)

~~~diff
- 00569e58 ["COPY", "tmp:0:8", ["const:4e5:8"]]
- 00569e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00569e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00569e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00569e58 ["COPY", "tmp:0:8", ["const:572:8"]]
+ 00569e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00569e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00569e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00569e58 bytes 08951391
+ 00569e58 bytes 08c91591
- 00569e5c ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00569e5c bytes 49eaff90
+ 00569e5c ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00569e5c bytes 49eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51eaa88d2bad9483886ab0bcd2a065b2"></a>

### [`0056a080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056a080.md) → [`0056a080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056a080.md) FUN_0056a080

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00574780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574780.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00574780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574780.md) · 呼出先 12件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056a0d4",
      "incomplete_value": true,
      "site": "0056a0d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056a0d4",
      "incomplete_value": true,
      "site": "0056a0d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf3:8"
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
      "definition_site": "0056a0e0",
      "incomplete_value": true,
      "site": "0056a0f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:725:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056a0e0",
      "incomplete_value": true,
      "site": "0056a0f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:71f:8"
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
      "definition_site": "0056a0f4",
      "incomplete_value": true,
      "site": "0056a0f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0056a0f4",
      "incomplete_value": true,
      "site": "0056a0f4",
      "value": [
        "LOAD",
        "8",
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
      "0056a0c0",
      "READ",
      [
        "storage",
        "00291bf3",
        null,
        "string"
      ]
    ],
    [
      "0056a0e0",
      "READ",
      [
        "storage",
        "002aa71f",
        null,
        "string"
      ]
    ],
    [
      "0056a0e8",
      "READ",
      [
        "storage",
        "002aa72c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056a0c0",
      "READ",
      [
        "storage",
        "00291c80",
        null,
        "string"
      ]
    ],
    [
      "0056a0e0",
      "READ",
      [
        "storage",
        "002aa725",
        null,
        "string"
      ]
    ],
    [
      "0056a0e8",
      "READ",
      [
        "storage",
        "002aa732",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056a0b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056a080.md#insn-0056a0b8) · [`0056a0d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056a080.md#insn-0056a0d8)
- 新版 [`0056a0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056a080.md#insn-0056a0b8) · [`0056a0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056a080.md#insn-0056a0d8)

~~~diff
- 0056a0b8 ["COPY", "tmp:0:8", ["const:bf3:8"]]
- 0056a0b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056a0b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056a0b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056a0b8 ["COPY", "tmp:0:8", ["const:c80:8"]]
+ 0056a0b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056a0b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056a0b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056a0b8 bytes 29cd2f91
+ 0056a0b8 bytes 29013291
- 0056a0d8 ["COPY", "register:4048:8", ["const:2aa000:8"]]
- 0056a0d8 bytes 09eaff90
+ 0056a0d8 ["COPY", "register:4048:8", ["const:2aa000:8"]]
+ 0056a0d8 bytes 09eaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3def05a25ba2f19fc289f36e71887500"></a>

### [`0056a298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056a298.md) → [`0056a298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056a298.md) FUN_0056a298

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056bde8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056bde8.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566290.md)
- 新版 呼出元 1件 [`0056bde8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056bde8.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056a314",
      "incomplete_value": true,
      "site": "0056a32c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d22:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056a314",
      "incomplete_value": true,
      "site": "0056a32c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c95:8"
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
      "0056a2d4",
      "DATA",
      [
        "storage",
        "00befe78",
        null,
        "undefined *"
      ]
    ],
    [
      "0056a314",
      "READ",
      [
        "storage",
        "00297c95",
        null,
        "string"
      ]
    ],
    [
      "0056a348",
      "READ",
      [
        "storage",
        "00291bfd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056a2d4",
      "DATA",
      [
        "storage",
        "00beff28",
        null,
        "undefined *"
      ]
    ],
    [
      "0056a314",
      "READ",
      [
        "storage",
        "00297d22",
        null,
        "string"
      ]
    ],
    [
      "0056a348",
      "READ",
      [
        "storage",
        "00291c8a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056a2bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056a298.md#insn-0056a2bc) · [`0056a30c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056a298.md#insn-0056a30c) · [`0056a340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056a298.md#insn-0056a340)
- 新版 [`0056a2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056a298.md#insn-0056a2bc) · [`0056a30c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056a298.md#insn-0056a30c) · [`0056a340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056a298.md#insn-0056a340)

~~~diff
- 0056a2bc ["COPY", "tmp:0:8", ["const:e78:8"]]
- 0056a2bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056a2bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056a2bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056a2bc ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 0056a2bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056a2bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056a2bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056a2bc bytes 29e13991
+ 0056a2bc bytes 29a13c91
- 0056a30c ["COPY", "tmp:0:8", ["const:c95:8"]]
- 0056a30c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056a30c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056a30c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056a30c ["COPY", "tmp:0:8", ["const:d22:8"]]
+ 0056a30c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056a30c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056a30c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056a30c bytes 29553291
+ 0056a30c bytes 29893491
- 0056a340 ["COPY", "tmp:0:8", ["const:bfd:8"]]
- 0056a340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056a340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056a340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056a340 ["COPY", "tmp:0:8", ["const:c8a:8"]]
+ 0056a340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056a340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056a340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056a340 bytes 08f52f91
+ 0056a340 bytes 08293291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8fdbe5aa5e8e8bd5ae1550a6f2fd01c"></a>

### [`0056a900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056a900.md) → [`0056a900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056a900.md) FUN_0056a900

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566968.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056a95c",
      "incomplete_value": true,
      "site": "0056a95c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056a95c",
      "incomplete_value": true,
      "site": "0056a95c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:53c:8"
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
      "0056a950",
      "READ",
      [
        "storage",
        "0029d53c",
        null,
        "string"
      ]
    ],
    [
      "0056a970",
      "READ",
      [
        "storage",
        "0029f5dd",
        null,
        "string"
      ]
    ],
    [
      "0056a974",
      "READ",
      [
        "storage",
        "0029f5eb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056a950",
      "READ",
      [
        "storage",
        "0029d5c9",
        null,
        "string"
      ]
    ],
    [
      "0056a970",
      "READ",
      [
        "storage",
        "0029f66a",
        null,
        "string"
      ]
    ],
    [
      "0056a974",
      "READ",
      [
        "storage",
        "0029f678",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056a94c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056a900.md#insn-0056a94c) · [`0056a96c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056a900.md#insn-0056a96c)
- 新版 [`0056a94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056a900.md#insn-0056a94c) · [`0056a96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056a900.md#insn-0056a96c)

~~~diff
- 0056a94c ["COPY", "tmp:0:8", ["const:53c:8"]]
- 0056a94c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056a94c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056a94c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056a94c ["COPY", "tmp:0:8", ["const:5c9:8"]]
+ 0056a94c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056a94c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056a94c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056a94c bytes 08f11491
+ 0056a94c bytes 08251791
- 0056a96c ["COPY", "tmp:0:8", ["const:5dd:8"]]
- 0056a96c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056a96c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056a96c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056a96c ["COPY", "tmp:0:8", ["const:66a:8"]]
+ 0056a96c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056a96c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056a96c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056a96c bytes 08751791
+ 0056a96c bytes 08a91991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f592cc73ca838e14dec289dca35ff3b"></a>

### [`0056aad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056aad8.md) → [`0056aad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056aad8.md) FUN_0056aad8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00558f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00558f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558f34.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566968.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056ab4c",
      "incomplete_value": true,
      "site": "0056ab58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:78b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ab4c",
      "incomplete_value": true,
      "site": "0056ab58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:785:8"
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
      "definition_site": "0056ab5c",
      "incomplete_value": true,
      "site": "0056ab5c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0056ab5c",
      "incomplete_value": true,
      "site": "0056ab5c",
      "value": [
        "LOAD",
        "8",
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
      "0056ab4c",
      "READ",
      [
        "storage",
        "002aa785",
        null,
        "string"
      ]
    ],
    [
      "0056ab50",
      "READ",
      [
        "storage",
        "002aa793",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056ab4c",
      "READ",
      [
        "storage",
        "002aa78b",
        null,
        "string"
      ]
    ],
    [
      "0056ab50",
      "READ",
      [
        "storage",
        "002aa799",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ab48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056aad8.md#insn-0056ab48)
- 新版 [`0056ab48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056aad8.md#insn-0056ab48)

~~~diff
- 0056ab48 ["COPY", "tmp:0:8", ["const:785:8"]]
- 0056ab48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056ab48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056ab48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056ab48 ["COPY", "tmp:0:8", ["const:78b:8"]]
+ 0056ab48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056ab48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056ab48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056ab48 bytes 29151e91
+ 0056ab48 bytes 292d1e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10c9a8df1ce6cea0b3b0b1337cab1689"></a>

### [`0056acb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056acb4.md) → [`0056acb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056acb4.md) FUN_0056acb4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566968.md) [`00566978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566978.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566968.md) [`00566978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566978.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.90% / 新版 94.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056ad28",
      "incomplete_value": true,
      "site": "0056ad30",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:ab7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ad28",
      "incomplete_value": true,
      "site": "0056ad30",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:a2a:8"
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
      "definition_site": "0056ad34",
      "incomplete_value": true,
      "site": "0056ad34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0056ad34",
      "incomplete_value": true,
      "site": "0056ad34",
      "value": [
        "LOAD",
        "8",
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
      "0056ad28",
      "READ",
      [
        "storage",
        "00294a2a",
        null,
        "string"
      ]
    ],
    [
      "0056ad2c",
      "READ",
      [
        "storage",
        "00294a38",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056ad28",
      "READ",
      [
        "storage",
        "00294ab7",
        null,
        "string"
      ]
    ],
    [
      "0056ad2c",
      "READ",
      [
        "storage",
        "00294ac5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ad24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056acb4.md#insn-0056ad24)
- 新版 [`0056ad24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056acb4.md#insn-0056ad24)

~~~diff
- 0056ad24 ["COPY", "tmp:0:8", ["const:a2a:8"]]
- 0056ad24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056ad24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056ad24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056ad24 ["COPY", "tmp:0:8", ["const:ab7:8"]]
+ 0056ad24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056ad24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056ad24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056ad24 bytes 08a92891
+ 0056ad24 bytes 08dd2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51eda590babeaca798c5224f6558c0cf"></a>

### [`0056ae88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056ae88.md) → [`0056ae88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056ae88.md) FUN_0056ae88

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 11件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566968.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.85% / 新版 94.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056aef8",
      "incomplete_value": true,
      "site": "0056af00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d37:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056aef8",
      "incomplete_value": true,
      "site": "0056af00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:caa:8"
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
      "definition_site": "0056af04",
      "incomplete_value": true,
      "site": "0056af04",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0056af04",
      "incomplete_value": true,
      "site": "0056af04",
      "value": [
        "LOAD",
        "8",
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
      "0056aef8",
      "READ",
      [
        "storage",
        "00297caa",
        null,
        "string"
      ]
    ],
    [
      "0056aefc",
      "READ",
      [
        "storage",
        "00297cb8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056aef8",
      "READ",
      [
        "storage",
        "00297d37",
        null,
        "string"
      ]
    ],
    [
      "0056aefc",
      "READ",
      [
        "storage",
        "00297d45",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056aef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056ae88.md#insn-0056aef4)
- 新版 [`0056aef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056ae88.md#insn-0056aef4)

~~~diff
- 0056aef4 ["COPY", "tmp:0:8", ["const:caa:8"]]
- 0056aef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056aef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056aef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056aef4 ["COPY", "tmp:0:8", ["const:d37:8"]]
+ 0056aef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056aef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056aef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056aef4 bytes 08a93291
+ 0056aef4 bytes 08dd3491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89ecc5bd24c0a1dbc543a984f80fb179"></a>

### [`0056b058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b058.md) → [`0056b058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b058.md) FUN_0056b058

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566968.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.06% / 新版 91.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b0b4",
      "incomplete_value": true,
      "site": "0056b0b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d4e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b0b4",
      "incomplete_value": true,
      "site": "0056b0b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc1:8"
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
      "definition_site": "0056b0d0",
      "incomplete_value": true,
      "site": "0056b0e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b0d0",
      "incomplete_value": true,
      "site": "0056b0e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:652:8"
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
      "definition_site": "0056b0d0",
      "incomplete_value": true,
      "site": "0056b0e0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056b0d0",
      "incomplete_value": true,
      "site": "0056b0e0",
      "value": [
        "LOAD",
        "16",
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
      "0056b0a4",
      "READ",
      [
        "storage",
        "00297cc1",
        null,
        "string"
      ]
    ],
    [
      "0056b0d0",
      "READ",
      [
        "storage",
        "0029c652",
        null,
        "string"
      ]
    ],
    [
      "0056b0d0",
      "READ",
      [
        "storage",
        "0029c662",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056b0a4",
      "READ",
      [
        "storage",
        "00297d4e",
        null,
        "string"
      ]
    ],
    [
      "0056b0d0",
      "READ",
      [
        "storage",
        "0029c6df",
        null,
        "string"
      ]
    ],
    [
      "0056b0d0",
      "READ",
      [
        "storage",
        "0029c6ef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b09c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b058.md#insn-0056b09c) · [`0056b0c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b058.md#insn-0056b0c8) · [`0056b0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b058.md#insn-0056b0cc)
- 新版 [`0056b09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b058.md#insn-0056b09c) · [`0056b0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b058.md#insn-0056b0c8)

~~~diff
- 0056b09c ["COPY", "tmp:0:8", ["const:cc1:8"]]
- 0056b09c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056b09c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056b09c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056b09c ["COPY", "tmp:0:8", ["const:d4e:8"]]
+ 0056b09c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056b09c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056b09c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056b09c bytes 29053391
+ 0056b09c bytes 29393591
- 0056b0c8 ["COPY", "tmp:0:8", ["const:652:8"]]
- 0056b0c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056b0c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056b0c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056b0c8 ["COPY", "tmp:0:8", ["const:6df:8"]]
+ 0056b0c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b0c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b0c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056b0c8 bytes 08491991
+ 0056b0c8 bytes 087d1b91
- 0056b0cc ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0056b0cc bytes 29eaffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bc2c638377e2369cff7493efbe19d8f"></a>

### [`0056b2b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b2b8.md) → [`0056b2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b2b8.md) FUN_0056b2b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566968.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.11% / 新版 89.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b31c",
      "incomplete_value": true,
      "site": "0056b31c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5d4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b31c",
      "incomplete_value": true,
      "site": "0056b31c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:547:8"
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
      "definition_site": "0056b334",
      "incomplete_value": true,
      "site": "0056b344",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:62a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b334",
      "incomplete_value": true,
      "site": "0056b344",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:631:8"
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
      "definition_site": "0056b334",
      "incomplete_value": true,
      "site": "0056b344",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056b334",
      "incomplete_value": true,
      "site": "0056b344",
      "value": [
        "LOAD",
        "16",
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
      "0056b308",
      "READ",
      [
        "storage",
        "0029d547",
        null,
        "string"
      ]
    ],
    [
      "0056b334",
      "READ",
      [
        "storage",
        "002a4631",
        null,
        "string"
      ]
    ],
    [
      "0056b334",
      "READ",
      [
        "storage",
        "002a4641",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056b308",
      "READ",
      [
        "storage",
        "0029d5d4",
        null,
        "string"
      ]
    ],
    [
      "0056b334",
      "READ",
      [
        "storage",
        "002a462a",
        null,
        "string"
      ]
    ],
    [
      "0056b334",
      "READ",
      [
        "storage",
        "002a463a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b2b8.md#insn-0056b300) · [`0056b32c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b2b8.md#insn-0056b32c) · [`0056b330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b2b8.md#insn-0056b330)
- 新版 [`0056b300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b2b8.md#insn-0056b300) · [`0056b32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b2b8.md#insn-0056b32c)

~~~diff
- 0056b300 ["COPY", "tmp:0:8", ["const:547:8"]]
- 0056b300 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056b300 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056b300 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056b300 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 0056b300 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056b300 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056b300 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056b300 bytes 291d1591
+ 0056b300 bytes 29511791
- 0056b32c ["COPY", "tmp:0:8", ["const:631:8"]]
- 0056b32c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056b32c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056b32c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056b32c ["COPY", "tmp:0:8", ["const:62a:8"]]
+ 0056b32c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b32c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b32c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056b32c bytes 08c51891
+ 0056b32c bytes 08a91891
- 0056b330 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0056b330 bytes 29eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52186a4a64a30521c05ae46b9bbdda99"></a>

### [`0056b4a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b4a0.md) → [`0056b4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b4a0.md) FUN_0056b4a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566968.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.08% / 新版 92.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b518",
      "incomplete_value": true,
      "site": "0056b528",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:59e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b518",
      "incomplete_value": true,
      "site": "0056b528",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:511:8"
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
      "definition_site": "0056b518",
      "incomplete_value": true,
      "site": "0056b528",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056b518",
      "incomplete_value": true,
      "site": "0056b528",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b52c",
      "incomplete_value": true,
      "site": "0056b538",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056b52c",
      "incomplete_value": true,
      "site": "0056b538",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056b518",
      "READ",
      [
        "storage",
        "0029b511",
        null,
        "string"
      ]
    ],
    [
      "0056b518",
      "READ",
      [
        "storage",
        "0029b521",
        null,
        "string"
      ]
    ],
    [
      "0056b52c",
      "READ",
      [
        "storage",
        "0029b531",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056b518",
      "READ",
      [
        "storage",
        "0029b59e",
        null,
        "string"
      ]
    ],
    [
      "0056b518",
      "READ",
      [
        "storage",
        "0029b5ae",
        null,
        "string"
      ]
    ],
    [
      "0056b52c",
      "READ",
      [
        "storage",
        "0029b5be",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b4a0.md#insn-0056b510) · [`0056b514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b4a0.md#insn-0056b514)
- 新版 [`0056b510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b4a0.md#insn-0056b510) · [`0056b514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b4a0.md#insn-0056b514)

~~~diff
- 0056b510 ["COPY", "tmp:0:8", ["const:511:8"]]
- 0056b510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056b510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056b510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056b510 ["COPY", "tmp:0:8", ["const:59e:8"]]
+ 0056b510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056b510 bytes 08451491
+ 0056b510 bytes 08791691
- 0056b514 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0056b514 bytes 29eaffb0
+ 0056b514 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0056b514 bytes 29eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c2080ce1e2ec2ed784c0cf60f6fa2c0"></a>

### [`0056b870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b870.md) → [`0056b870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b870.md) FUN_0056b870

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566968.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056b8e8",
      "incomplete_value": true,
      "site": "0056b8f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:66a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056b8e8",
      "incomplete_value": true,
      "site": "0056b8f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:671:8"
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
      "definition_site": "0056b8e8",
      "incomplete_value": true,
      "site": "0056b8f8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056b8e8",
      "incomplete_value": true,
      "site": "0056b8f8",
      "value": [
        "LOAD",
        "16",
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
      "0056b8e8",
      "READ",
      [
        "storage",
        "002a4671",
        null,
        "string"
      ]
    ],
    [
      "0056b8e8",
      "READ",
      [
        "storage",
        "002a4681",
        null,
        "string"
      ]
    ],
    [
      "0056b8fc",
      "READ",
      [
        "storage",
        "002a4691",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056b8e8",
      "READ",
      [
        "storage",
        "002a466a",
        null,
        "string"
      ]
    ],
    [
      "0056b8e8",
      "READ",
      [
        "storage",
        "002a467a",
        null,
        "string"
      ]
    ],
    [
      "0056b8fc",
      "READ",
      [
        "storage",
        "002a468a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b870.md#insn-0056b8e0) · [`0056b8e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056b870.md#insn-0056b8e4)
- 新版 [`0056b8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b870.md#insn-0056b8e0) · [`0056b8e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056b870.md#insn-0056b8e4)

~~~diff
- 0056b8e0 ["COPY", "tmp:0:8", ["const:671:8"]]
- 0056b8e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056b8e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056b8e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056b8e0 ["COPY", "tmp:0:8", ["const:66a:8"]]
+ 0056b8e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b8e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056b8e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056b8e0 bytes 08c51991
+ 0056b8e0 bytes 08a91991
- 0056b8e4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0056b8e4 bytes 29eaffb0
+ 0056b8e4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0056b8e4 bytes 29eaffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cefda37235b8969579580e52f000c466"></a>

### [`0056ba54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056ba54.md) → [`0056ba54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056ba54.md) FUN_0056ba54

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566968.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056bacc",
      "incomplete_value": true,
      "site": "0056badc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056bacc",
      "incomplete_value": true,
      "site": "0056badc",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056bacc",
      "incomplete_value": true,
      "site": "0056badc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056bacc",
      "incomplete_value": true,
      "site": "0056badc",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056bae0",
      "incomplete_value": true,
      "site": "0056bae8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0056bae0",
      "incomplete_value": true,
      "site": "0056bae8",
      "value": [
        "LOAD",
        "16",
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
      "0056bacc",
      "READ",
      [
        "storage",
        "00294a61",
        null,
        "string"
      ]
    ],
    [
      "0056bacc",
      "READ",
      [
        "storage",
        "00294a71",
        null,
        "string"
      ]
    ],
    [
      "0056bae0",
      "READ",
      [
        "storage",
        "00294a81",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056bacc",
      "READ",
      [
        "storage",
        "00294aee",
        null,
        "string"
      ]
    ],
    [
      "0056bacc",
      "READ",
      [
        "storage",
        "00294afe",
        null,
        "string"
      ]
    ],
    [
      "0056bae0",
      "READ",
      [
        "storage",
        "00294b0e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056bac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056ba54.md#insn-0056bac4) · [`0056bac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056ba54.md#insn-0056bac8)
- 新版 [`0056bac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056ba54.md#insn-0056bac4) · [`0056bac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056ba54.md#insn-0056bac8)

~~~diff
- 0056bac4 ["COPY", "tmp:0:8", ["const:a41:8"]]
- 0056bac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056bac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056bac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056bac4 ["COPY", "tmp:0:8", ["const:ace:8"]]
+ 0056bac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056bac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056bac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056bac4 bytes 08052991
+ 0056bac4 bytes 08392b91
- 0056bac8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0056bac8 bytes 29eaffd0
+ 0056bac8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0056bac8 bytes 29eaffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd6d4816d5cd2f9928ac115c63de7f7b"></a>

### [`0056bde8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056bde8.md) → [`0056bde8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056bde8.md) FUN_0056bde8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00574fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574fe4.md) · 呼出先 2件 [`0056a298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056a/0056a298.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) · 呼出先 2件 [`0056a298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056a/0056a298.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0056be10",
      "incomplete_value": false,
      "site": "0056be1c",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056be10",
      "incomplete_value": false,
      "site": "0056be1c",
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
            "const:f00:8"
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
      "0056be1c",
      "DATA",
      [
        "storage",
        "00beff00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056be1c",
      "DATA",
      [
        "storage",
        "00beffb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056be10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056b/0056bde8.md#insn-0056be10)
- 新版 [`0056be10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056b/0056bde8.md#insn-0056be10)

~~~diff
- 0056be10 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 0056be10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056be10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056be10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056be10 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 0056be10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056be10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056be10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056be10 bytes 08013c91
+ 0056be10 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3d1c0805ac744afb10e8b8b9d0605d9"></a>

### [`0056c760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c760.md) → [`0056c760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c760.md) FUN_0056c760

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
      "definition_site": "0056c764",
      "incomplete_value": false,
      "site": "0056c768",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c764",
      "incomplete_value": false,
      "site": "0056c768",
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
      "0056c768",
      "DATA",
      [
        "storage",
        "00beff00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056c768",
      "DATA",
      [
        "storage",
        "00beffb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c760.md#insn-0056c764)
- 新版 [`0056c764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c760.md#insn-0056c764)

~~~diff
- 0056c764 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 0056c764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056c764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056c764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056c764 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 0056c764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056c764 bytes 08013c91
+ 0056c764 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-817db8f7c027de58430e7ecfa2e88ea9"></a>

### [`0056c770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c770.md) → [`0056c770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c770.md) FUN_0056c770

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
      "definition_site": "0056c780",
      "incomplete_value": false,
      "site": "0056c788",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c780",
      "incomplete_value": false,
      "site": "0056c788",
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
      "0056c788",
      "DATA",
      [
        "storage",
        "00beff00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056c788",
      "DATA",
      [
        "storage",
        "00beffb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c770.md#insn-0056c780)
- 新版 [`0056c780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c770.md#insn-0056c780)

~~~diff
- 0056c780 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 0056c780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056c780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056c780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056c780 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 0056c780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056c780 bytes 08013c91
+ 0056c780 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54a2a0e67526695fd7013fe9d46fd482"></a>

### [`0056c7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c7a0.md) → [`0056c7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c7a0.md) FUN_0056c7a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`005679e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00567/005679e4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005679e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00567/005679e4.md)

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
      "definition_site": "0056c7b0",
      "incomplete_value": false,
      "site": "0056c7b8",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c7b0",
      "incomplete_value": false,
      "site": "0056c7b8",
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
            "const:e78:8"
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
      "0056c7b8",
      "DATA",
      [
        "storage",
        "00befe78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056c7b8",
      "DATA",
      [
        "storage",
        "00beff28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c7a0.md#insn-0056c7b0)
- 新版 [`0056c7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c7a0.md#insn-0056c7b0)

~~~diff
- 0056c7b0 ["COPY", "tmp:0:8", ["const:e78:8"]]
- 0056c7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056c7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056c7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056c7b0 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 0056c7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056c7b0 bytes 08e13991
+ 0056c7b0 bytes 08a13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a13d4a663f3c1aaddae0f06d8f80c51"></a>

### [`0056c7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c7d8.md) → [`0056c7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c7d8.md) _INIT_34

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00557a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00557/00557a80.md) [`00569da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00569/00569da8.md) [`00b7d194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d194.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00557a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00557/00557a80.md) [`00569da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00569/00569da8.md) [`00b7d25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d25c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056c804",
      "incomplete_value": false,
      "site": "0056c804",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:498:8"
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
      "definition_site": "0056c804",
      "incomplete_value": false,
      "site": "0056c804",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:3d8:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056c808",
      "incomplete_value": false,
      "site": "0056c808",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:498:8"
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
      "definition_site": "0056c808",
      "incomplete_value": false,
      "site": "0056c808",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:3d8:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056c80c",
      "incomplete_value": false,
      "site": "0056c80c",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c80c",
      "incomplete_value": false,
      "site": "0056c80c",
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
            "const:3d8:8"
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
      "0056c7e8",
      "PARAM",
      [
        "storage",
        "00c263d8",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c800",
      "PARAM",
      [
        "storage",
        "00be5ed0",
        null,
        "pointer"
      ]
    ],
    [
      "0056c804",
      "WRITE",
      [
        "storage",
        "00c263e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056c7e8",
      "PARAM",
      [
        "storage",
        "00c26498",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c800",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ],
    [
      "0056c804",
      "WRITE",
      [
        "storage",
        "00c264a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c7e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c7d8.md#insn-0056c7e8) · [`0056c7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c7d8.md#insn-0056c7f0) · [`0056c81c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c7d8.md#insn-0056c81c)
- 新版 [`0056c7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c7d8.md#insn-0056c7e8) · [`0056c7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c7d8.md#insn-0056c7f0) · [`0056c81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c7d8.md#insn-0056c81c)

~~~diff
- 0056c7e8 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 0056c7e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056c7e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056c7e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056c7e8 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0056c7e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056c7e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056c7e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056c7e8 bytes 21600f91
+ 0056c7e8 bytes 21601291
- 0056c7f0 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 0056c7f0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0056c7f0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0056c7f0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0056c7f0 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 0056c7f0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0056c7f0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0056c7f0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0056c7f0 bytes 73423b91
+ 0056c7f0 bytes 73023e91
- 0056c81c ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 0056c81c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056c81c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056c81c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056c81c ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 0056c81c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056c81c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056c81c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056c81c bytes 21c00f91
+ 0056c81c bytes 21c01291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17dd4421f4b9d901280efe685bfbf9aa"></a>

### [`0056c8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c8b0.md) → [`0056c8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c8b0.md) FUN_0056c8b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0056cb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cb70.md) · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`0056cb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cb70.md) · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056c908",
      "incomplete_value": false,
      "site": "0056c908",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:574:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c908",
      "incomplete_value": false,
      "site": "0056c908",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:4b4:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:c:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056c910",
      "incomplete_value": false,
      "site": "0056c910",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:574:8"
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
      "definition_site": "0056c910",
      "incomplete_value": false,
      "site": "0056c910",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:4b4:8"
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0056c9c0",
      "incomplete_value": true,
      "site": "0056c9c0",
      "value": [
        "LOAD",
        "8",
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056c9c0",
      "incomplete_value": true,
      "site": "0056c9c0",
      "value": [
        "LOAD",
        "8",
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056c8fc",
      "READ",
      [
        "storage",
        "00c26550",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c908",
      "WRITE",
      [
        "storage",
        "00c264c0",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c910",
      "WRITE",
      [
        "storage",
        "00c264b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056c8fc",
      "READ",
      [
        "storage",
        "00c26610",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c908",
      "WRITE",
      [
        "storage",
        "00c26580",
        null,
        "undefined8"
      ]
    ],
    [
      "0056c910",
      "WRITE",
      [
        "storage",
        "00c26578",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056c8f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c8b0.md#insn-0056c8f4) · [`0056c8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c8b0.md#insn-0056c8fc) · [`0056c994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c8b0.md#insn-0056c994)
- 新版 [`0056c8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c8b0.md#insn-0056c8f4) · [`0056c8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c8b0.md#insn-0056c8fc) · [`0056c994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c8b0.md#insn-0056c994)

~~~diff
- 0056c8f4 ["COPY", "tmp:0:8", ["const:4b4:8"]]
- 0056c8f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056c8f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056c8f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056c8f4 ["COPY", "tmp:0:8", ["const:574:8"]]
+ 0056c8f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c8f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056c8f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056c8f4 bytes 08d11291
+ 0056c8f4 bytes 08d11591
- 0056c8fc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:550:8"]]
- 0056c8fc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056c8fc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:610:8"]]
+ 0056c8fc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0056c8fc bytes a0aa42f9
+ 0056c8fc bytes a00a43f9
- 0056c994 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:550:8"]]
- 0056c994 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056c994 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:610:8"]]
+ 0056c994 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0056c994 bytes a0aa42f9
+ 0056c994 bytes a00a43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e474e8fe3daab12b8eccaf98e4c998c2"></a>

### [`0056ca28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056ca28.md) → [`0056ca28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056ca28.md) FUN_0056ca28

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0056cb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cb70.md) · 呼出先 3件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0056cb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cb70.md) · 呼出先 3件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 78.05% / 新版 78.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056cb04",
      "incomplete_value": false,
      "site": "0056cb04",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:618:8"
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
      "definition_site": "0056cb04",
      "incomplete_value": false,
      "site": "0056cb04",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:558:8"
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
      "definition_site": "0056cb0c",
      "incomplete_value": false,
      "site": "0056cb0c",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:618:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056cb0c",
      "incomplete_value": false,
      "site": "0056cb0c",
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
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:558:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "0056cb0c",
      "incomplete_value": false,
      "site": "0056cb0c",
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
                "const:18:8"
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
      "definition_site": "0056cb0c",
      "incomplete_value": false,
      "site": "0056cb0c",
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
                "const:18:8"
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
      "0056ca48",
      "READ",
      [
        "storage",
        "00c26470",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ca70",
      "READ",
      [
        "storage",
        "00c26478",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ca74",
      "WRITE",
      [
        "storage",
        "00c26470",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056ca48",
      "READ",
      [
        "storage",
        "00c26530",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ca70",
      "READ",
      [
        "storage",
        "00c26538",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ca74",
      "WRITE",
      [
        "storage",
        "00c26530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ca48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056ca28.md#insn-0056ca48) · [`0056ca6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056ca28.md#insn-0056ca6c) · [`0056ca84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056ca28.md#insn-0056ca84)
- 新版 [`0056ca48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056ca28.md#insn-0056ca48) · [`0056ca6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056ca28.md#insn-0056ca6c) · [`0056ca84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056ca28.md#insn-0056ca84)

~~~diff
- 0056ca48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
- 0056ca48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056ca48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
+ 0056ca48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0056ca48 bytes 083942f9
+ 0056ca48 bytes 089942f9
- 0056ca6c ["COPY", "tmp:0:8", ["const:470:8"]]
- 0056ca6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056ca6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056ca6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056ca6c ["COPY", "tmp:0:8", ["const:530:8"]]
+ 0056ca6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056ca6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056ca6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056ca6c bytes 08c11191
+ 0056ca6c bytes 08c11491
- 0056ca84 ["COPY", "tmp:0:8", ["const:470:8"]]
- 0056ca84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056ca84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056ca84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056ca84 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 0056ca84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056ca84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056ca84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056ca84 bytes 08c11191
+ 0056ca84 bytes 08c11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3646776f38a55672a91f8055ce77604b"></a>

### [`0056cb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cb70.md) → [`0056cb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cb70.md) FUN_0056cb70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004184bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004184bc.md) [`0041876c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041876c.md) [`00444e6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444e6c.md) · 呼出先 5件 [`0056c8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c8b0.md) [`0056ca28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056ca28.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 3件 [`004184bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004184bc.md) [`0041876c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041876c.md) [`00444e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444e6c.md) · 呼出先 5件 [`0056c8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c8b0.md) [`0056ca28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056ca28.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 81.16% / 新版 81.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 2件

アドレスに依存する影響 `store_destination` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056cbb0",
      "incomplete_value": false,
      "site": "0056cbb0",
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
            "const:55c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056cbb0",
      "incomplete_value": false,
      "site": "0056cbb0",
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
            "const:49c:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056cbb8",
      "incomplete_value": false,
      "site": "0056cbb8",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056cbb8",
      "incomplete_value": false,
      "site": "0056cbb8",
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
            "const:4a0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056cbc0",
      "incomplete_value": false,
      "site": "0056cbc0",
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
            "const:564:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056cbc0",
      "incomplete_value": false,
      "site": "0056cbc0",
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
            "const:4a4:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056cbb0",
      "WRITE",
      [
        "storage",
        "00c2649c",
        null,
        "undefined4"
      ]
    ],
    [
      "0056cbb8",
      "WRITE",
      [
        "storage",
        "00c264a0",
        null,
        "undefined4"
      ]
    ],
    [
      "0056cbc0",
      "WRITE",
      [
        "storage",
        "00c264a4",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0056cbb0",
      "WRITE",
      [
        "storage",
        "00c2655c",
        null,
        "undefined4"
      ]
    ],
    [
      "0056cbb8",
      "WRITE",
      [
        "storage",
        "00c26560",
        null,
        "undefined4"
      ]
    ],
    [
      "0056cbc0",
      "WRITE",
      [
        "storage",
        "00c26564",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056cbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cb70.md#insn-0056cbb0) · [`0056cbb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cb70.md#insn-0056cbb8) · [`0056cbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cb70.md#insn-0056cbc0)
- 新版 [`0056cbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cb70.md#insn-0056cbb0) · [`0056cbb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cb70.md#insn-0056cbb8) · [`0056cbc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cb70.md#insn-0056cbc0)

~~~diff
- 0056cbb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:49c:8"]]
- 0056cbb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
+ 0056cbb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:55c:8"]]
+ 0056cbb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
- 0056cbb0 bytes 049d04b9
+ 0056cbb0 bytes 045d05b9
- 0056cbb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4a0:8"]]
- 0056cbb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:4"]]
+ 0056cbb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:560:8"]]
+ 0056cbb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:4"]]
- 0056cbb8 bytes 05a104b9
+ 0056cbb8 bytes 056105b9
- 0056cbc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4a4:8"]]
- 0056cbc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 0056cbc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:564:8"]]
+ 0056cbc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 0056cbc0 bytes 00a504b9
+ 0056cbc0 bytes 006505b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3708b5924b521af456decdf8f61e6b1"></a>

### [`0056cca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cca8.md) → [`0056cca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cca8.md) FUN_0056cca8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`005f483c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005f4/005f483c.md) [`00878704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00878/00878704.md) [`00879778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00879/00879778.md) [`008a5430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5430.md) · 呼出先 0件 
- 新版 呼出元 4件 [`005f483c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f4/005f483c.md) [`00878704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878704.md) [`00879778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00879/00879778.md) [`008a5430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5430.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056ccc4",
      "incomplete_value": false,
      "site": "0056ccc4",
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
            "const:564:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ccc4",
      "incomplete_value": false,
      "site": "0056ccc4",
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
            "const:4a4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056cccc",
      "incomplete_value": false,
      "site": "0056cccc",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056cccc",
      "incomplete_value": false,
      "site": "0056cccc",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056ccd8",
      "incomplete_value": false,
      "site": "0056ccd8",
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
            "const:56c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ccd8",
      "incomplete_value": false,
      "site": "0056ccd8",
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
            "const:4ac:8"
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
      "0056ccb8",
      "READ",
      [
        "storage",
        "00c26550",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ccc4",
      "WRITE",
      [
        "storage",
        "00c264a4",
        null,
        "undefined4"
      ]
    ],
    [
      "0056cccc",
      "WRITE",
      [
        "storage",
        "00c264a8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0056ccb8",
      "READ",
      [
        "storage",
        "00c26610",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ccc4",
      "WRITE",
      [
        "storage",
        "00c26564",
        null,
        "undefined4"
      ]
    ],
    [
      "0056cccc",
      "WRITE",
      [
        "storage",
        "00c26568",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ccc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cca8.md#insn-0056ccc4) · [`0056cccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cca8.md#insn-0056cccc) · [`0056ccd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cca8.md#insn-0056ccd8)
- 新版 [`0056ccc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cca8.md#insn-0056ccc4) · [`0056cccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cca8.md#insn-0056cccc) · [`0056ccd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cca8.md#insn-0056ccd8)

~~~diff
- 0056ccc4 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:4a4:8"]]
- 0056ccc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 0056ccc4 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:564:8"]]
+ 0056ccc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 0056ccc4 bytes 88a504b9
+ 0056ccc4 bytes 886505b9
- 0056cccc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4a8:8"]]
- 0056cccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 0056cccc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
+ 0056cccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0056cccc bytes 09a904b9
+ 0056cccc bytes 096905b9
- 0056ccd8 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:4ac:8"]]
- 0056ccd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
+ 0056ccd8 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:56c:8"]]
+ 0056ccd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 0056ccd8 bytes 4bad04b9
+ 0056ccd8 bytes 4b6d05b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3183964e98d1654e34dcd6d2a131adc"></a>

### [`0056cdfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cdfc.md) → [`0056cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cdfc.md) FUN_0056cdfc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0053a710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a710.md) [`0053a8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a8e8.md) [`0053aac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053aac4.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 3件 [`0053a710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a710.md) [`0053a8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a8e8.md) [`0053aac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053aac4.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_value, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 44.00% / 新版 44.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0056ce80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0056ce84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0056ce88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0056ce00",
      "READ",
      [
        "storage",
        "00c26540",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ce14",
      "READ",
      [
        "storage",
        "00c26538",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:0056ce34",
      "READ",
      [
        "storage",
        "00c26520",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056ce00",
      "READ",
      [
        "storage",
        "00c26600",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ce14",
      "READ",
      [
        "storage",
        "00c265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0056ce34",
      "READ",
      [
        "storage",
        "00c265e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ce68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cdfc.md#insn-0056ce68) · [`0056ce80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cdfc.md#insn-0056ce80)
- 新版 [`0056ce68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cdfc.md#insn-0056ce68)

~~~diff
- 0056ce68 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0056ce68 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 0056ce68 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0056ce68 ["COPY", "tmp:1:8", ["register:4080:8"]]
- 0056ce68 bytes eb03909a
+ 0056ce68 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0056ce68 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 0056ce68 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 0056ce68 ["COPY", "tmp:1:8", ["register:4080:8"]]
+ 0056ce68 bytes eb03909a
- 0056ce80 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:20:8"]]
- 0056ce80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4060:8"]]
- 0056ce80 bytes 4c1100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-251edb2b2ef9462bcc183be57d7de261"></a>

### [`0056cec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cec4.md) → [`0056cec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cec4.md) FUN_0056cec4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0053a710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a710.md) [`0053a8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a8e8.md) [`0053aac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053aac4.md) · 呼出先 1件 [`0056d4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056d/0056d4e0.md)
- 新版 呼出元 3件 [`0053a710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a710.md) [`0053a8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a8e8.md) [`0053aac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053aac4.md) · 呼出先 1件 [`0056d4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056d/0056d4e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056cf5c",
      "incomplete_value": true,
      "site": "0056cf64",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0056cf5c",
      "incomplete_value": true,
      "site": "0056cf64",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056cf60",
      "incomplete_value": true,
      "site": "0056cf68",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056cf60",
      "incomplete_value": true,
      "site": "0056cf68",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c26000:8"
              ],
              [
                "leaf",
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056cf78",
      "incomplete_value": false,
      "site": "0056cf78",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056cf78",
      "incomplete_value": false,
      "site": "0056cf78",
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
            "const:540:8"
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
      "0056cedc",
      "READ",
      [
        "storage",
        "00c26520",
        null,
        "undefined8"
      ]
    ],
    [
      "0056cefc",
      "READ",
      [
        "storage",
        "00c26538",
        null,
        "undefined8"
      ]
    ],
    [
      "0056cefc",
      "READ",
      [
        "storage",
        "00c26540",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0056cedc",
      "READ",
      [
        "storage",
        "00c265e0",
        null,
        "undefined8"
      ]
    ],
    [
      "0056cefc",
      "READ",
      [
        "storage",
        "00c265f8",
        null,
        "undefined8"
      ]
    ],
    [
      "0056cefc",
      "READ",
      [
        "storage",
        "00c26600",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056cf78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cec4.md#insn-0056cf78) · [`0056ced4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cec4.md#insn-0056ced4) · [`0056cf14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cec4.md#insn-0056cf14)
- 新版 [`0056cf78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cec4.md#insn-0056cf78) · [`0056ced4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cec4.md#insn-0056ced4) · [`0056cf14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cec4.md#insn-0056cf14)

~~~diff
- 0056cf78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:540:8"]]
- 0056cf78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 0056cf78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:600:8"]]
+ 0056cf78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0056cf78 bytes 09a102f9
+ 0056cf78 bytes 090103f9
- 0056ced4 ["COPY", "tmp:0:8", ["const:520:8"]]
- 0056ced4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056ced4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056ced4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056ced4 ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 0056ced4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056ced4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056ced4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056ced4 bytes 29811491
+ 0056ced4 bytes 29811791
- 0056cf14 ["COPY", "tmp:0:8", ["const:518:8"]]
- 0056cf14 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0056cf14 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0056cf14 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0056cf14 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 0056cf14 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0056cf14 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0056cf14 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0056cf14 bytes 73621491
+ 0056cf14 bytes 73621791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-940d147a9f040ed755f428fc936cf4c5"></a>

### [`0056cf88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cf88.md) → [`0056cf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cf88.md) FUN_0056cf88

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0053a8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053a/0053a8e8.md) · 呼出先 1件 [`00bdb440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb440.md)
- 新版 呼出元 1件 [`0053a8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a8e8.md) · 呼出先 1件 [`00bdb4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4f0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056cff0",
      "incomplete_value": false,
      "site": "0056cff0",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056cff0",
      "incomplete_value": false,
      "site": "0056cff0",
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
            "const:548:8"
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
      "0056cfa8",
      "READ",
      [
        "storage",
        "00c26500",
        null,
        "undefined4"
      ]
    ],
    [
      "0056cfbc",
      "READ",
      [
        "storage",
        "00c26508",
        null,
        "undefined4"
      ]
    ],
    [
      "0056cfbc",
      "READ",
      [
        "storage",
        "00c2650c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0056cfa8",
      "READ",
      [
        "storage",
        "00c265c0",
        null,
        "undefined4"
      ]
    ],
    [
      "0056cfbc",
      "READ",
      [
        "storage",
        "00c265c8",
        null,
        "undefined4"
      ]
    ],
    [
      "0056cfbc",
      "READ",
      [
        "storage",
        "00c265cc",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056cff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cf88.md#insn-0056cff0) · [`0056cfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cf88.md#insn-0056cfa0)
- 新版 [`0056cff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cf88.md#insn-0056cff0) · [`0056cfa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cf88.md#insn-0056cfa0)

~~~diff
- 0056cff0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0056cff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:548:8"]]
- 0056cff0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0056cff0 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0056cff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:608:8"]]
+ 0056cff0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0056cff0 bytes 09211539
+ 0056cff0 bytes 09211839
- 0056cfa0 ["COPY", "tmp:0:8", ["const:500:8"]]
- 0056cfa0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0056cfa0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0056cfa0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0056cfa0 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 0056cfa0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0056cfa0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0056cfa0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0056cfa0 bytes 73021491
+ 0056cfa0 bytes 73021791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1fe8e53843604b8ae1a0186d029ab9c"></a>

### [`0056dee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056d/0056dee0.md) → [`0056dee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056d/0056dee0.md) FUN_0056dee0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0056f4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f4d8.md) · 呼出先 17件 [`0052dd2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dd2c.md) [`0053239c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/0053239c.md) [`0056e384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e384.md) [`0056f6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f6a0.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 1件 [`0056f4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f4d8.md) · 呼出先 17件 [`0052dd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd2c.md) [`0053239c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053239c.md) [`0056e384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e384.md) [`0056f6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f6a0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.30% / 新版 95.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056df0c",
      "incomplete_value": false,
      "site": "0056df18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056df0c",
      "incomplete_value": false,
      "site": "0056df18",
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
            "const:f50:8"
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
      "definition_site": "0056df8c",
      "incomplete_value": true,
      "site": "0056df8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:555:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056df8c",
      "incomplete_value": true,
      "site": "0056df8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:55c:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056e004",
      "incomplete_value": false,
      "site": "0056e010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e004",
      "incomplete_value": false,
      "site": "0056e010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:100:8"
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
      "0056df18",
      "DATA",
      [
        "storage",
        "00beff50",
        null,
        "undefined *"
      ]
    ],
    [
      "0056df7c",
      "READ",
      [
        "storage",
        "002a355c",
        null,
        "string"
      ]
    ],
    [
      "0056dfdc",
      "READ",
      [
        "storage",
        "00beff88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056df18",
      "DATA",
      [
        "storage",
        "00bf0000",
        null,
        "undefined *"
      ]
    ],
    [
      "0056df7c",
      "READ",
      [
        "storage",
        "002a3555",
        null,
        "string"
      ]
    ],
    [
      "0056dfdc",
      "READ",
      [
        "storage",
        "00bf0038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056df08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056d/0056dee0.md#insn-0056df08) · [`0056df0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056d/0056dee0.md#insn-0056df0c) · [`0056df10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056d/0056dee0.md#insn-0056df10)
- 新版 [`0056df08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056d/0056dee0.md#insn-0056df08) · [`0056df0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056d/0056dee0.md#insn-0056df0c)

~~~diff
- 0056df08 ["COPY", "register:4048:8", ["const:bef000:8"]]
+ 0056df08 ["COPY", "register:4048:8", ["const:bf0000:8"]]
- 0056df08 bytes 093400d0
+ 0056df08 bytes 093400f0
- 0056df0c ["COPY", "tmp:0:8", ["const:f50:8"]]
- 0056df0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056df0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056df0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056df0c ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0056df0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056df0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056df0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056df0c bytes 29413d91
+ 0056df0c bytes 29010091
- 0056df10 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0056df10 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb259fe84fb92f3bf403c49c4f5e53fa"></a>

### [`0056e3e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e3e0.md) → [`0056e3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e3e0.md) FUN_0056e3e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`005323b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005323b0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd410.md) [`00bdd420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd420.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005323b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323b0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd4c0.md) [`00bdd4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd4d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.55% / 新版 91.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056e4ac",
      "incomplete_value": false,
      "site": "0056e4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e4ac",
      "incomplete_value": false,
      "site": "0056e4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "definition_site": "0056e43c",
      "incomplete_value": true,
      "site": "0056e440",
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
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e43c",
      "incomplete_value": true,
      "site": "0056e440",
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
              "LOAD"
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
      "0056e438",
      "READ",
      [
        "storage",
        "00c1b390",
        null,
        "pointer"
      ]
    ],
    [
      "0056e43c",
      "READ",
      [
        "storage",
        "00c23e5c",
        null,
        "undefined4"
      ]
    ],
    [
      "0056e444",
      "READ",
      [
        "storage",
        "00c23e60",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0056e438",
      "READ",
      [
        "storage",
        "00c1b440",
        null,
        "pointer"
      ]
    ],
    [
      "0056e43c",
      "READ",
      [
        "storage",
        "00c23f0c",
        null,
        "undefined4"
      ]
    ],
    [
      "0056e444",
      "READ",
      [
        "storage",
        "00c23f10",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e3e0.md#insn-0056e438) · [`0056e48c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e3e0.md#insn-0056e48c) · [`0056e4a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e3e0.md#insn-0056e4a0)
- 新版 [`0056e438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e3e0.md#insn-0056e438) · [`0056e48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e3e0.md#insn-0056e48c) · [`0056e4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e3e0.md#insn-0056e4a0)

~~~diff
- 0056e438 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:390:8"]]
- 0056e438 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056e438 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:440:8"]]
+ 0056e438 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 0056e438 bytes 18cb41f9
+ 0056e438 bytes 182342f9
- 0056e48c ["COPY", "tmp:0:8", ["const:120:8"]]
- 0056e48c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056e48c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056e48c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056e48c ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 0056e48c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056e48c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056e48c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056e48c bytes 08810491
+ 0056e48c bytes 08410791
- 0056e4a0 ["COPY", "tmp:0:8", ["const:170:8"]]
- 0056e4a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0056e4a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0056e4a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056e4a0 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 0056e4a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056e4a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056e4a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0056e4a0 bytes 29c10591
+ 0056e4a0 bytes 29810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-244a41db2b913784321ceb941a3f027b"></a>

### [`0056e528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e528.md) → [`0056e528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e528.md) FUN_0056e528

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`005323b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005323b0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd410.md) [`00bdd420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd420.md)
- 新版 呼出元 0件  · 呼出先 10件 [`005323b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323b0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd4c0.md) [`00bdd4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd4d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.09% / 新版 86.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056e604",
      "incomplete_value": false,
      "site": "0056e60c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e604",
      "incomplete_value": false,
      "site": "0056e60c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:120:8"
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
      "definition_site": "0056e624",
      "incomplete_value": false,
      "site": "0056e624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e624",
      "incomplete_value": false,
      "site": "0056e624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "definition_site": "0056e690",
      "incomplete_value": false,
      "site": "0056e698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e690",
      "incomplete_value": false,
      "site": "0056e698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "0056e588",
      "READ",
      [
        "storage",
        "00c1b390",
        null,
        "pointer"
      ]
    ],
    [
      "0056e58c",
      "READ",
      [
        "storage",
        "00c23e5c",
        null,
        "undefined4"
      ]
    ],
    [
      "0056e594",
      "READ",
      [
        "storage",
        "00c23e60",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0056e588",
      "READ",
      [
        "storage",
        "00c1b440",
        null,
        "pointer"
      ]
    ],
    [
      "0056e58c",
      "READ",
      [
        "storage",
        "00c23f0c",
        null,
        "undefined4"
      ]
    ],
    [
      "0056e594",
      "READ",
      [
        "storage",
        "00c23f10",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e528.md#insn-0056e588) · [`0056e604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e528.md#insn-0056e604) · [`0056e608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e528.md#insn-0056e608)
- 新版 [`0056e588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e528.md#insn-0056e588) · [`0056e604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e528.md#insn-0056e604)

~~~diff
- 0056e588 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:390:8"]]
- 0056e588 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056e588 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:440:8"]]
+ 0056e588 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 0056e588 bytes f7ca41f9
+ 0056e588 bytes f72242f9
- 0056e604 ["COPY", "tmp:0:8", ["const:120:8"]]
- 0056e604 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056e604 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056e604 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056e604 ["COPY", "tmp:0:8", ["const:1d0:8"]]
+ 0056e604 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056e604 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056e604 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056e604 bytes 08810491
+ 0056e604 bytes 08410791
- 0056e608 ["COPY", "register:40b0:8", ["register:4000:8"]]
- 0056e608 bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf8bf0b2275c9922d4c4a3b3041df0b1"></a>

### [`0056e724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e724.md) → [`0056e724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e724.md) FUN_0056e724

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`005323b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/005323b0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd4b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005323b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323b0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd560.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056e768",
      "incomplete_value": false,
      "site": "0056e770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e768",
      "incomplete_value": false,
      "site": "0056e770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:290:8"
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
      "definition_site": "0056e788",
      "incomplete_value": false,
      "site": "0056e788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e788",
      "incomplete_value": false,
      "site": "0056e788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
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
      "0056e770",
      "DATA",
      [
        "storage",
        "00bf0290",
        null,
        "undefined *"
      ]
    ],
    [
      "0056e788",
      "DATA",
      [
        "storage",
        "00bf02e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056e770",
      "DATA",
      [
        "storage",
        "00bf0340",
        null,
        "undefined *"
      ]
    ],
    [
      "0056e788",
      "DATA",
      [
        "storage",
        "00bf0390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e724.md#insn-0056e768) · [`0056e76c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e724.md#insn-0056e76c)
- 新版 [`0056e768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e724.md#insn-0056e768) · [`0056e76c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e724.md#insn-0056e76c)

~~~diff
- 0056e768 ["COPY", "tmp:0:8", ["const:290:8"]]
- 0056e768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0056e768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0056e768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0056e768 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 0056e768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0056e768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0056e768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0056e768 bytes 08410a91
+ 0056e768 bytes 08010d91
- 0056e76c ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0056e76c bytes f40300aa
+ 0056e76c ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 0056e76c bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba4e4b470a8ecf15834e86197e834a6a"></a>

### [`0056e8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e8b0.md) → [`0056e8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e8b0.md) FUN_0056e8b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0056f6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f6a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0056f6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f6a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056e8c8",
      "incomplete_value": false,
      "site": "0056e8d4",
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
            "const:b41:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e8c8",
      "incomplete_value": false,
      "site": "0056e8d4",
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
            "const:bd5:8"
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
      "0056e8c8",
      "PARAM",
      [
        "storage",
        "002adbd5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056e8c8",
      "PARAM",
      [
        "storage",
        "002adb41",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e8c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e8b0.md#insn-0056e8c8)
- 新版 [`0056e8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e8b0.md#insn-0056e8c8)

~~~diff
- 0056e8c8 ["COPY", "tmp:0:8", ["const:bd5:8"]]
- 0056e8c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056e8c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056e8c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056e8c8 ["COPY", "tmp:0:8", ["const:b41:8"]]
+ 0056e8c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056e8c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056e8c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056e8c8 bytes 21542f91
+ 0056e8c8 bytes 21042d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc1b9c4abd537c2e84d0485379072289"></a>

### [`0056e968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e968.md) → [`0056e968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e968.md) FUN_0056e968

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0056f6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f6a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0056f6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f6a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056e980",
      "incomplete_value": false,
      "site": "0056e98c",
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
            "const:a9e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e980",
      "incomplete_value": false,
      "site": "0056e98c",
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
            "const:a11:8"
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
      "0056e980",
      "PARAM",
      [
        "storage",
        "00293a11",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056e980",
      "PARAM",
      [
        "storage",
        "00293a9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e968.md#insn-0056e980)
- 新版 [`0056e980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e968.md#insn-0056e980)

~~~diff
- 0056e980 ["COPY", "tmp:0:8", ["const:a11:8"]]
- 0056e980 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056e980 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056e980 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056e980 ["COPY", "tmp:0:8", ["const:a9e:8"]]
+ 0056e980 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056e980 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056e980 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056e980 bytes 21442891
+ 0056e980 bytes 21782a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bb69dde2d50540a7df2bf62f6820f58"></a>

### [`0056e9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e9b0.md) → [`0056e9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e9b0.md) FUN_0056e9b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`0056f6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f6a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0056f6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f6a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056e9c8",
      "incomplete_value": false,
      "site": "0056e9d8",
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
            "const:5df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056e9c8",
      "incomplete_value": false,
      "site": "0056e9d8",
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
            "const:552:8"
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
      "0056e9c8",
      "PARAM",
      [
        "storage",
        "0029d552",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0056e9c8",
      "PARAM",
      [
        "storage",
        "0029d5df",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056e9c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e9b0.md#insn-0056e9c8)
- 新版 [`0056e9c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e9b0.md#insn-0056e9c8)

~~~diff
- 0056e9c8 ["COPY", "tmp:0:8", ["const:552:8"]]
- 0056e9c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056e9c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056e9c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056e9c8 ["COPY", "tmp:0:8", ["const:5df:8"]]
+ 0056e9c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056e9c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056e9c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056e9c8 bytes 21481591
+ 0056e9c8 bytes 217c1791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f058c9c928ead26c8f42fde75a804159"></a>

### [`0056eae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056eae0.md) → [`0056eae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056eae0.md) FUN_0056eae0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md) [`00bdd520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd520.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md) [`00bdd5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd5d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056eb08",
      "incomplete_value": false,
      "site": "0056eb18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056eb08",
      "incomplete_value": false,
      "site": "0056eb18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:100:8"
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
      "definition_site": "0056eb0c",
      "incomplete_value": true,
      "site": "0056eb18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056eb0c",
      "incomplete_value": true,
      "site": "0056eb18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f0:8"
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
      "0056eb08",
      "PARAM",
      [
        "storage",
        "00bf0100",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0056eb0c",
      "READ",
      [
        "storage",
        "00c1b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "0056eb0c",
      "PARAM",
      [
        "storage",
        "00bf0420",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0056eb08",
      "PARAM",
      [
        "storage",
        "00bf01b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0056eb0c",
      "READ",
      [
        "storage",
        "00c1b4a0",
        null,
        "pointer"
      ]
    ],
    [
      "0056eb0c",
      "PARAM",
      [
        "storage",
        "00bf04d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056eb08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056eae0.md#insn-0056eb08) · [`0056eb0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056eae0.md#insn-0056eb0c)
- 新版 [`0056eb08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056eae0.md#insn-0056eb08) · [`0056eb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056eae0.md#insn-0056eb0c)

~~~diff
- 0056eb08 ["COPY", "tmp:0:8", ["const:100:8"]]
- 0056eb08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056eb08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056eb08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056eb08 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 0056eb08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056eb08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056eb08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056eb08 bytes 21000491
+ 0056eb08 bytes 21c00691
- 0056eb0c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:3f0:8"]]
- 0056eb0c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056eb0c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:4a0:8"]]
+ 0056eb0c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 0056eb0c bytes 42f841f9
+ 0056eb0c bytes 425042f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-609c9a60f85a0d7b2699afda0b1712e4"></a>

### [`0056eda4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056eda4.md) → [`0056eda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056eda4.md) FUN_0056eda4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0056ccec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056ccec.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md) [`00bdd420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd420.md) [`00bdd450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd450.md) [`00bdd580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd580.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0056ccec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056ccec.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md) [`00bdd4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd4d0.md) [`00bdd500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd500.md) [`00bdd630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd630.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056ede4",
      "incomplete_value": true,
      "site": "0056edf0",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ede4",
      "incomplete_value": true,
      "site": "0056edf0",
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
            "const:70:8"
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
      "definition_site": "0056ee08",
      "incomplete_value": false,
      "site": "0056ee18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ee08",
      "incomplete_value": false,
      "site": "0056ee18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "definition_site": "0056ee10",
      "incomplete_value": false,
      "site": "0056ee18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ee10",
      "incomplete_value": false,
      "site": "0056ee18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "0056eddc",
      "PARAM",
      [
        "storage",
        "00bf0060",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0056ede4",
      "PARAM",
      [
        "storage",
        "00bf0070",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0056ee08",
      "PARAM",
      [
        "storage",
        "00bf0088",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0056eddc",
      "PARAM",
      [
        "storage",
        "00bf0110",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0056ede4",
      "PARAM",
      [
        "storage",
        "00bf0120",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0056ee08",
      "PARAM",
      [
        "storage",
        "00bf0138",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056eddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056eda4.md#insn-0056eddc) · [`0056ede4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056eda4.md#insn-0056ede4) · [`0056ee08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056eda4.md#insn-0056ee08)
- 新版 [`0056eddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056eda4.md#insn-0056eddc) · [`0056ede4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056eda4.md#insn-0056ede4) · [`0056ee08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056eda4.md#insn-0056ee08)

~~~diff
- 0056eddc ["COPY", "tmp:0:8", ["const:60:8"]]
- 0056eddc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056eddc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056eddc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056eddc ["COPY", "tmp:0:8", ["const:110:8"]]
+ 0056eddc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056eddc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056eddc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056eddc bytes 21800191
+ 0056eddc bytes 21400491
- 0056ede4 ["COPY", "tmp:0:8", ["const:70:8"]]
- 0056ede4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0056ede4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0056ede4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0056ede4 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 0056ede4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0056ede4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0056ede4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0056ede4 bytes 42c00191
+ 0056ede4 bytes 42800491
- 0056ee08 ["COPY", "tmp:0:8", ["const:88:8"]]
- 0056ee08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056ee08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056ee08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056ee08 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0056ee08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056ee08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056ee08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056ee08 bytes 21200291
+ 0056ee08 bytes 21e00491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdf0932797d5a1451bb514a9dd24b735"></a>

### [`0056eeec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056eeec.md) → [`0056eeec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056eeec.md) FUN_0056eeec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0056ccec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056ccec.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md) [`00bdd420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd420.md) [`00bdd450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd450.md) [`00bdd580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd580.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0056ccec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056ccec.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md) [`00bdd4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd4d0.md) [`00bdd500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd500.md) [`00bdd630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd630.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056ef5c",
      "incomplete_value": false,
      "site": "0056ef64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ef5c",
      "incomplete_value": false,
      "site": "0056ef64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "definition_site": "0056ef78",
      "incomplete_value": false,
      "site": "0056ef88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ef78",
      "incomplete_value": false,
      "site": "0056ef88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "definition_site": "0056ef80",
      "incomplete_value": false,
      "site": "0056ef88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056ef80",
      "incomplete_value": false,
      "site": "0056ef88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "0056ef2c",
      "PARAM",
      [
        "storage",
        "00bf0060",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0056ef34",
      "PARAM",
      [
        "storage",
        "00bf0070",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0056ef54",
      "PARAM",
      [
        "storage",
        "00bf0088",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0056ef2c",
      "PARAM",
      [
        "storage",
        "00bf0110",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0056ef34",
      "PARAM",
      [
        "storage",
        "00bf0120",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0056ef54",
      "PARAM",
      [
        "storage",
        "00bf0138",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056ef2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056eeec.md#insn-0056ef2c) · [`0056ef34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056eeec.md#insn-0056ef34) · [`0056ef54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056eeec.md#insn-0056ef54)
- 新版 [`0056ef2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056eeec.md#insn-0056ef2c) · [`0056ef34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056eeec.md#insn-0056ef34) · [`0056ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056eeec.md#insn-0056ef54)

~~~diff
- 0056ef2c ["COPY", "tmp:0:8", ["const:60:8"]]
- 0056ef2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056ef2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056ef2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056ef2c ["COPY", "tmp:0:8", ["const:110:8"]]
+ 0056ef2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056ef2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056ef2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056ef2c bytes 21800191
+ 0056ef2c bytes 21400491
- 0056ef34 ["COPY", "tmp:0:8", ["const:70:8"]]
- 0056ef34 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0056ef34 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0056ef34 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0056ef34 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 0056ef34 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0056ef34 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0056ef34 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0056ef34 bytes 42c00191
+ 0056ef34 bytes 42800491
- 0056ef54 ["COPY", "tmp:0:8", ["const:88:8"]]
- 0056ef54 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056ef54 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056ef54 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056ef54 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0056ef54 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056ef54 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056ef54 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056ef54 bytes 21200291
+ 0056ef54 bytes 21e00491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2068f8b7fd3554d32ac6e52bfc56d33f"></a>

### [`0056f1e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f1e8.md) → [`0056f1e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f1e8.md) FUN_0056f1e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056f270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f270.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0056f270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f270.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056f210",
      "incomplete_value": false,
      "site": "0056f22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056f210",
      "incomplete_value": false,
      "site": "0056f22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "definition_site": "0056f218",
      "incomplete_value": false,
      "site": "0056f22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0056f218",
      "incomplete_value": false,
      "site": "0056f22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf0000:8"
          ],
          [
            "leaf",
            "const:c0:8"
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
      "0056f210",
      "PARAM",
      [
        "storage",
        "00bf00b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0056f218",
      "PARAM",
      [
        "storage",
        "00bf00c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0056f210",
      "PARAM",
      [
        "storage",
        "00bf0160",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0056f218",
      "PARAM",
      [
        "storage",
        "00bf0170",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056f210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f1e8.md#insn-0056f210) · [`0056f218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f1e8.md#insn-0056f218)
- 新版 [`0056f210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f1e8.md#insn-0056f210) · [`0056f218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f1e8.md#insn-0056f218)

~~~diff
- 0056f210 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 0056f210 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0056f210 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0056f210 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056f210 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 0056f210 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056f210 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056f210 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0056f210 bytes 21c00291
+ 0056f210 bytes 21800591
- 0056f218 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0056f218 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0056f218 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0056f218 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0056f218 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 0056f218 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0056f218 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0056f218 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0056f218 bytes 42000391
+ 0056f218 bytes 42c00591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

