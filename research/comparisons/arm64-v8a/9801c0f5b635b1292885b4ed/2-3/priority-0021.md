# v16.0.1 → v16.0.2 · 最優先の変更候補 (21)

[一覧の目次](README.md)

<a id="compare-df1ded722f657f69371223aa877f315c"></a>

### [`005a0954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0954.md) → [`005a0994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a0994.md) FUN_005a0994

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a09c0",
      "incomplete_value": false,
      "site": "005a09c4",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
      "definition_site": "005a0980",
      "incomplete_value": false,
      "site": "005a0984",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a09c4",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a09c4",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0954.md#insn-005a0970) · [`005a0978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0954.md#insn-005a0978) · [`005a0990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0954.md#insn-005a0990)
- 新版 `005a09b0`（命令位置の公開資料なし） · `005a09b8`（命令位置の公開資料なし） · `005a09d0`（命令位置の公開資料なし）

~~~diff
- 005a0970 ["INT_ADD", "register:40f0:8", ["const:5a0970:8", "const:4:8"]]
- 005a0970 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a09b0 ["INT_ADD", "register:40f0:8", ["const:5a09b0:8", "const:4:8"]]
+ 005a09b0 ["CALL", null, ["callee:00c57f80:8"]]
- 005a0970 bytes 50dd1a94
+ 005a09b0 bytes 74dd1a94
- 005a0978 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005a0978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a0978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a0978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a09b8 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005a09b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a09b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a09b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a0978 bytes 08412891
+ 005a09b8 bytes 08812b91
- 005a0990 ["INT_ADD", "register:40f0:8", ["const:5a0990:8", "const:4:8"]]
- 005a0990 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a09d0 ["INT_ADD", "register:40f0:8", ["const:5a09d0:8", "const:4:8"]]
+ 005a09d0 ["CALL", null, ["callee:00c57f80:8"]]
- 005a0990 bytes 48dd1a94
+ 005a09d0 bytes 6cdd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42b26a444882b4359b4c1308f2937536"></a>

### [`005a09b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a09b8.md) → [`005a09f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a09f8.md) FUN_005a09f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a0a24",
      "incomplete_value": false,
      "site": "005a0a28",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
      "definition_site": "005a09e4",
      "incomplete_value": false,
      "site": "005a09e8",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a0a28",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a0a28",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a09d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a09b8.md#insn-005a09d4) · [`005a09dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a09b8.md#insn-005a09dc) · [`005a09f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a09b8.md#insn-005a09f4)
- 新版 `005a0a14`（命令位置の公開資料なし） · `005a0a1c`（命令位置の公開資料なし） · `005a0a34`（命令位置の公開資料なし）

~~~diff
- 005a09d4 ["INT_ADD", "register:40f0:8", ["const:5a09d4:8", "const:4:8"]]
- 005a09d4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a0a14 ["INT_ADD", "register:40f0:8", ["const:5a0a14:8", "const:4:8"]]
+ 005a0a14 ["CALL", null, ["callee:00c57f80:8"]]
- 005a09d4 bytes 37dd1a94
+ 005a0a14 bytes 5bdd1a94
- 005a09dc ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005a09dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a09dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a09dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0a1c ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005a0a1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0a1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0a1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a09dc bytes 08412891
+ 005a0a1c bytes 08812b91
- 005a09f4 ["INT_ADD", "register:40f0:8", ["const:5a09f4:8", "const:4:8"]]
- 005a09f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a0a34 ["INT_ADD", "register:40f0:8", ["const:5a0a34:8", "const:4:8"]]
+ 005a0a34 ["CALL", null, ["callee:00c57f80:8"]]
- 005a09f4 bytes 2fdd1a94
+ 005a0a34 bytes 53dd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06ce93864b1d13ca3a786361b413f9f0"></a>

### [`005a0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a18.md) → [`005a0a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a0a58.md) FUN_005a0a58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a0a60",
      "incomplete_value": false,
      "site": "005a0a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0a20",
      "incomplete_value": false,
      "site": "005a0a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a0a64",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a0a64",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a18.md#insn-005a0a20) · [`005a0a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a18.md#insn-005a0a44)
- 新版 `005a0a60`（命令位置の公開資料なし） · `005a0a84`（命令位置の公開資料なし）

~~~diff
- 005a0a20 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a0a20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a0a20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a0a20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a0a60 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a0a60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a0a60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a0a60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a0a20 bytes 29012891
+ 005a0a60 bytes 29412b91
- 005a0a44 ["INT_ADD", "register:40f0:8", ["const:5a0a44:8", "const:4:8"]]
- 005a0a44 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a0a84 ["INT_ADD", "register:40f0:8", ["const:5a0a84:8", "const:4:8"]]
+ 005a0a84 ["CALL", null, ["callee:00c57f80:8"]]
- 005a0a44 bytes 1bdd1a94
+ 005a0a84 bytes 3fdd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a2c539feb317fc4f7e6e169c8cee1af"></a>

### [`005a0a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a58.md) → [`005a0a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a0a98.md) FUN_005a0a98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a0a9c",
      "incomplete_value": false,
      "site": "005a0aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0a5c",
      "incomplete_value": false,
      "site": "005a0a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a0aa0",
      "DATA",
      [
        "storage",
        "00c6e450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a0aa0",
      "DATA",
      [
        "storage",
        "00c6e520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a58.md#insn-005a0a5c)
- 新版 `005a0a9c`（命令位置の公開資料なし）

~~~diff
- 005a0a5c ["COPY", "tmp:0:8", ["const:450:8"]]
- 005a0a5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a0a5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a0a5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0a9c ["COPY", "tmp:0:8", ["const:520:8"]]
+ 005a0a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a0a5c bytes 08411191
+ 005a0a9c bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ed07586255e91bfd0660f24f93b284e"></a>

### [`005a0a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a68.md) → [`005a0aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a0aa8.md) FUN_005a0aa8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a0ab8",
      "incomplete_value": false,
      "site": "005a0ac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0a78",
      "incomplete_value": false,
      "site": "005a0a80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:450:8"
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
      "005a0ac0",
      "DATA",
      [
        "storage",
        "00c6e450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a0ac0",
      "DATA",
      [
        "storage",
        "00c6e520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a68.md#insn-005a0a78) · [`005a0a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a68.md#insn-005a0a84)
- 新版 `005a0ab8`（命令位置の公開資料なし） · `005a0ac4`（命令位置の公開資料なし）

~~~diff
- 005a0a78 ["COPY", "tmp:0:8", ["const:450:8"]]
- 005a0a78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a0a78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a0a78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0ab8 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 005a0ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a0a78 bytes 08411191
+ 005a0ab8 bytes 08811491
- 005a0a84 ["INT_ADD", "register:40f0:8", ["const:5a0a84:8", "const:4:8"]]
- 005a0a84 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a0ac4 ["INT_ADD", "register:40f0:8", ["const:5a0ac4:8", "const:4:8"]]
+ 005a0ac4 ["CALL", null, ["callee:00c57f70:8"]]
- 005a0a84 bytes 07dd1a94
+ 005a0ac4 bytes 2bdd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e479fd0b7806f3f9a6aac253649ccc93"></a>

### [`005a0a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a98.md) → [`005a0ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a0ad8.md) FUN_005a0ad8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a0ae0",
      "incomplete_value": false,
      "site": "005a0ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0aa0",
      "incomplete_value": false,
      "site": "005a0aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a0ae4",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a0ae4",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0a98.md#insn-005a0aa0)
- 新版 `005a0ae0`（命令位置の公開資料なし）

~~~diff
- 005a0aa0 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a0aa0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a0aa0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a0aa0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a0ae0 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a0ae0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a0ae0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a0ae0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a0aa0 bytes 29012891
+ 005a0ae0 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6639eb47062a00712f2d15433e596577"></a>

### [`005a0abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0abc.md) → [`005a0afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a0afc.md) FUN_005a0afc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a0b00",
      "incomplete_value": false,
      "site": "005a0b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0ac0",
      "incomplete_value": false,
      "site": "005a0ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a0b04",
      "DATA",
      [
        "storage",
        "00c6e4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a0b04",
      "DATA",
      [
        "storage",
        "00c6e570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0abc.md#insn-005a0ac0)
- 新版 `005a0b00`（命令位置の公開資料なし）

~~~diff
- 005a0ac0 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 005a0ac0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a0ac0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a0ac0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0b00 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 005a0b00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0b00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0b00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a0ac0 bytes 08811291
+ 005a0b00 bytes 08c11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-235e7166a13cbbcf822815a3c6e43ec4"></a>

### [`005a0acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0acc.md) → [`005a0b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a0b0c.md) FUN_005a0b0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a0b1c",
      "incomplete_value": false,
      "site": "005a0b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0adc",
      "incomplete_value": false,
      "site": "005a0ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a0b24",
      "DATA",
      [
        "storage",
        "00c6e4a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a0b24",
      "DATA",
      [
        "storage",
        "00c6e570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0acc.md#insn-005a0adc) · [`005a0ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0acc.md#insn-005a0ae8)
- 新版 `005a0b1c`（命令位置の公開資料なし） · `005a0b28`（命令位置の公開資料なし）

~~~diff
- 005a0adc ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 005a0adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a0adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a0adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a0b1c ["COPY", "tmp:0:8", ["const:570:8"]]
+ 005a0b1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0b1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a0b1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a0adc bytes 08811291
+ 005a0b1c bytes 08c11591
- 005a0ae8 ["INT_ADD", "register:40f0:8", ["const:5a0ae8:8", "const:4:8"]]
- 005a0ae8 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a0b28 ["INT_ADD", "register:40f0:8", ["const:5a0b28:8", "const:4:8"]]
+ 005a0b28 ["CALL", null, ["callee:00c57f70:8"]]
- 005a0ae8 bytes eedc1a94
+ 005a0b28 bytes 12dd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6c248c7d686246d902a5fbe170ded67"></a>

### [`005a0b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0b04.md) → [`005a0b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a0b44.md) _INIT_44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a0b80",
      "incomplete_value": true,
      "site": "005a0b9c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0b40",
      "incomplete_value": true,
      "site": "005a0b5c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f26:8"
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
      "definition_site": "005a0ba4",
      "incomplete_value": true,
      "site": "005a0bc0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
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
    "old": {
      "definition_site": "005a0b64",
      "incomplete_value": true,
      "site": "005a0b80",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f39:8"
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
      "definition_site": "005a0bc4",
      "incomplete_value": true,
      "site": "005a0be0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0b84",
      "incomplete_value": true,
      "site": "005a0ba0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:dc2:8"
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
      "005a0b80",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a0ba4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a0bc4",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a0b80",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005a0ba4",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005a0bc4",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0b04.md#insn-005a0b7c) · [`005a0b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0b04.md#insn-005a0b9c) · [`005a0d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0b04.md#insn-005a0d38)
- 新版 `005a0bbc`（命令位置の公開資料なし） · `005a0bdc`（命令位置の公開資料なし） · `005a0d78`（命令位置の公開資料なし）

~~~diff
- 005a0b7c ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 005a0b7c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a0b7c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a0b7c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a0bbc ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 005a0bbc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0bbc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0bbc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a0b7c bytes 4a093791
+ 005a0bbc bytes 4ab93591
- 005a0b9c ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005a0b9c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a0b9c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a0b9c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a0bdc ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005a0bdc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0bdc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0bdc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a0b9c bytes 4a893d91
+ 005a0bdc bytes 4a553c91
- 005a0d38 ["INT_ADD", "register:40f0:8", ["const:5a0d38:8", "const:4:8"]]
- 005a0d38 ["CALL", null, ["callee:00c57f00:8"]]
+ 005a0d78 ["INT_ADD", "register:40f0:8", ["const:5a0d78:8", "const:4:8"]]
+ 005a0d78 ["CALL", null, ["callee:00c57f00:8"]]
- 005a0d38 bytes 3edc1a94
+ 005a0d78 bytes 62dc1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc0f7f59f2fc3d993a69fdcc17b85372"></a>

### [`005a0e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0e94.md) → [`005a0ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a0ed4.md) FUN_005a0ed4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005a1b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b80.md) [`005a1de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1de0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`005a1bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1bc0.md) [`005a1e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1e20.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.66% / 新版 97.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a0f28",
      "incomplete_value": true,
      "site": "005a0f28",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:1e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a0ee8",
      "incomplete_value": true,
      "site": "005a0ee8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:1a5:8"
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
      "definition_site": "005a1044",
      "incomplete_value": true,
      "site": "005a1050",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:530:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1004",
      "incomplete_value": true,
      "site": "005a1010",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:4f0:8"
              ]
            ]
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
      "005a0f0c",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a1044",
      "READ",
      [
        "storage",
        "002b74f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a0f0c",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "005a1044",
      "READ",
      [
        "storage",
        "002b7530",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a0f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0e94.md#insn-005a0f28) · [`005a0ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0e94.md#insn-005a0ec0) · [`005a0ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0e94.md#insn-005a0ef8)
- 新版 `005a0f68`（命令位置の公開資料なし） · `005a0f00`（命令位置の公開資料なし） · `005a0f38`（命令位置の公開資料なし）

~~~diff
- 005a0f28 ["INT_ADD", "register:40f0:8", ["const:5a0f28:8", "const:4:8"]]
- 005a0f28 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a0f68 ["INT_ADD", "register:40f0:8", ["const:5a0f68:8", "const:4:8"]]
+ 005a0f68 ["CALL", null, ["callee:00c57f80:8"]]
- 005a0f28 bytes e2db1a94
+ 005a0f68 bytes 06dc1a94
- 005a0ec0 ["COPY", "tmp:0:8", ["const:1a5:8"]]
- 005a0ec0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a0ec0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a0ec0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a0f00 ["COPY", "tmp:0:8", ["const:1e5:8"]]
+ 005a0f00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0f00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a0f00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a0ec0 bytes 4a950691
+ 005a0f00 bytes 4a950791
- 005a0ef8 ["INT_ADD", "register:40f0:8", ["const:5a0ef8:8", "const:4:8"]]
- 005a0ef8 ["CALL", null, ["callee:004410cc:8"]]
+ 005a0f38 ["INT_ADD", "register:40f0:8", ["const:5a0f38:8", "const:4:8"]]
+ 005a0f38 ["CALL", null, ["callee:004410cc:8"]]
- 005a0ef8 bytes 6580fa97
+ 005a0f38 bytes 6580fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8439b3c390753138a96a6637a9acb023"></a>

### [`005a13cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a13cc.md) → [`005a140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a140c.md) FUN_005a140c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0079c86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c86c.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)
- 新版 呼出元 1件 [`0079c8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c8c4.md) · 呼出先 1件 [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md)

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
      "definition_site": "005a142c",
      "incomplete_value": false,
      "site": "005a1438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a13ec",
      "incomplete_value": false,
      "site": "005a13f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:510:8"
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
      "005a1438",
      "DATA",
      [
        "storage",
        "00c6e510",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1438",
      "DATA",
      [
        "storage",
        "00c6e5e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a13e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a13cc.md#insn-005a13e0) · [`005a13ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a13cc.md#insn-005a13ec)
- 新版 `005a1420`（命令位置の公開資料なし） · `005a142c`（命令位置の公開資料なし）

~~~diff
- 005a13e0 ["INT_ADD", "register:40f0:8", ["const:5a13e0:8", "const:4:8"]]
- 005a13e0 ["CALL", null, ["callee:0059b948:8"]]
+ 005a1420 ["INT_ADD", "register:40f0:8", ["const:5a1420:8", "const:4:8"]]
+ 005a1420 ["CALL", null, ["callee:0059b948:8"]]
- 005a13e0 bytes 4ae9ff97
+ 005a1420 bytes 4ae9ff97
- 005a13ec ["COPY", "tmp:0:8", ["const:510:8"]]
- 005a13ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a13ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a13ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a142c ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 005a142c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a142c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a142c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a13ec bytes 29411491
+ 005a142c bytes 29811791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a31e7b93ead05972d8c67d8c2d59d192"></a>

### [`005a1470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1470.md) → [`005a14b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a14b0.md) FUN_005a14b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004593f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md) [`0059719c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md) [`00597504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597504.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459430.md) [`00459b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459b10.md) [`005971dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005971dc.md) [`00597544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597544.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a1500",
      "incomplete_value": false,
      "site": "005a1504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a14c0",
      "incomplete_value": false,
      "site": "005a14c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "005a1504",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ],
    [
      "005a1574",
      "DATA",
      [
        "storage",
        "00c63760",
        null,
        "pointer"
      ]
    ],
    [
      "005a15bc",
      "READ",
      [
        "storage",
        "00c63768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1504",
      "DATA",
      [
        "storage",
        "00c6d748",
        null,
        "pointer"
      ]
    ],
    [
      "005a1574",
      "DATA",
      [
        "storage",
        "00c63830",
        null,
        "pointer"
      ]
    ],
    [
      "005a15bc",
      "READ",
      [
        "storage",
        "00c63838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a14a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1470.md#insn-005a14a4) · [`005a14ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1470.md#insn-005a14ac) · [`005a14c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1470.md#insn-005a14c0)
- 新版 `005a14e4`（命令位置の公開資料なし） · `005a14ec`（命令位置の公開資料なし） · `005a1500`（命令位置の公開資料なし）

~~~diff
- 005a14a4 ["INT_ADD", "register:40f0:8", ["const:5a14a4:8", "const:4:8"]]
- 005a14a4 ["CALL", null, ["callee:0059bf84:8"]]
+ 005a14e4 ["INT_ADD", "register:40f0:8", ["const:5a14e4:8", "const:4:8"]]
+ 005a14e4 ["CALL", null, ["callee:0059bf84:8"]]
- 005a14a4 bytes a8eaff97
+ 005a14e4 bytes a8eaff97
- 005a14ac ["INT_ADD", "register:40f0:8", ["const:5a14ac:8", "const:4:8"]]
- 005a14ac ["CALL", null, ["callee:00c57f60:8"]]
+ 005a14ec ["INT_ADD", "register:40f0:8", ["const:5a14ec:8", "const:4:8"]]
+ 005a14ec ["CALL", null, ["callee:00c57f60:8"]]
- 005a14ac bytes 79da1a94
+ 005a14ec bytes 9dda1a94
- 005a14c0 ["COPY", "tmp:0:8", ["const:678:8"]]
- 005a14c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a14c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a14c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a1500 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 005a1500 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1500 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1500 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a14c0 bytes 29e11991
+ 005a1500 bytes 29211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b4e53e7aef792ad5701fdd8c484ed1b"></a>

### [`005a16e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a16e0.md) → [`005a1720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1720.md) FUN_005a1720

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a173c",
      "incomplete_value": false,
      "site": "005a1744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a16fc",
      "incomplete_value": false,
      "site": "005a1704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "definition_site": "005a1754",
      "incomplete_value": false,
      "site": "005a1754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1714",
      "incomplete_value": false,
      "site": "005a1714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "005a1744",
      "DATA",
      [
        "storage",
        "00c6e618",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1754",
      "DATA",
      [
        "storage",
        "00c6e568",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a1744",
      "DATA",
      [
        "storage",
        "00c6e6e8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1754",
      "DATA",
      [
        "storage",
        "00c6e638",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a16f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a16e0.md#insn-005a16f4) · [`005a16fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a16e0.md#insn-005a16fc) · [`005a1708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a16e0.md#insn-005a1708)
- 新版 `005a1734`（命令位置の公開資料なし） · `005a173c`（命令位置の公開資料なし）

~~~diff
- 005a16f4 ["INT_ADD", "register:40f0:8", ["const:5a16f4:8", "const:4:8"]]
- 005a16f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a1734 ["INT_ADD", "register:40f0:8", ["const:5a1734:8", "const:4:8"]]
+ 005a1734 ["CALL", null, ["callee:00c57f60:8"]]
- 005a16f4 bytes e7d91a94
+ 005a1734 bytes 0bda1a94
- 005a16fc ["COPY", "tmp:0:8", ["const:618:8"]]
- 005a16fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a16fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a16fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a173c ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 005a173c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a173c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a173c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a16fc bytes 08611891
+ 005a173c bytes 08a11b91
- 005a1708 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005a1708 bytes 683600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f886321349f0b2152f773c115b68a3c"></a>

### [`005a1728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1728.md) → [`005a1768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1768.md) FUN_005a1768

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`005a17d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a17d4.md) [`0079be08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079be08.md) [`0079c980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079c980.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`005a1814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1814.md) [`0079be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md) [`0079c9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c9d8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "005a17d4",
      "incomplete_value": false,
      "site": "005a17d8",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
      "definition_site": "005a1794",
      "incomplete_value": false,
      "site": "005a1798",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "005a17d8",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a17d8",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1728.md#insn-005a1774) · [`005a1784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1728.md#insn-005a1784) · [`005a178c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1728.md#insn-005a178c)
- 新版 `005a17b4`（命令位置の公開資料なし） · `005a17c4`（命令位置の公開資料なし） · `005a17cc`（命令位置の公開資料なし）

~~~diff
- 005a1774 ["INT_ADD", "register:40f0:8", ["const:5a1774:8", "const:4:8"]]
- 005a1774 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a17b4 ["INT_ADD", "register:40f0:8", ["const:5a17b4:8", "const:4:8"]]
+ 005a17b4 ["CALL", null, ["callee:00c57f80:8"]]
- 005a1774 bytes cfd91a94
+ 005a17b4 bytes f3d91a94
- 005a1784 ["INT_ADD", "register:40f0:8", ["const:5a1784:8", "const:4:8"]]
- 005a1784 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a17c4 ["INT_ADD", "register:40f0:8", ["const:5a17c4:8", "const:4:8"]]
+ 005a17c4 ["CALL", null, ["callee:00c57f80:8"]]
- 005a1784 bytes cbd91a94
+ 005a17c4 bytes efd91a94
- 005a178c ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005a178c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a178c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a178c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a17cc ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005a17cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a17cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a17cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a178c bytes 08412891
+ 005a17cc bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bac05fec543882c518277a90a2a7fb31"></a>

### [`005a17f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a17f8.md) → [`005a1838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1838.md) FUN_005a1838

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a18a0",
      "incomplete_value": false,
      "site": "005a18a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1860",
      "incomplete_value": false,
      "site": "005a1864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "005a18a4",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a18a4",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a17f8.md#insn-005a1844) · [`005a1854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a17f8.md#insn-005a1854) · [`005a1860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a17f8.md#insn-005a1860)
- 新版 `005a1884`（命令位置の公開資料なし） · `005a1894`（命令位置の公開資料なし） · `005a18a0`（命令位置の公開資料なし）

~~~diff
- 005a1844 ["INT_ADD", "register:40f0:8", ["const:5a1844:8", "const:4:8"]]
- 005a1844 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a1884 ["INT_ADD", "register:40f0:8", ["const:5a1884:8", "const:4:8"]]
+ 005a1884 ["CALL", null, ["callee:00c57f80:8"]]
- 005a1844 bytes 9bd91a94
+ 005a1884 bytes bfd91a94
- 005a1854 ["INT_ADD", "register:40f0:8", ["const:5a1854:8", "const:4:8"]]
- 005a1854 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a1894 ["INT_ADD", "register:40f0:8", ["const:5a1894:8", "const:4:8"]]
+ 005a1894 ["CALL", null, ["callee:00c57f80:8"]]
- 005a1854 bytes 97d91a94
+ 005a1894 bytes bbd91a94
- 005a1860 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a1860 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a1860 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a1860 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a18a0 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a18a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a18a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a18a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a1860 bytes 29012891
+ 005a18a0 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e417a9b57f366a9732cb2af984455b5"></a>

### [`005a1890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1890.md) → [`005a18d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a18d0.md) FUN_005a18d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a1938",
      "incomplete_value": false,
      "site": "005a193c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a18f8",
      "incomplete_value": false,
      "site": "005a18fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "005a193c",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a193c",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a18dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1890.md#insn-005a18dc) · [`005a18ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1890.md#insn-005a18ec) · [`005a18f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1890.md#insn-005a18f8)
- 新版 `005a191c`（命令位置の公開資料なし） · `005a192c`（命令位置の公開資料なし） · `005a1938`（命令位置の公開資料なし）

~~~diff
- 005a18dc ["INT_ADD", "register:40f0:8", ["const:5a18dc:8", "const:4:8"]]
- 005a18dc ["CALL", null, ["callee:00c57f80:8"]]
+ 005a191c ["INT_ADD", "register:40f0:8", ["const:5a191c:8", "const:4:8"]]
+ 005a191c ["CALL", null, ["callee:00c57f80:8"]]
- 005a18dc bytes 75d91a94
+ 005a191c bytes 99d91a94
- 005a18ec ["INT_ADD", "register:40f0:8", ["const:5a18ec:8", "const:4:8"]]
- 005a18ec ["CALL", null, ["callee:00c57f80:8"]]
+ 005a192c ["INT_ADD", "register:40f0:8", ["const:5a192c:8", "const:4:8"]]
+ 005a192c ["CALL", null, ["callee:00c57f80:8"]]
- 005a18ec bytes 71d91a94
+ 005a192c bytes 95d91a94
- 005a18f8 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a18f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a18f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a18f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a1938 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a1938 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1938 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1938 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a18f8 bytes 29012891
+ 005a1938 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b8290c46247615f47d9701bdb5fab4a"></a>

### [`005a1b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b0c.md) → [`005a1b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1b4c.md) FUN_005a1b4c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a1920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1920.md) [`005a1b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b80.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`005a1960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1960.md) [`005a1bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1bc0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "005a1b58",
      "incomplete_value": false,
      "site": "005a1b5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1b18",
      "incomplete_value": false,
      "site": "005a1b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f4c:8"
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
      "005a1b58",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a1b58",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b0c.md#insn-005a1b1c) · [`005a1b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1b0c.md#insn-005a1b18)
- 新版 `005a1b5c`（命令位置の公開資料なし） · `005a1b58`（命令位置の公開資料なし）

~~~diff
- 005a1b1c ["INT_ADD", "register:40f0:8", ["const:5a1b1c:8", "const:4:8"]]
- 005a1b1c ["CALL", null, ["callee:0043b7b8:8"]]
+ 005a1b5c ["INT_ADD", "register:40f0:8", ["const:5a1b5c:8", "const:4:8"]]
+ 005a1b5c ["CALL", null, ["callee:0043b7b8:8"]]
- 005a1b1c bytes 1767fa97
+ 005a1b5c bytes 1767fa97
- 005a1b18 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 005a1b18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005a1b18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005a1b18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005a1b58 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 005a1b58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005a1b58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005a1b58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005a1b18 bytes 00303d91
+ 005a1b58 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41a2e7621c244676504c9aa90e9ac061"></a>

### [`005a1de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1de0.md) → [`005a1e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1e20.md) FUN_005a1e20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005a0e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0e94.md) · 呼出先 3件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`005a1920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1920.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005a0ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a0ed4.md) · 呼出先 3件 [`0059b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b91c.md) [`005a1960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1960.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "005a1e58",
      "incomplete_value": false,
      "site": "005a1e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1e18",
      "incomplete_value": false,
      "site": "005a1e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "definition_site": "005a1ea0",
      "incomplete_value": false,
      "site": "005a1ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1e60",
      "incomplete_value": false,
      "site": "005a1e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "005a1e64",
      "DATA",
      [
        "storage",
        "00c6e5c8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1ea0",
      "DATA",
      [
        "storage",
        "00c6e4f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a1e64",
      "DATA",
      [
        "storage",
        "00c6e698",
        null,
        "undefined *"
      ]
    ],
    [
      "005a1ea0",
      "DATA",
      [
        "storage",
        "00c6e5c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1de0.md#insn-005a1e64) · [`005a1e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1de0.md#insn-005a1e08) · [`005a1e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1de0.md#insn-005a1e18)
- 新版 `005a1ea4`（命令位置の公開資料なし） · `005a1e48`（命令位置の公開資料なし） · `005a1e58`（命令位置の公開資料なし）

~~~diff
- 005a1e64 ["INT_ADD", "register:40f0:8", ["const:5a1e64:8", "const:4:8"]]
- 005a1e64 ["CALL", null, ["callee:005a1960:8"]]
+ 005a1ea4 ["INT_ADD", "register:40f0:8", ["const:5a1ea4:8", "const:4:8"]]
+ 005a1ea4 ["CALL", null, ["callee:005a1960:8"]]
- 005a1e64 bytes affeff97
+ 005a1ea4 bytes affeff97
- 005a1e08 ["INT_ADD", "register:40f0:8", ["const:5a1e08:8", "const:4:8"]]
- 005a1e08 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a1e48 ["INT_ADD", "register:40f0:8", ["const:5a1e48:8", "const:4:8"]]
+ 005a1e48 ["CALL", null, ["callee:00c57f60:8"]]
- 005a1e08 bytes 22d81a94
+ 005a1e48 bytes 46d81a94
- 005a1e18 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 005a1e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1e58 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 005a1e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1e18 bytes 08211791
+ 005a1e58 bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b33d83cf1d87fe768467f646031a68a"></a>

### [`005a1ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1ec0.md) → [`005a1f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1f00.md) FUN_005a1f00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a1f04",
      "incomplete_value": false,
      "site": "005a1f08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1ec4",
      "incomplete_value": false,
      "site": "005a1ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "005a1f08",
      "DATA",
      [
        "storage",
        "00c6e5c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1f08",
      "DATA",
      [
        "storage",
        "00c6e698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1ec0.md#insn-005a1ec4)
- 新版 `005a1f04`（命令位置の公開資料なし）

~~~diff
- 005a1ec4 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 005a1ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1f04 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 005a1f04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1f04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1f04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1ec4 bytes 08211791
+ 005a1f04 bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2255b8f40a7db13b3f4a1915f00c4cc"></a>

### [`005a1ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1ed0.md) → [`005a1f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1f10.md) FUN_005a1f10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a1f20",
      "incomplete_value": false,
      "site": "005a1f28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1ee0",
      "incomplete_value": false,
      "site": "005a1ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "005a1f28",
      "DATA",
      [
        "storage",
        "00c6e5c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1f28",
      "DATA",
      [
        "storage",
        "00c6e698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1ed0.md#insn-005a1ee0) · [`005a1eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1ed0.md#insn-005a1eec)
- 新版 `005a1f20`（命令位置の公開資料なし） · `005a1f2c`（命令位置の公開資料なし）

~~~diff
- 005a1ee0 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 005a1ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1f20 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 005a1f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1ee0 bytes 08211791
+ 005a1f20 bytes 08611a91
- 005a1eec ["INT_ADD", "register:40f0:8", ["const:5a1eec:8", "const:4:8"]]
- 005a1eec ["CALL", null, ["callee:00c57f70:8"]]
+ 005a1f2c ["INT_ADD", "register:40f0:8", ["const:5a1f2c:8", "const:4:8"]]
+ 005a1f2c ["CALL", null, ["callee:00c57f70:8"]]
- 005a1eec bytes edd71a94
+ 005a1f2c bytes 11d81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1801efa875daed092e18b6a61fb7316c"></a>

### [`005a1f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1f00.md) → [`005a1f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1f40.md) FUN_005a1f40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a1fa8",
      "incomplete_value": false,
      "site": "005a1fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1f68",
      "incomplete_value": false,
      "site": "005a1f6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "005a1fac",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a1fac",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1f00.md#insn-005a1f4c) · [`005a1f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1f00.md#insn-005a1f5c) · [`005a1f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1f00.md#insn-005a1f68)
- 新版 `005a1f8c`（命令位置の公開資料なし） · `005a1f9c`（命令位置の公開資料なし） · `005a1fa8`（命令位置の公開資料なし）

~~~diff
- 005a1f4c ["INT_ADD", "register:40f0:8", ["const:5a1f4c:8", "const:4:8"]]
- 005a1f4c ["CALL", null, ["callee:00c57f80:8"]]
+ 005a1f8c ["INT_ADD", "register:40f0:8", ["const:5a1f8c:8", "const:4:8"]]
+ 005a1f8c ["CALL", null, ["callee:00c57f80:8"]]
- 005a1f4c bytes d9d71a94
+ 005a1f8c bytes fdd71a94
- 005a1f5c ["INT_ADD", "register:40f0:8", ["const:5a1f5c:8", "const:4:8"]]
- 005a1f5c ["CALL", null, ["callee:00c57f80:8"]]
+ 005a1f9c ["INT_ADD", "register:40f0:8", ["const:5a1f9c:8", "const:4:8"]]
+ 005a1f9c ["CALL", null, ["callee:00c57f80:8"]]
- 005a1f5c bytes d5d71a94
+ 005a1f9c bytes f9d71a94
- 005a1f68 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a1f68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a1f68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a1f68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a1fa8 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a1fa8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1fa8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a1fa8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a1f68 bytes 29012891
+ 005a1fa8 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08a6bf7ae600fbbf4872d51915042f20"></a>

### [`005a1f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1f9c.md) → [`005a1fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1fdc.md) FUN_005a1fdc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a1fe0",
      "incomplete_value": false,
      "site": "005a1fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1fa0",
      "incomplete_value": false,
      "site": "005a1fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "005a1fe4",
      "DATA",
      [
        "storage",
        "00c6e618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a1fe4",
      "DATA",
      [
        "storage",
        "00c6e6e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1f9c.md#insn-005a1fa0)
- 新版 `005a1fe0`（命令位置の公開資料なし）

~~~diff
- 005a1fa0 ["COPY", "tmp:0:8", ["const:618:8"]]
- 005a1fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1fe0 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 005a1fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1fa0 bytes 08611891
+ 005a1fe0 bytes 08a11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f66f9fb77a27a6dccc67df9a796e20d"></a>

### [`005a1fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1fac.md) → [`005a1fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1fec.md) FUN_005a1fec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a1ffc",
      "incomplete_value": false,
      "site": "005a2004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a1fbc",
      "incomplete_value": false,
      "site": "005a1fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:618:8"
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
      "005a2004",
      "DATA",
      [
        "storage",
        "00c6e618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a2004",
      "DATA",
      [
        "storage",
        "00c6e6e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a1fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1fac.md#insn-005a1fbc) · [`005a1fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1fac.md#insn-005a1fc8)
- 新版 `005a1ffc`（命令位置の公開資料なし） · `005a2008`（命令位置の公開資料なし）

~~~diff
- 005a1fbc ["COPY", "tmp:0:8", ["const:618:8"]]
- 005a1fbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a1fbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a1fbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a1ffc ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 005a1ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a1ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a1fbc bytes 08611891
+ 005a1ffc bytes 08a11b91
- 005a1fc8 ["INT_ADD", "register:40f0:8", ["const:5a1fc8:8", "const:4:8"]]
- 005a1fc8 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a2008 ["INT_ADD", "register:40f0:8", ["const:5a2008:8", "const:4:8"]]
+ 005a2008 ["CALL", null, ["callee:00c57f70:8"]]
- 005a1fc8 bytes b6d71a94
+ 005a2008 bytes dad71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5b035092a7cafbaef5f18508df8aabb"></a>

### [`005a1fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1fe4.md) → [`005a2024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a2/005a2024.md) _INIT_45

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a20c4",
      "incomplete_value": true,
      "site": "005a20dc",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:4050:8"
              ],
              [
                "leaf",
                "const:f15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a2084",
      "incomplete_value": true,
      "site": "005a209c",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:4050:8"
              ],
              [
                "leaf",
                "const:f62:8"
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
      "definition_site": "005a2100",
      "incomplete_value": true,
      "site": "005a211c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a20c0",
      "incomplete_value": true,
      "site": "005a20dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f5d:8"
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
      "definition_site": "005a2120",
      "incomplete_value": true,
      "site": "005a2164",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ebc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a20e0",
      "incomplete_value": true,
      "site": "005a2124",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f09:8"
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
      "005a2060",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a2084",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a20a4",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a2060",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005a2084",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005a20a4",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a205c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1fe4.md#insn-005a205c) · [`005a2218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1fe4.md#insn-005a2218) · [`005a2010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1fe4.md#insn-005a2010)
- 新版 `005a209c`（命令位置の公開資料なし） · `005a2258`（命令位置の公開資料なし） · `005a2050`（命令位置の公開資料なし）

~~~diff
- 005a205c ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 005a205c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a205c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a205c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a209c ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 005a209c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a209c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a209c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a205c bytes 4a093791
+ 005a209c bytes 4ab93591
- 005a2218 ["INT_ADD", "register:40f0:8", ["const:5a2218:8", "const:4:8"]]
- 005a2218 ["CALL", null, ["callee:00c57f00:8"]]
+ 005a2258 ["INT_ADD", "register:40f0:8", ["const:5a2258:8", "const:4:8"]]
+ 005a2258 ["CALL", null, ["callee:00c57f00:8"]]
- 005a2218 bytes 06d71a94
+ 005a2258 bytes 2ad71a94
- 005a2010 ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 005a2010 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005a2010 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005a2010 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005a2050 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 005a2050 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005a2050 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005a2050 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005a2010 bytes 73021b91
+ 005a2050 bytes 73021f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f31daff000204f68d8fdf99c414d7217"></a>

### [`005a2374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2374.md) → [`005a23b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a2/005a23b4.md) FUN_005a23b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0059b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b91c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "005a2524",
      "incomplete_value": true,
      "site": "005a2524",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:522:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a24e4",
      "incomplete_value": true,
      "site": "005a24e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:576:8"
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
      "definition_site": "005a25dc",
      "incomplete_value": false,
      "site": "005a25e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a259c",
      "incomplete_value": false,
      "site": "005a25a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "005a23e4",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a2510",
      "READ",
      [
        "storage",
        "002bb576",
        null,
        "string"
      ]
    ],
    [
      "005a25c4",
      "DATA",
      [
        "storage",
        "00c6e740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a23e4",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "005a2510",
      "READ",
      [
        "storage",
        "002bb522",
        null,
        "string"
      ]
    ],
    [
      "005a25c4",
      "DATA",
      [
        "storage",
        "00c6e810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a2564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2374.md#insn-005a2564) · [`005a2398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2374.md#insn-005a2398) · [`005a23d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2374.md#insn-005a23d0)
- 新版 `005a25a4`（命令位置の公開資料なし） · `005a23d8`（命令位置の公開資料なし） · `005a2410`（命令位置の公開資料なし）

~~~diff
- 005a2564 ["INT_ADD", "register:40f0:8", ["const:5a2564:8", "const:4:8"]]
- 005a2564 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a25a4 ["INT_ADD", "register:40f0:8", ["const:5a25a4:8", "const:4:8"]]
+ 005a25a4 ["CALL", null, ["callee:00c57f80:8"]]
- 005a2564 bytes 53d61a94
+ 005a25a4 bytes 77d61a94
- 005a2398 ["COPY", "tmp:0:8", ["const:1a5:8"]]
- 005a2398 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a2398 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a2398 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a23d8 ["COPY", "tmp:0:8", ["const:1e5:8"]]
+ 005a23d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a23d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a23d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a2398 bytes 4a950691
+ 005a23d8 bytes 4a950791
- 005a23d0 ["INT_ADD", "register:40f0:8", ["const:5a23d0:8", "const:4:8"]]
- 005a23d0 ["CALL", null, ["callee:004410cc:8"]]
+ 005a2410 ["INT_ADD", "register:40f0:8", ["const:5a2410:8", "const:4:8"]]
+ 005a2410 ["CALL", null, ["callee:004410cc:8"]]
- 005a23d0 bytes 2f7bfa97
+ 005a2410 bytes 2f7bfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b76611ddc5c9ee18062c71c6a23cb94"></a>

### [`005a2734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2734.md) → [`005a2774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a2/005a2774.md) FUN_005a2774

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a2790",
      "incomplete_value": true,
      "site": "005a2794",
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
      "definition_site": "005a2750",
      "incomplete_value": true,
      "site": "005a2754",
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
      "005a2788",
      "READ",
      [
        "storage",
        "00c9b320",
        null,
        "pointer"
      ]
    ],
    [
      "005a2794",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a2788",
      "READ",
      [
        "storage",
        "00c9b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "005a2794",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a2748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2734.md#insn-005a2748) · [`005a2760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2734.md#insn-005a2760) · [`005a2770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2734.md#insn-005a2770)
- 新版 `005a2788`（命令位置の公開資料なし） · `005a27a0`（命令位置の公開資料なし） · `005a27b0`（命令位置の公開資料なし）

~~~diff
- 005a2748 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
- 005a2748 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a2788 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f0:8"]]
+ 005a2788 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a2748 bytes 089141f9
+ 005a2788 bytes 08f941f9
- 005a2760 ["INT_ADD", "register:40f0:8", ["const:5a2760:8", "const:4:8"]]
- 005a2760 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a27a0 ["INT_ADD", "register:40f0:8", ["const:5a27a0:8", "const:4:8"]]
+ 005a27a0 ["CALL", null, ["callee:00c57f80:8"]]
- 005a2760 bytes d4d51a94
+ 005a27a0 bytes f8d51a94
- 005a2770 ["INT_ADD", "register:40f0:8", ["const:5a2770:8", "const:4:8"]]
- 005a2770 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a27b0 ["INT_ADD", "register:40f0:8", ["const:5a27b0:8", "const:4:8"]]
+ 005a27b0 ["CALL", null, ["callee:00c57f80:8"]]
- 005a2770 bytes d0d51a94
+ 005a27b0 bytes f4d51a94
~~~


<a id="compare-08a7440a325669454511929db3143390"></a>

### [`005a2784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2784.md) → [`005a27c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a2/005a27c4.md) FUN_005a27c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a27cc",
      "incomplete_value": false,
      "site": "005a27d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a278c",
      "incomplete_value": false,
      "site": "005a2790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a27d0",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a27d0",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a278c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2784.md#insn-005a278c) · [`005a27b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2784.md#insn-005a27b0)
- 新版 `005a27cc`（命令位置の公開資料なし） · `005a27f0`（命令位置の公開資料なし）

~~~diff
- 005a278c ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a278c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a278c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a278c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a27cc ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a27cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a27cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a27cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a278c bytes 29012891
+ 005a27cc bytes 29412b91
- 005a27b0 ["INT_ADD", "register:40f0:8", ["const:5a27b0:8", "const:4:8"]]
- 005a27b0 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a27f0 ["INT_ADD", "register:40f0:8", ["const:5a27f0:8", "const:4:8"]]
+ 005a27f0 ["CALL", null, ["callee:00c57f80:8"]]
- 005a27b0 bytes c0d51a94
+ 005a27f0 bytes e4d51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acd3d5f7a802c538ec83127042044311"></a>

### [`005a27d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a27d4.md) → [`005a2814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a2/005a2814.md) FUN_005a2814

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a2824",
      "incomplete_value": false,
      "site": "005a282c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a27e4",
      "incomplete_value": false,
      "site": "005a27ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:740:8"
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
      "005a282c",
      "DATA",
      [
        "storage",
        "00c6e740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a282c",
      "DATA",
      [
        "storage",
        "00c6e810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a27e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a27d4.md#insn-005a27e4) · [`005a27f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a27d4.md#insn-005a27f0)
- 新版 `005a2824`（命令位置の公開資料なし） · `005a2830`（命令位置の公開資料なし）

~~~diff
- 005a27e4 ["COPY", "tmp:0:8", ["const:740:8"]]
- 005a27e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a27e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a27e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a2824 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 005a2824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a2824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a2824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a27e4 bytes 08011d91
+ 005a2824 bytes 08412091
- 005a27f0 ["INT_ADD", "register:40f0:8", ["const:5a27f0:8", "const:4:8"]]
- 005a27f0 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a2830 ["INT_ADD", "register:40f0:8", ["const:5a2830:8", "const:4:8"]]
+ 005a2830 ["CALL", null, ["callee:00c57f70:8"]]
- 005a27f0 bytes acd51a94
+ 005a2830 bytes d0d51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-084c009123d8646e046263dca93a307c"></a>

### [`005a2804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2804.md) → [`005a2844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a2/005a2844.md) FUN_005a2844

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a284c",
      "incomplete_value": true,
      "site": "005a2850",
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
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a280c",
      "incomplete_value": true,
      "site": "005a2810",
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
      "005a2850",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a2850",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a280c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2804.md#insn-005a280c)
- 新版 `005a284c`（命令位置の公開資料なし）

~~~diff
- 005a280c ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a280c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a280c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a280c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a284c ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a284c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a284c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a284c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a280c bytes 29012891
+ 005a284c bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3548214a6b80eadb6376737b3e91b9e"></a>

### [`005a2828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2828.md) → [`005a2868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a2/005a2868.md) FUN_005a2868

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a286c",
      "incomplete_value": false,
      "site": "005a2870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a282c",
      "incomplete_value": false,
      "site": "005a2830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:790:8"
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
      "005a2870",
      "DATA",
      [
        "storage",
        "00c6e790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a2870",
      "DATA",
      [
        "storage",
        "00c6e860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a282c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2828.md#insn-005a282c)
- 新版 `005a286c`（命令位置の公開資料なし）

~~~diff
- 005a282c ["COPY", "tmp:0:8", ["const:790:8"]]
- 005a282c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a282c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a282c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a286c ["COPY", "tmp:0:8", ["const:860:8"]]
+ 005a286c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a286c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a286c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a282c bytes 08411e91
+ 005a286c bytes 08812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc1cd0bdecd6289c566991f7ed4cde2c"></a>

### [`005a2838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2838.md) → [`005a2878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a2/005a2878.md) FUN_005a2878

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a2888",
      "incomplete_value": false,
      "site": "005a2890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:860:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a2848",
      "incomplete_value": false,
      "site": "005a2850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:790:8"
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
      "005a2890",
      "DATA",
      [
        "storage",
        "00c6e790",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a2890",
      "DATA",
      [
        "storage",
        "00c6e860",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a2848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2838.md#insn-005a2848) · [`005a2854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2838.md#insn-005a2854)
- 新版 `005a2888`（命令位置の公開資料なし） · `005a2894`（命令位置の公開資料なし）

~~~diff
- 005a2848 ["COPY", "tmp:0:8", ["const:790:8"]]
- 005a2848 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a2848 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a2848 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a2888 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 005a2888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a2888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a2888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a2848 bytes 08411e91
+ 005a2888 bytes 08812191
- 005a2854 ["INT_ADD", "register:40f0:8", ["const:5a2854:8", "const:4:8"]]
- 005a2854 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a2894 ["INT_ADD", "register:40f0:8", ["const:5a2894:8", "const:4:8"]]
+ 005a2894 ["CALL", null, ["callee:00c57f70:8"]]
- 005a2854 bytes 93d51a94
+ 005a2894 bytes b7d51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4eba362053d3978c14486fb45b070fd"></a>

### [`005a2870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2870.md) → [`005a28b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a2/005a28b0.md) _INIT_46

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.40% / 新版 90.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a28ec",
      "incomplete_value": true,
      "site": "005a2908",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a28ac",
      "incomplete_value": true,
      "site": "005a28c8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f26:8"
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
      "definition_site": "005a298c",
      "incomplete_value": true,
      "site": "005a29a8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a294c",
      "incomplete_value": true,
      "site": "005a2968",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f5d:8"
              ]
            ]
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
      "005a28ec",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a2910",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a2930",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a28ec",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005a2910",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005a2930",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a2908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2870.md#insn-005a2908) · [`005a289c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2870.md#insn-005a289c) · [`005a28a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2870.md#insn-005a28a8)
- 新版 `005a2948`（命令位置の公開資料なし） · `005a28dc`（命令位置の公開資料なし） · `005a28e8`（命令位置の公開資料なし）

~~~diff
- 005a2908 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005a2908 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a2908 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a2908 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a2948 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005a2948 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a2948 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a2948 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a2908 bytes 4a893d91
+ 005a2948 bytes 4a553c91
- 005a289c ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 005a289c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005a289c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005a289c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005a28dc ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 005a28dc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005a28dc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005a28dc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005a289c bytes 73621b91
+ 005a28dc bytes 73621f91
- 005a28a8 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 005a28a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a28a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a28a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a28e8 ["COPY", "tmp:0:8", ["const:f66:8"]]
+ 005a28e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a28e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a28e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a28a8 bytes 29993c91
+ 005a28e8 bytes 29993d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1fb0c77315f5753ab968ea75323afbb"></a>

### [`005a2c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2c00.md) → [`005a2c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a2/005a2c40.md) _INIT_47

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a2e68",
      "incomplete_value": false,
      "site": "005a2e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a2e28",
      "incomplete_value": false,
      "site": "005a2e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "definition_site": "005a2e70",
      "incomplete_value": false,
      "site": "005a2e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a2e30",
      "incomplete_value": false,
      "site": "005a2e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "005a2c7c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a2ca0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a2cc0",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a2c7c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005a2ca0",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005a2cc0",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a2e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2c00.md#insn-005a2e34) · [`005a2c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2c00.md#insn-005a2c2c) · [`005a2c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2c00.md#insn-005a2c34)
- 新版 `005a2e74`（命令位置の公開資料なし） · `005a2c6c`（命令位置の公開資料なし）

~~~diff
- 005a2e34 ["INT_ADD", "register:40f0:8", ["const:5a2e34:8", "const:4:8"]]
- 005a2e34 ["CALL", null, ["callee:00c57f00:8"]]
+ 005a2e74 ["INT_ADD", "register:40f0:8", ["const:5a2e74:8", "const:4:8"]]
+ 005a2e74 ["CALL", null, ["callee:00c57f00:8"]]
- 005a2e34 bytes ffd31a94
+ 005a2e74 bytes 23d41a94
- 005a2c2c ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 005a2c2c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005a2c2c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005a2c2c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005a2c6c ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 005a2c6c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005a2c6c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005a2c6c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005a2c2c bytes 73c21b91
+ 005a2c6c bytes 73c21f91
- 005a2c34 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 005a2c34 bytes a9e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06ee125a59de5ab221e9548e3e32a570"></a>

### [`005a2f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2f90.md) → [`005a2fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a2/005a2fd0.md) _INIT_48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.40% / 新版 90.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a300c",
      "incomplete_value": true,
      "site": "005a3028",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a2fcc",
      "incomplete_value": true,
      "site": "005a2fe8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f26:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a3200",
      "incomplete_value": true,
      "site": "005a3204",
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
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a31c0",
      "incomplete_value": true,
      "site": "005a31c4",
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
            "const:f90:8"
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
      "005a300c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a3030",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a3050",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a300c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005a3030",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005a3050",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a3028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2f90.md#insn-005a3028) · [`005a31c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2f90.md#insn-005a31c4) · [`005a2fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a2/005a2f90.md#insn-005a2fbc)
- 新版 `005a3068`（命令位置の公開資料なし） · `005a3204`（命令位置の公開資料なし） · `005a2ffc`（命令位置の公開資料なし）

~~~diff
- 005a3028 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005a3028 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a3028 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a3028 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a3068 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005a3068 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a3068 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a3068 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a3028 bytes 4a893d91
+ 005a3068 bytes 4a553c91
- 005a31c4 ["INT_ADD", "register:40f0:8", ["const:5a31c4:8", "const:4:8"]]
- 005a31c4 ["CALL", null, ["callee:00c57f00:8"]]
+ 005a3204 ["INT_ADD", "register:40f0:8", ["const:5a3204:8", "const:4:8"]]
+ 005a3204 ["CALL", null, ["callee:00c57f00:8"]]
- 005a31c4 bytes 1bd31a94
+ 005a3204 bytes 3fd31a94
- 005a2fbc ["COPY", "tmp:0:8", ["const:708:8"]]
- 005a2fbc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005a2fbc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005a2fbc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005a2ffc ["COPY", "tmp:0:8", ["const:808:8"]]
+ 005a2ffc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005a2ffc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005a2ffc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005a2fbc bytes 73221c91
+ 005a2ffc bytes 73222091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f3e69f62ba4a8ff2b3dbc3c97843eac"></a>

### [`005a3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md) → [`005a3360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a3/005a3360.md) FUN_005a3360

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md) [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) [`005a4594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`005a42e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42e0.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`005a45d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a45d4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a376c",
      "incomplete_value": true,
      "site": "005a3778",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
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
    "old": {
      "definition_site": "005a372c",
      "incomplete_value": true,
      "site": "005a3738",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:34b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 74,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a3398",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a3500",
      "READ",
      [
        "storage",
        "002a9e52",
        null,
        "string"
      ]
    ],
    [
      "005a366c",
      "READ",
      [
        "storage",
        "002b71b8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a3398",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "005a3500",
      "READ",
      [
        "storage",
        "002a9df6",
        null,
        "string"
      ]
    ],
    [
      "005a366c",
      "READ",
      [
        "storage",
        "002b71f8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a36f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md#insn-005a36f8) · [`005a334c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md#insn-005a334c) · [`005a3384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md#insn-005a3384)
- 新版 `005a3738`（命令位置の公開資料なし） · `005a338c`（命令位置の公開資料なし） · `005a33c4`（命令位置の公開資料なし）

~~~diff
- 005a36f8 ["INT_ADD", "register:40f0:8", ["const:5a36f8:8", "const:4:8"]]
- 005a36f8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a3738 ["INT_ADD", "register:40f0:8", ["const:5a3738:8", "const:4:8"]]
+ 005a3738 ["CALL", null, ["callee:00c57f80:8"]]
- 005a36f8 bytes eed11a94
+ 005a3738 bytes 12d21a94
- 005a334c ["COPY", "tmp:0:8", ["const:1a5:8"]]
- 005a334c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a334c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a334c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a338c ["COPY", "tmp:0:8", ["const:1e5:8"]]
+ 005a338c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a338c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a338c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a334c bytes 4a950691
+ 005a338c bytes 4a950791
- 005a3384 ["INT_ADD", "register:40f0:8", ["const:5a3384:8", "const:4:8"]]
- 005a3384 ["CALL", null, ["callee:004410cc:8"]]
+ 005a33c4 ["INT_ADD", "register:40f0:8", ["const:5a33c4:8", "const:4:8"]]
+ 005a33c4 ["CALL", null, ["callee:004410cc:8"]]
- 005a3384 bytes 4277fa97
+ 005a33c4 bytes 4277fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-946cf1eb5dc4b28bdbf818c4613d06ef"></a>

### [`005a3f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3f98.md) → [`005a3fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a3/005a3fd8.md) FUN_005a3fd8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a3ff4",
      "incomplete_value": false,
      "site": "005a3ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a3fb4",
      "incomplete_value": false,
      "site": "005a3fbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a400c",
      "incomplete_value": true,
      "site": "005a400c",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a3fcc",
      "incomplete_value": true,
      "site": "005a3fcc",
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
            "const:800:8"
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
      "005a3ffc",
      "DATA",
      [
        "storage",
        "00c6e908",
        null,
        "undefined *"
      ]
    ],
    [
      "005a400c",
      "DATA",
      [
        "storage",
        "00c6e800",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a3ffc",
      "DATA",
      [
        "storage",
        "00c6e9d8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a400c",
      "DATA",
      [
        "storage",
        "00c6e8d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a3fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3f98.md#insn-005a3fac) · [`005a3fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3f98.md#insn-005a3fb4) · [`005a3fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3f98.md#insn-005a3fc0)
- 新版 `005a3fec`（命令位置の公開資料なし） · `005a3ff4`（命令位置の公開資料なし）

~~~diff
- 005a3fac ["INT_ADD", "register:40f0:8", ["const:5a3fac:8", "const:4:8"]]
- 005a3fac ["CALL", null, ["callee:00c57f60:8"]]
+ 005a3fec ["INT_ADD", "register:40f0:8", ["const:5a3fec:8", "const:4:8"]]
+ 005a3fec ["CALL", null, ["callee:00c57f60:8"]]
- 005a3fac bytes b9cf1a94
+ 005a3fec bytes ddcf1a94
- 005a3fb4 ["COPY", "tmp:0:8", ["const:908:8"]]
- 005a3fb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a3fb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a3fb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a3ff4 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 005a3ff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a3ff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a3ff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a3fb4 bytes 08212491
+ 005a3ff4 bytes 08612791
- 005a3fc0 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005a3fc0 bytes 483600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2ef4304763dfb01f1b1737544056afd"></a>

### [`005a4030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4030.md) → [`005a4070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4070.md) FUN_005a4070

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a4548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4548.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a40a4",
      "incomplete_value": false,
      "site": "005a40a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4064",
      "incomplete_value": false,
      "site": "005a4068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "005a40a8",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a40a8",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4030.md#insn-005a4050) · [`005a4058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4030.md#insn-005a4058) · [`005a4064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4030.md#insn-005a4064)
- 新版 `005a4090`（命令位置の公開資料なし） · `005a4098`（命令位置の公開資料なし） · `005a40a4`（命令位置の公開資料なし）

~~~diff
- 005a4050 ["INT_ADD", "register:40f0:8", ["const:5a4050:8", "const:4:8"]]
- 005a4050 ["CALL", null, ["callee:005a4548:8"]]
+ 005a4090 ["INT_ADD", "register:40f0:8", ["const:5a4090:8", "const:4:8"]]
+ 005a4090 ["CALL", null, ["callee:005a4548:8"]]
- 005a4050 bytes 2e010094
+ 005a4090 bytes 2e010094
- 005a4058 ["INT_ADD", "register:40f0:8", ["const:5a4058:8", "const:4:8"]]
- 005a4058 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a4098 ["INT_ADD", "register:40f0:8", ["const:5a4098:8", "const:4:8"]]
+ 005a4098 ["CALL", null, ["callee:00c57f80:8"]]
- 005a4058 bytes 96cf1a94
+ 005a4098 bytes bacf1a94
- 005a4064 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a4064 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a4064 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a4064 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a40a4 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a40a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a40a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a40a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a4064 bytes 29012891
+ 005a40a4 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ab8d72747f69e98d52dad8229a6ec8f"></a>

### [`005a408c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a408c.md) → [`005a40cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a40cc.md) FUN_005a40cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a4548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4548.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a4100",
      "incomplete_value": false,
      "site": "005a4104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a40c0",
      "incomplete_value": false,
      "site": "005a40c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "005a4104",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a4104",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a40ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a408c.md#insn-005a40ac) · [`005a40b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a408c.md#insn-005a40b4) · [`005a40c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a408c.md#insn-005a40c0)
- 新版 `005a40ec`（命令位置の公開資料なし） · `005a40f4`（命令位置の公開資料なし） · `005a4100`（命令位置の公開資料なし）

~~~diff
- 005a40ac ["INT_ADD", "register:40f0:8", ["const:5a40ac:8", "const:4:8"]]
- 005a40ac ["CALL", null, ["callee:005a4548:8"]]
+ 005a40ec ["INT_ADD", "register:40f0:8", ["const:5a40ec:8", "const:4:8"]]
+ 005a40ec ["CALL", null, ["callee:005a4548:8"]]
- 005a40ac bytes 17010094
+ 005a40ec bytes 17010094
- 005a40b4 ["INT_ADD", "register:40f0:8", ["const:5a40b4:8", "const:4:8"]]
- 005a40b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a40f4 ["INT_ADD", "register:40f0:8", ["const:5a40f4:8", "const:4:8"]]
+ 005a40f4 ["CALL", null, ["callee:00c57f80:8"]]
- 005a40b4 bytes 7fcf1a94
+ 005a40f4 bytes a3cf1a94
- 005a40c0 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a40c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a40c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a40c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a4100 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a4100 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a4100 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a4100 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a40c0 bytes 29012891
+ 005a4100 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5292956edd220a6025f47f3282aee9e"></a>

### [`005a426c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a426c.md) → [`005a42ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42ac.md) FUN_005a42ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005a40e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md) [`005a4594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4594.md) [`0079cc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cc10.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 3件 [`005a4124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4124.md) [`005a45d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a45d4.md) [`0079cc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cc68.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "005a42b8",
      "incomplete_value": false,
      "site": "005a42bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4278",
      "incomplete_value": false,
      "site": "005a427c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f4c:8"
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
      "005a42b8",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a42b8",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a427c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a426c.md#insn-005a427c) · [`005a4278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a426c.md#insn-005a4278)
- 新版 `005a42bc`（命令位置の公開資料なし） · `005a42b8`（命令位置の公開資料なし）

~~~diff
- 005a427c ["INT_ADD", "register:40f0:8", ["const:5a427c:8", "const:4:8"]]
- 005a427c ["CALL", null, ["callee:0043b7b8:8"]]
+ 005a42bc ["INT_ADD", "register:40f0:8", ["const:5a42bc:8", "const:4:8"]]
+ 005a42bc ["CALL", null, ["callee:0043b7b8:8"]]
- 005a427c bytes 3f5dfa97
+ 005a42bc bytes 3f5dfa97
- 005a4278 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 005a4278 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005a4278 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005a4278 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005a42b8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 005a42b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005a42b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005a42b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005a4278 bytes 00303d91
+ 005a42b8 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d8c979efb85de260fd000bfc7d8aa78"></a>

### [`005a4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md) → [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) FUN_005a4498

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 19件 [`005a3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md) [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md) [`0079cf74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079c/0079cf74.md) [`0079d5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d5cc.md) [`007a0034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0034.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 19件 [`005a3360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a3/005a3360.md) [`005a42e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42e0.md) [`0079cfcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md) [`0079d624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d624.md) [`007a008c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a008c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "005a44a4",
      "incomplete_value": false,
      "site": "005a44a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4464",
      "incomplete_value": false,
      "site": "005a4468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:f4c:8"
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
      "005a44a4",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a44a4",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md#insn-005a4468) · [`005a4464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4458.md#insn-005a4464)
- 新版 `005a44a8`（命令位置の公開資料なし） · `005a44a4`（命令位置の公開資料なし）

~~~diff
- 005a4468 ["INT_ADD", "register:40f0:8", ["const:5a4468:8", "const:4:8"]]
- 005a4468 ["CALL", null, ["callee:0043b7b8:8"]]
+ 005a44a8 ["INT_ADD", "register:40f0:8", ["const:5a44a8:8", "const:4:8"]]
+ 005a44a8 ["CALL", null, ["callee:0043b7b8:8"]]
- 005a4468 bytes c45cfa97
+ 005a44a8 bytes c45cfa97
- 005a4464 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 005a4464 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005a4464 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005a4464 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005a44a4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 005a44a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005a44a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005a44a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005a4464 bytes 00303d91
+ 005a44a4 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbc1b2aea698157ca26bebf7a2572057"></a>

### [`005a491c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a491c.md) → [`005a495c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a495c.md) FUN_005a495c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005a3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a3/005a3320.md) · 呼出先 3件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`005a40e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a40e4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005a3360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a3/005a3360.md) · 呼出先 3件 [`0059b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b91c.md) [`005a4124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4124.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a49dc",
      "incomplete_value": false,
      "site": "005a49dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a499c",
      "incomplete_value": false,
      "site": "005a499c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a49a0",
      "DATA",
      [
        "storage",
        "00c6e8b8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a49dc",
      "DATA",
      [
        "storage",
        "00c6e7e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a49a0",
      "DATA",
      [
        "storage",
        "00c6e988",
        null,
        "undefined *"
      ]
    ],
    [
      "005a49dc",
      "DATA",
      [
        "storage",
        "00c6e8b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a491c.md#insn-005a4944) · [`005a4954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a491c.md#insn-005a4954) · [`005a496c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a491c.md#insn-005a496c)
- 新版 `005a4984`（命令位置の公開資料なし） · `005a4994`（命令位置の公開資料なし） · `005a49ac`（命令位置の公開資料なし）

~~~diff
- 005a4944 ["INT_ADD", "register:40f0:8", ["const:5a4944:8", "const:4:8"]]
- 005a4944 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a4984 ["INT_ADD", "register:40f0:8", ["const:5a4984:8", "const:4:8"]]
+ 005a4984 ["CALL", null, ["callee:00c57f60:8"]]
- 005a4944 bytes 53cd1a94
+ 005a4984 bytes 77cd1a94
- 005a4954 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 005a4954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a4954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a4954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a4994 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 005a4994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a4954 bytes 08e12291
+ 005a4994 bytes 08212691
- 005a496c ["INT_ADD", "register:40f0:8", ["const:5a496c:8", "const:4:8"]]
- 005a496c ["CALL", null, ["callee:0059b91c:8"]]
+ 005a49ac ["INT_ADD", "register:40f0:8", ["const:5a49ac:8", "const:4:8"]]
+ 005a49ac ["CALL", null, ["callee:0059b91c:8"]]
- 005a496c bytes dcdbff97
+ 005a49ac bytes dcdbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9c7b7c60affc7b3746531a4983489f9"></a>

### [`005a49fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a49fc.md) → [`005a4a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4a3c.md) FUN_005a4a3c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a4a40",
      "incomplete_value": false,
      "site": "005a4a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4a00",
      "incomplete_value": false,
      "site": "005a4a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
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
      "005a4a44",
      "DATA",
      [
        "storage",
        "00c6e8b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a4a44",
      "DATA",
      [
        "storage",
        "00c6e988",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a49fc.md#insn-005a4a00)
- 新版 `005a4a40`（命令位置の公開資料なし）

~~~diff
- 005a4a00 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 005a4a00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a4a00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a4a00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a4a40 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 005a4a40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4a40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4a40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a4a00 bytes 08e12291
+ 005a4a40 bytes 08212691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c931e46f0bb8b18c2bc987bf31860f8"></a>

### [`005a4a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4a3c.md) → [`005a4a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4a7c.md) FUN_005a4a7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a4548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4548.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a4ab0",
      "incomplete_value": false,
      "site": "005a4ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4a70",
      "incomplete_value": false,
      "site": "005a4a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "005a4ab4",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a4ab4",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4a3c.md#insn-005a4a5c) · [`005a4a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4a3c.md#insn-005a4a64) · [`005a4a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4a3c.md#insn-005a4a70)
- 新版 `005a4a9c`（命令位置の公開資料なし） · `005a4aa4`（命令位置の公開資料なし） · `005a4ab0`（命令位置の公開資料なし）

~~~diff
- 005a4a5c ["INT_ADD", "register:40f0:8", ["const:5a4a5c:8", "const:4:8"]]
- 005a4a5c ["CALL", null, ["callee:005a4548:8"]]
+ 005a4a9c ["INT_ADD", "register:40f0:8", ["const:5a4a9c:8", "const:4:8"]]
+ 005a4a9c ["CALL", null, ["callee:005a4548:8"]]
- 005a4a5c bytes abfeff97
+ 005a4a9c bytes abfeff97
- 005a4a64 ["INT_ADD", "register:40f0:8", ["const:5a4a64:8", "const:4:8"]]
- 005a4a64 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a4aa4 ["INT_ADD", "register:40f0:8", ["const:5a4aa4:8", "const:4:8"]]
+ 005a4aa4 ["CALL", null, ["callee:00c57f80:8"]]
- 005a4a64 bytes 13cd1a94
+ 005a4aa4 bytes 37cd1a94
- 005a4a70 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a4a70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a4a70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a4a70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a4ab0 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a4ab0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a4ab0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a4ab0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a4a70 bytes 29012891
+ 005a4ab0 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64cc03f9f6929000bfc10d814fe7ba3c"></a>

### [`005a4a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4a9c.md) → [`005a4adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4adc.md) FUN_005a4adc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a4ae0",
      "incomplete_value": false,
      "site": "005a4ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4aa0",
      "incomplete_value": false,
      "site": "005a4aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "005a4ae4",
      "DATA",
      [
        "storage",
        "00c6e908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a4ae4",
      "DATA",
      [
        "storage",
        "00c6e9d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4a9c.md#insn-005a4aa0)
- 新版 `005a4ae0`（命令位置の公開資料なし）

~~~diff
- 005a4aa0 ["COPY", "tmp:0:8", ["const:908:8"]]
- 005a4aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a4aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a4aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a4ae0 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 005a4ae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4ae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4ae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a4aa0 bytes 08212491
+ 005a4ae0 bytes 08612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b49590edf3d29cf910c34260fdb9203"></a>

### [`005a4aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4aac.md) → [`005a4aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4aec.md) FUN_005a4aec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a4afc",
      "incomplete_value": true,
      "site": "005a4b04",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4abc",
      "incomplete_value": true,
      "site": "005a4ac4",
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
            "const:908:8"
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
      "005a4b04",
      "DATA",
      [
        "storage",
        "00c6e908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a4b04",
      "DATA",
      [
        "storage",
        "00c6e9d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4aac.md#insn-005a4abc) · [`005a4ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4aac.md#insn-005a4ac8)
- 新版 `005a4afc`（命令位置の公開資料なし） · `005a4b08`（命令位置の公開資料なし）

~~~diff
- 005a4abc ["COPY", "tmp:0:8", ["const:908:8"]]
- 005a4abc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a4abc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a4abc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a4afc ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 005a4afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a4afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a4abc bytes 08212491
+ 005a4afc bytes 08612791
- 005a4ac8 ["INT_ADD", "register:40f0:8", ["const:5a4ac8:8", "const:4:8"]]
- 005a4ac8 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a4b08 ["INT_ADD", "register:40f0:8", ["const:5a4b08:8", "const:4:8"]]
+ 005a4b08 ["CALL", null, ["callee:00c57f70:8"]]
- 005a4ac8 bytes f6cc1a94
+ 005a4b08 bytes 1acd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82d57c416de305f215dadc4f9ba4a914"></a>

### [`005a4ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4ae4.md) → [`005a4b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4b24.md) _INIT_49

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a4be0",
      "incomplete_value": true,
      "site": "005a4bfc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:576:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a4ba0",
      "incomplete_value": true,
      "site": "005a4bbc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:5d2:8"
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
      "005a4b60",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a4b84",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a4ba4",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a4b60",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005a4b84",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005a4ba4",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a4b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4ae4.md#insn-005a4b7c) · [`005a4b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4ae4.md#insn-005a4b10) · [`005a4b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4ae4.md#insn-005a4b18)
- 新版 `005a4bbc`（命令位置の公開資料なし） · `005a4b50`（命令位置の公開資料なし）

~~~diff
- 005a4b7c ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005a4b7c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a4b7c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a4b7c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a4bbc ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005a4bbc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a4bbc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a4bbc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a4b7c bytes 4a893d91
+ 005a4bbc bytes 4a553c91
- 005a4b10 ["COPY", "tmp:0:8", ["const:720:8"]]
- 005a4b10 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005a4b10 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005a4b10 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005a4b50 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 005a4b50 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005a4b50 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005a4b50 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005a4b10 bytes 73821c91
+ 005a4b50 bytes 73822091
- 005a4b18 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 005a4b18 bytes 89e8fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62a57e22f7f4be7dcc4c4364596a39e8"></a>

### [`005a5018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5018.md) → [`005a5058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5058.md) FUN_005a5058

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`007adf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)
- 新版 呼出元 1件 [`007adf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007adf74.md) · 呼出先 1件 [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md)

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
      "definition_site": "005a5074",
      "incomplete_value": false,
      "site": "005a5078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5034",
      "incomplete_value": false,
      "site": "005a5038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      "005a5078",
      "DATA",
      [
        "storage",
        "00c6e978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5078",
      "DATA",
      [
        "storage",
        "00c6ea48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a502c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5018.md#insn-005a502c) · [`005a5034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5018.md#insn-005a5034)
- 新版 `005a506c`（命令位置の公開資料なし） · `005a5074`（命令位置の公開資料なし）

~~~diff
- 005a502c ["INT_ADD", "register:40f0:8", ["const:5a502c:8", "const:4:8"]]
- 005a502c ["CALL", null, ["callee:0059b948:8"]]
+ 005a506c ["INT_ADD", "register:40f0:8", ["const:5a506c:8", "const:4:8"]]
+ 005a506c ["CALL", null, ["callee:0059b948:8"]]
- 005a502c bytes 37daff97
+ 005a506c bytes 37daff97
- 005a5034 ["COPY", "tmp:0:8", ["const:978:8"]]
- 005a5034 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5034 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5034 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5074 ["COPY", "tmp:0:8", ["const:a48:8"]]
+ 005a5074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5034 bytes 08e12591
+ 005a5074 bytes 08212991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af9c27d8b303b70d7c33780574d3f48e"></a>

### [`005a5064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5064.md) → [`005a50a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a50a4.md) FUN_005a50a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "005a50b0",
      "incomplete_value": true,
      "site": "005a50c0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:23:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5070",
      "incomplete_value": true,
      "site": "005a5080",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b4000:8"
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
      "005a50b0",
      "READ",
      [
        "storage",
        "002b4ff2",
        null,
        "string"
      ]
    ],
    [
      "005a50b8",
      "READ",
      [
        "storage",
        "002b5000",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a50b0",
      "READ",
      [
        "storage",
        "002b5023",
        null,
        "string"
      ]
    ],
    [
      "005a50b8",
      "READ",
      [
        "storage",
        "002b5031",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5064.md#insn-005a5068) · [`005a506c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5064.md#insn-005a506c)
- 新版 `005a50a8`（命令位置の公開資料なし） · `005a50ac`（命令位置の公開資料なし）

~~~diff
- 005a5068 ["COPY", "register:4050:8", ["const:2b4000:8"]]
+ 005a50a8 ["COPY", "register:4050:8", ["const:2b5000:8"]]
- 005a5068 bytes 6ae8fff0
+ 005a50a8 bytes 8ae8ff90
- 005a506c ["COPY", "tmp:0:8", ["const:ff2:8"]]
- 005a506c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a506c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a506c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a50ac ["COPY", "tmp:0:8", ["const:23:8"]]
+ 005a50ac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a50ac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a50ac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a506c bytes 4ac93f91
+ 005a50ac bytes 4a8d0091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f44eab40f69f672217b4a20b371b83fc"></a>

### [`005a5190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5190.md) → [`005a51d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a51d0.md) FUN_005a51d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a51ec",
      "incomplete_value": false,
      "site": "005a51f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a51ac",
      "incomplete_value": false,
      "site": "005a51b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "definition_site": "005a5204",
      "incomplete_value": false,
      "site": "005a5204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a51c4",
      "incomplete_value": false,
      "site": "005a51c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
      "005a51f4",
      "DATA",
      [
        "storage",
        "00c6ea80",
        null,
        "undefined *"
      ]
    ],
    [
      "005a5204",
      "DATA",
      [
        "storage",
        "00c6e9d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a51f4",
      "DATA",
      [
        "storage",
        "00c6eb50",
        null,
        "undefined *"
      ]
    ],
    [
      "005a5204",
      "DATA",
      [
        "storage",
        "00c6eaa0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a51a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5190.md#insn-005a51a4) · [`005a51ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5190.md#insn-005a51ac) · [`005a51b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5190.md#insn-005a51b8)
- 新版 `005a51e4`（命令位置の公開資料なし） · `005a51ec`（命令位置の公開資料なし）

~~~diff
- 005a51a4 ["INT_ADD", "register:40f0:8", ["const:5a51a4:8", "const:4:8"]]
- 005a51a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a51e4 ["INT_ADD", "register:40f0:8", ["const:5a51e4:8", "const:4:8"]]
+ 005a51e4 ["CALL", null, ["callee:00c57f60:8"]]
- 005a51a4 bytes 3bcb1a94
+ 005a51e4 bytes 5fcb1a94
- 005a51ac ["COPY", "tmp:0:8", ["const:a80:8"]]
- 005a51ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a51ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a51ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a51ec ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 005a51ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a51ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a51ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a51ac bytes 08012a91
+ 005a51ec bytes 08412d91
- 005a51b8 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005a51b8 bytes 483600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-791730bfff5c0e59d35863b59893f368"></a>

### [`005a51d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a51d8.md) → [`005a5218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5218.md) FUN_005a5218

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5244",
      "incomplete_value": false,
      "site": "005a5248",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
      "definition_site": "005a5204",
      "incomplete_value": false,
      "site": "005a5208",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a5248",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5248",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a51f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a51d8.md#insn-005a51f4) · [`005a51fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a51d8.md#insn-005a51fc) · [`005a5214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a51d8.md#insn-005a5214)
- 新版 `005a5234`（命令位置の公開資料なし） · `005a523c`（命令位置の公開資料なし） · `005a5254`（命令位置の公開資料なし）

~~~diff
- 005a51f4 ["INT_ADD", "register:40f0:8", ["const:5a51f4:8", "const:4:8"]]
- 005a51f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a5234 ["INT_ADD", "register:40f0:8", ["const:5a5234:8", "const:4:8"]]
+ 005a5234 ["CALL", null, ["callee:00c57f80:8"]]
- 005a51f4 bytes 2fcb1a94
+ 005a5234 bytes 53cb1a94
- 005a51fc ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005a51fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a51fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a51fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a523c ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005a523c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a523c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a523c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a51fc bytes 08412891
+ 005a523c bytes 08812b91
- 005a5214 ["INT_ADD", "register:40f0:8", ["const:5a5214:8", "const:4:8"]]
- 005a5214 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a5254 ["INT_ADD", "register:40f0:8", ["const:5a5254:8", "const:4:8"]]
+ 005a5254 ["CALL", null, ["callee:00c57f80:8"]]
- 005a5214 bytes 27cb1a94
+ 005a5254 bytes 4bcb1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10bcaebb09a6bd457c146a363b9772e7"></a>

### [`005a523c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a523c.md) → [`005a527c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a527c.md) FUN_005a527c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a52a8",
      "incomplete_value": false,
      "site": "005a52ac",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
      "definition_site": "005a5268",
      "incomplete_value": false,
      "site": "005a526c",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a52ac",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a52ac",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a523c.md#insn-005a5258) · [`005a5260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a523c.md#insn-005a5260) · [`005a5278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a523c.md#insn-005a5278)
- 新版 `005a5298`（命令位置の公開資料なし） · `005a52a0`（命令位置の公開資料なし） · `005a52b8`（命令位置の公開資料なし）

~~~diff
- 005a5258 ["INT_ADD", "register:40f0:8", ["const:5a5258:8", "const:4:8"]]
- 005a5258 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a5298 ["INT_ADD", "register:40f0:8", ["const:5a5298:8", "const:4:8"]]
+ 005a5298 ["CALL", null, ["callee:00c57f80:8"]]
- 005a5258 bytes 16cb1a94
+ 005a5298 bytes 3acb1a94
- 005a5260 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005a5260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a52a0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005a52a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a52a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a52a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5260 bytes 08412891
+ 005a52a0 bytes 08812b91
- 005a5278 ["INT_ADD", "register:40f0:8", ["const:5a5278:8", "const:4:8"]]
- 005a5278 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a52b8 ["INT_ADD", "register:40f0:8", ["const:5a52b8:8", "const:4:8"]]
+ 005a52b8 ["CALL", null, ["callee:00c57f80:8"]]
- 005a5278 bytes 0ecb1a94
+ 005a52b8 bytes 32cb1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0110c81839e6d979cc088699acd88c3d"></a>

### [`005a529c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a529c.md) → [`005a52dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a52dc.md) FUN_005a52dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a52e4",
      "incomplete_value": false,
      "site": "005a52e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a52a4",
      "incomplete_value": false,
      "site": "005a52a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a52e8",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a52e8",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a52a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a529c.md#insn-005a52a4) · [`005a52c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a529c.md#insn-005a52c8)
- 新版 `005a52e4`（命令位置の公開資料なし） · `005a5308`（命令位置の公開資料なし）

~~~diff
- 005a52a4 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a52a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a52a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a52a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a52e4 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a52e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a52e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a52e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a52a4 bytes 29012891
+ 005a52e4 bytes 29412b91
- 005a52c8 ["INT_ADD", "register:40f0:8", ["const:5a52c8:8", "const:4:8"]]
- 005a52c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a5308 ["INT_ADD", "register:40f0:8", ["const:5a5308:8", "const:4:8"]]
+ 005a5308 ["CALL", null, ["callee:00c57f80:8"]]
- 005a52c8 bytes faca1a94
+ 005a5308 bytes 1ecb1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcdf1262d6db151ab985b35a6eb22ff7"></a>

### [`005a52dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a52dc.md) → [`005a531c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a531c.md) FUN_005a531c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005a4e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a4e74.md) · 呼出先 4件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005a4eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4eb4.md) · 呼出先 4件 [`0059b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b91c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5358",
      "incomplete_value": false,
      "site": "005a5360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5318",
      "incomplete_value": false,
      "site": "005a5320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "definition_site": "005a539c",
      "incomplete_value": false,
      "site": "005a53a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a535c",
      "incomplete_value": false,
      "site": "005a5360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "005a5360",
      "DATA",
      [
        "storage",
        "00c6ea30",
        null,
        "undefined *"
      ]
    ],
    [
      "005a53a0",
      "DATA",
      [
        "storage",
        "00c6e958",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a5360",
      "DATA",
      [
        "storage",
        "00c6eb00",
        null,
        "undefined *"
      ]
    ],
    [
      "005a53a0",
      "DATA",
      [
        "storage",
        "00c6ea28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a52dc.md#insn-005a5310) · [`005a5318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a52dc.md#insn-005a5318) · [`005a5350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a52dc.md#insn-005a5350)
- 新版 `005a5350`（命令位置の公開資料なし） · `005a5358`（命令位置の公開資料なし） · `005a5390`（命令位置の公開資料なし）

~~~diff
- 005a5310 ["INT_ADD", "register:40f0:8", ["const:5a5310:8", "const:4:8"]]
- 005a5310 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a5350 ["INT_ADD", "register:40f0:8", ["const:5a5350:8", "const:4:8"]]
+ 005a5350 ["CALL", null, ["callee:00c57f60:8"]]
- 005a5310 bytes e0ca1a94
+ 005a5350 bytes 04cb1a94
- 005a5318 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 005a5318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5358 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 005a5358 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5358 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5358 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5318 bytes 08c12891
+ 005a5358 bytes 08012c91
- 005a5350 ["INT_ADD", "register:40f0:8", ["const:5a5350:8", "const:4:8"]]
- 005a5350 ["CALL", null, ["callee:0059b91c:8"]]
+ 005a5390 ["INT_ADD", "register:40f0:8", ["const:5a5390:8", "const:4:8"]]
+ 005a5390 ["CALL", null, ["callee:0059b91c:8"]]
- 005a5350 bytes 63d9ff97
+ 005a5390 bytes 63d9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80979ad388abb9cf8e74082408b84448"></a>

### [`005a53dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a53dc.md) → [`005a541c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a541c.md) FUN_005a541c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a5420",
      "incomplete_value": false,
      "site": "005a5424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a53e0",
      "incomplete_value": false,
      "site": "005a53e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a5424",
      "DATA",
      [
        "storage",
        "00c6ea30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5424",
      "DATA",
      [
        "storage",
        "00c6eb00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a53e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a53dc.md#insn-005a53e0)
- 新版 `005a5420`（命令位置の公開資料なし）

~~~diff
- 005a53e0 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 005a53e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a53e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a53e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5420 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 005a5420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a53e0 bytes 08c12891
+ 005a5420 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd6619c9cf7d5f1e00a2b32d4ec0245"></a>

### [`005a53ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a53ec.md) → [`005a542c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a542c.md) FUN_005a542c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a543c",
      "incomplete_value": false,
      "site": "005a5444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a53fc",
      "incomplete_value": false,
      "site": "005a5404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a5444",
      "DATA",
      [
        "storage",
        "00c6ea30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5444",
      "DATA",
      [
        "storage",
        "00c6eb00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a53fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a53ec.md#insn-005a53fc) · [`005a5408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a53ec.md#insn-005a5408)
- 新版 `005a543c`（命令位置の公開資料なし） · `005a5448`（命令位置の公開資料なし）

~~~diff
- 005a53fc ["COPY", "tmp:0:8", ["const:a30:8"]]
- 005a53fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a53fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a53fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a543c ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 005a543c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a543c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a543c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a53fc bytes 08c12891
+ 005a543c bytes 08012c91
- 005a5408 ["INT_ADD", "register:40f0:8", ["const:5a5408:8", "const:4:8"]]
- 005a5408 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a5448 ["INT_ADD", "register:40f0:8", ["const:5a5448:8", "const:4:8"]]
+ 005a5448 ["CALL", null, ["callee:00c57f70:8"]]
- 005a5408 bytes a6ca1a94
+ 005a5448 bytes caca1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4528066c162a7503131b1dde0efca36"></a>

### [`005a541c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a541c.md) → [`005a545c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a545c.md) FUN_005a545c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a5464",
      "incomplete_value": false,
      "site": "005a5468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5424",
      "incomplete_value": false,
      "site": "005a5428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a5468",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a5468",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a541c.md#insn-005a5424)
- 新版 `005a5464`（命令位置の公開資料なし）

~~~diff
- 005a5424 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a5424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a5424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a5424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a5464 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a5464 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5464 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5464 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a5424 bytes 29012891
+ 005a5464 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e1ad52c121f0caeb26c985c9983314d"></a>

### [`005a5440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5440.md) → [`005a5480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5480.md) FUN_005a5480

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a5484",
      "incomplete_value": false,
      "site": "005a5488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5444",
      "incomplete_value": false,
      "site": "005a5448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "005a5488",
      "DATA",
      [
        "storage",
        "00c6ea80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5488",
      "DATA",
      [
        "storage",
        "00c6eb50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5440.md#insn-005a5444)
- 新版 `005a5484`（命令位置の公開資料なし）

~~~diff
- 005a5444 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 005a5444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5484 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 005a5484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5444 bytes 08012a91
+ 005a5484 bytes 08412d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17805acc56e7e2807c82e95f4ab732b2"></a>

### [`005a5450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5450.md) → [`005a5490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5490.md) FUN_005a5490

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a54a0",
      "incomplete_value": true,
      "site": "005a54a8",
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
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5460",
      "incomplete_value": true,
      "site": "005a5468",
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
            "const:a80:8"
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
      "005a54a8",
      "DATA",
      [
        "storage",
        "00c6ea80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a54a8",
      "DATA",
      [
        "storage",
        "00c6eb50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5450.md#insn-005a5460) · [`005a546c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5450.md#insn-005a546c)
- 新版 `005a54a0`（命令位置の公開資料なし） · `005a54ac`（命令位置の公開資料なし）

~~~diff
- 005a5460 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 005a5460 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5460 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5460 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a54a0 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 005a54a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a54a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a54a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5460 bytes 08012a91
+ 005a54a0 bytes 08412d91
- 005a546c ["INT_ADD", "register:40f0:8", ["const:5a546c:8", "const:4:8"]]
- 005a546c ["CALL", null, ["callee:00c57f70:8"]]
+ 005a54ac ["INT_ADD", "register:40f0:8", ["const:5a54ac:8", "const:4:8"]]
+ 005a54ac ["CALL", null, ["callee:00c57f70:8"]]
- 005a546c bytes 8dca1a94
+ 005a54ac bytes b1ca1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1fffa5b7dc87bbe0a28f6f098b488fe"></a>

### [`005a5488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5488.md) → [`005a54c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a54c8.md) _INIT_50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5504",
      "incomplete_value": true,
      "site": "005a5520",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a54c4",
      "incomplete_value": true,
      "site": "005a54e0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f26:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a56e8",
      "incomplete_value": false,
      "site": "005a56fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a56a8",
      "incomplete_value": false,
      "site": "005a56bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      "definition_site": "005a56f0",
      "incomplete_value": false,
      "site": "005a56fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a56b0",
      "incomplete_value": false,
      "site": "005a56bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:738:8"
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
      "005a5504",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a5528",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a5548",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a5504",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005a5528",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005a5548",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5488.md#insn-005a5520) · [`005a56bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5488.md#insn-005a56bc) · [`005a54b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5488.md#insn-005a54b4)
- 新版 `005a5560`（命令位置の公開資料なし） · `005a56fc`（命令位置の公開資料なし） · `005a54f4`（命令位置の公開資料なし）

~~~diff
- 005a5520 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005a5520 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a5520 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a5520 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a5560 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005a5560 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5560 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5560 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a5520 bytes 4a893d91
+ 005a5560 bytes 4a553c91
- 005a56bc ["INT_ADD", "register:40f0:8", ["const:5a56bc:8", "const:4:8"]]
- 005a56bc ["CALL", null, ["callee:00c57f00:8"]]
+ 005a56fc ["INT_ADD", "register:40f0:8", ["const:5a56fc:8", "const:4:8"]]
+ 005a56fc ["CALL", null, ["callee:00c57f00:8"]]
- 005a56bc bytes ddc91a94
+ 005a56fc bytes 01ca1a94
- 005a54b4 ["COPY", "tmp:0:8", ["const:738:8"]]
- 005a54b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005a54b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005a54b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005a54f4 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 005a54f4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005a54f4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005a54f4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005a54b4 bytes 73e21c91
+ 005a54f4 bytes 73e22091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16f9fbea8a7dd08e6eec60d5132c9145"></a>

### [`005a59bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a59bc.md) → [`005a59fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a59fc.md) FUN_005a59fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`007ad324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)
- 新版 呼出元 1件 [`007ad37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad37c.md) · 呼出先 1件 [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md)

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
      "definition_site": "005a5a18",
      "incomplete_value": false,
      "site": "005a5a1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a59d8",
      "incomplete_value": false,
      "site": "005a59dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:af0:8"
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
      "005a5a1c",
      "DATA",
      [
        "storage",
        "00c6eaf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5a1c",
      "DATA",
      [
        "storage",
        "00c6ebc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a59d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a59bc.md#insn-005a59d0) · [`005a59d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a59bc.md#insn-005a59d8)
- 新版 `005a5a10`（命令位置の公開資料なし） · `005a5a18`（命令位置の公開資料なし）

~~~diff
- 005a59d0 ["INT_ADD", "register:40f0:8", ["const:5a59d0:8", "const:4:8"]]
- 005a59d0 ["CALL", null, ["callee:0059b948:8"]]
+ 005a5a10 ["INT_ADD", "register:40f0:8", ["const:5a5a10:8", "const:4:8"]]
+ 005a5a10 ["CALL", null, ["callee:0059b948:8"]]
- 005a59d0 bytes ced7ff97
+ 005a5a10 bytes ced7ff97
- 005a59d8 ["COPY", "tmp:0:8", ["const:af0:8"]]
- 005a59d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a59d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a59d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5a18 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 005a5a18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5a18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5a18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a59d8 bytes 08c12b91
+ 005a5a18 bytes 08012f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-765c7c3c5a5c18b3a6502b6bbbc12b89"></a>

### [`005a5a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5a08.md) → [`005a5a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5a48.md) FUN_005a5a48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5a64",
      "incomplete_value": true,
      "site": "005a5a64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5a24",
      "incomplete_value": true,
      "site": "005a5a24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5a68",
      "incomplete_value": true,
      "site": "005a5a68",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005a5a28",
      "incomplete_value": true,
      "site": "005a5a28",
      "value": [
        "LOAD",
        "8",
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
      "005a5a54",
      "READ",
      [
        "storage",
        "002a5714",
        null,
        "string"
      ]
    ],
    [
      "005a5a5c",
      "READ",
      [
        "storage",
        "002a5719",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a5a54",
      "READ",
      [
        "storage",
        "002a56b8",
        null,
        "string"
      ]
    ],
    [
      "005a5a5c",
      "READ",
      [
        "storage",
        "002a56bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5a08.md#insn-005a5a10)
- 新版 `005a5a50`（命令位置の公開資料なし）

~~~diff
- 005a5a10 ["COPY", "tmp:0:8", ["const:714:8"]]
- 005a5a10 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a5a10 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a5a10 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a5a50 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 005a5a50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5a50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5a50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a5a10 bytes 4a511c91
+ 005a5a50 bytes 4ae11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d97afda0a2cdd210897d3bf158c810d8"></a>

### [`005a5a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5a60.md) → [`005a5aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5aa0.md) FUN_005a5aa0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bf44.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`0059bf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059bf84.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5af0",
      "incomplete_value": true,
      "site": "005a5af0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:b2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5ab0",
      "incomplete_value": true,
      "site": "005a5ab0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:b88:8"
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
      "005a5adc",
      "READ",
      [
        "storage",
        "002afb88",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a5adc",
      "READ",
      [
        "storage",
        "002afb2c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5a60.md#insn-005a5a8c) · [`005a5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5a60.md#insn-005a5a94) · [`005a5ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5a60.md#insn-005a5ac0)
- 新版 `005a5acc`（命令位置の公開資料なし） · `005a5ad4`（命令位置の公開資料なし） · `005a5b00`（命令位置の公開資料なし）

~~~diff
- 005a5a8c ["INT_ADD", "register:40f0:8", ["const:5a5a8c:8", "const:4:8"]]
- 005a5a8c ["CALL", null, ["callee:0059bf84:8"]]
+ 005a5acc ["INT_ADD", "register:40f0:8", ["const:5a5acc:8", "const:4:8"]]
+ 005a5acc ["CALL", null, ["callee:0059bf84:8"]]
- 005a5a8c bytes 2ed9ff97
+ 005a5acc bytes 2ed9ff97
- 005a5a94 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 005a5a94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a5a94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a5a94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a5ad4 ["COPY", "tmp:0:8", ["const:b2c:8"]]
+ 005a5ad4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5ad4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5ad4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a5a94 bytes 29212e91
+ 005a5ad4 bytes 29b12c91
- 005a5ac0 ["INT_ADD", "register:40f0:8", ["const:5a5ac0:8", "const:4:8"]]
- 005a5ac0 ["CALL", null, ["callee:004517dc:8"]]
+ 005a5b00 ["INT_ADD", "register:40f0:8", ["const:5a5b00:8", "const:4:8"]]
+ 005a5b00 ["CALL", null, ["callee:004517dc:8"]]
- 005a5ac0 bytes 37affa97
+ 005a5b00 bytes 37affa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-780809b4e4d66133b0a90a493aadaddf"></a>

### [`005a5b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5b30.md) → [`005a5b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5b70.md) FUN_005a5b70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5b8c",
      "incomplete_value": false,
      "site": "005a5b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5b4c",
      "incomplete_value": false,
      "site": "005a5b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "definition_site": "005a5ba4",
      "incomplete_value": false,
      "site": "005a5ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5b64",
      "incomplete_value": false,
      "site": "005a5b64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "005a5b94",
      "DATA",
      [
        "storage",
        "00c6ebf8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a5ba4",
      "DATA",
      [
        "storage",
        "00c6eb48",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a5b94",
      "DATA",
      [
        "storage",
        "00c6ecc8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a5ba4",
      "DATA",
      [
        "storage",
        "00c6ec18",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5b30.md#insn-005a5b44) · [`005a5b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5b30.md#insn-005a5b4c) · [`005a5b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5b30.md#insn-005a5b5c)
- 新版 `005a5b84`（命令位置の公開資料なし） · `005a5b8c`（命令位置の公開資料なし） · `005a5b9c`（命令位置の公開資料なし）

~~~diff
- 005a5b44 ["INT_ADD", "register:40f0:8", ["const:5a5b44:8", "const:4:8"]]
- 005a5b44 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a5b84 ["INT_ADD", "register:40f0:8", ["const:5a5b84:8", "const:4:8"]]
+ 005a5b84 ["CALL", null, ["callee:00c57f60:8"]]
- 005a5b44 bytes d3c81a94
+ 005a5b84 bytes f7c81a94
- 005a5b4c ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 005a5b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5b8c ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 005a5b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5b4c bytes 08e12f91
+ 005a5b8c bytes 08213391
- 005a5b5c ["COPY", "tmp:0:8", ["const:b48:8"]]
- 005a5b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5b9c ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 005a5b9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5b9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5b9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5b5c bytes 08212d91
+ 005a5b9c bytes 08613091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b4c0ce6a0086025a81927089dbe9d6a"></a>

### [`005a5c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5c3c.md) → [`005a5c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5c7c.md) FUN_005a5c7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a5c84",
      "incomplete_value": false,
      "site": "005a5c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5c44",
      "incomplete_value": false,
      "site": "005a5c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a5c88",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a5c88",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5c3c.md#insn-005a5c44) · [`005a5c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5c3c.md#insn-005a5c68)
- 新版 `005a5c84`（命令位置の公開資料なし） · `005a5ca8`（命令位置の公開資料なし）

~~~diff
- 005a5c44 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a5c44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a5c44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a5c44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a5c84 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a5c84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5c84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5c84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a5c44 bytes 29012891
+ 005a5c84 bytes 29412b91
- 005a5c68 ["INT_ADD", "register:40f0:8", ["const:5a5c68:8", "const:4:8"]]
- 005a5c68 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a5ca8 ["INT_ADD", "register:40f0:8", ["const:5a5ca8:8", "const:4:8"]]
+ 005a5ca8 ["CALL", null, ["callee:00c57f80:8"]]
- 005a5c68 bytes 92c81a94
+ 005a5ca8 bytes b6c81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72d5b10f338962c303b9797c06ad23a2"></a>

### [`005a5c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5c7c.md) → [`005a5cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5cbc.md) FUN_005a5cbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005a5818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5818.md) · 呼出先 4件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005a5858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5858.md) · 呼出先 4件 [`0059b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b91c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5cf8",
      "incomplete_value": false,
      "site": "005a5d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5cb8",
      "incomplete_value": false,
      "site": "005a5cc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "definition_site": "005a5d3c",
      "incomplete_value": false,
      "site": "005a5d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5cfc",
      "incomplete_value": false,
      "site": "005a5d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "005a5d00",
      "DATA",
      [
        "storage",
        "00c6eba8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a5d40",
      "DATA",
      [
        "storage",
        "00c6ead0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a5d00",
      "DATA",
      [
        "storage",
        "00c6ec78",
        null,
        "undefined *"
      ]
    ],
    [
      "005a5d40",
      "DATA",
      [
        "storage",
        "00c6eba0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5c7c.md#insn-005a5cb0) · [`005a5cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5c7c.md#insn-005a5cb8) · [`005a5cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5c7c.md#insn-005a5cf0)
- 新版 `005a5cf0`（命令位置の公開資料なし） · `005a5cf8`（命令位置の公開資料なし） · `005a5d30`（命令位置の公開資料なし）

~~~diff
- 005a5cb0 ["INT_ADD", "register:40f0:8", ["const:5a5cb0:8", "const:4:8"]]
- 005a5cb0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a5cf0 ["INT_ADD", "register:40f0:8", ["const:5a5cf0:8", "const:4:8"]]
+ 005a5cf0 ["CALL", null, ["callee:00c57f60:8"]]
- 005a5cb0 bytes 78c81a94
+ 005a5cf0 bytes 9cc81a94
- 005a5cb8 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 005a5cb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5cb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5cb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5cf8 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 005a5cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5cb8 bytes 08a12e91
+ 005a5cf8 bytes 08e13191
- 005a5cf0 ["INT_ADD", "register:40f0:8", ["const:5a5cf0:8", "const:4:8"]]
- 005a5cf0 ["CALL", null, ["callee:0059b91c:8"]]
+ 005a5d30 ["INT_ADD", "register:40f0:8", ["const:5a5d30:8", "const:4:8"]]
+ 005a5d30 ["CALL", null, ["callee:0059b91c:8"]]
- 005a5cf0 bytes fbd6ff97
+ 005a5d30 bytes fbd6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14cbc65cc2b502661cebddc8f4cd1e24"></a>

### [`005a5d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5d7c.md) → [`005a5dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5dbc.md) FUN_005a5dbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a5dc0",
      "incomplete_value": false,
      "site": "005a5dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5d80",
      "incomplete_value": false,
      "site": "005a5d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "005a5dc4",
      "DATA",
      [
        "storage",
        "00c6eba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5dc4",
      "DATA",
      [
        "storage",
        "00c6ec78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5d7c.md#insn-005a5d80)
- 新版 `005a5dc0`（命令位置の公開資料なし）

~~~diff
- 005a5d80 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 005a5d80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5d80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5d80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5dc0 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 005a5dc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5dc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5dc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5d80 bytes 08a12e91
+ 005a5dc0 bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae8a5f9862f94d1db1e7e4b9843a0ada"></a>

### [`005a5dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5dbc.md) → [`005a5dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5dfc.md) FUN_005a5dfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a5e04",
      "incomplete_value": false,
      "site": "005a5e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5dc4",
      "incomplete_value": false,
      "site": "005a5dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a5e08",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a5e08",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5dbc.md#insn-005a5dc4)
- 新版 `005a5e04`（命令位置の公開資料なし）

~~~diff
- 005a5dc4 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a5dc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a5dc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a5dc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a5e04 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a5e04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5e04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a5e04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a5dc4 bytes 29012891
+ 005a5e04 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b551130c84f919ffde06f0e3b2eaad5f"></a>

### [`005a5de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5de0.md) → [`005a5e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5e20.md) FUN_005a5e20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a5e24",
      "incomplete_value": false,
      "site": "005a5e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5de4",
      "incomplete_value": false,
      "site": "005a5de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a5e28",
      "DATA",
      [
        "storage",
        "00c6ebf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5e28",
      "DATA",
      [
        "storage",
        "00c6ecc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5de0.md#insn-005a5de4)
- 新版 `005a5e24`（命令位置の公開資料なし）

~~~diff
- 005a5de4 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 005a5de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5e24 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 005a5e24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5e24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5e24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5de4 bytes 08e12f91
+ 005a5e24 bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8be4f6ab45c396bdd58a0139ed511c94"></a>

### [`005a5df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5df0.md) → [`005a5e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5e30.md) FUN_005a5e30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a5e40",
      "incomplete_value": false,
      "site": "005a5e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5e00",
      "incomplete_value": false,
      "site": "005a5e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a5e48",
      "DATA",
      [
        "storage",
        "00c6ebf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a5e48",
      "DATA",
      [
        "storage",
        "00c6ecc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5df0.md#insn-005a5e00) · [`005a5e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5df0.md#insn-005a5e0c)
- 新版 `005a5e40`（命令位置の公開資料なし） · `005a5e4c`（命令位置の公開資料なし）

~~~diff
- 005a5e00 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 005a5e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a5e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a5e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a5e40 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 005a5e40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5e40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a5e40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a5e00 bytes 08e12f91
+ 005a5e40 bytes 08213391
- 005a5e0c ["INT_ADD", "register:40f0:8", ["const:5a5e0c:8", "const:4:8"]]
- 005a5e0c ["CALL", null, ["callee:00c57f70:8"]]
+ 005a5e4c ["INT_ADD", "register:40f0:8", ["const:5a5e4c:8", "const:4:8"]]
+ 005a5e4c ["CALL", null, ["callee:00c57f70:8"]]
- 005a5e0c bytes 25c81a94
+ 005a5e4c bytes 49c81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ec91d382064f2abc03e3f9b27fd7003"></a>

### [`005a5e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5e28.md) → [`005a5e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a5/005a5e68.md) _INIT_51

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.88% / 新版 85.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a5ec8",
      "incomplete_value": true,
      "site": "005a5ee4",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:4050:8"
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
    "old": {
      "definition_site": "005a5e88",
      "incomplete_value": true,
      "site": "005a5ea4",
      "value": [
        "LOAD",
        "16",
        [
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
                "register:4050:8"
              ],
              [
                "leaf",
                "const:f39:8"
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
      "definition_site": "005a5ee8",
      "incomplete_value": true,
      "site": "005a5f04",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5ea8",
      "incomplete_value": true,
      "site": "005a5ec4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:dc2:8"
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
      "definition_site": "005a5f08",
      "incomplete_value": true,
      "site": "005a5f20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a5ec8",
      "incomplete_value": true,
      "site": "005a5ee0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f62:8"
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
      "005a5ea4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a5ec8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a5ee8",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a5ea4",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005a5ec8",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005a5ee8",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a5ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5e28.md#insn-005a5ea0) · [`005a5ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5e28.md#insn-005a5ec0) · [`005a605c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a5/005a5e28.md#insn-005a605c)
- 新版 `005a5ee0`（命令位置の公開資料なし） · `005a5f00`（命令位置の公開資料なし） · `005a609c`（命令位置の公開資料なし）

~~~diff
- 005a5ea0 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 005a5ea0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a5ea0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a5ea0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a5ee0 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 005a5ee0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5ee0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5ee0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a5ea0 bytes 4a093791
+ 005a5ee0 bytes 4ab93591
- 005a5ec0 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005a5ec0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a5ec0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a5ec0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a5f00 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005a5f00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5f00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a5f00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a5ec0 bytes 4a893d91
+ 005a5f00 bytes 4a553c91
- 005a605c ["INT_ADD", "register:40f0:8", ["const:5a605c:8", "const:4:8"]]
- 005a605c ["CALL", null, ["callee:00c57f00:8"]]
+ 005a609c ["INT_ADD", "register:40f0:8", ["const:5a609c:8", "const:4:8"]]
+ 005a609c ["CALL", null, ["callee:00c57f00:8"]]
- 005a605c bytes 75c71a94
+ 005a609c bytes 99c71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-112c80d5543108b9903d23f69511a1e1"></a>

### [`005a61b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a61b8.md) → [`005a61f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a61f8.md) FUN_005a61f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005a6698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6698.md) [`005a6a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6a1c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`005a66d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a66d8.md) [`005a6a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a6a5c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.21% / 新版 96.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a6244",
      "incomplete_value": true,
      "site": "005a6244",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:1e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6204",
      "incomplete_value": true,
      "site": "005a6204",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:1a5:8"
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
      "definition_site": "005a637c",
      "incomplete_value": true,
      "site": "005a637c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:b2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a633c",
      "incomplete_value": true,
      "site": "005a633c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:b88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a6400",
      "incomplete_value": true,
      "site": "005a6400",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:62a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a63c0",
      "incomplete_value": true,
      "site": "005a63c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:686:8"
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
      "005a6228",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a636c",
      "READ",
      [
        "storage",
        "002afb88",
        null,
        "string"
      ]
    ],
    [
      "005a63f0",
      "READ",
      [
        "storage",
        "002a7686",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a6228",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "005a636c",
      "READ",
      [
        "storage",
        "002afb2c",
        null,
        "string"
      ]
    ],
    [
      "005a63f0",
      "READ",
      [
        "storage",
        "002a762a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a61b8.md#insn-005a6244) · [`005a637c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a61b8.md#insn-005a637c) · [`005a61dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a61b8.md#insn-005a61dc)
- 新版 `005a6284`（命令位置の公開資料なし） · `005a63bc`（命令位置の公開資料なし） · `005a621c`（命令位置の公開資料なし）

~~~diff
- 005a6244 ["INT_ADD", "register:40f0:8", ["const:5a6244:8", "const:4:8"]]
- 005a6244 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a6284 ["INT_ADD", "register:40f0:8", ["const:5a6284:8", "const:4:8"]]
+ 005a6284 ["CALL", null, ["callee:00c57f80:8"]]
- 005a6244 bytes 1bc71a94
+ 005a6284 bytes 3fc71a94
- 005a637c ["INT_ADD", "register:40f0:8", ["const:5a637c:8", "const:4:8"]]
- 005a637c ["CALL", null, ["callee:00c57f80:8"]]
+ 005a63bc ["INT_ADD", "register:40f0:8", ["const:5a63bc:8", "const:4:8"]]
+ 005a63bc ["CALL", null, ["callee:00c57f80:8"]]
- 005a637c bytes cdc61a94
+ 005a63bc bytes f1c61a94
- 005a61dc ["COPY", "tmp:0:8", ["const:1a5:8"]]
- 005a61dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a61dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a61dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a621c ["COPY", "tmp:0:8", ["const:1e5:8"]]
+ 005a621c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a621c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a621c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a61dc bytes 4a950691
+ 005a621c bytes 4a950791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c44c72a1026fc40385c49b45a94b425"></a>

### [`005a6698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6698.md) → [`005a66d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a66d8.md) FUN_005a66d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005a61b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a61b8.md) · 呼出先 3件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005a61f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a61f8.md) · 呼出先 3件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.21% / 新版 92.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a6714",
      "incomplete_value": true,
      "site": "005a6714",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:321:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a66d4",
      "incomplete_value": true,
      "site": "005a66d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
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
      "005a66fc",
      "READ",
      [
        "storage",
        "002c12e1",
        null,
        "string"
      ]
    ],
    [
      "005a670c",
      "READ",
      [
        "storage",
        "002c12e6",
        null,
        "string"
      ]
    ],
    [
      "005a6768",
      "READ",
      [
        "storage",
        "002a449c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a66fc",
      "READ",
      [
        "storage",
        "002c1321",
        null,
        "string"
      ]
    ],
    [
      "005a670c",
      "READ",
      [
        "storage",
        "002c1326",
        null,
        "string"
      ]
    ],
    [
      "005a6768",
      "READ",
      [
        "storage",
        "002a444f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a66b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6698.md#insn-005a66b4) · [`005a66e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6698.md#insn-005a66e8) · [`005a6704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6698.md#insn-005a6704)
- 新版 `005a66f4`（命令位置の公開資料なし） · `005a6728`（命令位置の公開資料なし） · `005a6744`（命令位置の公開資料なし）

~~~diff
- 005a66b4 ["COPY", "tmp:0:8", ["const:2e1:8"]]
- 005a66b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a66b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a66b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a66f4 ["COPY", "tmp:0:8", ["const:321:8"]]
+ 005a66f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a66f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a66f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a66b4 bytes 29850b91
+ 005a66f4 bytes 29850c91
- 005a66e8 ["INT_ADD", "register:40f0:8", ["const:5a66e8:8", "const:4:8"]]
- 005a66e8 ["CALL", null, ["callee:004410cc:8"]]
+ 005a6728 ["INT_ADD", "register:40f0:8", ["const:5a6728:8", "const:4:8"]]
+ 005a6728 ["CALL", null, ["callee:004410cc:8"]]
- 005a66e8 bytes 696afa97
+ 005a6728 bytes 696afa97
- 005a6704 ["COPY", "register:0:8", ["register:4040:8"]]
- 005a6704 ["INT_ADD", "register:40f0:8", ["const:5a6704:8", "const:4:8"]]
- 005a6704 ["CALLIND", null, ["register:0:8"]]
+ 005a6744 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005a6744 ["INT_ADD", "register:40f0:8", ["const:5a6744:8", "const:4:8"]]
+ 005a6744 ["CALLIND", null, ["register:0:8"]]
- 005a6704 bytes 00013fd6
+ 005a6744 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8727711115e23b0515bef3d6d805481"></a>

### [`005a6854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6854.md) → [`005a6894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a6894.md) FUN_005a6894

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a68b0",
      "incomplete_value": false,
      "site": "005a68b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6870",
      "incomplete_value": false,
      "site": "005a6878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "definition_site": "005a68c8",
      "incomplete_value": false,
      "site": "005a68c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6888",
      "incomplete_value": false,
      "site": "005a6888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "005a68b8",
      "DATA",
      [
        "storage",
        "00c6ed70",
        null,
        "undefined *"
      ]
    ],
    [
      "005a68c8",
      "DATA",
      [
        "storage",
        "00c6ec68",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a68b8",
      "DATA",
      [
        "storage",
        "00c6ee40",
        null,
        "undefined *"
      ]
    ],
    [
      "005a68c8",
      "DATA",
      [
        "storage",
        "00c6ed38",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6854.md#insn-005a6868) · [`005a6870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6854.md#insn-005a6870) · [`005a687c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6854.md#insn-005a687c)
- 新版 `005a68a8`（命令位置の公開資料なし） · `005a68b0`（命令位置の公開資料なし）

~~~diff
- 005a6868 ["INT_ADD", "register:40f0:8", ["const:5a6868:8", "const:4:8"]]
- 005a6868 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a68a8 ["INT_ADD", "register:40f0:8", ["const:5a68a8:8", "const:4:8"]]
+ 005a68a8 ["CALL", null, ["callee:00c57f60:8"]]
- 005a6868 bytes 8ac51a94
+ 005a68a8 bytes aec51a94
- 005a6870 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 005a6870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a6870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a6870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a68b0 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 005a68b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a68b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a68b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a6870 bytes 08c13591
+ 005a68b0 bytes 08013991
- 005a687c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005a687c bytes 48360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a4832bbde742d77452b812989f7f793"></a>

### [`005a689c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a689c.md) → [`005a68dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a68dc.md) FUN_005a68dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a68f8",
      "incomplete_value": true,
      "site": "005a68fc",
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
      "definition_site": "005a68b8",
      "incomplete_value": true,
      "site": "005a68bc",
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
      "005a68f0",
      "READ",
      [
        "storage",
        "00c9b320",
        null,
        "pointer"
      ]
    ],
    [
      "005a68fc",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a68f0",
      "READ",
      [
        "storage",
        "00c9b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "005a68fc",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a68b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a689c.md#insn-005a68b0) · [`005a68c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a689c.md#insn-005a68c8) · [`005a68d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a689c.md#insn-005a68d8)
- 新版 `005a68f0`（命令位置の公開資料なし） · `005a6908`（命令位置の公開資料なし） · `005a6918`（命令位置の公開資料なし）

~~~diff
- 005a68b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
- 005a68b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a68f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f0:8"]]
+ 005a68f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a68b0 bytes 089141f9
+ 005a68f0 bytes 08f941f9
- 005a68c8 ["INT_ADD", "register:40f0:8", ["const:5a68c8:8", "const:4:8"]]
- 005a68c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a6908 ["INT_ADD", "register:40f0:8", ["const:5a6908:8", "const:4:8"]]
+ 005a6908 ["CALL", null, ["callee:00c57f80:8"]]
- 005a68c8 bytes 7ac51a94
+ 005a6908 bytes 9ec51a94
- 005a68d8 ["INT_ADD", "register:40f0:8", ["const:5a68d8:8", "const:4:8"]]
- 005a68d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a6918 ["INT_ADD", "register:40f0:8", ["const:5a6918:8", "const:4:8"]]
+ 005a6918 ["CALL", null, ["callee:00c57f80:8"]]
- 005a68d8 bytes 76c51a94
+ 005a6918 bytes 9ac51a94
~~~


<a id="compare-1e87bab8dad579a474de8da94c5b0df9"></a>

### [`005a68ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a68ec.md) → [`005a692c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a692c.md) FUN_005a692c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a6954",
      "incomplete_value": false,
      "site": "005a6958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6914",
      "incomplete_value": false,
      "site": "005a6918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a6958",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a6958",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a68ec.md#insn-005a6908) · [`005a6914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a68ec.md#insn-005a6914)
- 新版 `005a6948`（命令位置の公開資料なし） · `005a6954`（命令位置の公開資料なし）

~~~diff
- 005a6908 ["INT_ADD", "register:40f0:8", ["const:5a6908:8", "const:4:8"]]
- 005a6908 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a6948 ["INT_ADD", "register:40f0:8", ["const:5a6948:8", "const:4:8"]]
+ 005a6948 ["CALL", null, ["callee:00c57f80:8"]]
- 005a6908 bytes 6ac51a94
+ 005a6948 bytes 8ec51a94
- 005a6914 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a6914 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a6914 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a6914 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a6954 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a6954 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a6954 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a6954 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a6914 bytes 29012891
+ 005a6954 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37e91057317867f03516c045bfd2c0f4"></a>

### [`005a693c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a693c.md) → [`005a697c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a697c.md) FUN_005a697c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a69a4",
      "incomplete_value": false,
      "site": "005a69a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6964",
      "incomplete_value": false,
      "site": "005a6968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a69a8",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a69a8",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a693c.md#insn-005a6958) · [`005a6964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a693c.md#insn-005a6964) · [`005a6974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a693c.md#insn-005a6974)
- 新版 `005a6998`（命令位置の公開資料なし） · `005a69a4`（命令位置の公開資料なし） · `005a69b4`（命令位置の公開資料なし）

~~~diff
- 005a6958 ["INT_ADD", "register:40f0:8", ["const:5a6958:8", "const:4:8"]]
- 005a6958 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a6998 ["INT_ADD", "register:40f0:8", ["const:5a6998:8", "const:4:8"]]
+ 005a6998 ["CALL", null, ["callee:00c57f80:8"]]
- 005a6958 bytes 56c51a94
+ 005a6998 bytes 7ac51a94
- 005a6964 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a6964 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a6964 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a6964 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a69a4 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a69a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a69a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a69a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a6964 bytes 29012891
+ 005a69a4 bytes 29412b91
- 005a6974 ["INT_ADD", "register:40f0:8", ["const:5a6974:8", "const:4:8"]]
- 005a6974 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a69b4 ["INT_ADD", "register:40f0:8", ["const:5a69b4:8", "const:4:8"]]
+ 005a69b4 ["CALL", null, ["callee:00c57f80:8"]]
- 005a6974 bytes 4fc51a94
+ 005a69b4 bytes 73c51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-517d47e16308579d67b578ed54969e1e"></a>

### [`005a6988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6988.md) → [`005a69c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a69c8.md) FUN_005a69c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a69cc",
      "incomplete_value": false,
      "site": "005a69d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a698c",
      "incomplete_value": false,
      "site": "005a6990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "005a69d0",
      "DATA",
      [
        "storage",
        "00c6ed20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a69d0",
      "DATA",
      [
        "storage",
        "00c6edf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a698c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6988.md#insn-005a698c)
- 新版 `005a69cc`（命令位置の公開資料なし）

~~~diff
- 005a698c ["COPY", "tmp:0:8", ["const:d20:8"]]
- 005a698c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a698c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a698c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a69cc ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 005a69cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a69cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a69cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a698c bytes 08813491
+ 005a69cc bytes 08c13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22e62f3ca104583f960fa2f523cc15a8"></a>

### [`005a6998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6998.md) → [`005a69d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a69d8.md) FUN_005a69d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a69e8",
      "incomplete_value": false,
      "site": "005a69f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a69a8",
      "incomplete_value": false,
      "site": "005a69b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "005a69f0",
      "DATA",
      [
        "storage",
        "00c6ed20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a69f0",
      "DATA",
      [
        "storage",
        "00c6edf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a69a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6998.md#insn-005a69a8) · [`005a69b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6998.md#insn-005a69b4)
- 新版 `005a69e8`（命令位置の公開資料なし） · `005a69f4`（命令位置の公開資料なし）

~~~diff
- 005a69a8 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 005a69a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a69a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a69a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a69e8 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 005a69e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a69e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a69e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a69a8 bytes 08813491
+ 005a69e8 bytes 08c13791
- 005a69b4 ["INT_ADD", "register:40f0:8", ["const:5a69b4:8", "const:4:8"]]
- 005a69b4 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a69f4 ["INT_ADD", "register:40f0:8", ["const:5a69f4:8", "const:4:8"]]
+ 005a69f4 ["CALL", null, ["callee:00c57f70:8"]]
- 005a69b4 bytes 3bc51a94
+ 005a69f4 bytes 5fc51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28bc16de008ff9651661f602deb75587"></a>

### [`005a69c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a69c8.md) → [`005a6a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a6a08.md) FUN_005a6a08

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a6a30",
      "incomplete_value": false,
      "site": "005a6a34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a69f0",
      "incomplete_value": false,
      "site": "005a69f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
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
      "005a6a34",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a6a34",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a69e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a69c8.md#insn-005a69e4) · [`005a69f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a69c8.md#insn-005a69f0)
- 新版 `005a6a24`（命令位置の公開資料なし） · `005a6a30`（命令位置の公開資料なし）

~~~diff
- 005a69e4 ["INT_ADD", "register:40f0:8", ["const:5a69e4:8", "const:4:8"]]
- 005a69e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a6a24 ["INT_ADD", "register:40f0:8", ["const:5a6a24:8", "const:4:8"]]
+ 005a6a24 ["CALL", null, ["callee:00c57f80:8"]]
- 005a69e4 bytes 33c51a94
+ 005a6a24 bytes 57c51a94
- 005a69f0 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a69f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a69f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a69f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a6a30 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a6a30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a6a30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a6a30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a69f0 bytes 29012891
+ 005a6a30 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2198a73f5197451b3185193c9d3775e"></a>

### [`005a6a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6a1c.md) → [`005a6a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a6a5c.md) FUN_005a6a5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005a61b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a61b8.md) · 呼出先 3件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`005a61f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a61f8.md) · 呼出先 3件 [`0059b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b91c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "005a6ad8",
      "incomplete_value": false,
      "site": "005a6ae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6a98",
      "incomplete_value": false,
      "site": "005a6aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:c48:8"
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
      "005a6ae0",
      "DATA",
      [
        "storage",
        "00c6ec48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a6ae0",
      "DATA",
      [
        "storage",
        "00c6ed18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6a1c.md#insn-005a6a90) · [`005a6a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6a1c.md#insn-005a6a98) · [`005a6ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6a1c.md#insn-005a6ac8)
- 新版 `005a6ad0`（命令位置の公開資料なし） · `005a6ad8`（命令位置の公開資料なし） · `005a6b08`（命令位置の公開資料なし）

~~~diff
- 005a6a90 ["INT_ADD", "register:40f0:8", ["const:5a6a90:8", "const:4:8"]]
- 005a6a90 ["CALL", null, ["callee:0059b91c:8"]]
+ 005a6ad0 ["INT_ADD", "register:40f0:8", ["const:5a6ad0:8", "const:4:8"]]
+ 005a6ad0 ["CALL", null, ["callee:0059b91c:8"]]
- 005a6a90 bytes 93d3ff97
+ 005a6ad0 bytes 93d3ff97
- 005a6a98 ["COPY", "tmp:0:8", ["const:c48:8"]]
- 005a6a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a6a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a6a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a6ad8 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 005a6ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a6a98 bytes 08213191
+ 005a6ad8 bytes 08613491
- 005a6ac8 ["INT_ADD", "register:40f0:8", ["const:5a6ac8:8", "const:4:8"]]
- 005a6ac8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a6b08 ["INT_ADD", "register:40f0:8", ["const:5a6b08:8", "const:4:8"]]
+ 005a6b08 ["CALL", null, ["callee:00c57f80:8"]]
- 005a6ac8 bytes fac41a94
+ 005a6b08 bytes 1ec51a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42b07199c919b06ca5f8cee2d1676833"></a>

### [`005a6b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6b34.md) → [`005a6b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a6b74.md) FUN_005a6b74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a6b78",
      "incomplete_value": false,
      "site": "005a6b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6b38",
      "incomplete_value": false,
      "site": "005a6b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a6b7c",
      "DATA",
      [
        "storage",
        "00c6ed70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a6b7c",
      "DATA",
      [
        "storage",
        "00c6ee40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6b34.md#insn-005a6b38)
- 新版 `005a6b78`（命令位置の公開資料なし）

~~~diff
- 005a6b38 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 005a6b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a6b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a6b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a6b78 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 005a6b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a6b38 bytes 08c13591
+ 005a6b78 bytes 08013991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-497212d373de1fbc420ae4d3d9631657"></a>

### [`005a6b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6b44.md) → [`005a6b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a6b84.md) FUN_005a6b84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a6b94",
      "incomplete_value": false,
      "site": "005a6b9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6b54",
      "incomplete_value": false,
      "site": "005a6b5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a6b9c",
      "DATA",
      [
        "storage",
        "00c6ed70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a6b9c",
      "DATA",
      [
        "storage",
        "00c6ee40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6b44.md#insn-005a6b54) · [`005a6b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6b44.md#insn-005a6b60)
- 新版 `005a6b94`（命令位置の公開資料なし） · `005a6ba0`（命令位置の公開資料なし）

~~~diff
- 005a6b54 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 005a6b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a6b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a6b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a6b94 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 005a6b94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6b94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a6b94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a6b54 bytes 08c13591
+ 005a6b94 bytes 08013991
- 005a6b60 ["INT_ADD", "register:40f0:8", ["const:5a6b60:8", "const:4:8"]]
- 005a6b60 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a6ba0 ["INT_ADD", "register:40f0:8", ["const:5a6ba0:8", "const:4:8"]]
+ 005a6ba0 ["CALL", null, ["callee:00c57f70:8"]]
- 005a6b60 bytes d0c41a94
+ 005a6ba0 bytes f4c41a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6bb1bc4599f3c3ce5d8b1e869cec9e1"></a>

### [`005a6f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6f0c.md) → [`005a6f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a6f4c.md) FUN_005a6f4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005a7a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7a58.md) [`005a7cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7cb4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`005a7a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7a98.md) [`005a7cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7cf4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.03% / 新版 99.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a6fa0",
      "incomplete_value": true,
      "site": "005a6fa0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:1e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a6f60",
      "incomplete_value": true,
      "site": "005a6f60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:1a5:8"
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
      "005a6f84",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a6f84",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a6fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6f0c.md#insn-005a6fa0) · [`005a6f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6f0c.md#insn-005a6f38) · [`005a6f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6f0c.md#insn-005a6f70)
- 新版 `005a6fe0`（命令位置の公開資料なし） · `005a6f78`（命令位置の公開資料なし） · `005a6fb0`（命令位置の公開資料なし）

~~~diff
- 005a6fa0 ["INT_ADD", "register:40f0:8", ["const:5a6fa0:8", "const:4:8"]]
- 005a6fa0 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a6fe0 ["INT_ADD", "register:40f0:8", ["const:5a6fe0:8", "const:4:8"]]
+ 005a6fe0 ["CALL", null, ["callee:00c57f80:8"]]
- 005a6fa0 bytes c4c31a94
+ 005a6fe0 bytes e8c31a94
- 005a6f38 ["COPY", "tmp:0:8", ["const:1a5:8"]]
- 005a6f38 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a6f38 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a6f38 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a6f78 ["COPY", "tmp:0:8", ["const:1e5:8"]]
+ 005a6f78 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a6f78 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a6f78 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a6f38 bytes 4a950691
+ 005a6f78 bytes 4a950791
- 005a6f70 ["INT_ADD", "register:40f0:8", ["const:5a6f70:8", "const:4:8"]]
- 005a6f70 ["CALL", null, ["callee:004410cc:8"]]
+ 005a6fb0 ["INT_ADD", "register:40f0:8", ["const:5a6fb0:8", "const:4:8"]]
+ 005a6fb0 ["CALL", null, ["callee:004410cc:8"]]
- 005a6f70 bytes 4768fa97
+ 005a6fb0 bytes 4768fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e2d23d61ab8602632657411e47b122e"></a>

### [`005a7534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7534.md) → [`005a7574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7574.md) FUN_005a7574

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009a50c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a5/009a50c0.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)
- 新版 呼出元 1件 [`009a5114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5114.md) · 呼出先 1件 [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md)

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
      "definition_site": "005a7590",
      "incomplete_value": false,
      "site": "005a7594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7550",
      "incomplete_value": false,
      "site": "005a7554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:de0:8"
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
      "005a7594",
      "DATA",
      [
        "storage",
        "00c6ede0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a7594",
      "DATA",
      [
        "storage",
        "00c6eeb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7534.md#insn-005a7548) · [`005a7550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7534.md#insn-005a7550)
- 新版 `005a7588`（命令位置の公開資料なし） · `005a7590`（命令位置の公開資料なし）

~~~diff
- 005a7548 ["INT_ADD", "register:40f0:8", ["const:5a7548:8", "const:4:8"]]
- 005a7548 ["CALL", null, ["callee:0059b948:8"]]
+ 005a7588 ["INT_ADD", "register:40f0:8", ["const:5a7588:8", "const:4:8"]]
+ 005a7588 ["CALL", null, ["callee:0059b948:8"]]
- 005a7548 bytes f0d0ff97
+ 005a7588 bytes f0d0ff97
- 005a7550 ["COPY", "tmp:0:8", ["const:de0:8"]]
- 005a7550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7590 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 005a7590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7550 bytes 08813791
+ 005a7590 bytes 08c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13fd6086f1814f1b7d4e2421069d5968"></a>

### [`005a756c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a756c.md) → [`005a75ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a75ac.md) FUN_005a75ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c581d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c582a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a75dc",
      "incomplete_value": true,
      "site": "005a75e8",
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
            "const:11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a759c",
      "incomplete_value": true,
      "site": "005a75a8",
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
            "const:fd1:8"
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
      "005a75dc",
      "PARAM",
      [
        "storage",
        "002bffd1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a75dc",
      "PARAM",
      [
        "storage",
        "002c0011",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a75a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a756c.md#insn-005a75a8) · [`005a7594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a756c.md#insn-005a7594) · [`005a7598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a756c.md#insn-005a7598)
- 新版 `005a75e8`（命令位置の公開資料なし） · `005a75d4`（命令位置の公開資料なし） · `005a75d8`（命令位置の公開資料なし）

~~~diff
- 005a75a8 ["INT_ADD", "register:40f0:8", ["const:5a75a8:8", "const:4:8"]]
- 005a75a8 ["CALL", null, ["callee:00c58030:8"]]
+ 005a75e8 ["INT_ADD", "register:40f0:8", ["const:5a75e8:8", "const:4:8"]]
+ 005a75e8 ["CALL", null, ["callee:00c58030:8"]]
- 005a75a8 bytes 6ec21a94
+ 005a75e8 bytes 92c21a94
- 005a7594 ["INT_ADD", "register:40f0:8", ["const:5a7594:8", "const:4:8"]]
- 005a7594 ["CALL", null, ["callee:00c582a0:8"]]
+ 005a75d4 ["INT_ADD", "register:40f0:8", ["const:5a75d4:8", "const:4:8"]]
+ 005a75d4 ["CALL", null, ["callee:00c582a0:8"]]
- 005a7594 bytes 0fc31a94
+ 005a75d4 bytes 33c31a94
- 005a7598 ["COPY", "register:4010:8", ["const:2bf000:8"]]
+ 005a75d8 ["COPY", "register:4010:8", ["const:2c0000:8"]]
- 005a7598 bytes c2e8ff90
+ 005a75d8 bytes c2e8ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e929d0bc030f0eb133e2e9f79de7dc34"></a>

### [`005a7654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7654.md) → [`005a7694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7694.md) FUN_005a7694

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a76b0",
      "incomplete_value": false,
      "site": "005a76b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7670",
      "incomplete_value": false,
      "site": "005a7678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "definition_site": "005a76c8",
      "incomplete_value": false,
      "site": "005a76c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7688",
      "incomplete_value": false,
      "site": "005a7688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "005a76b8",
      "DATA",
      [
        "storage",
        "00c6eee8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a76c8",
      "DATA",
      [
        "storage",
        "00c6ee38",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a76b8",
      "DATA",
      [
        "storage",
        "00c6efb8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a76c8",
      "DATA",
      [
        "storage",
        "00c6ef08",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7654.md#insn-005a7668) · [`005a7670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7654.md#insn-005a7670) · [`005a767c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7654.md#insn-005a767c)
- 新版 `005a76a8`（命令位置の公開資料なし） · `005a76b0`（命令位置の公開資料なし）

~~~diff
- 005a7668 ["INT_ADD", "register:40f0:8", ["const:5a7668:8", "const:4:8"]]
- 005a7668 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a76a8 ["INT_ADD", "register:40f0:8", ["const:5a76a8:8", "const:4:8"]]
+ 005a76a8 ["CALL", null, ["callee:00c57f60:8"]]
- 005a7668 bytes 0ac21a94
+ 005a76a8 bytes 2ec21a94
- 005a7670 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 005a7670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a76b0 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 005a76b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a76b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a76b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7670 bytes 08a13b91
+ 005a76b0 bytes 08e13e91
- 005a767c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005a767c bytes 283600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c86369d03995829b11b0cee6081ed13"></a>

### [`005a769c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a769c.md) → [`005a76dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a76dc.md) FUN_005a76dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a76f8",
      "incomplete_value": true,
      "site": "005a76fc",
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
      "definition_site": "005a76b8",
      "incomplete_value": true,
      "site": "005a76bc",
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
      "005a76f0",
      "READ",
      [
        "storage",
        "00c9b320",
        null,
        "pointer"
      ]
    ],
    [
      "005a76fc",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a76f0",
      "READ",
      [
        "storage",
        "00c9b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "005a76fc",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a76b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a769c.md#insn-005a76b0) · [`005a76c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a769c.md#insn-005a76c8) · [`005a76d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a769c.md#insn-005a76d8)
- 新版 `005a76f0`（命令位置の公開資料なし） · `005a7708`（命令位置の公開資料なし） · `005a7718`（命令位置の公開資料なし）

~~~diff
- 005a76b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
- 005a76b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a76f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f0:8"]]
+ 005a76f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a76b0 bytes 089141f9
+ 005a76f0 bytes 08f941f9
- 005a76c8 ["INT_ADD", "register:40f0:8", ["const:5a76c8:8", "const:4:8"]]
- 005a76c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7708 ["INT_ADD", "register:40f0:8", ["const:5a7708:8", "const:4:8"]]
+ 005a7708 ["CALL", null, ["callee:00c57f80:8"]]
- 005a76c8 bytes fac11a94
+ 005a7708 bytes 1ec21a94
- 005a76d8 ["INT_ADD", "register:40f0:8", ["const:5a76d8:8", "const:4:8"]]
- 005a76d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7718 ["INT_ADD", "register:40f0:8", ["const:5a7718:8", "const:4:8"]]
+ 005a7718 ["CALL", null, ["callee:00c57f80:8"]]
- 005a76d8 bytes f6c11a94
+ 005a7718 bytes 1ac21a94
~~~


<a id="compare-d9ef2d417863aa57f090f7c0b9544b0d"></a>

### [`005a76ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a76ec.md) → [`005a772c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a772c.md) FUN_005a772c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a7790",
      "incomplete_value": false,
      "site": "005a7794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7750",
      "incomplete_value": false,
      "site": "005a7754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "005a7794",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a7794",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a76ec.md#insn-005a7734) · [`005a7744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a76ec.md#insn-005a7744) · [`005a7750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a76ec.md#insn-005a7750)
- 新版 `005a7774`（命令位置の公開資料なし） · `005a7784`（命令位置の公開資料なし） · `005a7790`（命令位置の公開資料なし）

~~~diff
- 005a7734 ["INT_ADD", "register:40f0:8", ["const:5a7734:8", "const:4:8"]]
- 005a7734 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7774 ["INT_ADD", "register:40f0:8", ["const:5a7774:8", "const:4:8"]]
+ 005a7774 ["CALL", null, ["callee:00c57f80:8"]]
- 005a7734 bytes dfc11a94
+ 005a7774 bytes 03c21a94
- 005a7744 ["INT_ADD", "register:40f0:8", ["const:5a7744:8", "const:4:8"]]
- 005a7744 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7784 ["INT_ADD", "register:40f0:8", ["const:5a7784:8", "const:4:8"]]
+ 005a7784 ["CALL", null, ["callee:00c57f80:8"]]
- 005a7744 bytes dbc11a94
+ 005a7784 bytes ffc11a94
- 005a7750 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a7750 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a7750 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a7750 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a7790 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a7790 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a7790 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a7790 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a7750 bytes 29012891
+ 005a7790 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a9585ea99ca9e64ba0996bf40292403"></a>

### [`005a7780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7780.md) → [`005a77c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a77c0.md) FUN_005a77c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a7824",
      "incomplete_value": true,
      "site": "005a7828",
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
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a77e4",
      "incomplete_value": true,
      "site": "005a77e8",
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
            "const:a00:8"
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
      "005a7828",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a7828",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a77c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7780.md#insn-005a77c8) · [`005a77d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7780.md#insn-005a77d8) · [`005a77e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7780.md#insn-005a77e4)
- 新版 `005a7808`（命令位置の公開資料なし） · `005a7818`（命令位置の公開資料なし） · `005a7824`（命令位置の公開資料なし）

~~~diff
- 005a77c8 ["INT_ADD", "register:40f0:8", ["const:5a77c8:8", "const:4:8"]]
- 005a77c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7808 ["INT_ADD", "register:40f0:8", ["const:5a7808:8", "const:4:8"]]
+ 005a7808 ["CALL", null, ["callee:00c57f80:8"]]
- 005a77c8 bytes bac11a94
+ 005a7808 bytes dec11a94
- 005a77d8 ["INT_ADD", "register:40f0:8", ["const:5a77d8:8", "const:4:8"]]
- 005a77d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7818 ["INT_ADD", "register:40f0:8", ["const:5a7818:8", "const:4:8"]]
+ 005a7818 ["CALL", null, ["callee:00c57f80:8"]]
- 005a77d8 bytes b6c11a94
+ 005a7818 bytes dac11a94
- 005a77e4 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a77e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a77e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a77e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a7824 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a7824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a7824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a7824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a77e4 bytes 29012891
+ 005a7824 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f57f7d28ae725d82a3b80f283dcaa68b"></a>

### [`005a79f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a79f0.md) → [`005a7a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7a30.md) FUN_005a7a30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a780c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a780c.md) [`005a7a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7a58.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`005a784c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a784c.md) [`005a7a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7a98.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "005a7a3c",
      "incomplete_value": true,
      "site": "005a7a40",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a79fc",
      "incomplete_value": true,
      "site": "005a7a00",
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
            "const:f4c:8"
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
      "005a7a3c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a7a3c",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a79f0.md#insn-005a7a00) · [`005a79fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a79f0.md#insn-005a79fc)
- 新版 `005a7a40`（命令位置の公開資料なし） · `005a7a3c`（命令位置の公開資料なし）

~~~diff
- 005a7a00 ["INT_ADD", "register:40f0:8", ["const:5a7a00:8", "const:4:8"]]
- 005a7a00 ["CALL", null, ["callee:0043b7b8:8"]]
+ 005a7a40 ["INT_ADD", "register:40f0:8", ["const:5a7a40:8", "const:4:8"]]
+ 005a7a40 ["CALL", null, ["callee:0043b7b8:8"]]
- 005a7a00 bytes 5e4ffa97
+ 005a7a40 bytes 5e4ffa97
- 005a79fc ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 005a79fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005a79fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005a79fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005a7a3c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 005a7a3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005a7a3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005a7a3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005a79fc bytes 00303d91
+ 005a7a3c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f5b35fcf10199786dd3257263cd6b10"></a>

### [`005a7cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7cb4.md) → [`005a7cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7cf4.md) FUN_005a7cf4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005a6f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a6/005a6f0c.md) · 呼出先 3件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`005a780c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a780c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`005a6f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a6/005a6f4c.md) · 呼出先 3件 [`0059b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b91c.md) [`005a784c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a784c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a7d34",
      "incomplete_value": true,
      "site": "005a7d40",
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
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7cf4",
      "incomplete_value": true,
      "site": "005a7d00",
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
            "const:e98:8"
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
      "definition_site": "005a7d64",
      "incomplete_value": false,
      "site": "005a7d64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7d24",
      "incomplete_value": false,
      "site": "005a7d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
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
      "005a7d40",
      "DATA",
      [
        "storage",
        "00c6ee98",
        null,
        "undefined *"
      ]
    ],
    [
      "005a7d64",
      "DATA",
      [
        "storage",
        "00c6edc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a7d40",
      "DATA",
      [
        "storage",
        "00c6ef68",
        null,
        "undefined *"
      ]
    ],
    [
      "005a7d64",
      "DATA",
      [
        "storage",
        "00c6ee90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7cb4.md#insn-005a7ce0) · [`005a7cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7cb4.md#insn-005a7cf4) · [`005a7d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7cb4.md#insn-005a7d0c)
- 新版 `005a7d20`（命令位置の公開資料なし） · `005a7d34`（命令位置の公開資料なし） · `005a7d4c`（命令位置の公開資料なし）

~~~diff
- 005a7ce0 ["INT_ADD", "register:40f0:8", ["const:5a7ce0:8", "const:4:8"]]
- 005a7ce0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a7d20 ["INT_ADD", "register:40f0:8", ["const:5a7d20:8", "const:4:8"]]
+ 005a7d20 ["CALL", null, ["callee:00c57f60:8"]]
- 005a7ce0 bytes 6cc01a94
+ 005a7d20 bytes 90c01a94
- 005a7cf4 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 005a7cf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7cf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7cf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7d34 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 005a7d34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7d34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7d34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7cf4 bytes 08613a91
+ 005a7d34 bytes 08a13d91
- 005a7d0c ["INT_ADD", "register:40f0:8", ["const:5a7d0c:8", "const:4:8"]]
- 005a7d0c ["CALL", null, ["callee:0059b91c:8"]]
+ 005a7d4c ["INT_ADD", "register:40f0:8", ["const:5a7d4c:8", "const:4:8"]]
+ 005a7d4c ["CALL", null, ["callee:0059b91c:8"]]
- 005a7d0c bytes f4ceff97
+ 005a7d4c bytes f4ceff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4bd9306d00ab68bbd7d10d51aa18946"></a>

### [`005a7d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7d94.md) → [`005a7dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7dd4.md) FUN_005a7dd4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a7dd8",
      "incomplete_value": false,
      "site": "005a7ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7d98",
      "incomplete_value": false,
      "site": "005a7d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "005a7ddc",
      "DATA",
      [
        "storage",
        "00c6ee98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a7ddc",
      "DATA",
      [
        "storage",
        "00c6ef68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7d94.md#insn-005a7d98)
- 新版 `005a7dd8`（命令位置の公開資料なし）

~~~diff
- 005a7d98 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 005a7d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7dd8 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 005a7dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7d98 bytes 08613a91
+ 005a7dd8 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-812c065ff3e00e55600027b5d0e67df2"></a>

### [`005a7da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7da4.md) → [`005a7de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7de4.md) FUN_005a7de4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a7df4",
      "incomplete_value": false,
      "site": "005a7dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7db4",
      "incomplete_value": false,
      "site": "005a7dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
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
      "005a7dfc",
      "DATA",
      [
        "storage",
        "00c6ee98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a7dfc",
      "DATA",
      [
        "storage",
        "00c6ef68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7da4.md#insn-005a7db4) · [`005a7dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7da4.md#insn-005a7dc0)
- 新版 `005a7df4`（命令位置の公開資料なし） · `005a7e00`（命令位置の公開資料なし）

~~~diff
- 005a7db4 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 005a7db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7df4 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 005a7df4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7df4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7df4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7db4 bytes 08613a91
+ 005a7df4 bytes 08a13d91
- 005a7dc0 ["INT_ADD", "register:40f0:8", ["const:5a7dc0:8", "const:4:8"]]
- 005a7dc0 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a7e00 ["INT_ADD", "register:40f0:8", ["const:5a7e00:8", "const:4:8"]]
+ 005a7e00 ["CALL", null, ["callee:00c57f70:8"]]
- 005a7dc0 bytes 38c01a94
+ 005a7e00 bytes 5cc01a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a46369c8f69572d13e25cf703c753c3"></a>

### [`005a7dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7dd4.md) → [`005a7e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7e14.md) FUN_005a7e14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a7e78",
      "incomplete_value": false,
      "site": "005a7e7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7e38",
      "incomplete_value": false,
      "site": "005a7e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6d000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "005a7e7c",
      "DATA",
      [
        "storage",
        "00c6da00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a7e7c",
      "DATA",
      [
        "storage",
        "00c6dad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7dd4.md#insn-005a7e1c) · [`005a7e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7dd4.md#insn-005a7e2c) · [`005a7e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7dd4.md#insn-005a7e38)
- 新版 `005a7e5c`（命令位置の公開資料なし） · `005a7e6c`（命令位置の公開資料なし） · `005a7e78`（命令位置の公開資料なし）

~~~diff
- 005a7e1c ["INT_ADD", "register:40f0:8", ["const:5a7e1c:8", "const:4:8"]]
- 005a7e1c ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7e5c ["INT_ADD", "register:40f0:8", ["const:5a7e5c:8", "const:4:8"]]
+ 005a7e5c ["CALL", null, ["callee:00c57f80:8"]]
- 005a7e1c bytes 25c01a94
+ 005a7e5c bytes 49c01a94
- 005a7e2c ["INT_ADD", "register:40f0:8", ["const:5a7e2c:8", "const:4:8"]]
- 005a7e2c ["CALL", null, ["callee:00c57f80:8"]]
+ 005a7e6c ["INT_ADD", "register:40f0:8", ["const:5a7e6c:8", "const:4:8"]]
+ 005a7e6c ["CALL", null, ["callee:00c57f80:8"]]
- 005a7e2c bytes 21c01a94
+ 005a7e6c bytes 45c01a94
- 005a7e38 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a7e38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a7e38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a7e38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a7e78 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a7e78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a7e78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a7e78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a7e38 bytes 29012891
+ 005a7e78 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbe29e3f464f3784279ef7afc23c40b2"></a>

### [`005a7e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7e6c.md) → [`005a7eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7eac.md) FUN_005a7eac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "005a7eb0",
      "incomplete_value": false,
      "site": "005a7eb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7e70",
      "incomplete_value": false,
      "site": "005a7e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "005a7eb4",
      "DATA",
      [
        "storage",
        "00c6eee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a7eb4",
      "DATA",
      [
        "storage",
        "00c6efb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7e6c.md#insn-005a7e70)
- 新版 `005a7eb0`（命令位置の公開資料なし）

~~~diff
- 005a7e70 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 005a7e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7eb0 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 005a7eb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7eb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7eb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7e70 bytes 08a13b91
+ 005a7eb0 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83fc0ef291badaf34678603c4824bf3e"></a>

### [`005a7e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7e7c.md) → [`005a7ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7ebc.md) FUN_005a7ebc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005a7ecc",
      "incomplete_value": false,
      "site": "005a7ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7e8c",
      "incomplete_value": false,
      "site": "005a7e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "005a7ed4",
      "DATA",
      [
        "storage",
        "00c6eee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a7ed4",
      "DATA",
      [
        "storage",
        "00c6efb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7e7c.md#insn-005a7e8c) · [`005a7e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7e7c.md#insn-005a7e98)
- 新版 `005a7ecc`（命令位置の公開資料なし） · `005a7ed8`（命令位置の公開資料なし）

~~~diff
- 005a7e8c ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 005a7e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a7e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a7e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a7ecc ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 005a7ecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7ecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a7ecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a7e8c bytes 08a13b91
+ 005a7ecc bytes 08e13e91
- 005a7e98 ["INT_ADD", "register:40f0:8", ["const:5a7e98:8", "const:4:8"]]
- 005a7e98 ["CALL", null, ["callee:00c57f70:8"]]
+ 005a7ed8 ["INT_ADD", "register:40f0:8", ["const:5a7ed8:8", "const:4:8"]]
+ 005a7ed8 ["CALL", null, ["callee:00c57f70:8"]]
- 005a7e98 bytes 02c01a94
+ 005a7ed8 bytes 26c01a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b6cd92cacd2e62d0eb9d92de1fbebdc"></a>

### [`005a7eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7eb4.md) → [`005a7ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7ef4.md) _INIT_53

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a7f30",
      "incomplete_value": true,
      "site": "005a7f4c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7ef0",
      "incomplete_value": true,
      "site": "005a7f0c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f26:8"
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
      "definition_site": "005a7f54",
      "incomplete_value": true,
      "site": "005a7f70",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
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
    "old": {
      "definition_site": "005a7f14",
      "incomplete_value": true,
      "site": "005a7f30",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f39:8"
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
      "definition_site": "005a7f74",
      "incomplete_value": true,
      "site": "005a7f90",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a7f34",
      "incomplete_value": true,
      "site": "005a7f50",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:dc2:8"
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
      "005a7f30",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a7f54",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a7f74",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a7f30",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005a7f54",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005a7f74",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7eb4.md#insn-005a7f2c) · [`005a7f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7eb4.md#insn-005a7f4c) · [`005a80e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a7/005a7eb4.md#insn-005a80e8)
- 新版 `005a7f6c`（命令位置の公開資料なし） · `005a7f8c`（命令位置の公開資料なし） · `005a8128`（命令位置の公開資料なし）

~~~diff
- 005a7f2c ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 005a7f2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a7f2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a7f2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a7f6c ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 005a7f6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a7f6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a7f6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a7f2c bytes 4a093791
+ 005a7f6c bytes 4ab93591
- 005a7f4c ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005a7f4c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a7f4c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a7f4c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a7f8c ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005a7f8c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a7f8c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a7f8c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a7f4c bytes 4a893d91
+ 005a7f8c bytes 4a553c91
- 005a80e8 ["INT_ADD", "register:40f0:8", ["const:5a80e8:8", "const:4:8"]]
- 005a80e8 ["CALL", null, ["callee:00c57f00:8"]]
+ 005a8128 ["INT_ADD", "register:40f0:8", ["const:5a8128:8", "const:4:8"]]
+ 005a8128 ["CALL", null, ["callee:00c57f00:8"]]
- 005a80e8 bytes 52bf1a94
+ 005a8128 bytes 76bf1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5501a451baaf51a4e6997f0acf95483a"></a>

### [`005a8244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8244.md) → [`005a8284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8284.md) FUN_005a8284

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0059b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b91c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.18% / 新版 96.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a8488",
      "incomplete_value": false,
      "site": "005a8494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8448",
      "incomplete_value": false,
      "site": "005a8454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a84ac",
      "incomplete_value": false,
      "site": "005a84b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a846c",
      "incomplete_value": false,
      "site": "005a8474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "005a82b4",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a8494",
      "DATA",
      [
        "storage",
        "00c6f010",
        null,
        "undefined *"
      ]
    ],
    [
      "005a84b4",
      "DATA",
      [
        "storage",
        "00c6ef38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a82b4",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "005a8494",
      "DATA",
      [
        "storage",
        "00c6f0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "005a84b4",
      "DATA",
      [
        "storage",
        "00c6f008",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8244.md#insn-005a8434) · [`005a8268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8244.md#insn-005a8268) · [`005a82a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8244.md#insn-005a82a0)
- 新版 `005a8474`（命令位置の公開資料なし） · `005a82a8`（命令位置の公開資料なし） · `005a82e0`（命令位置の公開資料なし）

~~~diff
- 005a8434 ["INT_ADD", "register:40f0:8", ["const:5a8434:8", "const:4:8"]]
- 005a8434 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a8474 ["INT_ADD", "register:40f0:8", ["const:5a8474:8", "const:4:8"]]
+ 005a8474 ["CALL", null, ["callee:00c57f80:8"]]
- 005a8434 bytes 9fbe1a94
+ 005a8474 bytes c3be1a94
- 005a8268 ["COPY", "tmp:0:8", ["const:1a5:8"]]
- 005a8268 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a8268 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a8268 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a82a8 ["COPY", "tmp:0:8", ["const:1e5:8"]]
+ 005a82a8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a82a8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a82a8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a8268 bytes 4a950691
+ 005a82a8 bytes 4a950791
- 005a82a0 ["INT_ADD", "register:40f0:8", ["const:5a82a0:8", "const:4:8"]]
- 005a82a0 ["CALL", null, ["callee:004410cc:8"]]
+ 005a82e0 ["INT_ADD", "register:40f0:8", ["const:5a82e0:8", "const:4:8"]]
+ 005a82e0 ["CALL", null, ["callee:004410cc:8"]]
- 005a82a0 bytes 7b63fa97
+ 005a82e0 bytes 7b63fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f19249baa9188dee55eb244e7413828b"></a>

### [`005a8538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8538.md) → [`005a8578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8578.md) FUN_005a8578

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009a57b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a5/009a57b4.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)
- 新版 呼出元 1件 [`009a5808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5808.md) · 呼出先 1件 [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md)

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
      "definition_site": "005a859c",
      "incomplete_value": false,
      "site": "005a85a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6f000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a855c",
      "incomplete_value": false,
      "site": "005a8560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6e000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "005a85a0",
      "DATA",
      [
        "storage",
        "00c6ef58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a85a0",
      "DATA",
      [
        "storage",
        "00c6f028",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8538.md#insn-005a8554) · [`005a8558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8538.md#insn-005a8558) · [`005a855c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8538.md#insn-005a855c)
- 新版 `005a8594`（命令位置の公開資料なし） · `005a8598`（命令位置の公開資料なし） · `005a859c`（命令位置の公開資料なし）

~~~diff
- 005a8554 ["INT_ADD", "register:40f0:8", ["const:5a8554:8", "const:4:8"]]
- 005a8554 ["CALL", null, ["callee:0059b948:8"]]
+ 005a8594 ["INT_ADD", "register:40f0:8", ["const:5a8594:8", "const:4:8"]]
+ 005a8594 ["CALL", null, ["callee:0059b948:8"]]
- 005a8554 bytes edccff97
+ 005a8594 bytes edccff97
- 005a8558 ["COPY", "register:4040:8", ["const:c6e000:8"]]
+ 005a8598 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005a8558 bytes 283600d0
+ 005a8598 bytes 283600f0
- 005a855c ["COPY", "tmp:0:8", ["const:f58:8"]]
- 005a855c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a855c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a855c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a859c ["COPY", "tmp:0:8", ["const:28:8"]]
+ 005a859c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a859c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a859c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a855c bytes 08613d91
+ 005a859c bytes 08a10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da591990652276c73448baeb52cfc4ef"></a>

### [`005a857c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a857c.md) → [`005a85bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a85bc.md) FUN_005a85bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c581d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581d0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c582a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a85ec",
      "incomplete_value": false,
      "site": "005a85f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a85ac",
      "incomplete_value": false,
      "site": "005a85b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:fd1:8"
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
      "definition_site": "005a8618",
      "incomplete_value": false,
      "site": "005a8620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a85d8",
      "incomplete_value": false,
      "site": "005a85e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:79c:8"
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
      "005a85ec",
      "PARAM",
      [
        "storage",
        "002bffd1",
        null,
        "string"
      ]
    ],
    [
      "005a8618",
      "PARAM",
      [
        "storage",
        "002bc79c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a85ec",
      "PARAM",
      [
        "storage",
        "002c0011",
        null,
        "string"
      ]
    ],
    [
      "005a8618",
      "PARAM",
      [
        "storage",
        "002bc748",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a85b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a857c.md#insn-005a85b8) · [`005a85e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a857c.md#insn-005a85e0) · [`005a85a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a857c.md#insn-005a85a4)
- 新版 `005a85f8`（命令位置の公開資料なし） · `005a8620`（命令位置の公開資料なし） · `005a85e4`（命令位置の公開資料なし）

~~~diff
- 005a85b8 ["INT_ADD", "register:40f0:8", ["const:5a85b8:8", "const:4:8"]]
- 005a85b8 ["CALL", null, ["callee:00c58030:8"]]
+ 005a85f8 ["INT_ADD", "register:40f0:8", ["const:5a85f8:8", "const:4:8"]]
+ 005a85f8 ["CALL", null, ["callee:00c58030:8"]]
- 005a85b8 bytes 6abe1a94
+ 005a85f8 bytes 8ebe1a94
- 005a85e0 ["INT_ADD", "register:40f0:8", ["const:5a85e0:8", "const:4:8"]]
- 005a85e0 ["CALL", null, ["callee:00c58040:8"]]
+ 005a8620 ["INT_ADD", "register:40f0:8", ["const:5a8620:8", "const:4:8"]]
+ 005a8620 ["CALL", null, ["callee:00c58040:8"]]
- 005a85e0 bytes 64be1a94
+ 005a8620 bytes 88be1a94
- 005a85a4 ["INT_ADD", "register:40f0:8", ["const:5a85a4:8", "const:4:8"]]
- 005a85a4 ["CALL", null, ["callee:00c582a0:8"]]
+ 005a85e4 ["INT_ADD", "register:40f0:8", ["const:5a85e4:8", "const:4:8"]]
+ 005a85e4 ["CALL", null, ["callee:00c582a0:8"]]
- 005a85a4 bytes 0bbf1a94
+ 005a85e4 bytes 2fbf1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

