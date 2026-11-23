# v15.7.2 → v15.7.3 · 最優先の変更候補 (36)

[一覧の目次](README.md)

<a id="compare-acbd8f57823a81af79d5d77706eb6507"></a>

### [`007c3480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3480.md) → [`007c3480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3480.md) FUN_007c3480

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
      "definition_site": "007c3494",
      "incomplete_value": false,
      "site": "007c3498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3494",
      "incomplete_value": false,
      "site": "007c3498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "007c3498",
      "DATA",
      [
        "storage",
        "00bfd8f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3498",
      "DATA",
      [
        "storage",
        "00bfd9a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3480.md#insn-007c3494)
- 新版 [`007c3494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3480.md#insn-007c3494)

~~~diff
- 007c3494 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 007c3494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3494 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 007c3494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3494 bytes 08e12391
+ 007c3494 bytes 08a12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65b7e7f7114db148cff56e808769e4b5"></a>

### [`007c34bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c34bc.md) → [`007c34bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c34bc.md) FUN_007c34bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448034.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`006f1e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006f1/006f1e2c.md) [`0088600c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`006f1e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1e2c.md) [`0088600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c350c",
      "incomplete_value": false,
      "site": "007c351c",
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
      "definition_site": "007c350c",
      "incomplete_value": false,
      "site": "007c351c",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c3514",
      "incomplete_value": false,
      "site": "007c351c",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3514",
      "incomplete_value": false,
      "site": "007c351c",
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
            "const:468:8"
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
      "007c3500",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c350c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c3514",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c3500",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c350c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c3514",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c34bc.md#insn-007c3500) · [`007c350c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c34bc.md#insn-007c350c) · [`007c3514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c34bc.md#insn-007c3514)
- 新版 [`007c3500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c34bc.md#insn-007c3500) · [`007c350c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c34bc.md#insn-007c350c) · [`007c3514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c34bc.md#insn-007c3514)

~~~diff
- 007c3500 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007c3500 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c3500 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007c3500 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c3500 bytes 00dd44f9
+ 007c3500 bytes 003d45f9
- 007c350c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007c350c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c350c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c350c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c350c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007c350c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c350c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c350c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c350c bytes 21603691
+ 007c350c bytes 21203991
- 007c3514 ["COPY", "tmp:0:8", ["const:468:8"]]
- 007c3514 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c3514 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c3514 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c3514 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007c3514 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c3514 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c3514 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c3514 bytes 42a01191
+ 007c3514 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f21d7736a45c9862580789758f96e155"></a>

### [`007c36c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c36c0.md) → [`007c36c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c36c0.md) FUN_007c36c0

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
      "definition_site": "007c36e4",
      "incomplete_value": false,
      "site": "007c36e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c36e4",
      "incomplete_value": false,
      "site": "007c36e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      "007c36e4",
      "DATA",
      [
        "storage",
        "00bfd978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c36e4",
      "DATA",
      [
        "storage",
        "00bfda28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c36e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c36c0.md#insn-007c36e0)
- 新版 [`007c36e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c36c0.md#insn-007c36e0)

~~~diff
- 007c36e0 ["COPY", "tmp:0:8", ["const:978:8"]]
- 007c36e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c36e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c36e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c36e0 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 007c36e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c36e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c36e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c36e0 bytes 08e12591
+ 007c36e0 bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08ecf7dab6d3d39c90ed757540637dcc"></a>

### [`007c37c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c37c4.md) → [`007c37c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c37c4.md) FUN_007c37c4

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
      "definition_site": "007c37d8",
      "incomplete_value": false,
      "site": "007c37dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c37d8",
      "incomplete_value": false,
      "site": "007c37dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "007c37dc",
      "DATA",
      [
        "storage",
        "00bfd9f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c37dc",
      "DATA",
      [
        "storage",
        "00bfdaa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c37d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c37c4.md#insn-007c37d8)
- 新版 [`007c37d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c37c4.md#insn-007c37d8)

~~~diff
- 007c37d8 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 007c37d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c37d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c37d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c37d8 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 007c37d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c37d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c37d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c37d8 bytes 08e12791
+ 007c37d8 bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78e64f1f9190c755d8d0bb276897b899"></a>

### [`007c3874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3874.md) → [`007c3874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3874.md) FUN_007c3874

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
      "definition_site": "007c3898",
      "incomplete_value": false,
      "site": "007c3898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3898",
      "incomplete_value": false,
      "site": "007c3898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:a78:8"
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
      "007c3898",
      "DATA",
      [
        "storage",
        "00bfda78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3898",
      "DATA",
      [
        "storage",
        "00bfdb28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3874.md#insn-007c3894)
- 新版 [`007c3894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3874.md#insn-007c3894)

~~~diff
- 007c3894 ["COPY", "tmp:0:8", ["const:a78:8"]]
- 007c3894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3894 ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 007c3894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3894 bytes 08e12991
+ 007c3894 bytes 08a12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51012466435db2d361be1cc6a6e38455"></a>

### [`007c38c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c38c4.md) → [`007c38c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c38c4.md) FUN_007c38c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00445d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445d04.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00448034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448034.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007c3908",
      "incomplete_value": true,
      "site": "007c3908",
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
      "definition_site": "007c3908",
      "incomplete_value": true,
      "site": "007c3908",
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
      "definition_site": "007c3918",
      "incomplete_value": false,
      "site": "007c3920",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3918",
      "incomplete_value": false,
      "site": "007c3920",
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
            "const:468:8"
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
      "007c38fc",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c3910",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c3918",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c38fc",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c3910",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c3918",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c38fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c38c4.md#insn-007c38fc) · [`007c3910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c38c4.md#insn-007c3910) · [`007c3918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c38c4.md#insn-007c3918)
- 新版 [`007c38fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c38c4.md#insn-007c38fc) · [`007c3910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c38c4.md#insn-007c3910) · [`007c3918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c38c4.md#insn-007c3918)

~~~diff
- 007c38fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
- 007c38fc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c38fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 007c38fc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c38fc bytes 20dd44f9
+ 007c38fc bytes 203d45f9
- 007c3910 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007c3910 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c3910 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c3910 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c3910 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007c3910 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c3910 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c3910 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c3910 bytes 21603691
+ 007c3910 bytes 21203991
- 007c3918 ["COPY", "tmp:0:8", ["const:468:8"]]
- 007c3918 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c3918 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c3918 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c3918 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007c3918 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c3918 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c3918 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c3918 bytes 42a01191
+ 007c3918 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38b854daaf7ac48ba0d4814f145af07a"></a>

### [`007c3c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3c48.md) → [`007c3c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3c48.md) FUN_007c3c48

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
      "definition_site": "007c3c6c",
      "incomplete_value": false,
      "site": "007c3c6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3c6c",
      "incomplete_value": false,
      "site": "007c3c6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "007c3c6c",
      "DATA",
      [
        "storage",
        "00bfdaf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3c6c",
      "DATA",
      [
        "storage",
        "00bfdba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3c48.md#insn-007c3c68)
- 新版 [`007c3c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3c48.md#insn-007c3c68)

~~~diff
- 007c3c68 ["COPY", "tmp:0:8", ["const:af8:8"]]
- 007c3c68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3c68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3c68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3c68 ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 007c3c68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3c68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3c68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3c68 bytes 08e12b91
+ 007c3c68 bytes 08a12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8badeddbd3cafd9b688e8fa25bea2967"></a>

### [`007c3d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3d2c.md) → [`007c3d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d2c.md) FUN_007c3d2c

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
      "definition_site": "007c3d50",
      "incomplete_value": false,
      "site": "007c3d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3d50",
      "incomplete_value": false,
      "site": "007c3d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "007c3d50",
      "DATA",
      [
        "storage",
        "00bfdb78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3d50",
      "DATA",
      [
        "storage",
        "00bfdc28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3d2c.md#insn-007c3d4c)
- 新版 [`007c3d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d2c.md#insn-007c3d4c)

~~~diff
- 007c3d4c ["COPY", "tmp:0:8", ["const:b78:8"]]
- 007c3d4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3d4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3d4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3d4c ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 007c3d4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3d4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3d4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3d4c bytes 08e12d91
+ 007c3d4c bytes 08a13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afb62855c7dbee774cab59eb73897fd1"></a>

### [`007c3d7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3d7c.md) → [`007c3d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d7c.md) FUN_007c3d7c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00445d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445d04.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 93.15% / 新版 93.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007c3da0",
      "incomplete_value": true,
      "site": "007c3da0",
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
      "definition_site": "007c3da0",
      "incomplete_value": true,
      "site": "007c3da0",
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
      "007c3d98",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c3da8",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c3db0",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c3d98",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c3da8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c3db0",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3d98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3d7c.md#insn-007c3d98) · [`007c3da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3d7c.md#insn-007c3da8) · [`007c3db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3d7c.md#insn-007c3db0)
- 新版 [`007c3d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d7c.md#insn-007c3d98) · [`007c3da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d7c.md#insn-007c3da8) · [`007c3db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3d7c.md#insn-007c3db0)

~~~diff
- 007c3d98 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
- 007c3d98 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c3d98 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 007c3d98 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c3d98 bytes 20dd44f9
+ 007c3d98 bytes 203d45f9
- 007c3da8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007c3da8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c3da8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c3da8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c3da8 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007c3da8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c3da8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c3da8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c3da8 bytes 21603691
+ 007c3da8 bytes 21203991
- 007c3db0 ["COPY", "tmp:0:8", ["const:468:8"]]
- 007c3db0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c3db0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c3db0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c3db0 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007c3db0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c3db0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c3db0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c3db0 bytes 42a01191
+ 007c3db0 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f737734485f6e882a6d6c48077b1bcfe"></a>

### [`007c3ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3ecc.md) → [`007c3ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3ecc.md) FUN_007c3ecc

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
      "definition_site": "007c3ee0",
      "incomplete_value": false,
      "site": "007c3ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3ee0",
      "incomplete_value": false,
      "site": "007c3ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "007c3ee4",
      "DATA",
      [
        "storage",
        "00bfdbf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3ee4",
      "DATA",
      [
        "storage",
        "00bfdca8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3ecc.md#insn-007c3ee0)
- 新版 [`007c3ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3ecc.md#insn-007c3ee0)

~~~diff
- 007c3ee0 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 007c3ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3ee0 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 007c3ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3ee0 bytes 08e12f91
+ 007c3ee0 bytes 08a13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83214613b416a6a378403f3f5dbfcb96"></a>

### [`007c3f74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3f74.md) → [`007c3f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3f74.md) FUN_007c3f74

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
      "definition_site": "007c3f98",
      "incomplete_value": false,
      "site": "007c3f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c3f98",
      "incomplete_value": false,
      "site": "007c3f98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "007c3f98",
      "DATA",
      [
        "storage",
        "00bfdc78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c3f98",
      "DATA",
      [
        "storage",
        "00bfdd28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c3f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3f74.md#insn-007c3f94)
- 新版 [`007c3f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3f74.md#insn-007c3f94)

~~~diff
- 007c3f94 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 007c3f94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c3f94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c3f94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c3f94 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 007c3f94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3f94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c3f94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c3f94 bytes 08e13191
+ 007c3f94 bytes 08a13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49fd9345b79c45b90cdfae7cd85fa2ea"></a>

### [`007c3fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3fc4.md) → [`007c3fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3fc4.md) FUN_007c3fc4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0044ac1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007c42e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c42e0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c42e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c42e0.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c40d8",
      "incomplete_value": true,
      "site": "007c40ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9fd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c40d8",
      "incomplete_value": true,
      "site": "007c40ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a04:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c410c",
      "incomplete_value": false,
      "site": "007c410c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c410c",
      "incomplete_value": false,
      "site": "007c410c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "007c4020",
      "READ",
      [
        "storage",
        "00c1b5d8",
        null,
        "pointer"
      ]
    ],
    [
      "007c4038",
      "READ",
      [
        "storage",
        "00c241a4",
        null,
        "undefined4"
      ]
    ],
    [
      "007c4038",
      "READ",
      [
        "storage",
        "00c241a8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "007c4020",
      "READ",
      [
        "storage",
        "00c1b688",
        null,
        "pointer"
      ]
    ],
    [
      "007c4038",
      "READ",
      [
        "storage",
        "00c24254",
        null,
        "undefined4"
      ]
    ],
    [
      "007c4038",
      "READ",
      [
        "storage",
        "00c24258",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3fc4.md#insn-007c4020) · [`007c40d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3fc4.md#insn-007c40d0) · [`007c40d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c3/007c3fc4.md#insn-007c40d4)
- 新版 [`007c4020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3fc4.md#insn-007c4020) · [`007c40d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c3/007c3fc4.md#insn-007c40d0)

~~~diff
- 007c4020 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5d8:8"]]
- 007c4020 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c4020 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:688:8"]]
+ 007c4020 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 007c4020 bytes 29ed42f9
+ 007c4020 bytes 294543f9
- 007c40d0 ["COPY", "tmp:0:8", ["const:a04:8"]]
- 007c40d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c40d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c40d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c40d0 ["COPY", "tmp:0:8", ["const:9fd:8"]]
+ 007c40d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c40d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c40d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c40d0 bytes 29112891
+ 007c40d0 bytes 29f52791
- 007c40d4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 007c40d4 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1862d75ec661ff170f9d32f5105fb6c"></a>

### [`007c4298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4298.md) → [`007c4298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4298.md) FUN_007c4298

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
      "definition_site": "007c42bc",
      "incomplete_value": false,
      "site": "007c42bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c42bc",
      "incomplete_value": false,
      "site": "007c42bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "007c42bc",
      "DATA",
      [
        "storage",
        "00bfdce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c42bc",
      "DATA",
      [
        "storage",
        "00bfdd98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c42b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4298.md#insn-007c42b8)
- 新版 [`007c42b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4298.md#insn-007c42b8)

~~~diff
- 007c42b8 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 007c42b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c42b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c42b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c42b8 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 007c42b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c42b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c42b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c42b8 bytes 08a13391
+ 007c42b8 bytes 08613691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9118dde54ecab4ce45940038f651706"></a>

### [`007c42cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c42cc.md) → [`007c42cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c42cc.md) FUN_007c42cc

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
      "definition_site": "007c42d8",
      "incomplete_value": false,
      "site": "007c42d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c42d8",
      "incomplete_value": false,
      "site": "007c42d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "007c42d8",
      "DATA",
      [
        "storage",
        "00bfdce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c42d8",
      "DATA",
      [
        "storage",
        "00bfdd98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c42d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c42cc.md#insn-007c42d4)
- 新版 [`007c42d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c42cc.md#insn-007c42d4)

~~~diff
- 007c42d4 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 007c42d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c42d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c42d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c42d4 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 007c42d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c42d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c42d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c42d4 bytes 29a13391
+ 007c42d4 bytes 29613691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23a9b5b4826dd98a0086322fd696c8dd"></a>

### [`007c42e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c42e8.md) → [`007c42e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c42e8.md) FUN_007c42e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0044ac1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007c457c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c457c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c457c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c457c.md)

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
      "definition_site": "007c4374",
      "incomplete_value": true,
      "site": "007c4388",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a59:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4374",
      "incomplete_value": true,
      "site": "007c4388",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a62:8"
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
      "definition_site": "007c43a4",
      "incomplete_value": false,
      "site": "007c43a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c43a4",
      "incomplete_value": false,
      "site": "007c43a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:d58:8"
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
      "007c4374",
      "READ",
      [
        "storage",
        "002a9a62",
        null,
        "string"
      ]
    ],
    [
      "007c43a4",
      "DATA",
      [
        "storage",
        "00bfdd58",
        null,
        "undefined *"
      ]
    ],
    [
      "007c4428",
      "READ",
      [
        "storage",
        "00bfdd78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c4374",
      "READ",
      [
        "storage",
        "002a9a59",
        null,
        "string"
      ]
    ],
    [
      "007c43a4",
      "DATA",
      [
        "storage",
        "00bfde08",
        null,
        "undefined *"
      ]
    ],
    [
      "007c4428",
      "READ",
      [
        "storage",
        "00bfde28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c436c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c42e8.md#insn-007c436c) · [`007c4370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c42e8.md#insn-007c4370)
- 新版 [`007c436c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c42e8.md#insn-007c436c) · [`007c4370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c42e8.md#insn-007c4370)

~~~diff
- 007c436c ["COPY", "tmp:0:8", ["const:a62:8"]]
- 007c436c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c436c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c436c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c436c ["COPY", "tmp:0:8", ["const:a59:8"]]
+ 007c436c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c436c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c436c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c436c bytes 29892991
+ 007c436c bytes 29652991
- 007c4370 ["COPY", "register:4098:8", ["register:4000:8"]]
- 007c4370 bytes f30300aa
+ 007c4370 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 007c4370 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fa20779c5007edf9dc7b616e068d741"></a>

### [`007c4534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4534.md) → [`007c4534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4534.md) FUN_007c4534

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
      "definition_site": "007c4558",
      "incomplete_value": false,
      "site": "007c4558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4558",
      "incomplete_value": false,
      "site": "007c4558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:d58:8"
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
      "007c4558",
      "DATA",
      [
        "storage",
        "00bfdd58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4558",
      "DATA",
      [
        "storage",
        "00bfde08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4534.md#insn-007c4554)
- 新版 [`007c4554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4534.md#insn-007c4554)

~~~diff
- 007c4554 ["COPY", "tmp:0:8", ["const:d58:8"]]
- 007c4554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c4554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c4554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c4554 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 007c4554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c4554 bytes 08613591
+ 007c4554 bytes 08213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b05340ba4a7b313c81b8b6d9efd04605"></a>

### [`007c4568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4568.md) → [`007c4568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4568.md) FUN_007c4568

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
      "definition_site": "007c4574",
      "incomplete_value": false,
      "site": "007c4574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4574",
      "incomplete_value": false,
      "site": "007c4574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:d58:8"
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
      "007c4574",
      "DATA",
      [
        "storage",
        "00bfdd58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4574",
      "DATA",
      [
        "storage",
        "00bfde08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4568.md#insn-007c4570)
- 新版 [`007c4570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4568.md#insn-007c4570)

~~~diff
- 007c4570 ["COPY", "tmp:0:8", ["const:d58:8"]]
- 007c4570 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c4570 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c4570 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c4570 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 007c4570 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4570 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4570 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c4570 bytes 29613591
+ 007c4570 bytes 29213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-434303a3ea1ed53c3f4decf2683e390c"></a>

### [`007c4614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4614.md) → [`007c4614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4614.md) FUN_007c4614

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
      "definition_site": "007c4638",
      "incomplete_value": false,
      "site": "007c4638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4638",
      "incomplete_value": false,
      "site": "007c4638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "007c4638",
      "DATA",
      [
        "storage",
        "00bfddf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4638",
      "DATA",
      [
        "storage",
        "00bfdea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4614.md#insn-007c4634)
- 新版 [`007c4634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4614.md#insn-007c4634)

~~~diff
- 007c4634 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 007c4634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c4634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c4634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c4634 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 007c4634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c4634 bytes 08e13791
+ 007c4634 bytes 08a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f045fffd78b335be8b63a0e3e32a145"></a>

### [`007c4664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4664.md) → [`007c4664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4664.md) FUN_007c4664

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0044ac1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007c48f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c48f8.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c48f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c48f8.md)

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
      "definition_site": "007c46f0",
      "incomplete_value": true,
      "site": "007c4704",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a59:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c46f0",
      "incomplete_value": true,
      "site": "007c4704",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a62:8"
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
      "definition_site": "007c4720",
      "incomplete_value": false,
      "site": "007c4720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4720",
      "incomplete_value": false,
      "site": "007c4720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "007c46f0",
      "READ",
      [
        "storage",
        "002a9a62",
        null,
        "string"
      ]
    ],
    [
      "007c4720",
      "DATA",
      [
        "storage",
        "00bfde68",
        null,
        "undefined *"
      ]
    ],
    [
      "007c47a4",
      "READ",
      [
        "storage",
        "00bfde88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c46f0",
      "READ",
      [
        "storage",
        "002a9a59",
        null,
        "string"
      ]
    ],
    [
      "007c4720",
      "DATA",
      [
        "storage",
        "00bfdf18",
        null,
        "undefined *"
      ]
    ],
    [
      "007c47a4",
      "READ",
      [
        "storage",
        "00bfdf38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c46e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4664.md#insn-007c46e8) · [`007c46ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4664.md#insn-007c46ec)
- 新版 [`007c46e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4664.md#insn-007c46e8) · [`007c46ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4664.md#insn-007c46ec)

~~~diff
- 007c46e8 ["COPY", "tmp:0:8", ["const:a62:8"]]
- 007c46e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c46e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c46e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c46e8 ["COPY", "tmp:0:8", ["const:a59:8"]]
+ 007c46e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c46e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c46e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c46e8 bytes 29892991
+ 007c46e8 bytes 29652991
- 007c46ec ["COPY", "register:4098:8", ["register:4000:8"]]
- 007c46ec bytes f30300aa
+ 007c46ec ["COPY", "register:4098:8", ["register:4000:8"]]
+ 007c46ec bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cfaee9b2ef266a494cc1adb6c7cb985"></a>

### [`007c48b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c48b0.md) → [`007c48b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c48b0.md) FUN_007c48b0

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
      "definition_site": "007c48d4",
      "incomplete_value": false,
      "site": "007c48d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c48d4",
      "incomplete_value": false,
      "site": "007c48d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "007c48d4",
      "DATA",
      [
        "storage",
        "00bfde68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c48d4",
      "DATA",
      [
        "storage",
        "00bfdf18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c48d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c48b0.md#insn-007c48d0)
- 新版 [`007c48d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c48b0.md#insn-007c48d0)

~~~diff
- 007c48d0 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 007c48d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c48d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c48d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c48d0 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 007c48d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c48d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c48d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c48d0 bytes 08a13991
+ 007c48d0 bytes 08613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc8b621f984fcd41acc870cbebc42195"></a>

### [`007c48e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c48e4.md) → [`007c48e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c48e4.md) FUN_007c48e4

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
      "definition_site": "007c48f0",
      "incomplete_value": false,
      "site": "007c48f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c48f0",
      "incomplete_value": false,
      "site": "007c48f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "007c48f0",
      "DATA",
      [
        "storage",
        "00bfde68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c48f0",
      "DATA",
      [
        "storage",
        "00bfdf18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c48ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c48e4.md#insn-007c48ec)
- 新版 [`007c48ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c48e4.md#insn-007c48ec)

~~~diff
- 007c48ec ["COPY", "tmp:0:8", ["const:e68:8"]]
- 007c48ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c48ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c48ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c48ec ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 007c48ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c48ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c48ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c48ec bytes 29a13991
+ 007c48ec bytes 29613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4002bf76375a2465ccb10fea3839d1c4"></a>

### [`007c4990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4990.md) → [`007c4990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4990.md) FUN_007c4990

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
      "definition_site": "007c49b4",
      "incomplete_value": false,
      "site": "007c49b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c49b4",
      "incomplete_value": false,
      "site": "007c49b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "007c49b4",
      "DATA",
      [
        "storage",
        "00bfdef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c49b4",
      "DATA",
      [
        "storage",
        "00bfdfa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c49b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4990.md#insn-007c49b0)
- 新版 [`007c49b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4990.md#insn-007c49b0)

~~~diff
- 007c49b0 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 007c49b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c49b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c49b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c49b0 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 007c49b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c49b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c49b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c49b0 bytes 08e13b91
+ 007c49b0 bytes 08a13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcde07a839dd5b7f4c8978e2e83fdf83"></a>

### [`007c49e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c49e0.md) → [`007c49e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c49e0.md) FUN_007c49e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 17件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007c4d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4d50.md) [`007c4d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4d54.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c4d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d50.md) [`007c4d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d54.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.55% / 新版 90.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c4a70",
      "incomplete_value": true,
      "site": "007c4a80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4a70",
      "incomplete_value": true,
      "site": "007c4a80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d18:8"
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
      "definition_site": "007c4a74",
      "incomplete_value": true,
      "site": "007c4a84",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007c4a74",
      "incomplete_value": true,
      "site": "007c4a84",
      "value": [
        "LOAD",
        "8",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c4aa8",
      "incomplete_value": false,
      "site": "007c4aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4aa8",
      "incomplete_value": false,
      "site": "007c4aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "007c4a70",
      "READ",
      [
        "storage",
        "00294d18",
        null,
        "string"
      ]
    ],
    [
      "007c4a74",
      "READ",
      [
        "storage",
        "00294d28",
        null,
        "string"
      ]
    ],
    [
      "007c4aa8",
      "DATA",
      [
        "storage",
        "00bfdf68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4a70",
      "READ",
      [
        "storage",
        "00294da5",
        null,
        "string"
      ]
    ],
    [
      "007c4a74",
      "READ",
      [
        "storage",
        "00294db5",
        null,
        "string"
      ]
    ],
    [
      "007c4aa8",
      "DATA",
      [
        "storage",
        "00bfe018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c49e0.md#insn-007c4a68) · [`007c4a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c49e0.md#insn-007c4a6c)
- 新版 [`007c4a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c49e0.md#insn-007c4a68) · [`007c4a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c49e0.md#insn-007c4a6c)

~~~diff
- 007c4a68 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 007c4a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c4a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c4a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c4a68 ["COPY", "tmp:0:8", ["const:da5:8"]]
+ 007c4a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c4a68 bytes 08613491
+ 007c4a68 bytes 08953691
- 007c4a6c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 007c4a6c bytes 69d7ff90
+ 007c4a6c ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 007c4a6c bytes 69d7ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c02cb0b6e6cf84f529d284995ca0e70b"></a>

### [`007c4d08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4d08.md) → [`007c4d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d08.md) FUN_007c4d08

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
      "definition_site": "007c4d2c",
      "incomplete_value": false,
      "site": "007c4d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4d2c",
      "incomplete_value": false,
      "site": "007c4d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "007c4d2c",
      "DATA",
      [
        "storage",
        "00bfdf68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4d2c",
      "DATA",
      [
        "storage",
        "00bfe018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4d08.md#insn-007c4d24) · [`007c4d28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4d08.md#insn-007c4d28)
- 新版 [`007c4d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d08.md#insn-007c4d24) · [`007c4d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d08.md#insn-007c4d28)

~~~diff
- 007c4d24 ["COPY", "register:4040:8", ["const:bfd000:8"]]
+ 007c4d24 ["COPY", "register:4040:8", ["const:bfe000:8"]]
- 007c4d24 bytes c82100b0
+ 007c4d24 bytes c82100d0
- 007c4d28 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 007c4d28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c4d28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c4d28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c4d28 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 007c4d28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4d28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4d28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c4d28 bytes 08a13d91
+ 007c4d28 bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0de3a47137054d8292de19c5366b12e"></a>

### [`007c4d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4d3c.md) → [`007c4d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d3c.md) FUN_007c4d3c

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
      "definition_site": "007c4d48",
      "incomplete_value": false,
      "site": "007c4d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4d48",
      "incomplete_value": false,
      "site": "007c4d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "007c4d48",
      "DATA",
      [
        "storage",
        "00bfdf68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4d48",
      "DATA",
      [
        "storage",
        "00bfe018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4d3c.md#insn-007c4d40) · [`007c4d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4d3c.md#insn-007c4d44)
- 新版 [`007c4d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d3c.md#insn-007c4d40) · [`007c4d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d3c.md#insn-007c4d44)

~~~diff
- 007c4d40 ["COPY", "register:4048:8", ["const:bfd000:8"]]
+ 007c4d40 ["COPY", "register:4048:8", ["const:bfe000:8"]]
- 007c4d40 bytes c92100b0
+ 007c4d40 bytes c92100d0
- 007c4d44 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 007c4d44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c4d44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c4d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c4d44 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 007c4d44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4d44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c4d44 bytes 29a13d91
+ 007c4d44 bytes 29610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-667422c1995574cc41743c9eb93827fa"></a>

### [`007c4d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4d88.md) → [`007c4d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d88.md) FUN_007c4d88

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
      "definition_site": "007c4dac",
      "incomplete_value": false,
      "site": "007c4dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4dac",
      "incomplete_value": false,
      "site": "007c4dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "007c4dac",
      "DATA",
      [
        "storage",
        "00bfdfe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4dac",
      "DATA",
      [
        "storage",
        "00bfe098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4d88.md#insn-007c4da4) · [`007c4da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4d88.md#insn-007c4da8)
- 新版 [`007c4da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d88.md#insn-007c4da4) · [`007c4da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4d88.md#insn-007c4da8)

~~~diff
- 007c4da4 ["COPY", "register:4040:8", ["const:bfd000:8"]]
+ 007c4da4 ["COPY", "register:4040:8", ["const:bfe000:8"]]
- 007c4da4 bytes c82100b0
+ 007c4da4 bytes c82100d0
- 007c4da8 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 007c4da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c4da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c4da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c4da8 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 007c4da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c4da8 bytes 08a13f91
+ 007c4da8 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a8a5b4f52a4c5da56a1ddd01a7b2c2e"></a>

### [`007c4dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4dbc.md) → [`007c4dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4dbc.md) FUN_007c4dbc

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
      "definition_site": "007c4dc8",
      "incomplete_value": false,
      "site": "007c4dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4dc8",
      "incomplete_value": false,
      "site": "007c4dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfd000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "007c4dc8",
      "DATA",
      [
        "storage",
        "00bfdfe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4dc8",
      "DATA",
      [
        "storage",
        "00bfe098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4dbc.md#insn-007c4dc0) · [`007c4dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4dbc.md#insn-007c4dc4)
- 新版 [`007c4dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4dbc.md#insn-007c4dc0) · [`007c4dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4dbc.md#insn-007c4dc4)

~~~diff
- 007c4dc0 ["COPY", "register:4048:8", ["const:bfd000:8"]]
+ 007c4dc0 ["COPY", "register:4048:8", ["const:bfe000:8"]]
- 007c4dc0 bytes c92100b0
+ 007c4dc0 bytes c92100d0
- 007c4dc4 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 007c4dc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c4dc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c4dc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c4dc4 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 007c4dc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4dc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4dc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c4dc4 bytes 29a13f91
+ 007c4dc4 bytes 29610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c483e828304ee7f13b030b1db5a559d3"></a>

### [`007c4f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4f38.md) → [`007c4f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f38.md) FUN_007c4f38

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
      "definition_site": "007c4f5c",
      "incomplete_value": false,
      "site": "007c4f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4f5c",
      "incomplete_value": false,
      "site": "007c4f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:68:8"
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
      "007c4f5c",
      "DATA",
      [
        "storage",
        "00bfe068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4f5c",
      "DATA",
      [
        "storage",
        "00bfe118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4f38.md#insn-007c4f58)
- 新版 [`007c4f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f38.md#insn-007c4f58)

~~~diff
- 007c4f58 ["COPY", "tmp:0:8", ["const:68:8"]]
- 007c4f58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c4f58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c4f58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c4f58 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 007c4f58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4f58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c4f58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c4f58 bytes 08a10191
+ 007c4f58 bytes 08610491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-414ab2052ed34c938ef3e4a1cd644850"></a>

### [`007c4f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4f6c.md) → [`007c4f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f6c.md) FUN_007c4f6c

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
      "definition_site": "007c4f78",
      "incomplete_value": false,
      "site": "007c4f78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4f78",
      "incomplete_value": false,
      "site": "007c4f78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:68:8"
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
      "007c4f78",
      "DATA",
      [
        "storage",
        "00bfe068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c4f78",
      "DATA",
      [
        "storage",
        "00bfe118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4f74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4f6c.md#insn-007c4f74)
- 新版 [`007c4f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f6c.md#insn-007c4f74)

~~~diff
- 007c4f74 ["COPY", "tmp:0:8", ["const:68:8"]]
- 007c4f74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c4f74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c4f74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c4f74 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 007c4f74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4f74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c4f74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c4f74 bytes 29a10191
+ 007c4f74 bytes 29610491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8bff894ab6bb4e085a19c910b69dc5c"></a>

### [`007c4f88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4f88.md) → [`007c4f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f88.md) FUN_007c4f88

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`004489a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/004489a8.md) [`0044aa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044aa9c.md) [`00883bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883bb8.md) [`00883c74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883c74.md) [`00883c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883c7c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004489a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/004489a8.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`00883bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883bb8.md) [`00883c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883c74.md) [`00883c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883c7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c4fd8",
      "incomplete_value": true,
      "site": "007c4fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "007c4fd8",
      "incomplete_value": true,
      "site": "007c4fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c4fd4",
      "incomplete_value": false,
      "site": "007c4fe8",
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
      "definition_site": "007c4fd4",
      "incomplete_value": false,
      "site": "007c4fe8",
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
      "definition_site": "007c4fe0",
      "incomplete_value": false,
      "site": "007c4fe8",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c4fe0",
      "incomplete_value": false,
      "site": "007c4fe8",
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
            "const:468:8"
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
      "007c4fd4",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c4fd8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c4fe0",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c4fd4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c4fd8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c4fe0",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c4fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4f88.md#insn-007c4fd4) · [`007c4fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4f88.md#insn-007c4fd8) · [`007c4fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c4/007c4f88.md#insn-007c4fe0)
- 新版 [`007c4fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f88.md#insn-007c4fd4) · [`007c4fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f88.md#insn-007c4fd8) · [`007c4fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c4/007c4f88.md#insn-007c4fe0)

~~~diff
- 007c4fd4 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007c4fd4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c4fd4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c4fd4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c4fd4 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007c4fd4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c4fd4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c4fd4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c4fd4 bytes 21603691
+ 007c4fd4 bytes 21203991
- 007c4fd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007c4fd8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c4fd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007c4fd8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c4fd8 bytes 00dd44f9
+ 007c4fd8 bytes 003d45f9
- 007c4fe0 ["COPY", "tmp:0:8", ["const:468:8"]]
- 007c4fe0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c4fe0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c4fe0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c4fe0 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007c4fe0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c4fe0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c4fe0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c4fe0 bytes 42a01191
+ 007c4fe0 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-224be77372148918f03f9ddb78514bbe"></a>

### [`007c50cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c50cc.md) → [`007c50cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c50cc.md) FUN_007c50cc

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
      "definition_site": "007c50f0",
      "incomplete_value": false,
      "site": "007c50f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c50f0",
      "incomplete_value": false,
      "site": "007c50f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "007c50f0",
      "DATA",
      [
        "storage",
        "00bfe0f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c50f0",
      "DATA",
      [
        "storage",
        "00bfe1a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c50ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c50cc.md#insn-007c50ec)
- 新版 [`007c50ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c50cc.md#insn-007c50ec)

~~~diff
- 007c50ec ["COPY", "tmp:0:8", ["const:f8:8"]]
- 007c50ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c50ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c50ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c50ec ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 007c50ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c50ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c50ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c50ec bytes 08e10391
+ 007c50ec bytes 08a10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aee08e1315892aba1cbbd593ac3f690"></a>

### [`007c5174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5174.md) → [`007c5174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5174.md) FUN_007c5174

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
      "definition_site": "007c5188",
      "incomplete_value": false,
      "site": "007c518c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5188",
      "incomplete_value": false,
      "site": "007c518c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "007c518c",
      "DATA",
      [
        "storage",
        "00bfe178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c518c",
      "DATA",
      [
        "storage",
        "00bfe228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5174.md#insn-007c5188)
- 新版 [`007c5188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5174.md#insn-007c5188)

~~~diff
- 007c5188 ["COPY", "tmp:0:8", ["const:178:8"]]
- 007c5188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5188 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 007c5188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5188 bytes 08e10591
+ 007c5188 bytes 08a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a11a554b409689430bdd5c22a9b8bfc"></a>

### [`007c5224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5224.md) → [`007c5224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5224.md) FUN_007c5224

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
      "definition_site": "007c5238",
      "incomplete_value": false,
      "site": "007c523c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5238",
      "incomplete_value": false,
      "site": "007c523c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
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
      "007c523c",
      "DATA",
      [
        "storage",
        "00bfe1f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c523c",
      "DATA",
      [
        "storage",
        "00bfe2a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5224.md#insn-007c5238)
- 新版 [`007c5238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5224.md#insn-007c5238)

~~~diff
- 007c5238 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 007c5238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5238 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 007c5238 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5238 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5238 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5238 bytes 08e10791
+ 007c5238 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb7b275b21b1b5cc185a88d875765ddc"></a>

### [`007c52d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c52d4.md) → [`007c52d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c52d4.md) FUN_007c52d4

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
      "definition_site": "007c52e8",
      "incomplete_value": false,
      "site": "007c52ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c52e8",
      "incomplete_value": false,
      "site": "007c52ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "007c52ec",
      "DATA",
      [
        "storage",
        "00bfe278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c52ec",
      "DATA",
      [
        "storage",
        "00bfe328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c52e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c52d4.md#insn-007c52e8)
- 新版 [`007c52e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c52d4.md#insn-007c52e8)

~~~diff
- 007c52e8 ["COPY", "tmp:0:8", ["const:278:8"]]
- 007c52e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c52e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c52e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c52e8 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 007c52e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c52e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c52e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c52e8 bytes 08e10991
+ 007c52e8 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37bc296b80e790e7fb77b0930685a08b"></a>

### [`007c5384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5384.md) → [`007c5384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5384.md) FUN_007c5384

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
      "definition_site": "007c5398",
      "incomplete_value": false,
      "site": "007c539c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5398",
      "incomplete_value": false,
      "site": "007c539c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c539c",
      "DATA",
      [
        "storage",
        "00bfe2f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c539c",
      "DATA",
      [
        "storage",
        "00bfe3a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5384.md#insn-007c5398)
- 新版 [`007c5398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5384.md#insn-007c5398)

~~~diff
- 007c5398 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 007c5398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5398 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 007c5398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5398 bytes 08e10b91
+ 007c5398 bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcb495c562551b28a116b2d6db894b8f"></a>

### [`007c5434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5434.md) → [`007c5434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5434.md) FUN_007c5434

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
      "definition_site": "007c5458",
      "incomplete_value": false,
      "site": "007c5458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5458",
      "incomplete_value": false,
      "site": "007c5458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c5458",
      "DATA",
      [
        "storage",
        "00bfe378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5458",
      "DATA",
      [
        "storage",
        "00bfe428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5434.md#insn-007c5454)
- 新版 [`007c5454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5434.md#insn-007c5454)

~~~diff
- 007c5454 ["COPY", "tmp:0:8", ["const:378:8"]]
- 007c5454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5454 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 007c5454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5454 bytes 08e10d91
+ 007c5454 bytes 08a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f7dbac24e3c79f74ff2286daa737907"></a>

### [`007c5484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5484.md) → [`007c5484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5484.md) FUN_007c5484

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007c5768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5768.md) [`007c576c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c576c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c5768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5768.md) [`007c576c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c576c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c5578",
      "incomplete_value": false,
      "site": "007c5578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5578",
      "incomplete_value": false,
      "site": "007c5578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "007c5508",
      "READ",
      [
        "storage",
        "0029c8bc",
        null,
        "string"
      ]
    ],
    [
      "007c5510",
      "READ",
      [
        "storage",
        "0029c8c2",
        null,
        "string"
      ]
    ],
    [
      "007c553c",
      "DATA",
      [
        "storage",
        "00bfe3e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5508",
      "READ",
      [
        "storage",
        "0029c949",
        null,
        "string"
      ]
    ],
    [
      "007c5510",
      "READ",
      [
        "storage",
        "0029c94f",
        null,
        "string"
      ]
    ],
    [
      "007c553c",
      "DATA",
      [
        "storage",
        "00bfe498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5484.md#insn-007c5504) · [`007c5534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5484.md#insn-007c5534) · [`007c5570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5484.md#insn-007c5570)
- 新版 [`007c5504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5484.md#insn-007c5504) · [`007c5534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5484.md#insn-007c5534) · [`007c5570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5484.md#insn-007c5570)

~~~diff
- 007c5504 ["COPY", "tmp:0:8", ["const:8bc:8"]]
- 007c5504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c5504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c5504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c5504 ["COPY", "tmp:0:8", ["const:949:8"]]
+ 007c5504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c5504 bytes 29f12291
+ 007c5504 bytes 29252591
- 007c5534 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 007c5534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5534 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 007c5534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5534 bytes 08a10f91
+ 007c5534 bytes 08611291
- 007c5570 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 007c5570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5570 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 007c5570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5570 bytes 08a11b91
+ 007c5570 bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3a8a959d12a1f2c9d50743588af3bba"></a>

### [`007c5720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5720.md) → [`007c5720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5720.md) FUN_007c5720

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
      "definition_site": "007c5744",
      "incomplete_value": false,
      "site": "007c5744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5744",
      "incomplete_value": false,
      "site": "007c5744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
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
      "007c5744",
      "DATA",
      [
        "storage",
        "00bfe3e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5744",
      "DATA",
      [
        "storage",
        "00bfe498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5720.md#insn-007c5740)
- 新版 [`007c5740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5720.md#insn-007c5740)

~~~diff
- 007c5740 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 007c5740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5740 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 007c5740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5740 bytes 08a10f91
+ 007c5740 bytes 08611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9344c165cd3dd2a6b747c536441bb177"></a>

### [`007c5754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5754.md) → [`007c5754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5754.md) FUN_007c5754

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
      "definition_site": "007c5760",
      "incomplete_value": false,
      "site": "007c5760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5760",
      "incomplete_value": false,
      "site": "007c5760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
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
      "007c5760",
      "DATA",
      [
        "storage",
        "00bfe3e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5760",
      "DATA",
      [
        "storage",
        "00bfe498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c575c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5754.md#insn-007c575c)
- 新版 [`007c575c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5754.md#insn-007c575c)

~~~diff
- 007c575c ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 007c575c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c575c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c575c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c575c ["COPY", "tmp:0:8", ["const:498:8"]]
+ 007c575c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c575c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c575c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c575c bytes 29a10f91
+ 007c575c bytes 29611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58b6807045fae831ef05e7f3252ac749"></a>

### [`007c5770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5770.md) → [`007c5770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5770.md) FUN_007c5770

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00449bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449bac.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007c5ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5ac8.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c5ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ac8.md)

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
      "definition_site": "007c5810",
      "incomplete_value": false,
      "site": "007c5810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5810",
      "incomplete_value": false,
      "site": "007c5810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "definition_site": "007c5840",
      "incomplete_value": false,
      "site": "007c5840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5840",
      "incomplete_value": false,
      "site": "007c5840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "definition_site": "007c5860",
      "incomplete_value": false,
      "site": "007c5860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5860",
      "incomplete_value": false,
      "site": "007c5860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "007c5810",
      "DATA",
      [
        "storage",
        "00bfe458",
        null,
        "undefined *"
      ]
    ],
    [
      "007c5840",
      "DATA",
      [
        "storage",
        "00bfe5d8",
        null,
        "undefined *"
      ]
    ],
    [
      "007c5860",
      "DATA",
      [
        "storage",
        "00bfe658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5810",
      "DATA",
      [
        "storage",
        "00bfe508",
        null,
        "undefined *"
      ]
    ],
    [
      "007c5840",
      "DATA",
      [
        "storage",
        "00bfe688",
        null,
        "undefined *"
      ]
    ],
    [
      "007c5860",
      "DATA",
      [
        "storage",
        "00bfe708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5770.md#insn-007c5808) · [`007c583c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5770.md#insn-007c583c) · [`007c5858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5770.md#insn-007c5858)
- 新版 [`007c5808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5770.md#insn-007c5808) · [`007c583c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5770.md#insn-007c583c) · [`007c5858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5770.md#insn-007c5858)

~~~diff
- 007c5808 ["COPY", "tmp:0:8", ["const:458:8"]]
- 007c5808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5808 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 007c5808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5808 bytes 08611191
+ 007c5808 bytes 08211491
- 007c583c ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 007c583c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c583c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c583c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c583c ["COPY", "tmp:0:8", ["const:688:8"]]
+ 007c583c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c583c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c583c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c583c bytes 08611791
+ 007c583c bytes 08211a91
- 007c5858 ["COPY", "tmp:0:8", ["const:658:8"]]
- 007c5858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5858 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 007c5858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5858 bytes 08611991
+ 007c5858 bytes 08211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5bb7c8f31d805661ccb562e9a7c719c"></a>

### [`007c5a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5a80.md) → [`007c5a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5a80.md) FUN_007c5a80

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
      "definition_site": "007c5aa4",
      "incomplete_value": false,
      "site": "007c5aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5aa4",
      "incomplete_value": false,
      "site": "007c5aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "007c5aa4",
      "DATA",
      [
        "storage",
        "00bfe458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5aa4",
      "DATA",
      [
        "storage",
        "00bfe508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5a80.md#insn-007c5aa0)
- 新版 [`007c5aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5a80.md#insn-007c5aa0)

~~~diff
- 007c5aa0 ["COPY", "tmp:0:8", ["const:458:8"]]
- 007c5aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5aa0 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 007c5aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5aa0 bytes 08611191
+ 007c5aa0 bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feadab3b8f9538269f5549fe2448da72"></a>

### [`007c5ab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5ab4.md) → [`007c5ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ab4.md) FUN_007c5ab4

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
      "definition_site": "007c5ac0",
      "incomplete_value": false,
      "site": "007c5ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5ac0",
      "incomplete_value": false,
      "site": "007c5ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "007c5ac0",
      "DATA",
      [
        "storage",
        "00bfe458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5ac0",
      "DATA",
      [
        "storage",
        "00bfe508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5abc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5ab4.md#insn-007c5abc)
- 新版 [`007c5abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ab4.md#insn-007c5abc)

~~~diff
- 007c5abc ["COPY", "tmp:0:8", ["const:458:8"]]
- 007c5abc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c5abc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c5abc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c5abc ["COPY", "tmp:0:8", ["const:508:8"]]
+ 007c5abc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5abc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5abc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c5abc bytes 29611191
+ 007c5abc bytes 29211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95e5a4deec410bc879455d6c8d9df9bf"></a>

### [`007c5ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5ad0.md) → [`007c5ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ad0.md) FUN_007c5ad0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`007c5d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5d70.md) [`007c5d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5d74.md) [`007c5e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5e2c.md) [`007c5e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5e30.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`007c5d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d70.md) [`007c5d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d74.md) [`007c5e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5e2c.md) [`007c5e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5e30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.63% / 新版 96.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c5b44",
      "incomplete_value": false,
      "site": "007c5b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5b44",
      "incomplete_value": false,
      "site": "007c5b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007c5b44",
      "DATA",
      [
        "storage",
        "00bfe4c8",
        null,
        "undefined *"
      ]
    ],
    [
      "007c5b80",
      "DATA",
      [
        "storage",
        "00bfe548",
        null,
        "undefined *"
      ]
    ],
    [
      "007c5bb4",
      "READ",
      [
        "storage",
        "00bfe568",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c5b44",
      "DATA",
      [
        "storage",
        "00bfe578",
        null,
        "undefined *"
      ]
    ],
    [
      "007c5b80",
      "DATA",
      [
        "storage",
        "00bfe5f8",
        null,
        "undefined *"
      ]
    ],
    [
      "007c5bb4",
      "READ",
      [
        "storage",
        "00bfe618",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5ad0.md#insn-007c5b3c) · [`007c5b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5ad0.md#insn-007c5b78)
- 新版 [`007c5b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ad0.md#insn-007c5b3c) · [`007c5b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5ad0.md#insn-007c5b78)

~~~diff
- 007c5b3c ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 007c5b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5b3c ["COPY", "tmp:0:8", ["const:578:8"]]
+ 007c5b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5b3c bytes 08211391
+ 007c5b3c bytes 08e11591
- 007c5b78 ["COPY", "tmp:0:8", ["const:548:8"]]
- 007c5b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5b78 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 007c5b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5b78 bytes 08211591
+ 007c5b78 bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6462751b93cd3e770558404943182ae3"></a>

### [`007c5d28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5d28.md) → [`007c5d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d28.md) FUN_007c5d28

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
      "definition_site": "007c5d4c",
      "incomplete_value": false,
      "site": "007c5d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5d4c",
      "incomplete_value": false,
      "site": "007c5d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c5d4c",
      "DATA",
      [
        "storage",
        "00bfe4c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5d4c",
      "DATA",
      [
        "storage",
        "00bfe578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5d28.md#insn-007c5d48)
- 新版 [`007c5d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d28.md#insn-007c5d48)

~~~diff
- 007c5d48 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 007c5d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5d48 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 007c5d48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5d48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5d48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5d48 bytes 08211391
+ 007c5d48 bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afedf2388f9e9ad123ccb5e8b4ef1218"></a>

### [`007c5d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5d5c.md) → [`007c5d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d5c.md) FUN_007c5d5c

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
      "definition_site": "007c5d68",
      "incomplete_value": false,
      "site": "007c5d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5d68",
      "incomplete_value": false,
      "site": "007c5d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c5d68",
      "DATA",
      [
        "storage",
        "00bfe4c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5d68",
      "DATA",
      [
        "storage",
        "00bfe578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5d5c.md#insn-007c5d64)
- 新版 [`007c5d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5d5c.md#insn-007c5d64)

~~~diff
- 007c5d64 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 007c5d64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c5d64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c5d64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c5d64 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 007c5d64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5d64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5d64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c5d64 bytes 29211391
+ 007c5d64 bytes 29e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ca215163a3a0099ca3d8e859c8d2c5f"></a>

### [`007c5de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5de4.md) → [`007c5de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5de4.md) FUN_007c5de4

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
      "definition_site": "007c5e08",
      "incomplete_value": false,
      "site": "007c5e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5e08",
      "incomplete_value": false,
      "site": "007c5e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "007c5e08",
      "DATA",
      [
        "storage",
        "00bfe548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5e08",
      "DATA",
      [
        "storage",
        "00bfe5f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5de4.md#insn-007c5e04)
- 新版 [`007c5e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5de4.md#insn-007c5e04)

~~~diff
- 007c5e04 ["COPY", "tmp:0:8", ["const:548:8"]]
- 007c5e04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c5e04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c5e04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c5e04 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 007c5e04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5e04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c5e04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c5e04 bytes 08211591
+ 007c5e04 bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-284a6012599f4769ddfa5ac93690bba9"></a>

### [`007c5e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5e18.md) → [`007c5e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5e18.md) FUN_007c5e18

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
      "definition_site": "007c5e24",
      "incomplete_value": false,
      "site": "007c5e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c5e24",
      "incomplete_value": false,
      "site": "007c5e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "007c5e24",
      "DATA",
      [
        "storage",
        "00bfe548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c5e24",
      "DATA",
      [
        "storage",
        "00bfe5f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c5e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c5/007c5e18.md#insn-007c5e20)
- 新版 [`007c5e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c5/007c5e18.md#insn-007c5e20)

~~~diff
- 007c5e20 ["COPY", "tmp:0:8", ["const:548:8"]]
- 007c5e20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c5e20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c5e20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c5e20 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 007c5e20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5e20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c5e20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c5e20 bytes 29211591
+ 007c5e20 bytes 29e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee30f7ba98fe33ac5de11786489cd102"></a>

### [`007c616c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c616c.md) → [`007c616c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c616c.md) FUN_007c616c

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
      "definition_site": "007c6190",
      "incomplete_value": false,
      "site": "007c6190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6190",
      "incomplete_value": false,
      "site": "007c6190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "007c6190",
      "DATA",
      [
        "storage",
        "00bfe5d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6190",
      "DATA",
      [
        "storage",
        "00bfe688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c618c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c616c.md#insn-007c618c)
- 新版 [`007c618c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c616c.md#insn-007c618c)

~~~diff
- 007c618c ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 007c618c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c618c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c618c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c618c ["COPY", "tmp:0:8", ["const:688:8"]]
+ 007c618c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c618c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c618c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c618c bytes 08611791
+ 007c618c bytes 08211a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fcb07c929f12decf3b1b748f99c6d45"></a>

### [`007c61a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c61a0.md) → [`007c61a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c61a0.md) FUN_007c61a0

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
      "definition_site": "007c61ac",
      "incomplete_value": false,
      "site": "007c61ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c61ac",
      "incomplete_value": false,
      "site": "007c61ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "007c61ac",
      "DATA",
      [
        "storage",
        "00bfe5d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c61ac",
      "DATA",
      [
        "storage",
        "00bfe688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c61a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c61a0.md#insn-007c61a8)
- 新版 [`007c61a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c61a0.md#insn-007c61a8)

~~~diff
- 007c61a8 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 007c61a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c61a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c61a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c61a8 ["COPY", "tmp:0:8", ["const:688:8"]]
+ 007c61a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c61a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c61a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c61a8 bytes 29611791
+ 007c61a8 bytes 29211a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c478d8a897ac58dfeffc4c2ce0c5ac95"></a>

### [`007c6294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6294.md) → [`007c6294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6294.md) FUN_007c6294

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
      "definition_site": "007c62a0",
      "incomplete_value": false,
      "site": "007c62a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c62a0",
      "incomplete_value": false,
      "site": "007c62a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "007c62a0",
      "DATA",
      [
        "storage",
        "00bfe658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c62a0",
      "DATA",
      [
        "storage",
        "00bfe708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c629c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6294.md#insn-007c629c)
- 新版 [`007c629c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6294.md#insn-007c629c)

~~~diff
- 007c629c ["COPY", "tmp:0:8", ["const:658:8"]]
- 007c629c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c629c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c629c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c629c ["COPY", "tmp:0:8", ["const:708:8"]]
+ 007c629c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c629c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c629c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c629c bytes 29611991
+ 007c629c bytes 29211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f57d9df35bd6eaac00f3016b1a41a4fc"></a>

### [`007c62b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c62b0.md) → [`007c62b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c62b0.md) FUN_007c62b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004489a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044aa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044aa9c.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004489a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.60% / 新版 95.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007c62fc",
      "incomplete_value": true,
      "site": "007c62fc",
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
      "definition_site": "007c62fc",
      "incomplete_value": true,
      "site": "007c62fc",
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
      "definition_site": "007c6304",
      "incomplete_value": false,
      "site": "007c6314",
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
      "definition_site": "007c6304",
      "incomplete_value": false,
      "site": "007c6314",
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
      "definition_site": "007c630c",
      "incomplete_value": false,
      "site": "007c6314",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c630c",
      "incomplete_value": false,
      "site": "007c6314",
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
            "const:468:8"
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
      "007c62e0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c6304",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c630c",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c62e0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c6304",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c630c",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c62e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c62b0.md#insn-007c62e0) · [`007c6304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c62b0.md#insn-007c6304) · [`007c630c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c62b0.md#insn-007c630c)
- 新版 [`007c62e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c62b0.md#insn-007c62e0) · [`007c6304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c62b0.md#insn-007c6304) · [`007c630c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c62b0.md#insn-007c630c)

~~~diff
- 007c62e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007c62e0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c62e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007c62e0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c62e0 bytes 00dd44f9
+ 007c62e0 bytes 003d45f9
- 007c6304 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007c6304 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c6304 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c6304 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c6304 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007c6304 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c6304 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c6304 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c6304 bytes 21603691
+ 007c6304 bytes 21203991
- 007c630c ["COPY", "tmp:0:8", ["const:468:8"]]
- 007c630c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c630c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c630c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c630c ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007c630c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c630c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c630c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c630c bytes 42a01191
+ 007c630c bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87ebe9d6f23c6f3a54dc1090f7ef4dcf"></a>

### [`007c6448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6448.md) → [`007c6448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6448.md) FUN_007c6448

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
      "definition_site": "007c646c",
      "incomplete_value": false,
      "site": "007c646c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c646c",
      "incomplete_value": false,
      "site": "007c646c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c646c",
      "DATA",
      [
        "storage",
        "00bfe6e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c646c",
      "DATA",
      [
        "storage",
        "00bfe798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6448.md#insn-007c6468)
- 新版 [`007c6468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6448.md#insn-007c6468)

~~~diff
- 007c6468 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 007c6468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6468 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 007c6468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6468 bytes 08a11b91
+ 007c6468 bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cbc691a320d3e71887a468c59b489bd"></a>

### [`007c647c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c647c.md) → [`007c647c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c647c.md) FUN_007c647c

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
      "definition_site": "007c6488",
      "incomplete_value": false,
      "site": "007c6488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6488",
      "incomplete_value": false,
      "site": "007c6488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c6488",
      "DATA",
      [
        "storage",
        "00bfe6e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6488",
      "DATA",
      [
        "storage",
        "00bfe798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c647c.md#insn-007c6484)
- 新版 [`007c6484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c647c.md#insn-007c6484)

~~~diff
- 007c6484 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 007c6484 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c6484 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c6484 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c6484 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 007c6484 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c6484 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c6484 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c6484 bytes 29a11b91
+ 007c6484 bytes 29611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90b8fc123fd9d608eab2208418a7eee1"></a>

### [`007c6498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6498.md) → [`007c6498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6498.md) FUN_007c6498

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00447378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447378.md) [`004489a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0044aa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044aa9c.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00447378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447378.md) [`004489a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 97.99% / 新版 97.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007c64f0",
      "incomplete_value": true,
      "site": "007c64f0",
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
      "definition_site": "007c64f0",
      "incomplete_value": true,
      "site": "007c64f0",
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
      "007c64d4",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c64f8",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c6500",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c64d4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c64f8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c6500",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c64d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6498.md#insn-007c64d4) · [`007c64f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6498.md#insn-007c64f8) · [`007c6500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6498.md#insn-007c6500)
- 新版 [`007c64d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6498.md#insn-007c64d4) · [`007c64f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6498.md#insn-007c64f8) · [`007c6500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6498.md#insn-007c6500)

~~~diff
- 007c64d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007c64d4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c64d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007c64d4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c64d4 bytes 00dd44f9
+ 007c64d4 bytes 003d45f9
- 007c64f8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007c64f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c64f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c64f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c64f8 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007c64f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c64f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c64f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c64f8 bytes 21603691
+ 007c64f8 bytes 21203991
- 007c6500 ["COPY", "tmp:0:8", ["const:468:8"]]
- 007c6500 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c6500 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c6500 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c6500 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007c6500 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c6500 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c6500 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c6500 bytes 42a01191
+ 007c6500 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a8a380439ddbb580ae5fb1dff0799a8"></a>

### [`007c67e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c67e0.md) → [`007c67e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c67e0.md) FUN_007c67e0

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
      "definition_site": "007c6804",
      "incomplete_value": false,
      "site": "007c6804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6804",
      "incomplete_value": false,
      "site": "007c6804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "007c6804",
      "DATA",
      [
        "storage",
        "00bfe778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6804",
      "DATA",
      [
        "storage",
        "00bfe828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c67e0.md#insn-007c6800)
- 新版 [`007c6800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c67e0.md#insn-007c6800)

~~~diff
- 007c6800 ["COPY", "tmp:0:8", ["const:778:8"]]
- 007c6800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6800 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 007c6800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6800 bytes 08e11d91
+ 007c6800 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faf171a48232933ae48ca0077399b5b4"></a>

### [`007c6830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6830.md) → [`007c6830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6830.md) FUN_007c6830

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md) [`004489a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`004489a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/004489a8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.33% / 新版 96.33%

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
      "definition_site": "007c6870",
      "incomplete_value": true,
      "site": "007c6870",
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
      "definition_site": "007c6870",
      "incomplete_value": true,
      "site": "007c6870",
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
      "definition_site": "007c6878",
      "incomplete_value": false,
      "site": "007c6888",
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
      "definition_site": "007c6878",
      "incomplete_value": false,
      "site": "007c6888",
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
      "definition_site": "007c6880",
      "incomplete_value": false,
      "site": "007c6888",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6880",
      "incomplete_value": false,
      "site": "007c6888",
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
            "const:468:8"
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
      "007c6860",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c6878",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c6880",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c6860",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c6878",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c6880",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6830.md#insn-007c6860) · [`007c6878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6830.md#insn-007c6878) · [`007c6880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6830.md#insn-007c6880)
- 新版 [`007c6860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6830.md#insn-007c6860) · [`007c6878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6830.md#insn-007c6878) · [`007c6880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6830.md#insn-007c6880)

~~~diff
- 007c6860 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
- 007c6860 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c6860 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 007c6860 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c6860 bytes 20dd44f9
+ 007c6860 bytes 203d45f9
- 007c6878 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007c6878 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c6878 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c6878 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c6878 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007c6878 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c6878 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c6878 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c6878 bytes 21603691
+ 007c6878 bytes 21203991
- 007c6880 ["COPY", "tmp:0:8", ["const:468:8"]]
- 007c6880 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c6880 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c6880 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c6880 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007c6880 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c6880 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c6880 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c6880 bytes 42a01191
+ 007c6880 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ab7db22452a3f79752c3849dcfc1942"></a>

### [`007c6a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6a3c.md) → [`007c6a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6a3c.md) FUN_007c6a3c

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
      "definition_site": "007c6a50",
      "incomplete_value": false,
      "site": "007c6a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6a50",
      "incomplete_value": false,
      "site": "007c6a54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "007c6a54",
      "DATA",
      [
        "storage",
        "00bfe7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6a54",
      "DATA",
      [
        "storage",
        "00bfe8a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6a50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6a3c.md#insn-007c6a50)
- 新版 [`007c6a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6a3c.md#insn-007c6a50)

~~~diff
- 007c6a50 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 007c6a50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6a50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6a50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6a50 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 007c6a50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6a50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6a50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6a50 bytes 08e11f91
+ 007c6a50 bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-156e66d32700ded28bef6607d1ce70eb"></a>

### [`007c6b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6b9c.md) → [`007c6b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6b9c.md) FUN_007c6b9c

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
      "definition_site": "007c6bb0",
      "incomplete_value": false,
      "site": "007c6bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6bb0",
      "incomplete_value": false,
      "site": "007c6bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "007c6bb4",
      "DATA",
      [
        "storage",
        "00bfe8f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6bb4",
      "DATA",
      [
        "storage",
        "00bfe9a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6b9c.md#insn-007c6bb0)
- 新版 [`007c6bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6b9c.md#insn-007c6bb0)

~~~diff
- 007c6bb0 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 007c6bb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6bb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6bb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6bb0 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 007c6bb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6bb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6bb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6bb0 bytes 08e12391
+ 007c6bb0 bytes 08a12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d283ea416830884367315fb6cc25639"></a>

### [`007c6c4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6c4c.md) → [`007c6c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6c4c.md) FUN_007c6c4c

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
      "definition_site": "007c6c60",
      "incomplete_value": false,
      "site": "007c6c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6c60",
      "incomplete_value": false,
      "site": "007c6c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      "007c6c64",
      "DATA",
      [
        "storage",
        "00bfe978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6c64",
      "DATA",
      [
        "storage",
        "00bfea28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6c4c.md#insn-007c6c60)
- 新版 [`007c6c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6c4c.md#insn-007c6c60)

~~~diff
- 007c6c60 ["COPY", "tmp:0:8", ["const:978:8"]]
- 007c6c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6c60 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 007c6c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6c60 bytes 08e12591
+ 007c6c60 bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb473d5f88ca3e71b1ce2ae3eb817545"></a>

### [`007c6cfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6cfc.md) → [`007c6cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6cfc.md) FUN_007c6cfc

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
      "definition_site": "007c6d10",
      "incomplete_value": false,
      "site": "007c6d14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6d10",
      "incomplete_value": false,
      "site": "007c6d14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "007c6d14",
      "DATA",
      [
        "storage",
        "00bfe9f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6d14",
      "DATA",
      [
        "storage",
        "00bfeaa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6cfc.md#insn-007c6d10)
- 新版 [`007c6d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6cfc.md#insn-007c6d10)

~~~diff
- 007c6d10 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 007c6d10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6d10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6d10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6d10 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 007c6d10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6d10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6d10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6d10 bytes 08e12791
+ 007c6d10 bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2286c9553a2c60f32e79ff144570a83e"></a>

### [`007c6dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6dac.md) → [`007c6dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6dac.md) FUN_007c6dac

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
      "definition_site": "007c6dcc",
      "incomplete_value": false,
      "site": "007c6dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6dcc",
      "incomplete_value": false,
      "site": "007c6dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:a78:8"
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
      "007c6dd0",
      "DATA",
      [
        "storage",
        "00bfea78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6dd0",
      "DATA",
      [
        "storage",
        "00bfeb28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6dac.md#insn-007c6dcc)
- 新版 [`007c6dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6dac.md#insn-007c6dcc)

~~~diff
- 007c6dcc ["COPY", "tmp:0:8", ["const:a78:8"]]
- 007c6dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6dcc ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 007c6dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6dcc bytes 08e12991
+ 007c6dcc bytes 08a12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5c5a66f9fff14200fda949b5ce59ac5"></a>

### [`007c6e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6e78.md) → [`007c6e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6e78.md) FUN_007c6e78

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
      "definition_site": "007c6e8c",
      "incomplete_value": true,
      "site": "007c6e90",
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
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6e8c",
      "incomplete_value": true,
      "site": "007c6e90",
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
            "const:af8:8"
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
      "007c6e90",
      "DATA",
      [
        "storage",
        "00bfeaf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6e90",
      "DATA",
      [
        "storage",
        "00bfeba8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6e78.md#insn-007c6e8c)
- 新版 [`007c6e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6e78.md#insn-007c6e8c)

~~~diff
- 007c6e8c ["COPY", "tmp:0:8", ["const:af8:8"]]
- 007c6e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6e8c ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 007c6e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6e8c bytes 08e12b91
+ 007c6e8c bytes 08a12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e1388c635a145618aad1096ca056e08"></a>

### [`007c6f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6f28.md) → [`007c6f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f28.md) FUN_007c6f28

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
      "definition_site": "007c6f48",
      "incomplete_value": false,
      "site": "007c6f4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c6f48",
      "incomplete_value": false,
      "site": "007c6f4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "007c6f4c",
      "DATA",
      [
        "storage",
        "00bfeb78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c6f4c",
      "DATA",
      [
        "storage",
        "00bfec28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c6f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6f28.md#insn-007c6f48)
- 新版 [`007c6f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f28.md#insn-007c6f48)

~~~diff
- 007c6f48 ["COPY", "tmp:0:8", ["const:b78:8"]]
- 007c6f48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c6f48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c6f48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c6f48 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 007c6f48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6f48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c6f48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c6f48 bytes 08e12d91
+ 007c6f48 bytes 08a13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f944d31c6d51ab5c0de0718a15d20a8"></a>

### [`007c6f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6f80.md) → [`007c6f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f80.md) FUN_007c6f80

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.89% / 新版 96.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c71a0",
      "incomplete_value": true,
      "site": "007c71a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c71a0",
      "incomplete_value": true,
      "site": "007c71a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ac:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "007c7330",
      "incomplete_value": false,
      "site": "007c7330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c7330",
      "incomplete_value": false,
      "site": "007c7330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "007c7094",
      "READ",
      [
        "storage",
        "002a391d",
        null,
        "string"
      ]
    ],
    [
      "007c7184",
      "READ",
      [
        "storage",
        "002a27ac",
        null,
        "string"
      ]
    ],
    [
      "007c71e0",
      "DATA",
      [
        "storage",
        "00bfec68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c7094",
      "READ",
      [
        "storage",
        "002a3916",
        null,
        "string"
      ]
    ],
    [
      "007c7184",
      "READ",
      [
        "storage",
        "002a27a5",
        null,
        "string"
      ]
    ],
    [
      "007c71e0",
      "DATA",
      [
        "storage",
        "00bfed18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c708c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6f80.md#insn-007c708c) · [`007c7180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6f80.md#insn-007c7180) · [`007c71d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c6/007c6f80.md#insn-007c71d8)
- 新版 [`007c708c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f80.md#insn-007c708c) · [`007c7180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f80.md#insn-007c7180) · [`007c71d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c6/007c6f80.md#insn-007c71d8)

~~~diff
- 007c708c ["COPY", "tmp:0:8", ["const:91d:8"]]
- 007c708c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c708c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c708c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c708c ["COPY", "tmp:0:8", ["const:916:8"]]
+ 007c708c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c708c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c708c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c708c bytes 29752491
+ 007c708c bytes 29592491
- 007c7180 ["COPY", "tmp:0:8", ["const:7ac:8"]]
- 007c7180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007c7180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007c7180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007c7180 ["COPY", "tmp:0:8", ["const:7a5:8"]]
+ 007c7180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007c7180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007c7180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007c7180 bytes 29b11e91
+ 007c7180 bytes 29951e91
- 007c71d8 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 007c71d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c71d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c71d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c71d8 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 007c71d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c71d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c71d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c71d8 bytes 08a13191
+ 007c71d8 bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6be6cb505d90d7e2eb1f830cafa14ada"></a>

### [`007c7590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7590.md) → [`007c7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7590.md) FUN_007c7590

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
      "definition_site": "007c75b0",
      "incomplete_value": false,
      "site": "007c75b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c75b0",
      "incomplete_value": false,
      "site": "007c75b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "007c75b4",
      "DATA",
      [
        "storage",
        "00bfebe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c75b4",
      "DATA",
      [
        "storage",
        "00bfec98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c75b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7590.md#insn-007c75b0)
- 新版 [`007c75b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7590.md#insn-007c75b0)

~~~diff
- 007c75b0 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 007c75b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c75b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c75b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c75b0 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 007c75b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c75b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c75b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c75b0 bytes 08a12f91
+ 007c75b0 bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2867b0452c8e2370cfe76671aef30ea9"></a>

### [`007c76a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c76a0.md) → [`007c76a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c76a0.md) FUN_007c76a0

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
      "definition_site": "007c76b4",
      "incomplete_value": false,
      "site": "007c76b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c76b4",
      "incomplete_value": false,
      "site": "007c76b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "007c76b8",
      "DATA",
      [
        "storage",
        "00bfec68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c76b8",
      "DATA",
      [
        "storage",
        "00bfed18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c76b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c76a0.md#insn-007c76b4)
- 新版 [`007c76b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c76a0.md#insn-007c76b4)

~~~diff
- 007c76b4 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 007c76b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c76b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c76b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c76b4 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 007c76b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c76b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c76b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c76b4 bytes 08a13191
+ 007c76b4 bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38547db6ce984545a9d4897052da2548"></a>

### [`007c76c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c76c4.md) → [`007c76c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c76c4.md) FUN_007c76c4

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
      "definition_site": "007c76c8",
      "incomplete_value": false,
      "site": "007c76cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c76c8",
      "incomplete_value": false,
      "site": "007c76cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "007c76cc",
      "DATA",
      [
        "storage",
        "00bfec68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c76cc",
      "DATA",
      [
        "storage",
        "00bfed18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c76c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c76c4.md#insn-007c76c8)
- 新版 [`007c76c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c76c4.md#insn-007c76c8)

~~~diff
- 007c76c8 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 007c76c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c76c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c76c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c76c8 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 007c76c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c76c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c76c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c76c8 bytes 08a13191
+ 007c76c8 bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5395c00a6450c27c57659cff1738547"></a>

### [`007c7750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7750.md) → [`007c7750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7750.md) FUN_007c7750

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "007c776c",
      "incomplete_value": false,
      "site": "007c7778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c776c",
      "incomplete_value": false,
      "site": "007c7778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "007c7778",
      "DATA",
      [
        "storage",
        "00bfecf8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c7778",
      "DATA",
      [
        "storage",
        "00bfeda8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c776c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7750.md#insn-007c776c)
- 新版 [`007c776c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7750.md#insn-007c776c)

~~~diff
- 007c776c ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 007c776c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c776c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c776c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c776c ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 007c776c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c776c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c776c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c776c bytes 08e13391
+ 007c776c bytes 08a13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da4ac8f112d0bff7c817aac1aa0f7040"></a>

### [`007c7798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7798.md) → [`007c7798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7798.md) FUN_007c7798

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007c779c",
      "incomplete_value": false,
      "site": "007c77a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c779c",
      "incomplete_value": false,
      "site": "007c77a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "007c77a0",
      "DATA",
      [
        "storage",
        "00bfecf8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c77a0",
      "DATA",
      [
        "storage",
        "00bfeda8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c779c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7798.md#insn-007c779c)
- 新版 [`007c779c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7798.md#insn-007c779c)

~~~diff
- 007c779c ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 007c779c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c779c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c779c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c779c ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 007c779c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c779c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c779c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c779c bytes 08e13391
+ 007c779c bytes 08a13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e35240083d948e9e90e34663955d6d21"></a>

### [`007c77c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c77c8.md) → [`007c77c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c77c8.md) FUN_007c77c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 26件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 26件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.79% / 新版 98.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c7c68",
      "incomplete_value": false,
      "site": "007c7c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c7c68",
      "incomplete_value": false,
      "site": "007c7c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "007c7c44",
      "incomplete_value": false,
      "site": "007c7c4c",
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
            "const:ded:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c7c44",
      "incomplete_value": false,
      "site": "007c7c4c",
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
            "const:e81:8"
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
      "007c7c44",
      "PARAM",
      [
        "storage",
        "002ade81",
        null,
        "string"
      ]
    ],
    [
      "007c7c68",
      "DATA",
      [
        "storage",
        "00bfed68",
        null,
        "undefined *"
      ]
    ],
    [
      "007c7cc0",
      "READ",
      [
        "storage",
        "00bfed88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c7c44",
      "PARAM",
      [
        "storage",
        "002added",
        null,
        "string"
      ]
    ],
    [
      "007c7c68",
      "DATA",
      [
        "storage",
        "00bfee18",
        null,
        "undefined *"
      ]
    ],
    [
      "007c7cc0",
      "READ",
      [
        "storage",
        "00bfee38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c7c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c77c8.md#insn-007c7c44) · [`007c7c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c77c8.md#insn-007c7c60) · [`007c7c64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c77c8.md#insn-007c7c64)
- 新版 [`007c7c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c77c8.md#insn-007c7c44) · [`007c7c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c77c8.md#insn-007c7c60)

~~~diff
- 007c7c44 ["COPY", "tmp:0:8", ["const:e81:8"]]
- 007c7c44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c7c44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c7c44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c7c44 ["COPY", "tmp:0:8", ["const:ded:8"]]
+ 007c7c44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c7c44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c7c44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c7c44 bytes 21043a91
+ 007c7c44 bytes 21b43791
- 007c7c60 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 007c7c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c7c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c7c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c7c60 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 007c7c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c7c60 bytes 08a13591
+ 007c7c60 bytes 08613891
- 007c7c64 ["INT_SUB", "register:4098:8", ["register:40e8:8", "const:40:8"]]
- 007c7c64 bytes b30301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39aec31edc2884d64fafa5455607df20"></a>

### [`007c7dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7dac.md) → [`007c7dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7dac.md) FUN_007c7dac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007c77c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c77c8.md) [`007c8c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c8c78.md) · 呼出先 11件 [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`0063e588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063e588.md) [`0071a054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0071a/0071a054.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 2件 [`007c77c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c77c8.md) [`007c8c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8c78.md) · 呼出先 11件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0063e588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e588.md) [`0071a054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a054.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.18% / 新版 83.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007c7f24",
      "incomplete_value": false,
      "site": "007c7f24",
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
      "definition_site": "007c7f24",
      "incomplete_value": false,
      "site": "007c7f24",
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
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007c7f28",
      "incomplete_value": false,
      "site": "007c7f28",
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
      "definition_site": "007c7f28",
      "incomplete_value": false,
      "site": "007c7f28",
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
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c7f24",
      "incomplete_value": false,
      "site": "007c7f28",
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
      "definition_site": "007c7f24",
      "incomplete_value": false,
      "site": "007c7f28",
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
      "007c7df8",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "007c7e10",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      "007c7e14",
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
      "007c7df8",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "007c7e10",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "007c7e14",
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

- 旧版 [`007c7df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7dac.md#insn-007c7df0) · [`007c7df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7dac.md#insn-007c7df4) · [`007c7e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7dac.md#insn-007c7e0c)
- 新版 [`007c7df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7dac.md#insn-007c7df0) · [`007c7df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7dac.md#insn-007c7df4) · [`007c7e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7dac.md#insn-007c7e0c)

~~~diff
- 007c7df0 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 007c7df0 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 007c7df0 bytes e82200b0
+ 007c7df0 bytes e82200d0
- 007c7df4 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 007c7df4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c7df4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c7df4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c7df4 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 007c7df4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7df4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7df4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c7df4 bytes 08e13d91
+ 007c7df4 bytes 08e10091
- 007c7e0c ["COPY", "register:4000:8", ["const:c24000:8"]]
+ 007c7e0c ["COPY", "register:4000:8", ["const:c25000:8"]]
- 007c7e0c bytes e02200b0
+ 007c7e0c bytes e02200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e28fa3660b3b5bf70fcd123e8112e69"></a>

### [`007c7f88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7f88.md) → [`007c7f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7f88.md) FUN_007c7f88

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
      "definition_site": "007c7f9c",
      "incomplete_value": false,
      "site": "007c7fa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c7f9c",
      "incomplete_value": false,
      "site": "007c7fa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "007c7fa0",
      "DATA",
      [
        "storage",
        "00bfed68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c7fa0",
      "DATA",
      [
        "storage",
        "00bfee18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c7f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7f88.md#insn-007c7f9c)
- 新版 [`007c7f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7f88.md#insn-007c7f9c)

~~~diff
- 007c7f9c ["COPY", "tmp:0:8", ["const:d68:8"]]
- 007c7f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c7f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c7f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c7f9c ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 007c7f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c7f9c bytes 08a13591
+ 007c7f9c bytes 08613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-817612a96492bd7f611d1285732d0667"></a>

### [`007c7fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7fac.md) → [`007c7fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7fac.md) FUN_007c7fac

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
      "definition_site": "007c7fb0",
      "incomplete_value": false,
      "site": "007c7fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c7fb0",
      "incomplete_value": false,
      "site": "007c7fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "007c7fb4",
      "DATA",
      [
        "storage",
        "00bfed68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c7fb4",
      "DATA",
      [
        "storage",
        "00bfee18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c7fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c7/007c7fac.md#insn-007c7fb0)
- 新版 [`007c7fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c7/007c7fac.md#insn-007c7fb0)

~~~diff
- 007c7fb0 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 007c7fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c7fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c7fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c7fb0 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 007c7fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c7fb0 bytes 08a13591
+ 007c7fb0 bytes 08613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba634a6656e46337b12b7a5f017c46fa"></a>

### [`007c8038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c8038.md) → [`007c8038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8038.md) FUN_007c8038

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
      "definition_site": "007c805c",
      "incomplete_value": false,
      "site": "007c8060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c805c",
      "incomplete_value": false,
      "site": "007c8060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "007c8060",
      "DATA",
      [
        "storage",
        "00bfedf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c8060",
      "DATA",
      [
        "storage",
        "00bfeea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c805c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c8038.md#insn-007c805c)
- 新版 [`007c805c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8038.md#insn-007c805c)

~~~diff
- 007c805c ["COPY", "tmp:0:8", ["const:df8:8"]]
- 007c805c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c805c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c805c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c805c ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 007c805c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c805c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c805c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c805c bytes 08e13791
+ 007c805c bytes 08a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2504624bef90183060caf1b0a4fc6cf5"></a>

### [`007c80a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c80a0.md) → [`007c80a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c80a0.md) FUN_007c80a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 36件 [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md) [`00445d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445d90.md)
- 新版 呼出元 0件  · 呼出先 36件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00445d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.72% / 新版 99.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007c8114",
      "incomplete_value": true,
      "site": "007c8114",
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
      "definition_site": "007c8114",
      "incomplete_value": true,
      "site": "007c8114",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007c8124",
      "incomplete_value": true,
      "site": "007c812c",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c8124",
      "incomplete_value": true,
      "site": "007c812c",
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
            "const:468:8"
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
      "007c8104",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "007c811c",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c8124",
      "PARAM",
      [
        "storage",
        "00bf4468",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c8104",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c811c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c8124",
      "PARAM",
      [
        "storage",
        "00bf4518",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c80a0.md#insn-007c8104) · [`007c811c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c80a0.md#insn-007c811c) · [`007c8124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c80a0.md#insn-007c8124)
- 新版 [`007c8104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c80a0.md#insn-007c8104) · [`007c811c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c80a0.md#insn-007c811c) · [`007c8124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c80a0.md#insn-007c8124)

~~~diff
- 007c8104 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 007c8104 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c8104 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007c8104 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c8104 bytes 00dd44f9
+ 007c8104 bytes 003d45f9
- 007c811c ["COPY", "tmp:0:8", ["const:d98:8"]]
- 007c811c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c811c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c811c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c811c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 007c811c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c811c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c811c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c811c bytes 21603691
+ 007c811c bytes 21203991
- 007c8124 ["COPY", "tmp:0:8", ["const:468:8"]]
- 007c8124 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007c8124 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007c8124 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007c8124 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 007c8124 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007c8124 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007c8124 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007c8124 bytes 42a01191
+ 007c8124 bytes 42601491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3c496f413e27eafd88a74065547c02a"></a>

### [`007c8c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c8c10.md) → [`007c8c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8c10.md) FUN_007c8c10

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
      "definition_site": "007c8c34",
      "incomplete_value": false,
      "site": "007c8c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c8c34",
      "incomplete_value": false,
      "site": "007c8c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
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
      "007c8c38",
      "DATA",
      [
        "storage",
        "00bfee78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c8c38",
      "DATA",
      [
        "storage",
        "00bfef28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c8c10.md#insn-007c8c34)
- 新版 [`007c8c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8c10.md#insn-007c8c34)

~~~diff
- 007c8c34 ["COPY", "tmp:0:8", ["const:e78:8"]]
- 007c8c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c8c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c8c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c8c34 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 007c8c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c8c34 bytes 08e13991
+ 007c8c34 bytes 08a13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fadd6bda22a5b4f8a83afb9c566474f"></a>

### [`007c8ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c8ebc.md) → [`007c8ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8ebc.md) FUN_007c8ebc

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
      "definition_site": "007c8ed0",
      "incomplete_value": false,
      "site": "007c8ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c8ed0",
      "incomplete_value": false,
      "site": "007c8ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
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
      "007c8ed4",
      "DATA",
      [
        "storage",
        "00bfeef8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c8ed4",
      "DATA",
      [
        "storage",
        "00bfefa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c8ebc.md#insn-007c8ed0)
- 新版 [`007c8ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8ebc.md#insn-007c8ed0)

~~~diff
- 007c8ed0 ["COPY", "tmp:0:8", ["const:ef8:8"]]
- 007c8ed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c8ed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c8ed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c8ed0 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 007c8ed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8ed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8ed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c8ed0 bytes 08e13b91
+ 007c8ed0 bytes 08a13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddfe4cd19b93f21b97d96df973f6e580"></a>

### [`007c8f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c8f6c.md) → [`007c8f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8f6c.md) FUN_007c8f6c

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
      "definition_site": "007c8f80",
      "incomplete_value": false,
      "site": "007c8f84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c8f80",
      "incomplete_value": false,
      "site": "007c8f84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "007c8f84",
      "DATA",
      [
        "storage",
        "00bfef78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c8f84",
      "DATA",
      [
        "storage",
        "00bff028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c8f6c.md#insn-007c8f7c) · [`007c8f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c8/007c8f6c.md#insn-007c8f80)
- 新版 [`007c8f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8f6c.md#insn-007c8f7c) · [`007c8f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c8/007c8f6c.md#insn-007c8f80)

~~~diff
- 007c8f7c ["COPY", "register:4040:8", ["const:bfe000:8"]]
+ 007c8f7c ["COPY", "register:4040:8", ["const:bff000:8"]]
- 007c8f7c bytes a82100d0
+ 007c8f7c bytes a82100f0
- 007c8f80 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 007c8f80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c8f80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c8f80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c8f80 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 007c8f80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8f80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8f80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c8f80 bytes 08e13d91
+ 007c8f80 bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6edf30bfa512b69f2e90e5f9f724e7af"></a>

### [`007c901c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c901c.md) → [`007c901c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c901c.md) FUN_007c901c

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
      "definition_site": "007c9030",
      "incomplete_value": false,
      "site": "007c9034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9030",
      "incomplete_value": false,
      "site": "007c9034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfe000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
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
      "007c9034",
      "DATA",
      [
        "storage",
        "00bfeff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9034",
      "DATA",
      [
        "storage",
        "00bff0a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c902c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c901c.md#insn-007c902c) · [`007c9030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c901c.md#insn-007c9030)
- 新版 [`007c902c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c901c.md#insn-007c902c) · [`007c9030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c901c.md#insn-007c9030)

~~~diff
- 007c902c ["COPY", "register:4040:8", ["const:bfe000:8"]]
+ 007c902c ["COPY", "register:4040:8", ["const:bff000:8"]]
- 007c902c bytes a82100b0
+ 007c902c bytes a82100d0
- 007c9030 ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 007c9030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9030 ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 007c9030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9030 bytes 08e13f91
+ 007c9030 bytes 08a10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-715fa61f078a313264d9c1eafa008e04"></a>

### [`007c90cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c90cc.md) → [`007c90cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c90cc.md) FUN_007c90cc

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
      "definition_site": "007c90f0",
      "incomplete_value": false,
      "site": "007c90f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c90f0",
      "incomplete_value": false,
      "site": "007c90f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
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
      "007c90f0",
      "DATA",
      [
        "storage",
        "00bff078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c90f0",
      "DATA",
      [
        "storage",
        "00bff128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c90ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c90cc.md#insn-007c90ec)
- 新版 [`007c90ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c90cc.md#insn-007c90ec)

~~~diff
- 007c90ec ["COPY", "tmp:0:8", ["const:78:8"]]
- 007c90ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c90ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c90ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c90ec ["COPY", "tmp:0:8", ["const:128:8"]]
+ 007c90ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c90ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c90ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c90ec bytes 08e10191
+ 007c90ec bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77294feea51cca967dbbaa023ea5deff"></a>

### [`007c9190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9190.md) → [`007c9190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9190.md) FUN_007c9190

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
      "definition_site": "007c91b4",
      "incomplete_value": false,
      "site": "007c91b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c91b4",
      "incomplete_value": false,
      "site": "007c91b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "007c91b4",
      "DATA",
      [
        "storage",
        "00bff0f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c91b4",
      "DATA",
      [
        "storage",
        "00bff1a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c91b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9190.md#insn-007c91b0)
- 新版 [`007c91b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9190.md#insn-007c91b0)

~~~diff
- 007c91b0 ["COPY", "tmp:0:8", ["const:f8:8"]]
- 007c91b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c91b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c91b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c91b0 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 007c91b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c91b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c91b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c91b0 bytes 08e10391
+ 007c91b0 bytes 08a10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a105f3f324a63985a31fcbb3f6bdd20a"></a>

### [`007c9254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9254.md) → [`007c9254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9254.md) FUN_007c9254

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
      "definition_site": "007c9268",
      "incomplete_value": false,
      "site": "007c926c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9268",
      "incomplete_value": false,
      "site": "007c926c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "007c926c",
      "DATA",
      [
        "storage",
        "00bff178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c926c",
      "DATA",
      [
        "storage",
        "00bff228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9254.md#insn-007c9268)
- 新版 [`007c9268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9254.md#insn-007c9268)

~~~diff
- 007c9268 ["COPY", "tmp:0:8", ["const:178:8"]]
- 007c9268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9268 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 007c9268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9268 bytes 08e10591
+ 007c9268 bytes 08a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aba09f3382c1d0bd5e86ef30bb2adde"></a>

### [`007c9304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9304.md) → [`007c9304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9304.md) FUN_007c9304

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
      "definition_site": "007c9328",
      "incomplete_value": false,
      "site": "007c9328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9328",
      "incomplete_value": false,
      "site": "007c9328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
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
      "007c9328",
      "DATA",
      [
        "storage",
        "00bff1f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9328",
      "DATA",
      [
        "storage",
        "00bff2a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9304.md#insn-007c9324)
- 新版 [`007c9324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9304.md#insn-007c9324)

~~~diff
- 007c9324 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 007c9324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9324 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 007c9324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9324 bytes 08e10791
+ 007c9324 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9d6f6d37ac74dd25e7215944ba0a97"></a>

### [`007c9410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9410.md) → [`007c9410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9410.md) FUN_007c9410

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
      "definition_site": "007c9424",
      "incomplete_value": false,
      "site": "007c9428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9424",
      "incomplete_value": false,
      "site": "007c9428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:278:8"
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
      "007c9428",
      "DATA",
      [
        "storage",
        "00bff278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9428",
      "DATA",
      [
        "storage",
        "00bff328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9410.md#insn-007c9424)
- 新版 [`007c9424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9410.md#insn-007c9424)

~~~diff
- 007c9424 ["COPY", "tmp:0:8", ["const:278:8"]]
- 007c9424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9424 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 007c9424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9424 bytes 08e10991
+ 007c9424 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70c518c039758be32fe9254de297b881"></a>

### [`007c94f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c94f0.md) → [`007c94f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c94f0.md) FUN_007c94f0

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
      "definition_site": "007c9504",
      "incomplete_value": false,
      "site": "007c9508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9504",
      "incomplete_value": false,
      "site": "007c9508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
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
      "007c9508",
      "DATA",
      [
        "storage",
        "00bff2f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9508",
      "DATA",
      [
        "storage",
        "00bff3a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c94f0.md#insn-007c9504)
- 新版 [`007c9504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c94f0.md#insn-007c9504)

~~~diff
- 007c9504 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 007c9504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9504 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 007c9504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9504 bytes 08e10b91
+ 007c9504 bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ca8473c68a66cf90b39f0445e6f06fb"></a>

### [`007c9640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9640.md) → [`007c9640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9640.md) FUN_007c9640

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
      "definition_site": "007c9654",
      "incomplete_value": false,
      "site": "007c9658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9654",
      "incomplete_value": false,
      "site": "007c9658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "007c9658",
      "DATA",
      [
        "storage",
        "00bff378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9658",
      "DATA",
      [
        "storage",
        "00bff428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9640.md#insn-007c9654)
- 新版 [`007c9654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9640.md#insn-007c9654)

~~~diff
- 007c9654 ["COPY", "tmp:0:8", ["const:378:8"]]
- 007c9654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9654 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 007c9654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9654 bytes 08e10d91
+ 007c9654 bytes 08a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73c5ea7e104ce535657b05f52407fdce"></a>

### [`007c96f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c96f0.md) → [`007c96f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c96f0.md) FUN_007c96f0

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
      "definition_site": "007c9704",
      "incomplete_value": false,
      "site": "007c9708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9704",
      "incomplete_value": false,
      "site": "007c9708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
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
      "007c9708",
      "DATA",
      [
        "storage",
        "00bff3f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9708",
      "DATA",
      [
        "storage",
        "00bff4a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c96f0.md#insn-007c9704)
- 新版 [`007c9704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c96f0.md#insn-007c9704)

~~~diff
- 007c9704 ["COPY", "tmp:0:8", ["const:3f8:8"]]
- 007c9704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9704 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 007c9704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9704 bytes 08e10f91
+ 007c9704 bytes 08a11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fedd81f565458a3dc62969abc39f99c0"></a>

### [`007c97a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c97a0.md) → [`007c97a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c97a0.md) FUN_007c97a0

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
      "definition_site": "007c97b4",
      "incomplete_value": false,
      "site": "007c97b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c97b4",
      "incomplete_value": false,
      "site": "007c97b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:478:8"
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
      "007c97b8",
      "DATA",
      [
        "storage",
        "00bff478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c97b8",
      "DATA",
      [
        "storage",
        "00bff528",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c97b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c97a0.md#insn-007c97b4)
- 新版 [`007c97b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c97a0.md#insn-007c97b4)

~~~diff
- 007c97b4 ["COPY", "tmp:0:8", ["const:478:8"]]
- 007c97b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c97b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c97b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c97b4 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 007c97b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c97b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c97b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c97b4 bytes 08e11191
+ 007c97b4 bytes 08a11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5638759f9ded18246411841b62a7c39a"></a>

### [`007c9850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9850.md) → [`007c9850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9850.md) FUN_007c9850

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
      "definition_site": "007c9874",
      "incomplete_value": false,
      "site": "007c9874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9874",
      "incomplete_value": false,
      "site": "007c9874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
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
      "007c9874",
      "DATA",
      [
        "storage",
        "00bff4f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9874",
      "DATA",
      [
        "storage",
        "00bff5a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9850.md#insn-007c9870)
- 新版 [`007c9870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9850.md#insn-007c9870)

~~~diff
- 007c9870 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 007c9870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9870 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 007c9870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9870 bytes 08e11391
+ 007c9870 bytes 08a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce729cec293230237c5ac607b5c3ccb5"></a>

### [`007c9988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9988.md) → [`007c9988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9988.md) FUN_007c9988

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
      "definition_site": "007c99a8",
      "incomplete_value": false,
      "site": "007c99ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c99a8",
      "incomplete_value": false,
      "site": "007c99ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:578:8"
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
      "007c99ac",
      "DATA",
      [
        "storage",
        "00bff578",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c99ac",
      "DATA",
      [
        "storage",
        "00bff628",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c99a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9988.md#insn-007c99a8)
- 新版 [`007c99a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9988.md#insn-007c99a8)

~~~diff
- 007c99a8 ["COPY", "tmp:0:8", ["const:578:8"]]
- 007c99a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c99a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c99a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c99a8 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 007c99a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c99a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c99a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c99a8 bytes 08e11591
+ 007c99a8 bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c53d80ac4477f21dc4054244b9b1fe70"></a>

### [`007c9abc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9abc.md) → [`007c9abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9abc.md) FUN_007c9abc

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
      "definition_site": "007c9adc",
      "incomplete_value": false,
      "site": "007c9ae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9adc",
      "incomplete_value": false,
      "site": "007c9ae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "007c9ae0",
      "DATA",
      [
        "storage",
        "00bff5f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9ae0",
      "DATA",
      [
        "storage",
        "00bff6a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9adc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9abc.md#insn-007c9adc)
- 新版 [`007c9adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9abc.md#insn-007c9adc)

~~~diff
- 007c9adc ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 007c9adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9adc ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 007c9adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9adc bytes 08e11791
+ 007c9adc bytes 08a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92abf8d2561ba00318df3d1fee69e987"></a>

### [`007c9b88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9b88.md) → [`007c9b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9b88.md) FUN_007c9b88

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
      "definition_site": "007c9ba8",
      "incomplete_value": false,
      "site": "007c9bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9ba8",
      "incomplete_value": false,
      "site": "007c9bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "007c9bac",
      "DATA",
      [
        "storage",
        "00bff678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9bac",
      "DATA",
      [
        "storage",
        "00bff728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9b88.md#insn-007c9ba8)
- 新版 [`007c9ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9b88.md#insn-007c9ba8)

~~~diff
- 007c9ba8 ["COPY", "tmp:0:8", ["const:678:8"]]
- 007c9ba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9ba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9ba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9ba8 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 007c9ba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9ba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9ba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9ba8 bytes 08e11991
+ 007c9ba8 bytes 08a11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff5bbd2ab220679b18cf9c5aa46e053c"></a>

### [`007c9c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9c54.md) → [`007c9c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9c54.md) FUN_007c9c54

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
      "definition_site": "007c9c74",
      "incomplete_value": false,
      "site": "007c9c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9c74",
      "incomplete_value": false,
      "site": "007c9c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
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
      "007c9c78",
      "DATA",
      [
        "storage",
        "00bff6f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9c78",
      "DATA",
      [
        "storage",
        "00bff7a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9c74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9c54.md#insn-007c9c74)
- 新版 [`007c9c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9c54.md#insn-007c9c74)

~~~diff
- 007c9c74 ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 007c9c74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9c74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9c74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9c74 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 007c9c74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9c74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9c74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9c74 bytes 08e11b91
+ 007c9c74 bytes 08a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18c1af7aa4a810ea98f54150ba160280"></a>

### [`007c9d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9d44.md) → [`007c9d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9d44.md) FUN_007c9d44

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
      "definition_site": "007c9d64",
      "incomplete_value": false,
      "site": "007c9d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9d64",
      "incomplete_value": false,
      "site": "007c9d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "007c9d68",
      "DATA",
      [
        "storage",
        "00bff778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9d68",
      "DATA",
      [
        "storage",
        "00bff828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9d44.md#insn-007c9d64)
- 新版 [`007c9d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9d44.md#insn-007c9d64)

~~~diff
- 007c9d64 ["COPY", "tmp:0:8", ["const:778:8"]]
- 007c9d64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9d64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9d64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9d64 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 007c9d64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9d64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9d64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9d64 bytes 08e11d91
+ 007c9d64 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81abbbf64b4720b1538b1ad861eb9507"></a>

### [`007c9e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9e34.md) → [`007c9e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9e34.md) FUN_007c9e34

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
      "definition_site": "007c9e48",
      "incomplete_value": false,
      "site": "007c9e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9e48",
      "incomplete_value": false,
      "site": "007c9e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "007c9e4c",
      "DATA",
      [
        "storage",
        "00bff7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9e4c",
      "DATA",
      [
        "storage",
        "00bff8a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9e48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9e34.md#insn-007c9e48)
- 新版 [`007c9e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9e34.md#insn-007c9e48)

~~~diff
- 007c9e48 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 007c9e48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9e48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9e48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9e48 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 007c9e48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9e48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9e48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9e48 bytes 08e11f91
+ 007c9e48 bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a87b3aebe7c65cc23d1a414fe5cd2ad"></a>

### [`007c9ee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9ee4.md) → [`007c9ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9ee4.md) FUN_007c9ee4

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
      "definition_site": "007c9f08",
      "incomplete_value": false,
      "site": "007c9f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9f08",
      "incomplete_value": false,
      "site": "007c9f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:878:8"
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
      "007c9f0c",
      "DATA",
      [
        "storage",
        "00bff878",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007c9f0c",
      "DATA",
      [
        "storage",
        "00bff928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9f08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007c9/007c9ee4.md#insn-007c9f08)
- 新版 [`007c9f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007c9/007c9ee4.md#insn-007c9f08)

~~~diff
- 007c9f08 ["COPY", "tmp:0:8", ["const:878:8"]]
- 007c9f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c9f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c9f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c9f08 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 007c9f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c9f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c9f08 bytes 08e12191
+ 007c9f08 bytes 08a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18fc28ef6de39ede9a068265318b9898"></a>

### [`007ca0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca0e4.md) → [`007ca0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca0e4.md) FUN_007ca0e4

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
      "definition_site": "007ca104",
      "incomplete_value": false,
      "site": "007ca108",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca104",
      "incomplete_value": false,
      "site": "007ca108",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "007ca108",
      "DATA",
      [
        "storage",
        "00bff8f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ca108",
      "DATA",
      [
        "storage",
        "00bff9a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca0e4.md#insn-007ca104)
- 新版 [`007ca104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca0e4.md#insn-007ca104)

~~~diff
- 007ca104 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 007ca104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ca104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ca104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ca104 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 007ca104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ca104 bytes 08e12391
+ 007ca104 bytes 08a12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6b7eb597d164b24915047fcf80a3b9b"></a>

### [`007ca13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca13c.md) → [`007ca13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca13c.md) FUN_007ca13c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00459f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459f50.md) [`007ca3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca3a8.md) [`007ca3ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca3ac.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00459f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459f50.md) [`007ca3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca3a8.md) [`007ca3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca3ac.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ca1e4",
      "incomplete_value": false,
      "site": "007ca1e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca1e4",
      "incomplete_value": false,
      "site": "007ca1e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "definition_site": "007ca234",
      "incomplete_value": true,
      "site": "007ca234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dfa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca234",
      "incomplete_value": true,
      "site": "007ca234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e8e:8"
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
      "007ca1e4",
      "DATA",
      [
        "storage",
        "00bff968",
        null,
        "undefined *"
      ]
    ],
    [
      "007ca224",
      "READ",
      [
        "storage",
        "002ade8e",
        null,
        "string"
      ]
    ],
    [
      "007ca280",
      "READ",
      [
        "storage",
        "00bff988",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007ca1e4",
      "DATA",
      [
        "storage",
        "00bffa18",
        null,
        "undefined *"
      ]
    ],
    [
      "007ca224",
      "READ",
      [
        "storage",
        "002addfa",
        null,
        "string"
      ]
    ],
    [
      "007ca280",
      "READ",
      [
        "storage",
        "00bffa38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca13c.md#insn-007ca1dc) · [`007ca21c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca13c.md#insn-007ca21c)
- 新版 [`007ca1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca13c.md#insn-007ca1dc) · [`007ca21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca13c.md#insn-007ca21c)

~~~diff
- 007ca1dc ["COPY", "tmp:0:8", ["const:968:8"]]
- 007ca1dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ca1dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ca1dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ca1dc ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 007ca1dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ca1dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ca1dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ca1dc bytes 29a12591
+ 007ca1dc bytes 29612891
- 007ca21c ["COPY", "tmp:0:8", ["const:e8e:8"]]
- 007ca21c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007ca21c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007ca21c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007ca21c ["COPY", "tmp:0:8", ["const:dfa:8"]]
+ 007ca21c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007ca21c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007ca21c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007ca21c bytes 29393a91
+ 007ca21c bytes 29e93791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32ddc4239ba582433ce2407f20647b9e"></a>

### [`007ca358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca358.md) → [`007ca358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca358.md) FUN_007ca358

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
      "definition_site": "007ca378",
      "incomplete_value": false,
      "site": "007ca37c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca378",
      "incomplete_value": false,
      "site": "007ca37c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "007ca37c",
      "DATA",
      [
        "storage",
        "00bff968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ca37c",
      "DATA",
      [
        "storage",
        "00bffa18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca358.md#insn-007ca378)
- 新版 [`007ca378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca358.md#insn-007ca378)

~~~diff
- 007ca378 ["COPY", "tmp:0:8", ["const:968:8"]]
- 007ca378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ca378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ca378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ca378 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 007ca378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ca378 bytes 08a12591
+ 007ca378 bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9526b73cdee032d39ed0b7665ed87518"></a>

### [`007ca390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca390.md) → [`007ca390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca390.md) FUN_007ca390

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
      "definition_site": "007ca394",
      "incomplete_value": false,
      "site": "007ca398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca394",
      "incomplete_value": false,
      "site": "007ca398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bff000:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "007ca398",
      "DATA",
      [
        "storage",
        "00bff968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007ca398",
      "DATA",
      [
        "storage",
        "00bffa18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007ca/007ca390.md#insn-007ca394)
- 新版 [`007ca394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ca/007ca390.md#insn-007ca394)

~~~diff
- 007ca394 ["COPY", "tmp:0:8", ["const:968:8"]]
- 007ca394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ca394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ca394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ca394 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 007ca394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ca394 bytes 08a12591
+ 007ca394 bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

