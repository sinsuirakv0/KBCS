# v15.7.2 → v15.7.3 · 最優先の変更候補 (41)

[一覧の目次](README.md)

<a id="compare-4239bc4dd98ad09388f46adacece9389"></a>

### [`0085159c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/0085159c.md) → [`0085159c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/0085159c.md) FUN_0085159c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008515c4",
      "incomplete_value": false,
      "site": "008515c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008515c4",
      "incomplete_value": false,
      "site": "008515c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "008515c8",
      "DATA",
      [
        "storage",
        "00c028c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008515c8",
      "DATA",
      [
        "storage",
        "00c02970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008515c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/0085159c.md#insn-008515c4)
- 新版 [`008515c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/0085159c.md#insn-008515c4)

~~~diff
- 008515c4 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 008515c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008515c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008515c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008515c4 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 008515c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008515c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008515c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008515c4 bytes 29012391
+ 008515c4 bytes 29c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f70a2798c65cfbaf7b7f86776fd38b0a"></a>

### [`0085164c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/0085164c.md) → [`0085164c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/0085164c.md) FUN_0085164c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00851668",
      "incomplete_value": false,
      "site": "00851674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851668",
      "incomplete_value": false,
      "site": "00851674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "00851674",
      "DATA",
      [
        "storage",
        "00c028c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00851674",
      "DATA",
      [
        "storage",
        "00c02970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/0085164c.md#insn-00851668)
- 新版 [`00851668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/0085164c.md#insn-00851668)

~~~diff
- 00851668 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00851668 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00851668 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00851668 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00851668 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00851668 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00851668 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00851668 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00851668 bytes 29012391
+ 00851668 bytes 29c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b879f950af1adf46ad2f29c719484c9c"></a>

### [`0085182c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/0085182c.md) → [`0085182c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/0085182c.md) FUN_0085182c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00851844",
      "incomplete_value": false,
      "site": "00851850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851844",
      "incomplete_value": false,
      "site": "00851850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "00851850",
      "DATA",
      [
        "storage",
        "00c02950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00851850",
      "DATA",
      [
        "storage",
        "00c02a00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/0085182c.md#insn-00851844)
- 新版 [`00851844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/0085182c.md#insn-00851844)

~~~diff
- 00851844 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00851844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00851844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00851844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00851844 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00851844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00851844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00851844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00851844 bytes 08412591
+ 00851844 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ec059b7f4432c94851d4407d5678f75"></a>

### [`008518bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/008518bc.md) → [`008518bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008518bc.md) FUN_008518bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008518d4",
      "incomplete_value": false,
      "site": "008518e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008518d4",
      "incomplete_value": false,
      "site": "008518e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "008518e0",
      "DATA",
      [
        "storage",
        "00c02950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008518e0",
      "DATA",
      [
        "storage",
        "00c02a00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008518d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/008518bc.md#insn-008518d4)
- 新版 [`008518d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008518bc.md#insn-008518d4)

~~~diff
- 008518d4 ["COPY", "tmp:0:8", ["const:950:8"]]
- 008518d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008518d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008518d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008518d4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 008518d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008518d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008518d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008518d4 bytes 08412591
+ 008518d4 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce159a02e2e3915d7aa97e2d16aff902"></a>

### [`00851948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/00851948.md) → [`00851948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851948.md) FUN_00851948

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00851970",
      "incomplete_value": false,
      "site": "00851974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851970",
      "incomplete_value": false,
      "site": "00851974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "00851974",
      "DATA",
      [
        "storage",
        "00c02950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00851974",
      "DATA",
      [
        "storage",
        "00c02a00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/00851948.md#insn-00851970)
- 新版 [`00851970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851948.md#insn-00851970)

~~~diff
- 00851970 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00851970 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00851970 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00851970 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00851970 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00851970 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00851970 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00851970 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00851970 bytes 29412591
+ 00851970 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00d0f29ecfa9c141a87096664bf38d26"></a>

### [`008519f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/008519f8.md) → [`008519f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008519f8.md) FUN_008519f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00851a14",
      "incomplete_value": false,
      "site": "00851a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851a14",
      "incomplete_value": false,
      "site": "00851a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "00851a20",
      "DATA",
      [
        "storage",
        "00c02950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00851a20",
      "DATA",
      [
        "storage",
        "00c02a00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/008519f8.md#insn-00851a14)
- 新版 [`00851a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/008519f8.md#insn-00851a14)

~~~diff
- 00851a14 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00851a14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00851a14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00851a14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00851a14 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00851a14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00851a14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00851a14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00851a14 bytes 29412591
+ 00851a14 bytes 29012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ccf85800241284229d5b1515a5d28ae"></a>

### [`00851b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/00851b9c.md) → [`00851b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851b9c.md) FUN_00851b9c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0073de68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073d/0073de68.md) [`0073e4a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073e4a4.md) [`0073e89c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073e89c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0073de68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073de68.md) [`0073e4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e4a4.md) [`0073e89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e89c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.04% / 新版 99.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00851db0",
      "incomplete_value": false,
      "site": "00851db8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851db0",
      "incomplete_value": false,
      "site": "00851db8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "00851db8",
      "DATA",
      [
        "storage",
        "00c029c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00851e58",
      "READ",
      [
        "storage",
        "00c029e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00851db8",
      "DATA",
      [
        "storage",
        "00c02a70",
        null,
        "undefined *"
      ]
    ],
    [
      "00851e58",
      "READ",
      [
        "storage",
        "00c02a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00851/00851b9c.md#insn-00851db0)
- 新版 [`00851db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851b9c.md#insn-00851db0)

~~~diff
- 00851db0 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00851db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00851db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00851db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00851db0 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00851db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00851db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00851db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00851db0 bytes 08012791
+ 00851db0 bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bb1f56263b62abd499ead107107939d"></a>

### [`00852020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/00852020.md) → [`00852020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852020.md) FUN_00852020

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00852038",
      "incomplete_value": false,
      "site": "00852044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852038",
      "incomplete_value": false,
      "site": "00852044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "00852044",
      "DATA",
      [
        "storage",
        "00c029c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852044",
      "DATA",
      [
        "storage",
        "00c02a70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/00852020.md#insn-00852038)
- 新版 [`00852038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852020.md#insn-00852038)

~~~diff
- 00852038 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00852038 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00852038 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00852038 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00852038 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00852038 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00852038 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00852038 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00852038 bytes 08012791
+ 00852038 bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55a73030a98b08b9d3e19d52ed2ebccc"></a>

### [`008520b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/008520b0.md) → [`008520b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008520b0.md) FUN_008520b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008520c8",
      "incomplete_value": false,
      "site": "008520d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008520c8",
      "incomplete_value": false,
      "site": "008520d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "008520d4",
      "DATA",
      [
        "storage",
        "00c029c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008520d4",
      "DATA",
      [
        "storage",
        "00c02a70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008520c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/008520b0.md#insn-008520c8)
- 新版 [`008520c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008520b0.md#insn-008520c8)

~~~diff
- 008520c8 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 008520c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008520c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008520c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008520c8 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 008520c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008520c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008520c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008520c8 bytes 08012791
+ 008520c8 bytes 08c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cd4895dae3b71a16cef9a4578515a0c"></a>

### [`0085213c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/0085213c.md) → [`0085213c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/0085213c.md) FUN_0085213c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00852164",
      "incomplete_value": false,
      "site": "00852168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852164",
      "incomplete_value": false,
      "site": "00852168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "00852168",
      "DATA",
      [
        "storage",
        "00c029c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852168",
      "DATA",
      [
        "storage",
        "00c02a70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/0085213c.md#insn-00852164)
- 新版 [`00852164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/0085213c.md#insn-00852164)

~~~diff
- 00852164 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00852164 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00852164 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00852164 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00852164 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00852164 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00852164 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00852164 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00852164 bytes 29012791
+ 00852164 bytes 29c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cbd0fa18e9e6d0a432f313a9ad91bd2"></a>

### [`008521ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/008521ec.md) → [`008521ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008521ec.md) FUN_008521ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00852208",
      "incomplete_value": false,
      "site": "00852214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852208",
      "incomplete_value": false,
      "site": "00852214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "00852214",
      "DATA",
      [
        "storage",
        "00c029c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852214",
      "DATA",
      [
        "storage",
        "00c02a70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/008521ec.md#insn-00852208)
- 新版 [`00852208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008521ec.md#insn-00852208)

~~~diff
- 00852208 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00852208 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00852208 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00852208 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00852208 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00852208 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00852208 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00852208 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00852208 bytes 29012791
+ 00852208 bytes 29c12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d259e35c3cfe56a336edbe10e7699e52"></a>

### [`008523cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/008523cc.md) → [`008523cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008523cc.md) FUN_008523cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "008523e8",
      "incomplete_value": false,
      "site": "008523f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008523e8",
      "incomplete_value": false,
      "site": "008523f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "008523f0",
      "DATA",
      [
        "storage",
        "00c02a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008523f0",
      "DATA",
      [
        "storage",
        "00c02b00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008523e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/008523cc.md#insn-008523e8)
- 新版 [`008523e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008523cc.md#insn-008523e8)

~~~diff
- 008523e8 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 008523e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008523e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008523e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008523e8 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 008523e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008523e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008523e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008523e8 bytes 08412991
+ 008523e8 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf69216b6d29762071d1be0a6baac32a"></a>

### [`00852468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/00852468.md) → [`00852468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852468.md) FUN_00852468

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00852484",
      "incomplete_value": false,
      "site": "0085248c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852484",
      "incomplete_value": false,
      "site": "0085248c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "0085248c",
      "DATA",
      [
        "storage",
        "00c02a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085248c",
      "DATA",
      [
        "storage",
        "00c02b00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/00852468.md#insn-00852484)
- 新版 [`00852484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852468.md#insn-00852484)

~~~diff
- 00852484 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 00852484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00852484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00852484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00852484 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 00852484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00852484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00852484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00852484 bytes 08412991
+ 00852484 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a120087891480f3fe9837c090b4555c3"></a>

### [`008524fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/008524fc.md) → [`008524fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008524fc.md) FUN_008524fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00852528",
      "incomplete_value": false,
      "site": "00852528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852528",
      "incomplete_value": false,
      "site": "00852528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "00852528",
      "DATA",
      [
        "storage",
        "00c02a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852528",
      "DATA",
      [
        "storage",
        "00c02b00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/008524fc.md#insn-00852520)
- 新版 [`00852520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008524fc.md#insn-00852520)

~~~diff
- 00852520 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 00852520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00852520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00852520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00852520 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 00852520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00852520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00852520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00852520 bytes 08412991
+ 00852520 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c522a643115ff18f76e460995edf9f49"></a>

### [`008525a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/008525a4.md) → [`008525a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008525a4.md) FUN_008525a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008525c4",
      "incomplete_value": false,
      "site": "008525c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008525c4",
      "incomplete_value": false,
      "site": "008525c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "008525c4",
      "DATA",
      [
        "storage",
        "00c02a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008525c4",
      "DATA",
      [
        "storage",
        "00c02b00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008525c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/008525a4.md#insn-008525c0)
- 新版 [`008525c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/008525a4.md#insn-008525c0)

~~~diff
- 008525c0 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 008525c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008525c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008525c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008525c0 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 008525c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008525c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008525c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008525c0 bytes 08412991
+ 008525c0 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ccf6bbf05b3ffebf91a78ed945783d5"></a>

### [`0085274c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/0085274c.md) → [`0085274c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/0085274c.md) FUN_0085274c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0073e6dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073e6dc.md) [`0073eb44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073eb44.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`0084d6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084d/0084d6d0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0073e6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e6dc.md) [`0073eb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073eb44.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0084d6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d6d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.86% / 新版 98.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008528e0",
      "incomplete_value": false,
      "site": "008528e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008528e0",
      "incomplete_value": false,
      "site": "008528e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "008528e8",
      "DATA",
      [
        "storage",
        "00c02ac0",
        null,
        "undefined *"
      ]
    ],
    [
      "00852988",
      "READ",
      [
        "storage",
        "00c02ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008528e8",
      "DATA",
      [
        "storage",
        "00c02b70",
        null,
        "undefined *"
      ]
    ],
    [
      "00852988",
      "READ",
      [
        "storage",
        "00c02b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008528e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/0085274c.md#insn-008528e0)
- 新版 [`008528e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/0085274c.md#insn-008528e0)

~~~diff
- 008528e0 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 008528e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008528e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008528e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008528e0 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 008528e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008528e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008528e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008528e0 bytes 08012b91
+ 008528e0 bytes 08c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4da392bc49cf2f9f22ab4f98cb0d702"></a>

### [`00852c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/00852c58.md) → [`00852c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852c58.md) FUN_00852c58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00852c80",
      "incomplete_value": false,
      "site": "00852c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852c80",
      "incomplete_value": false,
      "site": "00852c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "00852c84",
      "DATA",
      [
        "storage",
        "00c02ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852c84",
      "DATA",
      [
        "storage",
        "00c02b70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/00852c58.md#insn-00852c80)
- 新版 [`00852c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852c58.md#insn-00852c80)

~~~diff
- 00852c80 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 00852c80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00852c80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00852c80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00852c80 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00852c80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00852c80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00852c80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00852c80 bytes 29012b91
+ 00852c80 bytes 29c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-199664d2b17ecdc86c820324c82161cf"></a>

### [`00852ee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/00852ee8.md) → [`00852ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852ee8.md) FUN_00852ee8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00852f00",
      "incomplete_value": false,
      "site": "00852f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852f00",
      "incomplete_value": false,
      "site": "00852f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
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
      "00852f0c",
      "DATA",
      [
        "storage",
        "00c02b50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852f0c",
      "DATA",
      [
        "storage",
        "00c02c00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/00852ee8.md#insn-00852f00)
- 新版 [`00852f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852ee8.md#insn-00852f00)

~~~diff
- 00852f00 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 00852f00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00852f00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00852f00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00852f00 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 00852f00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00852f00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00852f00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00852f00 bytes 08412d91
+ 00852f00 bytes 08013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95937efb3f0d3c1c2f6bbce5cacb8b40"></a>

### [`00852f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/00852f58.md) → [`00852f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852f58.md) FUN_00852f58

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00852f70",
      "incomplete_value": false,
      "site": "00852f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852f70",
      "incomplete_value": false,
      "site": "00852f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
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
      "00852f7c",
      "DATA",
      [
        "storage",
        "00c02b50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00852f7c",
      "DATA",
      [
        "storage",
        "00c02c00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00852/00852f58.md#insn-00852f70)
- 新版 [`00852f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00852/00852f58.md#insn-00852f70)

~~~diff
- 00852f70 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 00852f70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00852f70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00852f70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00852f70 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 00852f70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00852f70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00852f70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00852f70 bytes 08412d91
+ 00852f70 bytes 08013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1022999dee92b235b91e40a4ae95d60"></a>

### [`0085309c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/0085309c.md) → [`0085309c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085309c.md) FUN_0085309c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "008530b8",
      "incomplete_value": false,
      "site": "008530b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008530b8",
      "incomplete_value": false,
      "site": "008530b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b50:8"
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
      "008530b8",
      "DATA",
      [
        "storage",
        "00c02b50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008530b8",
      "DATA",
      [
        "storage",
        "00c02c00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008530b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/0085309c.md#insn-008530b0) · [`008530b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/0085309c.md#insn-008530b4)
- 新版 [`008530b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085309c.md#insn-008530b0) · [`008530b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085309c.md#insn-008530b4)

~~~diff
- 008530b0 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 008530b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008530b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008530b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008530b0 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 008530b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008530b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008530b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008530b0 bytes 08412d91
+ 008530b0 bytes 08013091
- 008530b4 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 008530b4 bytes f40301aa
+ 008530b4 ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 008530b4 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b20151897a7290b265e1d38aeba37730"></a>

### [`00853228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853228.md) → [`00853228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853228.md) FUN_00853228

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0042ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca08.md) [`00432904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432904.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0073ab94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073ab94.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`00432904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432904.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085330c",
      "incomplete_value": false,
      "site": "0085330c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085330c",
      "incomplete_value": false,
      "site": "0085330c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "0085330c",
      "DATA",
      [
        "storage",
        "00c02bc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00853388",
      "READ",
      [
        "storage",
        "00c02be8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085330c",
      "DATA",
      [
        "storage",
        "00c02c70",
        null,
        "undefined *"
      ]
    ],
    [
      "00853388",
      "READ",
      [
        "storage",
        "00c02c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853228.md#insn-00853304)
- 新版 [`00853304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853228.md#insn-00853304)

~~~diff
- 00853304 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00853304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00853304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00853304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00853304 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00853304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00853304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00853304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00853304 bytes 08012f91
+ 00853304 bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c68d234182ac1db8f5d1c31145933835"></a>

### [`008534fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/008534fc.md) → [`008534fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008534fc.md) FUN_008534fc

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
      "definition_site": "00853508",
      "incomplete_value": false,
      "site": "00853514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853508",
      "incomplete_value": false,
      "site": "00853514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "00853514",
      "DATA",
      [
        "storage",
        "00c02bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853514",
      "DATA",
      [
        "storage",
        "00c02c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/008534fc.md#insn-00853508)
- 新版 [`00853508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008534fc.md#insn-00853508)

~~~diff
- 00853508 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00853508 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00853508 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00853508 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00853508 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00853508 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00853508 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00853508 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00853508 bytes 4a012f91
+ 00853508 bytes 4ac13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c02910376721aba666da50b0f302b51"></a>

### [`00853540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853540.md) → [`00853540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853540.md) FUN_00853540

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
      "definition_site": "00853558",
      "incomplete_value": false,
      "site": "00853564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853558",
      "incomplete_value": false,
      "site": "00853564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "00853564",
      "DATA",
      [
        "storage",
        "00c02bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853564",
      "DATA",
      [
        "storage",
        "00c02c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853540.md#insn-00853558)
- 新版 [`00853558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853540.md#insn-00853558)

~~~diff
- 00853558 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00853558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00853558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00853558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00853558 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00853558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00853558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00853558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00853558 bytes 08012f91
+ 00853558 bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c148fd7759c0ed633bb6b5111e8be08"></a>

### [`0085359c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/0085359c.md) → [`0085359c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085359c.md) FUN_0085359c

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
      "definition_site": "008535c8",
      "incomplete_value": false,
      "site": "008535c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008535c8",
      "incomplete_value": false,
      "site": "008535c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "008535c8",
      "DATA",
      [
        "storage",
        "00c02bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008535c8",
      "DATA",
      [
        "storage",
        "00c02c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008535c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/0085359c.md#insn-008535c0)
- 新版 [`008535c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085359c.md#insn-008535c0)

~~~diff
- 008535c0 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 008535c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008535c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008535c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008535c0 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 008535c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008535c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008535c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008535c0 bytes 08012f91
+ 008535c0 bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ad42ce42feff1fb8743f2f8e0e58625"></a>

### [`00853624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853624.md) → [`00853624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853624.md) FUN_00853624

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
      "definition_site": "00853640",
      "incomplete_value": false,
      "site": "00853640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853640",
      "incomplete_value": false,
      "site": "00853640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "00853640",
      "DATA",
      [
        "storage",
        "00c02bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853640",
      "DATA",
      [
        "storage",
        "00c02c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085363c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853624.md#insn-0085363c)
- 新版 [`0085363c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853624.md#insn-0085363c)

~~~diff
- 0085363c ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 0085363c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085363c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085363c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085363c ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 0085363c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085363c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085363c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085363c bytes 29012f91
+ 0085363c bytes 29c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0a28f990f5a86720d9cdd14fdb3de4f"></a>

### [`008538e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/008538e0.md) → [`008538e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008538e0.md) FUN_008538e0

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
      "definition_site": "008538f4",
      "incomplete_value": false,
      "site": "008538f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008538f4",
      "incomplete_value": false,
      "site": "008538f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "008538f8",
      "DATA",
      [
        "storage",
        "00c02c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008538f8",
      "DATA",
      [
        "storage",
        "00c02d10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008538f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/008538e0.md#insn-008538f4)
- 新版 [`008538f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008538e0.md#insn-008538f4)

~~~diff
- 008538f4 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 008538f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008538f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008538f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008538f4 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 008538f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008538f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008538f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008538f4 bytes 08813191
+ 008538f4 bytes 08413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-098b346f2e06bde8ac9d6babd8b55e58"></a>

### [`0085393c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/0085393c.md) → [`0085393c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085393c.md) FUN_0085393c

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
      "definition_site": "00853954",
      "incomplete_value": false,
      "site": "00853958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853954",
      "incomplete_value": false,
      "site": "00853958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "00853958",
      "DATA",
      [
        "storage",
        "00c02c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853958",
      "DATA",
      [
        "storage",
        "00c02d10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/0085393c.md#insn-00853954)
- 新版 [`00853954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/0085393c.md#insn-00853954)

~~~diff
- 00853954 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 00853954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00853954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00853954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00853954 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00853954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00853954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00853954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00853954 bytes 08813191
+ 00853954 bytes 08413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b2d92a0e3bdc5c9160511c4f4e07c5d"></a>

### [`00853998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853998.md) → [`00853998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853998.md) FUN_00853998

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008539bc",
      "incomplete_value": false,
      "site": "008539c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008539bc",
      "incomplete_value": false,
      "site": "008539c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "008539c0",
      "DATA",
      [
        "storage",
        "00c02c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008539c0",
      "DATA",
      [
        "storage",
        "00c02d10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008539bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853998.md#insn-008539bc)
- 新版 [`008539bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853998.md#insn-008539bc)

~~~diff
- 008539bc ["COPY", "tmp:0:8", ["const:c60:8"]]
- 008539bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008539bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008539bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008539bc ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 008539bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008539bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008539bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008539bc bytes 29813191
+ 008539bc bytes 29413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79973215f31ad2a6815bbf4f1caaac26"></a>

### [`008539f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/008539f0.md) → [`008539f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008539f0.md) FUN_008539f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

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
      "definition_site": "008539f8",
      "incomplete_value": false,
      "site": "008539fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008539f8",
      "incomplete_value": false,
      "site": "008539fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "008539fc",
      "DATA",
      [
        "storage",
        "00c02c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008539fc",
      "DATA",
      [
        "storage",
        "00c02d10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008539f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/008539f0.md#insn-008539f8)
- 新版 [`008539f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/008539f0.md#insn-008539f8)

~~~diff
- 008539f8 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 008539f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008539f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008539f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008539f8 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 008539f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008539f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008539f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008539f8 bytes 29813191
+ 008539f8 bytes 29413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d11cfc112f7c779b192727fcb0c3654"></a>

### [`00853acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853acc.md) → [`00853acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853acc.md) FUN_00853acc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0042ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca08.md) [`00433930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/00433930.md) [`004418c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00441/004418c4.md) [`00853f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853f38.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`00433930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/00433930.md) [`004418c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004418c4.md) [`00853f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853f38.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00853c5c",
      "incomplete_value": false,
      "site": "00853c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853c5c",
      "incomplete_value": false,
      "site": "00853c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "00853c5c",
      "DATA",
      [
        "storage",
        "00c02cd0",
        null,
        "undefined *"
      ]
    ],
    [
      "00853cb0",
      "READ",
      [
        "storage",
        "00c02cf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853c5c",
      "DATA",
      [
        "storage",
        "00c02d80",
        null,
        "undefined *"
      ]
    ],
    [
      "00853cb0",
      "READ",
      [
        "storage",
        "00c02da8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853acc.md#insn-00853c50)
- 新版 [`00853c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853acc.md#insn-00853c50)

~~~diff
- 00853c50 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00853c50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00853c50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00853c50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00853c50 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 00853c50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00853c50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00853c50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00853c50 bytes 08413391
+ 00853c50 bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fa525d8ebb8cb05eca05be8cc9e2f8e"></a>

### [`00853e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853e08.md) → [`00853e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853e08.md) FUN_00853e08

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00853e10",
      "incomplete_value": false,
      "site": "00853e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853e10",
      "incomplete_value": false,
      "site": "00853e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "00853e14",
      "DATA",
      [
        "storage",
        "00c02cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853e14",
      "DATA",
      [
        "storage",
        "00c02d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853e08.md#insn-00853e10)
- 新版 [`00853e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853e08.md#insn-00853e10)

~~~diff
- 00853e10 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00853e10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00853e10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00853e10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00853e10 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 00853e10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00853e10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00853e10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00853e10 bytes 29413391
+ 00853e10 bytes 29013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71002785c8943d3aafac88362fb6fadc"></a>

### [`00853e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853e28.md) → [`00853e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853e28.md) FUN_00853e28

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00853e30",
      "incomplete_value": true,
      "site": "00853e34",
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
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853e30",
      "incomplete_value": true,
      "site": "00853e34",
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
            "const:cd0:8"
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
      "00853e34",
      "DATA",
      [
        "storage",
        "00c02cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853e34",
      "DATA",
      [
        "storage",
        "00c02d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853e28.md#insn-00853e30)
- 新版 [`00853e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853e28.md#insn-00853e30)

~~~diff
- 00853e30 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00853e30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00853e30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00853e30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00853e30 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 00853e30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00853e30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00853e30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00853e30 bytes 29413391
+ 00853e30 bytes 29013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81c4a29f770b6305a0bdc18ce1924bba"></a>

### [`00853e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853e68.md) → [`00853e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853e68.md) FUN_00853e68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00853e98",
      "incomplete_value": false,
      "site": "00853e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853e98",
      "incomplete_value": false,
      "site": "00853e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "00853e98",
      "DATA",
      [
        "storage",
        "00c02cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853e98",
      "DATA",
      [
        "storage",
        "00c02d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853e68.md#insn-00853e8c)
- 新版 [`00853e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853e68.md#insn-00853e8c)

~~~diff
- 00853e8c ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00853e8c ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00853e8c ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00853e8c ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00853e8c ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 00853e8c ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00853e8c ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00853e8c ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00853e8c bytes 6b413391
+ 00853e8c bytes 6b013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb17e97251f443814bec9b6bc6458f64"></a>

### [`00853ee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853ee4.md) → [`00853ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853ee4.md) FUN_00853ee4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

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
      "definition_site": "00853ef0",
      "incomplete_value": false,
      "site": "00853ef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853ef0",
      "incomplete_value": false,
      "site": "00853ef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "00853ef0",
      "DATA",
      [
        "storage",
        "00c02cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00853ef0",
      "DATA",
      [
        "storage",
        "00c02d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00853/00853ee4.md#insn-00853eec)
- 新版 [`00853eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853ee4.md#insn-00853eec)

~~~diff
- 00853eec ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00853eec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00853eec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00853eec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00853eec ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 00853eec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00853eec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00853eec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00853eec bytes 29413391
+ 00853eec bytes 29013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-767442ce5cdcba7f3261576ab63fab8b"></a>

### [`00854110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854110.md) → [`00854110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854110.md) _INIT_159

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085414c",
      "incomplete_value": true,
      "site": "00854168",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085414c",
      "incomplete_value": true,
      "site": "00854168",
      "value": [
        "LOAD",
        "16",
        [
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
      "definition_site": "00854170",
      "incomplete_value": true,
      "site": "0085418c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00854170",
      "incomplete_value": true,
      "site": "0085418c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008541b0",
      "incomplete_value": true,
      "site": "008541c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008541b0",
      "incomplete_value": true,
      "site": "008541c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0085414c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00854170",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00854190",
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
      "0085414c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00854170",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00854190",
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

- 旧版 [`0085413c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854110.md#insn-0085413c) · [`00854144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854110.md#insn-00854144)
- 新版 [`0085413c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854110.md#insn-0085413c) · [`00854144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854110.md#insn-00854144)

~~~diff
- 0085413c ["COPY", "tmp:0:8", ["const:510:8"]]
- 0085413c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0085413c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0085413c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0085413c ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 0085413c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0085413c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0085413c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0085413c bytes 73421491
+ 0085413c bytes 73421791
- 00854144 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00854144 bytes 89d2fff0
+ 00854144 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00854144 bytes 89d2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-602d1ca5c8281b294dbe52ffbea00493"></a>

### [`008544a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md) → [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) FUN_008544a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 10件 [`008577f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/008577f8.md) [`00857d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857d90.md) [`00857eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857eb4.md) [`00857fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857fd8.md) [`008580fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008580fc.md) · 呼出先 12件 [`00855e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855e58.md) [`00855e5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855e5c.md) [`00855ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855ea4.md) [`00856058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856058.md) [`0085605c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/0085605c.md)
- 新版 呼出元 10件 [`008577f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008577f8.md) [`00857d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857d90.md) [`00857eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857eb4.md) [`00857fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857fd8.md) [`008580fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580fc.md) · 呼出先 12件 [`00855e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e58.md) [`00855e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e5c.md) [`00855ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855ea4.md) [`00856058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856058.md) [`0085605c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/0085605c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008544d4",
      "incomplete_value": false,
      "site": "008544d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008544d4",
      "incomplete_value": false,
      "site": "008544d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d60:8"
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
      "008544d8",
      "DATA",
      [
        "storage",
        "00c02d60",
        null,
        "pointer"
      ]
    ],
    [
      "00854510",
      "DATA",
      [
        "storage",
        "00c02f18",
        null,
        "undefined *"
      ]
    ],
    [
      "00854544",
      "READ",
      [
        "storage",
        "00c02f38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008544d8",
      "DATA",
      [
        "storage",
        "00c02e10",
        null,
        "pointer"
      ]
    ],
    [
      "00854510",
      "DATA",
      [
        "storage",
        "00c02fc8",
        null,
        "undefined *"
      ]
    ],
    [
      "00854544",
      "READ",
      [
        "storage",
        "00c02fe8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008544d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md#insn-008544d4) · [`008544e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md#insn-008544e0) · [`0085454c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md#insn-0085454c)
- 新版 [`008544d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md#insn-008544d4) · [`008544e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md#insn-008544e0) · [`0085454c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md#insn-0085454c)

~~~diff
- 008544d4 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 008544d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008544d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008544d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008544d4 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 008544d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008544d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008544d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008544d4 bytes 08813591
+ 008544d4 bytes 08413891
- 008544e0 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 008544e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008544e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008544e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008544e0 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 008544e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008544e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008544e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008544e0 bytes 08613c91
+ 008544e0 bytes 08213f91
- 0085454c ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 0085454c ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085454c bytes 681d00d0
+ 0085454c bytes 681d00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c18cdd24fbdf75d7d7c575f367d09b4"></a>

### [`00854718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854718.md) → [`00854718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854718.md) FUN_00854718

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0081f58c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f58c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0081f58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f58c.md) · 呼出先 0件 

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
      "definition_site": "0085472c",
      "incomplete_value": false,
      "site": "00854730",
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
            "const:bc4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085472c",
      "incomplete_value": false,
      "site": "00854730",
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
            "const:bcd:8"
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
      "00854730",
      "DATA",
      [
        "storage",
        "002a9bcd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00854730",
      "DATA",
      [
        "storage",
        "002a9bc4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085472c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854718.md#insn-0085472c)
- 新版 [`0085472c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854718.md#insn-0085472c)

~~~diff
- 0085472c ["COPY", "tmp:0:8", ["const:bcd:8"]]
- 0085472c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085472c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085472c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085472c ["COPY", "tmp:0:8", ["const:bc4:8"]]
+ 0085472c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085472c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085472c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085472c bytes 08352f91
+ 0085472c bytes 08112f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-458190c9adc8e8026ba988c1cc62b831"></a>

### [`00854808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854808.md) → [`00854808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854808.md) FUN_00854808

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00a3cca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a3c/00a3cca4.md) · 呼出先 4件 [`00856bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856bc4.md) [`00856bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856bc8.md) [`00ad74d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad74d0.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00a3cca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3c/00a3cca4.md) · 呼出先 4件 [`00856bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bc4.md) [`00856bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bc8.md) [`00ad7598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7598.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "0085483c",
      "incomplete_value": false,
      "site": "0085483c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085483c",
      "incomplete_value": false,
      "site": "0085483c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "0085483c",
      "DATA",
      [
        "storage",
        "00c03138",
        null,
        "undefined *"
      ]
    ],
    [
      "0085487c",
      "READ",
      [
        "storage",
        "00c03158",
        null,
        "pointer"
      ]
    ],
    [
      "0085487c",
      "READ",
      [
        "storage",
        "00c03160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085483c",
      "DATA",
      [
        "storage",
        "00c031e8",
        null,
        "undefined *"
      ]
    ],
    [
      "0085487c",
      "READ",
      [
        "storage",
        "00c03208",
        null,
        "pointer"
      ]
    ],
    [
      "0085487c",
      "READ",
      [
        "storage",
        "00c03210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00854834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854808.md#insn-00854834)
- 新版 [`00854834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854808.md#insn-00854834)

~~~diff
- 00854834 ["COPY", "tmp:0:8", ["const:138:8"]]
- 00854834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00854834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00854834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00854834 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 00854834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00854834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00854834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00854834 bytes 08e10491
+ 00854834 bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dc5f31182098c399c4d381a1a396f8a"></a>

### [`00854900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854900.md) → [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) FUN_00854900

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`005d996c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005e0/005e02b0.md) [`0068d484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068d/0068d484.md) [`007127f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00712/007127f8.md) [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) · 呼出先 24件 [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) [`00574bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574bb4.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`0084bae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084b/0084bae8.md) [`00855054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855054.md)
- 新版 呼出元 7件 [`005d996c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005e0/005e02b0.md) [`0068d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md) [`007127f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00712/007127f8.md) [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 24件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`00574bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bb4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0084bae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084b/0084bae8.md) [`00855054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855054.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.76% / 新版 99.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00854a50",
      "incomplete_value": true,
      "site": "00854a58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00854a50",
      "incomplete_value": true,
      "site": "00854a58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:780:8"
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
      "00854a50",
      "READ",
      [
        "storage",
        "00c1b780",
        null,
        "pointer"
      ]
    ],
    [
      "00854a50",
      "PARAM",
      [
        "storage",
        "0109e370",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00854a50",
      "READ",
      [
        "storage",
        "00c1b830",
        null,
        "pointer"
      ]
    ],
    [
      "00854a50",
      "PARAM",
      [
        "storage",
        "0109e430",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00854a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854900.md#insn-00854a50)
- 新版 [`00854a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md#insn-00854a50)

~~~diff
- 00854a50 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:780:8"]]
- 00854a50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00854a50 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:830:8"]]
+ 00854a50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00854a50 bytes 21c043f9
+ 00854a50 bytes 211844f9
~~~


<a id="compare-2802d7f14ce836e20731d92949175efc"></a>

### [`00855450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855450.md) → [`00855450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855450.md) FUN_00855450

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`005f0e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005f0/005f0e9c.md) [`0060081c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00600/0060081c.md) [`006d5524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d5/006d5524.md) [`007172c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00717/007172c8.md) [`007ca13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca13c.md) · 呼出先 11件 [`0056c55c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c55c.md) [`00858960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858960.md) [`00858964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858964.md) [`00858a70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858a70.md) [`00858a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858a74.md)
- 新版 呼出元 6件 [`005f0e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0e9c.md) [`0060081c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00600/0060081c.md) [`006d5524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d5524.md) [`007172c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/007172c8.md) [`007ca13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca13c.md) · 呼出先 11件 [`0056c55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c55c.md) [`00858960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858960.md) [`00858964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858964.md) [`00858a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858a70.md) [`00858a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858a74.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.43% / 新版 95.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008555b0",
      "incomplete_value": false,
      "site": "008555b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008555b0",
      "incomplete_value": false,
      "site": "008555b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "definition_site": "008555d4",
      "incomplete_value": false,
      "site": "008555d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008555d4",
      "incomplete_value": false,
      "site": "008555d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
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
      "definition_site": "008555ec",
      "incomplete_value": false,
      "site": "008555ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008555ec",
      "incomplete_value": false,
      "site": "008555ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "008555b0",
      "DATA",
      [
        "storage",
        "00c03568",
        null,
        "undefined *"
      ]
    ],
    [
      "008555d4",
      "DATA",
      [
        "storage",
        "00c035e8",
        null,
        "undefined *"
      ]
    ],
    [
      "008555ec",
      "DATA",
      [
        "storage",
        "00c03668",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008555b0",
      "DATA",
      [
        "storage",
        "00c03618",
        null,
        "undefined *"
      ]
    ],
    [
      "008555d4",
      "DATA",
      [
        "storage",
        "00c03698",
        null,
        "undefined *"
      ]
    ],
    [
      "008555ec",
      "DATA",
      [
        "storage",
        "00c03718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008555ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855450.md#insn-008555ac) · [`008555d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855450.md#insn-008555d0) · [`008555e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855450.md#insn-008555e8)
- 新版 [`008555ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855450.md#insn-008555ac) · [`008555d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855450.md#insn-008555d0) · [`008555e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855450.md#insn-008555e8)

~~~diff
- 008555ac ["COPY", "tmp:0:8", ["const:568:8"]]
- 008555ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008555ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008555ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008555ac ["COPY", "tmp:0:8", ["const:618:8"]]
+ 008555ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008555ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008555ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008555ac bytes 29a11591
+ 008555ac bytes 29611891
- 008555d0 ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 008555d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008555d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008555d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008555d0 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 008555d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008555d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008555d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008555d0 bytes 4aa11791
+ 008555d0 bytes 4a611a91
- 008555e8 ["COPY", "tmp:0:8", ["const:668:8"]]
- 008555e8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008555e8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008555e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008555e8 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 008555e8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008555e8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008555e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008555e8 bytes 4aa11991
+ 008555e8 bytes 4a611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e15d61bfddba02313d00a0a4bc62a89"></a>

### [`0085587c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/0085587c.md) → [`0085587c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/0085587c.md) FUN_0085587c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007ca3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca3b0.md) · 呼出先 4件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md)
- 新版 呼出元 1件 [`007ca3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca3b0.md) · 呼出先 4件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0085595c",
      "incomplete_value": false,
      "site": "0085596c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085595c",
      "incomplete_value": false,
      "site": "0085596c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "definition_site": "00855964",
      "incomplete_value": false,
      "site": "0085596c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00855964",
      "incomplete_value": false,
      "site": "0085596c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "0085595c",
      "PARAM",
      [
        "storage",
        "00c02e50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00855964",
      "PARAM",
      [
        "storage",
        "00c02e60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0085595c",
      "PARAM",
      [
        "storage",
        "00c02f00",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00855964",
      "PARAM",
      [
        "storage",
        "00c02f10",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/0085587c.md#insn-0085595c) · [`00855964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/0085587c.md#insn-00855964)
- 新版 [`0085595c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/0085587c.md#insn-0085595c) · [`00855964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/0085587c.md#insn-00855964)

~~~diff
- 0085595c ["COPY", "tmp:0:8", ["const:e50:8"]]
- 0085595c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0085595c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0085595c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0085595c ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 0085595c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0085595c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0085595c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0085595c bytes 21403991
+ 0085595c bytes 21003c91
- 00855964 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 00855964 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00855964 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00855964 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00855964 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 00855964 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00855964 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00855964 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00855964 bytes 42803991
+ 00855964 bytes 42403c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-977cc4dd443e956a50eb0c2380458d6a"></a>

### [`008559d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/008559d8.md) → [`008559d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/008559d8.md) FUN_008559d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006d584c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d5/006d584c.md) [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 5件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md)
- 新版 呼出元 2件 [`006d584c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d5/006d584c.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 5件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00855ca4",
      "incomplete_value": false,
      "site": "00855cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00855ca4",
      "incomplete_value": false,
      "site": "00855cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00855d28",
      "incomplete_value": false,
      "site": "00855d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00855d28",
      "incomplete_value": false,
      "site": "00855d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00855d30",
      "incomplete_value": false,
      "site": "00855d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00855d30",
      "incomplete_value": false,
      "site": "00855d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00855c44",
      "PARAM",
      [
        "storage",
        "00c02e50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00855c4c",
      "PARAM",
      [
        "storage",
        "00c02ed8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00855c9c",
      "PARAM",
      [
        "storage",
        "00c02e50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00855c44",
      "PARAM",
      [
        "storage",
        "00c02f00",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00855c4c",
      "PARAM",
      [
        "storage",
        "00c02f88",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00855c9c",
      "PARAM",
      [
        "storage",
        "00c02f00",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00855c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/008559d8.md#insn-00855c44) · [`00855c4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/008559d8.md#insn-00855c4c) · [`00855c9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/008559d8.md#insn-00855c9c)
- 新版 [`00855c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/008559d8.md#insn-00855c44) · [`00855c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/008559d8.md#insn-00855c4c) · [`00855c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/008559d8.md#insn-00855c9c)

~~~diff
- 00855c44 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00855c44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00855c44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00855c44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00855c44 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 00855c44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00855c44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00855c44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00855c44 bytes 21403991
+ 00855c44 bytes 21003c91
- 00855c4c ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 00855c4c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00855c4c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00855c4c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00855c4c ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 00855c4c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00855c4c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00855c4c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00855c4c bytes 42603b91
+ 00855c4c bytes 42203e91
- 00855c9c ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00855c9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00855c9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00855c9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00855c9c ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 00855c9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00855c9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00855c9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00855c9c bytes 21403991
+ 00855c9c bytes 21003c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bb45061b83e32dfaa9d00d4131ef55f"></a>

### [`00855e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855e10.md) → [`00855e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e10.md) FUN_00855e10

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
      "definition_site": "00855e34",
      "incomplete_value": true,
      "site": "00855e34",
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
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00855e34",
      "incomplete_value": true,
      "site": "00855e34",
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
            "const:f18:8"
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
      "00855e34",
      "DATA",
      [
        "storage",
        "00c02f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00855e34",
      "DATA",
      [
        "storage",
        "00c02fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00855e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855e10.md#insn-00855e30)
- 新版 [`00855e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e10.md#insn-00855e30)

~~~diff
- 00855e30 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 00855e30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00855e30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00855e30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00855e30 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00855e30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00855e30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00855e30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00855e30 bytes 08613c91
+ 00855e30 bytes 08213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b2a025ca0b57cb57c7359ba2099b4c9"></a>

### [`00855e44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855e44.md) → [`00855e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e44.md) FUN_00855e44

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
      "definition_site": "00855e50",
      "incomplete_value": false,
      "site": "00855e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00855e50",
      "incomplete_value": false,
      "site": "00855e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "00855e50",
      "DATA",
      [
        "storage",
        "00c02f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00855e50",
      "DATA",
      [
        "storage",
        "00c02fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00855e4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00855/00855e44.md#insn-00855e4c)
- 新版 [`00855e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00855/00855e44.md#insn-00855e4c)

~~~diff
- 00855e4c ["COPY", "tmp:0:8", ["const:f18:8"]]
- 00855e4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00855e4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00855e4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00855e4c ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00855e4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00855e4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00855e4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00855e4c bytes 29613c91
+ 00855e4c bytes 29213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f82bcc2ada2f3b22b85073017f2f603"></a>

### [`00856010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856010.md) → [`00856010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856010.md) FUN_00856010

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
      "definition_site": "00856034",
      "incomplete_value": false,
      "site": "00856034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856034",
      "incomplete_value": false,
      "site": "00856034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "00856034",
      "DATA",
      [
        "storage",
        "00c02fa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00856034",
      "DATA",
      [
        "storage",
        "00c03058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085602c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856010.md#insn-0085602c) · [`00856030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856010.md#insn-00856030)
- 新版 [`0085602c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856010.md#insn-0085602c) · [`00856030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856010.md#insn-00856030)

~~~diff
- 0085602c ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 0085602c ["COPY", "register:4040:8", ["const:c03000:8"]]
- 0085602c bytes 681d0090
+ 0085602c bytes 681d00b0
- 00856030 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 00856030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00856030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00856030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00856030 ["COPY", "tmp:0:8", ["const:58:8"]]
+ 00856030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00856030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00856030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00856030 bytes 08a13e91
+ 00856030 bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0034804ff0f5fe460c44f50c131e28c"></a>

### [`00856204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856204.md) → [`00856204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856204.md) FUN_00856204

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
      "definition_site": "00856218",
      "incomplete_value": false,
      "site": "0085621c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856218",
      "incomplete_value": false,
      "site": "0085621c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "0085621c",
      "DATA",
      [
        "storage",
        "00c03038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085621c",
      "DATA",
      [
        "storage",
        "00c030e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856204.md#insn-00856218)
- 新版 [`00856218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856204.md#insn-00856218)

~~~diff
- 00856218 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00856218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00856218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00856218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00856218 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00856218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00856218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00856218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00856218 bytes 08e10091
+ 00856218 bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a4ea824304a8a9551b1cc841531c10f"></a>

### [`00856228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856228.md) → [`00856228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856228.md) FUN_00856228

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
      "definition_site": "0085622c",
      "incomplete_value": false,
      "site": "00856230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085622c",
      "incomplete_value": false,
      "site": "00856230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "00856230",
      "DATA",
      [
        "storage",
        "00c03038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00856230",
      "DATA",
      [
        "storage",
        "00c030e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085622c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856228.md#insn-0085622c)
- 新版 [`0085622c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856228.md#insn-0085622c)

~~~diff
- 0085622c ["COPY", "tmp:0:8", ["const:38:8"]]
- 0085622c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085622c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085622c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085622c ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 0085622c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085622c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085622c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085622c bytes 08e10091
+ 0085622c bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de91fa7ccf6b2e0600e668cb74269d29"></a>

### [`00856700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856700.md) → [`00856700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856700.md) FUN_00856700

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
      "definition_site": "00856724",
      "incomplete_value": false,
      "site": "00856724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856724",
      "incomplete_value": false,
      "site": "00856724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:b8:8"
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
      "00856724",
      "DATA",
      [
        "storage",
        "00c030b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00856724",
      "DATA",
      [
        "storage",
        "00c03168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856700.md#insn-00856720)
- 新版 [`00856720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856700.md#insn-00856720)

~~~diff
- 00856720 ["COPY", "tmp:0:8", ["const:b8:8"]]
- 00856720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00856720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00856720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00856720 ["COPY", "tmp:0:8", ["const:168:8"]]
+ 00856720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00856720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00856720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00856720 bytes 08e10291
+ 00856720 bytes 08a10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fa7d69181e4b36eee3e078d465bc6cb"></a>

### [`00856bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856bb0.md) → [`00856bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bb0.md) FUN_00856bb0

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
      "definition_site": "00856bbc",
      "incomplete_value": false,
      "site": "00856bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856bbc",
      "incomplete_value": false,
      "site": "00856bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "00856bbc",
      "DATA",
      [
        "storage",
        "00c03138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00856bbc",
      "DATA",
      [
        "storage",
        "00c031e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856bb0.md#insn-00856bb8)
- 新版 [`00856bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bb0.md#insn-00856bb8)

~~~diff
- 00856bb8 ["COPY", "tmp:0:8", ["const:138:8"]]
- 00856bb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00856bb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00856bb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00856bb8 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 00856bb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00856bb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00856bb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00856bb8 bytes 29e10491
+ 00856bb8 bytes 29a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75656dba0465a4c90edb6f3dca3aadd9"></a>

### [`00856bcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856bcc.md) → [`00856bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bcc.md) FUN_00856bcc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00856d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856d90.md) [`00856d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856d94.md) [`0085718c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/0085718c.md) [`00857190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857190.md) [`00ad7c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad7/00ad7c7c.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00856d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856d90.md) [`00856d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856d94.md) [`0085718c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/0085718c.md) [`00857190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857190.md) [`00ad7d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7d44.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.57% / 新版 90.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00856c04",
      "incomplete_value": false,
      "site": "00856c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856c04",
      "incomplete_value": false,
      "site": "00856c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "definition_site": "00856c10",
      "incomplete_value": false,
      "site": "00856c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856c10",
      "incomplete_value": false,
      "site": "00856c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "00856c04",
      "DATA",
      [
        "storage",
        "00c031a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00856c10",
      "DATA",
      [
        "storage",
        "00c03228",
        null,
        "undefined *"
      ]
    ],
    [
      "00856c44",
      "READ",
      [
        "storage",
        "00c03248",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00856c04",
      "DATA",
      [
        "storage",
        "00c03258",
        null,
        "undefined *"
      ]
    ],
    [
      "00856c10",
      "DATA",
      [
        "storage",
        "00c032d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00856c44",
      "READ",
      [
        "storage",
        "00c032f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856be4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856bcc.md#insn-00856be4) · [`00856c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856bcc.md#insn-00856c08)
- 新版 [`00856be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bcc.md#insn-00856be4) · [`00856c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856bcc.md#insn-00856c08)

~~~diff
- 00856be4 ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 00856be4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00856be4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00856be4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00856be4 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00856be4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00856be4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00856be4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00856be4 bytes 29a10691
+ 00856be4 bytes 29610991
- 00856c08 ["COPY", "register:4048:8", ["const:c03000:8"]]
- 00856c08 bytes 691d00b0
+ 00856c08 ["COPY", "register:4048:8", ["const:c03000:8"]]
+ 00856c08 bytes 691d00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49d61793537647cd7af9cbe732ff8ddb"></a>

### [`00856d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856d48.md) → [`00856d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856d48.md) FUN_00856d48

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
      "definition_site": "00856d6c",
      "incomplete_value": false,
      "site": "00856d6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856d6c",
      "incomplete_value": false,
      "site": "00856d6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "00856d6c",
      "DATA",
      [
        "storage",
        "00c031a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00856d6c",
      "DATA",
      [
        "storage",
        "00c03258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856d48.md#insn-00856d68)
- 新版 [`00856d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856d48.md#insn-00856d68)

~~~diff
- 00856d68 ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 00856d68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00856d68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00856d68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00856d68 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00856d68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00856d68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00856d68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00856d68 bytes 08a10691
+ 00856d68 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b486a9a207e4995daa74432e6c0a1538"></a>

### [`00856d7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856d7c.md) → [`00856d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856d7c.md) FUN_00856d7c

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
      "definition_site": "00856d88",
      "incomplete_value": false,
      "site": "00856d88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00856d88",
      "incomplete_value": false,
      "site": "00856d88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "00856d88",
      "DATA",
      [
        "storage",
        "00c031a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00856d88",
      "DATA",
      [
        "storage",
        "00c03258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00856d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00856/00856d7c.md#insn-00856d84)
- 新版 [`00856d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00856/00856d7c.md#insn-00856d84)

~~~diff
- 00856d84 ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 00856d84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00856d84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00856d84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00856d84 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00856d84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00856d84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00856d84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00856d84 bytes 29a10691
+ 00856d84 bytes 29610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e83a77125ad4e9bc8b5f4cfe3d84d1c9"></a>

### [`00857144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857144.md) → [`00857144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857144.md) FUN_00857144

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
      "definition_site": "00857168",
      "incomplete_value": false,
      "site": "00857168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857168",
      "incomplete_value": false,
      "site": "00857168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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
      "00857168",
      "DATA",
      [
        "storage",
        "00c03228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00857168",
      "DATA",
      [
        "storage",
        "00c032d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857144.md#insn-00857164)
- 新版 [`00857164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857144.md#insn-00857164)

~~~diff
- 00857164 ["COPY", "tmp:0:8", ["const:228:8"]]
- 00857164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857164 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 00857164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857164 bytes 08a10891
+ 00857164 bytes 08610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3c4209be4fc05d4b3e228cb46ec84f8"></a>

### [`00857178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857178.md) → [`00857178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857178.md) FUN_00857178

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
      "definition_site": "00857184",
      "incomplete_value": false,
      "site": "00857184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857184",
      "incomplete_value": false,
      "site": "00857184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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
      "00857184",
      "DATA",
      [
        "storage",
        "00c03228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00857184",
      "DATA",
      [
        "storage",
        "00c032d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857178.md#insn-00857180)
- 新版 [`00857180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857178.md#insn-00857180)

~~~diff
- 00857180 ["COPY", "tmp:0:8", ["const:228:8"]]
- 00857180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00857180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00857180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00857180 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 00857180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00857180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00857180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00857180 bytes 29a10891
+ 00857180 bytes 29610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bb9c583e8d47f2744610cc4b9254e61"></a>

### [`00857194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857194.md) → [`00857194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857194.md) FUN_00857194

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00469f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md) [`00678b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0067c/0067c7f0.md) [`0067c9c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0067c/0067c9c0.md) [`0067c9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0067c/0067c9c4.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00678b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c7f0.md) [`0067c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c0.md) [`0067c9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c4.md)

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
      "definition_site": "00857230",
      "incomplete_value": false,
      "site": "0085723c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857230",
      "incomplete_value": false,
      "site": "0085723c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "0085723c",
      "DATA",
      [
        "storage",
        "00c03298",
        null,
        "undefined *"
      ]
    ],
    [
      "00857288",
      "READ",
      [
        "storage",
        "00c032b8",
        null,
        "pointer"
      ]
    ],
    [
      "00857288",
      "READ",
      [
        "storage",
        "00c032c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085723c",
      "DATA",
      [
        "storage",
        "00c03348",
        null,
        "undefined *"
      ]
    ],
    [
      "00857288",
      "READ",
      [
        "storage",
        "00c03368",
        null,
        "pointer"
      ]
    ],
    [
      "00857288",
      "READ",
      [
        "storage",
        "00c03370",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857194.md#insn-00857230)
- 新版 [`00857230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857194.md#insn-00857230)

~~~diff
- 00857230 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00857230 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857230 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857230 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857230 ["COPY", "tmp:0:8", ["const:348:8"]]
+ 00857230 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857230 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857230 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857230 bytes 08610a91
+ 00857230 bytes 08210d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b89822a36238ebb8db2351f59306868c"></a>

### [`00857374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857374.md) → [`00857374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857374.md) FUN_00857374

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
      "definition_site": "00857388",
      "incomplete_value": false,
      "site": "0085738c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857388",
      "incomplete_value": false,
      "site": "0085738c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "0085738c",
      "DATA",
      [
        "storage",
        "00c03298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085738c",
      "DATA",
      [
        "storage",
        "00c03348",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857374.md#insn-00857388)
- 新版 [`00857388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857374.md#insn-00857388)

~~~diff
- 00857388 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00857388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857388 ["COPY", "tmp:0:8", ["const:348:8"]]
+ 00857388 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857388 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857388 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857388 bytes 08610a91
+ 00857388 bytes 08210d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c34ae967b59c2223e4799d64bac5e78"></a>

### [`00857398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857398.md) → [`00857398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857398.md) FUN_00857398

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
      "definition_site": "0085739c",
      "incomplete_value": false,
      "site": "008573a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085739c",
      "incomplete_value": false,
      "site": "008573a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "008573a0",
      "DATA",
      [
        "storage",
        "00c03298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008573a0",
      "DATA",
      [
        "storage",
        "00c03348",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085739c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857398.md#insn-0085739c)
- 新版 [`0085739c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857398.md#insn-0085739c)

~~~diff
- 0085739c ["COPY", "tmp:0:8", ["const:298:8"]]
- 0085739c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085739c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085739c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085739c ["COPY", "tmp:0:8", ["const:348:8"]]
+ 0085739c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085739c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085739c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085739c bytes 08610a91
+ 0085739c bytes 08210d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c901fc06148676bcf1a57d3cc76aadfe"></a>

### [`008577f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/008577f8.md) → [`008577f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008577f8.md) FUN_008577f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00857830",
      "incomplete_value": false,
      "site": "0085783c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857830",
      "incomplete_value": false,
      "site": "0085783c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "definition_site": "00857850",
      "incomplete_value": false,
      "site": "00857854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857850",
      "incomplete_value": false,
      "site": "00857854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0085786c",
      "incomplete_value": false,
      "site": "00857874",
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
            "const:8db:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085786c",
      "incomplete_value": false,
      "site": "00857874",
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
            "const:8e2:8"
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
      "0085783c",
      "DATA",
      [
        "storage",
        "00c03338",
        null,
        "undefined *"
      ]
    ],
    [
      "00857854",
      "DATA",
      [
        "storage",
        "00c02d80",
        null,
        "pointer"
      ]
    ],
    [
      "0085786c",
      "PARAM",
      [
        "storage",
        "002a28e2",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0085783c",
      "DATA",
      [
        "storage",
        "00c033e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00857854",
      "DATA",
      [
        "storage",
        "00c02e30",
        null,
        "pointer"
      ]
    ],
    [
      "0085786c",
      "PARAM",
      [
        "storage",
        "002a28db",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/008577f8.md#insn-00857830) · [`00857850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/008577f8.md#insn-00857850) · [`0085786c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/008577f8.md#insn-0085786c)
- 新版 [`00857830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008577f8.md#insn-00857830) · [`00857850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008577f8.md#insn-00857850) · [`0085786c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008577f8.md#insn-0085786c)

~~~diff
- 00857830 ["COPY", "tmp:0:8", ["const:338:8"]]
- 00857830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857830 ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 00857830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857830 bytes 08e10c91
+ 00857830 bytes 08a10f91
- 00857850 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 00857850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857850 ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 00857850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857850 bytes 08013691
+ 00857850 bytes 08c13891
- 0085786c ["COPY", "tmp:0:8", ["const:8e2:8"]]
- 0085786c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0085786c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0085786c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0085786c ["COPY", "tmp:0:8", ["const:8db:8"]]
+ 0085786c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0085786c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0085786c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0085786c bytes 21882391
+ 0085786c bytes 216c2391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73a7091d357d52c440ef605e6ae32c03"></a>

### [`008578cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/008578cc.md) → [`008578cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008578cc.md) FUN_008578cc

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
      "definition_site": "008578d0",
      "incomplete_value": false,
      "site": "008578d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008578d0",
      "incomplete_value": false,
      "site": "008578d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "008578d4",
      "DATA",
      [
        "storage",
        "00c03338",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008578d4",
      "DATA",
      [
        "storage",
        "00c033e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008578d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/008578cc.md#insn-008578d0)
- 新版 [`008578d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008578cc.md#insn-008578d0)

~~~diff
- 008578d0 ["COPY", "tmp:0:8", ["const:338:8"]]
- 008578d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008578d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008578d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008578d0 ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 008578d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008578d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008578d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008578d0 bytes 08e10c91
+ 008578d0 bytes 08a10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a22b2ed166f91b0ee58cf398b968f9a7"></a>

### [`008578dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/008578dc.md) → [`008578dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008578dc.md) FUN_008578dc

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
      "definition_site": "008578ec",
      "incomplete_value": false,
      "site": "008578f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008578ec",
      "incomplete_value": false,
      "site": "008578f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:338:8"
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
      "008578f4",
      "DATA",
      [
        "storage",
        "00c03338",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008578f4",
      "DATA",
      [
        "storage",
        "00c033e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008578ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/008578dc.md#insn-008578ec)
- 新版 [`008578ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/008578dc.md#insn-008578ec)

~~~diff
- 008578ec ["COPY", "tmp:0:8", ["const:338:8"]]
- 008578ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008578ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008578ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008578ec ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 008578ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008578ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008578ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008578ec bytes 08e10c91
+ 008578ec bytes 08a10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2741d64c6609697b217575280e00e223"></a>

### [`00857d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857d90.md) → [`00857d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857d90.md) FUN_00857d90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00857de8",
      "incomplete_value": false,
      "site": "00857dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857de8",
      "incomplete_value": false,
      "site": "00857dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00857e08",
      "incomplete_value": false,
      "site": "00857e10",
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
            "const:1ae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857e08",
      "incomplete_value": false,
      "site": "00857e10",
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
            "const:121:8"
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
      "definition_site": "00857e18",
      "incomplete_value": false,
      "site": "00857e20",
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
            "const:6fb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857e18",
      "incomplete_value": false,
      "site": "00857e20",
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
            "const:78f:8"
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
      "00857dd4",
      "DATA",
      [
        "storage",
        "00c03388",
        null,
        "undefined *"
      ]
    ],
    [
      "00857dec",
      "DATA",
      [
        "storage",
        "00c02da0",
        null,
        "pointer"
      ]
    ],
    [
      "00857e08",
      "PARAM",
      [
        "storage",
        "00298121",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00857dd4",
      "DATA",
      [
        "storage",
        "00c03438",
        null,
        "undefined *"
      ]
    ],
    [
      "00857dec",
      "DATA",
      [
        "storage",
        "00c02e50",
        null,
        "pointer"
      ]
    ],
    [
      "00857e08",
      "PARAM",
      [
        "storage",
        "002981ae",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857d90.md#insn-00857dc8) · [`00857de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857d90.md#insn-00857de8) · [`00857e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857d90.md#insn-00857e08)
- 新版 [`00857dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857d90.md#insn-00857dc8) · [`00857de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857d90.md#insn-00857de8) · [`00857e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857d90.md#insn-00857e08)

~~~diff
- 00857dc8 ["COPY", "tmp:0:8", ["const:388:8"]]
- 00857dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857dc8 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00857dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857dc8 bytes 08210e91
+ 00857dc8 bytes 08e11091
- 00857de8 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00857de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857de8 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00857de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857de8 bytes 08813691
+ 00857de8 bytes 08413991
- 00857e08 ["COPY", "tmp:0:8", ["const:121:8"]]
- 00857e08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00857e08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00857e08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00857e08 ["COPY", "tmp:0:8", ["const:1ae:8"]]
+ 00857e08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00857e08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00857e08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00857e08 bytes 21840491
+ 00857e08 bytes 21b80691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e338bae1f66624eaf64160295b832f05"></a>

### [`00857e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857e68.md) → [`00857e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857e68.md) FUN_00857e68

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
      "definition_site": "00857e6c",
      "incomplete_value": false,
      "site": "00857e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857e6c",
      "incomplete_value": false,
      "site": "00857e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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
      "00857e70",
      "DATA",
      [
        "storage",
        "00c03388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00857e70",
      "DATA",
      [
        "storage",
        "00c03438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857e6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857e68.md#insn-00857e6c)
- 新版 [`00857e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857e68.md#insn-00857e6c)

~~~diff
- 00857e6c ["COPY", "tmp:0:8", ["const:388:8"]]
- 00857e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857e6c ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00857e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857e6c bytes 08210e91
+ 00857e6c bytes 08e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfbf97dcf04317534703e215091b5e7e"></a>

### [`00857e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857e78.md) → [`00857e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857e78.md) FUN_00857e78

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
      "definition_site": "00857e88",
      "incomplete_value": false,
      "site": "00857e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857e88",
      "incomplete_value": false,
      "site": "00857e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:388:8"
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
      "00857e90",
      "DATA",
      [
        "storage",
        "00c03388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00857e90",
      "DATA",
      [
        "storage",
        "00c03438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857e78.md#insn-00857e88)
- 新版 [`00857e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857e78.md#insn-00857e88)

~~~diff
- 00857e88 ["COPY", "tmp:0:8", ["const:388:8"]]
- 00857e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857e88 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00857e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857e88 bytes 08210e91
+ 00857e88 bytes 08e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fddcb921bf80cdf0c729b09e80506fd"></a>

### [`00857eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857eb4.md) → [`00857eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857eb4.md) FUN_00857eb4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00857eec",
      "incomplete_value": false,
      "site": "00857ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857eec",
      "incomplete_value": false,
      "site": "00857ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "definition_site": "00857f0c",
      "incomplete_value": false,
      "site": "00857f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857f0c",
      "incomplete_value": false,
      "site": "00857f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00857f2c",
      "incomplete_value": false,
      "site": "00857f34",
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
            "const:a1f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857f2c",
      "incomplete_value": false,
      "site": "00857f34",
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
            "const:a26:8"
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
      "00857ef8",
      "DATA",
      [
        "storage",
        "00c033d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00857f10",
      "DATA",
      [
        "storage",
        "00c02dc0",
        null,
        "pointer"
      ]
    ],
    [
      "00857f2c",
      "PARAM",
      [
        "storage",
        "002a3a26",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00857ef8",
      "DATA",
      [
        "storage",
        "00c03488",
        null,
        "undefined *"
      ]
    ],
    [
      "00857f10",
      "DATA",
      [
        "storage",
        "00c02e70",
        null,
        "pointer"
      ]
    ],
    [
      "00857f2c",
      "PARAM",
      [
        "storage",
        "002a3a1f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857eb4.md#insn-00857eec) · [`00857f0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857eb4.md#insn-00857f0c) · [`00857f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857eb4.md#insn-00857f2c)
- 新版 [`00857eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857eb4.md#insn-00857eec) · [`00857f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857eb4.md#insn-00857f0c) · [`00857f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857eb4.md#insn-00857f2c)

~~~diff
- 00857eec ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 00857eec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857eec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857eec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857eec ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00857eec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857eec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857eec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857eec bytes 08610f91
+ 00857eec bytes 08211291
- 00857f0c ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 00857f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857f0c ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00857f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857f0c bytes 08013791
+ 00857f0c bytes 08c13991
- 00857f2c ["COPY", "tmp:0:8", ["const:a26:8"]]
- 00857f2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00857f2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00857f2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00857f2c ["COPY", "tmp:0:8", ["const:a1f:8"]]
+ 00857f2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00857f2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00857f2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00857f2c bytes 21982891
+ 00857f2c bytes 217c2891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-489361a2826302afd50c714ec8e26741"></a>

### [`00857f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857f8c.md) → [`00857f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857f8c.md) FUN_00857f8c

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
      "definition_site": "00857f90",
      "incomplete_value": false,
      "site": "00857f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857f90",
      "incomplete_value": false,
      "site": "00857f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "00857f94",
      "DATA",
      [
        "storage",
        "00c033d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00857f94",
      "DATA",
      [
        "storage",
        "00c03488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857f8c.md#insn-00857f90)
- 新版 [`00857f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857f8c.md#insn-00857f90)

~~~diff
- 00857f90 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 00857f90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857f90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857f90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857f90 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00857f90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857f90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857f90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857f90 bytes 08610f91
+ 00857f90 bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e64cb2514cc5ce8d9f75f87d99fcbce"></a>

### [`00857f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857f9c.md) → [`00857f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857f9c.md) FUN_00857f9c

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
      "definition_site": "00857fac",
      "incomplete_value": false,
      "site": "00857fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00857fac",
      "incomplete_value": false,
      "site": "00857fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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
      "00857fb4",
      "DATA",
      [
        "storage",
        "00c033d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00857fb4",
      "DATA",
      [
        "storage",
        "00c03488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00857fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857f9c.md#insn-00857fac)
- 新版 [`00857fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857f9c.md#insn-00857fac)

~~~diff
- 00857fac ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 00857fac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00857fac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00857fac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00857fac ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00857fac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00857fac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00857fac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00857fac bytes 08610f91
+ 00857fac bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-040e246be6b4426ee1f3aee0c73733a7"></a>

### [`00857fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857fd8.md) → [`00857fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857fd8.md) FUN_00857fd8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858030",
      "incomplete_value": false,
      "site": "00858034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858030",
      "incomplete_value": false,
      "site": "00858034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00858058"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00858060",
      "incomplete_value": false,
      "site": "00858068",
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
            "const:c41:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858060",
      "incomplete_value": false,
      "site": "00858068",
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
            "const:c48:8"
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
      "0085801c",
      "DATA",
      [
        "storage",
        "00c03428",
        null,
        "undefined *"
      ]
    ],
    [
      "00858034",
      "DATA",
      [
        "storage",
        "00c02de0",
        null,
        "pointer"
      ]
    ],
    [
      "00858050",
      "PARAM",
      [
        "storage",
        "0029b955",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0085801c",
      "DATA",
      [
        "storage",
        "00c034d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00858034",
      "DATA",
      [
        "storage",
        "00c02e90",
        null,
        "pointer"
      ]
    ],
    [
      "00858050",
      "PARAM",
      [
        "storage",
        "0029b9e2",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857fd8.md#insn-00858058) · [`00858010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857fd8.md#insn-00858010)
- 新版 [`00858058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857fd8.md#insn-00858058) · [`00858010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857fd8.md#insn-00858010)

~~~diff
- 00858058 ["INT_ADD", "register:40f0:8", ["const:858058:8", "const:4:8"]]
- 00858058 ["CALL", null, ["callee:00bdb2f0:8"]]
- 00858058 bytes 7a0c0e94
+ 00858058 ["INT_ADD", "register:40f0:8", ["const:858058:8", "const:4:8"]]
+ 00858058 ["CALL", null, ["callee:00bdb2f0:8"]]
+ 00858058 bytes a60c0e94
- 00858010 ["COPY", "tmp:0:8", ["const:428:8"]]
- 00858010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858010 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 00858010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858010 bytes 08a11091
+ 00858010 bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bb28da7b52e08a823a6252895fcc167"></a>

### [`008580b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008580b0.md) → [`008580b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580b0.md) FUN_008580b0

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
      "definition_site": "008580b4",
      "incomplete_value": false,
      "site": "008580b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008580b4",
      "incomplete_value": false,
      "site": "008580b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "008580b8",
      "DATA",
      [
        "storage",
        "00c03428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008580b8",
      "DATA",
      [
        "storage",
        "00c034d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008580b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008580b0.md#insn-008580b4)
- 新版 [`008580b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580b0.md#insn-008580b4)

~~~diff
- 008580b4 ["COPY", "tmp:0:8", ["const:428:8"]]
- 008580b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008580b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008580b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008580b4 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 008580b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008580b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008580b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008580b4 bytes 08a11091
+ 008580b4 bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8314fb015e020f02ea8ae52b1e6e575f"></a>

### [`008580fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008580fc.md) → [`008580fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580fc.md) FUN_008580fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858134",
      "incomplete_value": false,
      "site": "00858140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858134",
      "incomplete_value": false,
      "site": "00858140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "definition_site": "00858154",
      "incomplete_value": false,
      "site": "00858158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858154",
      "incomplete_value": false,
      "site": "00858158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00858170",
      "incomplete_value": false,
      "site": "00858178",
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
            "const:7ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858170",
      "incomplete_value": false,
      "site": "00858178",
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
            "const:880:8"
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
      "00858140",
      "DATA",
      [
        "storage",
        "00c03478",
        null,
        "undefined *"
      ]
    ],
    [
      "00858158",
      "DATA",
      [
        "storage",
        "00c02e20",
        null,
        "pointer"
      ]
    ],
    [
      "00858170",
      "PARAM",
      [
        "storage",
        "002a8880",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00858140",
      "DATA",
      [
        "storage",
        "00c03528",
        null,
        "undefined *"
      ]
    ],
    [
      "00858158",
      "DATA",
      [
        "storage",
        "00c02ed0",
        null,
        "pointer"
      ]
    ],
    [
      "00858170",
      "PARAM",
      [
        "storage",
        "002a87ec",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008580fc.md#insn-00858134) · [`00858154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008580fc.md#insn-00858154) · [`00858170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008580fc.md#insn-00858170)
- 新版 [`00858134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580fc.md#insn-00858134) · [`00858154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580fc.md#insn-00858154) · [`00858170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580fc.md#insn-00858170)

~~~diff
- 00858134 ["COPY", "tmp:0:8", ["const:478:8"]]
- 00858134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858134 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 00858134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858134 bytes 08e11191
+ 00858134 bytes 08a11491
- 00858154 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 00858154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858154 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00858154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858154 bytes 08813891
+ 00858154 bytes 08413b91
- 00858170 ["COPY", "tmp:0:8", ["const:880:8"]]
- 00858170 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00858170 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00858170 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00858170 ["COPY", "tmp:0:8", ["const:7ec:8"]]
+ 00858170 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00858170 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00858170 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00858170 bytes 21002291
+ 00858170 bytes 21b01f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e221362a7e1a2d63c97aad37bce8cf5"></a>

### [`008581d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008581d0.md) → [`008581d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008581d0.md) FUN_008581d0

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
      "definition_site": "008581d4",
      "incomplete_value": false,
      "site": "008581d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008581d4",
      "incomplete_value": false,
      "site": "008581d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "008581d8",
      "DATA",
      [
        "storage",
        "00c03478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008581d8",
      "DATA",
      [
        "storage",
        "00c03528",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008581d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008581d0.md#insn-008581d4)
- 新版 [`008581d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008581d0.md#insn-008581d4)

~~~diff
- 008581d4 ["COPY", "tmp:0:8", ["const:478:8"]]
- 008581d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008581d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008581d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008581d4 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 008581d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008581d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008581d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008581d4 bytes 08e11191
+ 008581d4 bytes 08a11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2617f20b4586c3d6a53b57ca8e9fb6db"></a>

### [`008581e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008581e0.md) → [`008581e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008581e0.md) FUN_008581e0

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
      "definition_site": "008581f0",
      "incomplete_value": false,
      "site": "008581f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008581f0",
      "incomplete_value": false,
      "site": "008581f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "008581f8",
      "DATA",
      [
        "storage",
        "00c03478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008581f8",
      "DATA",
      [
        "storage",
        "00c03528",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008581f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008581e0.md#insn-008581f0)
- 新版 [`008581f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008581e0.md#insn-008581f0)

~~~diff
- 008581f0 ["COPY", "tmp:0:8", ["const:478:8"]]
- 008581f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008581f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008581f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008581f0 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 008581f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008581f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008581f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008581f0 bytes 08e11191
+ 008581f0 bytes 08a11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3f8c00019ea4c7bff49717ef1d99e24"></a>

### [`0085821c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/0085821c.md) → [`0085821c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085821c.md) FUN_0085821c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858254",
      "incomplete_value": false,
      "site": "00858260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858254",
      "incomplete_value": false,
      "site": "00858260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "definition_site": "00858274",
      "incomplete_value": false,
      "site": "00858278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858274",
      "incomplete_value": false,
      "site": "00858278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00858290",
      "incomplete_value": false,
      "site": "00858298",
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
            "const:9c1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858290",
      "incomplete_value": false,
      "site": "00858298",
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
            "const:a55:8"
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
      "00858260",
      "DATA",
      [
        "storage",
        "00c034c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00858278",
      "DATA",
      [
        "storage",
        "00c02e00",
        null,
        "pointer"
      ]
    ],
    [
      "00858290",
      "PARAM",
      [
        "storage",
        "002a7a55",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00858260",
      "DATA",
      [
        "storage",
        "00c03578",
        null,
        "undefined *"
      ]
    ],
    [
      "00858278",
      "DATA",
      [
        "storage",
        "00c02eb0",
        null,
        "pointer"
      ]
    ],
    [
      "00858290",
      "PARAM",
      [
        "storage",
        "002a79c1",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/0085821c.md#insn-00858254) · [`00858274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/0085821c.md#insn-00858274) · [`00858290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/0085821c.md#insn-00858290)
- 新版 [`00858254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085821c.md#insn-00858254) · [`00858274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085821c.md#insn-00858274) · [`00858290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085821c.md#insn-00858290)

~~~diff
- 00858254 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 00858254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858254 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00858254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858254 bytes 08211391
+ 00858254 bytes 08e11591
- 00858274 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 00858274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858274 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 00858274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858274 bytes 08013891
+ 00858274 bytes 08c13a91
- 00858290 ["COPY", "tmp:0:8", ["const:a55:8"]]
- 00858290 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00858290 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00858290 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00858290 ["COPY", "tmp:0:8", ["const:9c1:8"]]
+ 00858290 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00858290 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00858290 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00858290 bytes 21542991
+ 00858290 bytes 21042791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3878d2bfea6827ce01e87ce04fa630a2"></a>

### [`008582f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008582f0.md) → [`008582f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008582f0.md) FUN_008582f0

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
      "definition_site": "008582f4",
      "incomplete_value": false,
      "site": "008582f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008582f4",
      "incomplete_value": false,
      "site": "008582f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "008582f8",
      "DATA",
      [
        "storage",
        "00c034c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008582f8",
      "DATA",
      [
        "storage",
        "00c03578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008582f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008582f0.md#insn-008582f4)
- 新版 [`008582f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008582f0.md#insn-008582f4)

~~~diff
- 008582f4 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 008582f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008582f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008582f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008582f4 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 008582f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008582f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008582f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008582f4 bytes 08211391
+ 008582f4 bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67f86f36aa2e30aa31dcf4f1fba49f13"></a>

### [`00858300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858300.md) → [`00858300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858300.md) FUN_00858300

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
      "definition_site": "00858310",
      "incomplete_value": false,
      "site": "00858318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858310",
      "incomplete_value": false,
      "site": "00858318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "00858318",
      "DATA",
      [
        "storage",
        "00c034c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858318",
      "DATA",
      [
        "storage",
        "00c03578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858300.md#insn-00858310)
- 新版 [`00858310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858300.md#insn-00858310)

~~~diff
- 00858310 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 00858310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858310 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00858310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858310 bytes 08211391
+ 00858310 bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c934526a4212e8008c6b5ce76262fc24"></a>

### [`0085833c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/0085833c.md) → [`0085833c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085833c.md) FUN_0085833c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0085790c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/0085790c.md) [`00857ea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857ea8.md) [`00857fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00857/00857fcc.md) [`008580f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008580f0.md) [`00858210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858210.md) · 呼出先 3件 [`00574ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 7件 [`0085790c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/0085790c.md) [`00857ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857ea8.md) [`00857fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00857/00857fcc.md) [`008580f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008580f0.md) [`00858210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858210.md) · 呼出先 3件 [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858360",
      "incomplete_value": false,
      "site": "00858364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858360",
      "incomplete_value": false,
      "site": "00858364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d60:8"
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
      "00858364",
      "DATA",
      [
        "storage",
        "00c02d60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00858364",
      "DATA",
      [
        "storage",
        "00c02e10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/0085833c.md#insn-00858360)
- 新版 [`00858360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085833c.md#insn-00858360)

~~~diff
- 00858360 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 00858360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858360 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 00858360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858360 bytes 08813591
+ 00858360 bytes 08413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c810e0479ac6992954027c66b4e29e5"></a>

### [`008584c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008584c0.md) → [`008584c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008584c0.md) FUN_008584c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.80% / 新版 89.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858528",
      "incomplete_value": false,
      "site": "00858530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858528",
      "incomplete_value": false,
      "site": "00858530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "definition_site": "0085854c",
      "incomplete_value": false,
      "site": "00858554",
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
            "const:9ce:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085854c",
      "incomplete_value": false,
      "site": "00858554",
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
            "const:a62:8"
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
      "definition_site": "0085855c",
      "incomplete_value": false,
      "site": "00858564",
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
            "const:dfa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085855c",
      "incomplete_value": false,
      "site": "00858564",
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
            "const:e8e:8"
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
      "00858518",
      "DATA",
      [
        "storage",
        "00c03518",
        null,
        "undefined *"
      ]
    ],
    [
      "00858530",
      "DATA",
      [
        "storage",
        "00c02e40",
        null,
        "pointer"
      ]
    ],
    [
      "0085854c",
      "PARAM",
      [
        "storage",
        "002a7a62",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00858518",
      "DATA",
      [
        "storage",
        "00c035c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00858530",
      "DATA",
      [
        "storage",
        "00c02ef0",
        null,
        "pointer"
      ]
    ],
    [
      "0085854c",
      "PARAM",
      [
        "storage",
        "002a79ce",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085850c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008584c0.md#insn-0085850c) · [`00858528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008584c0.md#insn-00858528) · [`0085854c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008584c0.md#insn-0085854c)
- 新版 [`0085850c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008584c0.md#insn-0085850c) · [`00858528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008584c0.md#insn-00858528) · [`0085854c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008584c0.md#insn-0085854c)

~~~diff
- 0085850c ["COPY", "tmp:0:8", ["const:518:8"]]
- 0085850c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085850c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085850c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085850c ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 0085850c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085850c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085850c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085850c bytes 08611491
+ 0085850c bytes 08211791
- 00858528 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00858528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858528 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 00858528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858528 bytes 08013991
+ 00858528 bytes 08c13b91
- 0085854c ["COPY", "tmp:0:8", ["const:a62:8"]]
- 0085854c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0085854c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0085854c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0085854c ["COPY", "tmp:0:8", ["const:9ce:8"]]
+ 0085854c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0085854c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0085854c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0085854c bytes 21882991
+ 0085854c bytes 21382791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fc1e14c40e1379497e70dfe399764f3"></a>

### [`008585b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008585b0.md) → [`008585b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008585b0.md) FUN_008585b0

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
      "definition_site": "008585b4",
      "incomplete_value": false,
      "site": "008585b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008585b4",
      "incomplete_value": false,
      "site": "008585b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "008585b8",
      "DATA",
      [
        "storage",
        "00c03518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008585b8",
      "DATA",
      [
        "storage",
        "00c035c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008585b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008585b0.md#insn-008585b4)
- 新版 [`008585b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008585b0.md#insn-008585b4)

~~~diff
- 008585b4 ["COPY", "tmp:0:8", ["const:518:8"]]
- 008585b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008585b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008585b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008585b4 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 008585b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008585b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008585b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008585b4 bytes 08611491
+ 008585b4 bytes 08211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cefcc231948868165ecf92c73c9843d"></a>

### [`008585c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008585c0.md) → [`008585c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008585c0.md) FUN_008585c0

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
      "definition_site": "008585d0",
      "incomplete_value": false,
      "site": "008585d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008585d0",
      "incomplete_value": false,
      "site": "008585d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "008585d8",
      "DATA",
      [
        "storage",
        "00c03518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008585d8",
      "DATA",
      [
        "storage",
        "00c035c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008585d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008585c0.md#insn-008585d0)
- 新版 [`008585d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008585c0.md#insn-008585d0)

~~~diff
- 008585d0 ["COPY", "tmp:0:8", ["const:518:8"]]
- 008585d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008585d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008585d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008585d0 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 008585d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008585d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008585d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008585d0 bytes 08611491
+ 008585d0 bytes 08211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba331e78a10e1135f94df5caa2c73bf"></a>

### [`008585f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008585f0.md) → [`008585f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008585f0.md) FUN_008585f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00574ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff4.md) [`0085833c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/0085833c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`0085833c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085833c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "00858618",
      "incomplete_value": false,
      "site": "00858618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858618",
      "incomplete_value": false,
      "site": "00858618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "00858618",
      "DATA",
      [
        "storage",
        "00c02e40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00858618",
      "DATA",
      [
        "storage",
        "00c02ef0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085860c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/008585f0.md#insn-0085860c)
- 新版 [`0085860c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/008585f0.md#insn-0085860c)

~~~diff
- 0085860c ["COPY", "tmp:0:8", ["const:e40:8"]]
- 0085860c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085860c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085860c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085860c ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 0085860c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085860c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085860c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085860c bytes 29013991
+ 0085860c bytes 29c13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63321209924208cd3835459ee9d22995"></a>

### [`00858670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858670.md) → [`00858670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858670.md) FUN_00858670

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008586a8",
      "incomplete_value": false,
      "site": "008586b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008586a8",
      "incomplete_value": false,
      "site": "008586b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "definition_site": "008586c8",
      "incomplete_value": false,
      "site": "008586cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008586c8",
      "incomplete_value": false,
      "site": "008586cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008586e8",
      "incomplete_value": false,
      "site": "008586f0",
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
            "const:7ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008586e8",
      "incomplete_value": false,
      "site": "008586f0",
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
            "const:880:8"
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
      "008586b4",
      "DATA",
      [
        "storage",
        "00c03478",
        null,
        "undefined *"
      ]
    ],
    [
      "008586cc",
      "DATA",
      [
        "storage",
        "00c02e20",
        null,
        "pointer"
      ]
    ],
    [
      "008586e8",
      "PARAM",
      [
        "storage",
        "002a8880",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008586b4",
      "DATA",
      [
        "storage",
        "00c03528",
        null,
        "undefined *"
      ]
    ],
    [
      "008586cc",
      "DATA",
      [
        "storage",
        "00c02ed0",
        null,
        "pointer"
      ]
    ],
    [
      "008586e8",
      "PARAM",
      [
        "storage",
        "002a87ec",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008586a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858670.md#insn-008586a8) · [`008586c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858670.md#insn-008586c8) · [`008586e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858670.md#insn-008586e8)
- 新版 [`008586a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858670.md#insn-008586a8) · [`008586c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858670.md#insn-008586c8) · [`008586e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858670.md#insn-008586e8)

~~~diff
- 008586a8 ["COPY", "tmp:0:8", ["const:478:8"]]
- 008586a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008586a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008586a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008586a8 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 008586a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008586a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008586a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008586a8 bytes 08e11191
+ 008586a8 bytes 08a11491
- 008586c8 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 008586c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008586c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008586c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008586c8 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 008586c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008586c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008586c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008586c8 bytes 08813891
+ 008586c8 bytes 08413b91
- 008586e8 ["COPY", "tmp:0:8", ["const:880:8"]]
- 008586e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008586e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008586e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008586e8 ["COPY", "tmp:0:8", ["const:7ec:8"]]
+ 008586e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008586e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008586e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008586e8 bytes 21002291
+ 008586e8 bytes 21b01f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13374820dd371b1a09ae5d8b24f314c9"></a>

### [`00858748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858748.md) → [`00858748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858748.md) FUN_00858748

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00858780",
      "incomplete_value": false,
      "site": "0085878c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858780",
      "incomplete_value": false,
      "site": "0085878c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
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
      "definition_site": "008587a0",
      "incomplete_value": false,
      "site": "008587a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008587a0",
      "incomplete_value": false,
      "site": "008587a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008587c0",
      "incomplete_value": false,
      "site": "008587c8",
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
            "const:9c1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008587c0",
      "incomplete_value": false,
      "site": "008587c8",
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
            "const:a55:8"
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
      "0085878c",
      "DATA",
      [
        "storage",
        "00c034c8",
        null,
        "undefined *"
      ]
    ],
    [
      "008587a4",
      "DATA",
      [
        "storage",
        "00c02e00",
        null,
        "pointer"
      ]
    ],
    [
      "008587c0",
      "PARAM",
      [
        "storage",
        "002a7a55",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0085878c",
      "DATA",
      [
        "storage",
        "00c03578",
        null,
        "undefined *"
      ]
    ],
    [
      "008587a4",
      "DATA",
      [
        "storage",
        "00c02eb0",
        null,
        "pointer"
      ]
    ],
    [
      "008587c0",
      "PARAM",
      [
        "storage",
        "002a79c1",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858748.md#insn-00858780) · [`008587a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858748.md#insn-008587a0) · [`008587c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858748.md#insn-008587c0)
- 新版 [`00858780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858748.md#insn-00858780) · [`008587a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858748.md#insn-008587a0) · [`008587c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858748.md#insn-008587c0)

~~~diff
- 00858780 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 00858780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858780 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00858780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858780 bytes 08211391
+ 00858780 bytes 08e11591
- 008587a0 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 008587a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008587a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008587a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008587a0 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 008587a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008587a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008587a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008587a0 bytes 08013891
+ 008587a0 bytes 08c13a91
- 008587c0 ["COPY", "tmp:0:8", ["const:a55:8"]]
- 008587c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008587c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008587c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008587c0 ["COPY", "tmp:0:8", ["const:9c1:8"]]
+ 008587c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008587c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008587c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008587c0 bytes 21542991
+ 008587c0 bytes 21042791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20ddef106c0360b57a638760732a924d"></a>

### [`00858820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858820.md) → [`00858820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858820.md) FUN_00858820

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00854900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00854/008544a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00854900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/00854900.md) · 呼出先 3件 [`008544a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00854/008544a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.76% / 新版 87.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085886c",
      "incomplete_value": false,
      "site": "00858878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085886c",
      "incomplete_value": false,
      "site": "00858878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
      "definition_site": "00858888",
      "incomplete_value": false,
      "site": "00858890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858888",
      "incomplete_value": false,
      "site": "00858890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:e40:8"
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
      "definition_site": "008588ac",
      "incomplete_value": false,
      "site": "008588b4",
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
            "const:9ce:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008588ac",
      "incomplete_value": false,
      "site": "008588b4",
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
            "const:a62:8"
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
      "00858878",
      "DATA",
      [
        "storage",
        "00c03518",
        null,
        "undefined *"
      ]
    ],
    [
      "00858890",
      "DATA",
      [
        "storage",
        "00c02e40",
        null,
        "pointer"
      ]
    ],
    [
      "008588ac",
      "PARAM",
      [
        "storage",
        "002a7a62",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00858878",
      "DATA",
      [
        "storage",
        "00c035c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00858890",
      "DATA",
      [
        "storage",
        "00c02ef0",
        null,
        "pointer"
      ]
    ],
    [
      "008588ac",
      "PARAM",
      [
        "storage",
        "002a79ce",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085886c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858820.md#insn-0085886c) · [`00858888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858820.md#insn-00858888) · [`008588ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858820.md#insn-008588ac)
- 新版 [`0085886c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858820.md#insn-0085886c) · [`00858888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858820.md#insn-00858888) · [`008588ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858820.md#insn-008588ac)

~~~diff
- 0085886c ["COPY", "tmp:0:8", ["const:518:8"]]
- 0085886c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085886c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085886c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085886c ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 0085886c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085886c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085886c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085886c bytes 08611491
+ 0085886c bytes 08211791
- 00858888 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00858888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858888 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 00858888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858888 bytes 08013991
+ 00858888 bytes 08c13b91
- 008588ac ["COPY", "tmp:0:8", ["const:a62:8"]]
- 008588ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008588ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008588ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008588ac ["COPY", "tmp:0:8", ["const:9ce:8"]]
+ 008588ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008588ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008588ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008588ac bytes 21882991
+ 008588ac bytes 21382791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1eb01a11cfc5aed66cbb915275cd43b"></a>

### [`00858918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858918.md) → [`00858918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858918.md) FUN_00858918

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
      "definition_site": "0085893c",
      "incomplete_value": false,
      "site": "0085893c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085893c",
      "incomplete_value": false,
      "site": "0085893c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "0085893c",
      "DATA",
      [
        "storage",
        "00c03568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085893c",
      "DATA",
      [
        "storage",
        "00c03618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858918.md#insn-00858938)
- 新版 [`00858938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858918.md#insn-00858938)

~~~diff
- 00858938 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00858938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858938 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 00858938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858938 bytes 08a11591
+ 00858938 bytes 08611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f911a9f53488d42eb9b20b3ef230e3b"></a>

### [`0085894c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/0085894c.md) → [`0085894c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085894c.md) FUN_0085894c

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
      "definition_site": "00858958",
      "incomplete_value": false,
      "site": "00858958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858958",
      "incomplete_value": false,
      "site": "00858958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "00858958",
      "DATA",
      [
        "storage",
        "00c03568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858958",
      "DATA",
      [
        "storage",
        "00c03618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/0085894c.md#insn-00858954)
- 新版 [`00858954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/0085894c.md#insn-00858954)

~~~diff
- 00858954 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00858954 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00858954 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00858954 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00858954 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 00858954 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00858954 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00858954 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00858954 bytes 29a11591
+ 00858954 bytes 29611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a920aa056c1486b254a624fe49338d2f"></a>

### [`00858a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858a28.md) → [`00858a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858a28.md) FUN_00858a28

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
      "definition_site": "00858a4c",
      "incomplete_value": false,
      "site": "00858a4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858a4c",
      "incomplete_value": false,
      "site": "00858a4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
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
      "00858a4c",
      "DATA",
      [
        "storage",
        "00c035e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858a4c",
      "DATA",
      [
        "storage",
        "00c03698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858a28.md#insn-00858a48)
- 新版 [`00858a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858a28.md#insn-00858a48)

~~~diff
- 00858a48 ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 00858a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858a48 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 00858a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858a48 bytes 08a11791
+ 00858a48 bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ca87bd8a12f4ccfae698c635fe1fec5"></a>

### [`00858a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858a5c.md) → [`00858a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858a5c.md) FUN_00858a5c

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
      "definition_site": "00858a68",
      "incomplete_value": false,
      "site": "00858a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858a68",
      "incomplete_value": false,
      "site": "00858a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
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
      "00858a68",
      "DATA",
      [
        "storage",
        "00c035e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858a68",
      "DATA",
      [
        "storage",
        "00c03698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858a5c.md#insn-00858a64)
- 新版 [`00858a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858a5c.md#insn-00858a64)

~~~diff
- 00858a64 ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 00858a64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00858a64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00858a64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00858a64 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 00858a64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00858a64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00858a64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00858a64 bytes 29a11791
+ 00858a64 bytes 29611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9825b8cab62a4d061ca5ac17826ca0e4"></a>

### [`00858b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858b20.md) → [`00858b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858b20.md) FUN_00858b20

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
      "definition_site": "00858b44",
      "incomplete_value": false,
      "site": "00858b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858b44",
      "incomplete_value": false,
      "site": "00858b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "00858b44",
      "DATA",
      [
        "storage",
        "00c03668",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858b44",
      "DATA",
      [
        "storage",
        "00c03718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858b20.md#insn-00858b40)
- 新版 [`00858b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858b20.md#insn-00858b40)

~~~diff
- 00858b40 ["COPY", "tmp:0:8", ["const:668:8"]]
- 00858b40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858b40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858b40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858b40 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00858b40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858b40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858b40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858b40 bytes 08a11991
+ 00858b40 bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61c435533f5b3f3dfda1c664adf263c1"></a>

### [`00858b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858b54.md) → [`00858b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858b54.md) FUN_00858b54

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
      "definition_site": "00858b60",
      "incomplete_value": false,
      "site": "00858b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858b60",
      "incomplete_value": false,
      "site": "00858b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "00858b60",
      "DATA",
      [
        "storage",
        "00c03668",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858b60",
      "DATA",
      [
        "storage",
        "00c03718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858b54.md#insn-00858b5c)
- 新版 [`00858b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858b54.md#insn-00858b5c)

~~~diff
- 00858b5c ["COPY", "tmp:0:8", ["const:668:8"]]
- 00858b5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00858b5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00858b5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00858b5c ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00858b5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00858b5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00858b5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00858b5c bytes 29a11991
+ 00858b5c bytes 29611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e15b00b929eb9b1a321b8edf49968477"></a>

### [`00858bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858bc4.md) → [`00858bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858bc4.md) FUN_00858bc4

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
      "definition_site": "00858be8",
      "incomplete_value": false,
      "site": "00858be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858be8",
      "incomplete_value": false,
      "site": "00858be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "00858be8",
      "DATA",
      [
        "storage",
        "00c036e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858be8",
      "DATA",
      [
        "storage",
        "00c03798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858be4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858bc4.md#insn-00858be4)
- 新版 [`00858be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858bc4.md#insn-00858be4)

~~~diff
- 00858be4 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 00858be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00858be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00858be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00858be4 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00858be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00858be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00858be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00858be4 bytes 08a11b91
+ 00858be4 bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d875078291b84c334e40ec6d2a7b899"></a>

### [`00858bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858bf8.md) → [`00858bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858bf8.md) FUN_00858bf8

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
      "definition_site": "00858c04",
      "incomplete_value": false,
      "site": "00858c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858c04",
      "incomplete_value": false,
      "site": "00858c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "00858c04",
      "DATA",
      [
        "storage",
        "00c036e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00858c04",
      "DATA",
      [
        "storage",
        "00c03798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00858c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858bf8.md#insn-00858c00)
- 新版 [`00858c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858bf8.md#insn-00858c00)

~~~diff
- 00858c00 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 00858c00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00858c00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00858c00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00858c00 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00858c00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00858c00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00858c00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00858c00 bytes 29a11b91
+ 00858c00 bytes 29611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ad92863578a9c3ab905190d835a4d47"></a>

### [`00858db8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858db8.md) → [`00858db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858db8.md) _INIT_160

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00858fe0",
      "incomplete_value": false,
      "site": "00858fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109e000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00858fe0",
      "incomplete_value": false,
      "site": "00858fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109e000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "definition_site": "00858fe8",
      "incomplete_value": false,
      "site": "00858fec",
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
      "definition_site": "00858fe8",
      "incomplete_value": false,
      "site": "00858fec",
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
      "00858df4",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00858e18",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00858e38",
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
      "00858df4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00858e18",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00858e38",
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

- 旧版 [`00858de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858db8.md#insn-00858de4) · [`00858dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00858/00858db8.md#insn-00858dec)
- 新版 [`00858de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858db8.md#insn-00858de4) · [`00858dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00858/00858db8.md#insn-00858dec)

~~~diff
- 00858de4 ["COPY", "tmp:0:8", ["const:528:8"]]
- 00858de4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00858de4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00858de4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00858de4 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 00858de4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00858de4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00858de4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00858de4 bytes 73a21491
+ 00858de4 bytes 73a21791
- 00858dec ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00858dec bytes 69d2fff0
+ 00858dec ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00858dec bytes 69d2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4df7a97b596db350bc4a283985637720"></a>

### [`00859148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859148.md) → [`00859148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859148.md) FUN_00859148

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`0044fc20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044f/0044fc20.md) [`0044fcd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044f/0044fcd4.md) [`0044fce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044f/0044fce4.md) [`0044fecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044f/0044fecc.md) [`004508a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/004508a4.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0044fc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fc20.md) [`0044fcd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fcd4.md) [`0044fce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fce4.md) [`0044fecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044f/0044fecc.md) [`004508a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/004508a4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00859290",
      "incomplete_value": false,
      "site": "00859298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00859290",
      "incomplete_value": false,
      "site": "00859298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "definition_site": "0085935c",
      "incomplete_value": true,
      "site": "0085935c",
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
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085935c",
      "incomplete_value": true,
      "site": "0085935c",
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
            "const:7b0:8"
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
      "definition_site": "008593a8",
      "incomplete_value": false,
      "site": "008593a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008593a8",
      "incomplete_value": false,
      "site": "008593a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "00859298",
      "DATA",
      [
        "storage",
        "00c038c0",
        null,
        "undefined *"
      ]
    ],
    [
      "008592d0",
      "READ",
      [
        "storage",
        "00c038e0",
        null,
        "pointer"
      ]
    ],
    [
      "008592d0",
      "READ",
      [
        "storage",
        "00c038e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00859298",
      "DATA",
      [
        "storage",
        "00c03970",
        null,
        "undefined *"
      ]
    ],
    [
      "008592d0",
      "READ",
      [
        "storage",
        "00c03990",
        null,
        "pointer"
      ]
    ],
    [
      "008592d0",
      "READ",
      [
        "storage",
        "00c03998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00859290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859148.md#insn-00859290) · [`00859350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859148.md#insn-00859350) · [`008593a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859148.md#insn-008593a4)
- 新版 [`00859290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859148.md#insn-00859290) · [`00859350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859148.md#insn-00859350) · [`008593a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859148.md#insn-008593a4)

~~~diff
- 00859290 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00859290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00859290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00859290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00859290 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00859290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00859290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00859290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00859290 bytes 08012391
+ 00859290 bytes 08c12591
- 00859350 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 00859350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00859350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00859350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00859350 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00859350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00859350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00859350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00859350 bytes 08c11e91
+ 00859350 bytes 08812191
- 008593a4 ["COPY", "tmp:0:8", ["const:840:8"]]
- 008593a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008593a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008593a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008593a4 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 008593a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008593a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008593a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008593a4 bytes 08012191
+ 008593a4 bytes 08c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58eacdbd4a499d38b81d54c19688bde2"></a>

### [`008594d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/008594d4.md) → [`008594d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/008594d4.md) FUN_008594d4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00859148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859148.md) [`0085c4c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c4c4.md) [`0085c698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c698.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00429a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429a14.md) [`00450668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/00450668.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b908.md)
- 新版 呼出元 3件 [`00859148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859148.md) [`0085c4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c4c4.md) [`0085c698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c698.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00429a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429a14.md) [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b908.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00859564",
      "incomplete_value": true,
      "site": "00859570",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:685:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00859564",
      "incomplete_value": true,
      "site": "00859570",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:719:8"
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
      "definition_site": "008595f4",
      "incomplete_value": true,
      "site": "008595f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008595f4",
      "incomplete_value": true,
      "site": "008595f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e67:8"
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
      "definition_site": "008595f8",
      "incomplete_value": true,
      "site": "008595f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008595f8",
      "incomplete_value": true,
      "site": "008595f8",
      "value": [
        "LOAD",
        "8",
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
      "00859518",
      "READ",
      [
        "storage",
        "00c25190",
        null,
        "undefined1"
      ]
    ],
    [
      "00859520",
      "READ",
      [
        "storage",
        "00c25190",
        null,
        "undefined1"
      ]
    ],
    [
      "00859524",
      "READ",
      [
        "storage",
        "00c251a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00859518",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined1"
      ]
    ],
    [
      "00859520",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined1"
      ]
    ],
    [
      "00859524",
      "READ",
      [
        "storage",
        "00c25260",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00859514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/008594d4.md#insn-00859514) · [`0085954c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/008594d4.md#insn-0085954c) · [`00859558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/008594d4.md#insn-00859558)
- 新版 [`00859514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/008594d4.md#insn-00859514) · [`0085954c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/008594d4.md#insn-0085954c) · [`00859558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/008594d4.md#insn-00859558)

~~~diff
- 00859514 ["COPY", "tmp:0:8", ["const:190:8"]]
- 00859514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00859514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00859514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00859514 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 00859514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00859514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00859514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00859514 bytes 08410691
+ 00859514 bytes 08410991
- 0085954c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 0085954c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0085954c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 0085954c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0085954c bytes 08e146f9
+ 0085954c bytes 083947f9
- 00859558 ["COPY", "tmp:0:8", ["const:719:8"]]
- 00859558 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00859558 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00859558 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00859558 ["COPY", "tmp:0:8", ["const:685:8"]]
+ 00859558 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00859558 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00859558 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00859558 bytes 29651c91
+ 00859558 bytes 29151a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52582f60120de96e1ae599bde41500db"></a>

### [`00859898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859898.md) → [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) FUN_00859898

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 93件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bce8.md) [`0041dfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041d/0041dfc0.md)
- 新版 呼出元 0件  · 呼出先 93件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.65% / 新版 98.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00859d38",
      "incomplete_value": false,
      "site": "00859d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00859d38",
      "incomplete_value": false,
      "site": "00859d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00859fe0",
      "incomplete_value": true,
      "site": "00859ff0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00859fe0",
      "incomplete_value": true,
      "site": "00859ff0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d7e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 72,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085b4b0",
      "incomplete_value": true,
      "site": "0085b4c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085b4b0",
      "incomplete_value": true,
      "site": "0085b4c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d7e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 123,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00859910",
      "READ",
      [
        "storage",
        "00295fa7",
        null,
        "string"
      ]
    ],
    [
      "00859c34",
      "PARAM",
      [
        "storage",
        "00292d8f",
        null,
        "string"
      ]
    ],
    [
      "00859d38",
      "DATA",
      [
        "storage",
        "00c039c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00859910",
      "READ",
      [
        "storage",
        "00296034",
        null,
        "string"
      ]
    ],
    [
      "00859c34",
      "PARAM",
      [
        "storage",
        "00292e1c",
        null,
        "string"
      ]
    ],
    [
      "00859d38",
      "DATA",
      [
        "storage",
        "00c03a70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00859904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859898.md#insn-00859904) · [`00859908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859898.md#insn-00859908) · [`00859c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859898.md#insn-00859c34)
- 新版 [`00859904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md#insn-00859904) · [`00859908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md#insn-00859908) · [`00859c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md#insn-00859c34)

~~~diff
- 00859904 ["COPY", "register:4048:8", ["const:295000:8"]]
+ 00859904 ["COPY", "register:4048:8", ["const:296000:8"]]
- 00859904 bytes e9d1ff90
+ 00859904 bytes e9d1ffb0
- 00859908 ["COPY", "tmp:0:8", ["const:fa7:8"]]
- 00859908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00859908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00859908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00859908 ["COPY", "tmp:0:8", ["const:34:8"]]
+ 00859908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00859908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00859908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00859908 bytes 299d3e91
+ 00859908 bytes 29d10091
- 00859c34 ["COPY", "tmp:0:8", ["const:d8f:8"]]
- 00859c34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00859c34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00859c34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00859c34 ["COPY", "tmp:0:8", ["const:e1c:8"]]
+ 00859c34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00859c34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00859c34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00859c34 bytes 213c3691
+ 00859c34 bytes 21703891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-224ce29937d274e32bb9eb8308e2277f"></a>

### [`0085c46c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c46c.md) → [`0085c46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c46c.md) FUN_0085c46c

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
      "definition_site": "0085c48c",
      "incomplete_value": false,
      "site": "0085c490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c48c",
      "incomplete_value": false,
      "site": "0085c490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "0085c490",
      "DATA",
      [
        "storage",
        "00c037b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c490",
      "DATA",
      [
        "storage",
        "00c03860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c48c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c46c.md#insn-0085c48c)
- 新版 [`0085c48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c46c.md#insn-0085c48c)

~~~diff
- 0085c48c ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 0085c48c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085c48c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085c48c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085c48c ["COPY", "tmp:0:8", ["const:860:8"]]
+ 0085c48c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c48c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c48c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085c48c bytes 08c11e91
+ 0085c48c bytes 08812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5e4d9007fd2ab31ad4cab137f013155"></a>

### [`0085c4a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c4a4.md) → [`0085c4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c4a4.md) FUN_0085c4a4

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
      "definition_site": "0085c4a8",
      "incomplete_value": false,
      "site": "0085c4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c4a8",
      "incomplete_value": false,
      "site": "0085c4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "0085c4ac",
      "DATA",
      [
        "storage",
        "00c037b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c4ac",
      "DATA",
      [
        "storage",
        "00c03860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c4a4.md#insn-0085c4a8)
- 新版 [`0085c4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c4a4.md#insn-0085c4a8)

~~~diff
- 0085c4a8 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 0085c4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085c4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085c4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085c4a8 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 0085c4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085c4a8 bytes 08c11e91
+ 0085c4a8 bytes 08812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6579301f868472d8a78b7545165e86b1"></a>

### [`0085c648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c648.md) → [`0085c648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c648.md) FUN_0085c648

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
      "definition_site": "0085c66c",
      "incomplete_value": false,
      "site": "0085c66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c66c",
      "incomplete_value": false,
      "site": "0085c66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "0085c66c",
      "DATA",
      [
        "storage",
        "00c03840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c66c",
      "DATA",
      [
        "storage",
        "00c038f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c648.md#insn-0085c668)
- 新版 [`0085c668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c648.md#insn-0085c668)

~~~diff
- 0085c668 ["COPY", "tmp:0:8", ["const:840:8"]]
- 0085c668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085c668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085c668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085c668 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 0085c668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085c668 bytes 08012191
+ 0085c668 bytes 08c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6908ce5fb7d438d4beb7e5c8686de86a"></a>

### [`0085c67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c67c.md) → [`0085c67c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c67c.md) FUN_0085c67c

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
      "definition_site": "0085c688",
      "incomplete_value": false,
      "site": "0085c688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c688",
      "incomplete_value": false,
      "site": "0085c688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
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
      "0085c688",
      "DATA",
      [
        "storage",
        "00c03840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c688",
      "DATA",
      [
        "storage",
        "00c038f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c67c.md#insn-0085c684)
- 新版 [`0085c684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c67c.md#insn-0085c684)

~~~diff
- 0085c684 ["COPY", "tmp:0:8", ["const:840:8"]]
- 0085c684 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0085c684 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0085c684 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0085c684 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 0085c684 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0085c684 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0085c684 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0085c684 bytes 29012191
+ 0085c684 bytes 29c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c737a723c07c9caa443dc02a580be15"></a>

### [`0085c6c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c6c8.md) → [`0085c6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c6c8.md) FUN_0085c6c8

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
      "definition_site": "0085c6dc",
      "incomplete_value": false,
      "site": "0085c6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c6dc",
      "incomplete_value": false,
      "site": "0085c6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "0085c6e0",
      "DATA",
      [
        "storage",
        "00c038c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c6e0",
      "DATA",
      [
        "storage",
        "00c03970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c6dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c6c8.md#insn-0085c6dc)
- 新版 [`0085c6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c6c8.md#insn-0085c6dc)

~~~diff
- 0085c6dc ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 0085c6dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085c6dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085c6dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085c6dc ["COPY", "tmp:0:8", ["const:970:8"]]
+ 0085c6dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c6dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c6dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085c6dc bytes 08012391
+ 0085c6dc bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59b7b8aaf2a2b81780bb7a447fdc9db8"></a>

### [`0085c6ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c6ec.md) → [`0085c6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c6ec.md) FUN_0085c6ec

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
      "definition_site": "0085c6f0",
      "incomplete_value": false,
      "site": "0085c6f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085c6f0",
      "incomplete_value": false,
      "site": "0085c6f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c03000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "0085c6f4",
      "DATA",
      [
        "storage",
        "00c038c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0085c6f4",
      "DATA",
      [
        "storage",
        "00c03970",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085c6f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0085c/0085c6ec.md#insn-0085c6f0)
- 新版 [`0085c6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c6ec.md#insn-0085c6f0)

~~~diff
- 0085c6f0 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 0085c6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0085c6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0085c6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0085c6f0 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 0085c6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0085c6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0085c6f0 bytes 08012391
+ 0085c6f0 bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

