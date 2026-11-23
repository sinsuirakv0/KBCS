# v15.7.2 → v15.7.3 · 最優先の変更候補 (48)

[一覧の目次](README.md)

<a id="compare-6094a46390bdf5c28ef26ec924db9225"></a>

### [`008fe16c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe16c.md) → [`008fe16c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe16c.md) FUN_008fe16c

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
      "definition_site": "008fe170",
      "incomplete_value": false,
      "site": "008fe174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe170",
      "incomplete_value": false,
      "site": "008fe174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
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
      "008fe174",
      "DATA",
      [
        "storage",
        "00c08e60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fe174",
      "DATA",
      [
        "storage",
        "00c08f10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe16c.md#insn-008fe170)
- 新版 `008fe170`（命令位置の公開資料なし）

~~~diff
- 008fe170 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 008fe170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe170 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 008fe170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe170 bytes 08813991
+ 008fe170 bytes 08413c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b6e7284d3522f2940a920d4c1f67339"></a>

### [`008fe22c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe22c.md) → [`008fe22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe22c.md) FUN_008fe22c

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
      "definition_site": "008fe240",
      "incomplete_value": false,
      "site": "008fe244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe240",
      "incomplete_value": false,
      "site": "008fe244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "008fe244",
      "DATA",
      [
        "storage",
        "00c08ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fe244",
      "DATA",
      [
        "storage",
        "00c08f90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe22c.md#insn-008fe240)
- 新版 `008fe240`（命令位置の公開資料なし）

~~~diff
- 008fe240 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 008fe240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe240 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 008fe240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe240 bytes 08813b91
+ 008fe240 bytes 08413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b99e20ff9765564bdf6a984706b8da80"></a>

### [`008fe250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe250.md) → [`008fe250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe250.md) FUN_008fe250

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
      "definition_site": "008fe254",
      "incomplete_value": false,
      "site": "008fe258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe254",
      "incomplete_value": false,
      "site": "008fe258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "008fe258",
      "DATA",
      [
        "storage",
        "00c08ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fe258",
      "DATA",
      [
        "storage",
        "00c08f90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe250.md#insn-008fe254)
- 新版 `008fe254`（命令位置の公開資料なし）

~~~diff
- 008fe254 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 008fe254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe254 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 008fe254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe254 bytes 08813b91
+ 008fe254 bytes 08413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b54fd319bfa781fbbc45a9fe6f38c32"></a>

### [`008fe310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe310.md) → [`008fe310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe310.md) FUN_008fe310

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
      "definition_site": "008fe324",
      "incomplete_value": false,
      "site": "008fe328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe324",
      "incomplete_value": false,
      "site": "008fe328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f70:8"
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
      "008fe328",
      "DATA",
      [
        "storage",
        "00c08f70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fe328",
      "DATA",
      [
        "storage",
        "00c09020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe310.md#insn-008fe320) · [`008fe324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe310.md#insn-008fe324)
- 新版 `008fe320`（命令位置の公開資料なし） · `008fe324`（命令位置の公開資料なし）

~~~diff
- 008fe320 ["COPY", "register:4040:8", ["const:c08000:8"]]
+ 008fe320 ["COPY", "register:4040:8", ["const:c09000:8"]]
- 008fe320 bytes 481800d0
+ 008fe320 bytes 481800f0
- 008fe324 ["COPY", "tmp:0:8", ["const:f70:8"]]
- 008fe324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe324 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 008fe324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe324 bytes 08c13d91
+ 008fe324 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7517f849578a12a7ccdcea6d8143236d"></a>

### [`008fe334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe334.md) → [`008fe334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe334.md) FUN_008fe334

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
      "definition_site": "008fe338",
      "incomplete_value": false,
      "site": "008fe33c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe338",
      "incomplete_value": false,
      "site": "008fe33c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
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
      "008fe33c",
      "DATA",
      [
        "storage",
        "00c08f70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fe33c",
      "DATA",
      [
        "storage",
        "00c09020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe334.md#insn-008fe334) · [`008fe338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe334.md#insn-008fe338)
- 新版 `008fe334`（命令位置の公開資料なし） · `008fe338`（命令位置の公開資料なし）

~~~diff
- 008fe334 ["COPY", "register:4040:8", ["const:c08000:8"]]
+ 008fe334 ["COPY", "register:4040:8", ["const:c09000:8"]]
- 008fe334 bytes 481800d0
+ 008fe334 bytes 481800f0
- 008fe338 ["COPY", "tmp:0:8", ["const:f70:8"]]
- 008fe338 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe338 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe338 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe338 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 008fe338 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe338 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe338 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe338 bytes 08c13d91
+ 008fe338 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a418038b412048d65bae2c267e5fb8a"></a>

### [`008fe34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe34c.md) → [`008fe34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe34c.md) FUN_008fe34c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 22件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 22件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fe51c",
      "incomplete_value": false,
      "site": "008fe52c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe51c",
      "incomplete_value": false,
      "site": "008fe52c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
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
      "definition_site": "008fe554",
      "incomplete_value": false,
      "site": "008fe564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe554",
      "incomplete_value": false,
      "site": "008fe564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "definition_site": "008fe61c",
      "incomplete_value": true,
      "site": "008fe634",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008fe61c",
      "incomplete_value": true,
      "site": "008fe634",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "008fe52c",
      "DATA",
      [
        "storage",
        "00c08fe0",
        null,
        "undefined *"
      ]
    ],
    [
      "008fe564",
      "DATA",
      [
        "storage",
        "00c09060",
        null,
        "undefined *"
      ]
    ],
    [
      "008fe5a0",
      "READ",
      [
        "storage",
        "00c09000",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008fe52c",
      "DATA",
      [
        "storage",
        "00c09090",
        null,
        "undefined *"
      ]
    ],
    [
      "008fe564",
      "DATA",
      [
        "storage",
        "00c09110",
        null,
        "undefined *"
      ]
    ],
    [
      "008fe5a0",
      "READ",
      [
        "storage",
        "00c090b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe34c.md#insn-008fe518) · [`008fe51c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe34c.md#insn-008fe51c) · [`008fe554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe34c.md#insn-008fe554)
- 新版 `008fe518`（命令位置の公開資料なし） · `008fe51c`（命令位置の公開資料なし） · `008fe554`（命令位置の公開資料なし）

~~~diff
- 008fe518 ["COPY", "register:4040:8", ["const:c08000:8"]]
+ 008fe518 ["COPY", "register:4040:8", ["const:c09000:8"]]
- 008fe518 bytes 481800d0
+ 008fe518 bytes 481800f0
- 008fe51c ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 008fe51c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe51c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe51c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe51c ["COPY", "tmp:0:8", ["const:90:8"]]
+ 008fe51c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe51c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe51c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe51c bytes 08813f91
+ 008fe51c bytes 08410291
- 008fe554 ["COPY", "tmp:0:8", ["const:60:8"]]
- 008fe554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe554 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 008fe554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe554 bytes 08810191
+ 008fe554 bytes 08410491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ff8f3f0b28cff041c5d26ecd7697df"></a>

### [`008fe76c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe76c.md) → [`008fe76c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe76c.md) FUN_008fe76c

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
      "definition_site": "008fe780",
      "incomplete_value": false,
      "site": "008fe784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe780",
      "incomplete_value": false,
      "site": "008fe784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
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
      "008fe784",
      "DATA",
      [
        "storage",
        "00c08fe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fe784",
      "DATA",
      [
        "storage",
        "00c09090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe77c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe76c.md#insn-008fe77c) · [`008fe780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe76c.md#insn-008fe780)
- 新版 `008fe77c`（命令位置の公開資料なし） · `008fe780`（命令位置の公開資料なし）

~~~diff
- 008fe77c ["COPY", "register:4040:8", ["const:c08000:8"]]
+ 008fe77c ["COPY", "register:4040:8", ["const:c09000:8"]]
- 008fe77c bytes 481800d0
+ 008fe77c bytes 481800f0
- 008fe780 ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 008fe780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe780 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 008fe780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe780 bytes 08813f91
+ 008fe780 bytes 08410291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73144e3fc71d49670bdfcfe193f97dc3"></a>

### [`008fe790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe790.md) → [`008fe790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe790.md) FUN_008fe790

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
      "definition_site": "008fe794",
      "incomplete_value": false,
      "site": "008fe798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe794",
      "incomplete_value": false,
      "site": "008fe798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
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
      "008fe798",
      "DATA",
      [
        "storage",
        "00c08fe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fe798",
      "DATA",
      [
        "storage",
        "00c09090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe790.md#insn-008fe790) · [`008fe794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe790.md#insn-008fe794)
- 新版 `008fe790`（命令位置の公開資料なし） · `008fe794`（命令位置の公開資料なし）

~~~diff
- 008fe790 ["COPY", "register:4040:8", ["const:c08000:8"]]
+ 008fe790 ["COPY", "register:4040:8", ["const:c09000:8"]]
- 008fe790 bytes 481800d0
+ 008fe790 bytes 481800f0
- 008fe794 ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 008fe794 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe794 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe794 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe794 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 008fe794 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe794 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe794 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe794 bytes 08813f91
+ 008fe794 bytes 08410291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c2cd6d9a5d3cf74b6ed416b099125e9"></a>

### [`008fe850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe850.md) → [`008fe850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe850.md) FUN_008fe850

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
      "definition_site": "008fe864",
      "incomplete_value": false,
      "site": "008fe868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe864",
      "incomplete_value": false,
      "site": "008fe868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "008fe868",
      "DATA",
      [
        "storage",
        "00c09060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fe868",
      "DATA",
      [
        "storage",
        "00c09110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe850.md#insn-008fe864)
- 新版 `008fe864`（命令位置の公開資料なし）

~~~diff
- 008fe864 ["COPY", "tmp:0:8", ["const:60:8"]]
- 008fe864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe864 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 008fe864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe864 bytes 08810191
+ 008fe864 bytes 08410491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-973dc6447c63416898b199fc620fa5fc"></a>

### [`008fe874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe874.md) → [`008fe874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe874.md) FUN_008fe874

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
      "definition_site": "008fe878",
      "incomplete_value": false,
      "site": "008fe87c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe878",
      "incomplete_value": false,
      "site": "008fe87c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "008fe87c",
      "DATA",
      [
        "storage",
        "00c09060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fe87c",
      "DATA",
      [
        "storage",
        "00c09110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe874.md#insn-008fe878)
- 新版 `008fe878`（命令位置の公開資料なし）

~~~diff
- 008fe878 ["COPY", "tmp:0:8", ["const:60:8"]]
- 008fe878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe878 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 008fe878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe878 bytes 08810191
+ 008fe878 bytes 08410491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8aa543a5b2d6595b65eff54d1f31b6f"></a>

### [`008fe934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe934.md) → [`008fe934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe934.md) FUN_008fe934

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
      "definition_site": "008fe954",
      "incomplete_value": false,
      "site": "008fe958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe954",
      "incomplete_value": false,
      "site": "008fe958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "008fe958",
      "DATA",
      [
        "storage",
        "00c090f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fe958",
      "DATA",
      [
        "storage",
        "00c091a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe934.md#insn-008fe954)
- 新版 `008fe954`（命令位置の公開資料なし）

~~~diff
- 008fe954 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 008fe954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe954 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 008fe954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe954 bytes 08c10391
+ 008fe954 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b688fd9d6a99e851e26fb841db334148"></a>

### [`008fe96c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe96c.md) → [`008fe96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe96c.md) FUN_008fe96c

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
      "definition_site": "008fe970",
      "incomplete_value": false,
      "site": "008fe974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe970",
      "incomplete_value": false,
      "site": "008fe974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "008fe974",
      "DATA",
      [
        "storage",
        "00c090f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fe974",
      "DATA",
      [
        "storage",
        "00c091a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe96c.md#insn-008fe970)
- 新版 `008fe970`（命令位置の公開資料なし）

~~~diff
- 008fe970 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 008fe970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe970 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 008fe970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe970 bytes 08c10391
+ 008fe970 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd828edbf0e52868eea52310229a4d84"></a>

### [`008fea5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fea5c.md) → [`008fea5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fea5c.md) FUN_008fea5c

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
      "definition_site": "008fea7c",
      "incomplete_value": false,
      "site": "008fea80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fea7c",
      "incomplete_value": false,
      "site": "008fea80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "008fea80",
      "DATA",
      [
        "storage",
        "00c09170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fea80",
      "DATA",
      [
        "storage",
        "00c09220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fea7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fea5c.md#insn-008fea7c)
- 新版 `008fea7c`（命令位置の公開資料なし）

~~~diff
- 008fea7c ["COPY", "tmp:0:8", ["const:170:8"]]
- 008fea7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fea7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fea7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fea7c ["COPY", "tmp:0:8", ["const:220:8"]]
+ 008fea7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fea7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fea7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fea7c bytes 08c10591
+ 008fea7c bytes 08810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b70399a0e8ee216e8737c3459154f28"></a>

### [`008fea94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fea94.md) → [`008fea94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fea94.md) FUN_008fea94

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
      "definition_site": "008fea98",
      "incomplete_value": false,
      "site": "008fea9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fea98",
      "incomplete_value": false,
      "site": "008fea9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "008fea9c",
      "DATA",
      [
        "storage",
        "00c09170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fea9c",
      "DATA",
      [
        "storage",
        "00c09220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fea98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fea94.md#insn-008fea98)
- 新版 `008fea98`（命令位置の公開資料なし）

~~~diff
- 008fea98 ["COPY", "tmp:0:8", ["const:170:8"]]
- 008fea98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fea98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fea98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fea98 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 008fea98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fea98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fea98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fea98 bytes 08c10591
+ 008fea98 bytes 08810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8742b927a33e5ca27916a41a2e1d8ea0"></a>

### [`008feb84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008feb84.md) → [`008feb84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008feb84.md) FUN_008feb84

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
      "definition_site": "008feb98",
      "incomplete_value": false,
      "site": "008feb9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008feb98",
      "incomplete_value": false,
      "site": "008feb9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "008feb9c",
      "DATA",
      [
        "storage",
        "00c091f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008feb9c",
      "DATA",
      [
        "storage",
        "00c092a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008feb98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008feb84.md#insn-008feb98)
- 新版 `008feb98`（命令位置の公開資料なし）

~~~diff
- 008feb98 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 008feb98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008feb98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008feb98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008feb98 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 008feb98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008feb98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008feb98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008feb98 bytes 08c10791
+ 008feb98 bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f880fe0c953e5e211ebb3e9bd918cfbf"></a>

### [`008feba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008feba8.md) → [`008feba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008feba8.md) FUN_008feba8

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
      "definition_site": "008febac",
      "incomplete_value": false,
      "site": "008febb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008febac",
      "incomplete_value": false,
      "site": "008febb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "008febb0",
      "DATA",
      [
        "storage",
        "00c091f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008febb0",
      "DATA",
      [
        "storage",
        "00c092a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008febac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008feba8.md#insn-008febac)
- 新版 `008febac`（命令位置の公開資料なし）

~~~diff
- 008febac ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 008febac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008febac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008febac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008febac ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 008febac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008febac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008febac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008febac bytes 08c10791
+ 008febac bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c43df0e64b4e3a17aed4c515cfcc1a5"></a>

### [`008febc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008febc0.md) → [`008febc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008febc0.md) FUN_008febc0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`006fd45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fd45c.md) [`006fd460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fd460.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006fd45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd45c.md) [`006fd460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd460.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008fec90",
      "incomplete_value": true,
      "site": "008feca4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:113:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fec90",
      "incomplete_value": true,
      "site": "008feca4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:86:8"
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
      "definition_site": "008feca8",
      "incomplete_value": true,
      "site": "008feca8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008feca8",
      "incomplete_value": true,
      "site": "008feca8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fecbc",
      "incomplete_value": false,
      "site": "008fecc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fecbc",
      "incomplete_value": false,
      "site": "008fecc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "008fec90",
      "READ",
      [
        "storage",
        "00295086",
        null,
        "string"
      ]
    ],
    [
      "008fec98",
      "READ",
      [
        "storage",
        "00295093",
        null,
        "string"
      ]
    ],
    [
      "008fecc4",
      "DATA",
      [
        "storage",
        "00c09260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fec90",
      "READ",
      [
        "storage",
        "00295113",
        null,
        "string"
      ]
    ],
    [
      "008fec98",
      "READ",
      [
        "storage",
        "00295120",
        null,
        "string"
      ]
    ],
    [
      "008fecc4",
      "DATA",
      [
        "storage",
        "00c09310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fec8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008febc0.md#insn-008fec8c) · [`008fecbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008febc0.md#insn-008fecbc) · [`008fecc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008febc0.md#insn-008fecc0)
- 新版 `008fec8c`（命令位置の公開資料なし） · `008fecbc`（命令位置の公開資料なし）

~~~diff
- 008fec8c ["COPY", "tmp:0:8", ["const:86:8"]]
- 008fec8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008fec8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008fec8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008fec8c ["COPY", "tmp:0:8", ["const:113:8"]]
+ 008fec8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008fec8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008fec8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008fec8c bytes 29190291
+ 008fec8c bytes 294d0491
- 008fecbc ["COPY", "tmp:0:8", ["const:260:8"]]
- 008fecbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fecbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fecbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fecbc ["COPY", "tmp:0:8", ["const:310:8"]]
+ 008fecbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fecbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fecbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fecbc bytes 08810991
+ 008fecbc bytes 08410c91
- 008fecc0 ["COPY", "tmp:0:8", ["const:30:8"]]
- 008fecc0 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 008fecc0 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 008fecc0 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 008fecc0 bytes f4c30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee9c8b08fdd795136fdfdd733d105193"></a>

### [`008fee6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fee6c.md) → [`008fee6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fee6c.md) FUN_008fee6c

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
      "definition_site": "008fee80",
      "incomplete_value": false,
      "site": "008fee84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fee80",
      "incomplete_value": false,
      "site": "008fee84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "008fee84",
      "DATA",
      [
        "storage",
        "00c09260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fee84",
      "DATA",
      [
        "storage",
        "00c09310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fee80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fee6c.md#insn-008fee80)
- 新版 `008fee80`（命令位置の公開資料なし）

~~~diff
- 008fee80 ["COPY", "tmp:0:8", ["const:260:8"]]
- 008fee80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fee80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fee80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fee80 ["COPY", "tmp:0:8", ["const:310:8"]]
+ 008fee80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fee80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fee80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fee80 bytes 08810991
+ 008fee80 bytes 08410c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31984433228f2a2007001e5fd3322433"></a>

### [`008fee90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fee90.md) → [`008fee90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fee90.md) FUN_008fee90

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
      "definition_site": "008fee94",
      "incomplete_value": false,
      "site": "008fee98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fee94",
      "incomplete_value": false,
      "site": "008fee98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "008fee98",
      "DATA",
      [
        "storage",
        "00c09260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fee98",
      "DATA",
      [
        "storage",
        "00c09310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fee94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fee90.md#insn-008fee94)
- 新版 `008fee94`（命令位置の公開資料なし）

~~~diff
- 008fee94 ["COPY", "tmp:0:8", ["const:260:8"]]
- 008fee94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fee94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fee94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fee94 ["COPY", "tmp:0:8", ["const:310:8"]]
+ 008fee94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fee94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fee94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fee94 bytes 08810991
+ 008fee94 bytes 08410c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-136cb4e799367486b94c7f0181304683"></a>

### [`008fef1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fef1c.md) → [`008fef1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fef1c.md) FUN_008fef1c

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
      "definition_site": "008fef30",
      "incomplete_value": false,
      "site": "008fef34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fef30",
      "incomplete_value": false,
      "site": "008fef34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "008fef34",
      "DATA",
      [
        "storage",
        "00c092f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fef34",
      "DATA",
      [
        "storage",
        "00c093a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fef30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fef1c.md#insn-008fef30)
- 新版 `008fef30`（命令位置の公開資料なし）

~~~diff
- 008fef30 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 008fef30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fef30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fef30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fef30 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 008fef30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fef30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fef30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fef30 bytes 08c10b91
+ 008fef30 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de6a2f329b8a56381e378df7dc9f42bc"></a>

### [`008fef40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fef40.md) → [`008fef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fef40.md) FUN_008fef40

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
      "definition_site": "008fef44",
      "incomplete_value": false,
      "site": "008fef48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fef44",
      "incomplete_value": false,
      "site": "008fef48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "008fef48",
      "DATA",
      [
        "storage",
        "00c092f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fef48",
      "DATA",
      [
        "storage",
        "00c093a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fef44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fef40.md#insn-008fef44)
- 新版 `008fef44`（命令位置の公開資料なし）

~~~diff
- 008fef44 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 008fef44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fef44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fef44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fef44 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 008fef44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fef44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fef44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fef44 bytes 08c10b91
+ 008fef44 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-583551bcf413a90401708a4575939f4b"></a>

### [`008ff09c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff09c.md) → [`008ff09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff09c.md) FUN_008ff09c

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
      "definition_site": "008ff0b0",
      "incomplete_value": false,
      "site": "008ff0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff0b0",
      "incomplete_value": false,
      "site": "008ff0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "008ff0b4",
      "DATA",
      [
        "storage",
        "00c09370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ff0b4",
      "DATA",
      [
        "storage",
        "00c09420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ff0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff09c.md#insn-008ff0b0)
- 新版 `008ff0b0`（命令位置の公開資料なし）

~~~diff
- 008ff0b0 ["COPY", "tmp:0:8", ["const:370:8"]]
- 008ff0b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ff0b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ff0b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ff0b0 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 008ff0b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff0b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff0b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ff0b0 bytes 08c10d91
+ 008ff0b0 bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d6e9d83e0f2ab48ba695fd085c7a55b"></a>

### [`008ff0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff0c0.md) → [`008ff0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff0c0.md) FUN_008ff0c0

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
      "definition_site": "008ff0c4",
      "incomplete_value": false,
      "site": "008ff0c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff0c4",
      "incomplete_value": false,
      "site": "008ff0c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "008ff0c8",
      "DATA",
      [
        "storage",
        "00c09370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ff0c8",
      "DATA",
      [
        "storage",
        "00c09420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ff0c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff0c0.md#insn-008ff0c4)
- 新版 `008ff0c4`（命令位置の公開資料なし）

~~~diff
- 008ff0c4 ["COPY", "tmp:0:8", ["const:370:8"]]
- 008ff0c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ff0c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ff0c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ff0c4 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 008ff0c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff0c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff0c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ff0c4 bytes 08c10d91
+ 008ff0c4 bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0e80b5bd3f0f3456a88971fe7fde0ba"></a>

### [`008ff208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff208.md) → [`008ff208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff208.md) FUN_008ff208

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
      "definition_site": "008ff228",
      "incomplete_value": false,
      "site": "008ff22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff228",
      "incomplete_value": false,
      "site": "008ff22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "008ff22c",
      "DATA",
      [
        "storage",
        "00c093f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ff22c",
      "DATA",
      [
        "storage",
        "00c094a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ff228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff208.md#insn-008ff228)
- 新版 `008ff228`（命令位置の公開資料なし）

~~~diff
- 008ff228 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 008ff228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ff228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ff228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ff228 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 008ff228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ff228 bytes 08c10f91
+ 008ff228 bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c67b027cee66dc58c817349a33c1ee0d"></a>

### [`008ff240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff240.md) → [`008ff240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff240.md) FUN_008ff240

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
      "definition_site": "008ff244",
      "incomplete_value": false,
      "site": "008ff248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff244",
      "incomplete_value": false,
      "site": "008ff248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "008ff248",
      "DATA",
      [
        "storage",
        "00c093f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ff248",
      "DATA",
      [
        "storage",
        "00c094a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ff244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff240.md#insn-008ff244)
- 新版 `008ff244`（命令位置の公開資料なし）

~~~diff
- 008ff244 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 008ff244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ff244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ff244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ff244 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 008ff244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ff244 bytes 08c10f91
+ 008ff244 bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ccc47a09347af54adf163d65dbf309b"></a>

### [`008ff330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff330.md) → [`008ff330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff330.md) FUN_008ff330

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
      "definition_site": "008ff350",
      "incomplete_value": false,
      "site": "008ff354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff350",
      "incomplete_value": false,
      "site": "008ff354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "008ff354",
      "DATA",
      [
        "storage",
        "00c09470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ff354",
      "DATA",
      [
        "storage",
        "00c09520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ff350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff330.md#insn-008ff350)
- 新版 `008ff350`（命令位置の公開資料なし）

~~~diff
- 008ff350 ["COPY", "tmp:0:8", ["const:470:8"]]
- 008ff350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ff350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ff350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ff350 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 008ff350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ff350 bytes 08c11191
+ 008ff350 bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db7184f9c05dca561f9eb808224a736c"></a>

### [`008ff368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff368.md) → [`008ff368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff368.md) FUN_008ff368

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
      "definition_site": "008ff36c",
      "incomplete_value": true,
      "site": "008ff370",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff36c",
      "incomplete_value": true,
      "site": "008ff370",
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
      "008ff370",
      "DATA",
      [
        "storage",
        "00c09470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ff370",
      "DATA",
      [
        "storage",
        "00c09520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ff36c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff368.md#insn-008ff36c)
- 新版 `008ff36c`（命令位置の公開資料なし）

~~~diff
- 008ff36c ["COPY", "tmp:0:8", ["const:470:8"]]
- 008ff36c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ff36c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ff36c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ff36c ["COPY", "tmp:0:8", ["const:520:8"]]
+ 008ff36c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff36c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff36c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ff36c bytes 08c11191
+ 008ff36c bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b522cc5e2cdfe2bb093cfb9eea1e973d"></a>

### [`008ff458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff458.md) → [`008ff458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff458.md) FUN_008ff458

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
      "definition_site": "008ff47c",
      "incomplete_value": false,
      "site": "008ff47c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff47c",
      "incomplete_value": false,
      "site": "008ff47c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "008ff47c",
      "DATA",
      [
        "storage",
        "00c094f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ff47c",
      "DATA",
      [
        "storage",
        "00c095a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ff478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff458.md#insn-008ff478)
- 新版 `008ff478`（命令位置の公開資料なし）

~~~diff
- 008ff478 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 008ff478 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ff478 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ff478 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ff478 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 008ff478 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff478 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ff478 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ff478 bytes 08c11391
+ 008ff478 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d47bb5001a7f361863b3919b2f05c28"></a>

### [`008ff48c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff48c.md) → [`008ff48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff48c.md) FUN_008ff48c

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
      "definition_site": "008ff498",
      "incomplete_value": false,
      "site": "008ff498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff498",
      "incomplete_value": false,
      "site": "008ff498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "008ff498",
      "DATA",
      [
        "storage",
        "00c094f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ff498",
      "DATA",
      [
        "storage",
        "00c095a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ff494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff48c.md#insn-008ff494)
- 新版 `008ff494`（命令位置の公開資料なし）

~~~diff
- 008ff494 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 008ff494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ff494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ff494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ff494 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 008ff494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ff494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ff494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ff494 bytes 29c11391
+ 008ff494 bytes 29811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37a65fd39df830e75e5bd23131e92fd9"></a>

### [`008ff4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff4a8.md) → [`008ff4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff4a8.md) FUN_008ff4a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 23件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0065059c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00650/0065059c.md)
- 新版 呼出元 0件  · 呼出先 23件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0065059c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/0065059c.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.44% / 新版 95.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008ff5c8",
      "incomplete_value": true,
      "site": "008ff5d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b87:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff5c8",
      "incomplete_value": true,
      "site": "008ff5d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:afa:8"
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
      "definition_site": "008ff658",
      "incomplete_value": true,
      "site": "008ff664",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e69:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff658",
      "incomplete_value": true,
      "site": "008ff664",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e63:8"
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
      "definition_site": "008ff7e8",
      "incomplete_value": false,
      "site": "008ff7e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff7e8",
      "incomplete_value": false,
      "site": "008ff7e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
      "008ff5c8",
      "READ",
      [
        "storage",
        "0029eafa",
        null,
        "string"
      ]
    ],
    [
      "008ff658",
      "READ",
      [
        "storage",
        "002abe63",
        null,
        "string"
      ]
    ],
    [
      "008ff6a0",
      "PARAM",
      [
        "storage",
        "0029d986",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008ff5c8",
      "READ",
      [
        "storage",
        "0029eb87",
        null,
        "string"
      ]
    ],
    [
      "008ff658",
      "READ",
      [
        "storage",
        "002abe69",
        null,
        "string"
      ]
    ],
    [
      "008ff6a0",
      "PARAM",
      [
        "storage",
        "0029da13",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ff5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff4a8.md#insn-008ff5c0) · [`008ff650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff4a8.md#insn-008ff650) · [`008ff6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff4a8.md#insn-008ff6a0)
- 新版 `008ff5c0`（命令位置の公開資料なし） · `008ff650`（命令位置の公開資料なし） · `008ff6a0`（命令位置の公開資料なし）

~~~diff
- 008ff5c0 ["COPY", "tmp:0:8", ["const:afa:8"]]
- 008ff5c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ff5c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ff5c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ff5c0 ["COPY", "tmp:0:8", ["const:b87:8"]]
+ 008ff5c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ff5c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ff5c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ff5c0 bytes 29e92b91
+ 008ff5c0 bytes 291d2e91
- 008ff650 ["COPY", "tmp:0:8", ["const:e63:8"]]
- 008ff650 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ff650 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ff650 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ff650 ["COPY", "tmp:0:8", ["const:e69:8"]]
+ 008ff650 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ff650 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ff650 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ff650 bytes 298d3991
+ 008ff650 bytes 29a53991
- 008ff6a0 ["COPY", "tmp:0:8", ["const:986:8"]]
- 008ff6a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008ff6a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008ff6a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008ff6a0 ["COPY", "tmp:0:8", ["const:a13:8"]]
+ 008ff6a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008ff6a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008ff6a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008ff6a0 bytes 21182691
+ 008ff6a0 bytes 214c2891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3439d4ff8bb688b2e41864b3319b3e48"></a>

### [`008ff9e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff9e4.md) → [`008ff9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff9e4.md) FUN_008ff9e4

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
      "definition_site": "008ffa08",
      "incomplete_value": false,
      "site": "008ffa08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ffa08",
      "incomplete_value": false,
      "site": "008ffa08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
      "008ffa08",
      "DATA",
      [
        "storage",
        "00c09560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ffa08",
      "DATA",
      [
        "storage",
        "00c09610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ffa04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff9e4.md#insn-008ffa04)
- 新版 `008ffa04`（命令位置の公開資料なし）

~~~diff
- 008ffa04 ["COPY", "tmp:0:8", ["const:560:8"]]
- 008ffa04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ffa04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ffa04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ffa04 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 008ffa04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ffa04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ffa04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ffa04 bytes 08811591
+ 008ffa04 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6e2e7de40cb0f1eee78c8b5e8d14f88"></a>

### [`008ffa18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffa18.md) → [`008ffa18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffa18.md) FUN_008ffa18

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
      "definition_site": "008ffa24",
      "incomplete_value": false,
      "site": "008ffa24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ffa24",
      "incomplete_value": false,
      "site": "008ffa24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
      "008ffa24",
      "DATA",
      [
        "storage",
        "00c09560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ffa24",
      "DATA",
      [
        "storage",
        "00c09610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ffa20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffa18.md#insn-008ffa20)
- 新版 `008ffa20`（命令位置の公開資料なし）

~~~diff
- 008ffa20 ["COPY", "tmp:0:8", ["const:560:8"]]
- 008ffa20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ffa20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ffa20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ffa20 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 008ffa20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ffa20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ffa20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ffa20 bytes 29811591
+ 008ffa20 bytes 29411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af12fb7f12ecc166f480e74bc5532307"></a>

### [`008ffb28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffb28.md) → [`008ffb28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffb28.md) FUN_008ffb28

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
      "definition_site": "008ffb48",
      "incomplete_value": false,
      "site": "008ffb4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ffb48",
      "incomplete_value": false,
      "site": "008ffb4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "008ffb4c",
      "DATA",
      [
        "storage",
        "00c095f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ffb4c",
      "DATA",
      [
        "storage",
        "00c096a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ffb48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffb28.md#insn-008ffb48)
- 新版 `008ffb48`（命令位置の公開資料なし）

~~~diff
- 008ffb48 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 008ffb48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ffb48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ffb48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ffb48 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 008ffb48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ffb48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ffb48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ffb48 bytes 08c11791
+ 008ffb48 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0441ed5e3df921049a9f0a5450eaae2"></a>

### [`008ffb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffb60.md) → [`008ffb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffb60.md) FUN_008ffb60

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
      "definition_site": "008ffb64",
      "incomplete_value": false,
      "site": "008ffb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ffb64",
      "incomplete_value": false,
      "site": "008ffb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "008ffb68",
      "DATA",
      [
        "storage",
        "00c095f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ffb68",
      "DATA",
      [
        "storage",
        "00c096a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ffb64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffb60.md#insn-008ffb64)
- 新版 `008ffb64`（命令位置の公開資料なし）

~~~diff
- 008ffb64 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 008ffb64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ffb64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ffb64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ffb64 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 008ffb64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ffb64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ffb64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ffb64 bytes 08c11791
+ 008ffb64 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9233e00c05b45b9bc6d436a4df1cbdd1"></a>

### [`008ffc98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffc98.md) → [`008ffc98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffc98.md) FUN_008ffc98

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
      "definition_site": "008ffcbc",
      "incomplete_value": false,
      "site": "008ffcc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ffcbc",
      "incomplete_value": false,
      "site": "008ffcc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "008ffcc0",
      "DATA",
      [
        "storage",
        "00c09670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ffcc0",
      "DATA",
      [
        "storage",
        "00c09720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ffcbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffc98.md#insn-008ffcbc)
- 新版 `008ffcbc`（命令位置の公開資料なし）

~~~diff
- 008ffcbc ["COPY", "tmp:0:8", ["const:670:8"]]
- 008ffcbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ffcbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ffcbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ffcbc ["COPY", "tmp:0:8", ["const:720:8"]]
+ 008ffcbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ffcbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ffcbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ffcbc bytes 08c11991
+ 008ffcbc bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d419ab2186db275f25fdfd534c7b3b36"></a>

### [`008ffcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffcd8.md) → [`008ffcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffcd8.md) FUN_008ffcd8

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
      "definition_site": "008ffcdc",
      "incomplete_value": false,
      "site": "008ffce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ffcdc",
      "incomplete_value": false,
      "site": "008ffce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "008ffce0",
      "DATA",
      [
        "storage",
        "00c09670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ffce0",
      "DATA",
      [
        "storage",
        "00c09720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ffcdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffcd8.md#insn-008ffcdc)
- 新版 `008ffcdc`（命令位置の公開資料なし）

~~~diff
- 008ffcdc ["COPY", "tmp:0:8", ["const:670:8"]]
- 008ffcdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ffcdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ffcdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ffcdc ["COPY", "tmp:0:8", ["const:720:8"]]
+ 008ffcdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ffcdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ffcdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ffcdc bytes 08c11991
+ 008ffcdc bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daf0295565f6e26ab0d1416f9d2cdc08"></a>

### [`008ffd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffd00.md) → [`008ffd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffd00.md) FUN_008ffd00

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`006dd65c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006dd/006dd65c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`006dd65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006dd65c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.48% / 新版 96.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fff7c",
      "incomplete_value": false,
      "site": "008fff7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fff7c",
      "incomplete_value": false,
      "site": "008fff7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008ffe10",
      "incomplete_value": true,
      "site": "008ffe10",
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
      "definition_site": "008ffe10",
      "incomplete_value": true,
      "site": "008ffe10",
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
      "definition_site": "008ffe18",
      "incomplete_value": false,
      "site": "008ffe28",
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
      "definition_site": "008ffe18",
      "incomplete_value": false,
      "site": "008ffe28",
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
      "008ffe00",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008ffe18",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008ffe20",
      "PARAM",
      [
        "storage",
        "00bf4450",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008ffe00",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008ffe18",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008ffe20",
      "PARAM",
      [
        "storage",
        "00bf4500",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ffe00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffd00.md#insn-008ffe00) · [`008ffe18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffd00.md#insn-008ffe18) · [`008ffe20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffd00.md#insn-008ffe20)
- 新版 `008ffe00`（命令位置の公開資料なし） · `008ffe18`（命令位置の公開資料なし） · `008ffe20`（命令位置の公開資料なし）

~~~diff
- 008ffe00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
- 008ffe00 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008ffe00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 008ffe00 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008ffe00 bytes 20dd44f9
+ 008ffe00 bytes 203d45f9
- 008ffe18 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008ffe18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008ffe18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008ffe18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008ffe18 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008ffe18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008ffe18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008ffe18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008ffe18 bytes 21603691
+ 008ffe18 bytes 21203991
- 008ffe20 ["COPY", "tmp:0:8", ["const:450:8"]]
- 008ffe20 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008ffe20 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008ffe20 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008ffe20 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 008ffe20 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008ffe20 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008ffe20 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008ffe20 bytes 42401191
+ 008ffe20 bytes 42001491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4d1aed26c044d01b60436665e759221"></a>

### [`00900138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900138.md) → [`00900138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900138.md) FUN_00900138

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
      "definition_site": "0090015c",
      "incomplete_value": false,
      "site": "0090015c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0090015c",
      "incomplete_value": false,
      "site": "0090015c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "0090015c",
      "DATA",
      [
        "storage",
        "00c096e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0090015c",
      "DATA",
      [
        "storage",
        "00c09790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00900158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900138.md#insn-00900158)
- 新版 `00900158`（命令位置の公開資料なし）

~~~diff
- 00900158 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00900158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00900158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00900158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00900158 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 00900158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00900158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00900158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00900158 bytes 08811b91
+ 00900158 bytes 08411e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-522fcc3e09ecf2166f5a2b6072ed6215"></a>

### [`0090016c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/0090016c.md) → [`0090016c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/0090016c.md) FUN_0090016c

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
      "definition_site": "00900178",
      "incomplete_value": false,
      "site": "00900178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00900178",
      "incomplete_value": false,
      "site": "00900178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "00900178",
      "DATA",
      [
        "storage",
        "00c096e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00900178",
      "DATA",
      [
        "storage",
        "00c09790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00900174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/0090016c.md#insn-00900174)
- 新版 `00900174`（命令位置の公開資料なし）

~~~diff
- 00900174 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00900174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00900174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00900174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00900174 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 00900174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00900174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00900174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00900174 bytes 29811b91
+ 00900174 bytes 29411e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9d7c1846f48bbe6f457e9b748c272c9"></a>

### [`009002a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009002a8.md) → [`009002a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009002a8.md) FUN_009002a8

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
      "definition_site": "009002bc",
      "incomplete_value": false,
      "site": "009002c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009002bc",
      "incomplete_value": false,
      "site": "009002c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "009002c0",
      "DATA",
      [
        "storage",
        "00c09770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009002c0",
      "DATA",
      [
        "storage",
        "00c09820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009002bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009002a8.md#insn-009002bc)
- 新版 `009002bc`（命令位置の公開資料なし）

~~~diff
- 009002bc ["COPY", "tmp:0:8", ["const:770:8"]]
- 009002bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009002bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009002bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009002bc ["COPY", "tmp:0:8", ["const:820:8"]]
+ 009002bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009002bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009002bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009002bc bytes 08c11d91
+ 009002bc bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84485e63e0cb340cdb546ee9c5de20ea"></a>

### [`009002cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009002cc.md) → [`009002cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009002cc.md) FUN_009002cc

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
      "definition_site": "009002d0",
      "incomplete_value": false,
      "site": "009002d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009002d0",
      "incomplete_value": false,
      "site": "009002d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "009002d4",
      "DATA",
      [
        "storage",
        "00c09770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009002d4",
      "DATA",
      [
        "storage",
        "00c09820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009002d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009002cc.md#insn-009002d0)
- 新版 `009002d0`（命令位置の公開資料なし）

~~~diff
- 009002d0 ["COPY", "tmp:0:8", ["const:770:8"]]
- 009002d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009002d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009002d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009002d0 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 009002d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009002d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009002d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009002d0 bytes 08c11d91
+ 009002d0 bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7d40fa50c424182363585263d4ab312"></a>

### [`009002e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009002e4.md) → [`009002e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009002e4.md) FUN_009002e4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`006fd45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fd45c.md) [`006fd460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fd460.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006fd45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd45c.md) [`006fd460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd460.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009003b4",
      "incomplete_value": true,
      "site": "009003c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:113:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009003b4",
      "incomplete_value": true,
      "site": "009003c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:86:8"
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
      "definition_site": "009003cc",
      "incomplete_value": true,
      "site": "009003cc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "009003cc",
      "incomplete_value": true,
      "site": "009003cc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009003e0",
      "incomplete_value": false,
      "site": "009003e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009003e0",
      "incomplete_value": false,
      "site": "009003e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "009003b4",
      "READ",
      [
        "storage",
        "00295086",
        null,
        "string"
      ]
    ],
    [
      "009003bc",
      "READ",
      [
        "storage",
        "00295093",
        null,
        "string"
      ]
    ],
    [
      "009003e8",
      "DATA",
      [
        "storage",
        "00c097e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009003b4",
      "READ",
      [
        "storage",
        "00295113",
        null,
        "string"
      ]
    ],
    [
      "009003bc",
      "READ",
      [
        "storage",
        "00295120",
        null,
        "string"
      ]
    ],
    [
      "009003e8",
      "DATA",
      [
        "storage",
        "00c09890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009003b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009002e4.md#insn-009003b0) · [`009003e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009002e4.md#insn-009003e0) · [`009003e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009002e4.md#insn-009003e4)
- 新版 `009003b0`（命令位置の公開資料なし） · `009003e0`（命令位置の公開資料なし）

~~~diff
- 009003b0 ["COPY", "tmp:0:8", ["const:86:8"]]
- 009003b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009003b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009003b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009003b0 ["COPY", "tmp:0:8", ["const:113:8"]]
+ 009003b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009003b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009003b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009003b0 bytes 29190291
+ 009003b0 bytes 294d0491
- 009003e0 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 009003e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009003e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009003e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009003e0 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 009003e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009003e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009003e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009003e0 bytes 08811f91
+ 009003e0 bytes 08412291
- 009003e4 ["COPY", "tmp:0:8", ["const:30:8"]]
- 009003e4 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 009003e4 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 009003e4 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 009003e4 bytes f4c30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62091bd7fe8e1457903740a5fc14f223"></a>

### [`00900590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900590.md) → [`00900590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900590.md) FUN_00900590

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
      "definition_site": "009005a4",
      "incomplete_value": false,
      "site": "009005a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009005a4",
      "incomplete_value": false,
      "site": "009005a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "009005a8",
      "DATA",
      [
        "storage",
        "00c097e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009005a8",
      "DATA",
      [
        "storage",
        "00c09890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009005a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900590.md#insn-009005a4)
- 新版 `009005a4`（命令位置の公開資料なし）

~~~diff
- 009005a4 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 009005a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009005a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009005a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009005a4 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 009005a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009005a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009005a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009005a4 bytes 08811f91
+ 009005a4 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd14f263bd8f67b2dfec2033d2206891"></a>

### [`009005b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009005b4.md) → [`009005b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009005b4.md) FUN_009005b4

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
      "definition_site": "009005b8",
      "incomplete_value": false,
      "site": "009005bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009005b8",
      "incomplete_value": false,
      "site": "009005bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "009005bc",
      "DATA",
      [
        "storage",
        "00c097e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009005bc",
      "DATA",
      [
        "storage",
        "00c09890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009005b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009005b4.md#insn-009005b8)
- 新版 `009005b8`（命令位置の公開資料なし）

~~~diff
- 009005b8 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 009005b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009005b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009005b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009005b8 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 009005b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009005b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009005b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009005b8 bytes 08811f91
+ 009005b8 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccc3c696fb0f3490d7d1559d055eadaa"></a>

### [`0090063c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/0090063c.md) → [`0090063c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/0090063c.md) _INIT_179

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00900678",
      "incomplete_value": true,
      "site": "00900694",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00900678",
      "incomplete_value": true,
      "site": "00900694",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0090069c",
      "incomplete_value": true,
      "site": "009006b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0090069c",
      "incomplete_value": true,
      "site": "009006b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009006bc",
      "incomplete_value": true,
      "site": "009006d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009006bc",
      "incomplete_value": true,
      "site": "009006d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00900678",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0090069c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "009006bc",
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
      "00900678",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0090069c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "009006bc",
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

- 旧版 [`00900668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/0090063c.md#insn-00900668) · [`00900670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/0090063c.md#insn-00900670)
- 新版 `00900668`（命令位置の公開資料なし） · `00900670`（命令位置の公開資料なし）

~~~diff
- 00900668 ["COPY", "tmp:0:8", ["const:768:8"]]
- 00900668 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00900668 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00900668 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00900668 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 00900668 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00900668 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00900668 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00900668 bytes 73a21d91
+ 00900668 bytes 73a22091
- 00900670 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00900670 bytes 29cdfff0
+ 00900670 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00900670 bytes 29cdfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-223c42a3c3aa5740309f67c03284e156"></a>

### [`009009cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009009cc.md) → [`009009cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009009cc.md) FUN_009009cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00982c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982c5c.md) · 呼出先 3件 [`00900ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900ae0.md) [`00a6d884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d884.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 1件 [`00982c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982c5c.md) · 呼出先 3件 [`00900ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900ae0.md) [`00a6d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d884.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00900a0c",
      "incomplete_value": false,
      "site": "00900a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00900a0c",
      "incomplete_value": false,
      "site": "00900a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00900a14",
      "DATA",
      [
        "storage",
        "00c09870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00900a14",
      "DATA",
      [
        "storage",
        "00c09920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00900a0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009009cc.md#insn-00900a0c)
- 新版 `00900a0c`（命令位置の公開資料なし）

~~~diff
- 00900a0c ["COPY", "tmp:0:8", ["const:870:8"]]
- 00900a0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00900a0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00900a0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00900a0c ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00900a0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00900a0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00900a0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00900a0c bytes 08c12191
+ 00900a0c bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc8565d4e973165baa78dd0800b93b71"></a>

### [`00900d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900d80.md) → [`00900d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900d80.md) FUN_00900d80

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00a6d8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d8b4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00a6d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d8b4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "00900d98",
      "incomplete_value": false,
      "site": "00900da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00900d98",
      "incomplete_value": false,
      "site": "00900da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00900da4",
      "DATA",
      [
        "storage",
        "00c09870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00900da4",
      "DATA",
      [
        "storage",
        "00c09920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00900d98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900d80.md#insn-00900d98)
- 新版 `00900d98`（命令位置の公開資料なし）

~~~diff
- 00900d98 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00900d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00900d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00900d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00900d98 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00900d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00900d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00900d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00900d98 bytes 08c12191
+ 00900d98 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6662ac434817b31aca9fd91faebd02f4"></a>

### [`00900e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900e0c.md) → [`00900e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900e0c.md) FUN_00900e0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00a6d8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d8b4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00a6d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d8b4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00900e24",
      "incomplete_value": false,
      "site": "00900e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00900e24",
      "incomplete_value": false,
      "site": "00900e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "00900e30",
      "DATA",
      [
        "storage",
        "00c09870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00900e30",
      "DATA",
      [
        "storage",
        "00c09920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00900e24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900e0c.md#insn-00900e24)
- 新版 `00900e24`（命令位置の公開資料なし）

~~~diff
- 00900e24 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00900e24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00900e24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00900e24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00900e24 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00900e24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00900e24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00900e24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00900e24 bytes 08c12191
+ 00900e24 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eb3b2f3c4c725f1555016e6d5dc063e"></a>

### [`00901338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901338.md) → [`00901338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901338.md) FUN_00901338

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
      "definition_site": "0090133c",
      "incomplete_value": false,
      "site": "00901340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0090133c",
      "incomplete_value": false,
      "site": "00901340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "00901340",
      "DATA",
      [
        "storage",
        "00c098c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00901340",
      "DATA",
      [
        "storage",
        "00c09970",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0090133c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901338.md#insn-0090133c)
- 新版 `0090133c`（命令位置の公開資料なし）

~~~diff
- 0090133c ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 0090133c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0090133c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0090133c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0090133c ["COPY", "tmp:0:8", ["const:970:8"]]
+ 0090133c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0090133c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0090133c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0090133c bytes 08012391
+ 0090133c bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dce3f8d756683378cda4db351c0a355"></a>

### [`00901388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901388.md) → [`00901388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901388.md) _INIT_180

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00901428",
      "incomplete_value": true,
      "site": "00901440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00901428",
      "incomplete_value": true,
      "site": "00901440",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "009013c4",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "009013e8",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00901408",
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
      "009013c4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "009013e8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00901408",
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

- 旧版 [`009013b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901388.md#insn-009013b4) · [`009013bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901388.md#insn-009013bc)
- 新版 `009013b4`（命令位置の公開資料なし） · `009013bc`（命令位置の公開資料なし）

~~~diff
- 009013b4 ["COPY", "tmp:0:8", ["const:780:8"]]
- 009013b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009013b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009013b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009013b4 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 009013b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009013b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009013b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009013b4 bytes 73021e91
+ 009013b4 bytes 73022191
- 009013bc ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 009013bc bytes 29cdffd0
+ 009013bc ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 009013bc bytes 29cdffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51da15f0350eae66c44e50fdc6c758b9"></a>

### [`00901718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901718.md) → [`00901718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901718.md) FUN_00901718

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`0044a6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a6d0.md) [`00464a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.44% / 新版 97.44%

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
      "definition_site": "00901750",
      "incomplete_value": true,
      "site": "0090175c",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00901750",
      "incomplete_value": true,
      "site": "0090175c",
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
      "definition_site": "0090190c",
      "incomplete_value": true,
      "site": "00901910",
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
      "definition_site": "0090190c",
      "incomplete_value": true,
      "site": "00901910",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0090175c",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "009018d8",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ],
    [
      "009018dc",
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
      "0090175c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "009018d8",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "009018dc",
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

- 旧版 [`00901750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901718.md#insn-00901750) · [`009018d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901718.md#insn-009018d8) · [`009018dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901718.md#insn-009018dc)
- 新版 `00901750`（命令位置の公開資料なし） · `009018d8`（命令位置の公開資料なし） · `009018dc`（命令位置の公開資料なし）

~~~diff
- 00901750 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00901750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00901750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00901750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00901750 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00901750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00901750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00901750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00901750 bytes 08e13191
+ 00901750 bytes 08a13491
- 009018d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 009018d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 009018d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 009018d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 009018d8 bytes 086146f9
+ 009018d8 bytes 08b946f9
- 009018dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cc8:8"]]
- 009018dc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 009018dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
+ 009018dc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 009018dc bytes b56646f9
+ 009018dc bytes b5be46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc3c2bf5c79c267040ad4510570346cb"></a>

### [`00901d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901d24.md) → [`00901d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901d24.md) _INIT_181

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
      "definition_site": "00901d60",
      "incomplete_value": true,
      "site": "00901d7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00901d60",
      "incomplete_value": true,
      "site": "00901d7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00901d84",
      "incomplete_value": true,
      "site": "00901da0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00901d84",
      "incomplete_value": true,
      "site": "00901da0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00901da4",
      "incomplete_value": true,
      "site": "00901dc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00901da4",
      "incomplete_value": true,
      "site": "00901dc0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00901d60",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00901d84",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00901da4",
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
      "00901d60",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00901d84",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00901da4",
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

- 旧版 [`00901d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901d24.md#insn-00901d50) · [`00901d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901d24.md#insn-00901d58)
- 新版 `00901d50`（命令位置の公開資料なし） · `00901d58`（命令位置の公開資料なし）

~~~diff
- 00901d50 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00901d50 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00901d50 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00901d50 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00901d50 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 00901d50 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00901d50 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00901d50 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00901d50 bytes 73621e91
+ 00901d50 bytes 73622191
- 00901d58 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00901d58 bytes 29cdffd0
+ 00901d58 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00901d58 bytes 29cdffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e8195712d0e1e86310b3c899befc281"></a>

### [`009020e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00902/009020e4.md) → [`009020e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00902/009020e4.md) FUN_009020e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 21件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.06% / 新版 96.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00902128",
      "incomplete_value": false,
      "site": "00902134",
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
      "definition_site": "00902128",
      "incomplete_value": false,
      "site": "00902134",
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
      "definition_site": "00902148",
      "incomplete_value": true,
      "site": "00902164",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00902148",
      "incomplete_value": true,
      "site": "00902164",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:eb9:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00902878",
      "incomplete_value": true,
      "site": "00902888",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00902878",
      "incomplete_value": true,
      "site": "00902888",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a7b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 111,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00902134",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00902148",
      "READ",
      [
        "storage",
        "00292eb9",
        null,
        "string"
      ]
    ],
    [
      "009022d8",
      "READ",
      [
        "storage",
        "002a5a42",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00902134",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00902148",
      "READ",
      [
        "storage",
        "00292f46",
        null,
        "string"
      ]
    ],
    [
      "009022d8",
      "READ",
      [
        "storage",
        "002a5a3b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00902128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00902/009020e4.md#insn-00902128) · [`0090213c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00902/009020e4.md#insn-0090213c)
- 新版 `00902128`（命令位置の公開資料なし） · `0090213c`（命令位置の公開資料なし）

~~~diff
- 00902128 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00902128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00902128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00902128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00902128 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00902128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00902128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00902128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00902128 bytes 08e13191
+ 00902128 bytes 08a13491
- 0090213c ["COPY", "register:4048:8", ["const:292000:8"]]
- 0090213c bytes 89ccff90
+ 0090213c ["COPY", "register:4048:8", ["const:292000:8"]]
+ 0090213c bytes 89ccff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8a7cdb67bbfddfdeb8a83385f969760"></a>

### [`00904150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00904/00904150.md) → [`00904150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00904/00904150.md) _INIT_182

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009041b0",
      "incomplete_value": true,
      "site": "009041cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009041b0",
      "incomplete_value": true,
      "site": "009041cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009041d0",
      "incomplete_value": true,
      "site": "009041ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009041d0",
      "incomplete_value": true,
      "site": "009041ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009041f0",
      "incomplete_value": true,
      "site": "00904208",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009041f0",
      "incomplete_value": true,
      "site": "00904208",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0090418c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "009041b0",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "009041d0",
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
      "0090418c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "009041b0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "009041d0",
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

- 旧版 [`0090417c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00904/00904150.md#insn-0090417c) · [`00904184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00904/00904150.md#insn-00904184)
- 新版 `0090417c`（命令位置の公開資料なし） · `00904184`（命令位置の公開資料なし）

~~~diff
- 0090417c ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 0090417c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0090417c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0090417c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0090417c ["COPY", "tmp:0:8", ["const:870:8"]]
+ 0090417c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0090417c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0090417c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0090417c bytes 73c21e91
+ 0090417c bytes 73c22191
- 00904184 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00904184 bytes 09cdfff0
+ 00904184 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00904184 bytes 09cdfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56c294fc1aef4d3c2cb6515faf665752"></a>

### [`009044e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00904/009044e0.md) → [`009044e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00904/009044e0.md) FUN_009044e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 20件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 20件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.12% / 新版 98.12%

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
      "definition_site": "00904524",
      "incomplete_value": false,
      "site": "00904530",
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
      "definition_site": "00904524",
      "incomplete_value": false,
      "site": "00904530",
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
      "definition_site": "00904544",
      "incomplete_value": true,
      "site": "0090455c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b22:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00904544",
      "incomplete_value": true,
      "site": "0090455c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a95:8"
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
      "definition_site": "00904560",
      "incomplete_value": true,
      "site": "00904560",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00904560",
      "incomplete_value": true,
      "site": "00904560",
      "value": [
        "LOAD",
        "8",
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
      "00904530",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00904544",
      "READ",
      [
        "storage",
        "0029ca95",
        null,
        "string"
      ]
    ],
    [
      "0090454c",
      "READ",
      [
        "storage",
        "0029caa2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00904530",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00904544",
      "READ",
      [
        "storage",
        "0029cb22",
        null,
        "string"
      ]
    ],
    [
      "0090454c",
      "READ",
      [
        "storage",
        "0029cb2f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00904524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00904/009044e0.md#insn-00904524) · [`00904540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00904/009044e0.md#insn-00904540) · [`009046b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00904/009044e0.md#insn-009046b8)
- 新版 `00904524`（命令位置の公開資料なし） · `00904540`（命令位置の公開資料なし） · `009046b8`（命令位置の公開資料なし）

~~~diff
- 00904524 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00904524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00904524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00904524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00904524 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00904524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00904524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00904524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00904524 bytes 08e13191
+ 00904524 bytes 08a13491
- 00904540 ["COPY", "tmp:0:8", ["const:a95:8"]]
- 00904540 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00904540 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00904540 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00904540 ["COPY", "tmp:0:8", ["const:b22:8"]]
+ 00904540 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00904540 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00904540 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00904540 bytes 29552a91
+ 00904540 bytes 29892c91
- 009046b8 ["COPY", "tmp:0:8", ["const:bb9:8"]]
- 009046b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009046b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009046b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009046b8 ["COPY", "tmp:0:8", ["const:c46:8"]]
+ 009046b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009046b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009046b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009046b8 bytes 4ae52e91
+ 009046b8 bytes 4a193191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92e3d7d073974fc53554012046b2fa3c"></a>

### [`00906b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md) → [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) FUN_00906b9c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0086b704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md) · 呼出先 51件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md)
- 新版 呼出元 1件 [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 51件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.51% / 新版 97.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_value` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00906c3c",
      "incomplete_value": true,
      "site": "00906c58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00906c3c",
      "incomplete_value": true,
      "site": "00906c58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:aab:8"
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
      "definition_site": "00906c5c",
      "incomplete_value": true,
      "site": "00906c5c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00906c5c",
      "incomplete_value": true,
      "site": "00906c5c",
      "value": [
        "LOAD",
        "8",
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00906f9c",
      "incomplete_value": true,
      "site": "00906fac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a29:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00906f9c",
      "incomplete_value": true,
      "site": "00906fac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:99c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00906c3c",
      "READ",
      [
        "storage",
        "0029caab",
        null,
        "string"
      ]
    ],
    [
      "00906c40",
      "READ",
      [
        "storage",
        "0029cab8",
        null,
        "string"
      ]
    ],
    [
      "00906e38",
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
      "00906c3c",
      "READ",
      [
        "storage",
        "0029cb38",
        null,
        "string"
      ]
    ],
    [
      "00906c40",
      "READ",
      [
        "storage",
        "0029cb45",
        null,
        "string"
      ]
    ],
    [
      "00906e38",
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

- 旧版 [`00906c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md#insn-00906c2c) · [`00906cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md#insn-00906cf4) · [`00906e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md#insn-00906e38)
- 新版 `00906c2c`（命令位置の公開資料なし） · `00906cf4`（命令位置の公開資料なし） · `00906e38`（命令位置の公開資料なし）

~~~diff
- 00906c2c ["COPY", "tmp:0:8", ["const:aab:8"]]
- 00906c2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00906c2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00906c2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00906c2c ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 00906c2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00906c2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00906c2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00906c2c bytes 29ad2a91
+ 00906c2c bytes 29e12c91
- 00906cf4 ["COPY", "tmp:0:8", ["const:1cf:8"]]
- 00906cf4 ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
- 00906cf4 ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
- 00906cf4 ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
+ 00906cf4 ["COPY", "tmp:0:8", ["const:25c:8"]]
+ 00906cf4 ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
+ 00906cf4 ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
+ 00906cf4 ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
- 00906cf4 bytes 7b3f0791
+ 00906cf4 bytes 7b730991
- 00906e38 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 00906e38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00906e38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00906e38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00906e38 ["COPY", "tmp:0:8", ["const:866:8"]]
+ 00906e38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00906e38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00906e38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00906e38 bytes 21641f91
+ 00906e38 bytes 21982191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0c17e68b30de10bc47cdea8d33422d7"></a>

### [`0090a308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090a/0090a308.md) → [`0090a308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090a/0090a308.md) FUN_0090a308

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0090a130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090a/0090a130.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0090a130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090a/0090a130.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0090a314",
      "incomplete_value": false,
      "site": "0090a318",
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
      "definition_site": "0090a314",
      "incomplete_value": false,
      "site": "0090a318",
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
      "0090a314",
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
      "0090a314",
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

- 旧版 [`0090a314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090a/0090a308.md#insn-0090a314)
- 新版 `0090a314`（命令位置の公開資料なし）

~~~diff
- 0090a314 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0090a314 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0090a314 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0090a314 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0090a314 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0090a314 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0090a314 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0090a314 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0090a314 bytes 00280c91
+ 0090a314 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8eaf263ab3d03b2c62e08be911d647e"></a>

### [`0090f6f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090f/0090f6f4.md) → [`0090f6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f6f4.md) FUN_0090f6f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0090f700",
      "incomplete_value": false,
      "site": "0090f704",
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
      "definition_site": "0090f700",
      "incomplete_value": false,
      "site": "0090f704",
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
      "0090f700",
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
      "0090f700",
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

- 旧版 [`0090f700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090f/0090f6f4.md#insn-0090f700)
- 新版 `0090f700`（命令位置の公開資料なし）

~~~diff
- 0090f700 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0090f700 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0090f700 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0090f700 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0090f700 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0090f700 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0090f700 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0090f700 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0090f700 bytes 00280c91
+ 0090f700 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49b4465620fc6a818eed556182789b2e"></a>

### [`0090f708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090f/0090f708.md) → [`0090f708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f708.md) FUN_0090f708

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00906b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md) [`0090f708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090f/0090f708.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) [`0090f708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f708.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

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
      "definition_site": "0090f860",
      "incomplete_value": true,
      "site": "0090f868",
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
            "const:30a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0090f860",
      "incomplete_value": true,
      "site": "0090f868",
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
      "definition_site": "0090f9b8",
      "incomplete_value": false,
      "site": "0090f9c0",
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
      "definition_site": "0090f9b8",
      "incomplete_value": false,
      "site": "0090f9c0",
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
      "definition_site": "0090fa60",
      "incomplete_value": false,
      "site": "0090fa6c",
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
      "definition_site": "0090fa60",
      "incomplete_value": false,
      "site": "0090fa6c",
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
      "0090f860",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0090f9b8",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0090fa60",
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
      "0090f860",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0090f9b8",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0090fa60",
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

- 旧版 [`0090f860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090f/0090f708.md#insn-0090f860) · [`0090f9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090f/0090f708.md#insn-0090f9b8) · [`0090fa60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090f/0090f708.md#insn-0090fa60)
- 新版 `0090f860`（命令位置の公開資料なし） · `0090f9b8`（命令位置の公開資料なし） · `0090fa60`（命令位置の公開資料なし）

~~~diff
- 0090f860 ["COPY", "tmp:0:8", ["const:311:8"]]
- 0090f860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0090f860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0090f860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0090f860 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0090f860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0090f860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0090f860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0090f860 bytes 21440c91
+ 0090f860 bytes 21280c91
- 0090f9b8 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0090f9b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0090f9b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0090f9b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0090f9b8 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0090f9b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0090f9b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0090f9b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0090f9b8 bytes 21d40b91
+ 0090f9b8 bytes 21b80b91
- 0090fa60 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 0090fa60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0090fa60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0090fa60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0090fa60 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 0090fa60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0090fa60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0090fa60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0090fa60 bytes 21681f91
+ 0090fa60 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aaede67ec9675ef76d336b9d3a27972"></a>

### [`009101cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00910/009101cc.md) → [`009101cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00910/009101cc.md) FUN_009101cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "009101d8",
      "incomplete_value": false,
      "site": "009101dc",
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
      "definition_site": "009101d8",
      "incomplete_value": false,
      "site": "009101dc",
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
      "009101d8",
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
      "009101d8",
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

- 旧版 [`009101d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00910/009101cc.md#insn-009101d8)
- 新版 `009101d8`（命令位置の公開資料なし）

~~~diff
- 009101d8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 009101d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009101d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009101d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009101d8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 009101d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009101d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009101d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009101d8 bytes 00280c91
+ 009101d8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ffb9cccd729950c8c793a69cb37fe4b"></a>

### [`00911e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00911/00911e34.md) → [`00911e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00911/00911e34.md) _INIT_183

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
      "definition_site": "00911e70",
      "incomplete_value": true,
      "site": "00911e8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00911e70",
      "incomplete_value": true,
      "site": "00911e8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00911e94",
      "incomplete_value": true,
      "site": "00911eb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00911e94",
      "incomplete_value": true,
      "site": "00911eb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00911eb4",
      "incomplete_value": true,
      "site": "00911ed0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00911eb4",
      "incomplete_value": true,
      "site": "00911ed0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00911e70",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00911e94",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00911eb4",
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
      "00911e70",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00911e94",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00911eb4",
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

- 旧版 [`00911e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00911/00911e34.md#insn-00911e60) · [`00911e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00911/00911e34.md#insn-00911e68)
- 新版 `00911e60`（命令位置の公開資料なし） · `00911e68`（命令位置の公開資料なし）

~~~diff
- 00911e60 ["COPY", "tmp:0:8", ["const:7c8:8"]]
- 00911e60 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00911e60 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00911e60 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00911e60 ["COPY", "tmp:0:8", ["const:888:8"]]
+ 00911e60 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00911e60 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00911e60 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00911e60 bytes 73221f91
+ 00911e60 bytes 73222291
- 00911e68 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00911e68 bytes a9ccffd0
+ 00911e68 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00911e68 bytes a9ccffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5c519381b8e24bd7235d44bf31a1976"></a>

### [`0092bc08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0092b/0092bc08.md) → [`0092bc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092b/0092bc08.md) FUN_0092bc08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 25件 [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`005a7c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a7c94.md) [`005dfeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005df/005dfeb0.md) [`0063e6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063e6d4.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`005a7c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7c94.md) [`005dfeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005df/005dfeb0.md) [`0063e6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e6d4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.74% / 新版 97.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 14件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0092c71c",
      "incomplete_value": false,
      "site": "0092c71c",
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
      "definition_site": "0092c71c",
      "incomplete_value": false,
      "site": "0092c71c",
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
    "ordinal": 38,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0092c720",
      "incomplete_value": false,
      "site": "0092c720",
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
      "definition_site": "0092c720",
      "incomplete_value": false,
      "site": "0092c720",
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
    "ordinal": 39,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0092c71c",
      "incomplete_value": false,
      "site": "0092c720",
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
      "definition_site": "0092c71c",
      "incomplete_value": false,
      "site": "0092c720",
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
    "ordinal": 39,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0092c464",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "0092c484",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      "0092c4f8",
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
      "0092c464",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0092c484",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "0092c4f8",
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

- 旧版 [`0092c458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0092b/0092bc08.md#insn-0092c458) · [`0092c45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0092b/0092bc08.md#insn-0092c45c) · [`0092c480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0092b/0092bc08.md#insn-0092c480)
- 新版 `0092c458`（命令位置の公開資料なし） · `0092c45c`（命令位置の公開資料なし） · `0092c480`（命令位置の公開資料なし）

~~~diff
- 0092c458 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0092c458 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 0092c458 bytes c8170090
+ 0092c458 bytes c81700b0
- 0092c45c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0092c45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0092c45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0092c45c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0092c45c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0092c45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0092c45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0092c45c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0092c45c bytes 08e13d91
+ 0092c45c bytes 08e10091
- 0092c480 ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 0092c480 ["COPY", "register:4000:8", ["const:c25000:8"]]
- 0092c480 bytes c0170090
+ 0092c480 bytes c01700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28a663bd3984b820d1722fe675715777"></a>

### [`00938cc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00938/00938cc0.md) → [`00938cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00938/00938cc0.md) FUN_00938cc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `boundary_candidate`

- 旧版 呼出元 0件  · 呼出先 4件 [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00827b94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827b94.md) [`009a6f44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009a6/009a6f44.md) [`00ace4cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ace/00ace4cc.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00827b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827b94.md) [`009a6f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a6/009a6f44.md) [`00ace594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ace/00ace594.md)

変更の種類 branch_condition_or_target, branch_count, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.91% / 新版 72.29%

CFGの説明率　旧版 88.89% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 1件, `call_count` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0093795c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00938d30",
      "value": [
        "leaf",
        "ram:ace594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00938d30",
      "value": [
        "leaf",
        "ram:ace4cc:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00938db4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00938d30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace4cc"
      ]
    ],
    [
      "unmatched:00938db4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace4cc"
      ]
    ],
    [
      "unmatched:00938dbc",
      "READ",
      [
        "storage",
        "Stack[0x88]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00937968",
      "READ",
      [
        "storage",
        "Stack[0x78]",
        null,
        null
      ]
    ],
    [
      "00937988",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00446d2c"
      ]
    ],
    [
      "0093798c",
      "UNCONDITIONAL_JUMP",
      [
        "unresolved_target",
        "0092ef94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00938d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00938/00938cc0.md#insn-00938d30)
- 新版 `0093795c`（命令位置の公開資料なし） · `00937988`（命令位置の公開資料なし） · `00938d30`（命令位置の公開資料なし）

~~~diff
+ 0093795c ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 0093795c ["CBRANCH", null, ["const:2:4", "register:100:1"]]
+ 0093795c ["INT_2COMP", "tmp:0:4", ["register:4048:4"]]
+ 0093795c ["INT_ZEXT", "register:4040:8", ["tmp:0:4"]]
+ 0093795c bytes 0845895a
+ 00937988 ["INT_ADD", "register:40f0:8", ["const:937988:8", "const:4:8"]]
+ 00937988 ["CALL", null, ["callee:00446d2c:8"]]
+ 00937988 bytes e93cec97
- 00938d30 ["INT_ADD", "register:40f0:8", ["const:938d30:8", "const:4:8"]]
- 00938d30 ["CALL", null, ["ram:ace4cc:8"]]
+ 00938d30 ["INT_ADD", "register:40f0:8", ["const:938d30:8", "const:4:8"]]
+ 00938d30 ["CALL", null, ["ram:ace594:8"]]
- 00938d30 bytes e7550694
+ 00938d30 bytes 19560694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-258e7cc92fef215e8e39127fcb511acd"></a>

### [`0093f290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0093f/0093f290.md) → [`0093f290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0093f/0093f290.md) FUN_0093f290

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0092e43c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0092e/0092e43c.md) · 呼出先 1件 [`00ace4cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ace/00ace4cc.md)
- 新版 呼出元 1件 [`0092e43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092e/0092e43c.md) · 呼出先 1件 [`00ace594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ace/00ace594.md)

変更の種類 call, call_target, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0093f298",
      "value": [
        "leaf",
        "ram:ace594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0093f298",
      "value": [
        "leaf",
        "ram:ace4cc:8"
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
      "0093f298",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace4cc"
      ]
    ]
  ],
  "added": [
    [
      "0093f298",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace594"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0093f298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0093f/0093f290.md#insn-0093f298)
- 新版 `0093f298`（命令位置の公開資料なし）

~~~diff
- 0093f298 ["INT_ADD", "register:40f0:8", ["const:93f298:8", "const:4:8"]]
- 0093f298 ["CALL", null, ["ram:ace4cc:8"]]
+ 0093f298 ["INT_ADD", "register:40f0:8", ["const:93f298:8", "const:4:8"]]
+ 0093f298 ["CALL", null, ["ram:ace594:8"]]
- 0093f298 bytes 8d3c0694
+ 0093f298 bytes bf3c0694
~~~


<a id="compare-7d9efe783dd0b286b6b62da1a54ee176"></a>

### [`0093f2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0093f/0093f2dc.md) → [`0093f2dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0093f/0093f2dc.md) FUN_0093f2dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0093249c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00932/0093249c.md) · 呼出先 3件 [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00ace4cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ace/00ace4cc.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`0093249c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00932/0093249c.md) · 呼出先 3件 [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00ace594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ace/00ace594.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call, call_target, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0093f2e4",
      "value": [
        "leaf",
        "ram:ace594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0093f2e4",
      "value": [
        "leaf",
        "ram:ace4cc:8"
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
      "0093f2e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace4cc"
      ]
    ]
  ],
  "added": [
    [
      "0093f2e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace594"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0093f2e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0093f/0093f2dc.md#insn-0093f2e4)
- 新版 `0093f2e4`（命令位置の公開資料なし）

~~~diff
- 0093f2e4 ["INT_ADD", "register:40f0:8", ["const:93f2e4:8", "const:4:8"]]
- 0093f2e4 ["CALL", null, ["ram:ace4cc:8"]]
+ 0093f2e4 ["INT_ADD", "register:40f0:8", ["const:93f2e4:8", "const:4:8"]]
+ 0093f2e4 ["CALL", null, ["ram:ace594:8"]]
- 0093f2e4 bytes 7a3c0694
+ 0093f2e4 bytes ac3c0694
~~~


<a id="compare-9d16a1a7cc4401f81dd99162c4b86044"></a>

### [`009428a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00942/009428a4.md) → [`009428a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/009428a4.md) FUN_009428a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00942564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00942/00942564.md) [`009428a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00942/009428a4.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00942564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/00942564.md) [`009428a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/009428a4.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.45% / 新版 99.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00942a38",
      "incomplete_value": false,
      "site": "00942a40",
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
      "definition_site": "00942a38",
      "incomplete_value": false,
      "site": "00942a40",
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
      "definition_site": "00942af0",
      "incomplete_value": false,
      "site": "00942af8",
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
      "definition_site": "00942af0",
      "incomplete_value": false,
      "site": "00942af8",
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
      "definition_site": "00943208",
      "incomplete_value": false,
      "site": "00943214",
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
      "definition_site": "00943208",
      "incomplete_value": false,
      "site": "00943214",
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
    "ordinal": 47,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00942a38",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00942af0",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00942f50",
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
      "00942a38",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00942af0",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00942f50",
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

- 旧版 [`00942a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00942/009428a4.md#insn-00942a38) · [`00942af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00942/009428a4.md#insn-00942af0) · [`00942f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00942/009428a4.md#insn-00942f50)
- 新版 `00942a38`（命令位置の公開資料なし） · `00942af0`（命令位置の公開資料なし） · `00942f50`（命令位置の公開資料なし）

~~~diff
- 00942a38 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00942a38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00942a38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00942a38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00942a38 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00942a38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00942a38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00942a38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00942a38 bytes 21440c91
+ 00942a38 bytes 21280c91
- 00942af0 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00942af0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00942af0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00942af0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00942af0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00942af0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00942af0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00942af0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00942af0 bytes 21d40b91
+ 00942af0 bytes 21b80b91
- 00942f50 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 00942f50 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00942f50 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00942f50 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00942f50 ["COPY", "tmp:0:8", ["const:672:8"]]
+ 00942f50 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00942f50 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00942f50 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00942f50 bytes 63941791
+ 00942f50 bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23b063599abb8ee7786c334205625ee4"></a>

### [`00943aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00943/00943aa0.md) → [`00943aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00943/00943aa0.md) FUN_00943aa0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009428a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00942/009428a4.md) [`00943aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00943/00943aa0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`009428a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/009428a4.md) [`00943aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00943/00943aa0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.40% / 新版 99.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00943c28",
      "incomplete_value": false,
      "site": "00943c30",
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
      "definition_site": "00943c28",
      "incomplete_value": false,
      "site": "00943c30",
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
      "definition_site": "00943ce0",
      "incomplete_value": false,
      "site": "00943ce8",
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
      "definition_site": "00943ce0",
      "incomplete_value": false,
      "site": "00943ce8",
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
      "definition_site": "009440f8",
      "incomplete_value": false,
      "site": "00944108",
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
      "definition_site": "009440f8",
      "incomplete_value": false,
      "site": "00944108",
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
      "00943c28",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00943ce0",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "009440f8",
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
      "00943c28",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00943ce0",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "009440f8",
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

- 旧版 [`00943c28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00943/00943aa0.md#insn-00943c28) · [`00943ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00943/00943aa0.md#insn-00943ce0) · [`009440f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00943/00943aa0.md#insn-009440f8)
- 新版 `00943c28`（命令位置の公開資料なし） · `00943ce0`（命令位置の公開資料なし） · `009440f8`（命令位置の公開資料なし）

~~~diff
- 00943c28 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00943c28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00943c28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00943c28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00943c28 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00943c28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00943c28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00943c28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00943c28 bytes 21440c91
+ 00943c28 bytes 21280c91
- 00943ce0 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00943ce0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00943ce0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00943ce0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00943ce0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00943ce0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00943ce0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00943ce0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00943ce0 bytes 21d40b91
+ 00943ce0 bytes 21b80b91
- 009440f8 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 009440f8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 009440f8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 009440f8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 009440f8 ["COPY", "tmp:0:8", ["const:672:8"]]
+ 009440f8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 009440f8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 009440f8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 009440f8 bytes 63941791
+ 009440f8 bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55f7cc59787cb268e5ac78a441e6a0d0"></a>

### [`00944ab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00944/00944ab4.md) → [`00944ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00944/00944ab4.md) FUN_00944ab4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00943aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00943/00943aa0.md) [`00944ab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00944/00944ab4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00943aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00943/00943aa0.md) [`00944ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00944/00944ab4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.38% / 新版 99.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00944c20",
      "incomplete_value": false,
      "site": "00944c28",
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
      "definition_site": "00944c20",
      "incomplete_value": false,
      "site": "00944c28",
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
      "definition_site": "00944db0",
      "incomplete_value": false,
      "site": "00944db8",
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
      "definition_site": "00944db0",
      "incomplete_value": false,
      "site": "00944db8",
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
      "definition_site": "00944e88",
      "incomplete_value": false,
      "site": "00944e94",
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
      "definition_site": "00944e88",
      "incomplete_value": false,
      "site": "00944e94",
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
      "00944c20",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00944db0",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00944e88",
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
      "00944c20",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00944db0",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00944e88",
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

- 旧版 [`00944c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00944/00944ab4.md#insn-00944c20) · [`00944db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00944/00944ab4.md#insn-00944db0) · [`00944e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00944/00944ab4.md#insn-00944e88)
- 新版 `00944c20`（命令位置の公開資料なし） · `00944db0`（命令位置の公開資料なし） · `00944e88`（命令位置の公開資料なし）

~~~diff
- 00944c20 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00944c20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00944c20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00944c20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00944c20 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00944c20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00944c20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00944c20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00944c20 bytes 21440c91
+ 00944c20 bytes 21280c91
- 00944db0 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00944db0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00944db0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00944db0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00944db0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00944db0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00944db0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00944db0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00944db0 bytes 21d40b91
+ 00944db0 bytes 21b80b91
- 00944e88 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00944e88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00944e88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00944e88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00944e88 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00944e88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00944e88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00944e88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00944e88 bytes 21681f91
+ 00944e88 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23865d3c504fa5ea592e57945c2b17f2"></a>

### [`00945a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00945/00945a50.md) → [`00945a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00945/00945a50.md) FUN_00945a50

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00944ab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00944/00944ab4.md) [`00945a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00945/00945a50.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00944ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00944/00944ab4.md) [`00945a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00945/00945a50.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.33% / 新版 99.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00945bc8",
      "incomplete_value": false,
      "site": "00945bd0",
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
      "definition_site": "00945bc8",
      "incomplete_value": false,
      "site": "00945bd0",
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
      "definition_site": "00945c80",
      "incomplete_value": false,
      "site": "00945c88",
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
      "definition_site": "00945c80",
      "incomplete_value": false,
      "site": "00945c88",
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
      "definition_site": "00946044",
      "incomplete_value": false,
      "site": "00946054",
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
      "definition_site": "00946044",
      "incomplete_value": false,
      "site": "00946054",
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
    "ordinal": 24,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00945bc8",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00945c80",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00946044",
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
      "00945bc8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00945c80",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00946044",
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

- 旧版 [`00945bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00945/00945a50.md#insn-00945bc8) · [`00945c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00945/00945a50.md#insn-00945c80) · [`00946044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00945/00945a50.md#insn-00946044)
- 新版 `00945bc8`（命令位置の公開資料なし） · `00945c80`（命令位置の公開資料なし） · `00946044`（命令位置の公開資料なし）

~~~diff
- 00945bc8 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00945bc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00945bc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00945bc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00945bc8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00945bc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00945bc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00945bc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00945bc8 bytes 21440c91
+ 00945bc8 bytes 21280c91
- 00945c80 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00945c80 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00945c80 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00945c80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00945c80 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00945c80 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00945c80 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00945c80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00945c80 bytes 21d40b91
+ 00945c80 bytes 21b80b91
- 00946044 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 00946044 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00946044 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00946044 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00946044 ["COPY", "tmp:0:8", ["const:672:8"]]
+ 00946044 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00946044 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00946044 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00946044 bytes 63941791
+ 00946044 bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22434228e9d43b330477620ec5e9d05b"></a>

### [`00946864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00946/00946864.md) → [`00946864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00946/00946864.md) FUN_00946864

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00945a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00945/00945a50.md) [`00946864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00946/00946864.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00945a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00945/00945a50.md) [`00946864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00946/00946864.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.27% / 新版 99.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00946bc8",
      "incomplete_value": false,
      "site": "00946bd4",
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
      "definition_site": "00946bc8",
      "incomplete_value": false,
      "site": "00946bd4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0094704c",
      "incomplete_value": false,
      "site": "00947054",
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
      "definition_site": "0094704c",
      "incomplete_value": false,
      "site": "00947054",
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
      "009469c8",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00946b20",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00946bc8",
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
      "009469c8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00946b20",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00946bc8",
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

- 旧版 [`009469c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00946/00946864.md#insn-009469c8) · [`00946b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00946/00946864.md#insn-00946b20) · [`00946bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00946/00946864.md#insn-00946bc8)
- 新版 `009469c8`（命令位置の公開資料なし） · `00946b20`（命令位置の公開資料なし） · `00946bc8`（命令位置の公開資料なし）

~~~diff
- 009469c8 ["COPY", "tmp:0:8", ["const:311:8"]]
- 009469c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009469c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009469c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009469c8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 009469c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009469c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009469c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009469c8 bytes 21440c91
+ 009469c8 bytes 21280c91
- 00946b20 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00946b20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00946b20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00946b20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00946b20 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00946b20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00946b20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00946b20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00946b20 bytes 21d40b91
+ 00946b20 bytes 21b80b91
- 00946bc8 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00946bc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00946bc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00946bc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00946bc8 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00946bc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00946bc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00946bc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00946bc8 bytes 21681f91
+ 00946bc8 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c14642e016d85e4c7a8cff4bd7c9e87"></a>

### [`0094757c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/0094757c.md) → [`0094757c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/0094757c.md) FUN_0094757c

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
      "definition_site": "00947590",
      "incomplete_value": false,
      "site": "00947594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947590",
      "incomplete_value": false,
      "site": "00947594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:910:8"
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
      "00947594",
      "DATA",
      [
        "storage",
        "00c09910",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00947594",
      "DATA",
      [
        "storage",
        "00c099c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00947590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/0094757c.md#insn-00947590)
- 新版 `00947590`（命令位置の公開資料なし）

~~~diff
- 00947590 ["COPY", "tmp:0:8", ["const:910:8"]]
- 00947590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00947590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00947590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00947590 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00947590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00947590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00947590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00947590 bytes 08412491
+ 00947590 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-487a243d345fd1e1d6c2f1c3c8c2e9a1"></a>

### [`0094762c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/0094762c.md) → [`0094762c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/0094762c.md) FUN_0094762c

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
      "definition_site": "0094764c",
      "incomplete_value": false,
      "site": "00947650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094764c",
      "incomplete_value": false,
      "site": "00947650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "00947650",
      "DATA",
      [
        "storage",
        "00c09990",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00947650",
      "DATA",
      [
        "storage",
        "00c09a40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0094764c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/0094762c.md#insn-0094764c)
- 新版 `0094764c`（命令位置の公開資料なし）

~~~diff
- 0094764c ["COPY", "tmp:0:8", ["const:990:8"]]
- 0094764c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0094764c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0094764c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0094764c ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 0094764c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0094764c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0094764c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0094764c bytes 08412691
+ 0094764c bytes 08012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01241eae7c54767e821f5ed4afb1902a"></a>

### [`00947684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947684.md) → [`00947684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947684.md) FUN_00947684

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046ff30.md) [`0065ec80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065e/0065ec80.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`0065ec80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ec80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094771c",
      "incomplete_value": true,
      "site": "0094772c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:976:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094771c",
      "incomplete_value": true,
      "site": "0094772c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:97d:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00947774",
      "incomplete_value": false,
      "site": "00947774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947774",
      "incomplete_value": false,
      "site": "00947774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "0094771c",
      "READ",
      [
        "storage",
        "002a297d",
        null,
        "string"
      ]
    ],
    [
      "00947774",
      "DATA",
      [
        "storage",
        "00c09a00",
        null,
        "undefined *"
      ]
    ],
    [
      "009477cc",
      "READ",
      [
        "storage",
        "00c09a20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0094771c",
      "READ",
      [
        "storage",
        "002a2976",
        null,
        "string"
      ]
    ],
    [
      "00947774",
      "DATA",
      [
        "storage",
        "00c09ab0",
        null,
        "undefined *"
      ]
    ],
    [
      "009477cc",
      "READ",
      [
        "storage",
        "00c09ad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00947714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947684.md#insn-00947714) · [`0094776c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947684.md#insn-0094776c) · [`00947770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947684.md#insn-00947770)
- 新版 `00947714`（命令位置の公開資料なし） · `0094776c`（命令位置の公開資料なし）

~~~diff
- 00947714 ["COPY", "tmp:0:8", ["const:97d:8"]]
- 00947714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00947714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00947714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00947714 ["COPY", "tmp:0:8", ["const:976:8"]]
+ 00947714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00947714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00947714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00947714 bytes 29f52591
+ 00947714 bytes 29d92591
- 0094776c ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0094776c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0094776c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0094776c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0094776c ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 0094776c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0094776c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0094776c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0094776c bytes 08012891
+ 0094776c bytes 08c12a91
- 00947770 ["INT_SUB", "register:40a0:8", ["register:40e8:8", "const:40:8"]]
- 00947770 bytes b40301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca60ffa5fbd7da61dde0432cda1ba74a"></a>

### [`00947964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947964.md) → [`00947964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947964.md) FUN_00947964

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
      "definition_site": "00947988",
      "incomplete_value": false,
      "site": "00947988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947988",
      "incomplete_value": false,
      "site": "00947988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "00947988",
      "DATA",
      [
        "storage",
        "00c09a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00947988",
      "DATA",
      [
        "storage",
        "00c09ab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00947984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947964.md#insn-00947984)
- 新版 `00947984`（命令位置の公開資料なし）

~~~diff
- 00947984 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00947984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00947984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00947984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00947984 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 00947984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00947984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00947984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00947984 bytes 08012891
+ 00947984 bytes 08c12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c879a8ee5aa8fa21b7efee6829b0c87c"></a>

### [`00947998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947998.md) → [`00947998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947998.md) FUN_00947998

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
      "definition_site": "009479a4",
      "incomplete_value": false,
      "site": "009479a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009479a4",
      "incomplete_value": false,
      "site": "009479a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "009479a4",
      "DATA",
      [
        "storage",
        "00c09a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009479a4",
      "DATA",
      [
        "storage",
        "00c09ab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009479a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947998.md#insn-009479a0)
- 新版 `009479a0`（命令位置の公開資料なし）

~~~diff
- 009479a0 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 009479a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009479a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009479a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009479a0 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 009479a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009479a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009479a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009479a0 bytes 29012891
+ 009479a0 bytes 29c12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1f5a1617531bede0089ab5d48582e31"></a>

### [`00947c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947c00.md) → [`00947c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947c00.md) FUN_00947c00

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
      "definition_site": "00947c14",
      "incomplete_value": false,
      "site": "00947c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947c14",
      "incomplete_value": false,
      "site": "00947c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "00947c18",
      "DATA",
      [
        "storage",
        "00c09a90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00947c18",
      "DATA",
      [
        "storage",
        "00c09b40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00947c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947c00.md#insn-00947c14)
- 新版 `00947c14`（命令位置の公開資料なし）

~~~diff
- 00947c14 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00947c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00947c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00947c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00947c14 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 00947c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00947c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00947c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00947c14 bytes 08412a91
+ 00947c14 bytes 08012d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-059d85713a2db812561f267baeaa9012"></a>

### [`00947d34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947d34.md) → [`00947d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947d34.md) FUN_00947d34

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00947d48",
      "incomplete_value": true,
      "site": "00947d4c",
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
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947d48",
      "incomplete_value": true,
      "site": "00947d4c",
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
            "const:b10:8"
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
      "00947d4c",
      "DATA",
      [
        "storage",
        "00c09b10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00947d4c",
      "DATA",
      [
        "storage",
        "00c09bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00947d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947d34.md#insn-00947d48)
- 新版 `00947d48`（命令位置の公開資料なし）

~~~diff
- 00947d48 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 00947d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00947d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00947d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00947d48 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00947d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00947d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00947d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00947d48 bytes 08412c91
+ 00947d48 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-988b0efacef5bede8f8cce74887e3ee1"></a>

### [`00948440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948440.md) → [`00948440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948440.md) FUN_00948440

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
      "definition_site": "00948454",
      "incomplete_value": false,
      "site": "00948458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00948454",
      "incomplete_value": false,
      "site": "00948458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "00948458",
      "DATA",
      [
        "storage",
        "00c09b90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00948458",
      "DATA",
      [
        "storage",
        "00c09c40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00948454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948440.md#insn-00948454)
- 新版 `00948454`（命令位置の公開資料なし）

~~~diff
- 00948454 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00948454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00948454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00948454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00948454 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00948454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00948454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00948454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00948454 bytes 08412e91
+ 00948454 bytes 08013191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aaf78fdab4f5ef6aecac2dfbbc8bfe3"></a>

### [`0094847c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/0094847c.md) → [`0094847c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/0094847c.md) FUN_0094847c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044592c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md) [`00447a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447a10.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.43% / 新版 99.43%

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
      "definition_site": "00948884",
      "incomplete_value": true,
      "site": "00948884",
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
      "definition_site": "00948884",
      "incomplete_value": true,
      "site": "00948884",
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
      "definition_site": "0094888c",
      "incomplete_value": false,
      "site": "0094889c",
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
      "definition_site": "0094888c",
      "incomplete_value": false,
      "site": "0094889c",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00948894",
      "incomplete_value": false,
      "site": "0094889c",
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
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00948894",
      "incomplete_value": false,
      "site": "0094889c",
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
            "const:c50:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00948880",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0094888c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00948894",
      "PARAM",
      [
        "storage",
        "00bf3c50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00948880",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0094888c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00948894",
      "PARAM",
      [
        "storage",
        "00bf3d00",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00948880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/0094847c.md#insn-00948880) · [`0094888c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/0094847c.md#insn-0094888c) · [`00948894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/0094847c.md#insn-00948894)
- 新版 `00948880`（命令位置の公開資料なし） · `0094888c`（命令位置の公開資料なし） · `00948894`（命令位置の公開資料なし）

~~~diff
- 00948880 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00948880 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00948880 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00948880 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00948880 bytes 00dd44f9
+ 00948880 bytes 003d45f9
- 0094888c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0094888c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0094888c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0094888c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0094888c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0094888c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0094888c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0094888c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0094888c bytes 21603691
+ 0094888c bytes 21203991
- 00948894 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00948894 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00948894 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00948894 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00948894 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 00948894 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00948894 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00948894 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00948894 bytes 42403191
+ 00948894 bytes 42003491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1677b07ffd03a1ccec6403c352a83e9"></a>

### [`00948a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948a24.md) → [`00948a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948a24.md) _INIT_184

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00948aa4",
      "incomplete_value": true,
      "site": "00948ac0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00948aa4",
      "incomplete_value": true,
      "site": "00948ac0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00948ac4",
      "incomplete_value": true,
      "site": "00948adc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00948ac4",
      "incomplete_value": true,
      "site": "00948adc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00948ae0",
      "incomplete_value": true,
      "site": "00948afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00948ae0",
      "incomplete_value": true,
      "site": "00948afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00948a60",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00948a84",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00948aa4",
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
      "00948a60",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00948a84",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00948aa4",
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

- 旧版 [`00948a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948a24.md#insn-00948a50) · [`00948a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948a24.md#insn-00948a5c) · [`00948a78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948a24.md#insn-00948a78)
- 新版 `00948a50`（命令位置の公開資料なし） · `00948a5c`（命令位置の公開資料なし） · `00948a78`（命令位置の公開資料なし）

~~~diff
- 00948a50 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 00948a50 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00948a50 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00948a50 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00948a50 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00948a50 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00948a50 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00948a50 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00948a50 bytes 73821f91
+ 00948a50 bytes 73822291
- 00948a5c ["COPY", "tmp:0:8", ["const:2e4:8"]]
- 00948a5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00948a5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00948a5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00948a5c ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 00948a5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00948a5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00948a5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00948a5c bytes 29910b91
+ 00948a5c bytes 29750b91
- 00948a78 ["COPY", "tmp:0:8", ["const:2f7:8"]]
- 00948a78 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00948a78 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00948a78 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00948a78 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 00948a78 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00948a78 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00948a78 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00948a78 bytes 4add0b91
+ 00948a78 bytes 4ac10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2c597f04f3e6a886ca0fc6c30008e5d"></a>

### [`00948db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948db4.md) → [`00948db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948db4.md) FUN_00948db4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00949ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949ed8.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`005748e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/005748e4.md) [`00574bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574bb4.md) [`009496f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/009496f0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00949ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949ed8.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`005748e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005748e4.md) [`00574bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bb4.md) [`009496f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/009496f0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.74% / 新版 97.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009491d0",
      "incomplete_value": true,
      "site": "009491d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "009491d0",
      "incomplete_value": true,
      "site": "009491d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00949328",
      "incomplete_value": true,
      "site": "00949328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00949328",
      "incomplete_value": true,
      "site": "00949328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 68,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009494c4",
      "incomplete_value": true,
      "site": "009494c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009494c4",
      "incomplete_value": true,
      "site": "009494c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:62c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 83,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00948ee8",
      "READ",
      [
        "storage",
        "002abee4",
        null,
        "string"
      ]
    ],
    [
      "00948ff8",
      "READ",
      [
        "storage",
        "002a779e",
        null,
        "string"
      ]
    ],
    [
      "009491c4",
      "READ",
      [
        "storage",
        "002936c1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00948ee8",
      "READ",
      [
        "storage",
        "002abeea",
        null,
        "string"
      ]
    ],
    [
      "00948ff8",
      "READ",
      [
        "storage",
        "002a770a",
        null,
        "string"
      ]
    ],
    [
      "009491c4",
      "READ",
      [
        "storage",
        "0029374e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00948ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948db4.md#insn-00948ee0) · [`00948ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948db4.md#insn-00948ff0) · [`009491b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948db4.md#insn-009491b8)
- 新版 `00948ee0`（命令位置の公開資料なし） · `00948ff0`（命令位置の公開資料なし） · `009491b8`（命令位置の公開資料なし）

~~~diff
- 00948ee0 ["COPY", "tmp:0:8", ["const:ee4:8"]]
- 00948ee0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00948ee0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00948ee0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00948ee0 ["COPY", "tmp:0:8", ["const:eea:8"]]
+ 00948ee0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00948ee0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00948ee0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00948ee0 bytes 29913b91
+ 00948ee0 bytes 29a93b91
- 00948ff0 ["COPY", "tmp:0:8", ["const:79e:8"]]
- 00948ff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00948ff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00948ff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00948ff0 ["COPY", "tmp:0:8", ["const:70a:8"]]
+ 00948ff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00948ff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00948ff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00948ff0 bytes 29791e91
+ 00948ff0 bytes 29291c91
- 009491b8 ["COPY", "tmp:0:8", ["const:6c1:8"]]
- 009491b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009491b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009491b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009491b8 ["COPY", "tmp:0:8", ["const:74e:8"]]
+ 009491b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009491b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009491b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009491b8 bytes 29051b91
+ 009491b8 bytes 29391d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b9ffc53ef68f25835b7f21e0150e921"></a>

### [`00949c4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949c4c.md) → [`00949c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949c4c.md) FUN_00949c4c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00419718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md) · 呼出先 11件 [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`00428cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428cb4.md) [`00428e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428e88.md) [`0053ee5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee5c.md) [`0053f0f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053f/0053f0f8.md)
- 新版 呼出元 1件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) · 呼出先 11件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`00428cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428cb4.md) [`00428e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428e88.md) [`0053ee5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) [`0053f0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f0f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00949d00",
      "incomplete_value": false,
      "site": "00949d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00949d00",
      "incomplete_value": false,
      "site": "00949d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00949cd8",
      "incomplete_value": true,
      "site": "00949ce0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00949cd8",
      "incomplete_value": true,
      "site": "00949ce0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:cd8:8"
              ]
            ]
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
      "00949cd8",
      "READ",
      [
        "storage",
        "00c1acd8",
        null,
        "pointer"
      ]
    ],
    [
      "00949cd8",
      "PARAM",
      [
        "storage",
        "00c25d10",
        null,
        "undefined1"
      ]
    ],
    [
      "00949d00",
      "DATA",
      [
        "storage",
        "00c09c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00949cd8",
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      "00949cd8",
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "00949d00",
      "DATA",
      [
        "storage",
        "00c09cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00949cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949c4c.md#insn-00949cd8) · [`00949cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949c4c.md#insn-00949cf8)
- 新版 `00949cd8`（命令位置の公開資料なし） · `00949cf8`（命令位置の公開資料なし）

~~~diff
- 00949cd8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:cd8:8"]]
- 00949cd8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00949cd8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d88:8"]]
+ 00949cd8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00949cd8 bytes 006c46f9
+ 00949cd8 bytes 00c446f9
- 00949cf8 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 00949cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00949cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00949cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00949cf8 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00949cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00949cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00949cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00949cf8 bytes 08a13091
+ 00949cf8 bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be45b94d686271486680b16af0e07200"></a>

### [`00949ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949ed8.md) → [`00949ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949ed8.md) FUN_00949ed8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0094bc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bc30.md) [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0045e558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045e/0045e558.md) [`0045f0ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045f/0045f0ac.md)
- 新版 呼出元 2件 [`0094bc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc30.md) [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0045e558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md) [`0045f0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f0ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.95% / 新版 97.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00949f44",
      "incomplete_value": true,
      "site": "00949f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00949f44",
      "incomplete_value": true,
      "site": "00949f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7cb:8"
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
      "definition_site": "0094a010",
      "incomplete_value": true,
      "site": "0094a010",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0094a010",
      "incomplete_value": true,
      "site": "0094a010",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094a254",
      "incomplete_value": true,
      "site": "0094a264",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:70a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094a254",
      "incomplete_value": true,
      "site": "0094a264",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:79e:8"
              ]
            ]
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
      "00949f30",
      "READ",
      [
        "storage",
        "002a57cb",
        null,
        "string"
      ]
    ],
    [
      "00949f58",
      "PARAM",
      [
        "storage",
        "002a9253",
        null,
        null
      ]
    ],
    [
      "0094a000",
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
      "00949f30",
      "READ",
      [
        "storage",
        "002a57c4",
        null,
        "string"
      ]
    ],
    [
      "00949f58",
      "PARAM",
      [
        "storage",
        "002a91bf",
        null,
        null
      ]
    ],
    [
      "0094a000",
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

- 旧版 [`00949f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949ed8.md#insn-00949f24) · [`00949f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949ed8.md#insn-00949f58) · [`00949ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949ed8.md#insn-00949ff8)
- 新版 `00949f24`（命令位置の公開資料なし） · `00949f58`（命令位置の公開資料なし） · `00949ff8`（命令位置の公開資料なし）

~~~diff
- 00949f24 ["COPY", "tmp:0:8", ["const:7cb:8"]]
- 00949f24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00949f24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00949f24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00949f24 ["COPY", "tmp:0:8", ["const:7c4:8"]]
+ 00949f24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00949f24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00949f24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00949f24 bytes 292d1f91
+ 00949f24 bytes 29111f91
- 00949f58 ["COPY", "tmp:0:8", ["const:253:8"]]
- 00949f58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00949f58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00949f58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00949f58 ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 00949f58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00949f58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00949f58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00949f58 bytes 214c0991
+ 00949f58 bytes 21fc0691
- 00949ff8 ["COPY", "tmp:0:8", ["const:8c5:8"]]
- 00949ff8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00949ff8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00949ff8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00949ff8 ["COPY", "tmp:0:8", ["const:952:8"]]
+ 00949ff8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00949ff8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00949ff8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00949ff8 bytes 29152391
+ 00949ff8 bytes 29492591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee5df706e20671ce06467bdb0c6c66a1"></a>

### [`0094ac20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094a/0094ac20.md) → [`0094ac20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094a/0094ac20.md) FUN_0094ac20

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00868124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868124.md) [`0094abb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094a/0094abb8.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md) [`0046ad74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046ad74.md) [`0046d7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d7c4.md)
- 新版 呼出元 2件 [`00868124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md) [`0094abb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094a/0094abb8.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`0046ad74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046ad74.md) [`0046d7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046d/0046d7c4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094af80",
      "incomplete_value": true,
      "site": "0094af80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094af80",
      "incomplete_value": true,
      "site": "0094af80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0094af70",
      "READ",
      [
        "storage",
        "002aa4a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0094af70",
      "READ",
      [
        "storage",
        "002aa4a7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0094af68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094a/0094ac20.md#insn-0094af68)
- 新版 `0094af68`（命令位置の公開資料なし）

~~~diff
- 0094af68 ["COPY", "tmp:0:8", ["const:4a1:8"]]
- 0094af68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0094af68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0094af68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0094af68 ["COPY", "tmp:0:8", ["const:4a7:8"]]
+ 0094af68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0094af68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0094af68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0094af68 bytes 29851291
+ 0094af68 bytes 299d1291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afd306c9b70a342a74cbb645f473829f"></a>

### [`0094bbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bbe0.md) → [`0094bbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bbe0.md) FUN_0094bbe0

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
      "definition_site": "0094bc04",
      "incomplete_value": false,
      "site": "0094bc04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094bc04",
      "incomplete_value": false,
      "site": "0094bc04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      "0094bc04",
      "DATA",
      [
        "storage",
        "00c09c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0094bc04",
      "DATA",
      [
        "storage",
        "00c09cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0094bc00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bbe0.md#insn-0094bc00)
- 新版 `0094bc00`（命令位置の公開資料なし）

~~~diff
- 0094bc00 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 0094bc00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0094bc00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0094bc00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0094bc00 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 0094bc00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0094bc00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0094bc00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0094bc00 bytes 08a13091
+ 0094bc00 bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99d50ea69cf7e8e6ba707b3f38d418b8"></a>

### [`0094bc14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bc14.md) → [`0094bc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc14.md) FUN_0094bc14

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
      "definition_site": "0094bc20",
      "incomplete_value": false,
      "site": "0094bc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094bc20",
      "incomplete_value": false,
      "site": "0094bc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0094bc20",
      "DATA",
      [
        "storage",
        "00c09c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0094bc20",
      "DATA",
      [
        "storage",
        "00c09cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0094bc1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bc14.md#insn-0094bc1c)
- 新版 `0094bc1c`（命令位置の公開資料なし）

~~~diff
- 0094bc1c ["COPY", "tmp:0:8", ["const:c28:8"]]
- 0094bc1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0094bc1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0094bc1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0094bc1c ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 0094bc1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0094bc1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0094bc1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0094bc1c bytes 29a13091
+ 0094bc1c bytes 29613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8081d88b89e9cd3e36ecc055ab25a33"></a>

### [`0094bc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bc30.md) → [`0094bc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc30.md) FUN_0094bc30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0045e558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045e/0045e558.md) [`0045f524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045f/0045f524.md) [`0045f660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045f/0045f660.md) [`0045f6d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045f/0045f6d8.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0045e558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md) [`0045f524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f524.md) [`0045f660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f660.md) [`0045f6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f6d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.97% / 新版 95.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094bd0c",
      "incomplete_value": true,
      "site": "0094bd0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094bd0c",
      "incomplete_value": true,
      "site": "0094bd0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7cb:8"
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
      "definition_site": "0094bdd4",
      "incomplete_value": true,
      "site": "0094bdd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0094bdd4",
      "incomplete_value": true,
      "site": "0094bdd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0094bec8",
      "incomplete_value": false,
      "site": "0094becc",
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
      "definition_site": "0094bec8",
      "incomplete_value": false,
      "site": "0094becc",
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
      "0094bcf8",
      "READ",
      [
        "storage",
        "002a57cb",
        null,
        "string"
      ]
    ],
    [
      "0094bd20",
      "PARAM",
      [
        "storage",
        "002a9253",
        null,
        null
      ]
    ],
    [
      "0094bdc4",
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
      "0094bcf8",
      "READ",
      [
        "storage",
        "002a57c4",
        null,
        "string"
      ]
    ],
    [
      "0094bd20",
      "PARAM",
      [
        "storage",
        "002a91bf",
        null,
        null
      ]
    ],
    [
      "0094bdc4",
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

- 旧版 [`0094bcec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bc30.md#insn-0094bcec) · [`0094bd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bc30.md#insn-0094bd20) · [`0094bdbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bc30.md#insn-0094bdbc)
- 新版 `0094bcec`（命令位置の公開資料なし） · `0094bd20`（命令位置の公開資料なし） · `0094bdbc`（命令位置の公開資料なし）

~~~diff
- 0094bcec ["COPY", "tmp:0:8", ["const:7cb:8"]]
- 0094bcec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0094bcec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0094bcec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0094bcec ["COPY", "tmp:0:8", ["const:7c4:8"]]
+ 0094bcec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0094bcec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0094bcec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0094bcec bytes 292d1f91
+ 0094bcec bytes 29111f91
- 0094bd20 ["COPY", "tmp:0:8", ["const:253:8"]]
- 0094bd20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0094bd20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0094bd20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0094bd20 ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 0094bd20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0094bd20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0094bd20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0094bd20 bytes 214c0991
+ 0094bd20 bytes 21fc0691
- 0094bdbc ["COPY", "tmp:0:8", ["const:8c5:8"]]
- 0094bdbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0094bdbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0094bdbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0094bdbc ["COPY", "tmp:0:8", ["const:952:8"]]
+ 0094bdbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0094bdbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0094bdbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0094bdbc bytes 29152391
+ 0094bdbc bytes 29492591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c88da115f759600538c00534d29988e4"></a>

### [`0094c570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094c/0094c570.md) → [`0094c570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094c/0094c570.md) FUN_0094c570

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0094c174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094c/0094c174.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0094c174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094c/0094c174.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0094c57c",
      "incomplete_value": false,
      "site": "0094c580",
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
      "definition_site": "0094c57c",
      "incomplete_value": false,
      "site": "0094c580",
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
      "0094c57c",
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
      "0094c57c",
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

- 旧版 [`0094c57c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094c/0094c570.md#insn-0094c57c)
- 新版 `0094c57c`（命令位置の公開資料なし）

~~~diff
- 0094c57c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0094c57c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0094c57c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0094c57c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0094c57c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0094c57c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0094c57c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0094c57c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0094c57c bytes 00280c91
+ 0094c57c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0975f47b4cdebc129be5ee21db7fc3a"></a>

### [`0094cd94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094c/0094cd94.md) → [`0094cd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094c/0094cd94.md) _INIT_185

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094cdd0",
      "incomplete_value": true,
      "site": "0094cdec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0094cdd0",
      "incomplete_value": true,
      "site": "0094cdec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0094cdf4",
      "incomplete_value": true,
      "site": "0094ce10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0094cdf4",
      "incomplete_value": true,
      "site": "0094ce10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0094ce14",
      "incomplete_value": true,
      "site": "0094ce30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0094ce14",
      "incomplete_value": true,
      "site": "0094ce30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0094cdd0",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0094cdf4",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0094ce14",
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
      "0094cdd0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0094cdf4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0094ce14",
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

- 旧版 [`0094cdc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094c/0094cd94.md#insn-0094cdc0) · [`0094cdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094c/0094cd94.md#insn-0094cdc8)
- 新版 `0094cdc0`（命令位置の公開資料なし） · `0094cdc8`（命令位置の公開資料なし）

~~~diff
- 0094cdc0 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 0094cdc0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0094cdc0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0094cdc0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0094cdc0 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 0094cdc0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0094cdc0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0094cdc0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0094cdc0 bytes 73e21f91
+ 0094cdc0 bytes 73e22291
- 0094cdc8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0094cdc8 bytes c9cafff0
+ 0094cdc8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0094cdc8 bytes c9cafff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed46d449a342c48b3376c35b8160844b"></a>

### [`0094d124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094d/0094d124.md) → [`0094d124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094d/0094d124.md) FUN_0094d124

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0094f7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) · 呼出先 22件 [`00459a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459a90.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`004752f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/004752f8.md) [`0060d83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060d/0060d83c.md)
- 新版 呼出元 2件 [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 22件 [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`004752f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/004752f8.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 36件, `store_condition` 2件, `store_destination` 31件, `store_value` 11件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0094d178",
      "incomplete_value": true,
      "site": "0094d178",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094d178",
      "incomplete_value": true,
      "site": "0094d178",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094df6c",
      "incomplete_value": true,
      "site": "0094df80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094df6c",
      "incomplete_value": true,
      "site": "0094df80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ac8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 99,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094e0c4",
      "incomplete_value": true,
      "site": "0094e0d8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:b55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094e0c4",
      "incomplete_value": true,
      "site": "0094e0d8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:ac8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 114,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0094d168",
      "READ",
      [
        "storage",
        "00c24630",
        null,
        "undefined4"
      ]
    ],
    [
      "0094d178",
      "WRITE",
      [
        "storage",
        "00c24630",
        null,
        "undefined4"
      ]
    ],
    [
      "0094d17c",
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
      "0094d168",
      "READ",
      [
        "storage",
        "00c246e0",
        null,
        "undefined4"
      ]
    ],
    [
      "0094d178",
      "WRITE",
      [
        "storage",
        "00c246e0",
        null,
        "undefined4"
      ]
    ],
    [
      "0094d17c",
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

- 旧版 [`0094d178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094d/0094d124.md#insn-0094d178) · [`0094d168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094d/0094d124.md#insn-0094d168) · [`0094d17c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094d/0094d124.md#insn-0094d17c)
- 新版 `0094d178`（命令位置の公開資料なし） · `0094d168`（命令位置の公開資料なし） · `0094d17c`（命令位置の公開資料なし）

~~~diff
- 0094d178 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:630:8"]]
- 0094d178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:4"]]
+ 0094d178 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6e0:8"]]
+ 0094d178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:4"]]
- 0094d178 bytes 183106b9
+ 0094d178 bytes 18e106b9
- 0094d168 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:630:8"]]
- 0094d168 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 0094d168 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 0094d168 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6e0:8"]]
+ 0094d168 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 0094d168 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 0094d168 bytes 093146b9
+ 0094d168 bytes 09e146b9
- 0094d17c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
- 0094d17c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0094d17c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 0094d17c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0094d17c bytes 20dd44f9
+ 0094d17c bytes 203d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71de8062fcb334201272412bd97f34b5"></a>

### [`0094efec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094e/0094efec.md) → [`0094efec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094e/0094efec.md) FUN_0094efec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00680c84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00680/00680c84.md) [`00957f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) · 呼出先 14件 [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00640490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00640/00640490.md) [`0066f824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0066f/0066f824.md) [`0094f64c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094f/0094f64c.md)
- 新版 呼出元 2件 [`00680c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00680/00680c84.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 14件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00640490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640490.md) [`0066f824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f824.md) [`0094f64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f64c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 91.41% / 新版 91.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0094f3dc",
      "incomplete_value": false,
      "site": "0094f3dc",
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
      "definition_site": "0094f3dc",
      "incomplete_value": false,
      "site": "0094f3dc",
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
    "ordinal": 25,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0094f3e0",
      "incomplete_value": false,
      "site": "0094f3e0",
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
      "definition_site": "0094f3e0",
      "incomplete_value": false,
      "site": "0094f3e0",
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
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0094f3dc",
      "incomplete_value": false,
      "site": "0094f3e0",
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
      "definition_site": "0094f3dc",
      "incomplete_value": false,
      "site": "0094f3e0",
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
      "0094f034",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0094f048",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0094f050",
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
      "0094f034",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0094f048",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0094f050",
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

- 旧版 [`0094f034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094e/0094efec.md#insn-0094f034) · [`0094f048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094e/0094efec.md#insn-0094f048) · [`0094f050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094e/0094efec.md#insn-0094f050)
- 新版 `0094f034`（命令位置の公開資料なし） · `0094f048`（命令位置の公開資料なし） · `0094f050`（命令位置の公開資料なし）

~~~diff
- 0094f034 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 0094f034 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0094f034 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0094f034 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0094f034 bytes 00dd44f9
+ 0094f034 bytes 003d45f9
- 0094f048 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0094f048 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0094f048 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0094f048 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0094f048 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0094f048 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0094f048 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0094f048 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0094f048 bytes 21603691
+ 0094f048 bytes 21203991
- 0094f050 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0094f050 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0094f050 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0094f050 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0094f050 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0094f050 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0094f050 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0094f050 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0094f050 bytes 42603291
+ 0094f050 bytes 42203591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-259a1d204081da652975efd29f9b3b6e"></a>

### [`00957320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957320.md) → [`00957320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957320.md) FUN_00957320

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00680c84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00680/00680c84.md) [`0092bc08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0092b/0092bc08.md) [`0094f7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) · 呼出先 18件 [`0042cde4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042cde4.md) [`0044b660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b660.md) [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`005bdd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005bd/005bdd1c.md) [`005dfeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005df/005dfeb0.md)
- 新版 呼出元 4件 [`00680c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00680/00680c84.md) [`0092bc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092b/0092bc08.md) [`0094f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 18件 [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`0044b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`005bdd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bd/005bdd1c.md) [`005dfeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005df/005dfeb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.65% / 新版 98.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009573ac",
      "incomplete_value": true,
      "site": "009573ac",
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
      "definition_site": "009573ac",
      "incomplete_value": true,
      "site": "009573ac",
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009573b4",
      "incomplete_value": false,
      "site": "009573c4",
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
      "definition_site": "009573b4",
      "incomplete_value": false,
      "site": "009573c4",
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
      "definition_site": "009573bc",
      "incomplete_value": false,
      "site": "009573c4",
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
      "definition_site": "009573bc",
      "incomplete_value": false,
      "site": "009573c4",
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
      "009573a8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "009573b4",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009573bc",
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
      "009573a8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009573b4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009573bc",
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

- 旧版 [`009573a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957320.md#insn-009573a8) · [`009573b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957320.md#insn-009573b4) · [`009573bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957320.md#insn-009573bc)
- 新版 `009573a8`（命令位置の公開資料なし） · `009573b4`（命令位置の公開資料なし） · `009573bc`（命令位置の公開資料なし）

~~~diff
- 009573a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 009573a8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 009573a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 009573a8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 009573a8 bytes 00dd44f9
+ 009573a8 bytes 003d45f9
- 009573b4 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 009573b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009573b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009573b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009573b4 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 009573b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009573b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009573b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009573b4 bytes 21603691
+ 009573b4 bytes 21203991
- 009573bc ["COPY", "tmp:0:8", ["const:c98:8"]]
- 009573bc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 009573bc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 009573bc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 009573bc ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 009573bc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 009573bc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 009573bc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 009573bc bytes 42603291
+ 009573bc bytes 42203591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd69243b505b7e60b30cd92b95de10cf"></a>

### [`00957f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) → [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) FUN_00957f9c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 128件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449bac.md) [`0044b660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b660.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 128件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`0044b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 65件, `store_condition` 2件, `store_destination` 40件, `store_value` 18件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009583ec",
      "incomplete_value": true,
      "site": "009583fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009583ec",
      "incomplete_value": true,
      "site": "009583fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:24f:8"
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
      "definition_site": "009583f0",
      "incomplete_value": true,
      "site": "00958400",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "009583f0",
      "incomplete_value": true,
      "site": "00958400",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00958424",
      "incomplete_value": false,
      "site": "00958424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00958424",
      "incomplete_value": false,
      "site": "00958424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "009583ec",
      "READ",
      [
        "storage",
        "0029824f",
        null,
        "string"
      ]
    ],
    [
      "009583f0",
      "READ",
      [
        "storage",
        "0029825c",
        null,
        "string"
      ]
    ],
    [
      "00958424",
      "DATA",
      [
        "storage",
        "00c09fb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009583ec",
      "READ",
      [
        "storage",
        "002982dc",
        null,
        "string"
      ]
    ],
    [
      "009583f0",
      "READ",
      [
        "storage",
        "002982e9",
        null,
        "string"
      ]
    ],
    [
      "00958424",
      "DATA",
      [
        "storage",
        "00c0a068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009583e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/assembly/00957/00957f9c-00957f9c-00960c98.md#insn-009583e4) · [`009583e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/assembly/00957/00957f9c-00957f9c-00960c98.md#insn-009583e8)
- 新版 `009583e4`（命令位置の公開資料なし） · `009583e8`（命令位置の公開資料なし）

~~~diff
- 009583e4 ["COPY", "tmp:0:8", ["const:24f:8"]]
- 009583e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009583e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009583e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009583e4 ["COPY", "tmp:0:8", ["const:2dc:8"]]
+ 009583e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009583e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009583e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009583e4 bytes 083d0991
+ 009583e4 bytes 08710b91
- 009583e8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 009583e8 bytes c9caffb0
+ 009583e8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 009583e8 bytes c9caffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7361f0301e1f6e4dc377ae2fb5700373"></a>

### [`00960d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00960/00960d40.md) → [`00960d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00960/00960d40.md) FUN_00960d40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00957f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) · 呼出先 7件 [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`008865b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00887/008879f4.md) [`0096dfdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dfdc.md) [`0096dfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dfe0.md)
- 新版 呼出元 1件 [`00957f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 7件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/008879f4.md) [`0096dfdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dfdc.md) [`0096dfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dfe0.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00960d7c",
      "incomplete_value": true,
      "site": "00960d7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2fa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00960d7c",
      "incomplete_value": true,
      "site": "00960d7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:26d:8"
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
      "definition_site": "00960d74",
      "incomplete_value": true,
      "site": "00960d80",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00960d74",
      "incomplete_value": true,
      "site": "00960d80",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00960d98",
      "incomplete_value": false,
      "site": "00960da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00960d98",
      "incomplete_value": false,
      "site": "00960da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
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
      "00960d64",
      "READ",
      [
        "storage",
        "0029826d",
        null,
        "string"
      ]
    ],
    [
      "00960d74",
      "READ",
      [
        "storage",
        "00298274",
        null,
        "string"
      ]
    ],
    [
      "00960da0",
      "DATA",
      [
        "storage",
        "00c0a1b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00960d64",
      "READ",
      [
        "storage",
        "002982fa",
        null,
        "string"
      ]
    ],
    [
      "00960d74",
      "READ",
      [
        "storage",
        "00298301",
        null,
        "string"
      ]
    ],
    [
      "00960da0",
      "DATA",
      [
        "storage",
        "00c0a268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00960d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00960/00960d40.md#insn-00960d5c) · [`00960d98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00960/00960d40.md#insn-00960d98) · [`00960d9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00960/00960d40.md#insn-00960d9c)
- 新版 `00960d5c`（命令位置の公開資料なし） · `00960d98`（命令位置の公開資料なし）

~~~diff
- 00960d5c ["COPY", "tmp:0:8", ["const:26d:8"]]
- 00960d5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00960d5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00960d5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00960d5c ["COPY", "tmp:0:8", ["const:2fa:8"]]
+ 00960d5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00960d5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00960d5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00960d5c bytes 29b50991
+ 00960d5c bytes 29e90b91
- 00960d98 ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 00960d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00960d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00960d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00960d98 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 00960d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00960d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00960d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00960d98 bytes 08e10691
+ 00960d98 bytes 08a10991
- 00960d9c ["COPY", "tmp:0:8", ["const:30:8"]]
- 00960d9c ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00960d9c ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00960d9c ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00960d9c bytes f5c30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71f2c76ce8b47e24918c26d4d54ccb97"></a>

### [`009613bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00961/009613bc.md) → [`009613bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00961/009613bc.md) FUN_009613bc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 35件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 35件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00961444",
      "incomplete_value": true,
      "site": "00961444",
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
      "definition_site": "00961444",
      "incomplete_value": true,
      "site": "00961444",
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
      "definition_site": "0096149c",
      "incomplete_value": true,
      "site": "0096149c",
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
      "definition_site": "0096149c",
      "incomplete_value": true,
      "site": "0096149c",
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096144c",
      "incomplete_value": false,
      "site": "0096145c",
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
      "definition_site": "0096144c",
      "incomplete_value": false,
      "site": "0096145c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00961420",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0096144c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00961454",
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
      "00961420",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0096144c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00961454",
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

- 旧版 [`00961420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00961/009613bc.md#insn-00961420) · [`0096144c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00961/009613bc.md#insn-0096144c) · [`00961454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00961/009613bc.md#insn-00961454)
- 新版 `00961420`（命令位置の公開資料なし） · `0096144c`（命令位置の公開資料なし） · `00961454`（命令位置の公開資料なし）

~~~diff
- 00961420 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:9b8:8"]]
- 00961420 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00961420 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:a78:8"]]
+ 00961420 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00961420 bytes 40dd44f9
+ 00961420 bytes 403d45f9
- 0096144c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0096144c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0096144c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0096144c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0096144c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0096144c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0096144c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0096144c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0096144c bytes 21603691
+ 0096144c bytes 21203991
- 00961454 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00961454 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00961454 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00961454 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00961454 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00961454 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00961454 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00961454 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00961454 bytes 42603291
+ 00961454 bytes 42203591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6651560ecd216c5d5c599f330616b5c0"></a>

### [`00965df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00965/00965df0.md) → [`00965df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00965/00965df0.md) FUN_00965df0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009613bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00961/009613bc.md) [`0096de04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096de04.md) · 呼出先 33件 [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md)
- 新版 呼出元 2件 [`009613bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00961/009613bc.md) [`0096de04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096de04.md) · 呼出先 33件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.57% / 新版 98.57%

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
      "definition_site": "00965e48",
      "incomplete_value": true,
      "site": "00965e48",
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
      "definition_site": "00965e48",
      "incomplete_value": true,
      "site": "00965e48",
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
      "definition_site": "00965e50",
      "incomplete_value": false,
      "site": "00965e60",
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
      "definition_site": "00965e50",
      "incomplete_value": false,
      "site": "00965e60",
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
      "definition_site": "00965e58",
      "incomplete_value": false,
      "site": "00965e60",
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
      "definition_site": "00965e58",
      "incomplete_value": false,
      "site": "00965e60",
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
      "00965e3c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00965e50",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00965e58",
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
      "00965e3c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00965e50",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00965e58",
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

- 旧版 [`00965e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00965/00965df0.md#insn-00965e3c) · [`00965e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00965/00965df0.md#insn-00965e50) · [`00965e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00965/00965df0.md#insn-00965e58)
- 新版 `00965e3c`（命令位置の公開資料なし） · `00965e50`（命令位置の公開資料なし） · `00965e58`（命令位置の公開資料なし）

~~~diff
- 00965e3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00965e3c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00965e3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00965e3c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00965e3c bytes 00dd44f9
+ 00965e3c bytes 003d45f9
- 00965e50 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00965e50 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00965e50 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00965e50 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00965e50 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00965e50 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00965e50 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00965e50 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00965e50 bytes 21603691
+ 00965e50 bytes 21203991
- 00965e58 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00965e58 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00965e58 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00965e58 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00965e58 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00965e58 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00965e58 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00965e58 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00965e58 bytes 42603291
+ 00965e58 bytes 42203591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68e087bef83da17cf3b0a92e2e20298c"></a>

### [`0096b7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096b/0096b7d8.md) → [`0096b7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096b/0096b7d8.md) FUN_0096b7d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00963004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00963/00963004.md) · 呼出先 6件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00447a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447a10.md) [`00448034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448034.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00963004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00963/00963004.md) · 呼出先 6件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "definition_site": "0096b81c",
      "incomplete_value": true,
      "site": "0096b81c",
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
      "definition_site": "0096b81c",
      "incomplete_value": true,
      "site": "0096b81c",
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
      "definition_site": "0096b824",
      "incomplete_value": false,
      "site": "0096b838",
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
      "definition_site": "0096b824",
      "incomplete_value": false,
      "site": "0096b838",
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
      "definition_site": "0096b82c",
      "incomplete_value": false,
      "site": "0096b838",
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
      "definition_site": "0096b82c",
      "incomplete_value": false,
      "site": "0096b838",
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
      "0096b818",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0096b824",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0096b82c",
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
      "0096b818",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0096b824",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0096b82c",
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

- 旧版 [`0096b818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096b/0096b7d8.md#insn-0096b818) · [`0096b824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096b/0096b7d8.md#insn-0096b824) · [`0096b82c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096b/0096b7d8.md#insn-0096b82c)
- 新版 `0096b818`（命令位置の公開資料なし） · `0096b824`（命令位置の公開資料なし） · `0096b82c`（命令位置の公開資料なし）

~~~diff
- 0096b818 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 0096b818 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0096b818 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0096b818 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0096b818 bytes 08dd44f9
+ 0096b818 bytes 083d45f9
- 0096b824 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0096b824 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0096b824 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0096b824 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0096b824 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0096b824 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0096b824 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0096b824 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0096b824 bytes 21603691
+ 0096b824 bytes 21203991
- 0096b82c ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0096b82c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0096b82c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0096b82c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0096b82c ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0096b82c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0096b82c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0096b82c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0096b82c bytes 42603291
+ 0096b82c bytes 42203591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0348cb406d4f05291eb5393f5b5aeea"></a>

### [`0096d13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d13c.md) → [`0096d13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d13c.md) FUN_0096d13c

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
      "definition_site": "0096d160",
      "incomplete_value": false,
      "site": "0096d160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096d160",
      "incomplete_value": false,
      "site": "0096d160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
      "0096d160",
      "DATA",
      [
        "storage",
        "00c09ca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096d160",
      "DATA",
      [
        "storage",
        "00c09d58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096d15c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d13c.md#insn-0096d15c)
- 新版 `0096d15c`（命令位置の公開資料なし）

~~~diff
- 0096d15c ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 0096d15c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096d15c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096d15c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096d15c ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 0096d15c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d15c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d15c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096d15c bytes 08a13291
+ 0096d15c bytes 08613591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85899b31ae8a0825d5a81a2d0c3b6f6d"></a>

### [`0096d530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d530.md) → [`0096d530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d530.md) FUN_0096d530

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
      "definition_site": "0096d554",
      "incomplete_value": false,
      "site": "0096d554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096d554",
      "incomplete_value": false,
      "site": "0096d554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "0096d554",
      "DATA",
      [
        "storage",
        "00c09d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096d554",
      "DATA",
      [
        "storage",
        "00c09de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096d550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d530.md#insn-0096d550)
- 新版 `0096d550`（命令位置の公開資料なし）

~~~diff
- 0096d550 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0096d550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096d550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096d550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096d550 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 0096d550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096d550 bytes 08e13491
+ 0096d550 bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37046da48f12fa22c5db7e59b4fe7457"></a>

### [`0096d668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d668.md) → [`0096d668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d668.md) FUN_0096d668

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
      "definition_site": "0096d68c",
      "incomplete_value": false,
      "site": "0096d68c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096d68c",
      "incomplete_value": false,
      "site": "0096d68c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "0096d68c",
      "DATA",
      [
        "storage",
        "00c09db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096d68c",
      "DATA",
      [
        "storage",
        "00c09e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096d688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d668.md#insn-0096d688)
- 新版 `0096d688`（命令位置の公開資料なし）

~~~diff
- 0096d688 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 0096d688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096d688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096d688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096d688 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 0096d688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096d688 bytes 08e13691
+ 0096d688 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

