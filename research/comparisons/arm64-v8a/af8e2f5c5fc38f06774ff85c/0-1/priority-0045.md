# v15.7.2 → v15.7.3 · 最優先の変更候補 (45)

[一覧の目次](README.md)

<a id="compare-6e61f6bf61b80e7c63f371781f1b57b6"></a>

### [`008a4e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a4/008a4e38.md) → [`008a4e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a4/008a4e38.md) FUN_008a4e38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 22件 [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00449b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449b7c.md) [`00449c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449c34.md) [`0052dd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dd50.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449b7c.md) [`00449c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c34.md) [`0052dd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.66% / 新版 93.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a4efc",
      "incomplete_value": false,
      "site": "008a4efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a4efc",
      "incomplete_value": false,
      "site": "008a4efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:730:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a4f64",
      "incomplete_value": false,
      "site": "008a4f68",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a4f64",
      "incomplete_value": false,
      "site": "008a4f68",
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
            "const:cb0:8"
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
      "definition_site": "008a4f88",
      "incomplete_value": false,
      "site": "008a4f8c",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a4f88",
      "incomplete_value": false,
      "site": "008a4f8c",
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
            "const:cb0:8"
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
      "008a4e68",
      "READ",
      [
        "storage",
        "00c1ac78",
        null,
        "pointer"
      ]
    ],
    [
      "008a4e74",
      "READ",
      [
        "storage",
        "00c24cb8",
        null,
        "undefined4"
      ]
    ],
    [
      "008a4e74",
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
      "008a4e68",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "008a4e74",
      "READ",
      [
        "storage",
        "00c24d78",
        null,
        "undefined4"
      ]
    ],
    [
      "008a4e74",
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

- 旧版 [`008a4e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a4/008a4e38.md#insn-008a4e68) · [`008a4e84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a4/008a4e38.md#insn-008a4e84) · [`008a4ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a4/008a4e38.md#insn-008a4ef4)
- 新版 `008a4e68`（命令位置の公開資料なし） · `008a4e84`（命令位置の公開資料なし） · `008a4ef4`（命令位置の公開資料なし）

~~~diff
- 008a4e68 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c78:8"]]
- 008a4e68 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 008a4e68 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d28:8"]]
+ 008a4e68 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 008a4e68 bytes 293d46f9
+ 008a4e68 bytes 299546f9
- 008a4e84 ["COPY", "tmp:0:8", ["const:a7d:8"]]
- 008a4e84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a4e84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a4e84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008a4e84 ["COPY", "tmp:0:8", ["const:b0a:8"]]
+ 008a4e84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008a4e84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008a4e84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a4e84 bytes 29f52991
+ 008a4e84 bytes 29292c91
- 008a4ef4 ["COPY", "tmp:0:8", ["const:730:8"]]
- 008a4ef4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a4ef4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a4ef4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008a4ef4 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 008a4ef4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008a4ef4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008a4ef4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a4ef4 bytes 29c11c91
+ 008a4ef4 bytes 29811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94bdfa1c0878728aa5e6fe1097790174"></a>

### [`008a53d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a53d8.md) → [`008a53d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a53d8.md) FUN_008a53d8

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
      "definition_site": "008a53f8",
      "incomplete_value": false,
      "site": "008a53fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a53f8",
      "incomplete_value": false,
      "site": "008a53fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
      "008a53fc",
      "DATA",
      [
        "storage",
        "00c06730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a53fc",
      "DATA",
      [
        "storage",
        "00c067e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a53f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a53d8.md#insn-008a53f8)
- 新版 `008a53f8`（命令位置の公開資料なし）

~~~diff
- 008a53f8 ["COPY", "tmp:0:8", ["const:730:8"]]
- 008a53f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a53f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a53f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a53f8 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 008a53f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a53f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a53f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a53f8 bytes 08c11c91
+ 008a53f8 bytes 08811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f4542179a3392bfe35031bcbc8cc328"></a>

### [`008a5410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5410.md) → [`008a5410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5410.md) FUN_008a5410

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
      "definition_site": "008a5414",
      "incomplete_value": false,
      "site": "008a5418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5414",
      "incomplete_value": false,
      "site": "008a5418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
      "008a5418",
      "DATA",
      [
        "storage",
        "00c06730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5418",
      "DATA",
      [
        "storage",
        "00c067e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5410.md#insn-008a5414)
- 新版 `008a5414`（命令位置の公開資料なし）

~~~diff
- 008a5414 ["COPY", "tmp:0:8", ["const:730:8"]]
- 008a5414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a5414 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 008a5414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5414 bytes 08c11c91
+ 008a5414 bytes 08811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34162b3728c0d8cafbfc2d35021466ab"></a>

### [`008a54b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a54b0.md) → [`008a54b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a54b0.md) FUN_008a54b0

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
      "definition_site": "008a54d4",
      "incomplete_value": false,
      "site": "008a54d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a54d4",
      "incomplete_value": false,
      "site": "008a54d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
      "008a54d4",
      "DATA",
      [
        "storage",
        "00c067d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a54d4",
      "DATA",
      [
        "storage",
        "00c06880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a54d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a54b0.md#insn-008a54d0)
- 新版 `008a54d0`（命令位置の公開資料なし）

~~~diff
- 008a54d0 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 008a54d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a54d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a54d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a54d0 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 008a54d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a54d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a54d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a54d0 bytes 08411f91
+ 008a54d0 bytes 08012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1204cd6a35445e207afc112c11722be"></a>

### [`008a54e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a54e4.md) → [`008a54e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a54e4.md) FUN_008a54e4

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
      "definition_site": "008a54f0",
      "incomplete_value": false,
      "site": "008a54f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a54f0",
      "incomplete_value": false,
      "site": "008a54f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
      "008a54f0",
      "DATA",
      [
        "storage",
        "00c067d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a54f0",
      "DATA",
      [
        "storage",
        "00c06880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a54ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a54e4.md#insn-008a54ec)
- 新版 `008a54ec`（命令位置の公開資料なし）

~~~diff
- 008a54ec ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 008a54ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a54ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a54ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008a54ec ["COPY", "tmp:0:8", ["const:880:8"]]
+ 008a54ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008a54ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008a54ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a54ec bytes 29411f91
+ 008a54ec bytes 29012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-971964b85ee8248750d9949c38844f4f"></a>

### [`008a5500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5500.md) → [`008a5500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5500.md) FUN_008a5500

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`0088482c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00884/0088482c.md) [`008a56d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a56d0.md) [`008a56d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a56d4.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0088482c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/0088482c.md) [`008a56d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a56d0.md) [`008a56d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a56d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a5594",
      "incomplete_value": false,
      "site": "008a5594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5594",
      "incomplete_value": false,
      "site": "008a5594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "008a5594",
      "DATA",
      [
        "storage",
        "00c06840",
        null,
        "undefined *"
      ]
    ],
    [
      "008a55d0",
      "READ",
      [
        "storage",
        "00c06860",
        null,
        "pointer"
      ]
    ],
    [
      "008a55d0",
      "READ",
      [
        "storage",
        "00c06868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5594",
      "DATA",
      [
        "storage",
        "00c068f0",
        null,
        "undefined *"
      ]
    ],
    [
      "008a55d0",
      "READ",
      [
        "storage",
        "00c06910",
        null,
        "pointer"
      ]
    ],
    [
      "008a55d0",
      "READ",
      [
        "storage",
        "00c06918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a558c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5500.md#insn-008a558c)
- 新版 `008a558c`（命令位置の公開資料なし）

~~~diff
- 008a558c ["COPY", "tmp:0:8", ["const:840:8"]]
- 008a558c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a558c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a558c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a558c ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 008a558c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a558c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a558c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a558c bytes 08012191
+ 008a558c bytes 08c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ebae0e42db7b80210036cc5c4bb6f6d"></a>

### [`008a5688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5688.md) → [`008a5688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5688.md) FUN_008a5688

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
      "definition_site": "008a56ac",
      "incomplete_value": false,
      "site": "008a56ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a56ac",
      "incomplete_value": false,
      "site": "008a56ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
      "008a56ac",
      "DATA",
      [
        "storage",
        "00c06840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a56ac",
      "DATA",
      [
        "storage",
        "00c068f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a56a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5688.md#insn-008a56a8)
- 新版 `008a56a8`（命令位置の公開資料なし）

~~~diff
- 008a56a8 ["COPY", "tmp:0:8", ["const:840:8"]]
- 008a56a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a56a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a56a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a56a8 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 008a56a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a56a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a56a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a56a8 bytes 08012191
+ 008a56a8 bytes 08c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8ffdeffaa2dc6685ea5d89f12cada99"></a>

### [`008a56bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a56bc.md) → [`008a56bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a56bc.md) FUN_008a56bc

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
      "definition_site": "008a56c8",
      "incomplete_value": false,
      "site": "008a56c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a56c8",
      "incomplete_value": false,
      "site": "008a56c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
      "008a56c8",
      "DATA",
      [
        "storage",
        "00c06840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a56c8",
      "DATA",
      [
        "storage",
        "00c068f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a56c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a56bc.md#insn-008a56c4)
- 新版 `008a56c4`（命令位置の公開資料なし）

~~~diff
- 008a56c4 ["COPY", "tmp:0:8", ["const:840:8"]]
- 008a56c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a56c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a56c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008a56c4 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 008a56c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008a56c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008a56c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a56c4 bytes 29012191
+ 008a56c4 bytes 29c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ad38c876fca11f4a127a98ceb773125"></a>

### [`008a577c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a577c.md) → [`008a577c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a577c.md) FUN_008a577c

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
      "definition_site": "008a5788",
      "incomplete_value": false,
      "site": "008a578c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5788",
      "incomplete_value": false,
      "site": "008a578c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
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
      "008a578c",
      "DATA",
      [
        "storage",
        "00c068d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a578c",
      "DATA",
      [
        "storage",
        "00c06980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a577c.md#insn-008a5788)
- 新版 `008a5788`（命令位置の公開資料なし）

~~~diff
- 008a5788 ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 008a5788 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a5788 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a5788 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008a5788 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 008a5788 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008a5788 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008a5788 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a5788 bytes 29412391
+ 008a5788 bytes 29012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7884f6984f69bb378825abbbe7ecb63"></a>

### [`008a57a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a57a0.md) → [`008a57a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a57a0.md) FUN_008a57a0

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
      "definition_site": "008a57a8",
      "incomplete_value": false,
      "site": "008a57ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a57a8",
      "incomplete_value": false,
      "site": "008a57ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
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
      "008a57ac",
      "DATA",
      [
        "storage",
        "00c068d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a57ac",
      "DATA",
      [
        "storage",
        "00c06980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a57a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a57a0.md#insn-008a57a8)
- 新版 `008a57a8`（命令位置の公開資料なし）

~~~diff
- 008a57a8 ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 008a57a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a57a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a57a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008a57a8 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 008a57a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008a57a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008a57a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a57a8 bytes 29412391
+ 008a57a8 bytes 29012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1d442d5c1aba25567f55ab2c8a545c3"></a>

### [`008a57e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a57e0.md) → [`008a57e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a57e0.md) FUN_008a57e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`008a4204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a4/008a4204.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`008a4204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a4/008a4204.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a5818",
      "incomplete_value": false,
      "site": "008a5818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5818",
      "incomplete_value": false,
      "site": "008a5818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
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
      "008a5818",
      "DATA",
      [
        "storage",
        "00c068d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5818",
      "DATA",
      [
        "storage",
        "00c06980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a57e0.md#insn-008a5808)
- 新版 `008a5808`（命令位置の公開資料なし）

~~~diff
- 008a5808 ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 008a5808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a5808 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 008a5808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5808 bytes 08412391
+ 008a5808 bytes 08012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-621450cc768437ea46d0af3d7b42e5f4"></a>

### [`008a58d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a58d8.md) → [`008a58d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a58d8.md) FUN_008a58d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`008a4204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a4/008a4204.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`008a4204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a4/008a4204.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a5904",
      "incomplete_value": false,
      "site": "008a5904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5904",
      "incomplete_value": false,
      "site": "008a5904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
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
      "008a5904",
      "DATA",
      [
        "storage",
        "00c068d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5904",
      "DATA",
      [
        "storage",
        "00c06980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a58f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a58d8.md#insn-008a58f4)
- 新版 `008a58f4`（命令位置の公開資料なし）

~~~diff
- 008a58f4 ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 008a58f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a58f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a58f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008a58f4 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 008a58f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008a58f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008a58f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a58f4 bytes 29412391
+ 008a58f4 bytes 29012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18f2221db388145e94487af3eebb1aa1"></a>

### [`008a5a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5a8c.md) → [`008a5a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5a8c.md) FUN_008a5a8c

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
      "definition_site": "008a5aa0",
      "incomplete_value": false,
      "site": "008a5aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5aa0",
      "incomplete_value": false,
      "site": "008a5aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "008a5aa4",
      "DATA",
      [
        "storage",
        "00c06950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5aa4",
      "DATA",
      [
        "storage",
        "00c06a00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5a8c.md#insn-008a5aa0)
- 新版 `008a5aa0`（命令位置の公開資料なし）

~~~diff
- 008a5aa0 ["COPY", "tmp:0:8", ["const:950:8"]]
- 008a5aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a5aa0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 008a5aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5aa0 bytes 08412591
+ 008a5aa0 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cefeda3d5c46421aca552c43817de97"></a>

### [`008a5ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5ab0.md) → [`008a5ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5ab0.md) FUN_008a5ab0

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
      "definition_site": "008a5ab4",
      "incomplete_value": false,
      "site": "008a5ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5ab4",
      "incomplete_value": false,
      "site": "008a5ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "008a5ab8",
      "DATA",
      [
        "storage",
        "00c06950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5ab8",
      "DATA",
      [
        "storage",
        "00c06a00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5ab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5ab0.md#insn-008a5ab4)
- 新版 `008a5ab4`（命令位置の公開資料なし）

~~~diff
- 008a5ab4 ["COPY", "tmp:0:8", ["const:950:8"]]
- 008a5ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a5ab4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 008a5ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5ab4 bytes 08412591
+ 008a5ab4 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-465e2d3036f7e1ed8d9116d6f4b0121e"></a>

### [`008a5b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5b0c.md) → [`008a5b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5b0c.md) FUN_008a5b0c

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
      "definition_site": "008a5b20",
      "incomplete_value": false,
      "site": "008a5b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5b20",
      "incomplete_value": false,
      "site": "008a5b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
      "008a5b24",
      "DATA",
      [
        "storage",
        "00c069d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5b24",
      "DATA",
      [
        "storage",
        "00c06a80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5b0c.md#insn-008a5b20)
- 新版 `008a5b20`（命令位置の公開資料なし）

~~~diff
- 008a5b20 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 008a5b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a5b20 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 008a5b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5b20 bytes 08412791
+ 008a5b20 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d10d0f60a40249d2842488e7ee5f162a"></a>

### [`008a5b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5b30.md) → [`008a5b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5b30.md) FUN_008a5b30

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
      "definition_site": "008a5b34",
      "incomplete_value": false,
      "site": "008a5b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5b34",
      "incomplete_value": false,
      "site": "008a5b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
      "008a5b38",
      "DATA",
      [
        "storage",
        "00c069d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5b38",
      "DATA",
      [
        "storage",
        "00c06a80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5b30.md#insn-008a5b34)
- 新版 `008a5b34`（命令位置の公開資料なし）

~~~diff
- 008a5b34 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 008a5b34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5b34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5b34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a5b34 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 008a5b34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5b34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5b34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5b34 bytes 08412791
+ 008a5b34 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27838f51bf95b506820ae81bf0960f2b"></a>

### [`008a5b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5b78.md) → [`008a5b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5b78.md) FUN_008a5b78

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
      "definition_site": "008a5b98",
      "incomplete_value": false,
      "site": "008a5b9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5b98",
      "incomplete_value": false,
      "site": "008a5b9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "008a5b9c",
      "DATA",
      [
        "storage",
        "00c06a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5b9c",
      "DATA",
      [
        "storage",
        "00c06b00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5b98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5b78.md#insn-008a5b98)
- 新版 `008a5b98`（命令位置の公開資料なし）

~~~diff
- 008a5b98 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 008a5b98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5b98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5b98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a5b98 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 008a5b98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5b98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5b98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5b98 bytes 08412991
+ 008a5b98 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e6b38a0cece7ad1bd943bca535ac88d"></a>

### [`008a5bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5bb0.md) → [`008a5bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5bb0.md) FUN_008a5bb0

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
      "definition_site": "008a5bb4",
      "incomplete_value": false,
      "site": "008a5bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5bb4",
      "incomplete_value": false,
      "site": "008a5bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "008a5bb8",
      "DATA",
      [
        "storage",
        "00c06a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5bb8",
      "DATA",
      [
        "storage",
        "00c06b00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5bb0.md#insn-008a5bb4)
- 新版 `008a5bb4`（命令位置の公開資料なし）

~~~diff
- 008a5bb4 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 008a5bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a5bb4 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 008a5bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5bb4 bytes 08412991
+ 008a5bb4 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3158f9db15a309a07721d1965b877b7"></a>

### [`008a5bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5bd0.md) → [`008a5bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5bd0.md) FUN_008a5bd0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 28件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0042ab60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042a/0042ab60.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469fac.md)
- 新版 呼出元 0件  · 呼出先 28件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0042ab60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042a/0042ab60.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.27% / 新版 94.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008a5cb8",
      "incomplete_value": true,
      "site": "008a5cc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:36b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5cb8",
      "incomplete_value": true,
      "site": "008a5cc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2de:8"
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
      "definition_site": "008a5cb8",
      "incomplete_value": true,
      "site": "008a5cc8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008a5cb8",
      "incomplete_value": true,
      "site": "008a5cc8",
      "value": [
        "LOAD",
        "16",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a5ce0",
      "incomplete_value": false,
      "site": "008a5ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a5ce0",
      "incomplete_value": false,
      "site": "008a5ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "008a5cb8",
      "READ",
      [
        "storage",
        "0029a2de",
        null,
        "string"
      ]
    ],
    [
      "008a5cb8",
      "READ",
      [
        "storage",
        "0029a2ee",
        null,
        "string"
      ]
    ],
    [
      "008a5ce8",
      "DATA",
      [
        "storage",
        "00c06b40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5cb8",
      "READ",
      [
        "storage",
        "0029a36b",
        null,
        "string"
      ]
    ],
    [
      "008a5cb8",
      "READ",
      [
        "storage",
        "0029a37b",
        null,
        "string"
      ]
    ],
    [
      "008a5ce8",
      "DATA",
      [
        "storage",
        "00c06bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5bd0.md#insn-008a5cb4) · [`008a5ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5bd0.md#insn-008a5ce0) · [`008a5d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5bd0.md#insn-008a5d5c)
- 新版 `008a5cb4`（命令位置の公開資料なし） · `008a5ce0`（命令位置の公開資料なし） · `008a5d5c`（命令位置の公開資料なし）

~~~diff
- 008a5cb4 ["COPY", "tmp:0:8", ["const:2de:8"]]
- 008a5cb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5cb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5cb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a5cb4 ["COPY", "tmp:0:8", ["const:36b:8"]]
+ 008a5cb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5cb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5cb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5cb4 bytes 08790b91
+ 008a5cb4 bytes 08ad0d91
- 008a5ce0 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 008a5ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a5ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a5ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a5ce0 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 008a5ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a5ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a5ce0 bytes 08012d91
+ 008a5ce0 bytes 08c12f91
- 008a5d5c ["COPY", "register:4040:8", ["const:2ae000:8"]]
+ 008a5d5c ["COPY", "register:4040:8", ["const:2ad000:8"]]
- 008a5d5c bytes 48d0ffb0
+ 008a5d5c bytes 48d0ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daab871a2db12e1580be5780cac459bb"></a>

### [`008a6330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6330.md) → [`008a6330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a6330.md) FUN_008a6330

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
      "definition_site": "008a6344",
      "incomplete_value": false,
      "site": "008a6348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6344",
      "incomplete_value": false,
      "site": "008a6348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "008a6348",
      "DATA",
      [
        "storage",
        "00c06ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a6348",
      "DATA",
      [
        "storage",
        "00c06b70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6330.md#insn-008a6344)
- 新版 `008a6344`（命令位置の公開資料なし）

~~~diff
- 008a6344 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 008a6344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a6344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a6344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a6344 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 008a6344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a6344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a6344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a6344 bytes 08012b91
+ 008a6344 bytes 08c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44495a3226ca587b5954b90cc8bb7668"></a>

### [`008a6354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6354.md) → [`008a6354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a6354.md) FUN_008a6354

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
      "definition_site": "008a6358",
      "incomplete_value": false,
      "site": "008a635c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6358",
      "incomplete_value": false,
      "site": "008a635c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "008a635c",
      "DATA",
      [
        "storage",
        "00c06ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a635c",
      "DATA",
      [
        "storage",
        "00c06b70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6354.md#insn-008a6358)
- 新版 `008a6358`（命令位置の公開資料なし）

~~~diff
- 008a6358 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 008a6358 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a6358 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a6358 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a6358 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 008a6358 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a6358 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a6358 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a6358 bytes 08012b91
+ 008a6358 bytes 08c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3945b946f29ba61fcdd758139680a0f5"></a>

### [`008a63b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a63b0.md) → [`008a63b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a63b0.md) FUN_008a63b0

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
      "definition_site": "008a63c4",
      "incomplete_value": false,
      "site": "008a63c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a63c4",
      "incomplete_value": false,
      "site": "008a63c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "008a63c8",
      "DATA",
      [
        "storage",
        "00c06b40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a63c8",
      "DATA",
      [
        "storage",
        "00c06bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a63c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a63b0.md#insn-008a63c4)
- 新版 `008a63c4`（命令位置の公開資料なし）

~~~diff
- 008a63c4 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 008a63c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a63c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a63c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a63c4 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 008a63c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a63c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a63c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a63c4 bytes 08012d91
+ 008a63c4 bytes 08c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d6f2d025abd0cf968f1e2e54d2c910d"></a>

### [`008a63d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a63d4.md) → [`008a63d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a63d4.md) FUN_008a63d4

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
      "definition_site": "008a63d8",
      "incomplete_value": false,
      "site": "008a63dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a63d8",
      "incomplete_value": false,
      "site": "008a63dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "008a63dc",
      "DATA",
      [
        "storage",
        "00c06b40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a63dc",
      "DATA",
      [
        "storage",
        "00c06bf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a63d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a63d4.md#insn-008a63d8)
- 新版 `008a63d8`（命令位置の公開資料なし）

~~~diff
- 008a63d8 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 008a63d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a63d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a63d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a63d8 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 008a63d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a63d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a63d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a63d8 bytes 08012d91
+ 008a63d8 bytes 08c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-304088985840d82d01e43709eb3ead76"></a>

### [`008a6430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6430.md) → [`008a6430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a6430.md) FUN_008a6430

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
      "definition_site": "008a6444",
      "incomplete_value": false,
      "site": "008a6448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6444",
      "incomplete_value": false,
      "site": "008a6448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "008a6448",
      "DATA",
      [
        "storage",
        "00c06bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a6448",
      "DATA",
      [
        "storage",
        "00c06c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6430.md#insn-008a6444)
- 新版 `008a6444`（命令位置の公開資料なし）

~~~diff
- 008a6444 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 008a6444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a6444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a6444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a6444 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 008a6444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a6444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a6444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a6444 bytes 08012f91
+ 008a6444 bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-300ae2202d98cb61d3c336b0863c5c84"></a>

### [`008a6454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6454.md) → [`008a6454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a6454.md) FUN_008a6454

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
      "definition_site": "008a6458",
      "incomplete_value": false,
      "site": "008a645c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6458",
      "incomplete_value": false,
      "site": "008a645c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
      "008a645c",
      "DATA",
      [
        "storage",
        "00c06bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a645c",
      "DATA",
      [
        "storage",
        "00c06c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6454.md#insn-008a6458)
- 新版 `008a6458`（命令位置の公開資料なし）

~~~diff
- 008a6458 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 008a6458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a6458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a6458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a6458 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 008a6458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a6458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a6458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a6458 bytes 08012f91
+ 008a6458 bytes 08c13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d441ede7552764d5dd0fbd8c42df084"></a>

### [`008a64b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a64b0.md) → [`008a64b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a64b0.md) FUN_008a64b0

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
      "definition_site": "008a64c4",
      "incomplete_value": true,
      "site": "008a64c8",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a64c4",
      "incomplete_value": true,
      "site": "008a64c8",
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
            "const:c40:8"
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
      "008a64c8",
      "DATA",
      [
        "storage",
        "00c06c40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a64c8",
      "DATA",
      [
        "storage",
        "00c06cf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a64c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a64b0.md#insn-008a64c4)
- 新版 `008a64c4`（命令位置の公開資料なし）

~~~diff
- 008a64c4 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 008a64c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a64c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a64c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a64c4 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 008a64c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a64c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a64c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a64c4 bytes 08013191
+ 008a64c4 bytes 08c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc062396e73219bee8bde1c485fa2c9d"></a>

### [`008a64d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a64d4.md) → [`008a64d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a64d4.md) FUN_008a64d4

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
      "definition_site": "008a64d8",
      "incomplete_value": false,
      "site": "008a64dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a64d8",
      "incomplete_value": false,
      "site": "008a64dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      "008a64dc",
      "DATA",
      [
        "storage",
        "00c06c40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a64dc",
      "DATA",
      [
        "storage",
        "00c06cf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a64d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a64d4.md#insn-008a64d8)
- 新版 `008a64d8`（命令位置の公開資料なし）

~~~diff
- 008a64d8 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 008a64d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a64d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a64d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a64d8 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 008a64d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a64d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a64d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a64d8 bytes 08013191
+ 008a64d8 bytes 08c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c191f66d7347c66097a32c1b829c652"></a>

### [`008a652c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a652c.md) → [`008a652c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a652c.md) FUN_008a652c

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
      "definition_site": "008a6538",
      "incomplete_value": false,
      "site": "008a6544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6538",
      "incomplete_value": false,
      "site": "008a6544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
      "008a6544",
      "DATA",
      [
        "storage",
        "00c06cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a6544",
      "DATA",
      [
        "storage",
        "00c06d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a652c.md#insn-008a6538)
- 新版 `008a6538`（命令位置の公開資料なし）

~~~diff
- 008a6538 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 008a6538 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008a6538 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008a6538 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008a6538 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 008a6538 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008a6538 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008a6538 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008a6538 bytes 4a413391
+ 008a6538 bytes 4a013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65e85ec918d9425dd0b29875940b5374"></a>

### [`008a6570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6570.md) → [`008a6570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a6570.md) FUN_008a6570

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
      "definition_site": "008a6588",
      "incomplete_value": false,
      "site": "008a6594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6588",
      "incomplete_value": false,
      "site": "008a6594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "008a6594",
      "DATA",
      [
        "storage",
        "00c06cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a6594",
      "DATA",
      [
        "storage",
        "00c06d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6570.md#insn-008a6588)
- 新版 `008a6588`（命令位置の公開資料なし）

~~~diff
- 008a6588 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 008a6588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a6588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a6588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a6588 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 008a6588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a6588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a6588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a6588 bytes 08413391
+ 008a6588 bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99c887e9502827a6e187af0b40840143"></a>

### [`008a65cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a65cc.md) → [`008a65cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a65cc.md) FUN_008a65cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a65f4",
      "incomplete_value": false,
      "site": "008a65f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a65f4",
      "incomplete_value": false,
      "site": "008a65f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
      "008a65f8",
      "DATA",
      [
        "storage",
        "00c06cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a65f8",
      "DATA",
      [
        "storage",
        "00c06d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a65f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a65cc.md#insn-008a65f4)
- 新版 `008a65f4`（命令位置の公開資料なし）

~~~diff
- 008a65f4 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 008a65f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a65f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a65f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008a65f4 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 008a65f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008a65f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008a65f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a65f4 bytes 29413391
+ 008a65f4 bytes 29013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27b6391783e22e862569a7ab540bd367"></a>

### [`008a6664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6664.md) → [`008a6664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a6664.md) FUN_008a6664

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a6684",
      "incomplete_value": false,
      "site": "008a6688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6684",
      "incomplete_value": false,
      "site": "008a6688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
      "008a6688",
      "DATA",
      [
        "storage",
        "00c06cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a6688",
      "DATA",
      [
        "storage",
        "00c06d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6664.md#insn-008a6684)
- 新版 `008a6684`（命令位置の公開資料なし）

~~~diff
- 008a6684 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 008a6684 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a6684 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a6684 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008a6684 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 008a6684 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008a6684 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008a6684 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a6684 bytes 29413391
+ 008a6684 bytes 29013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe697e9f3e66f90a712cc4efd3f085f9"></a>

### [`008a6c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6c3c.md) → [`008a6c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a6c3c.md) FUN_008a6c3c

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
      "definition_site": "008a6c48",
      "incomplete_value": false,
      "site": "008a6c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6c48",
      "incomplete_value": false,
      "site": "008a6c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
      "008a6c54",
      "DATA",
      [
        "storage",
        "00c06d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a6c54",
      "DATA",
      [
        "storage",
        "00c06e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6c3c.md#insn-008a6c48)
- 新版 `008a6c48`（命令位置の公開資料なし）

~~~diff
- 008a6c48 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 008a6c48 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008a6c48 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008a6c48 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008a6c48 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 008a6c48 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008a6c48 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008a6c48 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008a6c48 bytes 4a413591
+ 008a6c48 bytes 4a013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e35550156c531b8124ed1af64b64e971"></a>

### [`008a6c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6c80.md) → [`008a6c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a6c80.md) FUN_008a6c80

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
      "definition_site": "008a6c98",
      "incomplete_value": false,
      "site": "008a6ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6c98",
      "incomplete_value": false,
      "site": "008a6ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:d50:8"
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
      "008a6ca4",
      "DATA",
      [
        "storage",
        "00c06d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a6ca4",
      "DATA",
      [
        "storage",
        "00c06e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6c80.md#insn-008a6c98)
- 新版 `008a6c98`（命令位置の公開資料なし）

~~~diff
- 008a6c98 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 008a6c98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a6c98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a6c98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a6c98 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 008a6c98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a6c98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a6c98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a6c98 bytes 08413591
+ 008a6c98 bytes 08013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47eb8ead28e61d1ee3149b9cddbbbe2e"></a>

### [`008a6cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6cdc.md) → [`008a6cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a6cdc.md) FUN_008a6cdc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a6d04",
      "incomplete_value": false,
      "site": "008a6d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6d04",
      "incomplete_value": false,
      "site": "008a6d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:d50:8"
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
      "008a6d08",
      "DATA",
      [
        "storage",
        "00c06d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a6d08",
      "DATA",
      [
        "storage",
        "00c06e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6cdc.md#insn-008a6d04)
- 新版 `008a6d04`（命令位置の公開資料なし）

~~~diff
- 008a6d04 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 008a6d04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a6d04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a6d04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008a6d04 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 008a6d04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008a6d04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008a6d04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a6d04 bytes 29413591
+ 008a6d04 bytes 29013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb84bfa5bb7e0ffba1deb5e1145fdae9"></a>

### [`008a6d6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6d6c.md) → [`008a6d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a6/008a6d6c.md) FUN_008a6d6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "008a6d88",
      "incomplete_value": false,
      "site": "008a6d8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a6d88",
      "incomplete_value": false,
      "site": "008a6d8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:d50:8"
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
      "008a6d8c",
      "DATA",
      [
        "storage",
        "00c06d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a6d8c",
      "DATA",
      [
        "storage",
        "00c06e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a6/008a6d6c.md#insn-008a6d88)
- 新版 `008a6d88`（命令位置の公開資料なし）

~~~diff
- 008a6d88 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 008a6d88 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008a6d88 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008a6d88 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008a6d88 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 008a6d88 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008a6d88 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008a6d88 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008a6d88 bytes 4a413591
+ 008a6d88 bytes 4a013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd79bc311311faeda3d0d3c6f9657f9e"></a>

### [`008a7144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a7/008a7144.md) → [`008a7144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a7/008a7144.md) _INIT_167

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008a7180",
      "incomplete_value": true,
      "site": "008a719c",
      "value": [
        "LOAD",
        "16",
        [
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
      "definition_site": "008a7180",
      "incomplete_value": true,
      "site": "008a719c",
      "value": [
        "LOAD",
        "16",
        [
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
      "definition_site": "008a71a4",
      "incomplete_value": true,
      "site": "008a71c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008a71a4",
      "incomplete_value": true,
      "site": "008a71c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008a71e4",
      "incomplete_value": true,
      "site": "008a71fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008a71e4",
      "incomplete_value": true,
      "site": "008a71fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "008a7180",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "008a71a4",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "008a71c4",
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
      "008a7180",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008a71a4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008a71c4",
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

- 旧版 [`008a7170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a7/008a7144.md#insn-008a7170) · [`008a717c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a7/008a7144.md#insn-008a717c) · [`008a7198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a7/008a7144.md#insn-008a7198)
- 新版 `008a7170`（命令位置の公開資料なし） · `008a717c`（命令位置の公開資料なし） · `008a7198`（命令位置の公開資料なし）

~~~diff
- 008a7170 ["COPY", "tmp:0:8", ["const:640:8"]]
- 008a7170 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008a7170 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008a7170 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008a7170 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 008a7170 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008a7170 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008a7170 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008a7170 bytes 73021991
+ 008a7170 bytes 73021c91
- 008a717c ["COPY", "tmp:0:8", ["const:2e4:8"]]
- 008a717c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a717c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a717c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008a717c ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 008a717c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008a717c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008a717c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a717c bytes 29910b91
+ 008a717c bytes 29750b91
- 008a7198 ["COPY", "tmp:0:8", ["const:2f7:8"]]
- 008a7198 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008a7198 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008a7198 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008a7198 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 008a7198 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008a7198 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008a7198 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008a7198 bytes 4add0b91
+ 008a7198 bytes 4ac10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b353b248265b8a09c1b442bc39c9f2b"></a>

### [`008a74d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a7/008a74d4.md) → [`008a74d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a7/008a74d4.md) FUN_008a74d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008a9f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a9f60.md) · 呼出先 3件 [`008a75e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a7/008a75e8.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`008a9f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a9f60.md) · 呼出先 3件 [`008a75e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a7/008a75e8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a75c8",
      "incomplete_value": true,
      "site": "008a75c8",
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
            "const:6d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a75c8",
      "incomplete_value": true,
      "site": "008a75c8",
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
            "const:624:8"
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
      "008a7504",
      "READ",
      [
        "storage",
        "00c24624",
        null,
        "undefined4"
      ]
    ],
    [
      "008a75c8",
      "WRITE",
      [
        "storage",
        "00c24624",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "008a7504",
      "READ",
      [
        "storage",
        "00c246d4",
        null,
        "undefined4"
      ]
    ],
    [
      "008a75c8",
      "WRITE",
      [
        "storage",
        "00c246d4",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a75c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a7/008a74d4.md#insn-008a75c8) · [`008a7504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a7/008a74d4.md#insn-008a7504)
- 新版 `008a75c8`（命令位置の公開資料なし） · `008a7504`（命令位置の公開資料なし）

~~~diff
- 008a75c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:624:8"]]
- 008a75c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:4"]]
+ 008a75c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6d4:8"]]
+ 008a75c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:4"]]
- 008a75c8 bytes aa2606b9
+ 008a75c8 bytes aad606b9
- 008a7504 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:624:8"]]
- 008a7504 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 008a7504 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 008a7504 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6d4:8"]]
+ 008a7504 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 008a7504 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 008a7504 bytes a82646b9
+ 008a7504 bytes a8d646b9
~~~


<a id="compare-c6b4e8bec0a183c1c274bb6c9d178323"></a>

### [`008a80ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a8/008a80ec.md) → [`008a80ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a8/008a80ec.md) FUN_008a80ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008a9c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a9c24.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md)
- 新版 呼出元 1件 [`008a9c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a9c24.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a82ac",
      "incomplete_value": false,
      "site": "008a82b4",
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
            "const:d4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a82ac",
      "incomplete_value": false,
      "site": "008a82b4",
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
            "const:d53:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a82d4",
      "incomplete_value": false,
      "site": "008a82dc",
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
            "const:d2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a82d4",
      "incomplete_value": false,
      "site": "008a82dc",
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
            "const:d25:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008a8344",
      "incomplete_value": false,
      "site": "008a834c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:f72:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a8344",
      "incomplete_value": false,
      "site": "008a834c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:f7b:8"
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
      "008a82ac",
      "PARAM",
      [
        "storage",
        "002a5d53",
        null,
        "string"
      ]
    ],
    [
      "008a82d4",
      "PARAM",
      [
        "storage",
        "002aad25",
        null,
        "string"
      ]
    ],
    [
      "008a8344",
      "PARAM",
      [
        "storage",
        "002acf7b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008a82ac",
      "PARAM",
      [
        "storage",
        "002a5d4c",
        null,
        "string"
      ]
    ],
    [
      "008a82d4",
      "PARAM",
      [
        "storage",
        "002aad2b",
        null,
        "string"
      ]
    ],
    [
      "008a8344",
      "PARAM",
      [
        "storage",
        "002acf72",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a82ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a8/008a80ec.md#insn-008a82ac) · [`008a82d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a8/008a80ec.md#insn-008a82d4) · [`008a8344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a8/008a80ec.md#insn-008a8344)
- 新版 `008a82ac`（命令位置の公開資料なし） · `008a82d4`（命令位置の公開資料なし） · `008a8344`（命令位置の公開資料なし）

~~~diff
- 008a82ac ["COPY", "tmp:0:8", ["const:d53:8"]]
- 008a82ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008a82ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008a82ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008a82ac ["COPY", "tmp:0:8", ["const:d4c:8"]]
+ 008a82ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008a82ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008a82ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008a82ac bytes 214c3591
+ 008a82ac bytes 21303591
- 008a82d4 ["COPY", "tmp:0:8", ["const:d25:8"]]
- 008a82d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008a82d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008a82d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008a82d4 ["COPY", "tmp:0:8", ["const:d2b:8"]]
+ 008a82d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008a82d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008a82d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008a82d4 bytes 21943491
+ 008a82d4 bytes 21ac3491
- 008a8344 ["COPY", "tmp:0:8", ["const:f7b:8"]]
- 008a8344 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008a8344 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008a8344 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008a8344 ["COPY", "tmp:0:8", ["const:f72:8"]]
+ 008a8344 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008a8344 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008a8344 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008a8344 bytes 21ec3d91
+ 008a8344 bytes 21c83d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d261ee302cb18b5ddd8c8374f2c189a"></a>

### [`008a8630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a8/008a8630.md) → [`008a8630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a8/008a8630.md) FUN_008a8630

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008a99d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a99d0.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00445e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445e30.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446784.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md)
- 新版 呼出元 1件 [`008a99d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a99d0.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00445e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445e30.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446784.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008a8664",
      "incomplete_value": true,
      "site": "008a8664",
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
      "definition_site": "008a8664",
      "incomplete_value": true,
      "site": "008a8664",
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
      "definition_site": "008a866c",
      "incomplete_value": false,
      "site": "008a8680",
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
      "definition_site": "008a866c",
      "incomplete_value": false,
      "site": "008a8680",
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
      "definition_site": "008a8674",
      "incomplete_value": false,
      "site": "008a8680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a8674",
      "incomplete_value": false,
      "site": "008a8680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
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
      "008a865c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008a866c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008a8674",
      "PARAM",
      [
        "storage",
        "00c06dc0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008a865c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008a866c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008a8674",
      "PARAM",
      [
        "storage",
        "00c06e70",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a865c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a8/008a8630.md#insn-008a865c) · [`008a866c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a8/008a8630.md#insn-008a866c) · [`008a8674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a8/008a8630.md#insn-008a8674)
- 新版 `008a865c`（命令位置の公開資料なし） · `008a866c`（命令位置の公開資料なし） · `008a8674`（命令位置の公開資料なし）

~~~diff
- 008a865c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008a865c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008a865c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008a865c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008a865c bytes 08dd44f9
+ 008a865c bytes 083d45f9
- 008a866c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008a866c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008a866c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008a866c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008a866c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008a866c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008a866c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008a866c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008a866c bytes 21603691
+ 008a866c bytes 21203991
- 008a8674 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 008a8674 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008a8674 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008a8674 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008a8674 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 008a8674 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008a8674 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008a8674 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008a8674 bytes 42003791
+ 008a8674 bytes 42c03991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98df17bb865f11befd51819c734191ce"></a>

### [`008a8900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a8/008a8900.md) → [`008a8900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a8/008a8900.md) FUN_008a8900

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`008a90c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a90c0.md) · 呼出先 12件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`005f0660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005f0/005f0660.md) [`0062d9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0062d/0062d9b8.md)
- 新版 呼出元 1件 [`008a90c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a90c0.md) · 呼出先 12件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`005f0660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f0/005f0660.md) [`0062d9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9b8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.49% / 新版 99.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008a8dfc",
      "incomplete_value": false,
      "site": "008a8e08",
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
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a8dfc",
      "incomplete_value": false,
      "site": "008a8e08",
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
            "const:210:8"
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
      "008a8e08",
      "DATA",
      [
        "storage",
        "00bf6210",
        null,
        "undefined *"
      ]
    ],
    [
      "008a8e60",
      "READ",
      [
        "storage",
        "00bf6230",
        null,
        "pointer"
      ]
    ],
    [
      "008a8e60",
      "READ",
      [
        "storage",
        "00bf6238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a8e08",
      "DATA",
      [
        "storage",
        "00bf62c0",
        null,
        "undefined *"
      ]
    ],
    [
      "008a8e60",
      "READ",
      [
        "storage",
        "00bf62e0",
        null,
        "pointer"
      ]
    ],
    [
      "008a8e60",
      "READ",
      [
        "storage",
        "00bf62e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a8dfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a8/008a8900.md#insn-008a8dfc)
- 新版 `008a8dfc`（命令位置の公開資料なし）

~~~diff
- 008a8dfc ["COPY", "tmp:0:8", ["const:210:8"]]
- 008a8dfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a8dfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a8dfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a8dfc ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 008a8dfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a8dfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a8dfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a8dfc bytes 08410891
+ 008a8dfc bytes 08010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-617e1e165200b84abf76fa1951cb507a"></a>

### [`008a90c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a90c0.md) → [`008a90c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a90c0.md) FUN_008a90c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008a9c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a9c80.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`008a9c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a9c80.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a94ac",
      "incomplete_value": false,
      "site": "008a94ac",
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
            "const:6d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a94ac",
      "incomplete_value": false,
      "site": "008a94ac",
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
            "const:624:8"
          ]
        ]
      ]
    },
    "ordinal": 65,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008a9678",
      "incomplete_value": true,
      "site": "008a9678",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:909:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008a9678",
      "incomplete_value": true,
      "site": "008a9678",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 85,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008a967c",
      "incomplete_value": true,
      "site": "008a967c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008a967c",
      "incomplete_value": true,
      "site": "008a967c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 86,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008a94ac",
      "WRITE",
      [
        "storage",
        "00c24624",
        null,
        "undefined4"
      ]
    ],
    [
      "008a9564",
      "READ",
      [
        "storage",
        "002a5d53",
        null,
        "string"
      ]
    ],
    [
      "008a9568",
      "READ",
      [
        "storage",
        "002a5d59",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008a94ac",
      "WRITE",
      [
        "storage",
        "00c246d4",
        null,
        "undefined4"
      ]
    ],
    [
      "008a9564",
      "READ",
      [
        "storage",
        "002a5d4c",
        null,
        "string"
      ]
    ],
    [
      "008a9568",
      "READ",
      [
        "storage",
        "002a5d52",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a94ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a90c0.md#insn-008a94ac) · [`008a955c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a90c0.md#insn-008a955c) · [`008a95a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a90c0.md#insn-008a95a0)
- 新版 `008a94ac`（命令位置の公開資料なし） · `008a955c`（命令位置の公開資料なし） · `008a95a0`（命令位置の公開資料なし）

~~~diff
- 008a94ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:624:8"]]
- 008a94ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:4"]]
+ 008a94ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6d4:8"]]
+ 008a94ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:4"]]
- 008a94ac bytes 152506b9
+ 008a94ac bytes 15d506b9
- 008a955c ["COPY", "tmp:0:8", ["const:d53:8"]]
- 008a955c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008a955c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008a955c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008a955c ["COPY", "tmp:0:8", ["const:d4c:8"]]
+ 008a955c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008a955c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008a955c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008a955c bytes 294d3591
+ 008a955c bytes 29313591
- 008a95a0 ["COPY", "tmp:0:8", ["const:d25:8"]]
- 008a95a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a95a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a95a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008a95a0 ["COPY", "tmp:0:8", ["const:d2b:8"]]
+ 008a95a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008a95a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008a95a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a95a0 bytes 08953491
+ 008a95a0 bytes 08ad3491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff504725ec142d4757cf8095d86d1d43"></a>

### [`008a99d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a99d0.md) → [`008a99d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a99d0.md) FUN_008a99d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008aaa18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008aa/008aaa18.md) · 呼出先 8件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00446784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446784.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`008a8630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a8/008a8630.md)
- 新版 呼出元 1件 [`008aaa18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008aa/008aaa18.md) · 呼出先 8件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00446784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446784.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`008a8630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a8/008a8630.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 97.32% / 新版 97.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008a99f4",
      "incomplete_value": true,
      "site": "008a99f4",
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
      "definition_site": "008a99f4",
      "incomplete_value": true,
      "site": "008a99f4",
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
      "008a99f0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008a99fc",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008a9a04",
      "PARAM",
      [
        "storage",
        "00c06dc0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008a99f0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008a99fc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008a9a04",
      "PARAM",
      [
        "storage",
        "00c06e70",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a99f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a99d0.md#insn-008a99f0) · [`008a99fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a99d0.md#insn-008a99fc) · [`008a9a04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a99d0.md#insn-008a9a04)
- 新版 `008a99f0`（命令位置の公開資料なし） · `008a99fc`（命令位置の公開資料なし） · `008a9a04`（命令位置の公開資料なし）

~~~diff
- 008a99f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008a99f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008a99f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008a99f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008a99f0 bytes 08dd44f9
+ 008a99f0 bytes 083d45f9
- 008a99fc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008a99fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008a99fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008a99fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008a99fc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008a99fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008a99fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008a99fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008a99fc bytes 21603691
+ 008a99fc bytes 21203991
- 008a9a04 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 008a9a04 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008a9a04 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008a9a04 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008a9a04 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 008a9a04 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008a9a04 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008a9a04 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008a9a04 bytes 42003791
+ 008a9a04 bytes 42c03991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa0e59245dd1c6d3b813b5459e7865a8"></a>

### [`008a9c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a9c80.md) → [`008a9c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a9c80.md) FUN_008a9c80

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 13件 [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8f8.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00646dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00646/00646dc4.md) [`008a90c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a90c0.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 13件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00646dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646dc4.md) [`008a90c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a90c0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.65% / 新版 96.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a9cb4",
      "incomplete_value": false,
      "site": "008a9cb4",
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
      "definition_site": "008a9cb4",
      "incomplete_value": false,
      "site": "008a9cb4",
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
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008a9ca8",
      "incomplete_value": true,
      "site": "008a9cb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "008a9ca8",
      "incomplete_value": true,
      "site": "008a9cb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008a9cb8",
      "incomplete_value": false,
      "site": "008a9cb8",
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
      "definition_site": "008a9cb8",
      "incomplete_value": false,
      "site": "008a9cb8",
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
      "008a9ca8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008a9cac",
      "READ",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ],
    [
      "008a9cb4",
      "WRITE",
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
      "008a9ca8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008a9cac",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "008a9cb4",
      "WRITE",
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

- 旧版 [`008a9cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a9c80.md#insn-008a9cb4) · [`008a9cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a9c80.md#insn-008a9cb8) · [`008a9d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a9c80.md#insn-008a9d00)
- 新版 `008a9cb4`（命令位置の公開資料なし） · `008a9cb8`（命令位置の公開資料なし） · `008a9d00`（命令位置の公開資料なし）

~~~diff
- 008a9cb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 008a9cb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008a9cb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 008a9cb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008a9cb4 bytes 09d504f9
+ 008a9cb4 bytes 093505f9
- 008a9cb8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:9b8:8"]]
- 008a9cb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008a9cb8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:a78:8"]]
+ 008a9cb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008a9cb8 bytes 6adf04f9
+ 008a9cb8 bytes 6a3f05f9
- 008a9d00 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:9b8:8"]]
- 008a9d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008a9d00 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:a78:8"]]
+ 008a9d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008a9d00 bytes 74df04f9
+ 008a9d00 bytes 743f05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3e4034b0843c1f9e9dec72d67852556"></a>

### [`008a9f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a9f60.md) → [`008a9f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a9f60.md) FUN_008a9f60

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 24件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`0045a2e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045a/0045a2e4.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 24件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0045a2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a2e4.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.21% / 新版 96.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_destination` 6件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008aa994",
      "incomplete_value": false,
      "site": "008aa994",
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
      "definition_site": "008aa994",
      "incomplete_value": false,
      "site": "008aa994",
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
    "ordinal": 90,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008aa998",
      "incomplete_value": false,
      "site": "008aa998",
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
      "definition_site": "008aa998",
      "incomplete_value": false,
      "site": "008aa998",
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
    "ordinal": 91,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008aa994",
      "incomplete_value": false,
      "site": "008aa998",
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
      "definition_site": "008aa994",
      "incomplete_value": false,
      "site": "008aa998",
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
    "ordinal": 91,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008aa364",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008aa36c",
      "READ",
      [
        "storage",
        "00c24f70",
        null,
        "undefined8"
      ]
    ],
    [
      "008aa40c",
      "DATA",
      [
        "storage",
        "00c24174",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008aa364",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008aa36c",
      "READ",
      [
        "storage",
        "00c25030",
        null,
        "undefined8"
      ]
    ],
    [
      "008aa40c",
      "DATA",
      [
        "storage",
        "00c24224",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a9fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a9f60.md#insn-008a9fb0) · [`008a9fb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a9f60.md#insn-008a9fb4) · [`008a9fb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a9f60.md#insn-008a9fb8)
- 新版 `008a9fb0`（命令位置の公開資料なし） · `008a9fb4`（命令位置の公開資料なし） · `008a9fb8`（命令位置の公開資料なし）

~~~diff
- 008a9fb0 ["COPY", "register:40c0:8", ["const:c24000:8"]]
+ 008a9fb0 ["COPY", "register:40c0:8", ["const:c25000:8"]]
- 008a9fb0 bytes d81b00f0
+ 008a9fb0 bytes f81b0090
- 008a9fb4 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008a9fb4 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 008a9fb4 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 008a9fb4 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 008a9fb4 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008a9fb4 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 008a9fb4 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 008a9fb4 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 008a9fb4 bytes 18e33d91
+ 008a9fb4 bytes 18e30091
- 008a9fb8 ["COPY", "register:40a8:8", ["const:c24000:8"]]
+ 008a9fb8 ["COPY", "register:40a8:8", ["const:c25000:8"]]
- 008a9fb8 bytes d51b00f0
+ 008a9fb8 bytes f51b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c611254f800bd0b58253636904d05df6"></a>

### [`008aaa18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008aa/008aaa18.md) → [`008aaa18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008aa/008aaa18.md) FUN_008aaa18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 25件 [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00445d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 25件 [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008ab350",
      "incomplete_value": false,
      "site": "008ab350",
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
      "definition_site": "008ab350",
      "incomplete_value": false,
      "site": "008ab350",
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
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008ab354",
      "incomplete_value": false,
      "site": "008ab354",
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
      "definition_site": "008ab354",
      "incomplete_value": false,
      "site": "008ab354",
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
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ab350",
      "incomplete_value": false,
      "site": "008ab354",
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
      "definition_site": "008ab350",
      "incomplete_value": false,
      "site": "008ab354",
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
      "008aaa58",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008aaa64",
      "READ",
      [
        "storage",
        "00c24f70",
        null,
        "undefined8"
      ]
    ],
    [
      "008aaa78",
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
      "008aaa58",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008aaa64",
      "READ",
      [
        "storage",
        "00c25030",
        null,
        "undefined8"
      ]
    ],
    [
      "008aaa78",
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

- 旧版 [`008aaa40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008aa/008aaa18.md#insn-008aaa40) · [`008aaa44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008aa/008aaa18.md#insn-008aaa44) · [`008aaa60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008aa/008aaa18.md#insn-008aaa60)
- 新版 `008aaa40`（命令位置の公開資料なし） · `008aaa44`（命令位置の公開資料なし） · `008aaa60`（命令位置の公開資料なし）

~~~diff
- 008aaa40 ["COPY", "register:40b8:8", ["const:c24000:8"]]
+ 008aaa40 ["COPY", "register:40b8:8", ["const:c25000:8"]]
- 008aaa40 bytes d71b00d0
+ 008aaa40 bytes d71b00f0
- 008aaa44 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008aaa44 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 008aaa44 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 008aaa44 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 008aaa44 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008aaa44 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 008aaa44 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 008aaa44 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 008aaa44 bytes f7e23d91
+ 008aaa44 bytes f7e20091
- 008aaa60 ["COPY", "register:40c0:8", ["const:c24000:8"]]
+ 008aaa60 ["COPY", "register:40c0:8", ["const:c25000:8"]]
- 008aaa60 bytes d81b00d0
+ 008aaa60 bytes d81b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-646b0014c8eedbd045d5418ef34b9314"></a>

### [`008ac9ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ac/008ac9ec.md) → [`008ac9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ac/008ac9ec.md) FUN_008ac9ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008ac5b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ac/008ac5b4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`008ac5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ac/008ac5b4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "008ac9f8",
      "incomplete_value": false,
      "site": "008ac9fc",
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
      "definition_site": "008ac9f8",
      "incomplete_value": false,
      "site": "008ac9fc",
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
      "008ac9f8",
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
      "008ac9f8",
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

- 旧版 [`008ac9f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ac/008ac9ec.md#insn-008ac9f8)
- 新版 `008ac9f8`（命令位置の公開資料なし）

~~~diff
- 008ac9f8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008ac9f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008ac9f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008ac9f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008ac9f8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 008ac9f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008ac9f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008ac9f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008ac9f8 bytes 00280c91
+ 008ac9f8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-599c4413b2debf812c21ff94d157ad19"></a>

### [`008acbf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ac/008acbf0.md) → [`008acbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ac/008acbf0.md) FUN_008acbf0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008a9c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a9/008a9c80.md) · 呼出先 13件 [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060d/0060d83c.md) [`0072dfbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0072d/0072dfbc.md) [`00831724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00831/00831724.md)
- 新版 呼出元 1件 [`008a9c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a9c80.md) · 呼出先 13件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) [`0072dfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072d/0072dfbc.md) [`00831724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00831/00831724.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.83% / 新版 87.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 28件, `store_destination` 7件, `store_value` 20件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008acc28",
      "incomplete_value": false,
      "site": "008acc34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008acc28",
      "incomplete_value": false,
      "site": "008acc34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "definition_site": "008acc70",
      "incomplete_value": true,
      "site": "008acc70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:895:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008acc70",
      "incomplete_value": true,
      "site": "008acc70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:89c:8"
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
      "definition_site": "008acc88",
      "incomplete_value": true,
      "site": "008acc88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008acc88",
      "incomplete_value": true,
      "site": "008acc88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:772:8"
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
      "008acc34",
      "DATA",
      [
        "storage",
        "00c06de8",
        null,
        "pointer"
      ]
    ],
    [
      "008acc40",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008acc60",
      "READ",
      [
        "storage",
        "002a589c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008acc34",
      "DATA",
      [
        "storage",
        "00c06e98",
        null,
        "pointer"
      ]
    ],
    [
      "008acc40",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008acc60",
      "READ",
      [
        "storage",
        "002a5895",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008acc28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ac/008acbf0.md#insn-008acc28) · [`008acc2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ac/008acbf0.md#insn-008acc2c)
- 新版 `008acc28`（命令位置の公開資料なし） · `008acc2c`（命令位置の公開資料なし）

~~~diff
- 008acc28 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 008acc28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008acc28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008acc28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008acc28 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008acc28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008acc28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008acc28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008acc28 bytes 08a13791
+ 008acc28 bytes 08613a91
- 008acc2c ["COPY", "register:40c0:8", ["const:c24000:8"]]
- 008acc2c bytes d81b0090
+ 008acc2c ["COPY", "register:40c0:8", ["const:c25000:8"]]
+ 008acc2c bytes d81b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-458e1bf95f3881e9b57844e571ec80a0"></a>

### [`008ad8d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ad/008ad8d4.md) → [`008ad8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008ad8d4.md) FUN_008ad8d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065b/0065bff4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ad8ec",
      "incomplete_value": false,
      "site": "008ad8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ad8ec",
      "incomplete_value": false,
      "site": "008ad8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ad928",
      "incomplete_value": false,
      "site": "008ad92c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ad928",
      "incomplete_value": false,
      "site": "008ad92c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "008ad8f0",
      "DATA",
      [
        "storage",
        "00bfad08",
        null,
        "pointer"
      ]
    ],
    [
      "008ad92c",
      "DATA",
      [
        "storage",
        "00bf71e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008ad8f0",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "008ad92c",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ad8ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ad/008ad8d4.md#insn-008ad8ec) · [`008ad928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ad/008ad8d4.md#insn-008ad928)
- 新版 `008ad8ec`（命令位置の公開資料なし） · `008ad928`（命令位置の公開資料なし）

~~~diff
- 008ad8ec ["COPY", "tmp:0:8", ["const:d08:8"]]
- 008ad8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ad8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ad8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ad8ec ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 008ad8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ad8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ad8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ad8ec bytes 08213491
+ 008ad8ec bytes 08e13691
- 008ad928 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 008ad928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ad928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ad928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ad928 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 008ad928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ad928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ad928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ad928 bytes 08a10791
+ 008ad928 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3951416fab02396cf06e204b038fe9f3"></a>

### [`008ad974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ad/008ad974.md) → [`008ad974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008ad974.md) _INIT_168

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
      "definition_site": "008ad9b0",
      "incomplete_value": true,
      "site": "008ad9cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008ad9b0",
      "incomplete_value": true,
      "site": "008ad9cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008ad9d4",
      "incomplete_value": true,
      "site": "008ad9f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008ad9d4",
      "incomplete_value": true,
      "site": "008ad9f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008ad9f4",
      "incomplete_value": true,
      "site": "008ada10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008ad9f4",
      "incomplete_value": true,
      "site": "008ada10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "008ad9b0",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "008ad9d4",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "008ad9f4",
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
      "008ad9b0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008ad9d4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008ad9f4",
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

- 旧版 [`008ad9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ad/008ad974.md#insn-008ad9a0) · [`008ad9a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ad/008ad974.md#insn-008ad9a8)
- 新版 `008ad9a0`（命令位置の公開資料なし） · `008ad9a8`（命令位置の公開資料なし）

~~~diff
- 008ad9a0 ["COPY", "tmp:0:8", ["const:658:8"]]
- 008ad9a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008ad9a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008ad9a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008ad9a0 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 008ad9a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008ad9a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008ad9a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008ad9a0 bytes 73621991
+ 008ad9a0 bytes 73621c91
- 008ad9a8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008ad9a8 bytes c9cfffd0
+ 008ad9a8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008ad9a8 bytes c9cfffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-233ba6b436f42d9924fbc59541a0d2b6"></a>

### [`008add04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ad/008add04.md) → [`008add04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008add04.md) FUN_008add04

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008b1f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b1/008b1f3c.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`008b1f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b1f3c.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.76% / 新版 89.76%

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
      "definition_site": "008add50",
      "incomplete_value": false,
      "site": "008add58",
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
      "definition_site": "008add50",
      "incomplete_value": false,
      "site": "008add58",
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
      "definition_site": "008add7c",
      "incomplete_value": true,
      "site": "008add8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:aaa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008add7c",
      "incomplete_value": true,
      "site": "008add8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ab1:8"
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
      "definition_site": "008add90",
      "incomplete_value": true,
      "site": "008add90",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008add90",
      "incomplete_value": true,
      "site": "008add90",
      "value": [
        "LOAD",
        "8",
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
      "008add58",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "008add7c",
      "READ",
      [
        "storage",
        "002a3ab1",
        null,
        "string"
      ]
    ],
    [
      "008add80",
      "READ",
      [
        "storage",
        "002a3ac0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008add58",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "008add7c",
      "READ",
      [
        "storage",
        "002a3aaa",
        null,
        "string"
      ]
    ],
    [
      "008add80",
      "READ",
      [
        "storage",
        "002a3ab9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008add50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ad/008add04.md#insn-008add50) · [`008add74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ad/008add04.md#insn-008add74) · [`008add78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ad/008add04.md#insn-008add78)
- 新版 `008add50`（命令位置の公開資料なし） · `008add74`（命令位置の公開資料なし）

~~~diff
- 008add50 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 008add50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008add50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008add50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008add50 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 008add50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008add50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008add50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008add50 bytes 08e13191
+ 008add50 bytes 08a13491
- 008add74 ["COPY", "tmp:0:8", ["const:ab1:8"]]
- 008add74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008add74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008add74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008add74 ["COPY", "tmp:0:8", ["const:aaa:8"]]
+ 008add74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008add74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008add74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008add74 bytes 08c52a91
+ 008add74 bytes 08a92a91
- 008add78 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 008add78 bytes 09d0fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-492c5986c3dc19e75082067b9e334319"></a>

### [`008ae87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ae/008ae87c.md) → [`008ae87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ae/008ae87c.md) FUN_008ae87c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008b1f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b1/008b1f3c.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`008b1f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b1f3c.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ae8c0",
      "incomplete_value": false,
      "site": "008ae8c8",
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
      "definition_site": "008ae8c0",
      "incomplete_value": false,
      "site": "008ae8c8",
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
      "definition_site": "008ae8e0",
      "incomplete_value": true,
      "site": "008ae8ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a81:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ae8e0",
      "incomplete_value": true,
      "site": "008ae8ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b15:8"
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
      "definition_site": "008aea0c",
      "incomplete_value": true,
      "site": "008aea0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b3f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008aea0c",
      "incomplete_value": true,
      "site": "008aea0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008ae8c8",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "008ae8e0",
      "READ",
      [
        "storage",
        "002a7b15",
        null,
        "string"
      ]
    ],
    [
      "008ae9fc",
      "READ",
      [
        "storage",
        "0029bab2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008ae8c8",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "008ae8e0",
      "READ",
      [
        "storage",
        "002a7a81",
        null,
        "string"
      ]
    ],
    [
      "008ae9fc",
      "READ",
      [
        "storage",
        "0029bb3f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ae8c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ae/008ae87c.md#insn-008ae8c0) · [`008ae8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ae/008ae87c.md#insn-008ae8d8) · [`008ae9f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ae/008ae87c.md#insn-008ae9f8)
- 新版 `008ae8c0`（命令位置の公開資料なし） · `008ae8d8`（命令位置の公開資料なし） · `008ae9f8`（命令位置の公開資料なし）

~~~diff
- 008ae8c0 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 008ae8c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ae8c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ae8c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ae8c0 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 008ae8c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ae8c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ae8c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ae8c0 bytes 08e13191
+ 008ae8c0 bytes 08a13491
- 008ae8d8 ["COPY", "tmp:0:8", ["const:b15:8"]]
- 008ae8d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ae8d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ae8d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ae8d8 ["COPY", "tmp:0:8", ["const:a81:8"]]
+ 008ae8d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ae8d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ae8d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ae8d8 bytes 29552c91
+ 008ae8d8 bytes 29052a91
- 008ae9f8 ["COPY", "tmp:0:8", ["const:ab2:8"]]
- 008ae9f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ae9f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ae9f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ae9f8 ["COPY", "tmp:0:8", ["const:b3f:8"]]
+ 008ae9f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ae9f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ae9f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ae9f8 bytes 29c92a91
+ 008ae9f8 bytes 29fd2c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-031363ac61abf4bbafcb3e6b825c09f6"></a>

### [`008af36c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008af/008af36c.md) → [`008af36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008af/008af36c.md) FUN_008af36c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008b266c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b2/008b266c.md) · 呼出先 22件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00883d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883d4c.md) [`00883e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883e08.md)
- 新版 呼出元 1件 [`008b266c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b2/008b266c.md) · 呼出先 22件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d4c.md) [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.46% / 新版 96.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008af634",
      "incomplete_value": false,
      "site": "008af634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008af634",
      "incomplete_value": false,
      "site": "008af634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008af78c",
      "incomplete_value": false,
      "site": "008af78c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008af78c",
      "incomplete_value": false,
      "site": "008af78c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e88:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008af97c",
      "incomplete_value": true,
      "site": "008af97c",
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
      "definition_site": "008af97c",
      "incomplete_value": true,
      "site": "008af97c",
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
      "008af3b0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008af3bc",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008af3c4",
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
      "008af3b0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008af3bc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008af3c4",
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

- 旧版 [`008af3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008af/008af36c.md#insn-008af3b0) · [`008af3bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008af/008af36c.md#insn-008af3bc) · [`008af3c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008af/008af36c.md#insn-008af3c4)
- 新版 `008af3b0`（命令位置の公開資料なし） · `008af3bc`（命令位置の公開資料なし） · `008af3c4`（命令位置の公開資料なし）

~~~diff
- 008af3b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008af3b0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008af3b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008af3b0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008af3b0 bytes 00dd44f9
+ 008af3b0 bytes 003d45f9
- 008af3bc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008af3bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008af3bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008af3bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008af3bc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008af3bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008af3bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008af3bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008af3bc bytes 21603691
+ 008af3bc bytes 21203991
- 008af3c4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 008af3c4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008af3c4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008af3c4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008af3c4 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 008af3c4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008af3c4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008af3c4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008af3c4 bytes 42a00791
+ 008af3c4 bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afc0b6e00cfa581ef7ff6ca28e2c98f3"></a>

### [`008afd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008af/008afd10.md) → [`008afd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008af/008afd10.md) FUN_008afd10

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068d/0068d0f8.md) · 呼出先 21件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00447378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447378.md)
- 新版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md) · 呼出先 21件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00447378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447378.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.53% / 新版 99.53%

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
      "definition_site": "008afd5c",
      "incomplete_value": true,
      "site": "008afd5c",
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
      "definition_site": "008afd5c",
      "incomplete_value": true,
      "site": "008afd5c",
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
      "definition_site": "008afd64",
      "incomplete_value": false,
      "site": "008afd74",
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
      "definition_site": "008afd64",
      "incomplete_value": false,
      "site": "008afd74",
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
      "definition_site": "008afd6c",
      "incomplete_value": false,
      "site": "008afd74",
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
      "definition_site": "008afd6c",
      "incomplete_value": false,
      "site": "008afd74",
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
      "008afd58",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008afd64",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008afd6c",
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
      "008afd58",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008afd64",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008afd6c",
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

- 旧版 [`008afd58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008af/008afd10.md#insn-008afd58) · [`008afd64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008af/008afd10.md#insn-008afd64) · [`008afd6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008af/008afd10.md#insn-008afd6c)
- 新版 `008afd58`（命令位置の公開資料なし） · `008afd64`（命令位置の公開資料なし） · `008afd6c`（命令位置の公開資料なし）

~~~diff
- 008afd58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008afd58 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008afd58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008afd58 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008afd58 bytes 00dd44f9
+ 008afd58 bytes 003d45f9
- 008afd64 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008afd64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008afd64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008afd64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008afd64 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008afd64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008afd64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008afd64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008afd64 bytes 21603691
+ 008afd64 bytes 21203991
- 008afd6c ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 008afd6c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008afd6c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008afd6c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008afd6c ["COPY", "tmp:0:8", ["const:298:8"]]
+ 008afd6c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008afd6c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008afd6c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008afd6c bytes 42a00791
+ 008afd6c bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a68fa8c37379e4efce2507fe2b716a0"></a>

### [`008b0960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b0/008b0960.md) → [`008b0960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b0/008b0960.md) FUN_008b0960

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008b5c4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5c4c.md) · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`008b5c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5c4c.md) · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b0ae8",
      "incomplete_value": true,
      "site": "008b0afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008b0ae8",
      "incomplete_value": true,
      "site": "008b0afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b0b00",
      "incomplete_value": true,
      "site": "008b0b00",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008b0b00",
      "incomplete_value": true,
      "site": "008b0b00",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b0f4c",
      "incomplete_value": false,
      "site": "008b0f4c",
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
      "definition_site": "008b0f4c",
      "incomplete_value": false,
      "site": "008b0f4c",
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
    "ordinal": 53,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b0ad4",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008b0ae8",
      "READ",
      [
        "storage",
        "0029e637",
        null,
        "string"
      ]
    ],
    [
      "008b0aec",
      "READ",
      [
        "storage",
        "0029e644",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b0ad4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008b0ae8",
      "READ",
      [
        "storage",
        "0029e6c4",
        null,
        "string"
      ]
    ],
    [
      "008b0aec",
      "READ",
      [
        "storage",
        "0029e6d1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b0acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b0/008b0960.md#insn-008b0acc) · [`008b0ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b0/008b0960.md#insn-008b0ad0) · [`008b0ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b0/008b0960.md#insn-008b0ae0)
- 新版 `008b0acc`（命令位置の公開資料なし） · `008b0ad0`（命令位置の公開資料なし） · `008b0ae0`（命令位置の公開資料なし）

~~~diff
- 008b0acc ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 008b0acc ["COPY", "register:4040:8", ["const:c25000:8"]]
- 008b0acc bytes a81b0090
+ 008b0acc bytes a81b00b0
- 008b0ad0 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008b0ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b0ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b0ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b0ad0 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008b0ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b0ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b0ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b0ad0 bytes 08e13d91
+ 008b0ad0 bytes 08e10091
- 008b0ae0 ["COPY", "tmp:0:8", ["const:637:8"]]
- 008b0ae0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b0ae0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b0ae0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b0ae0 ["COPY", "tmp:0:8", ["const:6c4:8"]]
+ 008b0ae0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b0ae0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b0ae0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b0ae0 bytes 29dd1891
+ 008b0ae0 bytes 29111b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf86ac9981cb2b6f6d143d01d7cf7112"></a>

### [`008b11a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b1/008b11a4.md) → [`008b11a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b11a4.md) FUN_008b11a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008b627c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b627c.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0044a8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a8d8.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`006b5748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b5/006b5748.md)
- 新版 呼出元 1件 [`008b627c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b627c.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006b5748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b5/006b5748.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.76% / 新版 97.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b1418",
      "incomplete_value": true,
      "site": "008b1434",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a92:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b1418",
      "incomplete_value": true,
      "site": "008b1434",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b1534",
      "incomplete_value": true,
      "site": "008b1550",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a92:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b1534",
      "incomplete_value": true,
      "site": "008b1550",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b18c4",
      "incomplete_value": true,
      "site": "008b18c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e67:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b18c4",
      "incomplete_value": true,
      "site": "008b18c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dda:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 85,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b1418",
      "READ",
      [
        "storage",
        "002a7b26",
        null,
        "string"
      ]
    ],
    [
      "008b1460",
      "PARAM",
      [
        "storage",
        "002ab855",
        null,
        null
      ]
    ],
    [
      "008b1534",
      "READ",
      [
        "storage",
        "002a7b26",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b1418",
      "READ",
      [
        "storage",
        "002a7a92",
        null,
        "string"
      ]
    ],
    [
      "008b1460",
      "PARAM",
      [
        "storage",
        "002ab85b",
        null,
        null
      ]
    ],
    [
      "008b1534",
      "READ",
      [
        "storage",
        "002a7a92",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b1414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b1/008b11a4.md#insn-008b1414) · [`008b1460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b1/008b11a4.md#insn-008b1460) · [`008b1530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b1/008b11a4.md#insn-008b1530)
- 新版 `008b1414`（命令位置の公開資料なし） · `008b1460`（命令位置の公開資料なし） · `008b1530`（命令位置の公開資料なし）

~~~diff
- 008b1414 ["COPY", "tmp:0:8", ["const:b26:8"]]
- 008b1414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b1414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b1414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b1414 ["COPY", "tmp:0:8", ["const:a92:8"]]
+ 008b1414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b1414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b1414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b1414 bytes 08992c91
+ 008b1414 bytes 08492a91
- 008b1460 ["COPY", "tmp:0:8", ["const:855:8"]]
- 008b1460 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008b1460 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008b1460 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008b1460 ["COPY", "tmp:0:8", ["const:85b:8"]]
+ 008b1460 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008b1460 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008b1460 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008b1460 bytes 42542191
+ 008b1460 bytes 426c2191
- 008b1530 ["COPY", "tmp:0:8", ["const:b26:8"]]
- 008b1530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b1530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b1530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b1530 ["COPY", "tmp:0:8", ["const:a92:8"]]
+ 008b1530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b1530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b1530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b1530 bytes 08992c91
+ 008b1530 bytes 08492a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a579ce3e591fed294d5aa4e1422d097b"></a>

### [`008b1f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b1/008b1f3c.md) → [`008b1f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b1f3c.md) FUN_008b1f3c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0068c620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068c/0068c620.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00424bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md)
- 新版 呼出元 1件 [`0068c620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c620.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md)

変更の種類 call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.57% / 新版 91.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b1fe8",
      "incomplete_value": true,
      "site": "008b1fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:279:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b1fe8",
      "incomplete_value": true,
      "site": "008b1fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1ec:8"
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
      "definition_site": "008b1fec",
      "incomplete_value": true,
      "site": "008b1fec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008b1fec",
      "incomplete_value": true,
      "site": "008b1fec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b2010",
      "incomplete_value": true,
      "site": "008b2024",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c59:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b2010",
      "incomplete_value": true,
      "site": "008b2024",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bcc:8"
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
      "008b1fc4",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "008b1fd8",
      "READ",
      [
        "storage",
        "002981ec",
        null,
        "string"
      ]
    ],
    [
      "008b1fdc",
      "READ",
      [
        "storage",
        "002981f2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b1fc4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008b1fd8",
      "READ",
      [
        "storage",
        "00298279",
        null,
        "string"
      ]
    ],
    [
      "008b1fdc",
      "READ",
      [
        "storage",
        "0029827f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b1fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b1/008b1f3c.md#insn-008b1fbc) · [`008b1fc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b1/008b1f3c.md#insn-008b1fc0) · [`008b1fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b1/008b1f3c.md#insn-008b1fcc)
- 新版 `008b1fbc`（命令位置の公開資料なし） · `008b1fc0`（命令位置の公開資料なし）

~~~diff
- 008b1fbc ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 008b1fbc ["COPY", "register:4040:8", ["const:c25000:8"]]
- 008b1fbc bytes 881b00f0
+ 008b1fbc bytes a81b0090
- 008b1fc0 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008b1fc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b1fc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b1fc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b1fc0 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 008b1fc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b1fc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b1fc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b1fc0 bytes 08e13d91
+ 008b1fc0 bytes 08e10091
- 008b1fcc ["COPY", "register:4048:8", ["const:298000:8"]]
- 008b1fcc bytes 29cffff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65ce35706da119ca114c823dff943410"></a>

### [`008b266c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b2/008b266c.md) → [`008b266c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b2/008b266c.md) FUN_008b266c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0068c7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068c/0068c7d4.md) · 呼出先 42件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0042bab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042b/0042bab0.md) [`0042cde4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042cde4.md) [`0044aa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044aa9c.md)
- 新版 呼出元 1件 [`0068c7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c7d4.md) · 呼出先 42件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0042bab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bab0.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.31% / 新版 97.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b2764",
      "incomplete_value": true,
      "site": "008b2764",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "008b2764",
      "incomplete_value": true,
      "site": "008b2764",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b2808",
      "incomplete_value": true,
      "site": "008b2808",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b2808",
      "incomplete_value": true,
      "site": "008b2808",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d42:8"
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
      "definition_site": "008b2820",
      "incomplete_value": false,
      "site": "008b2820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b2820",
      "incomplete_value": false,
      "site": "008b2820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:308:8"
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
      "008b2754",
      "READ",
      [
        "storage",
        "002aa4a1",
        null,
        "string"
      ]
    ],
    [
      "008b27f4",
      "READ",
      [
        "storage",
        "002aad42",
        null,
        "string"
      ]
    ],
    [
      "008b2820",
      "DATA",
      [
        "storage",
        "00c07308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b2754",
      "READ",
      [
        "storage",
        "002aa4a7",
        null,
        "string"
      ]
    ],
    [
      "008b27f4",
      "READ",
      [
        "storage",
        "002aad48",
        null,
        "string"
      ]
    ],
    [
      "008b2820",
      "DATA",
      [
        "storage",
        "00c073b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b274c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b2/008b266c.md#insn-008b274c) · [`008b27e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b2/008b266c.md#insn-008b27e8) · [`008b281c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b2/008b266c.md#insn-008b281c)
- 新版 `008b274c`（命令位置の公開資料なし） · `008b27e8`（命令位置の公開資料なし） · `008b281c`（命令位置の公開資料なし）

~~~diff
- 008b274c ["COPY", "tmp:0:8", ["const:4a1:8"]]
- 008b274c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b274c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b274c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b274c ["COPY", "tmp:0:8", ["const:4a7:8"]]
+ 008b274c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b274c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b274c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b274c bytes 29851291
+ 008b274c bytes 299d1291
- 008b27e8 ["COPY", "tmp:0:8", ["const:d42:8"]]
- 008b27e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b27e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b27e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b27e8 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 008b27e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b27e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b27e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b27e8 bytes 29093591
+ 008b27e8 bytes 29213591
- 008b281c ["COPY", "tmp:0:8", ["const:308:8"]]
- 008b281c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b281c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b281c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b281c ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 008b281c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b281c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b281c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b281c bytes 08210c91
+ 008b281c bytes 08e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea72b2bb663b8b642483a76bec9b70f7"></a>

### [`008b3390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b3/008b3390.md) → [`008b3390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b3/008b3390.md) FUN_008b3390

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068d/0068d0f8.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00446074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446074.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448034.md)
- 新版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446074.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.58% / 新版 98.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008b33d4",
      "incomplete_value": true,
      "site": "008b33d4",
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
      "definition_site": "008b33d4",
      "incomplete_value": true,
      "site": "008b33d4",
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
      "definition_site": "008b33dc",
      "incomplete_value": false,
      "site": "008b33ec",
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
      "definition_site": "008b33dc",
      "incomplete_value": false,
      "site": "008b33ec",
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
      "definition_site": "008b33e4",
      "incomplete_value": false,
      "site": "008b33ec",
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
      "definition_site": "008b33e4",
      "incomplete_value": false,
      "site": "008b33ec",
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
      "008b33d0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008b33dc",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b33e4",
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
      "008b33d0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008b33dc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b33e4",
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

- 旧版 [`008b33d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b3/008b3390.md#insn-008b33d0) · [`008b33dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b3/008b3390.md#insn-008b33dc) · [`008b33e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b3/008b3390.md#insn-008b33e4)
- 新版 `008b33d0`（命令位置の公開資料なし） · `008b33dc`（命令位置の公開資料なし） · `008b33e4`（命令位置の公開資料なし）

~~~diff
- 008b33d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008b33d0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008b33d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008b33d0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008b33d0 bytes 00dd44f9
+ 008b33d0 bytes 003d45f9
- 008b33dc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008b33dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008b33dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008b33dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008b33dc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008b33dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008b33dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008b33dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008b33dc bytes 21603691
+ 008b33dc bytes 21203991
- 008b33e4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 008b33e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008b33e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008b33e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008b33e4 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 008b33e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008b33e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008b33e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008b33e4 bytes 42a00791
+ 008b33e4 bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fc01e7c7fcb03ae9b361c157583e94b"></a>

### [`008b3a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b3/008b3a28.md) → [`008b3a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b3/008b3a28.md) FUN_008b3a28

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068d/0068d0f8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00447a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447a10.md) [`0044a8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a8d8.md)
- 新版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.61% / 新版 99.61%

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
      "definition_site": "008b4128",
      "incomplete_value": true,
      "site": "008b4128",
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
      "definition_site": "008b4128",
      "incomplete_value": true,
      "site": "008b4128",
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
    "ordinal": 68,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008b4130",
      "incomplete_value": false,
      "site": "008b4140",
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
      "definition_site": "008b4130",
      "incomplete_value": false,
      "site": "008b4140",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008b4138",
      "incomplete_value": false,
      "site": "008b4140",
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
      "definition_site": "008b4138",
      "incomplete_value": false,
      "site": "008b4140",
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
    "ordinal": 29,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b4124",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008b4130",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b4138",
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
      "008b4124",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008b4130",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b4138",
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

- 旧版 [`008b4124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b3/008b3a28.md#insn-008b4124) · [`008b4130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b3/008b3a28.md#insn-008b4130) · [`008b4138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b3/008b3a28.md#insn-008b4138)
- 新版 `008b4124`（命令位置の公開資料なし） · `008b4130`（命令位置の公開資料なし） · `008b4138`（命令位置の公開資料なし）

~~~diff
- 008b4124 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008b4124 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008b4124 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008b4124 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008b4124 bytes 00dd44f9
+ 008b4124 bytes 003d45f9
- 008b4130 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008b4130 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008b4130 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008b4130 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008b4130 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008b4130 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008b4130 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008b4130 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008b4130 bytes 21603691
+ 008b4130 bytes 21203991
- 008b4138 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 008b4138 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008b4138 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008b4138 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008b4138 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 008b4138 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008b4138 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008b4138 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008b4138 bytes 42a00791
+ 008b4138 bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39ac91502919da7afeaa777583035505"></a>

### [`008b4224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b4224.md) → [`008b4224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4224.md) FUN_008b4224

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008af0b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008af/008af0b4.md) [`008b0960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b0/008b0960.md) [`008b4610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b4610.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`008af0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008af/008af0b4.md) [`008b0960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b0/008b0960.md) [`008b4610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4610.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "008b4230",
      "incomplete_value": false,
      "site": "008b4234",
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
      "definition_site": "008b4230",
      "incomplete_value": false,
      "site": "008b4234",
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
      "008b4230",
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
      "008b4230",
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

- 旧版 [`008b4230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b4224.md#insn-008b4230)
- 新版 `008b4230`（命令位置の公開資料なし）

~~~diff
- 008b4230 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008b4230 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b4230 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b4230 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b4230 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 008b4230 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4230 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4230 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b4230 bytes 00280c91
+ 008b4230 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-132f66bc8c4d13d5c162ac64f881c27a"></a>

### [`008b450c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b450c.md) → [`008b450c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b450c.md) FUN_008b450c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008b4328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b4328.md) [`008b4e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b4e00.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`008b4328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4328.md) [`008b4e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4e00.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "008b4518",
      "incomplete_value": false,
      "site": "008b451c",
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
      "definition_site": "008b4518",
      "incomplete_value": false,
      "site": "008b451c",
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
      "008b4518",
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
      "008b4518",
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

- 旧版 [`008b4518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b450c.md#insn-008b4518)
- 新版 `008b4518`（命令位置の公開資料なし）

~~~diff
- 008b4518 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008b4518 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b4518 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b4518 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b4518 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 008b4518 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4518 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4518 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b4518 bytes 00280c91
+ 008b4518 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-782c03930a396baa1a9a25285b1820e7"></a>

### [`008b45fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b45fc.md) → [`008b45fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b45fc.md) FUN_008b45fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008b0550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b0/008b0550.md) [`008b4c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b4c78.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`008b0550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b0/008b0550.md) [`008b4c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4c78.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "008b4608",
      "incomplete_value": false,
      "site": "008b460c",
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
      "definition_site": "008b4608",
      "incomplete_value": false,
      "site": "008b460c",
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
      "008b4608",
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
      "008b4608",
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

- 旧版 [`008b4608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b45fc.md#insn-008b4608)
- 新版 `008b4608`（命令位置の公開資料なし）

~~~diff
- 008b4608 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008b4608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b4608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b4608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b4608 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 008b4608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b4608 bytes 00280c91
+ 008b4608 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96bbbb25188a8af11d3a3cc4edccfcb0"></a>

### [`008b47cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b47cc.md) → [`008b47cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b47cc.md) FUN_008b47cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008ae87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ae/008ae87c.md) [`008b0550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b0/008b0550.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`008ae87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ae/008ae87c.md) [`008b0550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b0/008b0550.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "008b47d8",
      "incomplete_value": false,
      "site": "008b47dc",
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
      "definition_site": "008b47d8",
      "incomplete_value": false,
      "site": "008b47dc",
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
      "008b47d8",
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
      "008b47d8",
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

- 旧版 [`008b47d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b47cc.md#insn-008b47d8)
- 新版 `008b47d8`（命令位置の公開資料なし）

~~~diff
- 008b47d8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008b47d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b47d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b47d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b47d8 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 008b47d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b47d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b47d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b47d8 bytes 00280c91
+ 008b47d8 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-814f63486f9bdcefeb3f393cb20d616b"></a>

### [`008b49c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b49c4.md) → [`008b49c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b49c4.md) FUN_008b49c4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008b47e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b47e0.md) [`008b4f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b4f48.md) [`008b6558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6558.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`008b47e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b47e0.md) [`008b4f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4f48.md) [`008b6558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6558.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "008b49d0",
      "incomplete_value": false,
      "site": "008b49d4",
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
      "definition_site": "008b49d0",
      "incomplete_value": false,
      "site": "008b49d4",
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
      "008b49d0",
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
      "008b49d0",
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

- 旧版 [`008b49d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b49c4.md#insn-008b49d0)
- 新版 `008b49d0`（命令位置の公開資料なし）

~~~diff
- 008b49d0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008b49d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b49d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b49d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b49d0 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 008b49d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b49d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b49d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b49d0 bytes 00280c91
+ 008b49d0 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd1116893f60fd02eabe105790c0c06a"></a>

### [`008b4c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b4c10.md) → [`008b4c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4c10.md) FUN_008b4c10

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008b4a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b4a2c.md) [`008b50f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b50f8.md) [`008b635c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b635c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`008b4a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4a2c.md) [`008b50f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b50f8.md) [`008b635c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b635c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "008b4c1c",
      "incomplete_value": false,
      "site": "008b4c20",
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
      "definition_site": "008b4c1c",
      "incomplete_value": false,
      "site": "008b4c20",
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
      "008b4c1c",
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
      "008b4c1c",
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

- 旧版 [`008b4c1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b4/008b4c10.md#insn-008b4c1c)
- 新版 `008b4c1c`（命令位置の公開資料なし）

~~~diff
- 008b4c1c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008b4c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b4c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b4c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b4c1c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 008b4c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b4c1c bytes 00280c91
+ 008b4c1c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f11343b63d7588e960d64d546add1de"></a>

### [`008b52ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b52ac.md) → [`008b52ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b52ac.md) FUN_008b52ac

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
      "definition_site": "008b52d0",
      "incomplete_value": false,
      "site": "008b52d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b52d0",
      "incomplete_value": false,
      "site": "008b52d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "008b52d0",
      "DATA",
      [
        "storage",
        "00c06e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b52d0",
      "DATA",
      [
        "storage",
        "00c06eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b52cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b52ac.md#insn-008b52cc)
- 新版 `008b52cc`（命令位置の公開資料なし）

~~~diff
- 008b52cc ["COPY", "tmp:0:8", ["const:e08:8"]]
- 008b52cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b52cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b52cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b52cc ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 008b52cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b52cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b52cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b52cc bytes 08213891
+ 008b52cc bytes 08e13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76ba6c898bbe4fc86670acfb111e4257"></a>

### [`008b52e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b52e0.md) → [`008b52e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b52e0.md) FUN_008b52e0

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
      "definition_site": "008b52ec",
      "incomplete_value": false,
      "site": "008b52ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b52ec",
      "incomplete_value": false,
      "site": "008b52ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "008b52ec",
      "DATA",
      [
        "storage",
        "00c06e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b52ec",
      "DATA",
      [
        "storage",
        "00c06eb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b52e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b52e0.md#insn-008b52e8)
- 新版 `008b52e8`（命令位置の公開資料なし）

~~~diff
- 008b52e8 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 008b52e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b52e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b52e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b52e8 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 008b52e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b52e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b52e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b52e8 bytes 29213891
+ 008b52e8 bytes 29e13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c720e400883d7afbd9abcc440c4eebed"></a>

### [`008b542c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b542c.md) → [`008b542c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b542c.md) FUN_008b542c

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
      "definition_site": "008b5450",
      "incomplete_value": false,
      "site": "008b5450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5450",
      "incomplete_value": false,
      "site": "008b5450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e88:8"
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
      "008b5450",
      "DATA",
      [
        "storage",
        "00c06e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5450",
      "DATA",
      [
        "storage",
        "00c06f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b544c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b542c.md#insn-008b544c)
- 新版 `008b544c`（命令位置の公開資料なし）

~~~diff
- 008b544c ["COPY", "tmp:0:8", ["const:e88:8"]]
- 008b544c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b544c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b544c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b544c ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 008b544c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b544c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b544c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b544c bytes 08213a91
+ 008b544c bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cef6a1af1664a3d2ebc7be802c3ab041"></a>

### [`008b5460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5460.md) → [`008b5460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5460.md) FUN_008b5460

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
      "definition_site": "008b546c",
      "incomplete_value": false,
      "site": "008b546c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b546c",
      "incomplete_value": false,
      "site": "008b546c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e88:8"
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
      "008b546c",
      "DATA",
      [
        "storage",
        "00c06e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b546c",
      "DATA",
      [
        "storage",
        "00c06f38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5460.md#insn-008b5468)
- 新版 `008b5468`（命令位置の公開資料なし）

~~~diff
- 008b5468 ["COPY", "tmp:0:8", ["const:e88:8"]]
- 008b5468 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b5468 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b5468 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b5468 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 008b5468 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5468 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5468 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b5468 bytes 29213a91
+ 008b5468 bytes 29e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4ce56525cf2bc01e65cf426ecc91a79"></a>

### [`008b5528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5528.md) → [`008b5528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5528.md) FUN_008b5528

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
      "definition_site": "008b5548",
      "incomplete_value": false,
      "site": "008b554c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5548",
      "incomplete_value": false,
      "site": "008b554c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "008b554c",
      "DATA",
      [
        "storage",
        "00c06f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b554c",
      "DATA",
      [
        "storage",
        "00c06fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5528.md#insn-008b5548)
- 新版 `008b5548`（命令位置の公開資料なし）

~~~diff
- 008b5548 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 008b5548 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5548 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5548 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5548 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 008b5548 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5548 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5548 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5548 bytes 08213c91
+ 008b5548 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56d5b75e20c230c3cfb516d34d1d93d9"></a>

### [`008b5560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5560.md) → [`008b5560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5560.md) FUN_008b5560

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
      "definition_site": "008b5564",
      "incomplete_value": false,
      "site": "008b5568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5564",
      "incomplete_value": false,
      "site": "008b5568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "008b5568",
      "DATA",
      [
        "storage",
        "00c06f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5568",
      "DATA",
      [
        "storage",
        "00c06fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5560.md#insn-008b5564)
- 新版 `008b5564`（命令位置の公開資料なし）

~~~diff
- 008b5564 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 008b5564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5564 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 008b5564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5564 bytes 08213c91
+ 008b5564 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e488f1229d0c8de685c1beec4f68a4f8"></a>

### [`008b5580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5580.md) → [`008b5580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5580.md) FUN_008b5580

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.83% / 新版 93.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b56b0",
      "incomplete_value": true,
      "site": "008b56b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aa6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b56b0",
      "incomplete_value": true,
      "site": "008b56b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b3a:8"
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
      "definition_site": "008b5734",
      "incomplete_value": true,
      "site": "008b5734",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e77:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5734",
      "incomplete_value": true,
      "site": "008b5734",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dea:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008b5758",
      "incomplete_value": false,
      "site": "008b5758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5758",
      "incomplete_value": false,
      "site": "008b5758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "008b5698",
      "READ",
      [
        "storage",
        "002a7b3a",
        null,
        "string"
      ]
    ],
    [
      "008b56d4",
      "DATA",
      [
        "storage",
        "00c06ff8",
        null,
        "undefined *"
      ]
    ],
    [
      "008b571c",
      "READ",
      [
        "storage",
        "00292dea",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b5698",
      "READ",
      [
        "storage",
        "002a7aa6",
        null,
        "string"
      ]
    ],
    [
      "008b56d4",
      "DATA",
      [
        "storage",
        "00c070a8",
        null,
        "undefined *"
      ]
    ],
    [
      "008b571c",
      "READ",
      [
        "storage",
        "00292e77",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5580.md#insn-008b5690) · [`008b56c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5580.md#insn-008b56c8) · [`008b56cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5580.md#insn-008b56cc)
- 新版 `008b5690`（命令位置の公開資料なし） · `008b56c8`（命令位置の公開資料なし） · `008b56cc`（命令位置の公開資料なし）

~~~diff
- 008b5690 ["COPY", "tmp:0:8", ["const:b3a:8"]]
- 008b5690 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b5690 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b5690 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b5690 ["COPY", "tmp:0:8", ["const:aa6:8"]]
+ 008b5690 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5690 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5690 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b5690 bytes 29e92c91
+ 008b5690 bytes 29992a91
- 008b56c8 ["COPY", "register:4048:8", ["const:c06000:8"]]
+ 008b56c8 ["COPY", "register:4048:8", ["const:c07000:8"]]
- 008b56c8 bytes 891a00b0
+ 008b56c8 bytes 891a00d0
- 008b56cc ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 008b56cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b56cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b56cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b56cc ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 008b56cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b56cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b56cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b56cc bytes 29e13f91
+ 008b56cc bytes 29a10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e40b19226b6834608462dba91eb8bfe6"></a>

### [`008b5a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5a6c.md) → [`008b5a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5a6c.md) FUN_008b5a6c

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
      "definition_site": "008b5a8c",
      "incomplete_value": false,
      "site": "008b5a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5a8c",
      "incomplete_value": false,
      "site": "008b5a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "008b5a90",
      "DATA",
      [
        "storage",
        "00c06f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5a90",
      "DATA",
      [
        "storage",
        "00c07028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5a88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5a6c.md#insn-008b5a88) · [`008b5a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5a6c.md#insn-008b5a8c)
- 新版 `008b5a88`（命令位置の公開資料なし） · `008b5a8c`（命令位置の公開資料なし）

~~~diff
- 008b5a88 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008b5a88 ["COPY", "register:4040:8", ["const:c07000:8"]]
- 008b5a88 bytes 881a00b0
+ 008b5a88 bytes 881a00d0
- 008b5a8c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008b5a8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5a8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5a8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5a8c ["COPY", "tmp:0:8", ["const:28:8"]]
+ 008b5a8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5a8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5a8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5a8c bytes 08e13d91
+ 008b5a8c bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64360700d98bccc0c91b152c0cf43e24"></a>

### [`008b5aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5aa4.md) → [`008b5aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5aa4.md) FUN_008b5aa4

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
      "definition_site": "008b5aa8",
      "incomplete_value": false,
      "site": "008b5aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5aa8",
      "incomplete_value": false,
      "site": "008b5aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "008b5aac",
      "DATA",
      [
        "storage",
        "00c06f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5aac",
      "DATA",
      [
        "storage",
        "00c07028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5aa4.md#insn-008b5aa4) · [`008b5aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5aa4.md#insn-008b5aa8)
- 新版 `008b5aa4`（命令位置の公開資料なし） · `008b5aa8`（命令位置の公開資料なし）

~~~diff
- 008b5aa4 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008b5aa4 ["COPY", "register:4040:8", ["const:c07000:8"]]
- 008b5aa4 bytes 881a00b0
+ 008b5aa4 bytes 881a00d0
- 008b5aa8 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 008b5aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5aa8 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 008b5aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5aa8 bytes 08e13d91
+ 008b5aa8 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c656e95438e6f8a7fdcf8b0c357a60d"></a>

### [`008b5b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5b68.md) → [`008b5b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5b68.md) FUN_008b5b68

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
      "definition_site": "008b5b6c",
      "incomplete_value": false,
      "site": "008b5b70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5b6c",
      "incomplete_value": false,
      "site": "008b5b70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
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
      "008b5b70",
      "DATA",
      [
        "storage",
        "00c06ff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5b70",
      "DATA",
      [
        "storage",
        "00c070a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5b68.md#insn-008b5b68) · [`008b5b6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5b68.md#insn-008b5b6c)
- 新版 `008b5b68`（命令位置の公開資料なし） · `008b5b6c`（命令位置の公開資料なし）

~~~diff
- 008b5b68 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008b5b68 ["COPY", "register:4040:8", ["const:c07000:8"]]
- 008b5b68 bytes 881a00b0
+ 008b5b68 bytes 881a00d0
- 008b5b6c ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 008b5b6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5b6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5b6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5b6c ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 008b5b6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5b6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5b6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5b6c bytes 08e13f91
+ 008b5b6c bytes 08a10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f255113ae3eb428b91b4112ae988bad"></a>

### [`008b5bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5bf4.md) → [`008b5bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5bf4.md) FUN_008b5bf4

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
      "definition_site": "008b5c14",
      "incomplete_value": false,
      "site": "008b5c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5c14",
      "incomplete_value": false,
      "site": "008b5c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "008b5c18",
      "DATA",
      [
        "storage",
        "00c07078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5c18",
      "DATA",
      [
        "storage",
        "00c07128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5bf4.md#insn-008b5c14)
- 新版 `008b5c14`（命令位置の公開資料なし）

~~~diff
- 008b5c14 ["COPY", "tmp:0:8", ["const:78:8"]]
- 008b5c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5c14 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 008b5c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5c14 bytes 08e10191
+ 008b5c14 bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbceff88bd45281c369f48d24afd6210"></a>

### [`008b5c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5c2c.md) → [`008b5c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5c2c.md) FUN_008b5c2c

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
      "definition_site": "008b5c30",
      "incomplete_value": false,
      "site": "008b5c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5c30",
      "incomplete_value": false,
      "site": "008b5c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "008b5c34",
      "DATA",
      [
        "storage",
        "00c07078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5c34",
      "DATA",
      [
        "storage",
        "00c07128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5c2c.md#insn-008b5c30)
- 新版 `008b5c30`（命令位置の公開資料なし）

~~~diff
- 008b5c30 ["COPY", "tmp:0:8", ["const:78:8"]]
- 008b5c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5c30 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 008b5c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5c30 bytes 08e10191
+ 008b5c30 bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ecb3ef89c08db3716eadce550a56d1a"></a>

### [`008b5d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5d18.md) → [`008b5d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5d18.md) FUN_008b5d18

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
      "definition_site": "008b5d3c",
      "incomplete_value": false,
      "site": "008b5d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5d3c",
      "incomplete_value": false,
      "site": "008b5d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "008b5d3c",
      "DATA",
      [
        "storage",
        "00c07108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5d3c",
      "DATA",
      [
        "storage",
        "00c071b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5d18.md#insn-008b5d38)
- 新版 `008b5d38`（命令位置の公開資料なし）

~~~diff
- 008b5d38 ["COPY", "tmp:0:8", ["const:108:8"]]
- 008b5d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5d38 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 008b5d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5d38 bytes 08210491
+ 008b5d38 bytes 08e10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c5a60f73acae497c494b525562da71f"></a>

### [`008b5d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5d4c.md) → [`008b5d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5d4c.md) FUN_008b5d4c

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
      "definition_site": "008b5d58",
      "incomplete_value": false,
      "site": "008b5d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5d58",
      "incomplete_value": false,
      "site": "008b5d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "008b5d58",
      "DATA",
      [
        "storage",
        "00c07108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5d58",
      "DATA",
      [
        "storage",
        "00c071b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5d4c.md#insn-008b5d54)
- 新版 `008b5d54`（命令位置の公開資料なし）

~~~diff
- 008b5d54 ["COPY", "tmp:0:8", ["const:108:8"]]
- 008b5d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b5d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b5d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b5d54 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 008b5d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b5d54 bytes 29210491
+ 008b5d54 bytes 29e10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17b73cd012162bd680e11465be728952"></a>

### [`008b5d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5d68.md) → [`008b5d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5d68.md) FUN_008b5d68

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`008865b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/008865b0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.80% / 新版 85.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b5e44",
      "incomplete_value": true,
      "site": "008b5e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c63:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5e44",
      "incomplete_value": true,
      "site": "008b5e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c6c:8"
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
      "definition_site": "008b5e48",
      "incomplete_value": true,
      "site": "008b5e48",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008b5e48",
      "incomplete_value": true,
      "site": "008b5e48",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008b5e60",
      "incomplete_value": false,
      "site": "008b5e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5e60",
      "incomplete_value": false,
      "site": "008b5e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "008b5e04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008b5e98"
      ]
    ],
    [
      "008b5e24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008b5f0c"
      ]
    ],
    [
      "008b5e34",
      "READ",
      [
        "storage",
        "002a9c6c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b5e04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b5e98"
      ]
    ],
    [
      "008b5e24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b5f0c"
      ]
    ],
    [
      "008b5e34",
      "READ",
      [
        "storage",
        "002a9c63",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5d68.md#insn-008b5e2c) · [`008b5e5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5d68.md#insn-008b5e5c) · [`008b5e98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b5/008b5d68.md#insn-008b5e98)
- 新版 `008b5e2c`（命令位置の公開資料なし） · `008b5e5c`（命令位置の公開資料なし）

~~~diff
- 008b5e2c ["COPY", "tmp:0:8", ["const:c6c:8"]]
- 008b5e2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b5e2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b5e2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b5e2c ["COPY", "tmp:0:8", ["const:c63:8"]]
+ 008b5e2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5e2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5e2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b5e2c bytes 29b13191
+ 008b5e2c bytes 298d3191
- 008b5e5c ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 008b5e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5e5c ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 008b5e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5e5c bytes 08e10791
+ 008b5e5c bytes 08a10a91
- 008b5e98 ["COPY", "register:4048:8", ["const:299000:8"]]
- 008b5e98 bytes 29cfff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a51c54aed03454bd2ca76fbb7784de0e"></a>

### [`008b60b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b60b4.md) → [`008b60b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b60b4.md) FUN_008b60b4

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
      "definition_site": "008b60d8",
      "incomplete_value": false,
      "site": "008b60d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b60d8",
      "incomplete_value": false,
      "site": "008b60d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b60d8",
      "DATA",
      [
        "storage",
        "00c07178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b60d8",
      "DATA",
      [
        "storage",
        "00c07228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b60d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b60b4.md#insn-008b60d4)
- 新版 `008b60d4`（命令位置の公開資料なし）

~~~diff
- 008b60d4 ["COPY", "tmp:0:8", ["const:178:8"]]
- 008b60d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b60d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b60d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b60d4 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 008b60d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b60d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b60d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b60d4 bytes 08e10591
+ 008b60d4 bytes 08a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73038c977fe66b16c145d097038fa065"></a>

### [`008b60e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b60e8.md) → [`008b60e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b60e8.md) FUN_008b60e8

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
      "definition_site": "008b60f4",
      "incomplete_value": false,
      "site": "008b60f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b60f4",
      "incomplete_value": false,
      "site": "008b60f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b60f4",
      "DATA",
      [
        "storage",
        "00c07178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b60f4",
      "DATA",
      [
        "storage",
        "00c07228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b60f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b60e8.md#insn-008b60f0)
- 新版 `008b60f0`（命令位置の公開資料なし）

~~~diff
- 008b60f0 ["COPY", "tmp:0:8", ["const:178:8"]]
- 008b60f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b60f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b60f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b60f0 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 008b60f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b60f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b60f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b60f0 bytes 29e10591
+ 008b60f0 bytes 29a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-736680d9e9c45649ac74309b2bd60d34"></a>

### [`008b6170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6170.md) → [`008b6170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6170.md) FUN_008b6170

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
      "definition_site": "008b6194",
      "incomplete_value": false,
      "site": "008b6194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6194",
      "incomplete_value": false,
      "site": "008b6194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b6194",
      "DATA",
      [
        "storage",
        "00c071f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6194",
      "DATA",
      [
        "storage",
        "00c072a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6170.md#insn-008b6190)
- 新版 `008b6190`（命令位置の公開資料なし）

~~~diff
- 008b6190 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 008b6190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6190 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 008b6190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6190 bytes 08e10791
+ 008b6190 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be49ccee1702ee5c8e03dc7b11e68113"></a>

### [`008b61a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b61a4.md) → [`008b61a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b61a4.md) FUN_008b61a4

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
      "definition_site": "008b61b0",
      "incomplete_value": false,
      "site": "008b61b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b61b0",
      "incomplete_value": false,
      "site": "008b61b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b61b0",
      "DATA",
      [
        "storage",
        "00c071f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b61b0",
      "DATA",
      [
        "storage",
        "00c072a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b61ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b61a4.md#insn-008b61ac)
- 新版 `008b61ac`（命令位置の公開資料なし）

~~~diff
- 008b61ac ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 008b61ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b61ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b61ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b61ac ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 008b61ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b61ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b61ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b61ac bytes 29e10791
+ 008b61ac bytes 29a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f58290cee95f318e26e5bc73d921e1d"></a>

### [`008b622c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b622c.md) → [`008b622c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b622c.md) FUN_008b622c

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
      "definition_site": "008b6250",
      "incomplete_value": false,
      "site": "008b6250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6250",
      "incomplete_value": false,
      "site": "008b6250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b6250",
      "DATA",
      [
        "storage",
        "00c07278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6250",
      "DATA",
      [
        "storage",
        "00c07328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b624c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b622c.md#insn-008b624c)
- 新版 `008b624c`（命令位置の公開資料なし）

~~~diff
- 008b624c ["COPY", "tmp:0:8", ["const:278:8"]]
- 008b624c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b624c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b624c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b624c ["COPY", "tmp:0:8", ["const:328:8"]]
+ 008b624c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b624c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b624c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b624c bytes 08e10991
+ 008b624c bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77f9d06ca7f8b0a1c3c6f658fbdcde5d"></a>

### [`008b6260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6260.md) → [`008b6260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6260.md) FUN_008b6260

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
      "definition_site": "008b626c",
      "incomplete_value": false,
      "site": "008b626c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b626c",
      "incomplete_value": false,
      "site": "008b626c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b626c",
      "DATA",
      [
        "storage",
        "00c07278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b626c",
      "DATA",
      [
        "storage",
        "00c07328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6260.md#insn-008b6268)
- 新版 `008b6268`（命令位置の公開資料なし）

~~~diff
- 008b6268 ["COPY", "tmp:0:8", ["const:278:8"]]
- 008b6268 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6268 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6268 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b6268 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 008b6268 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6268 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6268 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6268 bytes 29e10991
+ 008b6268 bytes 29a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c55964014c28421d7d54ff0d7d59489"></a>

### [`008b6750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6750.md) → [`008b6750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6750.md) FUN_008b6750

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
      "definition_site": "008b6774",
      "incomplete_value": false,
      "site": "008b6774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6774",
      "incomplete_value": false,
      "site": "008b6774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b6774",
      "DATA",
      [
        "storage",
        "00c07308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6774",
      "DATA",
      [
        "storage",
        "00c073b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6750.md#insn-008b6770)
- 新版 `008b6770`（命令位置の公開資料なし）

~~~diff
- 008b6770 ["COPY", "tmp:0:8", ["const:308:8"]]
- 008b6770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6770 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 008b6770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6770 bytes 08210c91
+ 008b6770 bytes 08e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0a31f8267eef4d8594fb2406936ec93"></a>

### [`008b6784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6784.md) → [`008b6784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6784.md) FUN_008b6784

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
      "definition_site": "008b6790",
      "incomplete_value": false,
      "site": "008b6790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6790",
      "incomplete_value": false,
      "site": "008b6790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b6790",
      "DATA",
      [
        "storage",
        "00c07308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6790",
      "DATA",
      [
        "storage",
        "00c073b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b678c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6784.md#insn-008b678c)
- 新版 `008b678c`（命令位置の公開資料なし）

~~~diff
- 008b678c ["COPY", "tmp:0:8", ["const:308:8"]]
- 008b678c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b678c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b678c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b678c ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 008b678c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b678c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b678c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b678c bytes 29210c91
+ 008b678c bytes 29e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5ab440676f381f3f26139434c5aebd9"></a>

### [`008b6814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6814.md) → [`008b6814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6814.md) FUN_008b6814

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
      "definition_site": "008b6838",
      "incomplete_value": false,
      "site": "008b6838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6838",
      "incomplete_value": false,
      "site": "008b6838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b6838",
      "DATA",
      [
        "storage",
        "00c07388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6838",
      "DATA",
      [
        "storage",
        "00c07438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6814.md#insn-008b6834)
- 新版 `008b6834`（命令位置の公開資料なし）

~~~diff
- 008b6834 ["COPY", "tmp:0:8", ["const:388:8"]]
- 008b6834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6834 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 008b6834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6834 bytes 08210e91
+ 008b6834 bytes 08e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5742218e3f3d23650c2837b5c25ab21b"></a>

### [`008b6848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6848.md) → [`008b6848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6848.md) FUN_008b6848

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
      "definition_site": "008b6854",
      "incomplete_value": false,
      "site": "008b6854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6854",
      "incomplete_value": false,
      "site": "008b6854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b6854",
      "DATA",
      [
        "storage",
        "00c07388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6854",
      "DATA",
      [
        "storage",
        "00c07438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6848.md#insn-008b6850)
- 新版 `008b6850`（命令位置の公開資料なし）

~~~diff
- 008b6850 ["COPY", "tmp:0:8", ["const:388:8"]]
- 008b6850 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6850 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6850 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b6850 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 008b6850 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6850 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6850 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6850 bytes 29210e91
+ 008b6850 bytes 29e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-330743253c0a1f6886a7b5b89725ee44"></a>

### [`008b6908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6908.md) → [`008b6908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6908.md) FUN_008b6908

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
      "definition_site": "008b692c",
      "incomplete_value": false,
      "site": "008b692c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b692c",
      "incomplete_value": false,
      "site": "008b692c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "008b692c",
      "DATA",
      [
        "storage",
        "00c07408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b692c",
      "DATA",
      [
        "storage",
        "00c074b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6908.md#insn-008b6928)
- 新版 `008b6928`（命令位置の公開資料なし）

~~~diff
- 008b6928 ["COPY", "tmp:0:8", ["const:408:8"]]
- 008b6928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6928 ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 008b6928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6928 bytes 08211091
+ 008b6928 bytes 08e11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86883281ad3bdb2b775c6d136f708473"></a>

### [`008b693c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b693c.md) → [`008b693c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b693c.md) FUN_008b693c

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
      "definition_site": "008b6948",
      "incomplete_value": false,
      "site": "008b6948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6948",
      "incomplete_value": false,
      "site": "008b6948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "008b6948",
      "DATA",
      [
        "storage",
        "00c07408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6948",
      "DATA",
      [
        "storage",
        "00c074b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b693c.md#insn-008b6944)
- 新版 `008b6944`（命令位置の公開資料なし）

~~~diff
- 008b6944 ["COPY", "tmp:0:8", ["const:408:8"]]
- 008b6944 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6944 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6944 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b6944 ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 008b6944 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6944 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6944 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6944 bytes 29211091
+ 008b6944 bytes 29e11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c95ec8a703e87fed972995d3363fc83d"></a>

### [`008b69b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b69b8.md) → [`008b69b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b69b8.md) FUN_008b69b8

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
      "definition_site": "008b69dc",
      "incomplete_value": false,
      "site": "008b69dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b69dc",
      "incomplete_value": false,
      "site": "008b69dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "008b69dc",
      "DATA",
      [
        "storage",
        "00c07488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b69dc",
      "DATA",
      [
        "storage",
        "00c07538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b69d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b69b8.md#insn-008b69d8)
- 新版 `008b69d8`（命令位置の公開資料なし）

~~~diff
- 008b69d8 ["COPY", "tmp:0:8", ["const:488:8"]]
- 008b69d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b69d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b69d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b69d8 ["COPY", "tmp:0:8", ["const:538:8"]]
+ 008b69d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b69d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b69d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b69d8 bytes 08211291
+ 008b69d8 bytes 08e11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-363d8cb5218c63c4ccd0370c00080915"></a>

### [`008b69ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b69ec.md) → [`008b69ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b69ec.md) FUN_008b69ec

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
      "definition_site": "008b69f8",
      "incomplete_value": false,
      "site": "008b69f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b69f8",
      "incomplete_value": false,
      "site": "008b69f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "008b69f8",
      "DATA",
      [
        "storage",
        "00c07488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b69f8",
      "DATA",
      [
        "storage",
        "00c07538",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b69f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b69ec.md#insn-008b69f4)
- 新版 `008b69f4`（命令位置の公開資料なし）

~~~diff
- 008b69f4 ["COPY", "tmp:0:8", ["const:488:8"]]
- 008b69f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b69f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b69f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b69f4 ["COPY", "tmp:0:8", ["const:538:8"]]
+ 008b69f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b69f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b69f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b69f4 bytes 29211291
+ 008b69f4 bytes 29e11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5ae510db7e8b9b89096556696516ea4"></a>

### [`008b6a08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6a08.md) → [`008b6a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6a08.md) FUN_008b6a08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050ae28.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050ae28.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b6af0",
      "incomplete_value": true,
      "site": "008b6b08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8a3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6af0",
      "incomplete_value": true,
      "site": "008b6b08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:937:8"
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
      "definition_site": "008b6be0",
      "incomplete_value": false,
      "site": "008b6be0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6be0",
      "incomplete_value": false,
      "site": "008b6be0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b6af0",
      "READ",
      [
        "storage",
        "002a8937",
        null,
        "string"
      ]
    ],
    [
      "008b6be0",
      "DATA",
      [
        "storage",
        "00c074f8",
        null,
        "undefined *"
      ]
    ],
    [
      "008b6c2c",
      "READ",
      [
        "storage",
        "00c07518",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008b6af0",
      "READ",
      [
        "storage",
        "002a88a3",
        null,
        "string"
      ]
    ],
    [
      "008b6be0",
      "DATA",
      [
        "storage",
        "00c075a8",
        null,
        "undefined *"
      ]
    ],
    [
      "008b6c2c",
      "READ",
      [
        "storage",
        "00c075c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6a08.md#insn-008b6ae8) · [`008b6bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6a08.md#insn-008b6bd8)
- 新版 `008b6ae8`（命令位置の公開資料なし） · `008b6bd8`（命令位置の公開資料なし）

~~~diff
- 008b6ae8 ["COPY", "tmp:0:8", ["const:937:8"]]
- 008b6ae8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6ae8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6ae8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b6ae8 ["COPY", "tmp:0:8", ["const:8a3:8"]]
+ 008b6ae8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6ae8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6ae8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6ae8 bytes 29dd2491
+ 008b6ae8 bytes 298d2291
- 008b6bd8 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 008b6bd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6bd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6bd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6bd8 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 008b6bd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6bd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6bd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6bd8 bytes 08e11391
+ 008b6bd8 bytes 08a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24fc60011c1eb22e7223b752ee69a023"></a>

### [`008b6e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6e8c.md) → [`008b6e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6e8c.md) FUN_008b6e8c

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
      "definition_site": "008b6eb0",
      "incomplete_value": false,
      "site": "008b6eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6eb0",
      "incomplete_value": false,
      "site": "008b6eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
      "008b6eb0",
      "DATA",
      [
        "storage",
        "00c074f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6eb0",
      "DATA",
      [
        "storage",
        "00c075a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6eac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6e8c.md#insn-008b6eac)
- 新版 `008b6eac`（命令位置の公開資料なし）

~~~diff
- 008b6eac ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 008b6eac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6eac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6eac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6eac ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 008b6eac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6eac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6eac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6eac bytes 08e11391
+ 008b6eac bytes 08a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d0c45a79ff9600d0f80132dcd7d54a2"></a>

### [`008b6ec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6ec0.md) → [`008b6ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6ec0.md) FUN_008b6ec0

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
      "definition_site": "008b6ecc",
      "incomplete_value": false,
      "site": "008b6ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6ecc",
      "incomplete_value": false,
      "site": "008b6ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
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
      "008b6ecc",
      "DATA",
      [
        "storage",
        "00c074f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6ecc",
      "DATA",
      [
        "storage",
        "00c075a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6ec0.md#insn-008b6ec8)
- 新版 `008b6ec8`（命令位置の公開資料なし）

~~~diff
- 008b6ec8 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 008b6ec8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6ec8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6ec8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b6ec8 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 008b6ec8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6ec8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6ec8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6ec8 bytes 29e11391
+ 008b6ec8 bytes 29a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86f324bca5e6cbf70da6bda1894150df"></a>

### [`008b6f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6f3c.md) → [`008b6f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6f3c.md) FUN_008b6f3c

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
      "definition_site": "008b6f60",
      "incomplete_value": false,
      "site": "008b6f60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6f60",
      "incomplete_value": false,
      "site": "008b6f60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:588:8"
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
      "008b6f60",
      "DATA",
      [
        "storage",
        "00c07588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6f60",
      "DATA",
      [
        "storage",
        "00c07638",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6f5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6f3c.md#insn-008b6f5c)
- 新版 `008b6f5c`（命令位置の公開資料なし）

~~~diff
- 008b6f5c ["COPY", "tmp:0:8", ["const:588:8"]]
- 008b6f5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6f5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6f5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6f5c ["COPY", "tmp:0:8", ["const:638:8"]]
+ 008b6f5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6f5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6f5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6f5c bytes 08211691
+ 008b6f5c bytes 08e11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bd818bbb32d12d9549e76a7ee1861e3"></a>

### [`008b6f70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6f70.md) → [`008b6f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6f70.md) FUN_008b6f70

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
      "definition_site": "008b6f7c",
      "incomplete_value": false,
      "site": "008b6f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6f7c",
      "incomplete_value": false,
      "site": "008b6f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:588:8"
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
      "008b6f7c",
      "DATA",
      [
        "storage",
        "00c07588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6f7c",
      "DATA",
      [
        "storage",
        "00c07638",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6f70.md#insn-008b6f78)
- 新版 `008b6f78`（命令位置の公開資料なし）

~~~diff
- 008b6f78 ["COPY", "tmp:0:8", ["const:588:8"]]
- 008b6f78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6f78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6f78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b6f78 ["COPY", "tmp:0:8", ["const:638:8"]]
+ 008b6f78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6f78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6f78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6f78 bytes 29211691
+ 008b6f78 bytes 29e11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61b458eac9f95940afa760203f04d22a"></a>

### [`008b6f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6f8c.md) → [`008b6f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6f8c.md) FUN_008b6f8c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00444988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.85% / 新版 93.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008b6fc4",
      "incomplete_value": true,
      "site": "008b6fc4",
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
      "definition_site": "008b6fc4",
      "incomplete_value": true,
      "site": "008b6fc4",
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
      "definition_site": "008b6fcc",
      "incomplete_value": false,
      "site": "008b6fe0",
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
      "definition_site": "008b6fcc",
      "incomplete_value": false,
      "site": "008b6fe0",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008b6fd4",
      "incomplete_value": false,
      "site": "008b6fe0",
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
      "definition_site": "008b6fd4",
      "incomplete_value": false,
      "site": "008b6fe0",
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
      "008b6fc0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008b6fcc",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b6fd4",
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
      "008b6fc0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008b6fcc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b6fd4",
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

- 旧版 [`008b6fc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6f8c.md#insn-008b6fc0) · [`008b6fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6f8c.md#insn-008b6fcc) · [`008b6fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008b6/008b6f8c.md#insn-008b6fd4)
- 新版 `008b6fc0`（命令位置の公開資料なし） · `008b6fcc`（命令位置の公開資料なし） · `008b6fd4`（命令位置の公開資料なし）

~~~diff
- 008b6fc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008b6fc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008b6fc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008b6fc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008b6fc0 bytes 08dd44f9
+ 008b6fc0 bytes 083d45f9
- 008b6fcc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008b6fcc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008b6fcc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008b6fcc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008b6fcc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008b6fcc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008b6fcc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008b6fcc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008b6fcc bytes 21603691
+ 008b6fcc bytes 21203991
- 008b6fd4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 008b6fd4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008b6fd4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008b6fd4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008b6fd4 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 008b6fd4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008b6fd4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008b6fd4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008b6fd4 bytes 42a00791
+ 008b6fd4 bytes 42600a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

