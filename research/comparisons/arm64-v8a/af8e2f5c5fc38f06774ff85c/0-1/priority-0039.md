# v15.7.2 → v15.7.3 · 最優先の変更候補 (39)

[一覧の目次](README.md)

<a id="compare-5185cc109705a5b8126da2e2e1038677"></a>

### [`00838b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/00838b80.md) → [`00838b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838b80.md) FUN_00838b80

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
      "definition_site": "00838ba4",
      "incomplete_value": false,
      "site": "00838ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:f48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838ba4",
      "incomplete_value": false,
      "site": "00838ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "00838ba4",
      "DATA",
      [
        "storage",
        "00c00e98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00838ba4",
      "DATA",
      [
        "storage",
        "00c00f48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/00838b80.md#insn-00838ba0)
- 新版 `00838ba0`（命令位置の公開資料なし）

~~~diff
- 00838ba0 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 00838ba0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838ba0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838ba0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838ba0 ["COPY", "tmp:0:8", ["const:f48:8"]]
+ 00838ba0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838ba0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838ba0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838ba0 bytes 29613a91
+ 00838ba0 bytes 29213d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c478f70034a1d0f3bd2bb28b3de575be"></a>

### [`00838da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/00838da4.md) → [`00838da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838da4.md) FUN_00838da4

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
      "definition_site": "00838db0",
      "incomplete_value": false,
      "site": "00838db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838db0",
      "incomplete_value": false,
      "site": "00838db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
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
      "00838db4",
      "DATA",
      [
        "storage",
        "00c00f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00838db4",
      "DATA",
      [
        "storage",
        "00c00fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/00838da4.md#insn-00838db0)
- 新版 `00838db0`（命令位置の公開資料なし）

~~~diff
- 00838db0 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 00838db0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838db0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838db0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838db0 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00838db0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838db0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838db0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838db0 bytes 29613c91
+ 00838db0 bytes 29213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bddcb60d0841b9a04bb6d6815fed59b6"></a>

### [`00838dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/00838dc4.md) → [`00838dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838dc4.md) FUN_00838dc4

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
      "definition_site": "00838dcc",
      "incomplete_value": false,
      "site": "00838dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838dcc",
      "incomplete_value": false,
      "site": "00838dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
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
      "00838dd0",
      "DATA",
      [
        "storage",
        "00c00f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00838dd0",
      "DATA",
      [
        "storage",
        "00c00fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/00838dc4.md#insn-00838dcc)
- 新版 `00838dcc`（命令位置の公開資料なし）

~~~diff
- 00838dcc ["COPY", "tmp:0:8", ["const:f18:8"]]
- 00838dcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838dcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838dcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838dcc ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00838dcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838dcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838dcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838dcc bytes 29613c91
+ 00838dcc bytes 29213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7a25dc802c1db181f14068076f609a5"></a>

### [`00838e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/00838e00.md) → [`00838e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838e00.md) FUN_00838e00

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
      "definition_site": "00838e24",
      "incomplete_value": false,
      "site": "00838e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838e24",
      "incomplete_value": false,
      "site": "00838e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
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
      "00838e24",
      "DATA",
      [
        "storage",
        "00c00f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00838e24",
      "DATA",
      [
        "storage",
        "00c00fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/00838e00.md#insn-00838e20)
- 新版 `00838e20`（命令位置の公開資料なし）

~~~diff
- 00838e20 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 00838e20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838e20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838e20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838e20 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00838e20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838e20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838e20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838e20 bytes 29613c91
+ 00838e20 bytes 29213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b987340f87a9a613ce4a6d345ce88b20"></a>

### [`00838e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/00838e50.md) → [`00838e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838e50.md) FUN_00838e50

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
      "definition_site": "00838e5c",
      "incomplete_value": false,
      "site": "00838e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:fc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838e5c",
      "incomplete_value": false,
      "site": "00838e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
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
      "00838e5c",
      "DATA",
      [
        "storage",
        "00c00f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00838e5c",
      "DATA",
      [
        "storage",
        "00c00fc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00838e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/00838e50.md#insn-00838e58)
- 新版 `00838e58`（命令位置の公開資料なし）

~~~diff
- 00838e58 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 00838e58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00838e58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00838e58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00838e58 ["COPY", "tmp:0:8", ["const:fc8:8"]]
+ 00838e58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00838e58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00838e58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00838e58 bytes 29613c91
+ 00838e58 bytes 29213f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c79c4a365759c69537dd87b12caf48e"></a>

### [`00839024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/00839024.md) → [`00839024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839024.md) FUN_00839024

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
      "definition_site": "00839028",
      "incomplete_value": false,
      "site": "0083902c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839028",
      "incomplete_value": false,
      "site": "0083902c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "0083902c",
      "DATA",
      [
        "storage",
        "00c00f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083902c",
      "DATA",
      [
        "storage",
        "00c01048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/00839024.md#insn-00839024) · [`00839028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/00839024.md#insn-00839028)
- 新版 `00839024`（命令位置の公開資料なし） · `00839028`（命令位置の公開資料なし）

~~~diff
- 00839024 ["COPY", "register:4040:8", ["const:c00000:8"]]
+ 00839024 ["COPY", "register:4040:8", ["const:c01000:8"]]
- 00839024 bytes 281e00f0
+ 00839024 bytes 481e0090
- 00839028 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00839028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00839028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00839028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00839028 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00839028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00839028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00839028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00839028 bytes 08613e91
+ 00839028 bytes 08210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d753865d87c1bf0dbca4f2f1dea3946"></a>

### [`00839034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/00839034.md) → [`00839034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839034.md) FUN_00839034

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
      "definition_site": "00839044",
      "incomplete_value": false,
      "site": "0083904c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839044",
      "incomplete_value": false,
      "site": "0083904c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "0083904c",
      "DATA",
      [
        "storage",
        "00c00f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083904c",
      "DATA",
      [
        "storage",
        "00c01048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/00839034.md#insn-00839040) · [`00839044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/00839034.md#insn-00839044)
- 新版 `00839040`（命令位置の公開資料なし） · `00839044`（命令位置の公開資料なし）

~~~diff
- 00839040 ["COPY", "register:4040:8", ["const:c00000:8"]]
+ 00839040 ["COPY", "register:4040:8", ["const:c01000:8"]]
- 00839040 bytes 281e00f0
+ 00839040 bytes 481e0090
- 00839044 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00839044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00839044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00839044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00839044 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00839044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00839044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00839044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00839044 bytes 08613e91
+ 00839044 bytes 08210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6c213effb8d71d233c667c5171c9965"></a>

### [`00839074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/00839074.md) → [`00839074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839074.md) FUN_00839074

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`008216e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00821/008216e4.md) · 呼出先 3件 [`004759a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/004759a4.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`008216e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/008216e4.md) · 呼出先 3件 [`004759a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/004759a4.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

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
      "definition_site": "00839094",
      "incomplete_value": false,
      "site": "00839094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839094",
      "incomplete_value": false,
      "site": "00839094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "00839094",
      "DATA",
      [
        "storage",
        "00c00fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00839094",
      "DATA",
      [
        "storage",
        "00c01098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/00839074.md#insn-00839084) · [`00839088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/00839074.md#insn-00839088)
- 新版 `00839084`（命令位置の公開資料なし） · `00839088`（命令位置の公開資料なし）

~~~diff
- 00839084 ["COPY", "register:4040:8", ["const:c00000:8"]]
+ 00839084 ["COPY", "register:4040:8", ["const:c01000:8"]]
- 00839084 bytes 281e00f0
+ 00839084 bytes 481e0090
- 00839088 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00839088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00839088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00839088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00839088 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00839088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00839088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00839088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00839088 bytes 08a13f91
+ 00839088 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5698dd6c32447f325f34a3698e6222c5"></a>

### [`00839140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/00839140.md) → [`00839140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/00839140.md) FUN_00839140

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00839158",
      "incomplete_value": false,
      "site": "0083915c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839158",
      "incomplete_value": false,
      "site": "0083915c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "0083915c",
      "DATA",
      [
        "storage",
        "00c00fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083915c",
      "DATA",
      [
        "storage",
        "00c01098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/00839140.md#insn-00839154) · [`00839158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/00839140.md#insn-00839158)
- 新版 `00839154`（命令位置の公開資料なし） · `00839158`（命令位置の公開資料なし）

~~~diff
- 00839154 ["COPY", "register:4048:8", ["const:c00000:8"]]
+ 00839154 ["COPY", "register:4048:8", ["const:c01000:8"]]
- 00839154 bytes 291e00f0
+ 00839154 bytes 491e0090
- 00839158 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00839158 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00839158 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00839158 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00839158 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00839158 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00839158 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00839158 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00839158 bytes 29a13f91
+ 00839158 bytes 29610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02da81dabd5afbdaa6c7d242600961e1"></a>

### [`008391ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/008391ec.md) → [`008391ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00839/008391ec.md) FUN_008391ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00839204",
      "incomplete_value": false,
      "site": "00839208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839204",
      "incomplete_value": false,
      "site": "00839208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c00000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "00839208",
      "DATA",
      [
        "storage",
        "00c00fe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00839208",
      "DATA",
      [
        "storage",
        "00c01098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00839200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/008391ec.md#insn-00839200) · [`00839204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00839/008391ec.md#insn-00839204)
- 新版 `00839200`（命令位置の公開資料なし） · `00839204`（命令位置の公開資料なし）

~~~diff
- 00839200 ["COPY", "register:4048:8", ["const:c00000:8"]]
+ 00839200 ["COPY", "register:4048:8", ["const:c01000:8"]]
- 00839200 bytes 291e00f0
+ 00839200 bytes 491e0090
- 00839204 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00839204 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00839204 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00839204 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00839204 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 00839204 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00839204 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00839204 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00839204 bytes 29a13f91
+ 00839204 bytes 29610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b730bca2e0f12bf9131aa3f34bc33d4"></a>

### [`0083a270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083a270.md) → [`0083a270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083a270.md) FUN_0083a270

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ac28.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb460.md)
- 新版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083a2b8",
      "incomplete_value": true,
      "site": "0083a2b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0083a2b8",
      "incomplete_value": true,
      "site": "0083a2b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0083a298",
      "READ",
      [
        "storage",
        "002a8135",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083a298",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083a290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083a270.md#insn-0083a290)
- 新版 `0083a290`（命令位置の公開資料なし）

~~~diff
- 0083a290 ["COPY", "tmp:0:8", ["const:135:8"]]
- 0083a290 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083a290 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083a290 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083a290 ["COPY", "tmp:0:8", ["const:a1:8"]]
+ 0083a290 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083a290 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083a290 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083a290 bytes 4ad50491
+ 0083a290 bytes 4a850291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bd4790612566d4fe6f94c609f97d3cb"></a>

### [`0083a718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083a718.md) → [`0083a718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083a718.md) FUN_0083a718

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ac28.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb460.md)
- 新版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083a760",
      "incomplete_value": true,
      "site": "0083a760",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0083a760",
      "incomplete_value": true,
      "site": "0083a760",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0083a740",
      "READ",
      [
        "storage",
        "002a8135",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083a740",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083a738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083a718.md#insn-0083a738)
- 新版 `0083a738`（命令位置の公開資料なし）

~~~diff
- 0083a738 ["COPY", "tmp:0:8", ["const:135:8"]]
- 0083a738 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083a738 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083a738 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083a738 ["COPY", "tmp:0:8", ["const:a1:8"]]
+ 0083a738 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083a738 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083a738 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083a738 bytes 4ad50491
+ 0083a738 bytes 4a850291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c7eb4a9df4748bec43764b55f3c68c5"></a>

### [`0083a8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083a8a8.md) → [`0083a8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083a8a8.md) FUN_0083a8a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ac28.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb460.md)
- 新版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083a8f0",
      "incomplete_value": true,
      "site": "0083a8f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0083a8f0",
      "incomplete_value": true,
      "site": "0083a8f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0083a8d0",
      "READ",
      [
        "storage",
        "002a8135",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083a8d0",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083a8c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083a8a8.md#insn-0083a8c8)
- 新版 `0083a8c8`（命令位置の公開資料なし）

~~~diff
- 0083a8c8 ["COPY", "tmp:0:8", ["const:135:8"]]
- 0083a8c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083a8c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083a8c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083a8c8 ["COPY", "tmp:0:8", ["const:a1:8"]]
+ 0083a8c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083a8c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083a8c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083a8c8 bytes 4ad50491
+ 0083a8c8 bytes 4a850291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-648c61ef4f15c1b2cf5cbab1946d4ee1"></a>

### [`0083aa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083aa38.md) → [`0083aa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083aa38.md) FUN_0083aa38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0080dd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0080d/0080dd1c.md) [`009dc2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009dc/009dc2c8.md) [`009dc3f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009dc/009dc3f0.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ac28.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb460.md)
- 新版 呼出元 3件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) [`009dc2c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dc2c8.md) [`009dc3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009dc/009dc3f0.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083aa80",
      "incomplete_value": true,
      "site": "0083aa80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0083aa80",
      "incomplete_value": true,
      "site": "0083aa80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0083aa60",
      "READ",
      [
        "storage",
        "002a8135",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083aa60",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083aa58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083aa38.md#insn-0083aa58)
- 新版 `0083aa58`（命令位置の公開資料なし）

~~~diff
- 0083aa58 ["COPY", "tmp:0:8", ["const:135:8"]]
- 0083aa58 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083aa58 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083aa58 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083aa58 ["COPY", "tmp:0:8", ["const:a1:8"]]
+ 0083aa58 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083aa58 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083aa58 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083aa58 bytes 4ad50491
+ 0083aa58 bytes 4a850291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41476f8f6b72fa8aaa732ea93b81fe4a"></a>

### [`0083abc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083abc0.md) → [`0083abc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083abc0.md) FUN_0083abc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ac28.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb460.md)
- 新版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) · 呼出先 6件 [`0044ac28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac28.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083ac08",
      "incomplete_value": true,
      "site": "0083ac08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0083ac08",
      "incomplete_value": true,
      "site": "0083ac08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0083abe8",
      "READ",
      [
        "storage",
        "002a8135",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083abe8",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083abe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083abc0.md#insn-0083abe0)
- 新版 `0083abe0`（命令位置の公開資料なし）

~~~diff
- 0083abe0 ["COPY", "tmp:0:8", ["const:135:8"]]
- 0083abe0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083abe0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083abe0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083abe0 ["COPY", "tmp:0:8", ["const:a1:8"]]
+ 0083abe0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083abe0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083abe0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083abe0 bytes 4ad50491
+ 0083abe0 bytes 4a850291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db41e2d5776dde3530f6006dddceffa6"></a>

### [`0083aed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083aed8.md) → [`0083aed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083aed8.md) FUN_0083aed8

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
      "definition_site": "0083aedc",
      "incomplete_value": false,
      "site": "0083aee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083aedc",
      "incomplete_value": false,
      "site": "0083aee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:48:8"
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
      "0083aee0",
      "DATA",
      [
        "storage",
        "00c01048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083aee0",
      "DATA",
      [
        "storage",
        "00c010f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083aedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083aed8.md#insn-0083aedc)
- 新版 `0083aedc`（命令位置の公開資料なし）

~~~diff
- 0083aedc ["COPY", "tmp:0:8", ["const:48:8"]]
- 0083aedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083aedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083aedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083aedc ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 0083aedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083aedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083aedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083aedc bytes 08210191
+ 0083aedc bytes 08e10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e2958822594364f49f15eedd4ff6b56"></a>

### [`0083aee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083aee8.md) → [`0083aee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083aee8.md) FUN_0083aee8

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
      "definition_site": "0083aef8",
      "incomplete_value": false,
      "site": "0083af00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083aef8",
      "incomplete_value": false,
      "site": "0083af00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:48:8"
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
      "0083af00",
      "DATA",
      [
        "storage",
        "00c01048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083af00",
      "DATA",
      [
        "storage",
        "00c010f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083aef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083aee8.md#insn-0083aef8)
- 新版 `0083aef8`（命令位置の公開資料なし）

~~~diff
- 0083aef8 ["COPY", "tmp:0:8", ["const:48:8"]]
- 0083aef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083aef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083aef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083aef8 ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 0083aef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083aef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083aef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083aef8 bytes 08210191
+ 0083aef8 bytes 08e10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d59de943b8e0e2b2a1bd4c941d8a6c5c"></a>

### [`0083af28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083af28.md) → [`0083af28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083af28.md) FUN_0083af28

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
      "definition_site": "0083af4c",
      "incomplete_value": false,
      "site": "0083af4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083af4c",
      "incomplete_value": false,
      "site": "0083af4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083af4c",
      "DATA",
      [
        "storage",
        "00c01098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083af4c",
      "DATA",
      [
        "storage",
        "00c01148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083af48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083af28.md#insn-0083af48)
- 新版 `0083af48`（命令位置の公開資料なし）

~~~diff
- 0083af48 ["COPY", "tmp:0:8", ["const:98:8"]]
- 0083af48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083af48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083af48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083af48 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 0083af48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083af48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083af48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083af48 bytes 08610291
+ 0083af48 bytes 08210591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a292ca7ff492b46ebb191912d93f9dad"></a>

### [`0083af5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083af5c.md) → [`0083af5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083af5c.md) FUN_0083af5c

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
      "definition_site": "0083af68",
      "incomplete_value": false,
      "site": "0083af68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083af68",
      "incomplete_value": false,
      "site": "0083af68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "0083af68",
      "DATA",
      [
        "storage",
        "00c01098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083af68",
      "DATA",
      [
        "storage",
        "00c01148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083af64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083af5c.md#insn-0083af64)
- 新版 `0083af64`（命令位置の公開資料なし）

~~~diff
- 0083af64 ["COPY", "tmp:0:8", ["const:98:8"]]
- 0083af64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083af64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083af64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083af64 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 0083af64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083af64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083af64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083af64 bytes 29610291
+ 0083af64 bytes 29210591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-176b5dd7b1885d45582fb6b6cebdad36"></a>

### [`0083afec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083afec.md) → [`0083afec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083a/0083afec.md) FUN_0083afec

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
      "definition_site": "0083b010",
      "incomplete_value": false,
      "site": "0083b010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b010",
      "incomplete_value": false,
      "site": "0083b010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "0083b010",
      "DATA",
      [
        "storage",
        "00c01118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b010",
      "DATA",
      [
        "storage",
        "00c011c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b00c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083a/0083afec.md#insn-0083b00c)
- 新版 `0083b00c`（命令位置の公開資料なし）

~~~diff
- 0083b00c ["COPY", "tmp:0:8", ["const:118:8"]]
- 0083b00c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b00c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b00c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b00c ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 0083b00c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b00c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b00c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b00c bytes 08610491
+ 0083b00c bytes 08210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a67ff477e789fdd62b2c957d404b6b6"></a>

### [`0083b020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b020.md) → [`0083b020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b020.md) FUN_0083b020

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
      "definition_site": "0083b02c",
      "incomplete_value": false,
      "site": "0083b02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b02c",
      "incomplete_value": false,
      "site": "0083b02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "0083b02c",
      "DATA",
      [
        "storage",
        "00c01118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b02c",
      "DATA",
      [
        "storage",
        "00c011c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b020.md#insn-0083b028)
- 新版 `0083b028`（命令位置の公開資料なし）

~~~diff
- 0083b028 ["COPY", "tmp:0:8", ["const:118:8"]]
- 0083b028 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b028 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b028 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b028 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 0083b028 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b028 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b028 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b028 bytes 29610491
+ 0083b028 bytes 29210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41eff0ec0d3db7032a17ee72bf5bd909"></a>

### [`0083b0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b0b0.md) → [`0083b0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b0b0.md) FUN_0083b0b0

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
      "definition_site": "0083b0d4",
      "incomplete_value": false,
      "site": "0083b0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b0d4",
      "incomplete_value": false,
      "site": "0083b0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "0083b0d4",
      "DATA",
      [
        "storage",
        "00c01198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b0d4",
      "DATA",
      [
        "storage",
        "00c01248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b0b0.md#insn-0083b0d0)
- 新版 `0083b0d0`（命令位置の公開資料なし）

~~~diff
- 0083b0d0 ["COPY", "tmp:0:8", ["const:198:8"]]
- 0083b0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b0d0 ["COPY", "tmp:0:8", ["const:248:8"]]
+ 0083b0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b0d0 bytes 08610691
+ 0083b0d0 bytes 08210991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a30f18dd9c924ff6d432173223d63f7"></a>

### [`0083b0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b0e4.md) → [`0083b0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b0e4.md) FUN_0083b0e4

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
      "definition_site": "0083b0f0",
      "incomplete_value": false,
      "site": "0083b0f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b0f0",
      "incomplete_value": false,
      "site": "0083b0f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:198:8"
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
      "0083b0f0",
      "DATA",
      [
        "storage",
        "00c01198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b0f0",
      "DATA",
      [
        "storage",
        "00c01248",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b0e4.md#insn-0083b0ec)
- 新版 `0083b0ec`（命令位置の公開資料なし）

~~~diff
- 0083b0ec ["COPY", "tmp:0:8", ["const:198:8"]]
- 0083b0ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b0ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b0ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b0ec ["COPY", "tmp:0:8", ["const:248:8"]]
+ 0083b0ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b0ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b0ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b0ec bytes 29610691
+ 0083b0ec bytes 29210991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2062a7701a944e74d60fb6a40cfddba1"></a>

### [`0083b174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b174.md) → [`0083b174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b174.md) FUN_0083b174

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
      "definition_site": "0083b198",
      "incomplete_value": false,
      "site": "0083b198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b198",
      "incomplete_value": false,
      "site": "0083b198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "0083b198",
      "DATA",
      [
        "storage",
        "00c01218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b198",
      "DATA",
      [
        "storage",
        "00c012c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b174.md#insn-0083b194)
- 新版 `0083b194`（命令位置の公開資料なし）

~~~diff
- 0083b194 ["COPY", "tmp:0:8", ["const:218:8"]]
- 0083b194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b194 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 0083b194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b194 bytes 08610891
+ 0083b194 bytes 08210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e148be6960fd1d6d99d27beb948492f"></a>

### [`0083b1a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b1a8.md) → [`0083b1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b1a8.md) FUN_0083b1a8

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
      "definition_site": "0083b1b4",
      "incomplete_value": false,
      "site": "0083b1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b1b4",
      "incomplete_value": false,
      "site": "0083b1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      "0083b1b4",
      "DATA",
      [
        "storage",
        "00c01218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b1b4",
      "DATA",
      [
        "storage",
        "00c012c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b1a8.md#insn-0083b1b0)
- 新版 `0083b1b0`（命令位置の公開資料なし）

~~~diff
- 0083b1b0 ["COPY", "tmp:0:8", ["const:218:8"]]
- 0083b1b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b1b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b1b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b1b0 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 0083b1b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b1b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b1b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b1b0 bytes 29610891
+ 0083b1b0 bytes 29210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6fb7faefb2e877b357bb2e99f6d7fbb"></a>

### [`0083b238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b238.md) → [`0083b238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b238.md) FUN_0083b238

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
      "definition_site": "0083b25c",
      "incomplete_value": false,
      "site": "0083b25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b25c",
      "incomplete_value": false,
      "site": "0083b25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "0083b25c",
      "DATA",
      [
        "storage",
        "00c01298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b25c",
      "DATA",
      [
        "storage",
        "00c01348",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b238.md#insn-0083b258)
- 新版 `0083b258`（命令位置の公開資料なし）

~~~diff
- 0083b258 ["COPY", "tmp:0:8", ["const:298:8"]]
- 0083b258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b258 ["COPY", "tmp:0:8", ["const:348:8"]]
+ 0083b258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b258 bytes 08610a91
+ 0083b258 bytes 08210d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3f61aa8747437841dfc52f1a68fa81c"></a>

### [`0083b26c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b26c.md) → [`0083b26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b26c.md) FUN_0083b26c

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
      "definition_site": "0083b278",
      "incomplete_value": false,
      "site": "0083b278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b278",
      "incomplete_value": false,
      "site": "0083b278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0083b278",
      "DATA",
      [
        "storage",
        "00c01298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b278",
      "DATA",
      [
        "storage",
        "00c01348",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b26c.md#insn-0083b274)
- 新版 `0083b274`（命令位置の公開資料なし）

~~~diff
- 0083b274 ["COPY", "tmp:0:8", ["const:298:8"]]
- 0083b274 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b274 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b274 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b274 ["COPY", "tmp:0:8", ["const:348:8"]]
+ 0083b274 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b274 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b274 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b274 bytes 29610a91
+ 0083b274 bytes 29210d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bdaff0193b4859d10017481600f64e7"></a>

### [`0083b300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b300.md) → [`0083b300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b300.md) FUN_0083b300

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
      "definition_site": "0083b324",
      "incomplete_value": true,
      "site": "0083b324",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b324",
      "incomplete_value": true,
      "site": "0083b324",
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
            "const:318:8"
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
      "0083b324",
      "DATA",
      [
        "storage",
        "00c01318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b324",
      "DATA",
      [
        "storage",
        "00c013c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b300.md#insn-0083b320)
- 新版 `0083b320`（命令位置の公開資料なし）

~~~diff
- 0083b320 ["COPY", "tmp:0:8", ["const:318:8"]]
- 0083b320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b320 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0083b320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b320 bytes 08610c91
+ 0083b320 bytes 08210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd35fc6f95f5bf4b4475c51df5654927"></a>

### [`0083b334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b334.md) → [`0083b334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b334.md) FUN_0083b334

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
      "definition_site": "0083b340",
      "incomplete_value": false,
      "site": "0083b340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b340",
      "incomplete_value": false,
      "site": "0083b340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "0083b340",
      "DATA",
      [
        "storage",
        "00c01318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b340",
      "DATA",
      [
        "storage",
        "00c013c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b33c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b334.md#insn-0083b33c)
- 新版 `0083b33c`（命令位置の公開資料なし）

~~~diff
- 0083b33c ["COPY", "tmp:0:8", ["const:318:8"]]
- 0083b33c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b33c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b33c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b33c ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 0083b33c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b33c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b33c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b33c bytes 29610c91
+ 0083b33c bytes 29210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77a91afe59d391df2dfdf9ed771b8b82"></a>

### [`0083b3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b3a0.md) → [`0083b3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b3a0.md) FUN_0083b3a0

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
      "definition_site": "0083b3c4",
      "incomplete_value": true,
      "site": "0083b3c4",
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
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b3c4",
      "incomplete_value": true,
      "site": "0083b3c4",
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
            "const:398:8"
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
      "0083b3c4",
      "DATA",
      [
        "storage",
        "00c01398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b3c4",
      "DATA",
      [
        "storage",
        "00c01448",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b3a0.md#insn-0083b3c0)
- 新版 `0083b3c0`（命令位置の公開資料なし）

~~~diff
- 0083b3c0 ["COPY", "tmp:0:8", ["const:398:8"]]
- 0083b3c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b3c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b3c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b3c0 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 0083b3c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b3c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b3c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b3c0 bytes 08610e91
+ 0083b3c0 bytes 08211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa891307a250c64da3e3c5626b6e81a9"></a>

### [`0083b3d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b3d4.md) → [`0083b3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b3d4.md) FUN_0083b3d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083b3e0",
      "incomplete_value": true,
      "site": "0083b3e0",
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
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b3e0",
      "incomplete_value": true,
      "site": "0083b3e0",
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
            "const:398:8"
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
      "0083b3e0",
      "DATA",
      [
        "storage",
        "00c01398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b3e0",
      "DATA",
      [
        "storage",
        "00c01448",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b3dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b3d4.md#insn-0083b3dc)
- 新版 `0083b3dc`（命令位置の公開資料なし）

~~~diff
- 0083b3dc ["COPY", "tmp:0:8", ["const:398:8"]]
- 0083b3dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b3dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b3dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b3dc ["COPY", "tmp:0:8", ["const:448:8"]]
+ 0083b3dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b3dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b3dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b3dc bytes 29610e91
+ 0083b3dc bytes 29211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2342bbc08fc655d4cc7031bfeaa5e4c0"></a>

### [`0083b3f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b3f0.md) → [`0083b3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b3f0.md) FUN_0083b3f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0042c9c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c9c0.md) [`0042ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca08.md) [`00433930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00433/00433930.md) [`004418c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00441/004418c4.md) [`004419a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00441/004419a0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0042c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c9c0.md) [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`00433930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/00433930.md) [`004418c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004418c4.md) [`004419a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004419a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.13% / 新版 97.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083b4f8",
      "incomplete_value": true,
      "site": "0083b508",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e11:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b4f8",
      "incomplete_value": true,
      "site": "0083b508",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ea5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083b5a0",
      "incomplete_value": true,
      "site": "0083b5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b5a0",
      "incomplete_value": true,
      "site": "0083b5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "ordinal": 61,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083b754",
      "incomplete_value": false,
      "site": "0083b758",
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
      "definition_site": "0083b754",
      "incomplete_value": false,
      "site": "0083b758",
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
    "ordinal": 109,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083b4f8",
      "READ",
      [
        "storage",
        "002adea5",
        null,
        "string"
      ]
    ],
    [
      "0083b5a0",
      "DATA",
      [
        "storage",
        "00c01418",
        null,
        "undefined *"
      ]
    ],
    [
      "0083b700",
      "READ",
      [
        "storage",
        "00c01440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b4f8",
      "READ",
      [
        "storage",
        "002ade11",
        null,
        "string"
      ]
    ],
    [
      "0083b5a0",
      "DATA",
      [
        "storage",
        "00c014c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0083b700",
      "READ",
      [
        "storage",
        "00c014f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b4f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b3f0.md#insn-0083b4f0) · [`0083b598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b3f0.md#insn-0083b598) · [`0083b74c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b3f0.md#insn-0083b74c)
- 新版 `0083b4f0`（命令位置の公開資料なし） · `0083b598`（命令位置の公開資料なし） · `0083b74c`（命令位置の公開資料なし）

~~~diff
- 0083b4f0 ["COPY", "tmp:0:8", ["const:ea5:8"]]
- 0083b4f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b4f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b4f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b4f0 ["COPY", "tmp:0:8", ["const:e11:8"]]
+ 0083b4f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b4f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b4f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b4f0 bytes 29953a91
+ 0083b4f0 bytes 29453891
- 0083b598 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0083b598 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083b598 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083b598 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083b598 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0083b598 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083b598 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083b598 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083b598 bytes 4a611091
+ 0083b598 bytes 4a211391
- 0083b74c ["COPY", "tmp:0:8", ["const:470:8"]]
- 0083b74c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083b74c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083b74c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083b74c ["COPY", "tmp:0:8", ["const:520:8"]]
+ 0083b74c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b74c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083b74c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083b74c bytes 08c11191
+ 0083b74c bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1b0649fdfdaf7e6205872babe4421f1"></a>

### [`0083b938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b938.md) → [`0083b938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b938.md) FUN_0083b938

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`004418c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00441/004418c4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004418c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004418c4.md)

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
      "definition_site": "0083b940",
      "incomplete_value": false,
      "site": "0083b944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b940",
      "incomplete_value": false,
      "site": "0083b944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0083b944",
      "DATA",
      [
        "storage",
        "00c01418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b944",
      "DATA",
      [
        "storage",
        "00c014c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b938.md#insn-0083b940)
- 新版 `0083b940`（命令位置の公開資料なし）

~~~diff
- 0083b940 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0083b940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b940 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0083b940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b940 bytes 29611091
+ 0083b940 bytes 29211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f566831fe070c4a6ba16e8165a258616"></a>

### [`0083b958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b958.md) → [`0083b958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b958.md) FUN_0083b958

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`004418c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00441/004418c4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004418c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004418c4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0083b960",
      "incomplete_value": false,
      "site": "0083b964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b960",
      "incomplete_value": false,
      "site": "0083b964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0083b964",
      "DATA",
      [
        "storage",
        "00c01418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b964",
      "DATA",
      [
        "storage",
        "00c014c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b958.md#insn-0083b960)
- 新版 `0083b960`（命令位置の公開資料なし）

~~~diff
- 0083b960 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0083b960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b960 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0083b960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b960 bytes 29611091
+ 0083b960 bytes 29211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26126c8ebbb9ad0c92c110efb1f71017"></a>

### [`0083b994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b994.md) → [`0083b994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083b994.md) FUN_0083b994

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`004419a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00441/004419a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004419a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004419a0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083b9c8",
      "incomplete_value": true,
      "site": "0083b9c8",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083b9c8",
      "incomplete_value": true,
      "site": "0083b9c8",
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
      "0083b9c8",
      "DATA",
      [
        "storage",
        "00c01418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083b9c8",
      "DATA",
      [
        "storage",
        "00c014c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083b9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083b994.md#insn-0083b9b8)
- 新版 `0083b9b8`（命令位置の公開資料なし）

~~~diff
- 0083b9b8 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0083b9b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083b9b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083b9b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083b9b8 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0083b9b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b9b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083b9b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083b9b8 bytes 29611091
+ 0083b9b8 bytes 29211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f479f80496630f9f4bd870e54af3f27"></a>

### [`0083ba24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083ba24.md) → [`0083ba24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083ba24.md) FUN_0083ba24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`004419a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00441/004419a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004419a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00441/004419a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083ba4c",
      "incomplete_value": false,
      "site": "0083ba4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083ba4c",
      "incomplete_value": false,
      "site": "0083ba4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0083ba4c",
      "DATA",
      [
        "storage",
        "00c01418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083ba4c",
      "DATA",
      [
        "storage",
        "00c014c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083ba44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083ba24.md#insn-0083ba44)
- 新版 `0083ba44`（命令位置の公開資料なし）

~~~diff
- 0083ba44 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0083ba44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083ba44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083ba44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083ba44 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0083ba44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083ba44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083ba44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083ba44 bytes 4a611091
+ 0083ba44 bytes 4a211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64ce44abefe3f405627e7c18b02c9851"></a>

### [`0083bb78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083bb78.md) → [`0083bb78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083bb78.md) FUN_0083bb78

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00829340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00829/00829340.md) [`0083bb78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083bb78.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00829340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829340.md) [`0083bb78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083bb78.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.04% / 新版 99.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083bce8",
      "incomplete_value": false,
      "site": "0083bcf0",
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
      "definition_site": "0083bce8",
      "incomplete_value": false,
      "site": "0083bcf0",
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
      "definition_site": "0083bda8",
      "incomplete_value": false,
      "site": "0083bdb0",
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
      "definition_site": "0083bda8",
      "incomplete_value": false,
      "site": "0083bdb0",
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
      "definition_site": "0083c088",
      "incomplete_value": true,
      "site": "0083c098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:672:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083c088",
      "incomplete_value": true,
      "site": "0083c098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
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
      "0083bce8",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0083bda8",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0083c088",
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
      "0083bce8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0083bda8",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0083c088",
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

- 旧版 [`0083bce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083bb78.md#insn-0083bce8) · [`0083bda8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083bb78.md#insn-0083bda8) · [`0083c088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083bb78.md#insn-0083c088)
- 新版 `0083bce8`（命令位置の公開資料なし） · `0083bda8`（命令位置の公開資料なし） · `0083c088`（命令位置の公開資料なし）

~~~diff
- 0083bce8 ["COPY", "tmp:0:8", ["const:311:8"]]
- 0083bce8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083bce8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083bce8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083bce8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0083bce8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083bce8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083bce8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083bce8 bytes 21440c91
+ 0083bce8 bytes 21280c91
- 0083bda8 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0083bda8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083bda8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083bda8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083bda8 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0083bda8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083bda8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083bda8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083bda8 bytes 21d40b91
+ 0083bda8 bytes 21b80b91
- 0083c088 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 0083c088 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 0083c088 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 0083c088 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 0083c088 ["COPY", "tmp:0:8", ["const:672:8"]]
+ 0083c088 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 0083c088 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 0083c088 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 0083c088 bytes 63941791
+ 0083c088 bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a387589fb5be0757b9daaf74e57a3d65"></a>

### [`0083c478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083c/0083c478.md) → [`0083c478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083c478.md) FUN_0083c478

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0083bb78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083b/0083bb78.md) [`0083c478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083c/0083c478.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0083bb78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083b/0083bb78.md) [`0083c478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083c478.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083c5d0",
      "incomplete_value": false,
      "site": "0083c5d8",
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
      "definition_site": "0083c5d0",
      "incomplete_value": false,
      "site": "0083c5d8",
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
      "definition_site": "0083c68c",
      "incomplete_value": false,
      "site": "0083c694",
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
      "definition_site": "0083c68c",
      "incomplete_value": false,
      "site": "0083c694",
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
      "definition_site": "0083cb94",
      "incomplete_value": false,
      "site": "0083cb9c",
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
      "definition_site": "0083cb94",
      "incomplete_value": false,
      "site": "0083cb9c",
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
      "0083c5d0",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0083c68c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0083c9fc",
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
      "0083c5d0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0083c68c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0083c9fc",
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

- 旧版 [`0083c5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083c/0083c478.md#insn-0083c5d0) · [`0083c68c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083c/0083c478.md#insn-0083c68c) · [`0083c9fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083c/0083c478.md#insn-0083c9fc)
- 新版 `0083c5d0`（命令位置の公開資料なし） · `0083c68c`（命令位置の公開資料なし） · `0083c9fc`（命令位置の公開資料なし）

~~~diff
- 0083c5d0 ["COPY", "tmp:0:8", ["const:311:8"]]
- 0083c5d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083c5d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083c5d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083c5d0 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0083c5d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083c5d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083c5d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083c5d0 bytes 21440c91
+ 0083c5d0 bytes 21280c91
- 0083c68c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0083c68c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083c68c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083c68c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083c68c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0083c68c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083c68c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083c68c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083c68c bytes 21d40b91
+ 0083c68c bytes 21b80b91
- 0083c9fc ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 0083c9fc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 0083c9fc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 0083c9fc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 0083c9fc ["COPY", "tmp:0:8", ["const:672:8"]]
+ 0083c9fc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 0083c9fc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 0083c9fc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 0083c9fc bytes 63941791
+ 0083c9fc bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01b7960486522d2c215415e5b5a823bc"></a>

### [`0083cdb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083c/0083cdb0.md) → [`0083cdb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083cdb0.md) FUN_0083cdb0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0083c478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083c/0083c478.md) [`0083cdb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083c/0083cdb0.md) [`008648a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00864/008648a8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`0083c478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083c478.md) [`0083cdb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083c/0083cdb0.md) [`008648a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00864/008648a8.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083cf00",
      "incomplete_value": false,
      "site": "0083cf08",
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
      "definition_site": "0083cf00",
      "incomplete_value": false,
      "site": "0083cf08",
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
      "definition_site": "0083d058",
      "incomplete_value": false,
      "site": "0083d060",
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
      "definition_site": "0083d058",
      "incomplete_value": false,
      "site": "0083d060",
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
      "definition_site": "0083d100",
      "incomplete_value": false,
      "site": "0083d10c",
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
      "definition_site": "0083d100",
      "incomplete_value": false,
      "site": "0083d10c",
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
      "0083cf00",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0083d058",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0083d100",
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
      "0083cf00",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0083d058",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0083d100",
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

- 旧版 [`0083cf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083c/0083cdb0.md#insn-0083cf00) · [`0083d058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083c/0083cdb0.md#insn-0083d058) · [`0083d100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083c/0083cdb0.md#insn-0083d100)
- 新版 `0083cf00`（命令位置の公開資料なし） · `0083d058`（命令位置の公開資料なし） · `0083d100`（命令位置の公開資料なし）

~~~diff
- 0083cf00 ["COPY", "tmp:0:8", ["const:311:8"]]
- 0083cf00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083cf00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083cf00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083cf00 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0083cf00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083cf00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083cf00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083cf00 bytes 21440c91
+ 0083cf00 bytes 21280c91
- 0083d058 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0083d058 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083d058 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083d058 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083d058 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0083d058 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083d058 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083d058 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083d058 bytes 21d40b91
+ 0083d058 bytes 21b80b91
- 0083d100 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0083d100 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0083d100 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0083d100 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0083d100 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0083d100 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0083d100 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0083d100 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0083d100 bytes 21681f91
+ 0083d100 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbdb263867e18a70f90d172db2ecac0e"></a>

### [`0083d5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083d5a0.md) → [`0083d5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5a0.md) FUN_0083d5a0

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
      "definition_site": "0083d5c4",
      "incomplete_value": false,
      "site": "0083d5c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083d5c4",
      "incomplete_value": false,
      "site": "0083d5c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
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
      "0083d5c4",
      "DATA",
      [
        "storage",
        "00c014b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083d5c4",
      "DATA",
      [
        "storage",
        "00c01568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083d5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083d5a0.md#insn-0083d5c0)
- 新版 `0083d5c0`（命令位置の公開資料なし）

~~~diff
- 0083d5c0 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 0083d5c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083d5c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083d5c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083d5c0 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 0083d5c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083d5c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083d5c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083d5c0 bytes 08e11291
+ 0083d5c0 bytes 08a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26712efe0894e499bf7d5cd3ad7370b8"></a>

### [`0083d5d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083d5d4.md) → [`0083d5d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5d4.md) FUN_0083d5d4

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
      "definition_site": "0083d5e0",
      "incomplete_value": false,
      "site": "0083d5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083d5e0",
      "incomplete_value": false,
      "site": "0083d5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
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
      "0083d5e0",
      "DATA",
      [
        "storage",
        "00c014b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083d5e0",
      "DATA",
      [
        "storage",
        "00c01568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083d5dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083d5d4.md#insn-0083d5dc)
- 新版 `0083d5dc`（命令位置の公開資料なし）

~~~diff
- 0083d5dc ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 0083d5dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083d5dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083d5dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083d5dc ["COPY", "tmp:0:8", ["const:568:8"]]
+ 0083d5dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083d5dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083d5dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083d5dc bytes 29e11291
+ 0083d5dc bytes 29a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dfab32d1f7b79847bced2ef4711e889"></a>

### [`0083d5f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083d5f0.md) → [`0083d5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5f0.md) FUN_0083d5f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fff8.md) [`0042aea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042aea8.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`0042aea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042aea8.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.49% / 新版 97.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083d6d0",
      "incomplete_value": true,
      "site": "0083d6e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083d6d0",
      "incomplete_value": true,
      "site": "0083d6e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d39:8"
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
      "definition_site": "0083d7a0",
      "incomplete_value": false,
      "site": "0083d7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083d7a0",
      "incomplete_value": false,
      "site": "0083d7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "0083d6d0",
      "READ",
      [
        "storage",
        "00292d39",
        null,
        "string"
      ]
    ],
    [
      "0083d7a0",
      "DATA",
      [
        "storage",
        "00c01528",
        null,
        "undefined *"
      ]
    ],
    [
      "0083d850",
      "READ",
      [
        "storage",
        "00c01548",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0083d6d0",
      "READ",
      [
        "storage",
        "00292dc6",
        null,
        "string"
      ]
    ],
    [
      "0083d7a0",
      "DATA",
      [
        "storage",
        "00c015d8",
        null,
        "undefined *"
      ]
    ],
    [
      "0083d850",
      "READ",
      [
        "storage",
        "00c015f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083d6c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083d5f0.md#insn-0083d6c8) · [`0083d79c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083d5f0.md#insn-0083d79c)
- 新版 `0083d6c8`（命令位置の公開資料なし） · `0083d79c`（命令位置の公開資料なし）

~~~diff
- 0083d6c8 ["COPY", "tmp:0:8", ["const:d39:8"]]
- 0083d6c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083d6c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083d6c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083d6c8 ["COPY", "tmp:0:8", ["const:dc6:8"]]
+ 0083d6c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083d6c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083d6c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083d6c8 bytes 29e53491
+ 0083d6c8 bytes 29193791
- 0083d79c ["COPY", "tmp:0:8", ["const:528:8"]]
- 0083d79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083d79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083d79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083d79c ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 0083d79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083d79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083d79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083d79c bytes 08a11491
+ 0083d79c bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eb254aa6fb2c4243b34d9cc62c10447"></a>

### [`0083da74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083da74.md) → [`0083da74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083da74.md) FUN_0083da74

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
      "definition_site": "0083da98",
      "incomplete_value": true,
      "site": "0083da98",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083da98",
      "incomplete_value": true,
      "site": "0083da98",
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
            "const:528:8"
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
      "0083da98",
      "DATA",
      [
        "storage",
        "00c01528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083da98",
      "DATA",
      [
        "storage",
        "00c015d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083da94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083da74.md#insn-0083da94)
- 新版 `0083da94`（命令位置の公開資料なし）

~~~diff
- 0083da94 ["COPY", "tmp:0:8", ["const:528:8"]]
- 0083da94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083da94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083da94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083da94 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 0083da94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083da94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083da94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083da94 bytes 08a11491
+ 0083da94 bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25065eec4f6385cdf695c0147360e6de"></a>

### [`0083daa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083daa8.md) → [`0083daa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083daa8.md) FUN_0083daa8

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
      "definition_site": "0083dab4",
      "incomplete_value": false,
      "site": "0083dab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083dab4",
      "incomplete_value": false,
      "site": "0083dab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "0083dab4",
      "DATA",
      [
        "storage",
        "00c01528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083dab4",
      "DATA",
      [
        "storage",
        "00c015d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083dab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083daa8.md#insn-0083dab0)
- 新版 `0083dab0`（命令位置の公開資料なし）

~~~diff
- 0083dab0 ["COPY", "tmp:0:8", ["const:528:8"]]
- 0083dab0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083dab0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083dab0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083dab0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 0083dab0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dab0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dab0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083dab0 bytes 29a11491
+ 0083dab0 bytes 29611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0ba7f4fdcddb483a86a01d42d8dbe1c"></a>

### [`0083db04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083db04.md) → [`0083db04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083db04.md) FUN_0083db04

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
      "definition_site": "0083db08",
      "incomplete_value": false,
      "site": "0083db0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083db08",
      "incomplete_value": false,
      "site": "0083db0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
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
      "0083db0c",
      "DATA",
      [
        "storage",
        "00c015b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0083db0c",
      "DATA",
      [
        "storage",
        "00c01668",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083db08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083db04.md#insn-0083db08)
- 新版 `0083db08`（命令位置の公開資料なし）

~~~diff
- 0083db08 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 0083db08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083db08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083db08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083db08 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 0083db08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083db08 bytes 08e11691
+ 0083db08 bytes 08a11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-937b414758c78988ba93042389be5a94"></a>

### [`0083db14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083db14.md) → [`0083db14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083db14.md) FUN_0083db14

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
      "definition_site": "0083db24",
      "incomplete_value": false,
      "site": "0083db2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083db24",
      "incomplete_value": false,
      "site": "0083db2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:5b8:8"
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
      "0083db2c",
      "DATA",
      [
        "storage",
        "00c015b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0083db2c",
      "DATA",
      [
        "storage",
        "00c01668",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083db24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083db14.md#insn-0083db24)
- 新版 `0083db24`（命令位置の公開資料なし）

~~~diff
- 0083db24 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 0083db24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083db24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083db24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083db24 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 0083db24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083db24 bytes 08e11691
+ 0083db24 bytes 08a11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5089bc2e84b2b7136b2968fbe5e4d3d"></a>

### [`0083db58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083db58.md) → [`0083db58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083db58.md) FUN_0083db58

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
      "definition_site": "0083db78",
      "incomplete_value": false,
      "site": "0083db7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083db78",
      "incomplete_value": false,
      "site": "0083db7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "0083db7c",
      "DATA",
      [
        "storage",
        "00c01608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083db7c",
      "DATA",
      [
        "storage",
        "00c016b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083db78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083db58.md#insn-0083db78)
- 新版 `0083db78`（命令位置の公開資料なし）

~~~diff
- 0083db78 ["COPY", "tmp:0:8", ["const:608:8"]]
- 0083db78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083db78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083db78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083db78 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 0083db78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083db78 bytes 08211891
+ 0083db78 bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ecf913947724cf476a47b8cf900bb3c"></a>

### [`0083db90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083db90.md) → [`0083db90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083db90.md) FUN_0083db90

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
      "definition_site": "0083db94",
      "incomplete_value": false,
      "site": "0083db98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083db94",
      "incomplete_value": false,
      "site": "0083db98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "0083db98",
      "DATA",
      [
        "storage",
        "00c01608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083db98",
      "DATA",
      [
        "storage",
        "00c016b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083db94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083db90.md#insn-0083db94)
- 新版 `0083db94`（命令位置の公開資料なし）

~~~diff
- 0083db94 ["COPY", "tmp:0:8", ["const:608:8"]]
- 0083db94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083db94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083db94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083db94 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 0083db94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083db94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083db94 bytes 08211891
+ 0083db94 bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-131c87464347e7e9fa47cd62299e6fe2"></a>

### [`0083dbdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083dbdc.md) → [`0083dbdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dbdc.md) FUN_0083dbdc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0083dbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083dbb0.md) [`0083df14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083df14.md) · 呼出先 7件 [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0052dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dad8.md) [`0052dae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dae4.md) [`00574ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff0.md) [`00a28744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a28/00a28744.md)
- 新版 呼出元 2件 [`0083dbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dbb0.md) [`0083df14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083df14.md) · 呼出先 7件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0052dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad8.md) [`0052dae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dae4.md) [`00574ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff0.md) [`00a28744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a28/00a28744.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.90% / 新版 95.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083dc8c",
      "incomplete_value": true,
      "site": "0083dc9c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:bb7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083dc8c",
      "incomplete_value": true,
      "site": "0083dc9c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:bb1:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083dbf4",
      "incomplete_value": false,
      "site": "0083dc00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c34000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083dbf4",
      "incomplete_value": false,
      "site": "0083dc00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c34000:8"
          ],
          [
            "leaf",
            "const:340:8"
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
      "0083dbf4",
      "PARAM",
      [
        "storage",
        "00c34340",
        null,
        null
      ]
    ],
    [
      "0083dc18",
      "READ",
      [
        "storage",
        "002a6cc3",
        null,
        "string"
      ]
    ],
    [
      "0083dc8c",
      "READ",
      [
        "storage",
        "002aabb1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083dbf4",
      "PARAM",
      [
        "storage",
        "00c34400",
        null,
        null
      ]
    ],
    [
      "0083dc18",
      "READ",
      [
        "storage",
        "002a6cbc",
        null,
        "string"
      ]
    ],
    [
      "0083dc8c",
      "READ",
      [
        "storage",
        "002aabb7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083dbf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083dbdc.md#insn-0083dbf4) · [`0083dc10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083dbdc.md#insn-0083dc10) · [`0083dc84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083dbdc.md#insn-0083dc84)
- 新版 `0083dbf4`（命令位置の公開資料なし） · `0083dc10`（命令位置の公開資料なし） · `0083dc84`（命令位置の公開資料なし）

~~~diff
- 0083dbf4 ["COPY", "tmp:0:8", ["const:340:8"]]
- 0083dbf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0083dbf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0083dbf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0083dbf4 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 0083dbf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0083dbf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0083dbf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0083dbf4 bytes 00000d91
+ 0083dbf4 bytes 00001091
- 0083dc10 ["COPY", "tmp:0:8", ["const:cc3:8"]]
- 0083dc10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083dc10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083dc10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083dc10 ["COPY", "tmp:0:8", ["const:cbc:8"]]
+ 0083dc10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dc10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dc10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083dc10 bytes 290d3391
+ 0083dc10 bytes 29f13291
- 0083dc84 ["COPY", "tmp:0:8", ["const:bb1:8"]]
- 0083dc84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083dc84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083dc84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083dc84 ["COPY", "tmp:0:8", ["const:bb7:8"]]
+ 0083dc84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dc84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dc84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083dc84 bytes 29c52e91
+ 0083dc84 bytes 29dd2e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3962259a397e6a043f00fc242a9adfca"></a>

### [`0083debc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083debc.md) → [`0083debc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083debc.md) FUN_0083debc

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
      "definition_site": "0083dedc",
      "incomplete_value": false,
      "site": "0083dee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083dedc",
      "incomplete_value": false,
      "site": "0083dee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0083dee0",
      "DATA",
      [
        "storage",
        "00c01688",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083dee0",
      "DATA",
      [
        "storage",
        "00c01738",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083dedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083debc.md#insn-0083dedc)
- 新版 `0083dedc`（命令位置の公開資料なし）

~~~diff
- 0083dedc ["COPY", "tmp:0:8", ["const:688:8"]]
- 0083dedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083dedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083dedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083dedc ["COPY", "tmp:0:8", ["const:738:8"]]
+ 0083dedc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083dedc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083dedc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083dedc bytes 08211a91
+ 0083dedc bytes 08e11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd83ea617714ee63c6dcb5a03d11de1c"></a>

### [`0083df44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083df44.md) → [`0083df44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083df44.md) FUN_0083df44

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
      "definition_site": "0083df64",
      "incomplete_value": false,
      "site": "0083df68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083df64",
      "incomplete_value": false,
      "site": "0083df68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:708:8"
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
      "0083df68",
      "DATA",
      [
        "storage",
        "00c01708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083df68",
      "DATA",
      [
        "storage",
        "00c017b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083df64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083df44.md#insn-0083df64)
- 新版 `0083df64`（命令位置の公開資料なし）

~~~diff
- 0083df64 ["COPY", "tmp:0:8", ["const:708:8"]]
- 0083df64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083df64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083df64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083df64 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 0083df64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083df64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083df64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083df64 bytes 08211c91
+ 0083df64 bytes 08e11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-348ff6722378b6dd0156ba80cd59ccb3"></a>

### [`0083df7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083df7c.md) → [`0083df7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083df7c.md) FUN_0083df7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083df80",
      "incomplete_value": true,
      "site": "0083df84",
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
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083df80",
      "incomplete_value": true,
      "site": "0083df84",
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
            "const:708:8"
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
      "0083df84",
      "DATA",
      [
        "storage",
        "00c01708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083df84",
      "DATA",
      [
        "storage",
        "00c017b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083df80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083df7c.md#insn-0083df80)
- 新版 `0083df80`（命令位置の公開資料なし）

~~~diff
- 0083df80 ["COPY", "tmp:0:8", ["const:708:8"]]
- 0083df80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083df80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083df80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083df80 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 0083df80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083df80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083df80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083df80 bytes 08211c91
+ 0083df80 bytes 08e11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ea8329fe01e4d71542093e38d2ee252"></a>

### [`0083dfc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083dfc8.md) → [`0083dfc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083dfc8.md) FUN_0083dfc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0083df9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083df9c.md) [`0083e950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083e/0083e950.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469fac.md) [`0052dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dad8.md)
- 新版 呼出元 2件 [`0083df9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083df9c.md) [`0083e950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083e/0083e950.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`0052dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad8.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083e168",
      "incomplete_value": true,
      "site": "0083e168",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:99b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083e168",
      "incomplete_value": true,
      "site": "0083e168",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a2f:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0083e23c",
      "incomplete_value": true,
      "site": "0083e23c",
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
      "definition_site": "0083e23c",
      "incomplete_value": true,
      "site": "0083e23c",
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
    "ordinal": 15,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0083dff8",
      "READ",
      [
        "storage",
        "0029e9f2",
        null,
        "string"
      ]
    ],
    [
      "0083dffc",
      "READ",
      [
        "storage",
        "0029e9f9",
        null,
        "string"
      ]
    ],
    [
      "0083e11c",
      "READ",
      [
        "storage",
        "002a1a42",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083dff8",
      "READ",
      [
        "storage",
        "0029ea7f",
        null,
        "string"
      ]
    ],
    [
      "0083dffc",
      "READ",
      [
        "storage",
        "0029ea86",
        null,
        "string"
      ]
    ],
    [
      "0083e11c",
      "READ",
      [
        "storage",
        "002a1acf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083dff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083dfc8.md#insn-0083dff0) · [`0083e114`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083dfc8.md#insn-0083e114) · [`0083e150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083dfc8.md#insn-0083e150)
- 新版 `0083dff0`（命令位置の公開資料なし） · `0083e114`（命令位置の公開資料なし） · `0083e150`（命令位置の公開資料なし）

~~~diff
- 0083dff0 ["COPY", "tmp:0:8", ["const:9f2:8"]]
- 0083dff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083dff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083dff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083dff0 ["COPY", "tmp:0:8", ["const:a7f:8"]]
+ 0083dff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083dff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083dff0 bytes 29c92791
+ 0083dff0 bytes 29fd2991
- 0083e114 ["COPY", "tmp:0:8", ["const:a42:8"]]
- 0083e114 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083e114 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083e114 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083e114 ["COPY", "tmp:0:8", ["const:acf:8"]]
+ 0083e114 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083e114 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083e114 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083e114 bytes 29092991
+ 0083e114 bytes 293d2b91
- 0083e150 ["COPY", "tmp:0:8", ["const:a2f:8"]]
- 0083e150 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083e150 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083e150 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083e150 ["COPY", "tmp:0:8", ["const:99b:8"]]
+ 0083e150 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083e150 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083e150 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083e150 bytes 29bd2891
+ 0083e150 bytes 296d2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-816bcea8e5a8eb3fa0c51fbda78bb1c9"></a>

### [`0083e8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083e/0083e8f8.md) → [`0083e8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083e/0083e8f8.md) FUN_0083e8f8

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
      "definition_site": "0083e918",
      "incomplete_value": false,
      "site": "0083e91c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083e918",
      "incomplete_value": false,
      "site": "0083e91c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "0083e91c",
      "DATA",
      [
        "storage",
        "00c01788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083e91c",
      "DATA",
      [
        "storage",
        "00c01838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083e918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083e/0083e8f8.md#insn-0083e918)
- 新版 `0083e918`（命令位置の公開資料なし）

~~~diff
- 0083e918 ["COPY", "tmp:0:8", ["const:788:8"]]
- 0083e918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083e918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083e918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083e918 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 0083e918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083e918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083e918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083e918 bytes 08211e91
+ 0083e918 bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fba7fec7fd9fe14af9aa51f6b7d5fb61"></a>

### [`0083e930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083e/0083e930.md) → [`0083e930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083e/0083e930.md) FUN_0083e930

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
      "definition_site": "0083e934",
      "incomplete_value": false,
      "site": "0083e938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083e934",
      "incomplete_value": false,
      "site": "0083e938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "0083e938",
      "DATA",
      [
        "storage",
        "00c01788",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083e938",
      "DATA",
      [
        "storage",
        "00c01838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083e934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083e/0083e930.md#insn-0083e934)
- 新版 `0083e934`（命令位置の公開資料なし）

~~~diff
- 0083e934 ["COPY", "tmp:0:8", ["const:788:8"]]
- 0083e934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083e934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083e934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083e934 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 0083e934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083e934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083e934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083e934 bytes 08211e91
+ 0083e934 bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a62f7b1a3e96628ce04ae610a6373557"></a>

### [`0083e97c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083e/0083e97c.md) → [`0083e97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083e/0083e97c.md) FUN_0083e97c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0082b53c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0082b/0082b53c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0082b53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082b/0082b53c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0083e988",
      "incomplete_value": false,
      "site": "0083e98c",
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
      "definition_site": "0083e988",
      "incomplete_value": false,
      "site": "0083e98c",
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
      "0083e988",
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
      "0083e988",
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

- 旧版 [`0083e988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083e/0083e97c.md#insn-0083e988)
- 新版 `0083e988`（命令位置の公開資料なし）

~~~diff
- 0083e988 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0083e988 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0083e988 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0083e988 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0083e988 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0083e988 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0083e988 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0083e988 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0083e988 bytes 00280c91
+ 0083e988 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab5419740e458e01372f8cb4c3ff7dd2"></a>

### [`0083f60c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083f60c.md) → [`0083f60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f60c.md) FUN_0083f60c

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
      "definition_site": "0083f630",
      "incomplete_value": false,
      "site": "0083f630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f630",
      "incomplete_value": false,
      "site": "0083f630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
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
      "0083f630",
      "DATA",
      [
        "storage",
        "00c01808",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083f630",
      "DATA",
      [
        "storage",
        "00c018b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083f62c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083f60c.md#insn-0083f62c)
- 新版 `0083f62c`（命令位置の公開資料なし）

~~~diff
- 0083f62c ["COPY", "tmp:0:8", ["const:808:8"]]
- 0083f62c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083f62c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083f62c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083f62c ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 0083f62c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083f62c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083f62c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083f62c bytes 08212091
+ 0083f62c bytes 08e12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e24d7b4ea8613eabf9c150613ccceb9"></a>

### [`0083f65c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083f65c.md) → [`0083f65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f65c.md) FUN_0083f65c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0082b53c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0082b/0082b53c.md) · 呼出先 10件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`007cd120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cd/007cd120.md) [`007cea80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ce/007cea80.md) [`007ceacc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ce/007ceacc.md) [`007d22d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007d2/007d22d4.md)
- 新版 呼出元 1件 [`0082b53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0082b/0082b53c.md) · 呼出先 10件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`007cd120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd120.md) [`007cea80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ce/007cea80.md) [`007ceacc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ce/007ceacc.md) [`007d22d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007d2/007d22d4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.97% / 新版 98.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0083f7d8",
      "incomplete_value": false,
      "site": "0083f7dc",
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
            "const:5cf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f7d8",
      "incomplete_value": false,
      "site": "0083f7dc",
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
            "const:5d6:8"
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
      "0083f7d8",
      "PARAM",
      [
        "storage",
        "002a35d6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0083f7d8",
      "PARAM",
      [
        "storage",
        "002a35cf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083f7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083f65c.md#insn-0083f7d8)
- 新版 `0083f7d8`（命令位置の公開資料なし）

~~~diff
- 0083f7d8 ["COPY", "tmp:0:8", ["const:5d6:8"]]
- 0083f7d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0083f7d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0083f7d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0083f7d8 ["COPY", "tmp:0:8", ["const:5cf:8"]]
+ 0083f7d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0083f7d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0083f7d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0083f7d8 bytes 00581791
+ 0083f7d8 bytes 003c1791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0b4c0cca94a4f3e27957ba1407518ad"></a>

### [`0083f810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083f810.md) → [`0083f810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f810.md) FUN_0083f810

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
      "definition_site": "0083f834",
      "incomplete_value": false,
      "site": "0083f834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f834",
      "incomplete_value": false,
      "site": "0083f834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "0083f834",
      "DATA",
      [
        "storage",
        "00c01898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083f834",
      "DATA",
      [
        "storage",
        "00c01948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083f830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083f810.md#insn-0083f830)
- 新版 `0083f830`（命令位置の公開資料なし）

~~~diff
- 0083f830 ["COPY", "tmp:0:8", ["const:898:8"]]
- 0083f830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083f830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083f830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083f830 ["COPY", "tmp:0:8", ["const:948:8"]]
+ 0083f830 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083f830 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083f830 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083f830 bytes 08612291
+ 0083f830 bytes 08212591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f5e1fba11e715d34dd1a2533924cb19"></a>

### [`0083f844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083f844.md) → [`0083f844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083f844.md) FUN_0083f844

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083f850",
      "incomplete_value": true,
      "site": "0083f850",
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
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f850",
      "incomplete_value": true,
      "site": "0083f850",
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
            "const:898:8"
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
      "0083f850",
      "DATA",
      [
        "storage",
        "00c01898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083f850",
      "DATA",
      [
        "storage",
        "00c01948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083f84c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083f844.md#insn-0083f84c)
- 新版 `0083f84c`（命令位置の公開資料なし）

~~~diff
- 0083f84c ["COPY", "tmp:0:8", ["const:898:8"]]
- 0083f84c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083f84c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083f84c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083f84c ["COPY", "tmp:0:8", ["const:948:8"]]
+ 0083f84c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083f84c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083f84c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083f84c bytes 29612291
+ 0083f84c bytes 29212591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa1adabc4bda142c52cb19fc5b05e97f"></a>

### [`0083fb9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fb9c.md) → [`0083fb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fb9c.md) FUN_0083fb9c

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
      "definition_site": "0083fba4",
      "incomplete_value": false,
      "site": "0083fba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fba4",
      "incomplete_value": false,
      "site": "0083fba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "0083fba8",
      "DATA",
      [
        "storage",
        "00c01928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fba8",
      "DATA",
      [
        "storage",
        "00c019d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fb9c.md#insn-0083fba4)
- 新版 `0083fba4`（命令位置の公開資料なし）

~~~diff
- 0083fba4 ["COPY", "tmp:0:8", ["const:928:8"]]
- 0083fba4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083fba4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083fba4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083fba4 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 0083fba4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fba4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fba4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083fba4 bytes 29a12491
+ 0083fba4 bytes 29612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a970d23fcf490ea9751301b325f28ae2"></a>

### [`0083fbbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fbbc.md) → [`0083fbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fbbc.md) FUN_0083fbbc

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
      "definition_site": "0083fbc4",
      "incomplete_value": false,
      "site": "0083fbc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fbc4",
      "incomplete_value": false,
      "site": "0083fbc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "0083fbc8",
      "DATA",
      [
        "storage",
        "00c01928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fbc8",
      "DATA",
      [
        "storage",
        "00c019d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fbc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fbbc.md#insn-0083fbc4)
- 新版 `0083fbc4`（命令位置の公開資料なし）

~~~diff
- 0083fbc4 ["COPY", "tmp:0:8", ["const:928:8"]]
- 0083fbc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083fbc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083fbc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083fbc4 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 0083fbc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fbc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fbc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083fbc4 bytes 29a12491
+ 0083fbc4 bytes 29612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc3693314c516ca3e6885d8297431394"></a>

### [`0083fbfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fbfc.md) → [`0083fbfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fbfc.md) FUN_0083fbfc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083fc28",
      "incomplete_value": false,
      "site": "0083fc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fc28",
      "incomplete_value": false,
      "site": "0083fc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "0083fc28",
      "DATA",
      [
        "storage",
        "00c01928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fc28",
      "DATA",
      [
        "storage",
        "00c019d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fc20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fbfc.md#insn-0083fc20)
- 新版 `0083fc20`（命令位置の公開資料なし）

~~~diff
- 0083fc20 ["COPY", "tmp:0:8", ["const:928:8"]]
- 0083fc20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083fc20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083fc20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083fc20 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 0083fc20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083fc20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083fc20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083fc20 bytes 4aa12491
+ 0083fc20 bytes 4a612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99f4bc7e6bcc1ab4f01afe001f52169a"></a>

### [`0083fc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fc70.md) → [`0083fc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fc70.md) FUN_0083fc70

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

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
      "definition_site": "0083fc78",
      "incomplete_value": false,
      "site": "0083fc78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fc78",
      "incomplete_value": false,
      "site": "0083fc78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "0083fc78",
      "DATA",
      [
        "storage",
        "00c01928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fc78",
      "DATA",
      [
        "storage",
        "00c019d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fc74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fc70.md#insn-0083fc74)
- 新版 `0083fc74`（命令位置の公開資料なし）

~~~diff
- 0083fc74 ["COPY", "tmp:0:8", ["const:928:8"]]
- 0083fc74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083fc74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083fc74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083fc74 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 0083fc74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083fc74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083fc74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083fc74 bytes 08a12491
+ 0083fc74 bytes 08612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1550efa69bfe1ad501b8bf27efc77b16"></a>

### [`0083fdcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fdcc.md) → [`0083fdcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fdcc.md) FUN_0083fdcc

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
      "definition_site": "0083fdd4",
      "incomplete_value": false,
      "site": "0083fdd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fdd4",
      "incomplete_value": false,
      "site": "0083fdd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "0083fdd8",
      "DATA",
      [
        "storage",
        "00c019a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fdd8",
      "DATA",
      [
        "storage",
        "00c01a58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fdd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fdcc.md#insn-0083fdd4)
- 新版 `0083fdd4`（命令位置の公開資料なし）

~~~diff
- 0083fdd4 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 0083fdd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083fdd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083fdd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083fdd4 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 0083fdd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fdd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fdd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083fdd4 bytes 29a12691
+ 0083fdd4 bytes 29612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6edd5250795c1af2f3b56172eea7b67"></a>

### [`0083fdec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fdec.md) → [`0083fdec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fdec.md) FUN_0083fdec

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
      "definition_site": "0083fdf4",
      "incomplete_value": false,
      "site": "0083fdf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fdf4",
      "incomplete_value": false,
      "site": "0083fdf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "0083fdf8",
      "DATA",
      [
        "storage",
        "00c019a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fdf8",
      "DATA",
      [
        "storage",
        "00c01a58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fdf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fdec.md#insn-0083fdf4)
- 新版 `0083fdf4`（命令位置の公開資料なし）

~~~diff
- 0083fdf4 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 0083fdf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083fdf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0083fdf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0083fdf4 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 0083fdf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fdf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083fdf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0083fdf4 bytes 29a12691
+ 0083fdf4 bytes 29612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca7033d5f937da514267dcaf55509362"></a>

### [`0083fe2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fe2c.md) → [`0083fe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fe2c.md) FUN_0083fe2c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083fe58",
      "incomplete_value": false,
      "site": "0083fe58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fe58",
      "incomplete_value": false,
      "site": "0083fe58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "0083fe58",
      "DATA",
      [
        "storage",
        "00c019a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fe58",
      "DATA",
      [
        "storage",
        "00c01a58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fe50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fe2c.md#insn-0083fe50)
- 新版 `0083fe50`（命令位置の公開資料なし）

~~~diff
- 0083fe50 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 0083fe50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0083fe50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0083fe50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0083fe50 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 0083fe50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0083fe50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0083fe50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0083fe50 bytes 4aa12691
+ 0083fe50 bytes 4a612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-331318a715cbee181821673b109c0842"></a>

### [`0083fea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fea0.md) → [`0083fea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fea0.md) FUN_0083fea0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

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
      "definition_site": "0083fea8",
      "incomplete_value": false,
      "site": "0083fea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083fea8",
      "incomplete_value": false,
      "site": "0083fea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "0083fea8",
      "DATA",
      [
        "storage",
        "00c019a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0083fea8",
      "DATA",
      [
        "storage",
        "00c01a58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0083fea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fea0.md#insn-0083fea4)
- 新版 `0083fea4`（命令位置の公開資料なし）

~~~diff
- 0083fea4 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 0083fea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083fea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0083fea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0083fea4 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 0083fea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083fea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083fea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0083fea4 bytes 08a12691
+ 0083fea4 bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d32d500a339a11897a1f776f46572c36"></a>

### [`0083fffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fffc.md) → [`0083fffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fffc.md) FUN_0083fffc

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
      "definition_site": "00840000",
      "incomplete_value": false,
      "site": "00840004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840000",
      "incomplete_value": false,
      "site": "00840004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "00840004",
      "DATA",
      [
        "storage",
        "00c01a40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00840004",
      "DATA",
      [
        "storage",
        "00c01af0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fffc.md#insn-00840000)
- 新版 `00840000`（命令位置の公開資料なし）

~~~diff
- 00840000 ["COPY", "tmp:0:8", ["const:a40:8"]]
- 00840000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00840000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00840000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00840000 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00840000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00840000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00840000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00840000 bytes 08012991
+ 00840000 bytes 08c12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89add7ec4bf9cf061819ba4be452f05a"></a>

### [`0084000c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/0084000c.md) → [`0084000c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/0084000c.md) FUN_0084000c

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
      "definition_site": "0084001c",
      "incomplete_value": false,
      "site": "00840024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084001c",
      "incomplete_value": false,
      "site": "00840024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      "00840024",
      "DATA",
      [
        "storage",
        "00c01a40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00840024",
      "DATA",
      [
        "storage",
        "00c01af0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084001c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/0084000c.md#insn-0084001c)
- 新版 `0084001c`（命令位置の公開資料なし）

~~~diff
- 0084001c ["COPY", "tmp:0:8", ["const:a40:8"]]
- 0084001c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084001c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084001c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084001c ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 0084001c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084001c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084001c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084001c bytes 08012991
+ 0084001c bytes 08c12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b494443987793f6e0e76acf92a7d7d4"></a>

### [`0084004c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/0084004c.md) → [`0084004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/0084004c.md) FUN_0084004c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00829478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00829/00829478.md) · 呼出先 6件 [`004215a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/004215a0.md) [`00421b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421b40.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00829478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md) · 呼出先 6件 [`004215a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md) [`00421b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421b40.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "0084008c",
      "incomplete_value": false,
      "site": "0084008c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084008c",
      "incomplete_value": false,
      "site": "0084008c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "0084008c",
      "DATA",
      [
        "storage",
        "00c01a90",
        null,
        "undefined *"
      ]
    ],
    [
      "00840104",
      "READ",
      [
        "storage",
        "002980f7",
        null,
        "string"
      ]
    ],
    [
      "00840108",
      "READ",
      [
        "storage",
        "002980fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0084008c",
      "DATA",
      [
        "storage",
        "00c01b40",
        null,
        "undefined *"
      ]
    ],
    [
      "00840104",
      "READ",
      [
        "storage",
        "00298184",
        null,
        "string"
      ]
    ],
    [
      "00840108",
      "READ",
      [
        "storage",
        "0029818b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/0084004c.md#insn-00840088) · [`008400d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/0084004c.md#insn-008400d4) · [`008400dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/0084004c.md#insn-008400dc)
- 新版 `00840088`（命令位置の公開資料なし） · `008400d4`（命令位置の公開資料なし） · `008400dc`（命令位置の公開資料なし）

~~~diff
- 00840088 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00840088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00840088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00840088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00840088 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 00840088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00840088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00840088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00840088 bytes 08412a91
+ 00840088 bytes 08012d91
- 008400d4 ["COPY", "tmp:0:8", ["const:f7:8"]]
- 008400d4 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 008400d4 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 008400d4 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 008400d4 ["COPY", "tmp:0:8", ["const:184:8"]]
+ 008400d4 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 008400d4 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 008400d4 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 008400d4 bytes 9cdf0391
+ 008400d4 bytes 9c130691
- 008400dc ["COPY", "tmp:0:8", ["const:57c:8"]]
- 008400dc ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 008400dc ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 008400dc ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 008400dc ["COPY", "tmp:0:8", ["const:62c:8"]]
+ 008400dc ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 008400dc ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 008400dc ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 008400dc bytes f7f21591
+ 008400dc bytes f7b21891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b31dc36bf6897f9d44a59695dd80ccdb"></a>

### [`00840274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840274.md) → [`00840274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840274.md) FUN_00840274

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008406c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/008406c0.md) · 呼出先 5件 [`004618e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00461/004618e8.md) [`00470ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470ac0.md) [`0081fa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081fa64.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`008406c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/008406c0.md) · 呼出先 5件 [`004618e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00461/004618e8.md) [`00470ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470ac0.md) [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.82% / 新版 87.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008402d8",
      "incomplete_value": false,
      "site": "008402e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109c000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008402d8",
      "incomplete_value": false,
      "site": "008402e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109c000:8"
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
      "definition_site": "008402e8",
      "incomplete_value": false,
      "site": "008402f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109d000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008402e8",
      "incomplete_value": false,
      "site": "008402f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109d000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "definition_site": "00840310",
      "incomplete_value": false,
      "site": "00840318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109c000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840310",
      "incomplete_value": false,
      "site": "00840318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109c000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "008402b4",
      "DATA",
      [
        "storage",
        "00c01a90",
        null,
        "undefined *"
      ]
    ],
    [
      "008402bc",
      "READ",
      [
        "storage",
        "00f5c758",
        null,
        "undefined1"
      ]
    ],
    [
      "008402cc",
      "READ",
      [
        "storage",
        "00fec1b3",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "008402b4",
      "DATA",
      [
        "storage",
        "00c01b40",
        null,
        "undefined *"
      ]
    ],
    [
      "008402bc",
      "READ",
      [
        "storage",
        "00f5c818",
        null,
        "undefined1"
      ]
    ],
    [
      "008402cc",
      "READ",
      [
        "storage",
        "00fec273",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840274.md#insn-00840298) · [`008402a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840274.md#insn-008402a4) · [`008402d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840274.md#insn-008402d8)
- 新版 `00840298`（命令位置の公開資料なし） · `008402a4`（命令位置の公開資料なし） · `008402d8`（命令位置の公開資料なし）

~~~diff
- 00840298 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00840298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00840298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00840298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00840298 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 00840298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00840298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00840298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00840298 bytes 29412a91
+ 00840298 bytes 29012d91
- 008402a4 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 008402a4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 008402a4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 008402a4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 008402a4 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 008402a4 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 008402a4 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 008402a4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 008402a4 bytes 94c20391
+ 008402a4 bytes 94c20691
- 008402d8 ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 008402d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008402d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008402d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008402d8 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 008402d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008402d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008402d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008402d8 bytes 00a01691
+ 008402d8 bytes 00a01991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54317660f6f7ff1385c1f70a64121c30"></a>

### [`008406e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/008406e4.md) → [`008406e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/008406e4.md) FUN_008406e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 17件 [`004215a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/004215a0.md) [`004222e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004215a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md) [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.24% / 新版 91.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0084071c",
      "incomplete_value": false,
      "site": "00840720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c28000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084071c",
      "incomplete_value": false,
      "site": "00840720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c28000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      "definition_site": "00840838",
      "incomplete_value": false,
      "site": "00840850",
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
      "definition_site": "00840838",
      "incomplete_value": false,
      "site": "00840850",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00840934",
      "incomplete_value": true,
      "site": "00840938",
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
      "definition_site": "00840934",
      "incomplete_value": true,
      "site": "00840938",
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
      "0084071c",
      "PARAM",
      [
        "storage",
        "00c280f0",
        null,
        null
      ]
    ],
    [
      "00840790",
      "READ",
      [
        "storage",
        "00298107",
        null,
        "string"
      ]
    ],
    [
      "00840794",
      "READ",
      [
        "storage",
        "00c1ada0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0084071c",
      "PARAM",
      [
        "storage",
        "00c281b0",
        null,
        null
      ]
    ],
    [
      "00840790",
      "READ",
      [
        "storage",
        "00298194",
        null,
        "string"
      ]
    ],
    [
      "00840794",
      "READ",
      [
        "storage",
        "00c1ae50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084071c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/008406e4.md#insn-0084071c) · [`00840760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/008406e4.md#insn-00840760) · [`0084078c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/008406e4.md#insn-0084078c)
- 新版 `0084071c`（命令位置の公開資料なし） · `00840760`（命令位置の公開資料なし） · `0084078c`（命令位置の公開資料なし）

~~~diff
- 0084071c ["COPY", "tmp:0:8", ["const:f0:8"]]
- 0084071c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0084071c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0084071c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0084071c ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 0084071c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0084071c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0084071c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0084071c bytes 00c00391
+ 0084071c bytes 00c00691
- 00840760 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00840760 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00840760 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00840760 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00840760 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 00840760 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00840760 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00840760 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00840760 bytes 39c30391
+ 00840760 bytes 39c30691
- 0084078c ["COPY", "tmp:0:8", ["const:107:8"]]
- 0084078c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084078c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084078c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084078c ["COPY", "tmp:0:8", ["const:194:8"]]
+ 0084078c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084078c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084078c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084078c bytes 081d0491
+ 0084078c bytes 08510691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6193c667af0515f658548d5f36a5c214"></a>

### [`00840d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840d1c.md) → [`00840d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d1c.md) FUN_00840d1c

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
      "definition_site": "00840d20",
      "incomplete_value": false,
      "site": "00840d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840d20",
      "incomplete_value": false,
      "site": "00840d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "00840d24",
      "DATA",
      [
        "storage",
        "00c01ad8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00840d24",
      "DATA",
      [
        "storage",
        "00c01b88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840d1c.md#insn-00840d20)
- 新版 `00840d20`（命令位置の公開資料なし）

~~~diff
- 00840d20 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 00840d20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00840d20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00840d20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00840d20 ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 00840d20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00840d20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00840d20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00840d20 bytes 08612b91
+ 00840d20 bytes 08212e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-131f4347d7ff6f72cc3ebbd76c494bbe"></a>

### [`00840d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840d2c.md) → [`00840d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d2c.md) FUN_00840d2c

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
      "definition_site": "00840d3c",
      "incomplete_value": false,
      "site": "00840d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840d3c",
      "incomplete_value": false,
      "site": "00840d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "00840d44",
      "DATA",
      [
        "storage",
        "00c01ad8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00840d44",
      "DATA",
      [
        "storage",
        "00c01b88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00840d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840d2c.md#insn-00840d3c)
- 新版 `00840d3c`（命令位置の公開資料なし）

~~~diff
- 00840d3c ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 00840d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00840d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00840d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00840d3c ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 00840d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00840d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00840d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00840d3c bytes 08612b91
+ 00840d3c bytes 08212e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56176c7370ca5d76efe889ca8da1b736"></a>

### [`00840d6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840d6c.md) → [`00840d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840d6c.md) FUN_00840d6c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00829478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00829/00829478.md) [`008443c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00844/008443c8.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff0.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 2件 [`00829478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md) [`008443c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008443c8.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.87% / 新版 90.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00840db0",
      "incomplete_value": false,
      "site": "00840db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840db0",
      "incomplete_value": false,
      "site": "00840db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b28:8"
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
      "definition_site": "00840e18",
      "incomplete_value": true,
      "site": "00840e18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00840e18",
      "incomplete_value": true,
      "site": "00840e18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00840e4c",
      "incomplete_value": true,
      "site": "00840e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00840e4c",
      "incomplete_value": true,
      "site": "00840e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:f40:8"
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
      "00840db0",
      "DATA",
      [
        "storage",
        "00c01b28",
        null,
        "undefined *"
      ]
    ],
    [
      "00840de4",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00840e04",
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
      "00840db0",
      "DATA",
      [
        "storage",
        "00c01bd8",
        null,
        "undefined *"
      ]
    ],
    [
      "00840de4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00840e04",
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

- 旧版 [`00840dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840d6c.md#insn-00840dac) · [`00840ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840d6c.md#insn-00840ddc) · [`00840de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840d6c.md#insn-00840de0)
- 新版 `00840dac`（命令位置の公開資料なし） · `00840ddc`（命令位置の公開資料なし） · `00840de0`（命令位置の公開資料なし）

~~~diff
- 00840dac ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00840dac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00840dac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00840dac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00840dac ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 00840dac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00840dac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00840dac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00840dac bytes 08a12c91
+ 00840dac bytes 08612f91
- 00840ddc ["COPY", "register:40d0:8", ["const:c24000:8"]]
+ 00840ddc ["COPY", "register:40d0:8", ["const:c25000:8"]]
- 00840ddc bytes 3a1f0090
+ 00840ddc bytes 3a1f00b0
- 00840de0 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00840de0 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 00840de0 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 00840de0 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 00840de0 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00840de0 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 00840de0 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 00840de0 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 00840de0 bytes 5ae33d91
+ 00840de0 bytes 5ae30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b6cc3edbcb958b90798384a6fa1431e"></a>

### [`00841168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841168.md) → [`00841168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841168.md) FUN_00841168

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00841180",
      "incomplete_value": false,
      "site": "00841184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841180",
      "incomplete_value": false,
      "site": "00841184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b28:8"
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
      "00841184",
      "DATA",
      [
        "storage",
        "00c01b28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00841184",
      "DATA",
      [
        "storage",
        "00c01bd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841168.md#insn-00841180)
- 新版 `00841180`（命令位置の公開資料なし）

~~~diff
- 00841180 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00841180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00841180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00841180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00841180 ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 00841180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00841180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00841180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00841180 bytes 29a12c91
+ 00841180 bytes 29612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de071f5e163a108cb8ee886103e42c84"></a>

### [`00841214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841214.md) → [`00841214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841214.md) FUN_00841214

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0084122c",
      "incomplete_value": false,
      "site": "00841230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084122c",
      "incomplete_value": false,
      "site": "00841230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b28:8"
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
      "00841230",
      "DATA",
      [
        "storage",
        "00c01b28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00841230",
      "DATA",
      [
        "storage",
        "00c01bd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084122c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841214.md#insn-0084122c)
- 新版 `0084122c`（命令位置の公開資料なし）

~~~diff
- 0084122c ["COPY", "tmp:0:8", ["const:b28:8"]]
- 0084122c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084122c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084122c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084122c ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 0084122c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084122c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084122c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084122c bytes 29a12c91
+ 0084122c bytes 29612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6453a1a21836f7e1a562c0ef4fa82099"></a>

### [`008412b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/008412b0.md) → [`008412b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/008412b0.md) FUN_008412b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fff8.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0053dc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053dc30.md) [`0073ab94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073ab94.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0053dc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dc30.md) [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.46% / 新版 96.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00841304",
      "incomplete_value": true,
      "site": "00841314",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:272:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841304",
      "incomplete_value": true,
      "site": "00841314",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:279:8"
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
      "definition_site": "008413d4",
      "incomplete_value": true,
      "site": "008413d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9c5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008413d4",
      "incomplete_value": true,
      "site": "008413d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:938:8"
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
      "definition_site": "008413d8",
      "incomplete_value": true,
      "site": "008413d8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008413d8",
      "incomplete_value": true,
      "site": "008413d8",
      "value": [
        "LOAD",
        "8",
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
      "00841304",
      "READ",
      [
        "storage",
        "002a4279",
        null,
        "string"
      ]
    ],
    [
      "008413c4",
      "READ",
      [
        "storage",
        "0029b938",
        null,
        "string"
      ]
    ],
    [
      "008413c8",
      "READ",
      [
        "storage",
        "0029b93e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00841304",
      "READ",
      [
        "storage",
        "002a4272",
        null,
        "string"
      ]
    ],
    [
      "008413c4",
      "READ",
      [
        "storage",
        "0029b9c5",
        null,
        "string"
      ]
    ],
    [
      "008413c8",
      "READ",
      [
        "storage",
        "0029b9cb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008412fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/008412b0.md#insn-008412fc) · [`008413bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/008412b0.md#insn-008413bc)
- 新版 `008412fc`（命令位置の公開資料なし） · `008413bc`（命令位置の公開資料なし）

~~~diff
- 008412fc ["COPY", "tmp:0:8", ["const:279:8"]]
- 008412fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008412fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008412fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008412fc ["COPY", "tmp:0:8", ["const:272:8"]]
+ 008412fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008412fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008412fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008412fc bytes 08e50991
+ 008412fc bytes 08c90991
- 008413bc ["COPY", "tmp:0:8", ["const:938:8"]]
- 008413bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008413bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008413bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008413bc ["COPY", "tmp:0:8", ["const:9c5:8"]]
+ 008413bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008413bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008413bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008413bc bytes 29e12491
+ 008413bc bytes 29152791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c42dcf476b0b58b94781198045374425"></a>

### [`0084177c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/0084177c.md) → [`0084177c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/0084177c.md) FUN_0084177c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008412b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/008412b0.md) [`008427a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008427a8.md) · 呼出先 9件 [`0042ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca08.md) [`0042ca70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca70.md) [`0084224c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/0084224c.md) [`0084229c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/0084229c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 2件 [`008412b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/008412b0.md) [`008427a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008427a8.md) · 呼出先 9件 [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`0042ca70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca70.md) [`0084224c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/0084224c.md) [`0084229c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/0084229c.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.06% / 新版 95.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008417e4",
      "incomplete_value": false,
      "site": "008417e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008417e4",
      "incomplete_value": false,
      "site": "008417e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "definition_site": "00841804",
      "incomplete_value": false,
      "site": "00841804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841804",
      "incomplete_value": false,
      "site": "00841804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "008417e4",
      "DATA",
      [
        "storage",
        "00c01b88",
        null,
        "undefined *"
      ]
    ],
    [
      "00841804",
      "DATA",
      [
        "storage",
        "00c01b88",
        null,
        "undefined *"
      ]
    ],
    [
      "00841844",
      "READ",
      [
        "storage",
        "00c01ba8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008417e4",
      "DATA",
      [
        "storage",
        "00c01c38",
        null,
        "undefined *"
      ]
    ],
    [
      "00841804",
      "DATA",
      [
        "storage",
        "00c01c38",
        null,
        "undefined *"
      ]
    ],
    [
      "00841844",
      "READ",
      [
        "storage",
        "00c01c58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008417d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/0084177c.md#insn-008417d4) · [`008417fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/0084177c.md#insn-008417fc)
- 新版 `008417d4`（命令位置の公開資料なし） · `008417fc`（命令位置の公開資料なし）

~~~diff
- 008417d4 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 008417d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008417d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008417d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008417d4 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 008417d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008417d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008417d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008417d4 bytes 08212e91
+ 008417d4 bytes 08e13091
- 008417fc ["COPY", "tmp:0:8", ["const:b88:8"]]
- 008417fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008417fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008417fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008417fc ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 008417fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008417fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008417fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008417fc bytes 08212e91
+ 008417fc bytes 08e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-521e03b6b7379095fb3d5c1e590c6663"></a>

### [`00841924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841924.md) → [`00841924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841924.md) FUN_00841924

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008412b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/008412b0.md) [`008423bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008423bc.md) · 呼出先 7件 [`0084297c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/0084297c.md) [`008429cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008429cc.md) [`0084d6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084d/0084d6d0.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 2件 [`008412b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/008412b0.md) [`008423bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008423bc.md) · 呼出先 7件 [`0084297c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/0084297c.md) [`008429cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008429cc.md) [`0084d6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d6d0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00841984",
      "incomplete_value": false,
      "site": "00841984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841984",
      "incomplete_value": false,
      "site": "00841984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "definition_site": "008419a4",
      "incomplete_value": false,
      "site": "008419a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008419a4",
      "incomplete_value": false,
      "site": "008419a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "00841984",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ],
    [
      "008419a4",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ],
    [
      "008419e8",
      "READ",
      [
        "storage",
        "00c01ca8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00841984",
      "DATA",
      [
        "storage",
        "00c01d38",
        null,
        "undefined *"
      ]
    ],
    [
      "008419a4",
      "DATA",
      [
        "storage",
        "00c01d38",
        null,
        "undefined *"
      ]
    ],
    [
      "008419e8",
      "READ",
      [
        "storage",
        "00c01d58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841924.md#insn-00841974) · [`0084199c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841924.md#insn-0084199c)
- 新版 `00841974`（命令位置の公開資料なし） · `0084199c`（命令位置の公開資料なし）

~~~diff
- 00841974 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00841974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00841974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00841974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00841974 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00841974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00841974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00841974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00841974 bytes 08213291
+ 00841974 bytes 08e13491
- 0084199c ["COPY", "tmp:0:8", ["const:c88:8"]]
- 0084199c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084199c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084199c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084199c ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 0084199c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084199c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084199c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084199c bytes 08213291
+ 0084199c bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69fae3da641b160714497f09c7b75cd5"></a>

### [`00841a9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841a9c.md) → [`00841a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841a9c.md) FUN_00841a9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008412b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/008412b0.md) · 呼出先 7件 [`00842db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842db4.md) [`00842e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842e04.md) [`0084dd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084d/0084dd1c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`008412b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/008412b0.md) · 呼出先 7件 [`00842db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842db4.md) [`00842e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842e04.md) [`0084dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084dd1c.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00841afc",
      "incomplete_value": false,
      "site": "00841afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841afc",
      "incomplete_value": false,
      "site": "00841afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "definition_site": "00841b1c",
      "incomplete_value": false,
      "site": "00841b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841b1c",
      "incomplete_value": false,
      "site": "00841b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "00841afc",
      "DATA",
      [
        "storage",
        "00c01d08",
        null,
        "undefined *"
      ]
    ],
    [
      "00841b1c",
      "DATA",
      [
        "storage",
        "00c01d08",
        null,
        "undefined *"
      ]
    ],
    [
      "00841b60",
      "READ",
      [
        "storage",
        "00c01d28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00841afc",
      "DATA",
      [
        "storage",
        "00c01db8",
        null,
        "undefined *"
      ]
    ],
    [
      "00841b1c",
      "DATA",
      [
        "storage",
        "00c01db8",
        null,
        "undefined *"
      ]
    ],
    [
      "00841b60",
      "READ",
      [
        "storage",
        "00c01dd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841a9c.md#insn-00841aec) · [`00841b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841a9c.md#insn-00841b14)
- 新版 `00841aec`（命令位置の公開資料なし） · `00841b14`（命令位置の公開資料なし）

~~~diff
- 00841aec ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00841aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00841aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00841aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00841aec ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00841aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00841aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00841aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00841aec bytes 08213491
+ 00841aec bytes 08e13691
- 00841b14 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00841b14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00841b14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00841b14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00841b14 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00841b14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00841b14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00841b14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00841b14 bytes 08213491
+ 00841b14 bytes 08e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78fde83d5dd9d7c25d8978b809fa5934"></a>

### [`00841c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841c14.md) → [`00841c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841c14.md) FUN_00841c14

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`008412b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/008412b0.md) [`00842a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842a50.md) [`00842e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842e88.md) [`00843d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00843/00843d2c.md) · 呼出先 16件 [`0042ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042ca08.md) [`00430dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430dd8.md) [`0073a038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073ab94.md) [`008430b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00843/008430b0.md)
- 新版 呼出元 4件 [`008412b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/008412b0.md) [`00842a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842a50.md) [`00842e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842e88.md) [`00843d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/00843d2c.md) · 呼出先 16件 [`0042ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca08.md) [`00430dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430dd8.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md) [`008430b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00843/008430b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00841c70",
      "incomplete_value": true,
      "site": "00841c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841c70",
      "incomplete_value": true,
      "site": "00841c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:113:8"
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
      "definition_site": "00841c78",
      "incomplete_value": true,
      "site": "00841c78",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00841c78",
      "incomplete_value": true,
      "site": "00841c78",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00841cbc",
      "incomplete_value": true,
      "site": "00841ccc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00841cbc",
      "incomplete_value": true,
      "site": "00841ccc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d92:8"
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
      "00841c64",
      "READ",
      [
        "storage",
        "00298113",
        null,
        "string"
      ]
    ],
    [
      "00841c68",
      "READ",
      [
        "storage",
        "00298118",
        null,
        "string"
      ]
    ],
    [
      "00841cbc",
      "READ",
      [
        "storage",
        "00293d92",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00841c64",
      "READ",
      [
        "storage",
        "002981a0",
        null,
        "string"
      ]
    ],
    [
      "00841c68",
      "READ",
      [
        "storage",
        "002981a5",
        null,
        "string"
      ]
    ],
    [
      "00841cbc",
      "READ",
      [
        "storage",
        "00293e1f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00841c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841c14.md#insn-00841c5c) · [`00841cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841c14.md#insn-00841cb4) · [`00841d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841c14.md#insn-00841d04)
- 新版 `00841c5c`（命令位置の公開資料なし） · `00841cb4`（命令位置の公開資料なし） · `00841d04`（命令位置の公開資料なし）

~~~diff
- 00841c5c ["COPY", "tmp:0:8", ["const:113:8"]]
- 00841c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00841c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00841c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00841c5c ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 00841c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00841c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00841c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00841c5c bytes 084d0491
+ 00841c5c bytes 08810691
- 00841cb4 ["COPY", "tmp:0:8", ["const:d92:8"]]
- 00841cb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00841cb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00841cb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00841cb4 ["COPY", "tmp:0:8", ["const:e1f:8"]]
+ 00841cb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00841cb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00841cb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00841cb4 bytes 29493691
+ 00841cb4 bytes 297d3891
- 00841d04 ["COPY", "tmp:0:8", ["const:f12:8"]]
- 00841d04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00841d04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00841d04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00841d04 ["COPY", "tmp:0:8", ["const:f9f:8"]]
+ 00841d04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00841d04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00841d04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00841d04 bytes 29493c91
+ 00841d04 bytes 297d3e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fa5d443ec59c55c815e3ca1aa463434"></a>

### [`00842100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842100.md) → [`00842100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842100.md) FUN_00842100

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
      "definition_site": "00842114",
      "incomplete_value": false,
      "site": "00842118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842114",
      "incomplete_value": false,
      "site": "00842118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "00842118",
      "DATA",
      [
        "storage",
        "00c01b88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842118",
      "DATA",
      [
        "storage",
        "00c01c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842114`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842100.md#insn-00842114)
- 新版 `00842114`（命令位置の公開資料なし）

~~~diff
- 00842114 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00842114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842114 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00842114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842114 bytes 08212e91
+ 00842114 bytes 08e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3ae4cac7a51036b9f5e0ed76c56ebf3"></a>

### [`0084215c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/0084215c.md) → [`0084215c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/0084215c.md) FUN_0084215c

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
      "definition_site": "00842174",
      "incomplete_value": false,
      "site": "00842178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842174",
      "incomplete_value": false,
      "site": "00842178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "00842178",
      "DATA",
      [
        "storage",
        "00c01b88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842178",
      "DATA",
      [
        "storage",
        "00c01c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/0084215c.md#insn-00842174)
- 新版 `00842174`（命令位置の公開資料なし）

~~~diff
- 00842174 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00842174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842174 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00842174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842174 bytes 08212e91
+ 00842174 bytes 08e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f8a475366d4f0e4b1aede463f59fb1a"></a>

### [`008421b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008421b8.md) → [`008421b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008421b8.md) FUN_008421b8

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
      "definition_site": "008421dc",
      "incomplete_value": false,
      "site": "008421e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008421dc",
      "incomplete_value": false,
      "site": "008421e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "008421e0",
      "DATA",
      [
        "storage",
        "00c01b88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008421e0",
      "DATA",
      [
        "storage",
        "00c01c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008421dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008421b8.md#insn-008421dc)
- 新版 `008421dc`（命令位置の公開資料なし）

~~~diff
- 008421dc ["COPY", "tmp:0:8", ["const:b88:8"]]
- 008421dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008421dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008421dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008421dc ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 008421dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008421dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008421dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008421dc bytes 29212e91
+ 008421dc bytes 29e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbf7126839f5d0d38bcc2ca208b3c559"></a>

### [`00842210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842210.md) → [`00842210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842210.md) FUN_00842210

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
      "definition_site": "00842218",
      "incomplete_value": false,
      "site": "0084221c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842218",
      "incomplete_value": false,
      "site": "0084221c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "0084221c",
      "DATA",
      [
        "storage",
        "00c01b88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084221c",
      "DATA",
      [
        "storage",
        "00c01c38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842210.md#insn-00842218)
- 新版 `00842218`（命令位置の公開資料なし）

~~~diff
- 00842218 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00842218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00842218 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00842218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00842218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00842218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842218 bytes 29212e91
+ 00842218 bytes 29e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c46cf4a46e7f31214e72fc1b77bd345"></a>

### [`008423bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008423bc.md) → [`008423bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008423bc.md) FUN_008423bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008422ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008422ec.md) · 呼出先 7件 [`00841924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841924.md) [`00842708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842708.md) [`00842758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842758.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`008422ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008422ec.md) · 呼出先 7件 [`00841924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841924.md) [`00842708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842708.md) [`00842758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842758.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00842458",
      "incomplete_value": false,
      "site": "00842458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842458",
      "incomplete_value": false,
      "site": "00842458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "definition_site": "00842474",
      "incomplete_value": false,
      "site": "00842474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842474",
      "incomplete_value": false,
      "site": "00842474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "00842458",
      "DATA",
      [
        "storage",
        "00c01bf8",
        null,
        "undefined *"
      ]
    ],
    [
      "00842474",
      "DATA",
      [
        "storage",
        "00c01bf8",
        null,
        "undefined *"
      ]
    ],
    [
      "008424bc",
      "READ",
      [
        "storage",
        "00c01c18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00842458",
      "DATA",
      [
        "storage",
        "00c01ca8",
        null,
        "undefined *"
      ]
    ],
    [
      "00842474",
      "DATA",
      [
        "storage",
        "00c01ca8",
        null,
        "undefined *"
      ]
    ],
    [
      "008424bc",
      "READ",
      [
        "storage",
        "00c01cc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008423bc.md#insn-00842448) · [`0084246c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008423bc.md#insn-0084246c)
- 新版 `00842448`（命令位置の公開資料なし） · `0084246c`（命令位置の公開資料なし）

~~~diff
- 00842448 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00842448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842448 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00842448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842448 bytes 08e12f91
+ 00842448 bytes 08a13291
- 0084246c ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 0084246c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084246c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084246c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0084246c ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 0084246c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0084246c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0084246c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084246c bytes 08e12f91
+ 0084246c bytes 08a13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ab464313da2bc5d61eaecab29575e97"></a>

### [`008425bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008425bc.md) → [`008425bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008425bc.md) FUN_008425bc

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
      "definition_site": "008425d0",
      "incomplete_value": false,
      "site": "008425d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008425d0",
      "incomplete_value": false,
      "site": "008425d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "008425d4",
      "DATA",
      [
        "storage",
        "00c01bf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008425d4",
      "DATA",
      [
        "storage",
        "00c01ca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008425d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008425bc.md#insn-008425d0)
- 新版 `008425d0`（命令位置の公開資料なし）

~~~diff
- 008425d0 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 008425d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008425d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008425d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008425d0 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 008425d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008425d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008425d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008425d0 bytes 08e12f91
+ 008425d0 bytes 08a13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76919cac6e731b7f72a76de22a70a9dc"></a>

### [`00842618`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842618.md) → [`00842618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842618.md) FUN_00842618

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
      "definition_site": "00842630",
      "incomplete_value": false,
      "site": "00842634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842630",
      "incomplete_value": false,
      "site": "00842634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "00842634",
      "DATA",
      [
        "storage",
        "00c01bf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842634",
      "DATA",
      [
        "storage",
        "00c01ca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842618.md#insn-00842630)
- 新版 `00842630`（命令位置の公開資料なし）

~~~diff
- 00842630 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00842630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842630 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00842630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842630 bytes 08e12f91
+ 00842630 bytes 08a13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cddc710dc4246108270cf90b4897ef4c"></a>

### [`00842674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842674.md) → [`00842674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842674.md) FUN_00842674

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
      "definition_site": "00842698",
      "incomplete_value": false,
      "site": "0084269c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842698",
      "incomplete_value": false,
      "site": "0084269c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "0084269c",
      "DATA",
      [
        "storage",
        "00c01bf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084269c",
      "DATA",
      [
        "storage",
        "00c01ca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842674.md#insn-00842698)
- 新版 `00842698`（命令位置の公開資料なし）

~~~diff
- 00842698 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00842698 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842698 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842698 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00842698 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00842698 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00842698 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00842698 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842698 bytes 29e12f91
+ 00842698 bytes 29a13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04a2396134a08113f66cfe1df1577b3b"></a>

### [`008426cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008426cc.md) → [`008426cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008426cc.md) FUN_008426cc

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
      "definition_site": "008426d4",
      "incomplete_value": false,
      "site": "008426d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008426d4",
      "incomplete_value": false,
      "site": "008426d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "008426d8",
      "DATA",
      [
        "storage",
        "00c01bf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008426d8",
      "DATA",
      [
        "storage",
        "00c01ca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008426d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008426cc.md#insn-008426d4)
- 新版 `008426d4`（命令位置の公開資料なし）

~~~diff
- 008426d4 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 008426d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008426d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008426d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008426d4 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 008426d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008426d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008426d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008426d4 bytes 29e12f91
+ 008426d4 bytes 29a13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-671fca5533c93403b84d288ee5c9742b"></a>

### [`00842830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842830.md) → [`00842830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842830.md) FUN_00842830

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
      "definition_site": "00842844",
      "incomplete_value": false,
      "site": "00842848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842844",
      "incomplete_value": false,
      "site": "00842848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "00842848",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842848",
      "DATA",
      [
        "storage",
        "00c01d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842830.md#insn-00842844)
- 新版 `00842844`（命令位置の公開資料なし）

~~~diff
- 00842844 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00842844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842844 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00842844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842844 bytes 08213291
+ 00842844 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38ac761a89bac4159b16aa181096299a"></a>

### [`0084288c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/0084288c.md) → [`0084288c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/0084288c.md) FUN_0084288c

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
      "definition_site": "008428a4",
      "incomplete_value": false,
      "site": "008428a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008428a4",
      "incomplete_value": false,
      "site": "008428a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "008428a8",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008428a8",
      "DATA",
      [
        "storage",
        "00c01d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008428a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/0084288c.md#insn-008428a4)
- 新版 `008428a4`（命令位置の公開資料なし）

~~~diff
- 008428a4 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 008428a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008428a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008428a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008428a4 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 008428a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008428a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008428a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008428a4 bytes 08213291
+ 008428a4 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a81a399f53cbef60dc0a3ff947d5f55f"></a>

### [`008428e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008428e8.md) → [`008428e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/008428e8.md) FUN_008428e8

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
      "definition_site": "0084290c",
      "incomplete_value": false,
      "site": "00842910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084290c",
      "incomplete_value": false,
      "site": "00842910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "00842910",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842910",
      "DATA",
      [
        "storage",
        "00c01d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084290c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/008428e8.md#insn-0084290c)
- 新版 `0084290c`（命令位置の公開資料なし）

~~~diff
- 0084290c ["COPY", "tmp:0:8", ["const:c88:8"]]
- 0084290c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084290c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084290c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0084290c ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 0084290c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0084290c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0084290c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084290c bytes 29213291
+ 0084290c bytes 29e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8af859267f0b0ceb9c2643d74b6f39ac"></a>

### [`00842940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842940.md) → [`00842940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842940.md) FUN_00842940

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
      "definition_site": "00842948",
      "incomplete_value": false,
      "site": "0084294c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842948",
      "incomplete_value": false,
      "site": "0084294c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "0084294c",
      "DATA",
      [
        "storage",
        "00c01c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0084294c",
      "DATA",
      [
        "storage",
        "00c01d38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842940.md#insn-00842948)
- 新版 `00842948`（命令位置の公開資料なし）

~~~diff
- 00842948 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00842948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00842948 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00842948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00842948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00842948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842948 bytes 29213291
+ 00842948 bytes 29e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42075447afe28945258c8cc74cfcb2da"></a>

### [`00842a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842a50.md) → [`00842a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842a50.md) FUN_00842a50

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00842a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842a1c.md) · 呼出先 6件 [`00574ff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff4.md) [`00841c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00841/00841c14.md) [`009bd60c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009bd/009bd60c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00842a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842a1c.md) · 呼出先 6件 [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`00841c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00841/00841c14.md) [`009bd60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd60c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.16% / 新版 84.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00842aa0",
      "incomplete_value": true,
      "site": "00842ab0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842aa0",
      "incomplete_value": true,
      "site": "00842ab0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec3:8"
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
      "definition_site": "00842aa0",
      "incomplete_value": true,
      "site": "00842ab0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00842aa0",
      "incomplete_value": true,
      "site": "00842ab0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00842ab4",
      "incomplete_value": true,
      "site": "00842abc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00842ab4",
      "incomplete_value": true,
      "site": "00842abc",
      "value": [
        "LOAD",
        "16",
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
      "00842aa0",
      "READ",
      [
        "storage",
        "00294ec3",
        null,
        "string"
      ]
    ],
    [
      "00842aa0",
      "READ",
      [
        "storage",
        "00294ed3",
        null,
        "string"
      ]
    ],
    [
      "00842ab4",
      "READ",
      [
        "storage",
        "00294ee3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00842aa0",
      "READ",
      [
        "storage",
        "00294f50",
        null,
        "string"
      ]
    ],
    [
      "00842aa0",
      "READ",
      [
        "storage",
        "00294f60",
        null,
        "string"
      ]
    ],
    [
      "00842ab4",
      "READ",
      [
        "storage",
        "00294f70",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842a50.md#insn-00842a98) · [`00842a9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842a50.md#insn-00842a9c)
- 新版 `00842a98`（命令位置の公開資料なし） · `00842a9c`（命令位置の公開資料なし）

~~~diff
- 00842a98 ["COPY", "tmp:0:8", ["const:ec3:8"]]
- 00842a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842a98 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 00842a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842a98 bytes 080d3b91
+ 00842a98 bytes 08413d91
- 00842a9c ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00842a9c bytes 69d3fff0
+ 00842a9c ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00842a9c bytes 69d3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46d24711667bcb34a14186cdfb51b45f"></a>

### [`00842c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842c68.md) → [`00842c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842c68.md) FUN_00842c68

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
      "definition_site": "00842c7c",
      "incomplete_value": false,
      "site": "00842c80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842c7c",
      "incomplete_value": false,
      "site": "00842c80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "00842c80",
      "DATA",
      [
        "storage",
        "00c01d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842c80",
      "DATA",
      [
        "storage",
        "00c01db8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842c68.md#insn-00842c7c)
- 新版 `00842c7c`（命令位置の公開資料なし）

~~~diff
- 00842c7c ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00842c7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842c7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842c7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842c7c ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00842c7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842c7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842c7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842c7c bytes 08213491
+ 00842c7c bytes 08e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a9c8b750576910dc2d2713c94684154"></a>

### [`00842cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842cc4.md) → [`00842cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842cc4.md) FUN_00842cc4

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
      "definition_site": "00842cdc",
      "incomplete_value": false,
      "site": "00842ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842cdc",
      "incomplete_value": false,
      "site": "00842ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "00842ce0",
      "DATA",
      [
        "storage",
        "00c01d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842ce0",
      "DATA",
      [
        "storage",
        "00c01db8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842cc4.md#insn-00842cdc)
- 新版 `00842cdc`（命令位置の公開資料なし）

~~~diff
- 00842cdc ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00842cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00842cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00842cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00842cdc ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00842cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00842cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00842cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00842cdc bytes 08213491
+ 00842cdc bytes 08e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8af81b7590234b55956b17fe3cb63dcb"></a>

### [`00842d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842d20.md) → [`00842d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00842/00842d20.md) FUN_00842d20

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
      "definition_site": "00842d44",
      "incomplete_value": false,
      "site": "00842d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00842d44",
      "incomplete_value": false,
      "site": "00842d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "00842d48",
      "DATA",
      [
        "storage",
        "00c01d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00842d48",
      "DATA",
      [
        "storage",
        "00c01db8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00842d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00842/00842d20.md#insn-00842d44)
- 新版 `00842d44`（命令位置の公開資料なし）

~~~diff
- 00842d44 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00842d44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00842d44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00842d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00842d44 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00842d44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00842d44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00842d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00842d44 bytes 29213491
+ 00842d44 bytes 29e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

