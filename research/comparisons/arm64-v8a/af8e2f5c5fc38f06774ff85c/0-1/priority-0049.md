# v15.7.2 → v15.7.3 · 最優先の変更候補 (49)

[一覧の目次](README.md)

<a id="compare-6707110e704f55da8e0e3c6fb13e2cb5"></a>

### [`0096d6b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d6b8.md) → [`0096d6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d6b8.md) FUN_0096d6b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00666298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00666/00666298.md) [`006a8e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006a8/006a8e60.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00666298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00666/00666298.md) [`006a8e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8e60.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.39% / 新版 97.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096d7c0",
      "incomplete_value": true,
      "site": "0096d7d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0096d7c0",
      "incomplete_value": true,
      "site": "0096d7d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096d7bc",
      "incomplete_value": false,
      "site": "0096d7d4",
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
      "definition_site": "0096d7bc",
      "incomplete_value": false,
      "site": "0096d7d4",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096d7c8",
      "incomplete_value": false,
      "site": "0096d7d4",
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
      "definition_site": "0096d7c8",
      "incomplete_value": false,
      "site": "0096d7d4",
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
      "0096d7bc",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0096d7c0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0096d7c8",
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
      "0096d7bc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0096d7c0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0096d7c8",
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

- 旧版 [`0096d7bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d6b8.md#insn-0096d7bc) · [`0096d7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d6b8.md#insn-0096d7c0) · [`0096d7c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d6b8.md#insn-0096d7c8)
- 新版 `0096d7bc`（命令位置の公開資料なし） · `0096d7c0`（命令位置の公開資料なし） · `0096d7c8`（命令位置の公開資料なし）

~~~diff
- 0096d7bc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 0096d7bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0096d7bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0096d7bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0096d7bc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0096d7bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0096d7bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0096d7bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0096d7bc bytes 21603691
+ 0096d7bc bytes 21203991
- 0096d7c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 0096d7c0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0096d7c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0096d7c0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0096d7c0 bytes 00dd44f9
+ 0096d7c0 bytes 003d45f9
- 0096d7c8 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0096d7c8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0096d7c8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0096d7c8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0096d7c8 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0096d7c8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0096d7c8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0096d7c8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0096d7c8 bytes 42603291
+ 0096d7c8 bytes 42203591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad7cfe91e499b4a10be477b21c03d8d3"></a>

### [`0096d8d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d8d4.md) → [`0096d8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d8d4.md) FUN_0096d8d4

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
      "definition_site": "0096d8f4",
      "incomplete_value": false,
      "site": "0096d8f8",
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
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096d8f4",
      "incomplete_value": false,
      "site": "0096d8f8",
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
            "const:e38:8"
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
      "0096d8f8",
      "DATA",
      [
        "storage",
        "00c09e38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096d8f8",
      "DATA",
      [
        "storage",
        "00c09ee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096d8f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d8d4.md#insn-0096d8f4)
- 新版 `0096d8f4`（命令位置の公開資料なし）

~~~diff
- 0096d8f4 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 0096d8f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096d8f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096d8f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096d8f4 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0096d8f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d8f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096d8f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096d8f4 bytes 08e13891
+ 0096d8f4 bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f85d254fe0b341eae0edb2707e00f8df"></a>

### [`0096da04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096da04.md) → [`0096da04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096da04.md) FUN_0096da04

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
      "definition_site": "0096da28",
      "incomplete_value": false,
      "site": "0096da28",
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
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096da28",
      "incomplete_value": false,
      "site": "0096da28",
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
            "const:eb8:8"
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
      "0096da28",
      "DATA",
      [
        "storage",
        "00c09eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096da28",
      "DATA",
      [
        "storage",
        "00c09f68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096da24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096da04.md#insn-0096da24)
- 新版 `0096da24`（命令位置の公開資料なし）

~~~diff
- 0096da24 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 0096da24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096da24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096da24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096da24 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 0096da24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096da24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096da24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096da24 bytes 08e13a91
+ 0096da24 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04a030c2aa66c2f9c9bc916dbee9d9c7"></a>

### [`0096dc00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dc00.md) → [`0096dc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dc00.md) FUN_0096dc00

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
      "definition_site": "0096dc24",
      "incomplete_value": false,
      "site": "0096dc24",
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
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096dc24",
      "incomplete_value": false,
      "site": "0096dc24",
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
            "const:f38:8"
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
      "0096dc24",
      "DATA",
      [
        "storage",
        "00c09f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096dc24",
      "DATA",
      [
        "storage",
        "00c09fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096dc20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dc00.md#insn-0096dc20)
- 新版 `0096dc20`（命令位置の公開資料なし）

~~~diff
- 0096dc20 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0096dc20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096dc20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096dc20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096dc20 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 0096dc20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dc20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dc20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096dc20 bytes 08e13c91
+ 0096dc20 bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b7f5e42b34d8cafb9793912c65a2249"></a>

### [`0096dc34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dc34.md) → [`0096dc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dc34.md) FUN_0096dc34

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
      "definition_site": "0096dc40",
      "incomplete_value": false,
      "site": "0096dc40",
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
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096dc40",
      "incomplete_value": false,
      "site": "0096dc40",
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
            "const:f38:8"
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
      "0096dc40",
      "DATA",
      [
        "storage",
        "00c09f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096dc40",
      "DATA",
      [
        "storage",
        "00c09fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096dc3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dc34.md#insn-0096dc3c)
- 新版 `0096dc3c`（命令位置の公開資料なし）

~~~diff
- 0096dc3c ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0096dc3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0096dc3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0096dc3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0096dc3c ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 0096dc3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0096dc3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0096dc3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0096dc3c bytes 29e13c91
+ 0096dc3c bytes 29a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e56079fa73f7be0ea2038802844f77a5"></a>

### [`0096dcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dcd8.md) → [`0096dcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dcd8.md) FUN_0096dcd8

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
      "definition_site": "0096dcfc",
      "incomplete_value": false,
      "site": "0096dcfc",
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
      "definition_site": "0096dcfc",
      "incomplete_value": false,
      "site": "0096dcfc",
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
      "0096dcfc",
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
      "0096dcfc",
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

- 旧版 [`0096dcf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dcd8.md#insn-0096dcf4) · [`0096dcf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dcd8.md#insn-0096dcf8)
- 新版 `0096dcf4`（命令位置の公開資料なし） · `0096dcf8`（命令位置の公開資料なし）

~~~diff
- 0096dcf4 ["COPY", "register:4040:8", ["const:c09000:8"]]
+ 0096dcf4 ["COPY", "register:4040:8", ["const:c0a000:8"]]
- 0096dcf4 bytes e8140090
+ 0096dcf4 bytes e81400b0
- 0096dcf8 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0096dcf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096dcf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096dcf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096dcf8 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 0096dcf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dcf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dcf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096dcf8 bytes 08e13e91
+ 0096dcf8 bytes 08a10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd12243371da503746d77cc1a830e0af"></a>

### [`0096dd0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dd0c.md) → [`0096dd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dd0c.md) FUN_0096dd0c

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
      "definition_site": "0096dd18",
      "incomplete_value": true,
      "site": "0096dd18",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096dd18",
      "incomplete_value": true,
      "site": "0096dd18",
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
            "const:fb8:8"
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
      "0096dd18",
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
      "0096dd18",
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

- 旧版 [`0096dd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dd0c.md#insn-0096dd10) · [`0096dd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dd0c.md#insn-0096dd14)
- 新版 `0096dd10`（命令位置の公開資料なし） · `0096dd14`（命令位置の公開資料なし）

~~~diff
- 0096dd10 ["COPY", "register:4048:8", ["const:c09000:8"]]
+ 0096dd10 ["COPY", "register:4048:8", ["const:c0a000:8"]]
- 0096dd10 bytes e9140090
+ 0096dd10 bytes e91400b0
- 0096dd14 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0096dd14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0096dd14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0096dd14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0096dd14 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 0096dd14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0096dd14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0096dd14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0096dd14 bytes 29e13e91
+ 0096dd14 bytes 29a10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-512094243de48cff972d0aafc1815cb1"></a>

### [`0096ddb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096ddb4.md) → [`0096ddb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096ddb4.md) FUN_0096ddb4

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
      "definition_site": "0096ddd8",
      "incomplete_value": false,
      "site": "0096ddd8",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096ddd8",
      "incomplete_value": false,
      "site": "0096ddd8",
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
            "const:38:8"
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
      "0096ddd8",
      "DATA",
      [
        "storage",
        "00c0a038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096ddd8",
      "DATA",
      [
        "storage",
        "00c0a0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096ddd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096ddb4.md#insn-0096ddd4)
- 新版 `0096ddd4`（命令位置の公開資料なし）

~~~diff
- 0096ddd4 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0096ddd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096ddd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096ddd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096ddd4 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 0096ddd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096ddd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096ddd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096ddd4 bytes 08e10091
+ 0096ddd4 bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de43e27b00c37ab45767dec81ec7c05d"></a>

### [`0096dde8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dde8.md) → [`0096dde8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dde8.md) FUN_0096dde8

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
      "definition_site": "0096ddf4",
      "incomplete_value": false,
      "site": "0096ddf4",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096ddf4",
      "incomplete_value": false,
      "site": "0096ddf4",
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
      "0096ddf4",
      "DATA",
      [
        "storage",
        "00c0a038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096ddf4",
      "DATA",
      [
        "storage",
        "00c0a0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096ddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dde8.md#insn-0096ddf0)
- 新版 `0096ddf0`（命令位置の公開資料なし）

~~~diff
- 0096ddf0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0096ddf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0096ddf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0096ddf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0096ddf0 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 0096ddf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0096ddf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0096ddf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0096ddf0 bytes 29e10091
+ 0096ddf0 bytes 29a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88cfaae78ac0d7e71530bcff307294db"></a>

### [`0096de48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096de48.md) → [`0096de48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096de48.md) FUN_0096de48

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
      "definition_site": "0096de5c",
      "incomplete_value": false,
      "site": "0096de60",
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
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096de5c",
      "incomplete_value": false,
      "site": "0096de60",
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
            "const:b8:8"
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
      "0096de60",
      "DATA",
      [
        "storage",
        "00c0a0b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096de60",
      "DATA",
      [
        "storage",
        "00c0a168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096de5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096de48.md#insn-0096de5c)
- 新版 `0096de5c`（命令位置の公開資料なし）

~~~diff
- 0096de5c ["COPY", "tmp:0:8", ["const:b8:8"]]
- 0096de5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096de5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096de5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096de5c ["COPY", "tmp:0:8", ["const:168:8"]]
+ 0096de5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096de5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096de5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096de5c bytes 08e10291
+ 0096de5c bytes 08a10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7eb8104aac430818821b5bb0a720e5"></a>

### [`0096de6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096de6c.md) → [`0096de6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096de6c.md) FUN_0096de6c

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
      "definition_site": "0096de70",
      "incomplete_value": false,
      "site": "0096de74",
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
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096de70",
      "incomplete_value": false,
      "site": "0096de74",
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
            "const:b8:8"
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
      "0096de74",
      "DATA",
      [
        "storage",
        "00c0a0b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096de74",
      "DATA",
      [
        "storage",
        "00c0a168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096de70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096de6c.md#insn-0096de70)
- 新版 `0096de70`（命令位置の公開資料なし）

~~~diff
- 0096de70 ["COPY", "tmp:0:8", ["const:b8:8"]]
- 0096de70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096de70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096de70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096de70 ["COPY", "tmp:0:8", ["const:168:8"]]
+ 0096de70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096de70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096de70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096de70 bytes 08e10291
+ 0096de70 bytes 08a10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dc058b64992c256c2bca1340c3bd64e"></a>

### [`0096df1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096df1c.md) → [`0096df1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096df1c.md) FUN_0096df1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0096df20",
      "incomplete_value": true,
      "site": "0096df24",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096df20",
      "incomplete_value": true,
      "site": "0096df24",
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
      "0096df24",
      "DATA",
      [
        "storage",
        "00c0a138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096df24",
      "DATA",
      [
        "storage",
        "00c0a1e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096df20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096df1c.md#insn-0096df20)
- 新版 `0096df20`（命令位置の公開資料なし）

~~~diff
- 0096df20 ["COPY", "tmp:0:8", ["const:138:8"]]
- 0096df20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096df20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096df20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096df20 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 0096df20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096df20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096df20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096df20 bytes 08e10491
+ 0096df20 bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4879b6a4b867cef2f2b2a7f1b841f6e1"></a>

### [`0096dfa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dfa8.md) → [`0096dfa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dfa8.md) FUN_0096dfa8

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
      "definition_site": "0096dfbc",
      "incomplete_value": false,
      "site": "0096dfc0",
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
      "definition_site": "0096dfbc",
      "incomplete_value": false,
      "site": "0096dfc0",
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
      "0096dfc0",
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
      "0096dfc0",
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

- 旧版 [`0096dfbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dfa8.md#insn-0096dfbc)
- 新版 `0096dfbc`（命令位置の公開資料なし）

~~~diff
- 0096dfbc ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 0096dfbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096dfbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096dfbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096dfbc ["COPY", "tmp:0:8", ["const:268:8"]]
+ 0096dfbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dfbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dfbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096dfbc bytes 08e10691
+ 0096dfbc bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f128d848bfcae86a18b71451558cdd8d"></a>

### [`0096dfcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dfcc.md) → [`0096dfcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dfcc.md) FUN_0096dfcc

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
      "definition_site": "0096dfd0",
      "incomplete_value": false,
      "site": "0096dfd4",
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
      "definition_site": "0096dfd0",
      "incomplete_value": false,
      "site": "0096dfd4",
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
      "0096dfd4",
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
      "0096dfd4",
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

- 旧版 [`0096dfd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dfcc.md#insn-0096dfd0)
- 新版 `0096dfd0`（命令位置の公開資料なし）

~~~diff
- 0096dfd0 ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 0096dfd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096dfd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096dfd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096dfd0 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 0096dfd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dfd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096dfd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096dfd0 bytes 08e10691
+ 0096dfd0 bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c31d5542c55981c81605ee52d8973e7e"></a>

### [`0096e054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096e/0096e054.md) → [`0096e054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096e/0096e054.md) _INIT_186

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
      "definition_site": "0096e0b4",
      "incomplete_value": true,
      "site": "0096e0d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096e0b4",
      "incomplete_value": true,
      "site": "0096e0d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096e150",
      "incomplete_value": true,
      "site": "0096e194",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096e150",
      "incomplete_value": true,
      "site": "0096e194",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096e27c",
      "incomplete_value": false,
      "site": "0096e288",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096e27c",
      "incomplete_value": false,
      "site": "0096e288",
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
            "const:810:8"
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
      "0096e090",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0096e0b4",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0096e0d4",
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
      "0096e090",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0096e0b4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0096e0d4",
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

- 旧版 [`0096e080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096e/0096e054.md#insn-0096e080) · [`0096e088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096e/0096e054.md#insn-0096e088)
- 新版 `0096e080`（命令位置の公開資料なし） · `0096e088`（命令位置の公開資料なし）

~~~diff
- 0096e080 ["COPY", "tmp:0:8", ["const:810:8"]]
- 0096e080 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0096e080 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0096e080 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0096e080 ["COPY", "tmp:0:8", ["const:8d0:8"]]
+ 0096e080 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0096e080 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0096e080 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0096e080 bytes 73422091
+ 0096e080 bytes 73422391
- 0096e088 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0096e088 bytes c9c9ffb0
+ 0096e088 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0096e088 bytes c9c9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fa77535032e7a3576ef5b4780f07da6"></a>

### [`0096eab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096e/0096eab4.md) → [`0096eab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096e/0096eab4.md) _INIT_187

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0096eaf0",
      "incomplete_value": true,
      "site": "0096eb0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eaf0",
      "incomplete_value": true,
      "site": "0096eb0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eb14",
      "incomplete_value": true,
      "site": "0096eb30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eb14",
      "incomplete_value": true,
      "site": "0096eb30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eb34",
      "incomplete_value": true,
      "site": "0096eb50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eb34",
      "incomplete_value": true,
      "site": "0096eb50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0096eaf0",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0096eb14",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0096eb34",
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
      "0096eaf0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0096eb14",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0096eb34",
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

- 旧版 [`0096eae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096e/0096eab4.md#insn-0096eae0) · [`0096eae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096e/0096eab4.md#insn-0096eae8)
- 新版 `0096eae0`（命令位置の公開資料なし） · `0096eae8`（命令位置の公開資料なし）

~~~diff
- 0096eae0 ["COPY", "tmp:0:8", ["const:828:8"]]
- 0096eae0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0096eae0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0096eae0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0096eae0 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 0096eae0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0096eae0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0096eae0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0096eae0 bytes 73a22091
+ 0096eae0 bytes 73a22391
- 0096eae8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0096eae8 bytes c9c9ffb0
+ 0096eae8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0096eae8 bytes c9c9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a670eaa11bb8b6c2f954a658a894c80"></a>

### [`0096ee44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096e/0096ee44.md) → [`0096ee44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096e/0096ee44.md) _INIT_188

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0096ee80",
      "incomplete_value": true,
      "site": "0096ee9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096ee80",
      "incomplete_value": true,
      "site": "0096ee9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eea4",
      "incomplete_value": true,
      "site": "0096eec0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eea4",
      "incomplete_value": true,
      "site": "0096eec0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eec4",
      "incomplete_value": true,
      "site": "0096eee0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0096eec4",
      "incomplete_value": true,
      "site": "0096eee0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0096ee80",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0096eea4",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0096eec4",
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
      "0096ee80",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0096eea4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0096eec4",
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

- 旧版 [`0096ee70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096e/0096ee44.md#insn-0096ee70) · [`0096ee78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096e/0096ee44.md#insn-0096ee78)
- 新版 `0096ee70`（命令位置の公開資料なし） · `0096ee78`（命令位置の公開資料なし）

~~~diff
- 0096ee70 ["COPY", "tmp:0:8", ["const:840:8"]]
- 0096ee70 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0096ee70 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0096ee70 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0096ee70 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 0096ee70 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0096ee70 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0096ee70 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0096ee70 bytes 73022191
+ 0096ee70 bytes 73022491
- 0096ee78 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0096ee78 bytes c9c9ffb0
+ 0096ee78 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0096ee78 bytes c9c9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4085ec757e13775f6b1f0f8ea8f62130"></a>

### [`0096f1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f1dc.md) → [`0096f1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f1dc.md) FUN_0096f1dc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00868b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868b14.md) · 呼出先 1件 [`0046b1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b1e0.md)
- 新版 呼出元 1件 [`00868b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md) · 呼出先 1件 [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096f1ec",
      "incomplete_value": false,
      "site": "0096f1f4",
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
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096f1ec",
      "incomplete_value": false,
      "site": "0096f1f4",
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
      "0096f1ec",
      "PARAM",
      [
        "storage",
        "0109e870",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0096f1ec",
      "PARAM",
      [
        "storage",
        "0109e930",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096f1ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f1dc.md#insn-0096f1ec)
- 新版 `0096f1ec`（命令位置の公開資料なし）

~~~diff
- 0096f1ec ["COPY", "tmp:0:8", ["const:870:8"]]
- 0096f1ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0096f1ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0096f1ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0096f1ec ["COPY", "tmp:0:8", ["const:930:8"]]
+ 0096f1ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0096f1ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0096f1ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0096f1ec bytes 21c02191
+ 0096f1ec bytes 21c02491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f29747b9e4675d99df557029dfb98bf"></a>

### [`0096f208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f208.md) → [`0096f208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f208.md) FUN_0096f208

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00868b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868b14.md) · 呼出先 1件 [`0046b1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b1e0.md)
- 新版 呼出元 1件 [`00868b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md) · 呼出先 1件 [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0096f218",
      "incomplete_value": false,
      "site": "0096f220",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096f218",
      "incomplete_value": false,
      "site": "0096f220",
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
            "const:890:8"
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
      "0096f218",
      "PARAM",
      [
        "storage",
        "0109e890",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0096f218",
      "PARAM",
      [
        "storage",
        "0109e950",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096f218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f208.md#insn-0096f218)
- 新版 `0096f218`（命令位置の公開資料なし）

~~~diff
- 0096f218 ["COPY", "tmp:0:8", ["const:890:8"]]
- 0096f218 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0096f218 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0096f218 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0096f218 ["COPY", "tmp:0:8", ["const:950:8"]]
+ 0096f218 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0096f218 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0096f218 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0096f218 bytes 21402291
+ 0096f218 bytes 21402591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c2890b3e819e68aaf1d5c52c67ebfb8"></a>

### [`0096f234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f234.md) → [`0096f234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f234.md) FUN_0096f234

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00868b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868b14.md) · 呼出先 12件 [`0046b2bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b2bc.md) [`00470da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470da0.md) [`00470da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470da8.md) [`00470e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470e10.md) [`0096f440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f440.md)
- 新版 呼出元 1件 [`00868b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md) · 呼出先 12件 [`0046b2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b2bc.md) [`00470da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470da0.md) [`00470da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470da8.md) [`00470e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470e10.md) [`0096f440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0096f2d8",
      "incomplete_value": false,
      "site": "0096f2dc",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096f2d8",
      "incomplete_value": false,
      "site": "0096f2dc",
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
            "const:2c8:8"
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
      "0096f2c0",
      "DATA",
      [
        "storage",
        "00c0a238",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f2dc",
      "DATA",
      [
        "storage",
        "00c0a2c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f314",
      "READ",
      [
        "storage",
        "00c0a2e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0096f2c0",
      "DATA",
      [
        "storage",
        "00c0a2e8",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f2dc",
      "DATA",
      [
        "storage",
        "00c0a378",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f314",
      "READ",
      [
        "storage",
        "00c0a398",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096f2b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f234.md#insn-0096f2b8) · [`0096f2d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f234.md#insn-0096f2d8)
- 新版 `0096f2b8`（命令位置の公開資料なし） · `0096f2d8`（命令位置の公開資料なし）

~~~diff
- 0096f2b8 ["COPY", "tmp:0:8", ["const:238:8"]]
- 0096f2b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096f2b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096f2b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096f2b8 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 0096f2b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f2b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f2b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096f2b8 bytes 08e10891
+ 0096f2b8 bytes 08a10b91
- 0096f2d8 ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 0096f2d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096f2d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096f2d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096f2d8 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 0096f2d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f2d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f2d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096f2d8 bytes 08210b91
+ 0096f2d8 bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82e76c1e3ddca4eac02ccccba7a42d53"></a>

### [`0096f440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f440.md) → [`0096f440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f440.md) FUN_0096f440

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0096f234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f234.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/00576268.md) [`00582d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00582/00582d1c.md) [`0076b910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0076b/0076b948.md)
- 新版 呼出元 1件 [`0096f234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f234.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`00582d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00582/00582d1c.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b948.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.01% / 新版 98.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0096f4b0",
      "incomplete_value": false,
      "site": "0096f4b4",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0096f4b0",
      "incomplete_value": false,
      "site": "0096f4b4",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "0096f4b4",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f584",
      "DATA",
      [
        "storage",
        "00c0a458",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f638",
      "READ",
      [
        "storage",
        "00c0a480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096f4b4",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f584",
      "DATA",
      [
        "storage",
        "00c0a508",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f638",
      "READ",
      [
        "storage",
        "00c0a530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096f4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f440.md#insn-0096f4a8) · [`0096f57c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f440.md#insn-0096f57c)
- 新版 `0096f4a8`（命令位置の公開資料なし） · `0096f57c`（命令位置の公開資料なし）

~~~diff
- 0096f4a8 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0096f4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096f4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096f4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096f4a8 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0096f4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096f4a8 bytes 08412591
+ 0096f4a8 bytes 08012891
- 0096f57c ["COPY", "tmp:0:8", ["const:458:8"]]
- 0096f57c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096f57c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096f57c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096f57c ["COPY", "tmp:0:8", ["const:508:8"]]
+ 0096f57c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f57c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f57c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096f57c bytes 08611191
+ 0096f57c bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f306148ce81c4c7a707dadb4708ff6b"></a>

### [`0096f888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f888.md) → [`0096f888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f888.md) FUN_0096f888

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00868b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868b14.md) · 呼出先 12件 [`0046b2bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b2bc.md) [`00470da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470da0.md) [`00470da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470da8.md) [`00470e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470e10.md) [`0096fb34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096fb34.md)
- 新版 呼出元 1件 [`00868b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868b14.md) · 呼出先 12件 [`0046b2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b2bc.md) [`00470da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470da0.md) [`00470da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470da8.md) [`00470e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470e10.md) [`0096fb34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096fb34.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.58% / 新版 96.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0096f97c",
      "incomplete_value": false,
      "site": "0096f97c",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096f97c",
      "incomplete_value": false,
      "site": "0096f97c",
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
            "const:348:8"
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
      "definition_site": "0096f998",
      "incomplete_value": false,
      "site": "0096f99c",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096f998",
      "incomplete_value": false,
      "site": "0096f99c",
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
            "const:3d8:8"
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
      "0096f97c",
      "DATA",
      [
        "storage",
        "00c0a348",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f99c",
      "DATA",
      [
        "storage",
        "00c0a3d8",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f9d4",
      "READ",
      [
        "storage",
        "00c0a3f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0096f97c",
      "DATA",
      [
        "storage",
        "00c0a3f8",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f99c",
      "DATA",
      [
        "storage",
        "00c0a488",
        null,
        "undefined *"
      ]
    ],
    [
      "0096f9d4",
      "READ",
      [
        "storage",
        "00c0a4a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096f974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f888.md#insn-0096f974) · [`0096f998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f888.md#insn-0096f998)
- 新版 `0096f974`（命令位置の公開資料なし） · `0096f998`（命令位置の公開資料なし）

~~~diff
- 0096f974 ["COPY", "tmp:0:8", ["const:348:8"]]
- 0096f974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096f974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096f974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096f974 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 0096f974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096f974 bytes 08210d91
+ 0096f974 bytes 08e10f91
- 0096f998 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 0096f998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096f998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096f998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096f998 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 0096f998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096f998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096f998 bytes 08610f91
+ 0096f998 bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9be9f69026e3f817afd986b085749f3"></a>

### [`0096fb34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096fb34.md) → [`0096fb34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096fb34.md) FUN_0096fb34

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0096f888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f888.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/00576268.md) [`00583d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00583/00583d20.md) [`0076b910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0076b/0076b948.md)
- 新版 呼出元 1件 [`0096f888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f888.md) · 呼出先 13件 [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`00583d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00583/00583d20.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md) [`0076b948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b948.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.54% / 新版 97.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0096fbac",
      "incomplete_value": false,
      "site": "0096fbb0",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0096fbac",
      "incomplete_value": false,
      "site": "0096fbb0",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0096fc80",
      "incomplete_value": false,
      "site": "0096fc80",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096fc80",
      "incomplete_value": false,
      "site": "0096fc80",
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
            "const:4d8:8"
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
      "0096fbb0",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ],
    [
      "0096fc80",
      "DATA",
      [
        "storage",
        "00c0a4d8",
        null,
        "undefined *"
      ]
    ],
    [
      "0096fd34",
      "READ",
      [
        "storage",
        "00c0a500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0096fbb0",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0096fc80",
      "DATA",
      [
        "storage",
        "00c0a588",
        null,
        "undefined *"
      ]
    ],
    [
      "0096fd34",
      "READ",
      [
        "storage",
        "00c0a5b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096fba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096fb34.md#insn-0096fba4) · [`0096fc78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096fb34.md#insn-0096fc78)
- 新版 `0096fba4`（命令位置の公開資料なし） · `0096fc78`（命令位置の公開資料なし）

~~~diff
- 0096fba4 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0096fba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096fba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096fba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096fba4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0096fba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096fba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096fba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096fba4 bytes 08412591
+ 0096fba4 bytes 08012891
- 0096fc78 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 0096fc78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0096fc78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0096fc78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0096fc78 ["COPY", "tmp:0:8", ["const:588:8"]]
+ 0096fc78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0096fc78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0096fc78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0096fc78 bytes 08611391
+ 0096fc78 bytes 08211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-173b010707a940f451eefc76fcd73044"></a>

### [`0096ff84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096ff84.md) → [`0096ff84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096ff84.md) FUN_0096ff84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00970720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/00970720.md) [`0097107c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/0097107c.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004512c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00451/004512c0.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fdf4.md) [`0071edcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0071e/0071edcc.md)
- 新版 呼出元 2件 [`00970720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970720.md) [`0097107c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/0097107c.md) · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004512c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00451/004512c0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046fdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fdf4.md) [`0071edcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071e/0071edcc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.51% / 新版 95.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097023c",
      "incomplete_value": true,
      "site": "0097023c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:987:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097023c",
      "incomplete_value": true,
      "site": "0097023c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:98e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00970240",
      "incomplete_value": true,
      "site": "00970240",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00970240",
      "incomplete_value": true,
      "site": "00970240",
      "value": [
        "LOAD",
        "8",
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
      "0096ffd4",
      "READ",
      [
        "storage",
        "002a9ce4",
        null,
        "string"
      ]
    ],
    [
      "0097014c",
      "PARAM",
      [
        "storage",
        "00299ab6",
        null,
        null
      ]
    ],
    [
      "00970184",
      "READ",
      [
        "storage",
        "0029eb34",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0096ffd4",
      "READ",
      [
        "storage",
        "002a9cdb",
        null,
        "string"
      ]
    ],
    [
      "0097014c",
      "PARAM",
      [
        "storage",
        "00299b43",
        null,
        null
      ]
    ],
    [
      "00970184",
      "READ",
      [
        "storage",
        "0029ebc1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0096ffd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096ff84.md#insn-0096ffd0) · [`00970048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096ff84.md#insn-00970048) · [`00970180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096ff84.md#insn-00970180)
- 新版 `0096ffd0`（命令位置の公開資料なし） · `00970048`（命令位置の公開資料なし） · `00970180`（命令位置の公開資料なし）

~~~diff
- 0096ffd0 ["COPY", "tmp:0:8", ["const:ce4:8"]]
- 0096ffd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0096ffd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0096ffd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0096ffd0 ["COPY", "tmp:0:8", ["const:cdb:8"]]
+ 0096ffd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0096ffd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0096ffd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0096ffd0 bytes 29913391
+ 0096ffd0 bytes 296d3391
- 00970048 ["COPY", "tmp:0:8", ["const:ab6:8"]]
- 00970048 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00970048 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00970048 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00970048 ["COPY", "tmp:0:8", ["const:b43:8"]]
+ 00970048 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00970048 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00970048 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00970048 bytes d6da2a91
+ 00970048 bytes d60e2d91
- 00970180 ["COPY", "tmp:0:8", ["const:b34:8"]]
- 00970180 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00970180 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00970180 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00970180 ["COPY", "tmp:0:8", ["const:bc1:8"]]
+ 00970180 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00970180 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00970180 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00970180 bytes 4ad12c91
+ 00970180 bytes 4a052f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa2112bb13e3f2f0a26c86419c6e8676"></a>

### [`009706c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/009706c8.md) → [`009706c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/009706c8.md) FUN_009706c8

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
      "definition_site": "009706e8",
      "incomplete_value": false,
      "site": "009706ec",
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
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009706e8",
      "incomplete_value": false,
      "site": "009706ec",
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
            "const:238:8"
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
      "009706ec",
      "DATA",
      [
        "storage",
        "00c0a238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009706ec",
      "DATA",
      [
        "storage",
        "00c0a2e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009706e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/009706c8.md#insn-009706e8)
- 新版 `009706e8`（命令位置の公開資料なし）

~~~diff
- 009706e8 ["COPY", "tmp:0:8", ["const:238:8"]]
- 009706e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009706e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009706e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009706e8 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 009706e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009706e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009706e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009706e8 bytes 08e10891
+ 009706e8 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-736c0b470cd651cd5f70c39cc3f7e994"></a>

### [`00970700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/00970700.md) → [`00970700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970700.md) FUN_00970700

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
      "definition_site": "00970708",
      "incomplete_value": false,
      "site": "0097070c",
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
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00970708",
      "incomplete_value": false,
      "site": "0097070c",
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
            "const:238:8"
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
      "0097070c",
      "DATA",
      [
        "storage",
        "00c0a238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097070c",
      "DATA",
      [
        "storage",
        "00c0a2e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00970708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/00970700.md#insn-00970708)
- 新版 `00970708`（命令位置の公開資料なし）

~~~diff
- 00970708 ["COPY", "tmp:0:8", ["const:238:8"]]
- 00970708 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00970708 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00970708 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00970708 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00970708 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00970708 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00970708 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00970708 bytes 29e10891
+ 00970708 bytes 29a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45d3525cb556190d4125a7dbe0834ef6"></a>

### [`00970d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/00970d64.md) → [`00970d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970d64.md) FUN_00970d64

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00970c1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/00970c1c.md) [`00970dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/00970dcc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00970c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970c1c.md) [`00970dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970dcc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00970d70",
      "incomplete_value": false,
      "site": "00970d74",
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
      "definition_site": "00970d70",
      "incomplete_value": false,
      "site": "00970d74",
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
      "00970d70",
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
      "00970d70",
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

- 旧版 [`00970d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/00970d64.md#insn-00970d70)
- 新版 `00970d70`（命令位置の公開資料なし）

~~~diff
- 00970d70 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00970d70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00970d70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00970d70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00970d70 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00970d70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00970d70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00970d70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00970d70 bytes 00280c91
+ 00970d70 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fd7a2bb8ca720342758b9df63694322"></a>

### [`00970fb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/00970fb4.md) → [`00970fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970fb4.md) FUN_00970fb4

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
      "definition_site": "00970fc8",
      "incomplete_value": false,
      "site": "00970fcc",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00970fc8",
      "incomplete_value": false,
      "site": "00970fcc",
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
            "const:2c8:8"
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
      "00970fcc",
      "DATA",
      [
        "storage",
        "00c0a2c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00970fcc",
      "DATA",
      [
        "storage",
        "00c0a378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00970fc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/00970fb4.md#insn-00970fc8)
- 新版 `00970fc8`（命令位置の公開資料なし）

~~~diff
- 00970fc8 ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 00970fc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00970fc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00970fc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00970fc8 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00970fc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00970fc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00970fc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00970fc8 bytes 08210b91
+ 00970fc8 bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae148ab5afd9f865c5815cc8f72456e2"></a>

### [`00970fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/00970fd8.md) → [`00970fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00970/00970fd8.md) FUN_00970fd8

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
      "definition_site": "00970fdc",
      "incomplete_value": false,
      "site": "00970fe0",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00970fdc",
      "incomplete_value": false,
      "site": "00970fe0",
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
            "const:2c8:8"
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
      "00970fe0",
      "DATA",
      [
        "storage",
        "00c0a2c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00970fe0",
      "DATA",
      [
        "storage",
        "00c0a378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00970fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00970/00970fd8.md#insn-00970fdc)
- 新版 `00970fdc`（命令位置の公開資料なし）

~~~diff
- 00970fdc ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 00970fdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00970fdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00970fdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00970fdc ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00970fdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00970fdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00970fdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00970fdc bytes 08210b91
+ 00970fdc bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2312dbe63e52e1c2c750d7cca56d0922"></a>

### [`00971024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971024.md) → [`00971024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971024.md) FUN_00971024

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
      "definition_site": "00971044",
      "incomplete_value": false,
      "site": "00971048",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00971044",
      "incomplete_value": false,
      "site": "00971048",
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
            "const:348:8"
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
      "00971048",
      "DATA",
      [
        "storage",
        "00c0a348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00971048",
      "DATA",
      [
        "storage",
        "00c0a3f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00971044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971024.md#insn-00971044)
- 新版 `00971044`（命令位置の公開資料なし）

~~~diff
- 00971044 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00971044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00971044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00971044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00971044 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00971044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00971044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00971044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00971044 bytes 08210d91
+ 00971044 bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e73211d9888f44fa07594c45990b393a"></a>

### [`0097105c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/0097105c.md) → [`0097105c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/0097105c.md) FUN_0097105c

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
      "definition_site": "00971064",
      "incomplete_value": false,
      "site": "00971068",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00971064",
      "incomplete_value": false,
      "site": "00971068",
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
            "const:348:8"
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
      "00971068",
      "DATA",
      [
        "storage",
        "00c0a348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00971068",
      "DATA",
      [
        "storage",
        "00c0a3f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00971064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/0097105c.md#insn-00971064)
- 新版 `00971064`（命令位置の公開資料なし）

~~~diff
- 00971064 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00971064 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00971064 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00971064 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00971064 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00971064 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00971064 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00971064 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00971064 bytes 29210d91
+ 00971064 bytes 29e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1402ccb3b7479a8bf1629744b2e6e2d8"></a>

### [`00971200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971200.md) → [`00971200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971200.md) FUN_00971200

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
      "definition_site": "00971214",
      "incomplete_value": false,
      "site": "00971218",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00971214",
      "incomplete_value": false,
      "site": "00971218",
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
            "const:3d8:8"
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
      "00971218",
      "DATA",
      [
        "storage",
        "00c0a3d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00971218",
      "DATA",
      [
        "storage",
        "00c0a488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00971214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971200.md#insn-00971214)
- 新版 `00971214`（命令位置の公開資料なし）

~~~diff
- 00971214 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 00971214 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00971214 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00971214 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00971214 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00971214 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00971214 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00971214 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00971214 bytes 08610f91
+ 00971214 bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13b68a71566ce0f46ebe469fc2ecb6f7"></a>

### [`00971224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971224.md) → [`00971224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971224.md) FUN_00971224

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
      "definition_site": "00971228",
      "incomplete_value": false,
      "site": "0097122c",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00971228",
      "incomplete_value": false,
      "site": "0097122c",
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
      "0097122c",
      "DATA",
      [
        "storage",
        "00c0a3d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097122c",
      "DATA",
      [
        "storage",
        "00c0a488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00971228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971224.md#insn-00971228)
- 新版 `00971228`（命令位置の公開資料なし）

~~~diff
- 00971228 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 00971228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00971228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00971228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00971228 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00971228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00971228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00971228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00971228 bytes 08610f91
+ 00971228 bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09c35057146debe22a0a7a725c66630d"></a>

### [`00971268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971268.md) → [`00971268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971268.md) FUN_00971268

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0096ff84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096ff84.md) [`00971268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971268.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0096ff84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096ff84.md) [`00971268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971268.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.92% / 新版 98.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009713bc",
      "incomplete_value": false,
      "site": "009713c4",
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
      "definition_site": "009713bc",
      "incomplete_value": false,
      "site": "009713c4",
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
      "definition_site": "00971514",
      "incomplete_value": false,
      "site": "0097151c",
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
      "definition_site": "00971514",
      "incomplete_value": false,
      "site": "0097151c",
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
      "definition_site": "00971870",
      "incomplete_value": false,
      "site": "00971878",
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
      "definition_site": "00971870",
      "incomplete_value": false,
      "site": "00971878",
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
      "009713bc",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00971514",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "009715bc",
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
      "009713bc",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00971514",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "009715bc",
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

- 旧版 [`009713bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971268.md#insn-009713bc) · [`00971514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971268.md#insn-00971514) · [`009715bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971268.md#insn-009715bc)
- 新版 `009713bc`（命令位置の公開資料なし） · `00971514`（命令位置の公開資料なし） · `009715bc`（命令位置の公開資料なし）

~~~diff
- 009713bc ["COPY", "tmp:0:8", ["const:311:8"]]
- 009713bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009713bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009713bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009713bc ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 009713bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009713bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009713bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009713bc bytes 21440c91
+ 009713bc bytes 21280c91
- 00971514 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00971514 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00971514 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00971514 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00971514 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00971514 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00971514 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00971514 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00971514 bytes 21d40b91
+ 00971514 bytes 21b80b91
- 009715bc ["COPY", "tmp:0:8", ["const:7da:8"]]
- 009715bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009715bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009715bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009715bc ["COPY", "tmp:0:8", ["const:867:8"]]
+ 009715bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009715bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009715bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009715bc bytes 21681f91
+ 009715bc bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-963f2f4dbf5303555871a543c30c2a47"></a>

### [`00971a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971a68.md) → [`00971a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971a68.md) FUN_00971a68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0096ff84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096ff84.md) [`00971a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971a68.md) [`0097a888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a888.md) [`00aae970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aae/00aae970.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`0096ff84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096ff84.md) [`00971a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971a68.md) [`0097a888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a888.md) [`00aaea38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaea38.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00971bbc",
      "incomplete_value": true,
      "site": "00971bc4",
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
      "definition_site": "00971bbc",
      "incomplete_value": true,
      "site": "00971bc4",
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
      "definition_site": "00971c78",
      "incomplete_value": true,
      "site": "00971c80",
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
            "const:2ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00971c78",
      "incomplete_value": true,
      "site": "00971c80",
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
      "definition_site": "00971fe8",
      "incomplete_value": true,
      "site": "00971ff8",
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
      "definition_site": "00971fe8",
      "incomplete_value": true,
      "site": "00971ff8",
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
      "00971bbc",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00971c78",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00971fe8",
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
      "00971bbc",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00971c78",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00971fe8",
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

- 旧版 [`00971bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971a68.md#insn-00971bbc) · [`00971c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971a68.md#insn-00971c78) · [`00971fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971a68.md#insn-00971fe8)
- 新版 `00971bbc`（命令位置の公開資料なし） · `00971c78`（命令位置の公開資料なし） · `00971fe8`（命令位置の公開資料なし）

~~~diff
- 00971bbc ["COPY", "tmp:0:8", ["const:311:8"]]
- 00971bbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00971bbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00971bbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00971bbc ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00971bbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00971bbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00971bbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00971bbc bytes 21440c91
+ 00971bbc bytes 21280c91
- 00971c78 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00971c78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00971c78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00971c78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00971c78 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00971c78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00971c78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00971c78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00971c78 bytes 21d40b91
+ 00971c78 bytes 21b80b91
- 00971fe8 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 00971fe8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00971fe8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00971fe8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00971fe8 ["COPY", "tmp:0:8", ["const:672:8"]]
+ 00971fe8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00971fe8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00971fe8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00971fe8 bytes 63941791
+ 00971fe8 bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be89768e89ec609ee8891cf157d5d34a"></a>

### [`0097239c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/0097239c.md) → [`0097239c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/0097239c.md) FUN_0097239c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0096f440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096f440.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0096f440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096f440.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "009723d4",
      "incomplete_value": false,
      "site": "009723dc",
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
      "definition_site": "009723d4",
      "incomplete_value": false,
      "site": "009723dc",
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
      "009723dc",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00972494",
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
      "009723dc",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00972494",
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

- 旧版 [`009723d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/0097239c.md#insn-009723d4) · [`009723d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/0097239c.md#insn-009723d8)
- 新版 `009723d4`（命令位置の公開資料なし） · `009723d8`（命令位置の公開資料なし）

~~~diff
- 009723d4 ["COPY", "tmp:0:8", ["const:98:8"]]
- 009723d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009723d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009723d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009723d4 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 009723d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009723d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009723d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009723d4 bytes 08610291
+ 009723d4 bytes 08210591
- 009723d8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 009723d8 bytes f30300aa
+ 009723d8 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 009723d8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6600e5c450757165afcd8020715bf10f"></a>

### [`00972514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972514.md) → [`00972514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972514.md) FUN_00972514

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097252c",
      "incomplete_value": true,
      "site": "0097253c",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097252c",
      "incomplete_value": true,
      "site": "0097253c",
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
            "const:458:8"
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
      "0097253c",
      "DATA",
      [
        "storage",
        "00c0a458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097253c",
      "DATA",
      [
        "storage",
        "00c0a508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097252c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972514.md#insn-0097252c)
- 新版 `0097252c`（命令位置の公開資料なし）

~~~diff
- 0097252c ["COPY", "tmp:0:8", ["const:458:8"]]
- 0097252c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097252c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097252c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097252c ["COPY", "tmp:0:8", ["const:508:8"]]
+ 0097252c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097252c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097252c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097252c bytes 08611191
+ 0097252c bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc044e3b651493af74e6db50c353eda3"></a>

### [`009725a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/009725a4.md) → [`009725a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/009725a4.md) FUN_009725a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "009725bc",
      "incomplete_value": false,
      "site": "009725cc",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009725bc",
      "incomplete_value": false,
      "site": "009725cc",
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
            "const:458:8"
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
      "009725cc",
      "DATA",
      [
        "storage",
        "00c0a458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009725cc",
      "DATA",
      [
        "storage",
        "00c0a508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009725bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/009725a4.md#insn-009725bc)
- 新版 `009725bc`（命令位置の公開資料なし）

~~~diff
- 009725bc ["COPY", "tmp:0:8", ["const:458:8"]]
- 009725bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009725bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009725bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009725bc ["COPY", "tmp:0:8", ["const:508:8"]]
+ 009725bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009725bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009725bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009725bc bytes 08611191
+ 009725bc bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9a42d06fcb3cae02e148a1ae3f91922"></a>

### [`00972630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972630.md) → [`00972630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972630.md) FUN_00972630

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00972660",
      "incomplete_value": false,
      "site": "00972660",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00972660",
      "incomplete_value": false,
      "site": "00972660",
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
            "const:458:8"
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
      "00972660",
      "DATA",
      [
        "storage",
        "00c0a458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00972660",
      "DATA",
      [
        "storage",
        "00c0a508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00972658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972630.md#insn-00972658)
- 新版 `00972658`（命令位置の公開資料なし）

~~~diff
- 00972658 ["COPY", "tmp:0:8", ["const:458:8"]]
- 00972658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972658 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 00972658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972658 bytes 08611191
+ 00972658 bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9068beebafffaf0afac1dc45c4dc30e8"></a>

### [`00972738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972738.md) → [`00972738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972738.md) FUN_00972738

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00972760",
      "incomplete_value": false,
      "site": "00972760",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00972760",
      "incomplete_value": false,
      "site": "00972760",
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
            "const:458:8"
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
      "00972760",
      "DATA",
      [
        "storage",
        "00c0a458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00972760",
      "DATA",
      [
        "storage",
        "00c0a508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00972758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972738.md#insn-00972758) · [`0097275c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972738.md#insn-0097275c)
- 新版 `00972758`（命令位置の公開資料なし） · `0097275c`（命令位置の公開資料なし）

~~~diff
- 00972758 ["COPY", "tmp:0:8", ["const:458:8"]]
- 00972758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972758 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 00972758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972758 bytes 08611191
+ 00972758 bytes 08211491
- 0097275c ["COPY", "register:40a0:8", ["register:4008:8"]]
- 0097275c bytes f40301aa
+ 0097275c ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 0097275c bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b53bca9e794aa8921fc49a3aaf6dabd"></a>

### [`00972af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972af8.md) → [`00972af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972af8.md) FUN_00972af8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0096fb34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096f/0096fb34.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00592/00592ccc.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`0096fb34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096f/0096fb34.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "00972b30",
      "incomplete_value": false,
      "site": "00972b38",
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
      "definition_site": "00972b30",
      "incomplete_value": false,
      "site": "00972b38",
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
      "00972b38",
      "DATA",
      [
        "storage",
        "00bf3098",
        null,
        "pointer"
      ]
    ],
    [
      "00972bf0",
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
      "00972b38",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00972bf0",
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

- 旧版 [`00972b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972af8.md#insn-00972b30) · [`00972b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972af8.md#insn-00972b34)
- 新版 `00972b30`（命令位置の公開資料なし） · `00972b34`（命令位置の公開資料なし）

~~~diff
- 00972b30 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00972b30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972b30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972b30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972b30 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00972b30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972b30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972b30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972b30 bytes 08610291
+ 00972b30 bytes 08210591
- 00972b34 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00972b34 bytes f30300aa
+ 00972b34 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00972b34 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af984be8b603f43e5a32a34390f0f666"></a>

### [`00972c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972c70.md) → [`00972c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972c70.md) FUN_00972c70

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00972c88",
      "incomplete_value": false,
      "site": "00972c98",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00972c88",
      "incomplete_value": false,
      "site": "00972c98",
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
            "const:4d8:8"
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
      "00972c98",
      "DATA",
      [
        "storage",
        "00c0a4d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00972c98",
      "DATA",
      [
        "storage",
        "00c0a588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00972c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972c70.md#insn-00972c88)
- 新版 `00972c88`（命令位置の公開資料なし）

~~~diff
- 00972c88 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 00972c88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972c88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972c88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972c88 ["COPY", "tmp:0:8", ["const:588:8"]]
+ 00972c88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972c88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972c88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972c88 bytes 08611391
+ 00972c88 bytes 08211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a19efbd2fddcfc3afe438d41405c17b8"></a>

### [`00972d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972d00.md) → [`00972d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972d00.md) FUN_00972d00

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00972d18",
      "incomplete_value": false,
      "site": "00972d28",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00972d18",
      "incomplete_value": false,
      "site": "00972d28",
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
            "const:4d8:8"
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
      "00972d28",
      "DATA",
      [
        "storage",
        "00c0a4d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00972d28",
      "DATA",
      [
        "storage",
        "00c0a588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00972d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972d00.md#insn-00972d18)
- 新版 `00972d18`（命令位置の公開資料なし）

~~~diff
- 00972d18 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 00972d18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972d18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972d18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972d18 ["COPY", "tmp:0:8", ["const:588:8"]]
+ 00972d18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972d18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972d18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972d18 bytes 08611391
+ 00972d18 bytes 08211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34543bf20cb84dfb9a7d6fd2db876858"></a>

### [`00972d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972d8c.md) → [`00972d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972d8c.md) FUN_00972d8c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00972dbc",
      "incomplete_value": true,
      "site": "00972dbc",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00972dbc",
      "incomplete_value": true,
      "site": "00972dbc",
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
            "const:4d8:8"
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
      "00972dbc",
      "DATA",
      [
        "storage",
        "00c0a4d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00972dbc",
      "DATA",
      [
        "storage",
        "00c0a588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00972db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972d8c.md#insn-00972db4)
- 新版 `00972db4`（命令位置の公開資料なし）

~~~diff
- 00972db4 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 00972db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972db4 ["COPY", "tmp:0:8", ["const:588:8"]]
+ 00972db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972db4 bytes 08611391
+ 00972db4 bytes 08211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1efbe59fa81bb079fd5bcaecf080244c"></a>

### [`00972e94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972e94.md) → [`00972e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00972/00972e94.md) FUN_00972e94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00972ebc",
      "incomplete_value": false,
      "site": "00972ebc",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00972ebc",
      "incomplete_value": false,
      "site": "00972ebc",
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
            "const:4d8:8"
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
      "00972ebc",
      "DATA",
      [
        "storage",
        "00c0a4d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00972ebc",
      "DATA",
      [
        "storage",
        "00c0a588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00972eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972e94.md#insn-00972eb4) · [`00972eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00972/00972e94.md#insn-00972eb8)
- 新版 `00972eb4`（命令位置の公開資料なし） · `00972eb8`（命令位置の公開資料なし）

~~~diff
- 00972eb4 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 00972eb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00972eb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00972eb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00972eb4 ["COPY", "tmp:0:8", ["const:588:8"]]
+ 00972eb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00972eb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00972eb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00972eb4 bytes 08611391
+ 00972eb4 bytes 08211691
- 00972eb8 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 00972eb8 bytes f40301aa
+ 00972eb8 ["COPY", "register:40a0:8", ["register:4008:8"]]
+ 00972eb8 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c1ae1b81afb4fc2c141574720750d91"></a>

### [`00973254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973254.md) → [`00973254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973254.md) _INIT_189

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00b55550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55550.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00973290",
      "incomplete_value": true,
      "site": "009732ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00973290",
      "incomplete_value": true,
      "site": "009732ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009732f4",
      "incomplete_value": true,
      "site": "0097330c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009732f4",
      "incomplete_value": true,
      "site": "0097330c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009734a4",
      "incomplete_value": true,
      "site": "009734bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ba7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009734a4",
      "incomplete_value": true,
      "site": "009734bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b1a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00973290",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "009732b4",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "009732d4",
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
      "00973290",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "009732b4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "009732d4",
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

- 旧版 [`00973280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973254.md#insn-00973280) · [`00973288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973254.md#insn-00973288)
- 新版 `00973280`（命令位置の公開資料なし） · `00973288`（命令位置の公開資料なし）

~~~diff
- 00973280 ["COPY", "tmp:0:8", ["const:858:8"]]
- 00973280 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00973280 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00973280 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00973280 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 00973280 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00973280 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00973280 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00973280 bytes 73622191
+ 00973280 bytes 73622491
- 00973288 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00973288 bytes a9c9ff90
+ 00973288 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00973288 bytes a9c9ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c89cb4bf45b23004b7d80952bd622d88"></a>

### [`00973680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973680.md) → [`00973680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973680.md) FUN_00973680

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0073a198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a198.md) [`00976fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/00976fb0.md) [`0097ff3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097ff3c.md) [`0097ffb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097ffb0.md) · 呼出先 2件 [`009d6a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009d6/009d6a64.md) [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md)
- 新版 呼出元 4件 [`0073a198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a198.md) [`00976fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976fb0.md) [`0097ff3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097ff3c.md) [`0097ffb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097ffb0.md) · 呼出先 2件 [`009d6a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6a64.md) [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009736a0",
      "incomplete_value": false,
      "site": "009736a8",
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
      "definition_site": "009736a0",
      "incomplete_value": false,
      "site": "009736a8",
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009736a0",
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
      "009736a0",
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

- 旧版 [`009736a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973680.md#insn-009736a0)
- 新版 `009736a0`（命令位置の公開資料なし）

~~~diff
- 009736a0 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 009736a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009736a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009736a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009736a0 ["COPY", "tmp:0:8", ["const:866:8"]]
+ 009736a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009736a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009736a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009736a0 bytes 21641f91
+ 009736a0 bytes 21982191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47b18eef0f4581019b0e5d38c1fcbce1"></a>

### [`00973970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973970.md) → [`00973970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973970.md) FUN_00973970

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0097ffb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097ffb0.md) · 呼出先 9件 [`00469fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469fac.md) [`007cd560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cd/007cd560.md) [`009d6a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009d6/009d6a64.md) [`009d6ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009d6/009d6ae4.md) [`009d750c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009d7/009d750c.md)
- 新版 呼出元 1件 [`0097ffb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097ffb0.md) · 呼出先 9件 [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`007cd560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd560.md) [`009d6a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6a64.md) [`009d6ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6ae4.md) [`009d750c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d7/009d750c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009739cc",
      "incomplete_value": false,
      "site": "009739dc",
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
      "definition_site": "009739cc",
      "incomplete_value": false,
      "site": "009739dc",
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
      "009739cc",
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
      "009739cc",
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

- 旧版 [`009739cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973970.md#insn-009739cc)
- 新版 `009739cc`（命令位置の公開資料なし）

~~~diff
- 009739cc ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 009739cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009739cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009739cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009739cc ["COPY", "tmp:0:8", ["const:866:8"]]
+ 009739cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009739cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009739cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009739cc bytes 21641f91
+ 009739cc bytes 21982191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e5caca93d78d88c3ecab0ad46db06f5"></a>

### [`00973b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973b10.md) → [`00973b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973b10.md) FUN_00973b10

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009743fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00974/009743fc.md) · 呼出先 15件 [`00428c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428c14.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0053ee5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee5c.md) [`00728090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00728/00728090.md) [`00975468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975468.md)
- 新版 呼出元 1件 [`009743fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00974/009743fc.md) · 呼出先 15件 [`00428c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428c14.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0053ee5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`00975468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975468.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.61% / 新版 94.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00973d20",
      "incomplete_value": true,
      "site": "00973d20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:169:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00973d20",
      "incomplete_value": true,
      "site": "00973d20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:170:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00973d18",
      "incomplete_value": true,
      "site": "00973d2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:299:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00973d18",
      "incomplete_value": true,
      "site": "00973d2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:20c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00973d80",
      "incomplete_value": true,
      "site": "00973d80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5fe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00973d80",
      "incomplete_value": true,
      "site": "00973d80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:571:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00973b8c",
      "PARAM",
      [
        "storage",
        "002a6e42",
        null,
        "string"
      ]
    ],
    [
      "00973bf0",
      "PARAM",
      [
        "storage",
        "002a8981",
        null,
        "string"
      ]
    ],
    [
      "00973c60",
      "PARAM",
      [
        "storage",
        "002a29c2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00973b8c",
      "PARAM",
      [
        "storage",
        "002a6e3b",
        null,
        "string"
      ]
    ],
    [
      "00973bf0",
      "PARAM",
      [
        "storage",
        "002a88ed",
        null,
        "string"
      ]
    ],
    [
      "00973c60",
      "PARAM",
      [
        "storage",
        "002a29bb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00973b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973b10.md#insn-00973b8c) · [`00973bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973b10.md#insn-00973bf0) · [`00973c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973b10.md#insn-00973c60)
- 新版 `00973b8c`（命令位置の公開資料なし） · `00973bf0`（命令位置の公開資料なし） · `00973c60`（命令位置の公開資料なし）

~~~diff
- 00973b8c ["COPY", "tmp:0:8", ["const:e42:8"]]
- 00973b8c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00973b8c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00973b8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00973b8c ["COPY", "tmp:0:8", ["const:e3b:8"]]
+ 00973b8c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00973b8c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00973b8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00973b8c bytes 21083991
+ 00973b8c bytes 21ec3891
- 00973bf0 ["COPY", "tmp:0:8", ["const:981:8"]]
- 00973bf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00973bf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00973bf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00973bf0 ["COPY", "tmp:0:8", ["const:8ed:8"]]
+ 00973bf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00973bf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00973bf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00973bf0 bytes 21042691
+ 00973bf0 bytes 21b42391
- 00973c60 ["COPY", "tmp:0:8", ["const:9c2:8"]]
- 00973c60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00973c60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00973c60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00973c60 ["COPY", "tmp:0:8", ["const:9bb:8"]]
+ 00973c60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00973c60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00973c60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00973c60 bytes 21082791
+ 00973c60 bytes 21ec2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23deff06d15a5e6499f120ecc445e877"></a>

### [`009743fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00974/009743fc.md) → [`009743fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00974/009743fc.md) FUN_009743fc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00989a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00989/00989a48.md) · 呼出先 16件 [`00428c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428c14.md) [`0053ee5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee5c.md) [`00728090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00728/00728090.md) [`00973b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973b10.md) [`00975ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975ac0.md)
- 新版 呼出元 1件 [`00989a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/00989a48.md) · 呼出先 16件 [`00428c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428c14.md) [`0053ee5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`00973b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973b10.md) [`00975ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975ac0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.02% / 新版 94.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097444c",
      "incomplete_value": false,
      "site": "0097444c",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097444c",
      "incomplete_value": false,
      "site": "0097444c",
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
            "const:5d8:8"
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
      "definition_site": "00974620",
      "incomplete_value": true,
      "site": "00974620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5fe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00974620",
      "incomplete_value": true,
      "site": "00974620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:571:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00974624",
      "incomplete_value": true,
      "site": "00974624",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00974624",
      "incomplete_value": true,
      "site": "00974624",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 38,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0097444c",
      "DATA",
      [
        "storage",
        "00c0a5d8",
        null,
        "undefined *"
      ]
    ],
    [
      "009744a8",
      "PARAM",
      [
        "storage",
        "002a6e42",
        null,
        "string"
      ]
    ],
    [
      "0097450c",
      "PARAM",
      [
        "storage",
        "002a8981",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0097444c",
      "DATA",
      [
        "storage",
        "00c0a688",
        null,
        "undefined *"
      ]
    ],
    [
      "009744a8",
      "PARAM",
      [
        "storage",
        "002a6e3b",
        null,
        "string"
      ]
    ],
    [
      "0097450c",
      "PARAM",
      [
        "storage",
        "002a88ed",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00974440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00974/009743fc.md#insn-00974440) · [`009744a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00974/009743fc.md#insn-009744a8) · [`0097450c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00974/009743fc.md#insn-0097450c)
- 新版 `00974440`（命令位置の公開資料なし） · `009744a8`（命令位置の公開資料なし） · `0097450c`（命令位置の公開資料なし）

~~~diff
- 00974440 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00974440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00974440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00974440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00974440 ["COPY", "tmp:0:8", ["const:688:8"]]
+ 00974440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00974440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00974440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00974440 bytes 08611791
+ 00974440 bytes 08211a91
- 009744a8 ["COPY", "tmp:0:8", ["const:e42:8"]]
- 009744a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009744a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009744a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009744a8 ["COPY", "tmp:0:8", ["const:e3b:8"]]
+ 009744a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009744a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009744a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009744a8 bytes 21083991
+ 009744a8 bytes 21ec3891
- 0097450c ["COPY", "tmp:0:8", ["const:981:8"]]
- 0097450c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0097450c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0097450c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0097450c ["COPY", "tmp:0:8", ["const:8ed:8"]]
+ 0097450c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0097450c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0097450c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0097450c bytes 21042691
+ 0097450c bytes 21b42391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1d4e6e891c29968ff005186bbe831d0"></a>

### [`009749a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00974/009749a4.md) → [`009749a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00974/009749a4.md) FUN_009749a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00980fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980fdc.md) · 呼出先 18件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`005857bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00585/005857bc.md) [`005859d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00585/005859d8.md)
- 新版 呼出元 1件 [`00980fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980fdc.md) · 呼出先 18件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`005857bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00585/005857bc.md) [`005859d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00585/005859d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.75% / 新版 99.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00974d3c",
      "incomplete_value": false,
      "site": "00974d40",
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
            "const:d71:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00974d3c",
      "incomplete_value": false,
      "site": "00974d40",
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
            "const:d6b:8"
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
      "00974d3c",
      "PARAM",
      [
        "storage",
        "002aad6b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00974d3c",
      "PARAM",
      [
        "storage",
        "002aad71",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00974d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00974/009749a4.md#insn-00974d3c)
- 新版 `00974d3c`（命令位置の公開資料なし）

~~~diff
- 00974d3c ["COPY", "tmp:0:8", ["const:d6b:8"]]
- 00974d3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00974d3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00974d3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00974d3c ["COPY", "tmp:0:8", ["const:d71:8"]]
+ 00974d3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00974d3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00974d3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00974d3c bytes 21ac3591
+ 00974d3c bytes 21c43591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-044511c882915a92c7436ec07991d1c5"></a>

### [`009752b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/009752b8.md) → [`009752b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/009752b8.md) FUN_009752b8

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
      "definition_site": "009752d0",
      "incomplete_value": false,
      "site": "009752dc",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009752d0",
      "incomplete_value": false,
      "site": "009752dc",
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
            "const:558:8"
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
      "009752dc",
      "DATA",
      [
        "storage",
        "00c0a558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009752dc",
      "DATA",
      [
        "storage",
        "00c0a608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009752d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/009752b8.md#insn-009752d0)
- 新版 `009752d0`（命令位置の公開資料なし）

~~~diff
- 009752d0 ["COPY", "tmp:0:8", ["const:558:8"]]
- 009752d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009752d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009752d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009752d0 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 009752d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009752d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009752d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009752d0 bytes 08611591
+ 009752d0 bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2c1b9c0b1c67300e30398092201fd6b"></a>

### [`00975314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975314.md) → [`00975314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975314.md) FUN_00975314

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
      "definition_site": "0097533c",
      "incomplete_value": false,
      "site": "00975340",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097533c",
      "incomplete_value": false,
      "site": "00975340",
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
            "const:558:8"
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
      "00975340",
      "DATA",
      [
        "storage",
        "00c0a558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00975340",
      "DATA",
      [
        "storage",
        "00c0a608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097533c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975314.md#insn-0097533c)
- 新版 `0097533c`（命令位置の公開資料なし）

~~~diff
- 0097533c ["COPY", "tmp:0:8", ["const:558:8"]]
- 0097533c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097533c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097533c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097533c ["COPY", "tmp:0:8", ["const:608:8"]]
+ 0097533c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097533c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097533c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097533c bytes 29611591
+ 0097533c bytes 29211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc0fb0c18ea21b7343671eae2aeeb047"></a>

### [`009753ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/009753ac.md) → [`009753ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/009753ac.md) FUN_009753ac

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
      "definition_site": "009753cc",
      "incomplete_value": false,
      "site": "009753d0",
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
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009753cc",
      "incomplete_value": false,
      "site": "009753d0",
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
            "const:558:8"
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
      "009753d0",
      "DATA",
      [
        "storage",
        "00c0a558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009753d0",
      "DATA",
      [
        "storage",
        "00c0a608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009753cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/009753ac.md#insn-009753cc)
- 新版 `009753cc`（命令位置の公開資料なし）

~~~diff
- 009753cc ["COPY", "tmp:0:8", ["const:558:8"]]
- 009753cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009753cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009753cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009753cc ["COPY", "tmp:0:8", ["const:608:8"]]
+ 009753cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009753cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009753cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009753cc bytes 29611591
+ 009753cc bytes 29211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b8b829db6a15d0a4566ee682f9e39a7"></a>

### [`009754b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/009754b8.md) → [`009754b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/009754b8.md) FUN_009754b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00574054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574054.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00574054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00975684",
      "incomplete_value": true,
      "site": "00975684",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:356:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00975684",
      "incomplete_value": true,
      "site": "00975684",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ea:8"
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
      "definition_site": "00975678",
      "incomplete_value": true,
      "site": "00975688",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00975678",
      "incomplete_value": true,
      "site": "00975688",
      "value": [
        "LOAD",
        "8",
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
      "00975674",
      "READ",
      [
        "storage",
        "002a83ea",
        null,
        "string"
      ]
    ],
    [
      "00975678",
      "READ",
      [
        "storage",
        "002a83f1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00975674",
      "READ",
      [
        "storage",
        "002a8356",
        null,
        "string"
      ]
    ],
    [
      "00975678",
      "READ",
      [
        "storage",
        "002a835d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097566c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/009754b8.md#insn-0097566c)
- 新版 `0097566c`（命令位置の公開資料なし）

~~~diff
- 0097566c ["COPY", "tmp:0:8", ["const:3ea:8"]]
- 0097566c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097566c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097566c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097566c ["COPY", "tmp:0:8", ["const:356:8"]]
+ 0097566c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097566c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097566c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097566c bytes 29a90f91
+ 0097566c bytes 29590d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d8ff54c3c3369bf9a3b63ebea4876da"></a>

### [`00975a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975a8c.md) → [`00975a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975a8c.md) FUN_00975a8c

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
      "definition_site": "00975aa0",
      "incomplete_value": false,
      "site": "00975aa4",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00975aa0",
      "incomplete_value": false,
      "site": "00975aa4",
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
            "const:5d8:8"
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
      "00975aa4",
      "DATA",
      [
        "storage",
        "00c0a5d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00975aa4",
      "DATA",
      [
        "storage",
        "00c0a688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00975aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975a8c.md#insn-00975aa0)
- 新版 `00975aa0`（命令位置の公開資料なし）

~~~diff
- 00975aa0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00975aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00975aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00975aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00975aa0 ["COPY", "tmp:0:8", ["const:688:8"]]
+ 00975aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00975aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00975aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00975aa0 bytes 08611791
+ 00975aa0 bytes 08211a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-891408feb71ca8b7d2a5922d32d7c1ea"></a>

### [`00975ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975ab0.md) → [`00975ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975ab0.md) FUN_00975ab0

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
      "definition_site": "00975ab4",
      "incomplete_value": false,
      "site": "00975ab8",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00975ab4",
      "incomplete_value": false,
      "site": "00975ab8",
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
      "00975ab8",
      "DATA",
      [
        "storage",
        "00c0a5d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00975ab8",
      "DATA",
      [
        "storage",
        "00c0a688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00975ab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975ab0.md#insn-00975ab4)
- 新版 `00975ab4`（命令位置の公開資料なし）

~~~diff
- 00975ab4 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00975ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00975ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00975ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00975ab4 ["COPY", "tmp:0:8", ["const:688:8"]]
+ 00975ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00975ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00975ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00975ab4 bytes 08611791
+ 00975ab4 bytes 08211a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba892a6dd7a5508936e2828c51c087e"></a>

### [`00975af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975af8.md) → [`00975af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975af8.md) FUN_00975af8

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
      "definition_site": "00975b1c",
      "incomplete_value": false,
      "site": "00975b1c",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00975b1c",
      "incomplete_value": false,
      "site": "00975b1c",
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
            "const:658:8"
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
      "00975b1c",
      "DATA",
      [
        "storage",
        "00c0a658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00975b1c",
      "DATA",
      [
        "storage",
        "00c0a708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00975b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975af8.md#insn-00975b18)
- 新版 `00975b18`（命令位置の公開資料なし）

~~~diff
- 00975b18 ["COPY", "tmp:0:8", ["const:658:8"]]
- 00975b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00975b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00975b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00975b18 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00975b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00975b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00975b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00975b18 bytes 08611991
+ 00975b18 bytes 08211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9767324da915b3321b1b4d46c71009d0"></a>

### [`00975b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975b2c.md) → [`00975b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975b2c.md) FUN_00975b2c

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
      "definition_site": "00975b38",
      "incomplete_value": false,
      "site": "00975b38",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00975b38",
      "incomplete_value": false,
      "site": "00975b38",
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
      "00975b38",
      "DATA",
      [
        "storage",
        "00c0a658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00975b38",
      "DATA",
      [
        "storage",
        "00c0a708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00975b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975b2c.md#insn-00975b34)
- 新版 `00975b34`（命令位置の公開資料なし）

~~~diff
- 00975b34 ["COPY", "tmp:0:8", ["const:658:8"]]
- 00975b34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00975b34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00975b34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00975b34 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00975b34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00975b34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00975b34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00975b34 bytes 29611991
+ 00975b34 bytes 29211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e53c95724ed8432eb2b047827a9b683f"></a>

### [`00975b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975b48.md) → [`00975b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975b48.md) FUN_00975b48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00574054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574054.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00574054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.17% / 新版 98.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00975c74",
      "incomplete_value": true,
      "site": "00975c74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:356:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00975c74",
      "incomplete_value": true,
      "site": "00975c74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ea:8"
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
      "definition_site": "00975c68",
      "incomplete_value": true,
      "site": "00975c78",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00975c68",
      "incomplete_value": true,
      "site": "00975c78",
      "value": [
        "LOAD",
        "8",
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
      "00975c64",
      "READ",
      [
        "storage",
        "002a83ea",
        null,
        "string"
      ]
    ],
    [
      "00975c68",
      "READ",
      [
        "storage",
        "002a83f1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00975c64",
      "READ",
      [
        "storage",
        "002a8356",
        null,
        "string"
      ]
    ],
    [
      "00975c68",
      "READ",
      [
        "storage",
        "002a835d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00975c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975b48.md#insn-00975c5c)
- 新版 `00975c5c`（命令位置の公開資料なし）

~~~diff
- 00975c5c ["COPY", "tmp:0:8", ["const:3ea:8"]]
- 00975c5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00975c5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00975c5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00975c5c ["COPY", "tmp:0:8", ["const:356:8"]]
+ 00975c5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00975c5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00975c5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00975c5c bytes 29a90f91
+ 00975c5c bytes 29590d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45401a67ad89ec7fa3921db0a28db105"></a>

### [`009763c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/009763c8.md) → [`009763c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/009763c8.md) FUN_009763c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00976040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/00976040.md) [`00976638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/00976638.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00976040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976040.md) [`00976638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976638.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "009763d4",
      "incomplete_value": false,
      "site": "009763d8",
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
      "definition_site": "009763d4",
      "incomplete_value": false,
      "site": "009763d8",
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
      "009763d4",
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
      "009763d4",
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

- 旧版 [`009763d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/009763c8.md#insn-009763d4)
- 新版 `009763d4`（命令位置の公開資料なし）

~~~diff
- 009763d4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 009763d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009763d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009763d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009763d4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 009763d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009763d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009763d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009763d4 bytes 00280c91
+ 009763d4 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6ee90786d8bd355462a70e6f821ab9b"></a>

### [`009767c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/009767c4.md) → [`009767c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/009767c4.md) _INIT_190

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00976824",
      "incomplete_value": true,
      "site": "00976840",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00976824",
      "incomplete_value": true,
      "site": "00976840",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00976844",
      "incomplete_value": true,
      "site": "00976860",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00976844",
      "incomplete_value": true,
      "site": "00976860",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009769ec",
      "incomplete_value": false,
      "site": "009769f8",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009769ec",
      "incomplete_value": false,
      "site": "009769f8",
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
            "const:8a8:8"
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
      "00976800",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00976824",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00976844",
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
      "00976800",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00976824",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00976844",
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

- 旧版 [`009767f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/009767c4.md#insn-009767f0) · [`009767f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/009767c4.md#insn-009767f8)
- 新版 `009767f0`（命令位置の公開資料なし） · `009767f8`（命令位置の公開資料なし）

~~~diff
- 009767f0 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 009767f0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009767f0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009767f0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009767f0 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 009767f0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009767f0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009767f0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009767f0 bytes 73a22291
+ 009767f0 bytes 73a22591
- 009767f8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 009767f8 bytes 89c9ffb0
+ 009767f8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 009767f8 bytes 89c9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-771e7ee9cfeec3fd1e2857bffd006f95"></a>

### [`00976fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/00976fb0.md) → [`00976fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976fb0.md) FUN_00976fb0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a2c36c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a2c/00a2c36c.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00837f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00837/00837f3c.md) [`00973680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973680.md) [`00973ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973ae8.md) [`00976638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/00976638.md)
- 新版 呼出元 1件 [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00837f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00837/00837f3c.md) [`00973680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973680.md) [`00973ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973ae8.md) [`00976638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976638.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097711c",
      "incomplete_value": false,
      "site": "00977128",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097711c",
      "incomplete_value": false,
      "site": "00977128",
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
            "const:6d8:8"
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
      "00977128",
      "DATA",
      [
        "storage",
        "00c0a6d8",
        null,
        "pointer"
      ]
    ],
    [
      "00977198",
      "READ",
      [
        "storage",
        "00c0a6e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00977128",
      "DATA",
      [
        "storage",
        "00c0a788",
        null,
        "pointer"
      ]
    ],
    [
      "00977198",
      "READ",
      [
        "storage",
        "00c0a798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097711c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/00976fb0.md#insn-0097711c)
- 新版 `0097711c`（命令位置の公開資料なし）

~~~diff
- 0097711c ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 0097711c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097711c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097711c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097711c ["COPY", "tmp:0:8", ["const:788:8"]]
+ 0097711c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097711c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097711c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097711c bytes 08611b91
+ 0097711c bytes 08211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f7b86b8d0886d8a1b3411566b04f989"></a>

### [`00977828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00977/00977828.md) → [`00977828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00977/00977828.md) FUN_00977828

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073a198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073a198.md) · 呼出先 11件 [`0097af60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097af60.md) [`0097af6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097af6c.md) [`0097de84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097de84.md) [`0097e4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097e4d8.md) [`0097ffb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097ffb0.md)
- 新版 呼出元 1件 [`0073a198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a198.md) · 呼出先 11件 [`0097af60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097af60.md) [`0097af6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097af6c.md) [`0097de84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097de84.md) [`0097e4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097e4d8.md) [`0097ffb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097ffb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00977978",
      "incomplete_value": false,
      "site": "00977984",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00977978",
      "incomplete_value": false,
      "site": "00977984",
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
            "const:6d8:8"
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
      "00977984",
      "DATA",
      [
        "storage",
        "00c0a6d8",
        null,
        "pointer"
      ]
    ],
    [
      "00977a3c",
      "READ",
      [
        "storage",
        "00c0a6e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00977984",
      "DATA",
      [
        "storage",
        "00c0a788",
        null,
        "pointer"
      ]
    ],
    [
      "00977a3c",
      "READ",
      [
        "storage",
        "00c0a798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00977978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00977/00977828.md#insn-00977978)
- 新版 `00977978`（命令位置の公開資料なし）

~~~diff
- 00977978 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 00977978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00977978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00977978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00977978 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 00977978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00977978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00977978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00977978 bytes 08611b91
+ 00977978 bytes 08211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2979dd902a45f808bf89a209709d58a7"></a>

### [`009785f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00978/009785f0.md) → [`009785f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009785f0.md) FUN_009785f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00761844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00761/00761844.md) [`009785f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00978/009785f0.md) [`0097c594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c594.md) [`00a3371c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a33/00a3371c.md) · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00728090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00728/00728090.md) [`009785f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00978/009785f0.md) [`0097c514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c514.md) [`0097c938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c938.md)
- 新版 呼出元 4件 [`00761844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761844.md) [`009785f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009785f0.md) [`0097c594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c594.md) [`00a3371c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a3371c.md) · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`009785f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009785f0.md) [`0097c514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c514.md) [`0097c938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c938.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.80% / 新版 98.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009787f8",
      "incomplete_value": false,
      "site": "00978804",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009787f8",
      "incomplete_value": false,
      "site": "00978804",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009788c8",
      "incomplete_value": false,
      "site": "009788c8",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009788c8",
      "incomplete_value": false,
      "site": "009788c8",
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
            "const:7a8:8"
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
      "00978804",
      "DATA",
      [
        "storage",
        "00c0a728",
        null,
        "undefined *"
      ]
    ],
    [
      "009788c8",
      "DATA",
      [
        "storage",
        "00c0a7a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00978948",
      "READ",
      [
        "storage",
        "00c0a7d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00978804",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "undefined *"
      ]
    ],
    [
      "009788c8",
      "DATA",
      [
        "storage",
        "00c0a858",
        null,
        "undefined *"
      ]
    ],
    [
      "00978948",
      "READ",
      [
        "storage",
        "00c0a880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009787f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00978/009785f0.md#insn-009787f8) · [`009788c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00978/009785f0.md#insn-009788c0)
- 新版 `009787f8`（命令位置の公開資料なし） · `009788c0`（命令位置の公開資料なし）

~~~diff
- 009787f8 ["COPY", "tmp:0:8", ["const:728:8"]]
- 009787f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009787f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009787f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009787f8 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 009787f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009787f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009787f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009787f8 bytes 08a11c91
+ 009787f8 bytes 08611f91
- 009788c0 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 009788c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009788c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009788c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009788c0 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 009788c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009788c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009788c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009788c0 bytes 08a11e91
+ 009788c0 bytes 08612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f39e584f2d3c472e3741d588b80c6f6"></a>

### [`00979104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00979/00979104.md) → [`00979104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979104.md) FUN_00979104

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) · 呼出先 13件 [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00609f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00609/00609f20.md) [`008865b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00887/008879f4.md) [`0097cac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cac8.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 13件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00609f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/00609f20.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/008879f4.md) [`0097cac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cac8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.52% / 新版 92.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097918c",
      "incomplete_value": true,
      "site": "0097918c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097918c",
      "incomplete_value": true,
      "site": "0097918c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eee:8"
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
      "definition_site": "00979190",
      "incomplete_value": true,
      "site": "00979190",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00979190",
      "incomplete_value": true,
      "site": "00979190",
      "value": [
        "LOAD",
        "8",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009791ec",
      "incomplete_value": false,
      "site": "009791ec",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009791ec",
      "incomplete_value": false,
      "site": "009791ec",
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
            "const:8a8:8"
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
      "0097917c",
      "READ",
      [
        "storage",
        "002abeee",
        null,
        "string"
      ]
    ],
    [
      "00979180",
      "READ",
      [
        "storage",
        "002abef3",
        null,
        "string"
      ]
    ],
    [
      "009791ec",
      "DATA",
      [
        "storage",
        "00c0a8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097917c",
      "READ",
      [
        "storage",
        "002abef4",
        null,
        "string"
      ]
    ],
    [
      "00979180",
      "READ",
      [
        "storage",
        "002abef9",
        null,
        "string"
      ]
    ],
    [
      "009791ec",
      "DATA",
      [
        "storage",
        "00c0a958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00979174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00979/00979104.md#insn-00979174) · [`009791e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00979/00979104.md#insn-009791e4) · [`009791e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00979/00979104.md#insn-009791e8)
- 新版 `00979174`（命令位置の公開資料なし） · `009791e4`（命令位置の公開資料なし）

~~~diff
- 00979174 ["COPY", "tmp:0:8", ["const:eee:8"]]
- 00979174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00979174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00979174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00979174 ["COPY", "tmp:0:8", ["const:ef4:8"]]
+ 00979174 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00979174 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00979174 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00979174 bytes 29b93b91
+ 00979174 bytes 29d13b91
- 009791e4 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 009791e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009791e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009791e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009791e4 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 009791e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009791e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009791e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009791e4 bytes 08a12291
+ 009791e4 bytes 08612591
- 009791e8 ["INT_SUB", "register:40a8:8", ["register:40e8:8", "const:40:8"]]
- 009791e8 bytes b50301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21a7a2c01a00cada5088463e44e2a5bb"></a>

### [`00979584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00979/00979584.md) → [`00979584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979584.md) FUN_00979584

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) · 呼出先 15件 [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0087cfbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0087c/0087cfbc.md) [`008865b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00887/008879f4.md) [`0097cb78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cb78.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 15件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0087cfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087cfbc.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/008879f4.md) [`0097cb78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cb78.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.62% / 新版 94.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009796ac",
      "incomplete_value": false,
      "site": "009796ac",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009796ac",
      "incomplete_value": false,
      "site": "009796ac",
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
            "const:928:8"
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
      "00979610",
      "READ",
      [
        "storage",
        "002a5dd3",
        null,
        "string"
      ]
    ],
    [
      "00979614",
      "READ",
      [
        "storage",
        "002a5de3",
        null,
        "string"
      ]
    ],
    [
      "009796ac",
      "DATA",
      [
        "storage",
        "00c0a928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00979610",
      "READ",
      [
        "storage",
        "002a5dcc",
        null,
        "string"
      ]
    ],
    [
      "00979614",
      "READ",
      [
        "storage",
        "002a5ddc",
        null,
        "string"
      ]
    ],
    [
      "009796ac",
      "DATA",
      [
        "storage",
        "00c0a9d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009795f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00979/00979584.md#insn-009795f4) · [`009796a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00979/00979584.md#insn-009796a4)
- 新版 `009795f4`（命令位置の公開資料なし） · `009796a4`（命令位置の公開資料なし）

~~~diff
- 009795f4 ["COPY", "tmp:0:8", ["const:dd3:8"]]
- 009795f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009795f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009795f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009795f4 ["COPY", "tmp:0:8", ["const:dcc:8"]]
+ 009795f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009795f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009795f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009795f4 bytes 084d3791
+ 009795f4 bytes 08313791
- 009796a4 ["COPY", "tmp:0:8", ["const:928:8"]]
- 009796a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009796a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009796a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009796a4 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 009796a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009796a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009796a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009796a4 bytes 08a12491
+ 009796a4 bytes 08612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b86c7dc63cf5d5ac4ef8649b81c43a95"></a>

### [`00979d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00979/00979d0c.md) → [`00979d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979d0c.md) FUN_00979d0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) · 呼出先 13件 [`00976c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/00976c10.md) [`00976da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00976/00976da4.md) [`0097a1a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a1a8.md) [`0097b0c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097b/0097b0c8.md) [`0097cfcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cfcc.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 13件 [`00976c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976c10.md) [`00976da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976da4.md) [`0097a1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a1a8.md) [`0097b0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097b/0097b0c8.md) [`0097cfcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cfcc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.23% / 新版 99.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00979ea4",
      "incomplete_value": false,
      "site": "00979ea4",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00979ea4",
      "incomplete_value": false,
      "site": "00979ea4",
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
            "const:9a8:8"
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
      "00979ea4",
      "DATA",
      [
        "storage",
        "00c0a9a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00979f58",
      "READ",
      [
        "storage",
        "00c0a9d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00979ea4",
      "DATA",
      [
        "storage",
        "00c0aa58",
        null,
        "undefined *"
      ]
    ],
    [
      "00979f58",
      "READ",
      [
        "storage",
        "00c0aa80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00979e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00979/00979d0c.md#insn-00979e9c)
- 新版 `00979e9c`（命令位置の公開資料なし）

~~~diff
- 00979e9c ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 00979e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00979e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00979e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00979e9c ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 00979e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00979e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00979e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00979e9c bytes 08a12691
+ 00979e9c bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2c1904b95f91fb239ba3fcfe540d20a"></a>

### [`0097a22c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a22c.md) → [`0097a22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a22c.md) FUN_0097a22c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0086b704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0046fdf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fdf4.md) [`006ff834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ff/006ff834.md)
- 新版 呼出元 1件 [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046fdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fdf4.md) [`006ff834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ff/006ff834.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097a2c4",
      "incomplete_value": true,
      "site": "0097a2d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097a2c4",
      "incomplete_value": true,
      "site": "0097a2d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f79:8"
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
      "definition_site": "0097a2c4",
      "incomplete_value": true,
      "site": "0097a2d4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0097a2c4",
      "incomplete_value": true,
      "site": "0097a2d4",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097a2d8",
      "incomplete_value": true,
      "site": "0097a2e8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0097a2d8",
      "incomplete_value": true,
      "site": "0097a2e8",
      "value": [
        "LOAD",
        "16",
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
      "0097a2c4",
      "READ",
      [
        "storage",
        "00294f79",
        null,
        null
      ]
    ],
    [
      "0097a2c4",
      "READ",
      [
        "storage",
        "00294f89",
        null,
        null
      ]
    ],
    [
      "0097a2d8",
      "READ",
      [
        "storage",
        "00294f99",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0097a2c4",
      "READ",
      [
        "storage",
        "00295006",
        null,
        null
      ]
    ],
    [
      "0097a2c4",
      "READ",
      [
        "storage",
        "00295016",
        null,
        null
      ]
    ],
    [
      "0097a2d8",
      "READ",
      [
        "storage",
        "00295026",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097a2b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a22c.md#insn-0097a2b8) · [`0097a2bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a22c.md#insn-0097a2bc) · [`0097a390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a22c.md#insn-0097a390)
- 新版 `0097a2b8`（命令位置の公開資料なし） · `0097a2bc`（命令位置の公開資料なし） · `0097a390`（命令位置の公開資料なし）

~~~diff
- 0097a2b8 ["COPY", "register:4040:8", ["const:294000:8"]]
+ 0097a2b8 ["COPY", "register:4040:8", ["const:295000:8"]]
- 0097a2b8 bytes c8c8ffd0
+ 0097a2b8 bytes c8c8fff0
- 0097a2bc ["COPY", "tmp:0:8", ["const:f79:8"]]
- 0097a2bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097a2bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097a2bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097a2bc ["COPY", "tmp:0:8", ["const:6:8"]]
+ 0097a2bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097a2bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097a2bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097a2bc bytes 08e53d91
+ 0097a2bc bytes 08190091
- 0097a390 ["COPY", "tmp:0:8", ["const:b31:8"]]
- 0097a390 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0097a390 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0097a390 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0097a390 ["COPY", "tmp:0:8", ["const:bbe:8"]]
+ 0097a390 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0097a390 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0097a390 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0097a390 bytes 73c62c91
+ 0097a390 bytes 73fa2e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8efed9fae63ebf79c83b81c12c2db13"></a>

### [`0097a888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a888.md) → [`0097a888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a888.md) FUN_0097a888

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0097a22c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a22c.md) · 呼出先 22件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`004512c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00451/004512c0.md) [`00469128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469128.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md)
- 新版 呼出元 1件 [`0097a22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a22c.md) · 呼出先 22件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`004512c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00451/004512c0.md) [`00469128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469128.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097aa5c",
      "incomplete_value": true,
      "site": "0097aa7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ce7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097aa5c",
      "incomplete_value": true,
      "site": "0097aa7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cf0:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097aa5c",
      "incomplete_value": true,
      "site": "0097aa7c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0097aa5c",
      "incomplete_value": true,
      "site": "0097aa7c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097acac",
      "incomplete_value": true,
      "site": "0097acac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e8c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097acac",
      "incomplete_value": true,
      "site": "0097acac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dff:8"
              ]
            ]
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
      "0097aa5c",
      "READ",
      [
        "storage",
        "002a9cf0",
        null,
        "string"
      ]
    ],
    [
      "0097aa5c",
      "READ",
      [
        "storage",
        "002a9d00",
        null,
        "string"
      ]
    ],
    [
      "0097ab64",
      "PARAM",
      [
        "storage",
        "002950a6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0097aa5c",
      "READ",
      [
        "storage",
        "002a9ce7",
        null,
        "string"
      ]
    ],
    [
      "0097aa5c",
      "READ",
      [
        "storage",
        "002a9cf7",
        null,
        "string"
      ]
    ],
    [
      "0097ab64",
      "PARAM",
      [
        "storage",
        "00295133",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097aa54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a888.md#insn-0097aa54) · [`0097aaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a888.md#insn-0097aaa0) · [`0097ac38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a888.md#insn-0097ac38)
- 新版 `0097aa54`（命令位置の公開資料なし） · `0097aaa0`（命令位置の公開資料なし） · `0097ac38`（命令位置の公開資料なし）

~~~diff
- 0097aa54 ["COPY", "tmp:0:8", ["const:cf0:8"]]
- 0097aa54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097aa54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097aa54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097aa54 ["COPY", "tmp:0:8", ["const:ce7:8"]]
+ 0097aa54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097aa54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097aa54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097aa54 bytes 29c13391
+ 0097aa54 bytes 299d3391
- 0097aaa0 ["COPY", "tmp:0:8", ["const:a6:8"]]
- 0097aaa0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 0097aaa0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 0097aaa0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 0097aaa0 ["COPY", "tmp:0:8", ["const:133:8"]]
+ 0097aaa0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 0097aaa0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 0097aaa0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 0097aaa0 bytes b59a0291
+ 0097aaa0 bytes b5ce0491
- 0097ac38 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 0097ac38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097ac38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097ac38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097ac38 ["COPY", "tmp:0:8", ["const:e45:8"]]
+ 0097ac38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097ac38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097ac38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097ac38 bytes 29313991
+ 0097ac38 bytes 29153991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed7a7e56916ddcc4dd686463a32cf141"></a>

### [`0097af20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097af20.md) → [`0097af20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097af20.md) FUN_0097af20

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
      "definition_site": "0097af24",
      "incomplete_value": false,
      "site": "0097af28",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097af24",
      "incomplete_value": false,
      "site": "0097af28",
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
      "0097af28",
      "DATA",
      [
        "storage",
        "00c0a6d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0097af28",
      "DATA",
      [
        "storage",
        "00c0a788",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097af24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097af20.md#insn-0097af24)
- 新版 `0097af24`（命令位置の公開資料なし）

~~~diff
- 0097af24 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 0097af24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097af24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097af24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097af24 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 0097af24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097af24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097af24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097af24 bytes 08611b91
+ 0097af24 bytes 08211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a35f155d3979d0f0f04ab0cc16f3737"></a>

### [`0097af30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097af30.md) → [`0097af30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097af30.md) FUN_0097af30

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
      "definition_site": "0097af40",
      "incomplete_value": false,
      "site": "0097af48",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097af40",
      "incomplete_value": false,
      "site": "0097af48",
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
            "const:6d8:8"
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
      "0097af48",
      "DATA",
      [
        "storage",
        "00c0a6d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0097af48",
      "DATA",
      [
        "storage",
        "00c0a788",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097af40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097af30.md#insn-0097af40)
- 新版 `0097af40`（命令位置の公開資料なし）

~~~diff
- 0097af40 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 0097af40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097af40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097af40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097af40 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 0097af40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097af40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097af40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097af40 bytes 08611b91
+ 0097af40 bytes 08211e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6d4c368fb77708b6303626540469b5e"></a>

### [`0097b0c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097b/0097b0c8.md) → [`0097b0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097b/0097b0c8.md) FUN_0097b0c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009772ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00977/009772ec.md) [`00979d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00979/00979d0c.md) [`0097af6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097af6c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`009772ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00977/009772ec.md) [`00979d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979d0c.md) [`0097af6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097af6c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0097b0d4",
      "incomplete_value": false,
      "site": "0097b0d8",
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
      "definition_site": "0097b0d4",
      "incomplete_value": false,
      "site": "0097b0d8",
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
      "0097b0d4",
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
      "0097b0d4",
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

- 旧版 [`0097b0d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097b/0097b0c8.md#insn-0097b0d4)
- 新版 `0097b0d4`（命令位置の公開資料なし）

~~~diff
- 0097b0d4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0097b0d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0097b0d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0097b0d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0097b0d4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0097b0d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0097b0d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0097b0d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0097b0d4 bytes 00280c91
+ 0097b0d4 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aebf5e5ea55689ae1d0a8a6af94630b"></a>

### [`0097c214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c214.md) → [`0097c214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c214.md) FUN_0097c214

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00977d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00977/00977d04.md) [`00a40cb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a40/00a40cb0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00977d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00977/00977d04.md) [`00a40cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a40/00a40cb0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0097c220",
      "incomplete_value": true,
      "site": "0097c224",
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
      "definition_site": "0097c220",
      "incomplete_value": true,
      "site": "0097c224",
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
      "0097c220",
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
      "0097c220",
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

- 旧版 [`0097c220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c214.md#insn-0097c220)
- 新版 `0097c220`（命令位置の公開資料なし）

~~~diff
- 0097c220 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0097c220 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0097c220 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0097c220 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0097c220 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0097c220 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0097c220 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0097c220 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0097c220 bytes 00280c91
+ 0097c220 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-083d290aa743814b8cdeae335db7d4ec"></a>

### [`0097c228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c228.md) → [`0097c228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c228.md) FUN_0097c228

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0097c240",
      "incomplete_value": false,
      "site": "0097c244",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c240",
      "incomplete_value": false,
      "site": "0097c244",
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
            "const:728:8"
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
      "0097c244",
      "DATA",
      [
        "storage",
        "00c0a728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c244",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c228.md#insn-0097c240)
- 新版 `0097c240`（命令位置の公開資料なし）

~~~diff
- 0097c240 ["COPY", "tmp:0:8", ["const:728:8"]]
- 0097c240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097c240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097c240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097c240 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0097c240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097c240 bytes 08a11c91
+ 0097c240 bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86b90ecec298201fec88a2d70178d780"></a>

### [`0097c2b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c2b8.md) → [`0097c2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c2b8.md) FUN_0097c2b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0097c2d0",
      "incomplete_value": false,
      "site": "0097c2d4",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c2d0",
      "incomplete_value": false,
      "site": "0097c2d4",
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
            "const:728:8"
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
      "0097c2d4",
      "DATA",
      [
        "storage",
        "00c0a728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c2d4",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c2b8.md#insn-0097c2d0)
- 新版 `0097c2d0`（命令位置の公開資料なし）

~~~diff
- 0097c2d0 ["COPY", "tmp:0:8", ["const:728:8"]]
- 0097c2d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097c2d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097c2d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097c2d0 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0097c2d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c2d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c2d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097c2d0 bytes 08a11c91
+ 0097c2d0 bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0445fbeed5491f4faa5d08d0f9d7a16"></a>

### [`0097c344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c344.md) → [`0097c344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c344.md) FUN_0097c344

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0097c360",
      "incomplete_value": false,
      "site": "0097c370",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c360",
      "incomplete_value": false,
      "site": "0097c370",
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
            "const:728:8"
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
      "0097c370",
      "DATA",
      [
        "storage",
        "00c0a728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c370",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c344.md#insn-0097c360)
- 新版 `0097c360`（命令位置の公開資料なし）

~~~diff
- 0097c360 ["COPY", "tmp:0:8", ["const:728:8"]]
- 0097c360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097c360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097c360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097c360 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0097c360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097c360 bytes 08a11c91
+ 0097c360 bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6810f179548163723e4945668bca7793"></a>

### [`0097c3f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c3f4.md) → [`0097c3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c3f4.md) FUN_0097c3f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

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
      "definition_site": "0097c404",
      "incomplete_value": false,
      "site": "0097c40c",
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
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c404",
      "incomplete_value": false,
      "site": "0097c40c",
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
            "const:728:8"
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
      "0097c40c",
      "DATA",
      [
        "storage",
        "00c0a728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c40c",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c3f4.md#insn-0097c404)
- 新版 `0097c404`（命令位置の公開資料なし）

~~~diff
- 0097c404 ["COPY", "tmp:0:8", ["const:728:8"]]
- 0097c404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097c404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097c404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097c404 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0097c404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097c404 bytes 08a11c91
+ 0097c404 bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-239839cd062422522a8152a74bd61c3f"></a>

### [`0097c764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c764.md) → [`0097c764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c764.md) FUN_0097c764

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
      "definition_site": "0097c770",
      "incomplete_value": false,
      "site": "0097c77c",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c770",
      "incomplete_value": false,
      "site": "0097c77c",
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
            "const:7a8:8"
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
      "0097c77c",
      "DATA",
      [
        "storage",
        "00c0a7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c77c",
      "DATA",
      [
        "storage",
        "00c0a858",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c764.md#insn-0097c770)
- 新版 `0097c770`（命令位置の公開資料なし）

~~~diff
- 0097c770 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 0097c770 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0097c770 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0097c770 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0097c770 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 0097c770 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0097c770 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0097c770 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0097c770 bytes 4aa11e91
+ 0097c770 bytes 4a612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29ce138fee9d79320b75a67ceaece5f8"></a>

### [`0097c7a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c7a8.md) → [`0097c7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c7a8.md) FUN_0097c7a8

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
      "definition_site": "0097c7c0",
      "incomplete_value": false,
      "site": "0097c7cc",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c7c0",
      "incomplete_value": false,
      "site": "0097c7cc",
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
            "const:7a8:8"
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
      "0097c7cc",
      "DATA",
      [
        "storage",
        "00c0a7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c7cc",
      "DATA",
      [
        "storage",
        "00c0a858",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c7a8.md#insn-0097c7c0)
- 新版 `0097c7c0`（命令位置の公開資料なし）

~~~diff
- 0097c7c0 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 0097c7c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097c7c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097c7c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097c7c0 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 0097c7c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c7c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c7c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097c7c0 bytes 08a11e91
+ 0097c7c0 bytes 08612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6750dd8f5570a1bb77d134b8360f7da3"></a>

### [`0097c804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c804.md) → [`0097c804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c804.md) FUN_0097c804

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
      "definition_site": "0097c830",
      "incomplete_value": false,
      "site": "0097c830",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c830",
      "incomplete_value": false,
      "site": "0097c830",
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
            "const:7a8:8"
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
      "0097c830",
      "DATA",
      [
        "storage",
        "00c0a7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c830",
      "DATA",
      [
        "storage",
        "00c0a858",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c804.md#insn-0097c828)
- 新版 `0097c828`（命令位置の公開資料なし）

~~~diff
- 0097c828 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 0097c828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097c828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097c828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097c828 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 0097c828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097c828 bytes 08a11e91
+ 0097c828 bytes 08612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf2bef86258263b88afe7b1bc643ee73"></a>

### [`0097c88c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c88c.md) → [`0097c88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c88c.md) FUN_0097c88c

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
      "definition_site": "0097c8a8",
      "incomplete_value": false,
      "site": "0097c8a8",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c8a8",
      "incomplete_value": false,
      "site": "0097c8a8",
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
            "const:7a8:8"
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
      "0097c8a8",
      "DATA",
      [
        "storage",
        "00c0a7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c8a8",
      "DATA",
      [
        "storage",
        "00c0a858",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097c88c.md#insn-0097c8a4)
- 新版 `0097c8a4`（命令位置の公開資料なし）

~~~diff
- 0097c8a4 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 0097c8a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097c8a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097c8a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097c8a4 ["COPY", "tmp:0:8", ["const:858:8"]]
+ 0097c8a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097c8a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097c8a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097c8a4 bytes 29a11e91
+ 0097c8a4 bytes 29612191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96e065e1b1e461fc29c075385b0393e0"></a>

### [`0097ca28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097ca28.md) → [`0097ca28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097ca28.md) FUN_0097ca28

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
      "definition_site": "0097ca3c",
      "incomplete_value": false,
      "site": "0097ca40",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097ca3c",
      "incomplete_value": false,
      "site": "0097ca40",
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
            "const:828:8"
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
      "0097ca40",
      "DATA",
      [
        "storage",
        "00c0a828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097ca40",
      "DATA",
      [
        "storage",
        "00c0a8d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097ca3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097ca28.md#insn-0097ca3c)
- 新版 `0097ca3c`（命令位置の公開資料なし）

~~~diff
- 0097ca3c ["COPY", "tmp:0:8", ["const:828:8"]]
- 0097ca3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097ca3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097ca3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097ca3c ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 0097ca3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ca3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ca3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097ca3c bytes 08a12091
+ 0097ca3c bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecd4a6aea28a74656efdc241dde70766"></a>

### [`0097ca4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097ca4c.md) → [`0097ca4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097ca4c.md) FUN_0097ca4c

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
      "definition_site": "0097ca50",
      "incomplete_value": false,
      "site": "0097ca54",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097ca50",
      "incomplete_value": false,
      "site": "0097ca54",
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
            "const:828:8"
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
      "0097ca54",
      "DATA",
      [
        "storage",
        "00c0a828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097ca54",
      "DATA",
      [
        "storage",
        "00c0a8d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097ca50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097ca4c.md#insn-0097ca50)
- 新版 `0097ca50`（命令位置の公開資料なし）

~~~diff
- 0097ca50 ["COPY", "tmp:0:8", ["const:828:8"]]
- 0097ca50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097ca50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097ca50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097ca50 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 0097ca50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ca50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ca50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097ca50 bytes 08a12091
+ 0097ca50 bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba2019d5f903821ca29d06476571aba5"></a>

### [`0097ca94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097ca94.md) → [`0097ca94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097ca94.md) FUN_0097ca94

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
      "definition_site": "0097caa8",
      "incomplete_value": false,
      "site": "0097caac",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097caa8",
      "incomplete_value": false,
      "site": "0097caac",
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
            "const:8a8:8"
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
      "0097caac",
      "DATA",
      [
        "storage",
        "00c0a8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097caac",
      "DATA",
      [
        "storage",
        "00c0a958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097caa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097ca94.md#insn-0097caa8)
- 新版 `0097caa8`（命令位置の公開資料なし）

~~~diff
- 0097caa8 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 0097caa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097caa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097caa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097caa8 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 0097caa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097caa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097caa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097caa8 bytes 08a12291
+ 0097caa8 bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06276ce3303ffdacd9206c0accaaba8f"></a>

### [`0097cab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cab8.md) → [`0097cab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cab8.md) FUN_0097cab8

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
      "definition_site": "0097cabc",
      "incomplete_value": false,
      "site": "0097cac0",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097cabc",
      "incomplete_value": false,
      "site": "0097cac0",
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
            "const:8a8:8"
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
      "0097cac0",
      "DATA",
      [
        "storage",
        "00c0a8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097cac0",
      "DATA",
      [
        "storage",
        "00c0a958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097cabc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cab8.md#insn-0097cabc)
- 新版 `0097cabc`（命令位置の公開資料なし）

~~~diff
- 0097cabc ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 0097cabc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097cabc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097cabc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097cabc ["COPY", "tmp:0:8", ["const:958:8"]]
+ 0097cabc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cabc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cabc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097cabc bytes 08a12291
+ 0097cabc bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b0942326a36a46b0af9823315ad2aa9"></a>

### [`0097cb44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cb44.md) → [`0097cb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cb44.md) FUN_0097cb44

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
      "definition_site": "0097cb58",
      "incomplete_value": false,
      "site": "0097cb5c",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097cb58",
      "incomplete_value": false,
      "site": "0097cb5c",
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
            "const:928:8"
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
      "0097cb5c",
      "DATA",
      [
        "storage",
        "00c0a928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097cb5c",
      "DATA",
      [
        "storage",
        "00c0a9d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097cb58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cb44.md#insn-0097cb58)
- 新版 `0097cb58`（命令位置の公開資料なし）

~~~diff
- 0097cb58 ["COPY", "tmp:0:8", ["const:928:8"]]
- 0097cb58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097cb58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097cb58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097cb58 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 0097cb58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cb58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cb58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097cb58 bytes 08a12491
+ 0097cb58 bytes 08612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e1684b1a454778ad508eb2203509f30"></a>

### [`0097cb68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cb68.md) → [`0097cb68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cb68.md) FUN_0097cb68

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
      "definition_site": "0097cb6c",
      "incomplete_value": false,
      "site": "0097cb70",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097cb6c",
      "incomplete_value": false,
      "site": "0097cb70",
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
      "0097cb70",
      "DATA",
      [
        "storage",
        "00c0a928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097cb70",
      "DATA",
      [
        "storage",
        "00c0a9d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097cb6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cb68.md#insn-0097cb6c)
- 新版 `0097cb6c`（命令位置の公開資料なし）

~~~diff
- 0097cb6c ["COPY", "tmp:0:8", ["const:928:8"]]
- 0097cb6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097cb6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097cb6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097cb6c ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 0097cb6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cb6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cb6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097cb6c bytes 08a12491
+ 0097cb6c bytes 08612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eb2eecb79c4a1d782a32f58dd13bb57"></a>

### [`0097cc18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cc18.md) → [`0097cc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cc18.md) FUN_0097cc18

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0097cc30",
      "incomplete_value": false,
      "site": "0097cc40",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097cc30",
      "incomplete_value": false,
      "site": "0097cc40",
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
      "0097cc40",
      "DATA",
      [
        "storage",
        "00c0a9a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097cc40",
      "DATA",
      [
        "storage",
        "00c0aa58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097cc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cc18.md#insn-0097cc30)
- 新版 `0097cc30`（命令位置の公開資料なし）

~~~diff
- 0097cc30 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 0097cc30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097cc30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097cc30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097cc30 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 0097cc30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cc30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cc30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097cc30 bytes 08a12691
+ 0097cc30 bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c221b434657de49f3e2c19bf167794c1"></a>

### [`0097cca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cca8.md) → [`0097cca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cca8.md) FUN_0097cca8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "0097ccc0",
      "incomplete_value": false,
      "site": "0097ccd0",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097ccc0",
      "incomplete_value": false,
      "site": "0097ccd0",
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
      "0097ccd0",
      "DATA",
      [
        "storage",
        "00c0a9a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097ccd0",
      "DATA",
      [
        "storage",
        "00c0aa58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097ccc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cca8.md#insn-0097ccc0)
- 新版 `0097ccc0`（命令位置の公開資料なし）

~~~diff
- 0097ccc0 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 0097ccc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097ccc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097ccc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097ccc0 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 0097ccc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ccc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ccc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097ccc0 bytes 08a12691
+ 0097ccc0 bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69a16801684ced96e63df139622740a6"></a>

### [`0097cd34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cd34.md) → [`0097cd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cd34.md) FUN_0097cd34

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0097cd64",
      "incomplete_value": false,
      "site": "0097cd64",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097cd64",
      "incomplete_value": false,
      "site": "0097cd64",
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
            "const:9a8:8"
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
      "0097cd64",
      "DATA",
      [
        "storage",
        "00c0a9a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097cd64",
      "DATA",
      [
        "storage",
        "00c0aa58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097cd5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097c/0097cd34.md#insn-0097cd5c)
- 新版 `0097cd5c`（命令位置の公開資料なし）

~~~diff
- 0097cd5c ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 0097cd5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097cd5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097cd5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097cd5c ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 0097cd5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cd5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cd5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097cd5c bytes 08a12691
+ 0097cd5c bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23e671b0079fdfa0cc830c26286c9758"></a>

### [`0097d128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097d128.md) → [`0097d128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097d128.md) _INIT_191

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
      "definition_site": "0097d164",
      "incomplete_value": true,
      "site": "0097d180",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0097d164",
      "incomplete_value": true,
      "site": "0097d180",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0097d1c8",
      "incomplete_value": true,
      "site": "0097d1e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0097d1c8",
      "incomplete_value": true,
      "site": "0097d1e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0097d224",
      "incomplete_value": true,
      "site": "0097d268",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0097d224",
      "incomplete_value": true,
      "site": "0097d268",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0097d164",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0097d188",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0097d1a8",
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
      "0097d164",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0097d188",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0097d1a8",
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

- 旧版 [`0097d154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097d128.md#insn-0097d154) · [`0097d15c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097d128.md#insn-0097d15c)
- 新版 `0097d154`（命令位置の公開資料なし） · `0097d15c`（命令位置の公開資料なし）

~~~diff
- 0097d154 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 0097d154 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0097d154 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0097d154 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0097d154 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 0097d154 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0097d154 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0097d154 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0097d154 bytes 73022391
+ 0097d154 bytes 73022691
- 0097d15c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0097d15c bytes 49c9ffd0
+ 0097d15c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0097d15c bytes 49c9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7afa48ee24ef654e340ac78c02121d39"></a>

### [`0097d4b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097d4b8.md) → [`0097d4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097d4b8.md) FUN_0097d4b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005846a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00584/005846a8.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`005857bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00585/005857bc.md) [`0097db1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097db1c.md) [`00980108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00980/00980108.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`005846a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00584/005846a8.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`005857bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00585/005857bc.md) [`0097db1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097db1c.md) [`00980108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980108.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097d624",
      "incomplete_value": true,
      "site": "0097d634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:356:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097d624",
      "incomplete_value": true,
      "site": "0097d634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ea:8"
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
      "definition_site": "0097d638",
      "incomplete_value": true,
      "site": "0097d638",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0097d638",
      "incomplete_value": true,
      "site": "0097d638",
      "value": [
        "LOAD",
        "8",
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
      "0097d624",
      "READ",
      [
        "storage",
        "002a83ea",
        null,
        "string"
      ]
    ],
    [
      "0097d62c",
      "READ",
      [
        "storage",
        "002a83f1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0097d624",
      "READ",
      [
        "storage",
        "002a8356",
        null,
        "string"
      ]
    ],
    [
      "0097d62c",
      "READ",
      [
        "storage",
        "002a835d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097d61c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097d4b8.md#insn-0097d61c)
- 新版 `0097d61c`（命令位置の公開資料なし）

~~~diff
- 0097d61c ["COPY", "tmp:0:8", ["const:3ea:8"]]
- 0097d61c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0097d61c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0097d61c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0097d61c ["COPY", "tmp:0:8", ["const:356:8"]]
+ 0097d61c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0097d61c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0097d61c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0097d61c bytes 4aa90f91
+ 0097d61c bytes 4a590d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ea6115c9b4eb3528b6661035d3e1fe2"></a>

### [`0097db1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097db1c.md) → [`0097db1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097db1c.md) FUN_0097db1c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00586014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00586/00586014.md) [`0058717c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00587/0058717c.md) [`0097d4b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097d4b8.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`005859d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00585/005859d8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 3件 [`00586014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00586/00586014.md) [`0058717c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00587/0058717c.md) [`0097d4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097d4b8.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`005859d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00585/005859d8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.53% / 新版 98.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097db88",
      "incomplete_value": true,
      "site": "0097db88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097db88",
      "incomplete_value": true,
      "site": "0097db88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:346:8"
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
      "0097db70",
      "READ",
      [
        "storage",
        "002a9346",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0097db70",
      "READ",
      [
        "storage",
        "002a92b2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097db6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097db1c.md#insn-0097db6c)
- 新版 `0097db6c`（命令位置の公開資料なし）

~~~diff
- 0097db6c ["COPY", "tmp:0:8", ["const:346:8"]]
- 0097db6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097db6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097db6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097db6c ["COPY", "tmp:0:8", ["const:2b2:8"]]
+ 0097db6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097db6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097db6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097db6c bytes 29190d91
+ 0097db6c bytes 29c90a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f79d5db8b85fa364f04ffa87eb47de6a"></a>

### [`0097deec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097deec.md) → [`0097deec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097deec.md) FUN_0097deec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`009784b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00978/009784b4.md) [`00978d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00978/00978d0c.md) [`0097ea24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097ea24.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00728090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00728/00728090.md) [`00973ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973ae8.md) [`00973af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973af8.md) [`0097e4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097e4e8.md)
- 新版 呼出元 3件 [`009784b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009784b4.md) [`00978d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/00978d0c.md) [`0097ea24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ea24.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`00973ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973ae8.md) [`00973af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973af8.md) [`0097e4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097e4e8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097e074",
      "incomplete_value": false,
      "site": "0097e080",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097e074",
      "incomplete_value": false,
      "site": "0097e080",
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
            "const:a38:8"
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
      "definition_site": "0097e134",
      "incomplete_value": false,
      "site": "0097e140",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097e134",
      "incomplete_value": false,
      "site": "0097e140",
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
            "const:ab8:8"
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
      "0097e080",
      "DATA",
      [
        "storage",
        "00c0aa38",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e140",
      "DATA",
      [
        "storage",
        "00c0aab8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e1d0",
      "READ",
      [
        "storage",
        "00c0aae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097e080",
      "DATA",
      [
        "storage",
        "00c0aae8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e140",
      "DATA",
      [
        "storage",
        "00c0ab68",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e1d0",
      "READ",
      [
        "storage",
        "00c0ab90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097e074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097deec.md#insn-0097e074) · [`0097e134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097deec.md#insn-0097e134)
- 新版 `0097e074`（命令位置の公開資料なし） · `0097e134`（命令位置の公開資料なし）

~~~diff
- 0097e074 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 0097e074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097e074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097e074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097e074 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 0097e074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097e074 bytes 08e12891
+ 0097e074 bytes 08a12b91
- 0097e134 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 0097e134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097e134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097e134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097e134 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 0097e134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097e134 bytes 08e12a91
+ 0097e134 bytes 08a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-588950c931bf273cd5503fd5c3ae2f40"></a>

### [`0097e4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097e4e8.md) → [`0097e4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097e4e8.md) FUN_0097e4e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0071bdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0071b/0071bdc8.md) [`0097deec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097d/0097deec.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/00576268.md) [`00587858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00587/00587858.md) [`0076b910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0076b/0076b910.md)
- 新版 呼出元 2件 [`0071bdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071bdc8.md) [`0097deec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097deec.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`00587858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00587/00587858.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097e5b8",
      "incomplete_value": false,
      "site": "0097e5bc",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0097e5b8",
      "incomplete_value": false,
      "site": "0097e5bc",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097e648",
      "incomplete_value": false,
      "site": "0097e648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097e648",
      "incomplete_value": false,
      "site": "0097e648",
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
            "const:fb8:8"
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
      "definition_site": "0097e758",
      "incomplete_value": false,
      "site": "0097e758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097e758",
      "incomplete_value": false,
      "site": "0097e758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "0097e5bc",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e648",
      "DATA",
      [
        "storage",
        "00c0afb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e6bc",
      "READ",
      [
        "storage",
        "00c0afe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097e5bc",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e648",
      "DATA",
      [
        "storage",
        "00c0b068",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e6bc",
      "READ",
      [
        "storage",
        "00c0b090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097e5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097e4e8.md#insn-0097e5b0) · [`0097e63c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097e4e8.md#insn-0097e63c) · [`0097e640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097e4e8.md#insn-0097e640)
- 新版 `0097e5b0`（命令位置の公開資料なし） · `0097e63c`（命令位置の公開資料なし） · `0097e640`（命令位置の公開資料なし）

~~~diff
- 0097e5b0 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0097e5b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097e5b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097e5b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097e5b0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0097e5b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e5b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e5b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097e5b0 bytes 08412591
+ 0097e5b0 bytes 08012891
- 0097e63c ["COPY", "register:4040:8", ["const:c0a000:8"]]
+ 0097e63c ["COPY", "register:4040:8", ["const:c0b000:8"]]
- 0097e63c bytes 68140090
+ 0097e63c bytes 681400b0
- 0097e640 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0097e640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097e640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097e640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097e640 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 0097e640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097e640 bytes 08e13e91
+ 0097e640 bytes 08a10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d157fe1acd077925e9d6c819caa311fc"></a>

### [`0097ea24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097ea24.md) → [`0097ea24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ea24.md) FUN_0097ea24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00977c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00977/00977c00.md) · 呼出先 15件 [`00728090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00728/00728090.md) [`00973ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973ae8.md) [`00973af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973af0.md) [`00975098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975098.md) [`00975120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00975/00975120.md)
- 新版 呼出元 1件 [`00977c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00977/00977c00.md) · 呼出先 15件 [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`00973ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973ae8.md) [`00973af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973af0.md) [`00975098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975098.md) [`00975120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.12% / 新版 96.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097ea8c",
      "incomplete_value": true,
      "site": "0097ea8c",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097ea8c",
      "incomplete_value": true,
      "site": "0097ea8c",
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
            "const:b38:8"
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
      "0097ea8c",
      "DATA",
      [
        "storage",
        "00c0ab38",
        null,
        "undefined *"
      ]
    ],
    [
      "0097eae0",
      "DATA",
      [
        "storage",
        "00c0abb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097eaf8",
      "DATA",
      [
        "storage",
        "00c0ac38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097ea8c",
      "DATA",
      [
        "storage",
        "00c0abe8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097eae0",
      "DATA",
      [
        "storage",
        "00c0ac68",
        null,
        "undefined *"
      ]
    ],
    [
      "0097eaf8",
      "DATA",
      [
        "storage",
        "00c0ace8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097ea84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097ea24.md#insn-0097ea84) · [`0097eadc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097ea24.md#insn-0097eadc) · [`0097eaf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097ea24.md#insn-0097eaf4)
- 新版 `0097ea84`（命令位置の公開資料なし） · `0097eadc`（命令位置の公開資料なし） · `0097eaf4`（命令位置の公開資料なし）

~~~diff
- 0097ea84 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 0097ea84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097ea84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097ea84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097ea84 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 0097ea84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ea84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ea84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097ea84 bytes 08e12c91
+ 0097ea84 bytes 08a12f91
- 0097eadc ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 0097eadc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097eadc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097eadc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097eadc ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 0097eadc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097eadc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097eadc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097eadc bytes 08e12e91
+ 0097eadc bytes 08a13191
- 0097eaf4 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 0097eaf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097eaf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097eaf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097eaf4 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 0097eaf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097eaf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097eaf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097eaf4 bytes 08e13091
+ 0097eaf4 bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92291079b2116a1795c14ccba7142cc0"></a>

### [`0097ec84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097ec84.md) → [`0097ec84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ec84.md) FUN_0097ec84

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0071b838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0071b/0071b838.md) [`0071c4c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0071c/0071c4c8.md) [`009785f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00978/009785f0.md) [`0097ea24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097ea24.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/00576268.md) [`005866f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00586/005866f0.md) [`0076b910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0076b/0076b910.md)
- 新版 呼出元 4件 [`0071b838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071b838.md) [`0071c4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071c4c8.md) [`009785f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009785f0.md) [`0097ea24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ea24.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`005866f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00586/005866f0.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.11% / 新版 97.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097ed48",
      "incomplete_value": false,
      "site": "0097ed4c",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0097ed48",
      "incomplete_value": false,
      "site": "0097ed4c",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097edd8",
      "incomplete_value": false,
      "site": "0097edd8",
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
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097edd8",
      "incomplete_value": false,
      "site": "0097edd8",
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
            "const:eb8:8"
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
      "definition_site": "0097eee8",
      "incomplete_value": false,
      "site": "0097eee8",
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
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097eee8",
      "incomplete_value": false,
      "site": "0097eee8",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0097ed4c",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ],
    [
      "0097edd8",
      "DATA",
      [
        "storage",
        "00c0aeb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097ee4c",
      "READ",
      [
        "storage",
        "00c0aee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097ed4c",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0097edd8",
      "DATA",
      [
        "storage",
        "00c0af68",
        null,
        "undefined *"
      ]
    ],
    [
      "0097ee4c",
      "READ",
      [
        "storage",
        "00c0af90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097ed40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097ec84.md#insn-0097ed40) · [`0097edd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097ec84.md#insn-0097edd0) · [`0097eee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097e/0097ec84.md#insn-0097eee0)
- 新版 `0097ed40`（命令位置の公開資料なし） · `0097edd0`（命令位置の公開資料なし） · `0097eee0`（命令位置の公開資料なし）

~~~diff
- 0097ed40 ["COPY", "tmp:0:8", ["const:950:8"]]
- 0097ed40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097ed40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097ed40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097ed40 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0097ed40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ed40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ed40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097ed40 bytes 08412591
+ 0097ed40 bytes 08012891
- 0097edd0 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 0097edd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097edd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097edd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097edd0 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 0097edd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097edd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097edd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097edd0 bytes 08e13a91
+ 0097edd0 bytes 08a13d91
- 0097eee0 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0097eee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097eee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097eee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097eee0 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 0097eee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097eee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097eee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097eee0 bytes 08e13c91
+ 0097eee0 bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e0dba4bb2024115d445f4c549e12f65"></a>

### [`0097f1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097f1b0.md) → [`0097f1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f1b0.md) FUN_0097f1b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00979d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00979/00979d0c.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`00728090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00728/00728090.md) [`00973ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00973/00973ae8.md) [`0097499c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00974/0097499c.md) [`0097f740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097f740.md)
- 新版 呼出元 1件 [`00979d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979d0c.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`00973ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973ae8.md) [`0097499c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00974/0097499c.md) [`0097f740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f740.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097f30c",
      "incomplete_value": false,
      "site": "0097f30c",
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
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097f30c",
      "incomplete_value": false,
      "site": "0097f30c",
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
            "const:cb8:8"
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
      "definition_site": "0097f3cc",
      "incomplete_value": false,
      "site": "0097f3cc",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097f3cc",
      "incomplete_value": false,
      "site": "0097f3cc",
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
            "const:d38:8"
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
      "0097f30c",
      "DATA",
      [
        "storage",
        "00c0acb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f3cc",
      "DATA",
      [
        "storage",
        "00c0ad38",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f454",
      "READ",
      [
        "storage",
        "00c0ad60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097f30c",
      "DATA",
      [
        "storage",
        "00c0ad68",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f3cc",
      "DATA",
      [
        "storage",
        "00c0ade8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f454",
      "READ",
      [
        "storage",
        "00c0ae10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097f304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097f1b0.md#insn-0097f304) · [`0097f3c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097f1b0.md#insn-0097f3c4)
- 新版 `0097f304`（命令位置の公開資料なし） · `0097f3c4`（命令位置の公開資料なし）

~~~diff
- 0097f304 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 0097f304 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097f304 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097f304 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097f304 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 0097f304 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097f304 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097f304 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097f304 bytes 29e13291
+ 0097f304 bytes 29a13591
- 0097f3c4 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0097f3c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097f3c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097f3c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097f3c4 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 0097f3c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097f3c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097f3c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097f3c4 bytes 29e13491
+ 0097f3c4 bytes 29a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20739be3ef08a3df87fc2fe4c18a53b4"></a>

### [`0097f740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097f740.md) → [`0097f740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f740.md) FUN_0097f740

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0071cb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0071c/0071cb00.md) [`0097f1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097f1b0.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00576/00576268.md) [`00584fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00584/00584fe0.md) [`0076b910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0076b/0076b910.md)
- 新版 呼出元 2件 [`0071cb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071cb00.md) [`0097f1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f1b0.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`00584fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00584/00584fe0.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.11% / 新版 97.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097f804",
      "incomplete_value": false,
      "site": "0097f808",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:a00:8"
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
      "definition_site": "0097f804",
      "incomplete_value": false,
      "site": "0097f808",
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
                "const:bf0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097f894",
      "incomplete_value": false,
      "site": "0097f894",
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
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097f894",
      "incomplete_value": false,
      "site": "0097f894",
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
            "const:db8:8"
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
      "definition_site": "0097f9a4",
      "incomplete_value": false,
      "site": "0097f9a4",
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
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097f9a4",
      "incomplete_value": false,
      "site": "0097f9a4",
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
            "const:e38:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0097f808",
      "DATA",
      [
        "storage",
        "00bf0960",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f894",
      "DATA",
      [
        "storage",
        "00c0adb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f908",
      "READ",
      [
        "storage",
        "00c0ade0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097f808",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f894",
      "DATA",
      [
        "storage",
        "00c0ae68",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f908",
      "READ",
      [
        "storage",
        "00c0ae90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097f7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097f740.md#insn-0097f7fc) · [`0097f88c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097f740.md#insn-0097f88c) · [`0097f99c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097f/0097f740.md#insn-0097f99c)
- 新版 `0097f7fc`（命令位置の公開資料なし） · `0097f88c`（命令位置の公開資料なし） · `0097f99c`（命令位置の公開資料なし）

~~~diff
- 0097f7fc ["COPY", "tmp:0:8", ["const:950:8"]]
- 0097f7fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097f7fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097f7fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097f7fc ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0097f7fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097f7fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097f7fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097f7fc bytes 08412591
+ 0097f7fc bytes 08012891
- 0097f88c ["COPY", "tmp:0:8", ["const:db8:8"]]
- 0097f88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097f88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097f88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097f88c ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 0097f88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097f88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097f88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097f88c bytes 08e13691
+ 0097f88c bytes 08a13991
- 0097f99c ["COPY", "tmp:0:8", ["const:e38:8"]]
- 0097f99c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097f99c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097f99c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097f99c ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0097f99c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097f99c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097f99c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097f99c bytes 08e13891
+ 0097f99c bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

