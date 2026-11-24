# v16.0.1 → v16.0.2 · 最優先の変更候補 (18)

[一覧の目次](README.md)

<a id="compare-bf6310ddb4a94d48ea9bf86265ce2694"></a>

### [`00582ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ca0.md) → [`00582ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582ce0.md) FUN_00582ce0

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
      "definition_site": "00582cf0",
      "incomplete_value": false,
      "site": "00582cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582cb0",
      "incomplete_value": false,
      "site": "00582cb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00582cf8",
      "DATA",
      [
        "storage",
        "00c6c7f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00582cf8",
      "DATA",
      [
        "storage",
        "00c6c8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ca0.md#insn-00582cb0) · [`00582cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ca0.md#insn-00582cbc)
- 新版 `00582cf0`（命令位置の公開資料なし） · `00582cfc`（命令位置の公開資料なし）

~~~diff
- 00582cb0 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 00582cb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00582cb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00582cb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00582cf0 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00582cf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00582cf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00582cf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00582cb0 bytes 08c11f91
+ 00582cf0 bytes 08012391
- 00582cbc ["INT_ADD", "register:40f0:8", ["const:582cbc:8", "const:4:8"]]
- 00582cbc ["CALL", null, ["callee:00c57f70:8"]]
+ 00582cfc ["INT_ADD", "register:40f0:8", ["const:582cfc:8", "const:4:8"]]
+ 00582cfc ["CALL", null, ["callee:00c57f70:8"]]
- 00582cbc bytes 79541b94
+ 00582cfc bytes 9d541b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c35eab6a672fa0bd8dae7cf35c118d4"></a>

### [`00582ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ce0.md) → [`00582d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582d20.md) FUN_00582d20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00581aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581aa8.md) · 呼出先 4件 [`004bca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e90.md)
- 新版 呼出元 1件 [`00581ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ae8.md) · 呼出先 4件 [`004bca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f60.md)

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
      "definition_site": "00582d58",
      "incomplete_value": false,
      "site": "00582d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582d18",
      "incomplete_value": false,
      "site": "00582d18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "definition_site": "00582d88",
      "incomplete_value": true,
      "site": "00582d88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:957:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582d48",
      "incomplete_value": true,
      "site": "00582d48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9b3:8"
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
      "definition_site": "00582e44",
      "incomplete_value": true,
      "site": "00582e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00582e04",
      "incomplete_value": true,
      "site": "00582e04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:139:8"
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
      "00582d58",
      "DATA",
      [
        "storage",
        "00c6c840",
        null,
        "undefined *"
      ]
    ],
    [
      "00582d78",
      "READ",
      [
        "storage",
        "002a79b3",
        null,
        "string"
      ]
    ],
    [
      "00582e30",
      "READ",
      [
        "storage",
        "002a2139",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00582d58",
      "DATA",
      [
        "storage",
        "00c6c910",
        null,
        "undefined *"
      ]
    ],
    [
      "00582d78",
      "READ",
      [
        "storage",
        "002a7957",
        null,
        "string"
      ]
    ],
    [
      "00582e30",
      "READ",
      [
        "storage",
        "002a20ec",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00582d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ce0.md#insn-00582d0c) · [`00582d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ce0.md#insn-00582d30) · [`00582d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ce0.md#insn-00582d5c)
- 新版 `00582d4c`（命令位置の公開資料なし） · `00582d70`（命令位置の公開資料なし） · `00582d9c`（命令位置の公開資料なし）

~~~diff
- 00582d0c ["COPY", "tmp:0:8", ["const:840:8"]]
- 00582d0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582d0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582d0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582d4c ["COPY", "tmp:0:8", ["const:910:8"]]
+ 00582d4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582d4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582d4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582d0c bytes 29012191
+ 00582d4c bytes 29412491
- 00582d30 ["COPY", "tmp:0:8", ["const:9b3:8"]]
- 00582d30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00582d30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00582d30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00582d70 ["COPY", "tmp:0:8", ["const:957:8"]]
+ 00582d70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00582d70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00582d70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00582d30 bytes 29cd2691
+ 00582d70 bytes 295d2591
- 00582d5c ["INT_ADD", "register:40f0:8", ["const:582d5c:8", "const:4:8"]]
- 00582d5c ["CALL", null, ["callee:00c58f60:8"]]
+ 00582d9c ["INT_ADD", "register:40f0:8", ["const:582d9c:8", "const:4:8"]]
+ 00582d9c ["CALL", null, ["callee:00c58f60:8"]]
- 00582d5c bytes 4d581b94
+ 00582d9c bytes 71581b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c440c37ba4701cbfd2aee7bf99f76287"></a>

### [`00582ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ffc.md) → [`0058303c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058303c.md) FUN_0058303c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0058304c",
      "incomplete_value": false,
      "site": "0058304c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058300c",
      "incomplete_value": false,
      "site": "0058300c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "0058304c",
      "DATA",
      [
        "storage",
        "00c6c840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058304c",
      "DATA",
      [
        "storage",
        "00c6c910",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582ffc.md#insn-00583008)
- 新版 `00583048`（命令位置の公開資料なし）

~~~diff
- 00583008 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00583008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00583008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00583008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00583048 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 00583048 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00583048 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00583048 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00583008 bytes 29012191
+ 00583048 bytes 29412491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2324529e2b247c565d0c8380baef4079"></a>

### [`00583024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583024.md) → [`00583064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583064.md) FUN_00583064

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00583070",
      "incomplete_value": false,
      "site": "00583070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583030",
      "incomplete_value": false,
      "site": "00583030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00583070",
      "DATA",
      [
        "storage",
        "00c6c840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00583070",
      "DATA",
      [
        "storage",
        "00c6c910",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058302c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583024.md#insn-0058302c) · [`00583054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583024.md#insn-00583054)
- 新版 `0058306c`（命令位置の公開資料なし） · `00583094`（命令位置の公開資料なし）

~~~diff
- 0058302c ["COPY", "tmp:0:8", ["const:840:8"]]
- 0058302c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058302c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058302c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058306c ["COPY", "tmp:0:8", ["const:910:8"]]
+ 0058306c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058306c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058306c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058302c bytes 29012191
+ 0058306c bytes 29412491
- 00583054 ["COPY", "register:0:8", ["register:4048:8"]]
- 00583054 ["INT_ADD", "register:40f0:8", ["const:583054:8", "const:4:8"]]
- 00583054 ["CALLIND", null, ["register:0:8"]]
+ 00583094 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00583094 ["INT_ADD", "register:40f0:8", ["const:583094:8", "const:4:8"]]
+ 00583094 ["CALLIND", null, ["register:0:8"]]
- 00583054 bytes 20013fd6
+ 00583094 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1b1706b83ce64088ae73430b5b848a5"></a>

### [`005834b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005834b8.md) → [`005834f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005834f8.md) FUN_005834f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00583620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583620.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 1件 [`00583660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583660.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

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
      "definition_site": "00583518",
      "incomplete_value": false,
      "site": "00583518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005834d8",
      "incomplete_value": false,
      "site": "005834d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "00583518",
      "DATA",
      [
        "storage",
        "00c6c8c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00583518",
      "DATA",
      [
        "storage",
        "00c6c998",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005834d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005834b8.md#insn-005834d0) · [`00583514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005834b8.md#insn-00583514) · [`00583540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005834b8.md#insn-00583540)
- 新版 `00583510`（命令位置の公開資料なし） · `00583554`（命令位置の公開資料なし） · `00583580`（命令位置の公開資料なし）

~~~diff
- 005834d0 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 005834d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005834d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005834d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00583510 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00583510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00583510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00583510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005834d0 bytes 08212391
+ 00583510 bytes 08612691
- 00583514 ["INT_ADD", "register:40f0:8", ["const:583514:8", "const:4:8"]]
- 00583514 ["CALL", null, ["callee:0043bb60:8"]]
+ 00583554 ["INT_ADD", "register:40f0:8", ["const:583554:8", "const:4:8"]]
+ 00583554 ["CALL", null, ["callee:0043bb60:8"]]
- 00583514 bytes 83e1fa97
+ 00583554 bytes 83e1fa97
- 00583540 ["INT_ADD", "register:40f0:8", ["const:583540:8", "const:4:8"]]
- 00583540 ["CALL", null, ["callee:0043bb60:8"]]
+ 00583580 ["INT_ADD", "register:40f0:8", ["const:583580:8", "const:4:8"]]
+ 00583580 ["CALL", null, ["callee:0043bb60:8"]]
- 00583540 bytes 78e1fa97
+ 00583580 bytes 78e1fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e8af95a67fc26f707712e04a6fce188"></a>

### [`00583620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583620.md) → [`00583660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583660.md) FUN_00583660

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00561d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d30.md) · 呼出先 2件 [`005834b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005834b8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00561d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d70.md) · 呼出先 2件 [`005834f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005834f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0058369c",
      "incomplete_value": false,
      "site": "005836a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058365c",
      "incomplete_value": false,
      "site": "00583668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a08:8"
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
      "005836a8",
      "DATA",
      [
        "storage",
        "00c6ca08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005836a8",
      "DATA",
      [
        "storage",
        "00c6cad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583620.md#insn-00583650) · [`0058365c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583620.md#insn-0058365c) · [`00583680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583620.md#insn-00583680)
- 新版 `00583690`（命令位置の公開資料なし） · `0058369c`（命令位置の公開資料なし） · `005836c0`（命令位置の公開資料なし）

~~~diff
- 00583650 ["INT_ADD", "register:40f0:8", ["const:583650:8", "const:4:8"]]
- 00583650 ["CALL", null, ["callee:00c57f60:8"]]
+ 00583690 ["INT_ADD", "register:40f0:8", ["const:583690:8", "const:4:8"]]
+ 00583690 ["CALL", null, ["callee:00c57f60:8"]]
- 00583650 bytes 10521b94
+ 00583690 bytes 34521b94
- 0058365c ["COPY", "tmp:0:8", ["const:a08:8"]]
- 0058365c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058365c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058365c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058369c ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 0058369c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058369c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058369c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058365c bytes 08212891
+ 0058369c bytes 08612b91
- 00583680 ["INT_ADD", "register:40f0:8", ["const:583680:8", "const:4:8"]]
- 00583680 ["CALL", null, ["callee:005834f8:8"]]
+ 005836c0 ["INT_ADD", "register:40f0:8", ["const:5836c0:8", "const:4:8"]]
+ 005836c0 ["CALL", null, ["callee:005834f8:8"]]
- 00583680 bytes 8effff97
+ 005836c0 bytes 8effff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72e16b5759f0a3ec2e142aa86e38c71a"></a>

### [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) → [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) FUN_005838ec

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005838a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838a4.md) [`00584938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md) · 呼出先 25件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00583dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583dd8.md) [`00587128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587128.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 2件 [`005838e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838e4.md) [`00584978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584978.md) · 呼出先 25件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00583e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583e18.md) [`00587168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587168.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.63% / 新版 93.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00583974",
      "incomplete_value": true,
      "site": "00583988",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "old": {
      "definition_site": "00583934",
      "incomplete_value": true,
      "site": "00583948",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:6a0:8"
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
      "definition_site": "00583980",
      "incomplete_value": true,
      "site": "00583990",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00583940",
      "incomplete_value": true,
      "site": "00583950",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00583980",
      "incomplete_value": true,
      "site": "00583990",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00583940",
      "incomplete_value": true,
      "site": "00583950",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00583944",
      "READ",
      [
        "storage",
        "002ad90f",
        null,
        "string"
      ]
    ],
    [
      "0058394c",
      "READ",
      [
        "storage",
        "002ad915",
        null,
        "string"
      ]
    ],
    [
      "00583974",
      "READ",
      [
        "storage",
        "002c26a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00583944",
      "READ",
      [
        "storage",
        "002ad8b3",
        null,
        "string"
      ]
    ],
    [
      "0058394c",
      "READ",
      [
        "storage",
        "002ad8b9",
        null,
        "string"
      ]
    ],
    [
      "00583974",
      "READ",
      [
        "storage",
        "002c26e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058399c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md#insn-0058399c) · [`00583c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md#insn-00583c40) · [`00583c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md#insn-00583c80)
- 新版 `005839dc`（命令位置の公開資料なし） · `00583c80`（命令位置の公開資料なし） · `00583cc0`（命令位置の公開資料なし）

~~~diff
- 0058399c ["INT_ADD", "register:40f0:8", ["const:58399c:8", "const:4:8"]]
- 0058399c ["CALL", null, ["callee:00c57f80:8"]]
+ 005839dc ["INT_ADD", "register:40f0:8", ["const:5839dc:8", "const:4:8"]]
+ 005839dc ["CALL", null, ["callee:00c57f80:8"]]
- 0058399c bytes 45511b94
+ 005839dc bytes 69511b94
- 00583c40 ["INT_ADD", "register:40f0:8", ["const:583c40:8", "const:4:8"]]
- 00583c40 ["CALL", null, ["callee:00587168:8"]]
+ 00583c80 ["INT_ADD", "register:40f0:8", ["const:583c80:8", "const:4:8"]]
+ 00583c80 ["CALL", null, ["callee:00587168:8"]]
- 00583c40 bytes 3a0d0094
+ 00583c80 bytes 3a0d0094
- 00583c80 ["INT_ADD", "register:40f0:8", ["const:583c80:8", "const:4:8"]]
- 00583c80 ["CALL", null, ["ram:589f08:8"]]
+ 00583cc0 ["INT_ADD", "register:40f0:8", ["const:583cc0:8", "const:4:8"]]
+ 00583cc0 ["CALL", null, ["ram:589f48:8"]]
- 00583c80 bytes a2180094
+ 00583cc0 bytes a2180094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53ef347261f39d58d7cb3dc4bc2a9c88"></a>

### [`00583dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583dd8.md) → [`00583e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583e18.md) FUN_00583e18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 2件 [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) · 呼出先 7件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.34% / 新版 98.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00583f28",
      "incomplete_value": false,
      "site": "00583f30",
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
            "const:19e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583ee8",
      "incomplete_value": false,
      "site": "00583ef0",
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
            "const:1eb:8"
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
      "definition_site": "00583f8c",
      "incomplete_value": false,
      "site": "00583f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:d12:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583f4c",
      "incomplete_value": false,
      "site": "00583f54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:d6e:8"
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
      "definition_site": "00583ff0",
      "incomplete_value": false,
      "site": "00583ff8",
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
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00583fb0",
      "incomplete_value": false,
      "site": "00583fb8",
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
            "const:91c:8"
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
      "00583f28",
      "PARAM",
      [
        "storage",
        "002a01eb",
        null,
        "string"
      ]
    ],
    [
      "00583f8c",
      "PARAM",
      [
        "storage",
        "002b0d6e",
        null,
        "string"
      ]
    ],
    [
      "00583ff0",
      "PARAM",
      [
        "storage",
        "002ac91c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00583f28",
      "PARAM",
      [
        "storage",
        "002a019e",
        null,
        "string"
      ]
    ],
    [
      "00583f8c",
      "PARAM",
      [
        "storage",
        "002b0d12",
        null,
        "string"
      ]
    ],
    [
      "00583ff0",
      "PARAM",
      [
        "storage",
        "002ac8c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00583ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583dd8.md#insn-00583ef0) · [`00583f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583dd8.md#insn-00583f54) · [`00583fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583dd8.md#insn-00583fb8)
- 新版 `00583f30`（命令位置の公開資料なし） · `00583f94`（命令位置の公開資料なし） · `00583ff8`（命令位置の公開資料なし）

~~~diff
- 00583ef0 ["INT_ADD", "register:40f0:8", ["const:583ef0:8", "const:4:8"]]
- 00583ef0 ["CALL", null, ["callee:00c58040:8"]]
+ 00583f30 ["INT_ADD", "register:40f0:8", ["const:583f30:8", "const:4:8"]]
+ 00583f30 ["CALL", null, ["callee:00c58040:8"]]
- 00583ef0 bytes 20501b94
+ 00583f30 bytes 44501b94
- 00583f54 ["INT_ADD", "register:40f0:8", ["const:583f54:8", "const:4:8"]]
- 00583f54 ["CALL", null, ["callee:00c58040:8"]]
+ 00583f94 ["INT_ADD", "register:40f0:8", ["const:583f94:8", "const:4:8"]]
+ 00583f94 ["CALL", null, ["callee:00c58040:8"]]
- 00583f54 bytes 07501b94
+ 00583f94 bytes 2b501b94
- 00583fb8 ["INT_ADD", "register:40f0:8", ["const:583fb8:8", "const:4:8"]]
- 00583fb8 ["CALL", null, ["callee:00c58040:8"]]
+ 00583ff8 ["INT_ADD", "register:40f0:8", ["const:583ff8:8", "const:4:8"]]
+ 00583ff8 ["CALL", null, ["callee:00c58040:8"]]
- 00583fb8 bytes ee4f1b94
+ 00583ff8 bytes 12501b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e7e997cd765fec1c8d8cf2aee9fb67c"></a>

### [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) → [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) FUN_005841ec

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005841a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841a4.md) · 呼出先 27件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00583dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583dd8.md) [`00586810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586810.md) [`00586974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586974.md) [`0058724c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058724c.md)
- 新版 呼出元 1件 [`005841e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841e4.md) · 呼出先 27件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00583e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/00583e18.md) [`00586850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586850.md) [`005869b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/005869b4.md) [`0058728c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058728c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00584284",
      "incomplete_value": true,
      "site": "00584290",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:6e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00584244",
      "incomplete_value": true,
      "site": "00584250",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:6a0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00584560",
      "incomplete_value": false,
      "site": "00584570",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00584520",
      "incomplete_value": false,
      "site": "00584530",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005846d0",
      "value": [
        "leaf",
        "ram:589f48:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00584690",
      "value": [
        "leaf",
        "ram:589f08:8"
      ]
    },
    "ordinal": 42,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00584250",
      "READ",
      [
        "storage",
        "002ad90f",
        null,
        "string"
      ]
    ],
    [
      "00584258",
      "READ",
      [
        "storage",
        "002ad915",
        null,
        "string"
      ]
    ],
    [
      "00584280",
      "READ",
      [
        "storage",
        "002a43dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00584250",
      "READ",
      [
        "storage",
        "002ad8b3",
        null,
        "string"
      ]
    ],
    [
      "00584258",
      "READ",
      [
        "storage",
        "002ad8b9",
        null,
        "string"
      ]
    ],
    [
      "00584280",
      "READ",
      [
        "storage",
        "002a438f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00584530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md#insn-00584530) · [`00584570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md#insn-00584570) · [`00584650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md#insn-00584650)
- 新版 `00584570`（命令位置の公開資料なし） · `005845b0`（命令位置の公開資料なし） · `00584690`（命令位置の公開資料なし）

~~~diff
- 00584530 ["INT_ADD", "register:40f0:8", ["const:584530:8", "const:4:8"]]
- 00584530 ["CALL", null, ["callee:0058728c:8"]]
+ 00584570 ["INT_ADD", "register:40f0:8", ["const:584570:8", "const:4:8"]]
+ 00584570 ["CALL", null, ["callee:0058728c:8"]]
- 00584530 bytes 470b0094
+ 00584570 bytes 470b0094
- 00584570 ["COPY", "register:0:8", ["register:4040:8"]]
- 00584570 ["INT_ADD", "register:40f0:8", ["const:584570:8", "const:4:8"]]
- 00584570 ["CALLIND", null, ["register:0:8"]]
+ 005845b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005845b0 ["INT_ADD", "register:40f0:8", ["const:5845b0:8", "const:4:8"]]
+ 005845b0 ["CALLIND", null, ["register:0:8"]]
- 00584570 bytes 00013fd6
+ 005845b0 bytes 00013fd6
- 00584650 ["COPY", "register:0:8", ["register:4040:8"]]
- 00584650 ["INT_ADD", "register:40f0:8", ["const:584650:8", "const:4:8"]]
- 00584650 ["CALLIND", null, ["register:0:8"]]
+ 00584690 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00584690 ["INT_ADD", "register:40f0:8", ["const:584690:8", "const:4:8"]]
+ 00584690 ["CALLIND", null, ["register:0:8"]]
- 00584650 bytes 00013fd6
+ 00584690 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb28935e304c431330143d0c15cbe65a"></a>

### [`00584938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md) → [`00584978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/00584978.md) FUN_00584978

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) [`00587468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587468.md) [`005874c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005874c8.md) [`0058784c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058784c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) [`005874a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005874a8.md) [`00587508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587508.md) [`0058788c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/0058788c.md)

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
      "definition_site": "005849bc",
      "incomplete_value": false,
      "site": "005849c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058497c",
      "incomplete_value": false,
      "site": "00584984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "005849e8",
      "incomplete_value": false,
      "site": "005849f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005849a8",
      "incomplete_value": false,
      "site": "005849b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00584a58",
      "incomplete_value": false,
      "site": "00584a58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00584a18",
      "incomplete_value": false,
      "site": "00584a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:af0:8"
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
      "005849c4",
      "DATA",
      [
        "storage",
        "00c6ca58",
        null,
        "pointer"
      ]
    ],
    [
      "005849f0",
      "DATA",
      [
        "storage",
        "00c6caa8",
        null,
        "pointer"
      ]
    ],
    [
      "00584a58",
      "DATA",
      [
        "storage",
        "00c6caf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005849c4",
      "DATA",
      [
        "storage",
        "00c6cb28",
        null,
        "pointer"
      ]
    ],
    [
      "005849f0",
      "DATA",
      [
        "storage",
        "00c6cb78",
        null,
        "pointer"
      ]
    ],
    [
      "00584a58",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00584970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md#insn-00584970) · [`005849d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md#insn-005849d8) · [`0058497c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/00584938.md#insn-0058497c)
- 新版 `005849b0`（命令位置の公開資料なし） · `00584a18`（命令位置の公開資料なし） · `005849bc`（命令位置の公開資料なし）

~~~diff
- 00584970 ["INT_ADD", "register:40f0:8", ["const:584970:8", "const:4:8"]]
- 00584970 ["CALL", null, ["callee:00c57f60:8"]]
+ 005849b0 ["INT_ADD", "register:40f0:8", ["const:5849b0:8", "const:4:8"]]
+ 005849b0 ["CALL", null, ["callee:00c57f60:8"]]
- 00584970 bytes 484d1b94
+ 005849b0 bytes 6c4d1b94
- 005849d8 ["INT_ADD", "register:40f0:8", ["const:5849d8:8", "const:4:8"]]
- 005849d8 ["CALL", null, ["callee:00c581b0:8"]]
+ 00584a18 ["INT_ADD", "register:40f0:8", ["const:584a18:8", "const:4:8"]]
+ 00584a18 ["CALL", null, ["callee:00c581b0:8"]]
- 005849d8 bytes c24d1b94
+ 00584a18 bytes e64d1b94
- 0058497c ["COPY", "tmp:0:8", ["const:a58:8"]]
- 0058497c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058497c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058497c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005849bc ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 005849bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005849bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005849bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058497c bytes 08612991
+ 005849bc bytes 08a12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afbad8b0ccd21cd0436a35181ca095da"></a>

### [`005853cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005853cc.md) → [`0058540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058540c.md) FUN_0058540c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005856cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md) [`005865cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005865cc.md) · 呼出先 10件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00587f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f14.md) [`00587f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f64.md) [`005880f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005880f4.md)
- 新版 呼出元 2件 [`0058570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md) [`0058660c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/0058660c.md) · 呼出先 10件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00587f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f54.md) [`00587fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587fa4.md) [`00588134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588134.md)

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
      "definition_site": "00585638",
      "incomplete_value": true,
      "site": "00585638",
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
      "definition_site": "005855f8",
      "incomplete_value": true,
      "site": "005855f8",
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
            "const:320:8"
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
      "definition_site": "0058543c",
      "incomplete_value": true,
      "site": "0058543c",
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
      "definition_site": "005853fc",
      "incomplete_value": true,
      "site": "005853fc",
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
      "definition_site": "005854cc",
      "incomplete_value": true,
      "site": "005854cc",
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
      "definition_site": "0058548c",
      "incomplete_value": true,
      "site": "0058548c",
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
      "00585438",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "00585480",
      "READ",
      [
        "storage",
        "00ca63f0",
        null,
        "undefined8"
      ]
    ],
    [
      "005854a4",
      "PARAM",
      [
        "storage",
        "00ca6338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00585438",
      "READ",
      [
        "storage",
        "00ca6440",
        null,
        "undefined8"
      ]
    ],
    [
      "00585480",
      "READ",
      [
        "storage",
        "00ca64f0",
        null,
        "undefined8"
      ]
    ],
    [
      "005854a4",
      "PARAM",
      [
        "storage",
        "00ca6438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058546c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005853cc.md#insn-0058546c) · [`00585524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005853cc.md#insn-00585524) · [`005855b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005853cc.md#insn-005855b4)
- 新版 `005854ac`（命令位置の公開資料なし） · `00585564`（命令位置の公開資料なし） · `005855f4`（命令位置の公開資料なし）

~~~diff
- 0058546c ["INT_ADD", "register:40f0:8", ["const:58546c:8", "const:4:8"]]
- 0058546c ["CALL", null, ["callee:00588134:8"]]
+ 005854ac ["INT_ADD", "register:40f0:8", ["const:5854ac:8", "const:4:8"]]
+ 005854ac ["CALL", null, ["callee:00588134:8"]]
- 0058546c bytes 220b0094
+ 005854ac bytes 220b0094
- 00585524 ["INT_ADD", "register:40f0:8", ["const:585524:8", "const:4:8"]]
- 00585524 ["CALL", null, ["callee:00587fa4:8"]]
+ 00585564 ["INT_ADD", "register:40f0:8", ["const:585564:8", "const:4:8"]]
+ 00585564 ["CALL", null, ["callee:00587fa4:8"]]
- 00585524 bytes 900a0094
+ 00585564 bytes 900a0094
- 005855b4 ["INT_ADD", "register:40f0:8", ["const:5855b4:8", "const:4:8"]]
- 005855b4 ["CALL", null, ["callee:00c57f50:8"]]
+ 005855f4 ["INT_ADD", "register:40f0:8", ["const:5855f4:8", "const:4:8"]]
+ 005855f4 ["CALL", null, ["callee:00c57f50:8"]]
- 005855b4 bytes 334a1b94
+ 005855f4 bytes 574a1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24e9e505a22cad3fd4100c1c6272182b"></a>

### [`005856cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md) → [`0058570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md) Java_jp_co_ponos_battlecats_MyActivity_newResponse

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`0057e090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e090.md) [`00581e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e10.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`0057e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e0d0.md) [`00581e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e50.md)

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
      "definition_site": "00585868",
      "incomplete_value": false,
      "site": "00585874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00585828",
      "incomplete_value": false,
      "site": "00585834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:510:8"
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
      "definition_site": "00585c08",
      "incomplete_value": true,
      "site": "00585c08",
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
      "definition_site": "00585bc8",
      "incomplete_value": true,
      "site": "00585bc8",
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
            "const:320:8"
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
      "definition_site": "00585754",
      "incomplete_value": true,
      "site": "00585754",
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
      "definition_site": "00585714",
      "incomplete_value": true,
      "site": "00585714",
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
      "0058574c",
      "READ",
      [
        "storage",
        "00ca6328",
        null,
        "undefined8"
      ]
    ],
    [
      "00585798",
      "READ",
      [
        "storage",
        "00ca6378",
        null,
        "undefined8"
      ]
    ],
    [
      "00585874",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058574c",
      "READ",
      [
        "storage",
        "00ca6428",
        null,
        "undefined8"
      ]
    ],
    [
      "00585798",
      "READ",
      [
        "storage",
        "00ca6478",
        null,
        "undefined8"
      ]
    ],
    [
      "00585874",
      "DATA",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005857f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md#insn-005857f4) · [`005859f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md#insn-005859f4) · [`00585a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md#insn-00585a80)
- 新版 `00585834`（命令位置の公開資料なし） · `00585a34`（命令位置の公開資料なし） · `00585ac0`（命令位置の公開資料なし）

~~~diff
- 005857f4 ["INT_ADD", "register:40f0:8", ["const:5857f4:8", "const:4:8"]]
- 005857f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00585834 ["INT_ADD", "register:40f0:8", ["const:585834:8", "const:4:8"]]
+ 00585834 ["CALL", null, ["callee:00c57f60:8"]]
- 005857f4 bytes a7491b94
+ 00585834 bytes cb491b94
- 005859f4 ["INT_ADD", "register:40f0:8", ["const:5859f4:8", "const:4:8"]]
- 005859f4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00585a34 ["INT_ADD", "register:40f0:8", ["const:585a34:8", "const:4:8"]]
+ 00585a34 ["CALL", null, ["callee:00c53da0:8"]]
- 005859f4 bytes c3381b94
+ 00585a34 bytes db381b94
- 00585a80 ["INT_ADD", "register:40f0:8", ["const:585a80:8", "const:4:8"]]
- 00585a80 ["CALL", null, ["callee:00c53da0:8"]]
+ 00585ac0 ["INT_ADD", "register:40f0:8", ["const:585ac0:8", "const:4:8"]]
+ 00585ac0 ["CALL", null, ["callee:00c53da0:8"]]
- 00585a80 bytes a0381b94
+ 00585ac0 bytes b8381b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d093ab6d3ec2632f54c9b4177c57a0b3"></a>

### [`00585f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585f10.md) → [`00585f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585f50.md) Java_jp_co_ponos_battlecats_MyActivity_onResponseCodeHeaders

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00585d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585d50.md) [`00588354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588354.md) [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00585d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585d90.md) [`00588394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588394.md) [`00589994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589994.md)

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
      "definition_site": "00585f84",
      "incomplete_value": true,
      "site": "00585f84",
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
      "definition_site": "00585f44",
      "incomplete_value": true,
      "site": "00585f44",
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
      "definition_site": "0058609c",
      "incomplete_value": true,
      "site": "0058609c",
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
      "definition_site": "0058605c",
      "incomplete_value": true,
      "site": "0058605c",
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
        "0058605c"
      ],
      [
        "FALL_THROUGH",
        "0058609c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0058609c",
      "incomplete_value": true,
      "site": "005860bc",
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
      "definition_site": "0058605c",
      "incomplete_value": true,
      "site": "0058607c",
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
      "00585f7c",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "00585fd8",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ],
    [
      "00586094",
      "READ",
      [
        "storage",
        "00ca62e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00585f7c",
      "READ",
      [
        "storage",
        "00ca6440",
        null,
        "undefined8"
      ]
    ],
    [
      "00585fd8",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ],
    [
      "00586094",
      "READ",
      [
        "storage",
        "00ca63e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005860c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585f10.md#insn-005860c0) · [`00585f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585f10.md#insn-00585f38) · [`00585f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585f10.md#insn-00585f4c)
- 新版 `00586100`（命令位置の公開資料なし） · `00585f78`（命令位置の公開資料なし） · `00585f8c`（命令位置の公開資料なし）

~~~diff
- 005860c0 ["INT_ADD", "register:40f0:8", ["const:5860c0:8", "const:4:8"]]
- 005860c0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00586100 ["INT_ADD", "register:40f0:8", ["const:586100:8", "const:4:8"]]
+ 00586100 ["CALL", null, ["callee:00c53da0:8"]]
- 005860c0 bytes 10371b94
+ 00586100 bytes 28371b94
- 00585f38 ["COPY", "tmp:0:8", ["const:340:8"]]
- 00585f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00585f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00585f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00585f78 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00585f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00585f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00585f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00585f38 bytes 08010d91
+ 00585f78 bytes 08011191
- 00585f4c ["COPY", "tmp:0:8", ["const:340:8"]]
- 00585f4c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00585f4c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00585f4c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00585f8c ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00585f8c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00585f8c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00585f8c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00585f4c bytes d6020d91
+ 00585f8c bytes d6021191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcc2c04196c01fbba179e6cc071aab3c"></a>

### [`005862e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005862e4.md) → [`00586324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586324.md) Java_jp_co_ponos_battlecats_MyActivity_onResponseData

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0057e090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e090.md) [`00581e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581e10.md) [`00589be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0057e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e0d0.md) [`00581e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581e50.md) [`00589c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

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
      "definition_site": "00586354",
      "incomplete_value": true,
      "site": "00586354",
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
      "definition_site": "00586314",
      "incomplete_value": true,
      "site": "00586314",
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
      "definition_site": "00586494",
      "incomplete_value": true,
      "site": "00586494",
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
      "definition_site": "00586454",
      "incomplete_value": true,
      "site": "00586454",
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
        "00586454"
      ],
      [
        "FALL_THROUGH",
        "00586494"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00586494",
      "incomplete_value": true,
      "site": "005864b4",
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
      "definition_site": "00586454",
      "incomplete_value": true,
      "site": "00586474",
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
      "00586350",
      "READ",
      [
        "storage",
        "00ca6340",
        null,
        "undefined8"
      ]
    ],
    [
      "005863a8",
      "READ",
      [
        "storage",
        "00ca63c0",
        null,
        "undefined8"
      ]
    ],
    [
      "005863d8",
      "DATA",
      [
        "storage",
        "00c6c510",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00586350",
      "READ",
      [
        "storage",
        "00ca6440",
        null,
        "undefined8"
      ]
    ],
    [
      "005863a8",
      "READ",
      [
        "storage",
        "00ca64c0",
        null,
        "undefined8"
      ]
    ],
    [
      "005863d8",
      "DATA",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005864b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005862e4.md#insn-005864b8) · [`0058630c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005862e4.md#insn-0058630c) · [`0058631c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005862e4.md#insn-0058631c)
- 新版 `005864f8`（命令位置の公開資料なし） · `0058634c`（命令位置の公開資料なし） · `0058635c`（命令位置の公開資料なし）

~~~diff
- 005864b8 ["INT_ADD", "register:40f0:8", ["const:5864b8:8", "const:4:8"]]
- 005864b8 ["CALL", null, ["callee:00c53da0:8"]]
+ 005864f8 ["INT_ADD", "register:40f0:8", ["const:5864f8:8", "const:4:8"]]
+ 005864f8 ["CALL", null, ["callee:00c53da0:8"]]
- 005864b8 bytes 12361b94
+ 005864f8 bytes 2a361b94
- 0058630c ["COPY", "tmp:0:8", ["const:340:8"]]
- 0058630c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058630c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058630c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058634c ["COPY", "tmp:0:8", ["const:440:8"]]
+ 0058634c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058634c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058634c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058630c bytes 08010d91
+ 0058634c bytes 08011191
- 0058631c ["COPY", "tmp:0:8", ["const:340:8"]]
- 0058631c ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 0058631c ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 0058631c ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 0058635c ["COPY", "tmp:0:8", ["const:440:8"]]
+ 0058635c ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 0058635c ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 0058635c ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 0058631c bytes 18030d91
+ 0058635c bytes 18031191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7033eafe84fe6d9344f9d114e3fd26fd"></a>

### [`005865dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005865dc.md) → [`0058661c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/0058661c.md) FUN_0058661c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005866dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005866dc.md) · 呼出先 4件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0058671c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/0058671c.md) · 呼出先 4件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00586638",
      "incomplete_value": false,
      "site": "0058663c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005865f8",
      "incomplete_value": false,
      "site": "005865fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "0058663c",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058663c",
      "DATA",
      [
        "storage",
        "00c6c9b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005865f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005865dc.md#insn-005865f8) · [`00586634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005865dc.md#insn-00586634) · [`00586648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/005865dc.md#insn-00586648)
- 新版 `00586638`（命令位置の公開資料なし） · `00586674`（命令位置の公開資料なし） · `00586688`（命令位置の公開資料なし）

~~~diff
- 005865f8 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 005865f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005865f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005865f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00586638 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00586638 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00586638 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00586638 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005865f8 bytes 08a12391
+ 00586638 bytes 08e12691
- 00586634 ["INT_ADD", "register:40f0:8", ["const:586634:8", "const:4:8"]]
- 00586634 ["CALL", null, ["callee:00c53da0:8"]]
+ 00586674 ["INT_ADD", "register:40f0:8", ["const:586674:8", "const:4:8"]]
+ 00586674 ["CALL", null, ["callee:00c53da0:8"]]
- 00586634 bytes b3351b94
+ 00586674 bytes cb351b94
- 00586648 ["COPY", "register:0:8", ["register:4040:8"]]
- 00586648 ["INT_ADD", "register:40f0:8", ["const:586648:8", "const:4:8"]]
- 00586648 ["CALLIND", null, ["register:0:8"]]
+ 00586688 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00586688 ["INT_ADD", "register:40f0:8", ["const:586688:8", "const:4:8"]]
+ 00586688 ["CALLIND", null, ["register:0:8"]]
- 00586648 bytes 00013fd6
+ 00586688 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-906151079e7f458a0de2b90d12013095"></a>

### [`00586700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586700.md) → [`00586740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586740.md) FUN_00586740

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00586758",
      "incomplete_value": false,
      "site": "0058675c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00586718",
      "incomplete_value": false,
      "site": "0058671c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "0058675c",
      "DATA",
      [
        "storage",
        "00c6c8c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058675c",
      "DATA",
      [
        "storage",
        "00c6c998",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058675c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586700.md#insn-0058675c) · [`00586718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586700.md#insn-00586718) · [`0058674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586700.md#insn-0058674c)
- 新版 `0058679c`（命令位置の公開資料なし） · `00586758`（命令位置の公開資料なし） · `0058678c`（命令位置の公開資料なし）

~~~diff
- 0058675c ["INT_ADD", "register:40f0:8", ["const:58675c:8", "const:4:8"]]
- 0058675c ["CALL", null, ["callee:00c57f80:8"]]
+ 0058679c ["INT_ADD", "register:40f0:8", ["const:58679c:8", "const:4:8"]]
+ 0058679c ["CALL", null, ["callee:00c57f80:8"]]
- 0058675c bytes d5451b94
+ 0058679c bytes f9451b94
- 00586718 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00586718 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00586718 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00586718 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00586758 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00586758 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00586758 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00586758 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00586718 bytes 29212391
+ 00586758 bytes 29612691
- 0058674c ["INT_ADD", "register:40f0:8", ["const:58674c:8", "const:4:8"]]
- 0058674c ["CALL", null, ["callee:00c57f80:8"]]
+ 0058678c ["INT_ADD", "register:40f0:8", ["const:58678c:8", "const:4:8"]]
+ 0058678c ["CALL", null, ["callee:00c57f80:8"]]
- 0058674c bytes d9451b94
+ 0058678c bytes fd451b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a89cfb7585838c9ba4d4884fbcac538"></a>

### [`00586788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586788.md) → [`005867c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/005867c8.md) FUN_005867c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005867e0",
      "incomplete_value": false,
      "site": "005867e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005867a0",
      "incomplete_value": false,
      "site": "005867a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "005867e4",
      "DATA",
      [
        "storage",
        "00c6c8c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005867e4",
      "DATA",
      [
        "storage",
        "00c6c998",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005867a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586788.md#insn-005867a0) · [`005867c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586788.md#insn-005867c8) · [`005867e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586788.md#insn-005867e0)
- 新版 `005867e0`（命令位置の公開資料なし） · `00586808`（命令位置の公開資料なし） · `00586820`（命令位置の公開資料なし）

~~~diff
- 005867a0 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 005867a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005867a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005867a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005867e0 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 005867e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005867e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005867e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005867a0 bytes 29212391
+ 005867e0 bytes 29612691
- 005867c8 ["INT_ADD", "register:40f0:8", ["const:5867c8:8", "const:4:8"]]
- 005867c8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00586808 ["INT_ADD", "register:40f0:8", ["const:586808:8", "const:4:8"]]
+ 00586808 ["CALL", null, ["callee:00c57f80:8"]]
- 005867c8 bytes ba451b94
+ 00586808 bytes de451b94
- 005867e0 ["INT_ADD", "register:40f0:8", ["const:5867e0:8", "const:4:8"]]
- 005867e0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00586820 ["INT_ADD", "register:40f0:8", ["const:586820:8", "const:4:8"]]
+ 00586820 ["CALL", null, ["callee:00c57f80:8"]]
- 005867e0 bytes b4451b94
+ 00586820 bytes d8451b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ed39577cb98827eaa2bab76da285c78"></a>

### [`005870d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005870d8.md) → [`00587118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587118.md) FUN_00587118

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
      "definition_site": "0058711c",
      "incomplete_value": false,
      "site": "00587120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005870dc",
      "incomplete_value": false,
      "site": "005870e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a08:8"
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
      "00587120",
      "DATA",
      [
        "storage",
        "00c6ca08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587120",
      "DATA",
      [
        "storage",
        "00c6cad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005870dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005870d8.md#insn-005870dc)
- 新版 `0058711c`（命令位置の公開資料なし）

~~~diff
- 005870dc ["COPY", "tmp:0:8", ["const:a08:8"]]
- 005870dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005870dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005870dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058711c ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 0058711c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058711c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058711c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005870dc bytes 08212891
+ 0058711c bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f63699e4e7689d5c466e9b5ad0910811"></a>

### [`00587428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587428.md) → [`00587468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587468.md) FUN_00587468

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
      "definition_site": "0058746c",
      "incomplete_value": false,
      "site": "00587470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058742c",
      "incomplete_value": false,
      "site": "00587430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "00587470",
      "DATA",
      [
        "storage",
        "00c6ca58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00587470",
      "DATA",
      [
        "storage",
        "00c6cb28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058742c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587428.md#insn-0058742c)
- 新版 `0058746c`（命令位置の公開資料なし）

~~~diff
- 0058742c ["COPY", "tmp:0:8", ["const:a58:8"]]
- 0058742c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058742c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058742c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058746c ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 0058746c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058746c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058746c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058742c bytes 08612991
+ 0058746c bytes 08a12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-230ad49af12b6aca09d8ff3b27e67f8a"></a>

### [`00587438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587438.md) → [`00587478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587478.md) FUN_00587478

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
      "definition_site": "00587488",
      "incomplete_value": false,
      "site": "00587490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587448",
      "incomplete_value": false,
      "site": "00587450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "00587490",
      "DATA",
      [
        "storage",
        "00c6ca58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00587490",
      "DATA",
      [
        "storage",
        "00c6cb28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587438.md#insn-00587448) · [`00587454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587438.md#insn-00587454)
- 新版 `00587488`（命令位置の公開資料なし） · `00587494`（命令位置の公開資料なし）

~~~diff
- 00587448 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00587448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587488 ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 00587488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587448 bytes 08612991
+ 00587488 bytes 08a12c91
- 00587454 ["INT_ADD", "register:40f0:8", ["const:587454:8", "const:4:8"]]
- 00587454 ["CALL", null, ["callee:00c57f70:8"]]
+ 00587494 ["INT_ADD", "register:40f0:8", ["const:587494:8", "const:4:8"]]
+ 00587494 ["CALL", null, ["callee:00c57f70:8"]]
- 00587454 bytes 93421b94
+ 00587494 bytes b7421b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2832b4b24628b44317bcb1a0432386c9"></a>

### [`00587474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587474.md) → [`005874b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005874b4.md) FUN_005874b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

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
      "definition_site": "005874d8",
      "incomplete_value": true,
      "site": "005874d8",
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
      "definition_site": "00587498",
      "incomplete_value": true,
      "site": "00587498",
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
      "005874cc",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "005874d8",
      "DATA",
      [
        "storage",
        "00c92cd8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005874cc",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "005874d8",
      "DATA",
      [
        "storage",
        "00c92da8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058748c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587474.md#insn-0058748c) · [`0058749c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587474.md#insn-0058749c) · [`005874a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587474.md#insn-005874a4)
- 新版 `005874cc`（命令位置の公開資料なし） · `005874dc`（命令位置の公開資料なし） · `005874e4`（命令位置の公開資料なし）

~~~diff
- 0058748c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
- 0058748c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005874cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
+ 005874cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0058748c bytes 082946f9
+ 005874cc bytes 089146f9
- 0058749c ["INT_ADD", "register:40f0:8", ["const:58749c:8", "const:4:8"]]
- 0058749c ["CALL", null, ["callee:00c581a0:8"]]
+ 005874dc ["INT_ADD", "register:40f0:8", ["const:5874dc:8", "const:4:8"]]
+ 005874dc ["CALL", null, ["callee:00c581a0:8"]]
- 0058749c bytes 0d431b94
+ 005874dc bytes 31431b94
- 005874a4 ["INT_ADD", "register:40f0:8", ["const:5874a4:8", "const:4:8"]]
- 005874a4 ["CALL", null, ["callee:00c57f30:8"]]
+ 005874e4 ["INT_ADD", "register:40f0:8", ["const:5874e4:8", "const:4:8"]]
+ 005874e4 ["CALL", null, ["callee:00c57f30:8"]]
- 005874a4 bytes 6f421b94
+ 005874e4 bytes 93421b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce12f9b444b14c3e754c671f601b9d0c"></a>

### [`005875e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005875e8.md) → [`00587628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587628.md) FUN_00587628

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00587468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587468.md) · 呼出先 12件 [`0045a6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6c8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)
- 新版 呼出元 1件 [`005874a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005874a8.md) · 呼出先 12件 [`0045a708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a708.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.15% / 新版 93.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005876cc",
      "incomplete_value": true,
      "site": "005876d0",
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
      "definition_site": "0058768c",
      "incomplete_value": true,
      "site": "00587690",
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
      "definition_site": "005876a8",
      "incomplete_value": true,
      "site": "005876b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587668",
      "incomplete_value": true,
      "site": "00587670",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:c58:8"
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
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005876a4",
      "incomplete_value": false,
      "site": "005876b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:45a000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587664",
      "incomplete_value": false,
      "site": "00587670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:45a000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005876a4",
      "PARAM",
      [
        "storage",
        "0045a6c8",
        null,
        null
      ]
    ],
    [
      "005876a8",
      "READ",
      [
        "storage",
        "00c9ac58",
        null,
        "pointer"
      ]
    ],
    [
      "005876a8",
      "PARAM",
      [
        "storage",
        "00c92cb0",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005876a4",
      "PARAM",
      [
        "storage",
        "0045a708",
        null,
        null
      ]
    ],
    [
      "005876a8",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ],
    [
      "005876a8",
      "PARAM",
      [
        "storage",
        "00c92d80",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005875e8.md#insn-00587650) · [`00587670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005875e8.md#insn-00587670) · [`00587628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005875e8.md#insn-00587628)
- 新版 `00587690`（命令位置の公開資料なし） · `005876b0`（命令位置の公開資料なし） · `00587668`（命令位置の公開資料なし）

~~~diff
- 00587650 ["INT_ADD", "register:40f0:8", ["const:587650:8", "const:4:8"]]
- 00587650 ["CALL", null, ["callee:00c583f0:8"]]
+ 00587690 ["INT_ADD", "register:40f0:8", ["const:587690:8", "const:4:8"]]
+ 00587690 ["CALL", null, ["callee:00c583f0:8"]]
- 00587650 bytes 34431b94
+ 00587690 bytes 58431b94
- 00587670 ["INT_ADD", "register:40f0:8", ["const:587670:8", "const:4:8"]]
- 00587670 ["CALL", null, ["callee:00c58400:8"]]
+ 005876b0 ["INT_ADD", "register:40f0:8", ["const:5876b0:8", "const:4:8"]]
+ 005876b0 ["CALL", null, ["callee:00c58400:8"]]
- 00587670 bytes 30431b94
+ 005876b0 bytes 54431b94
- 00587628 ["INT_ADD", "register:40f0:8", ["const:587628:8", "const:4:8"]]
- 00587628 ["CALL", null, ["callee:00c583c0:8"]]
+ 00587668 ["INT_ADD", "register:40f0:8", ["const:587668:8", "const:4:8"]]
+ 00587668 ["CALL", null, ["callee:00c583c0:8"]]
- 00587628 bytes 32431b94
+ 00587668 bytes 56431b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ebbfce614b4beef48280cfdf770630c"></a>

### [`00587710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587710.md) → [`00587750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587750.md) FUN_00587750

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00587764",
      "incomplete_value": false,
      "site": "00587768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587724",
      "incomplete_value": false,
      "site": "00587728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:af0:8"
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
      "00587768",
      "DATA",
      [
        "storage",
        "00c6caf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587768",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587710.md#insn-00587724) · [`00587738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587710.md#insn-00587738) · [`00587758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587710.md#insn-00587758)
- 新版 `00587764`（命令位置の公開資料なし） · `00587778`（命令位置の公開資料なし） · `00587798`（命令位置の公開資料なし）

~~~diff
- 00587724 ["COPY", "tmp:0:8", ["const:af0:8"]]
- 00587724 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587724 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587724 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587764 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00587764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587724 bytes 08c12b91
+ 00587764 bytes 08012f91
- 00587738 ["INT_ADD", "register:40f0:8", ["const:587738:8", "const:4:8"]]
- 00587738 ["CALL", null, ["callee:00c53da0:8"]]
+ 00587778 ["INT_ADD", "register:40f0:8", ["const:587778:8", "const:4:8"]]
+ 00587778 ["CALL", null, ["callee:00c53da0:8"]]
- 00587738 bytes 72311b94
+ 00587778 bytes 8a311b94
- 00587758 ["COPY", "register:0:8", ["register:4040:8"]]
- 00587758 ["INT_ADD", "register:40f0:8", ["const:587758:8", "const:4:8"]]
- 00587758 ["CALLIND", null, ["register:0:8"]]
+ 00587798 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00587798 ["INT_ADD", "register:40f0:8", ["const:587798:8", "const:4:8"]]
+ 00587798 ["CALLIND", null, ["register:0:8"]]
- 00587758 bytes 00013fd6
+ 00587798 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f1ed43ba624475787fca82681b87093"></a>

### [`0058776c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058776c.md) → [`005877ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005877ac.md) FUN_005877ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005877c4",
      "incomplete_value": false,
      "site": "005877c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587784",
      "incomplete_value": false,
      "site": "00587788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "005877c8",
      "DATA",
      [
        "storage",
        "00c6caf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005877c8",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058776c.md#insn-00587784) · [`00587798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058776c.md#insn-00587798) · [`005877ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/0058776c.md#insn-005877ac)
- 新版 `005877c4`（命令位置の公開資料なし） · `005877d8`（命令位置の公開資料なし） · `005877ec`（命令位置の公開資料なし）

~~~diff
- 00587784 ["COPY", "tmp:0:8", ["const:af0:8"]]
- 00587784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005877c4 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 005877c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005877c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005877c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587784 bytes 08c12b91
+ 005877c4 bytes 08012f91
- 00587798 ["INT_ADD", "register:40f0:8", ["const:587798:8", "const:4:8"]]
- 00587798 ["CALL", null, ["callee:00c53da0:8"]]
+ 005877d8 ["INT_ADD", "register:40f0:8", ["const:5877d8:8", "const:4:8"]]
+ 005877d8 ["CALL", null, ["callee:00c53da0:8"]]
- 00587798 bytes 5a311b94
+ 005877d8 bytes 72311b94
- 005877ac ["COPY", "register:0:8", ["register:4040:8"]]
- 005877ac ["INT_ADD", "register:40f0:8", ["const:5877ac:8", "const:4:8"]]
- 005877ac ["CALLIND", null, ["register:0:8"]]
+ 005877ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005877ec ["INT_ADD", "register:40f0:8", ["const:5877ec:8", "const:4:8"]]
+ 005877ec ["CALLIND", null, ["register:0:8"]]
- 005877ac bytes 00013fd6
+ 005877ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5c52c4e6c3d03caa8a13cd4703f96c4"></a>

### [`005877c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005877c8.md) → [`00587808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587808.md) FUN_00587808

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0058782c",
      "incomplete_value": false,
      "site": "0058782c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005877ec",
      "incomplete_value": false,
      "site": "005877ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:af0:8"
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
      "0058782c",
      "DATA",
      [
        "storage",
        "00c6caf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058782c",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005877dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005877c8.md#insn-005877dc) · [`005877e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005877c8.md#insn-005877e8) · [`00587804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/005877c8.md#insn-00587804)
- 新版 `0058781c`（命令位置の公開資料なし） · `00587828`（命令位置の公開資料なし） · `00587844`（命令位置の公開資料なし）

~~~diff
- 005877dc ["INT_ADD", "register:40f0:8", ["const:5877dc:8", "const:4:8"]]
- 005877dc ["CALL", null, ["callee:00c57f60:8"]]
+ 0058781c ["INT_ADD", "register:40f0:8", ["const:58781c:8", "const:4:8"]]
+ 0058781c ["CALL", null, ["callee:00c57f60:8"]]
- 005877dc bytes ad411b94
+ 0058781c bytes d1411b94
- 005877e8 ["COPY", "tmp:0:8", ["const:af0:8"]]
- 005877e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005877e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005877e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00587828 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00587828 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00587828 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00587828 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005877e8 bytes 29c12b91
+ 00587828 bytes 29012f91
- 00587804 ["INT_ADD", "register:40f0:8", ["const:587804:8", "const:4:8"]]
- 00587804 ["CALL", null, ["callee:00c53d70:8"]]
+ 00587844 ["INT_ADD", "register:40f0:8", ["const:587844:8", "const:4:8"]]
+ 00587844 ["CALL", null, ["callee:00c53d70:8"]]
- 00587804 bytes 33311b94
+ 00587844 bytes 4b311b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d02ff55e2232898277f90addb295420"></a>

### [`00587818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587818.md) → [`00587858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587858.md) FUN_00587858

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "00587864",
      "incomplete_value": false,
      "site": "00587864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587824",
      "incomplete_value": false,
      "site": "00587824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00587864",
      "DATA",
      [
        "storage",
        "00c6caf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587864",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587818.md#insn-00587820) · [`00587840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587818.md#insn-00587840)
- 新版 `00587860`（命令位置の公開資料なし） · `00587880`（命令位置の公開資料なし）

~~~diff
- 00587820 ["COPY", "tmp:0:8", ["const:af0:8"]]
- 00587820 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00587820 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00587820 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00587860 ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00587860 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00587860 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00587860 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00587820 bytes 29c12b91
+ 00587860 bytes 29012f91
- 00587840 ["INT_ADD", "register:40f0:8", ["const:587840:8", "const:4:8"]]
- 00587840 ["CALL", null, ["callee:00c53d70:8"]]
+ 00587880 ["INT_ADD", "register:40f0:8", ["const:587880:8", "const:4:8"]]
+ 00587880 ["CALL", null, ["callee:00c53d70:8"]]
- 00587840 bytes 24311b94
+ 00587880 bytes 3c311b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcf0c0d0c13ba6375ac327d71fb624a7"></a>

### [`00587d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587d94.md) → [`00587dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587dd4.md) FUN_00587dd4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00587c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587c54.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00587c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587c94.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00587de0",
      "incomplete_value": false,
      "site": "00587de4",
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
      "definition_site": "00587da0",
      "incomplete_value": false,
      "site": "00587da4",
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
      "00587de0",
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
      "00587de0",
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

- 旧版 [`00587da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587d94.md#insn-00587da4) · [`00587da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587d94.md#insn-00587da0)
- 新版 `00587de4`（命令位置の公開資料なし） · `00587de0`（命令位置の公開資料なし）

~~~diff
- 00587da4 ["INT_ADD", "register:40f0:8", ["const:587da4:8", "const:4:8"]]
- 00587da4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00587de4 ["INT_ADD", "register:40f0:8", ["const:587de4:8", "const:4:8"]]
+ 00587de4 ["CALL", null, ["callee:0043b7b8:8"]]
- 00587da4 bytes 75cefa97
+ 00587de4 bytes 75cefa97
- 00587da0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00587da0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00587da0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00587da0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00587de0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00587de0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00587de0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00587de0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00587da0 bytes 00303d91
+ 00587de0 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06c7c41f9417199011961fdf46991196"></a>

### [`00587da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587da8.md) → [`00587de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587de8.md) FUN_00587de8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00585324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585324.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 1件 [`00585364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585364.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

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
      "definition_site": "00587e04",
      "incomplete_value": false,
      "site": "00587e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587dc4",
      "incomplete_value": false,
      "site": "00587dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "definition_site": "00587e10",
      "incomplete_value": false,
      "site": "00587e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587dd0",
      "incomplete_value": false,
      "site": "00587dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "00587e04",
      "DATA",
      [
        "storage",
        "00c6cb70",
        null,
        "undefined *"
      ]
    ],
    [
      "00587e10",
      "DATA",
      [
        "storage",
        "00c6c8e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587e04",
      "DATA",
      [
        "storage",
        "00c6cc40",
        null,
        "undefined *"
      ]
    ],
    [
      "00587e10",
      "DATA",
      [
        "storage",
        "00c6c9b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587da8.md#insn-00587dbc) · [`00587dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587da8.md#insn-00587dc8) · [`00587dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587da8.md#insn-00587dcc)
- 新版 `00587dfc`（命令位置の公開資料なし） · `00587e0c`（命令位置の公開資料なし）

~~~diff
- 00587dbc ["COPY", "tmp:0:8", ["const:b70:8"]]
- 00587dbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587dbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587dbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587dfc ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00587dfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587dfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587dfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587dbc bytes 08c12d91
+ 00587dfc bytes 08013191
- 00587dc8 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00587dc8 bytes 283700b0
- 00587dcc ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 00587dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587e0c ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00587e0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587e0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587e0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587dcc bytes 08a12391
+ 00587e0c bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77a0af45d9db07cf9c22a633ec8072db"></a>

### [`00587e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587e84.md) → [`00587ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587ec4.md) FUN_00587ec4

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
      "definition_site": "00587ec8",
      "incomplete_value": false,
      "site": "00587ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587e88",
      "incomplete_value": false,
      "site": "00587e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00587ecc",
      "DATA",
      [
        "storage",
        "00c6cb70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587ecc",
      "DATA",
      [
        "storage",
        "00c6cc40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587e84.md#insn-00587e88)
- 新版 `00587ec8`（命令位置の公開資料なし）

~~~diff
- 00587e88 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 00587e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587ec8 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00587ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587e88 bytes 08c12d91
+ 00587ec8 bytes 08013191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-438da5ee3512ce9d2530f43204be8b8f"></a>

### [`00587e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587e94.md) → [`00587ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587ed4.md) FUN_00587ed4

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
      "definition_site": "00587ee4",
      "incomplete_value": true,
      "site": "00587eec",
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
    "old": {
      "definition_site": "00587ea4",
      "incomplete_value": true,
      "site": "00587eac",
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
            "const:b70:8"
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
      "00587eec",
      "DATA",
      [
        "storage",
        "00c6cb70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587eec",
      "DATA",
      [
        "storage",
        "00c6cc40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587e94.md#insn-00587ea4) · [`00587eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587e94.md#insn-00587eb0)
- 新版 `00587ee4`（命令位置の公開資料なし） · `00587ef0`（命令位置の公開資料なし）

~~~diff
- 00587ea4 ["COPY", "tmp:0:8", ["const:b70:8"]]
- 00587ea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587ea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587ea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587ee4 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00587ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587ea4 bytes 08c12d91
+ 00587ee4 bytes 08013191
- 00587eb0 ["INT_ADD", "register:40f0:8", ["const:587eb0:8", "const:4:8"]]
- 00587eb0 ["CALL", null, ["callee:00c57f70:8"]]
+ 00587ef0 ["INT_ADD", "register:40f0:8", ["const:587ef0:8", "const:4:8"]]
+ 00587ef0 ["CALL", null, ["callee:00c57f70:8"]]
- 00587eb0 bytes fc3f1b94
+ 00587ef0 bytes 20401b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f65f383db923a0014543a97b6fdb0188"></a>

### [`00587ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587ed4.md) → [`00587f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f14.md) FUN_00587f14

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
      "definition_site": "00587f18",
      "incomplete_value": false,
      "site": "00587f1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587ed8",
      "incomplete_value": false,
      "site": "00587edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00587f1c",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00587f1c",
      "DATA",
      [
        "storage",
        "00c6cc90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587ed4.md#insn-00587ed8)
- 新版 `00587f18`（命令位置の公開資料なし）

~~~diff
- 00587ed8 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00587ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587f18 ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 00587f18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587f18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587f18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587ed8 bytes 08012f91
+ 00587f18 bytes 08413291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b8195cd91ccadb647bc265d31a63c7e"></a>

### [`00587ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587ee4.md) → [`00587f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f24.md) FUN_00587f24

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
      "definition_site": "00587f34",
      "incomplete_value": false,
      "site": "00587f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587ef4",
      "incomplete_value": false,
      "site": "00587efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00587f3c",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00587f3c",
      "DATA",
      [
        "storage",
        "00c6cc90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587ee4.md#insn-00587ef4) · [`00587f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587ee4.md#insn-00587f00)
- 新版 `00587f34`（命令位置の公開資料なし） · `00587f40`（命令位置の公開資料なし）

~~~diff
- 00587ef4 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00587ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587f34 ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 00587f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587ef4 bytes 08012f91
+ 00587f34 bytes 08413291
- 00587f00 ["INT_ADD", "register:40f0:8", ["const:587f00:8", "const:4:8"]]
- 00587f00 ["CALL", null, ["callee:00c57f70:8"]]
+ 00587f40 ["INT_ADD", "register:40f0:8", ["const:587f40:8", "const:4:8"]]
+ 00587f40 ["CALL", null, ["callee:00c57f70:8"]]
- 00587f00 bytes e83f1b94
+ 00587f40 bytes 0c401b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-513ea2827a9e96c47f670d7a26b6765b"></a>

### [`00587f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f14.md) → [`00587f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587f54.md) FUN_00587f54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005853cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005853cc.md) · 呼出先 2件 [`00587078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587078.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0058540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058540c.md) · 呼出先 2件 [`005870b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/005870b8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00587f68",
      "incomplete_value": false,
      "site": "00587f70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00587f28",
      "incomplete_value": false,
      "site": "00587f30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00587f70",
      "DATA",
      [
        "storage",
        "00c6c898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00587f70",
      "DATA",
      [
        "storage",
        "00c6c968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f14.md#insn-00587f28) · [`00587f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f14.md#insn-00587f38)
- 新版 `00587f68`（命令位置の公開資料なし） · `00587f78`（命令位置の公開資料なし）

~~~diff
- 00587f28 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00587f28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00587f28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00587f28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00587f68 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00587f68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00587f68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00587f68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00587f28 bytes 08612291
+ 00587f68 bytes 08a12591
- 00587f38 ["INT_ADD", "register:40f0:8", ["const:587f38:8", "const:4:8"]]
- 00587f38 ["CALL", null, ["callee:005870b8:8"]]
+ 00587f78 ["INT_ADD", "register:40f0:8", ["const:587f78:8", "const:4:8"]]
+ 00587f78 ["CALL", null, ["callee:005870b8:8"]]
- 00587f38 bytes 50fcff97
+ 00587f78 bytes 50fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fc0b7c005d2b9e2dd619d73572c4ae1"></a>

### [`00587f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f64.md) → [`00587fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587fa4.md) FUN_00587fa4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005853cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005853cc.md) · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0058540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058540c.md) · 呼出先 7件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00588054",
      "incomplete_value": false,
      "site": "0058805c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588014",
      "incomplete_value": false,
      "site": "0058801c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "0058805c",
      "DATA",
      [
        "storage",
        "00c6c898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058805c",
      "DATA",
      [
        "storage",
        "00c6c968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00587f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f64.md#insn-00587f9c) · [`00587fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f64.md#insn-00587fe8) · [`00588008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587f64.md#insn-00588008)
- 新版 `00587fdc`（命令位置の公開資料なし） · `00588028`（命令位置の公開資料なし） · `00588048`（命令位置の公開資料なし）

~~~diff
- 00587f9c ["INT_ADD", "register:40f0:8", ["const:587f9c:8", "const:4:8"]]
- 00587f9c ["CALL", null, ["callee:00c580b0:8"]]
+ 00587fdc ["INT_ADD", "register:40f0:8", ["const:587fdc:8", "const:4:8"]]
+ 00587fdc ["CALL", null, ["callee:00c580b0:8"]]
- 00587f9c bytes 11401b94
+ 00587fdc bytes 35401b94
- 00587fe8 ["INT_ADD", "register:40f0:8", ["const:587fe8:8", "const:4:8"]]
- 00587fe8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00588028 ["INT_ADD", "register:40f0:8", ["const:588028:8", "const:4:8"]]
+ 00588028 ["CALL", null, ["callee:00c57f60:8"]]
- 00587fe8 bytes aa3f1b94
+ 00588028 bytes ce3f1b94
- 00588008 ["INT_ADD", "register:40f0:8", ["const:588008:8", "const:4:8"]]
- 00588008 ["CALL", null, ["callee:00c580d0:8"]]
+ 00588048 ["INT_ADD", "register:40f0:8", ["const:588048:8", "const:4:8"]]
+ 00588048 ["CALL", null, ["callee:00c580d0:8"]]
- 00588008 bytes fe3f1b94
+ 00588048 bytes 22401b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ddc80e1dc62cd5b1b46eaf408d5b6d5"></a>

### [`00588354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588354.md) → [`00588394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588394.md) FUN_00588394

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005856cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/005856cc.md) [`00585f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585f10.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00586c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00586/00586c1c.md)
- 新版 呼出元 2件 [`0058570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/0058570c.md) [`00585f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585f50.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00586c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00586/00586c5c.md)

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
      "definition_site": "005883ac",
      "incomplete_value": false,
      "site": "005883b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058836c",
      "incomplete_value": false,
      "site": "00588370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "definition_site": "005883bc",
      "incomplete_value": false,
      "site": "005883c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058837c",
      "incomplete_value": false,
      "site": "00588388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "005883b0",
      "DATA",
      [
        "storage",
        "00c6cbc0",
        null,
        "pointer"
      ]
    ],
    [
      "005883c8",
      "DATA",
      [
        "storage",
        "00c6c898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005883b0",
      "DATA",
      [
        "storage",
        "00c6cc90",
        null,
        "pointer"
      ]
    ],
    [
      "005883c8",
      "DATA",
      [
        "storage",
        "00c6c968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058836c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588354.md#insn-0058836c) · [`00588378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588354.md#insn-00588378) · [`0058837c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588354.md#insn-0058837c)
- 新版 `005883ac`（命令位置の公開資料なし） · `005883bc`（命令位置の公開資料なし）

~~~diff
- 0058836c ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 0058836c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058836c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058836c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005883ac ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 005883ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005883ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005883ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058836c bytes 29012f91
+ 005883ac bytes 29413291
- 00588378 ["COPY", "register:4040:8", ["const:c6c000:8"]]
- 00588378 bytes 28370090
- 0058837c ["COPY", "tmp:0:8", ["const:898:8"]]
- 0058837c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058837c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058837c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005883bc ["COPY", "tmp:0:8", ["const:968:8"]]
+ 005883bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005883bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005883bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058837c bytes 08612291
+ 005883bc bytes 08a12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70fa32c23635af7883ae48240f6d078a"></a>

### [`00588424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588424.md) → [`00588464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588464.md) _INIT_32

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0058331c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058331c.md) [`0058334c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058334c.md) [`0058337c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/0058337c.md) [`00583384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/00583384.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0058335c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058335c.md) [`0058338c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/0058338c.md) [`005833bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005833bc.md) [`005833c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005833c4.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)

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
      "definition_site": "0058848c",
      "incomplete_value": false,
      "site": "0058848c",
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
                "const:ca6000:8"
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
      "definition_site": "0058844c",
      "incomplete_value": false,
      "site": "0058844c",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:2c0:8"
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
      "definition_site": "005884a8",
      "incomplete_value": false,
      "site": "005884a8",
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
                "const:ca6000:8"
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
      "definition_site": "00588468",
      "incomplete_value": false,
      "site": "00588468",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:2f0:8"
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
      "definition_site": "005884c8",
      "incomplete_value": false,
      "site": "005884c8",
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
                "const:ca6000:8"
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
      "definition_site": "00588488",
      "incomplete_value": false,
      "site": "00588488",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:320:8"
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
      "0058847c",
      "PARAM",
      [
        "storage",
        "00ca62c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00588444",
      "PARAM",
      [
        "storage",
        "0058331c",
        null,
        null
      ]
    ],
    [
      "00588488",
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058847c",
      "PARAM",
      [
        "storage",
        "00ca63c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00588484",
      "PARAM",
      [
        "storage",
        "0058335c",
        null,
        null
      ]
    ],
    [
      "00588488",
      "PARAM",
      [
        "storage",
        "00c63060",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588424.md#insn-00588450) · [`0058846c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588424.md#insn-0058846c)
- 新版 `00588490`（命令位置の公開資料なし）

~~~diff
- 00588450 ["INT_ADD", "register:40f0:8", ["const:588450:8", "const:4:8"]]
- 00588450 ["CALL", null, ["callee:00c57f00:8"]]
- 00588450 bytes 783e1b94
- 0058846c ["INT_ADD", "register:40f0:8", ["const:58846c:8", "const:4:8"]]
- 0058846c ["CALL", null, ["callee:00c57f00:8"]]
- 0058846c bytes 713e1b94
+ 00588490 ["INT_ADD", "register:40f0:8", ["const:588490:8", "const:4:8"]]
+ 00588490 ["CALL", null, ["callee:00c57f00:8"]]
+ 00588490 bytes 9c3e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e96a87b14e2869f25a9d526412a2ba0"></a>

### [`005884c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005884c8.md) → [`00588508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588508.md) FUN_00588508

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005975fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005975fc.md) · 呼出先 2件 [`00594938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00594/00594938.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0059763c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059763c.md) · 呼出先 2件 [`00594978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00594/00594978.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00588540",
      "incomplete_value": false,
      "site": "0058854c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588500",
      "incomplete_value": false,
      "site": "0058850c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "0058854c",
      "DATA",
      [
        "storage",
        "00c6cc10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058854c",
      "DATA",
      [
        "storage",
        "00c6cce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005884f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005884c8.md#insn-005884f4) · [`00588500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005884c8.md#insn-00588500) · [`0058851c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005884c8.md#insn-0058851c)
- 新版 `00588534`（命令位置の公開資料なし） · `00588540`（命令位置の公開資料なし） · `0058855c`（命令位置の公開資料なし）

~~~diff
- 005884f4 ["INT_ADD", "register:40f0:8", ["const:5884f4:8", "const:4:8"]]
- 005884f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00588534 ["INT_ADD", "register:40f0:8", ["const:588534:8", "const:4:8"]]
+ 00588534 ["CALL", null, ["callee:00c57f60:8"]]
- 005884f4 bytes 673e1b94
+ 00588534 bytes 8b3e1b94
- 00588500 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00588500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00588500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00588500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588540 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 00588540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00588500 bytes 08413091
+ 00588540 bytes 08813391
- 0058851c ["INT_ADD", "register:40f0:8", ["const:58851c:8", "const:4:8"]]
- 0058851c ["CALL", null, ["callee:00594978:8"]]
+ 0058855c ["INT_ADD", "register:40f0:8", ["const:58855c:8", "const:4:8"]]
+ 0058855c ["CALL", null, ["callee:00594978:8"]]
- 0058851c bytes 07310094
+ 0058855c bytes 07310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-659a1fc2a026eb2fa13cf8c42a4c5592"></a>

### [`0058855c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058855c.md) → [`0058859c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058859c.md) FUN_0058859c

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
      "definition_site": "005885a0",
      "incomplete_value": false,
      "site": "005885a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588560",
      "incomplete_value": false,
      "site": "00588564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "005885a4",
      "DATA",
      [
        "storage",
        "00c6cc10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005885a4",
      "DATA",
      [
        "storage",
        "00c6cce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058855c.md#insn-00588560)
- 新版 `005885a0`（命令位置の公開資料なし）

~~~diff
- 00588560 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00588560 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00588560 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00588560 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005885a0 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 005885a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005885a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005885a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00588560 bytes 08413091
+ 005885a0 bytes 08813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69e84668f42c6aa6e14481af551d58aa"></a>

### [`0058856c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058856c.md) → [`005885ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/005885ac.md) FUN_005885ac

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
      "definition_site": "005885bc",
      "incomplete_value": false,
      "site": "005885c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058857c",
      "incomplete_value": false,
      "site": "00588584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "005885c4",
      "DATA",
      [
        "storage",
        "00c6cc10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005885c4",
      "DATA",
      [
        "storage",
        "00c6cce0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058857c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058856c.md#insn-0058857c) · [`00588588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058856c.md#insn-00588588)
- 新版 `005885bc`（命令位置の公開資料なし） · `005885c8`（命令位置の公開資料なし）

~~~diff
- 0058857c ["COPY", "tmp:0:8", ["const:c10:8"]]
- 0058857c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058857c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058857c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005885bc ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 005885bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005885bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005885bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058857c bytes 08413091
+ 005885bc bytes 08813391
- 00588588 ["INT_ADD", "register:40f0:8", ["const:588588:8", "const:4:8"]]
- 00588588 ["CALL", null, ["callee:00c57f70:8"]]
+ 005885c8 ["INT_ADD", "register:40f0:8", ["const:5885c8:8", "const:4:8"]]
+ 005885c8 ["CALL", null, ["callee:00c57f70:8"]]
- 00588588 bytes 463e1b94
+ 005885c8 bytes 6a3e1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f655ac93bb678f5e131874ba6b7e15e"></a>

### [`005885f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885f8.md) → [`00588638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588638.md) FUN_00588638

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00588bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588bc0.md) · 呼出先 7件 [`00588cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588cec.md) [`0058ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00588c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588c00.md) · 呼出先 7件 [`00588d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588d2c.md) [`0058ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00588668",
      "incomplete_value": false,
      "site": "0058867c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588628",
      "incomplete_value": false,
      "site": "0058863c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "0058867c",
      "DATA",
      [
        "storage",
        "00c6cc60",
        null,
        "undefined *"
      ]
    ],
    [
      "0058874c",
      "DATA",
      [
        "storage",
        "00c6c260",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058867c",
      "DATA",
      [
        "storage",
        "00c6cd30",
        null,
        "undefined *"
      ]
    ],
    [
      "0058874c",
      "DATA",
      [
        "storage",
        "00c6c330",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885f8.md#insn-00588628) · [`00588658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885f8.md#insn-00588658) · [`00588670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885f8.md#insn-00588670)
- 新版 `00588668`（命令位置の公開資料なし） · `00588698`（命令位置の公開資料なし） · `005886b0`（命令位置の公開資料なし）

~~~diff
- 00588628 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 00588628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00588628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00588628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588668 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 00588668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00588628 bytes 08813191
+ 00588668 bytes 08c13491
- 00588658 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588658 ["INT_ADD", "register:40f0:8", ["const:588658:8", "const:4:8"]]
- 00588658 ["CALLIND", null, ["register:0:8"]]
+ 00588698 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588698 ["INT_ADD", "register:40f0:8", ["const:588698:8", "const:4:8"]]
+ 00588698 ["CALLIND", null, ["register:0:8"]]
- 00588658 bytes 00013fd6
+ 00588698 bytes 00013fd6
- 00588670 ["COPY", "register:0:8", ["register:4048:8"]]
- 00588670 ["INT_ADD", "register:40f0:8", ["const:588670:8", "const:4:8"]]
- 00588670 ["CALLIND", null, ["register:0:8"]]
+ 005886b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005886b0 ["INT_ADD", "register:40f0:8", ["const:5886b0:8", "const:4:8"]]
+ 005886b0 ["CALLIND", null, ["register:0:8"]]
- 00588670 bytes 20013fd6
+ 005886b0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96a04983fff1c2939e9674239d3f40cc"></a>

### [`005887e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005887e0.md) → [`00588820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588820.md) FUN_00588820

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00588834",
      "incomplete_value": false,
      "site": "00588838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005887f4",
      "incomplete_value": false,
      "site": "005887f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00588838",
      "DATA",
      [
        "storage",
        "00c6cc60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588838",
      "DATA",
      [
        "storage",
        "00c6cd30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005887f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005887e0.md#insn-005887f4) · [`00588808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005887e0.md#insn-00588808) · [`00588828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005887e0.md#insn-00588828)
- 新版 `00588834`（命令位置の公開資料なし） · `00588848`（命令位置の公開資料なし） · `00588868`（命令位置の公開資料なし）

~~~diff
- 005887f4 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 005887f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005887f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005887f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588834 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 00588834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005887f4 bytes 08813191
+ 00588834 bytes 08c13491
- 00588808 ["INT_ADD", "register:40f0:8", ["const:588808:8", "const:4:8"]]
- 00588808 ["CALL", null, ["callee:00c53da0:8"]]
+ 00588848 ["INT_ADD", "register:40f0:8", ["const:588848:8", "const:4:8"]]
+ 00588848 ["CALL", null, ["callee:00c53da0:8"]]
- 00588808 bytes 3e2d1b94
+ 00588848 bytes 562d1b94
- 00588828 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588828 ["INT_ADD", "register:40f0:8", ["const:588828:8", "const:4:8"]]
- 00588828 ["CALLIND", null, ["register:0:8"]]
+ 00588868 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588868 ["INT_ADD", "register:40f0:8", ["const:588868:8", "const:4:8"]]
+ 00588868 ["CALLIND", null, ["register:0:8"]]
- 00588828 bytes 00013fd6
+ 00588868 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e128445c70270c49257013c789b92f47"></a>

### [`0058883c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058883c.md) → [`0058887c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/0058887c.md) FUN_0058887c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00588894",
      "incomplete_value": false,
      "site": "00588898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588854",
      "incomplete_value": false,
      "site": "00588858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "00588898",
      "DATA",
      [
        "storage",
        "00c6cc60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588898",
      "DATA",
      [
        "storage",
        "00c6cd30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058883c.md#insn-00588854) · [`00588868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058883c.md#insn-00588868) · [`0058887c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/0058883c.md#insn-0058887c)
- 新版 `00588894`（命令位置の公開資料なし） · `005888a8`（命令位置の公開資料なし） · `005888bc`（命令位置の公開資料なし）

~~~diff
- 00588854 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 00588854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00588854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00588854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588894 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 00588894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00588854 bytes 08813191
+ 00588894 bytes 08c13491
- 00588868 ["INT_ADD", "register:40f0:8", ["const:588868:8", "const:4:8"]]
- 00588868 ["CALL", null, ["callee:00c53da0:8"]]
+ 005888a8 ["INT_ADD", "register:40f0:8", ["const:5888a8:8", "const:4:8"]]
+ 005888a8 ["CALL", null, ["callee:00c53da0:8"]]
- 00588868 bytes 262d1b94
+ 005888a8 bytes 3e2d1b94
- 0058887c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058887c ["INT_ADD", "register:40f0:8", ["const:58887c:8", "const:4:8"]]
- 0058887c ["CALLIND", null, ["register:0:8"]]
+ 005888bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005888bc ["INT_ADD", "register:40f0:8", ["const:5888bc:8", "const:4:8"]]
+ 005888bc ["CALLIND", null, ["register:0:8"]]
- 0058887c bytes 00013fd6
+ 005888bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80387cc9bf9992d19c94755b36346841"></a>

### [`00588bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588bc0.md) → [`00588c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588c00.md) FUN_00588c00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00588af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588af8.md) [`00597604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597604.md) · 呼出先 6件 [`005885f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885f8.md) [`005975fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005975fc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`00588b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588b38.md) [`00597644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597644.md) · 呼出先 6件 [`00588638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588638.md) [`0059763c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059763c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00588c50",
      "incomplete_value": false,
      "site": "00588c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588c10",
      "incomplete_value": false,
      "site": "00588c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "00588c5c",
      "DATA",
      [
        "storage",
        "00c6b940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00588c5c",
      "DATA",
      [
        "storage",
        "00c6ba10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588bc0.md#insn-00588bf4) · [`00588c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588bc0.md#insn-00588c04) · [`00588c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588bc0.md#insn-00588c10)
- 新版 `00588c34`（命令位置の公開資料なし） · `00588c44`（命令位置の公開資料なし） · `00588c50`（命令位置の公開資料なし）

~~~diff
- 00588bf4 ["INT_ADD", "register:40f0:8", ["const:588bf4:8", "const:4:8"]]
- 00588bf4 ["CALL", null, ["callee:0059763c:8"]]
+ 00588c34 ["INT_ADD", "register:40f0:8", ["const:588c34:8", "const:4:8"]]
+ 00588c34 ["CALL", null, ["callee:0059763c:8"]]
- 00588bf4 bytes 823a0094
+ 00588c34 bytes 823a0094
- 00588c04 ["INT_ADD", "register:40f0:8", ["const:588c04:8", "const:4:8"]]
- 00588c04 ["CALL", null, ["callee:00c57f60:8"]]
+ 00588c44 ["INT_ADD", "register:40f0:8", ["const:588c44:8", "const:4:8"]]
+ 00588c44 ["CALL", null, ["callee:00c57f60:8"]]
- 00588c04 bytes a33c1b94
+ 00588c44 bytes c73c1b94
- 00588c10 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00588c10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00588c10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00588c10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00588c50 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 00588c50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00588c50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00588c50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00588c10 bytes 08012591
+ 00588c50 bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-876679b268cae518648f95ee3bfee3bf"></a>

### [`00588df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588df8.md) → [`00588e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588e38.md) FUN_00588e38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0043af24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043af24.md) · 呼出先 3件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 1件 [`0043af64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043af64.md) · 呼出先 3件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md)

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
      "definition_site": "00588e4c",
      "incomplete_value": false,
      "site": "00588e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588e0c",
      "incomplete_value": false,
      "site": "00588e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00588e78",
      "incomplete_value": true,
      "site": "00588e78",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00588e38",
      "incomplete_value": true,
      "site": "00588e38",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00588e68",
      "incomplete_value": true,
      "site": "00588e78",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
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
      "definition_site": "00588e28",
      "incomplete_value": true,
      "site": "00588e38",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:350:8"
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
      "00588e4c",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "00588e68",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "00588e84",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00588e4c",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "00588e68",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "00588e84",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588df8.md#insn-00588e10) · [`00588e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588df8.md#insn-00588e38) · [`00588e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588df8.md#insn-00588e48)
- 新版 `00588e50`（命令位置の公開資料なし） · `00588e78`（命令位置の公開資料なし） · `00588e88`（命令位置の公開資料なし）

~~~diff
- 00588e10 ["INT_ADD", "register:40f0:8", ["const:588e10:8", "const:4:8"]]
- 00588e10 ["CALL", null, ["callee:00c5a3c0:8"]]
+ 00588e50 ["INT_ADD", "register:40f0:8", ["const:588e50:8", "const:4:8"]]
+ 00588e50 ["CALL", null, ["callee:00c5a3c0:8"]]
- 00588e10 bytes 38451b94
+ 00588e50 bytes 5c451b94
- 00588e38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588e38 ["INT_ADD", "register:40f0:8", ["const:588e38:8", "const:4:8"]]
- 00588e38 ["CALLIND", null, ["register:0:8"]]
+ 00588e78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588e78 ["INT_ADD", "register:40f0:8", ["const:588e78:8", "const:4:8"]]
+ 00588e78 ["CALLIND", null, ["register:0:8"]]
- 00588e38 bytes 00013fd6
+ 00588e78 bytes 00013fd6
- 00588e48 ["INT_ADD", "register:40f0:8", ["const:588e48:8", "const:4:8"]]
- 00588e48 ["CALL", null, ["callee:00c58210:8"]]
+ 00588e88 ["INT_ADD", "register:40f0:8", ["const:588e88:8", "const:4:8"]]
+ 00588e88 ["CALL", null, ["callee:00c58210:8"]]
- 00588e48 bytes be3c1b94
+ 00588e88 bytes e23c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d323a6dc4b5991cb4297dc3d9c05118a"></a>

### [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) → [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) FUN_00588eac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 138件 [`004976a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md) [`004978d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004978d0.md) [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) [`00571800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md) [`0057196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/0057196c.md) · 呼出先 2件 [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 138件 [`004976e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md) [`00497910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497910.md) [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00571840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md) [`005719ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005719ac.md) · 呼出先 2件 [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md)

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
      "definition_site": "00588ebc",
      "incomplete_value": false,
      "site": "00588ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588e7c",
      "incomplete_value": false,
      "site": "00588e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00588ee8",
      "incomplete_value": true,
      "site": "00588ee8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00588ea8",
      "incomplete_value": true,
      "site": "00588ea8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00588edc",
      "incomplete_value": true,
      "site": "00588ee8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
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
      "definition_site": "00588e9c",
      "incomplete_value": true,
      "site": "00588ea8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:350:8"
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
      "00588ebc",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "00588edc",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "00588ef4",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00588ebc",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "00588edc",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "00588ef4",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md#insn-00588e80) · [`00588ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md#insn-00588ea8) · [`00588eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md#insn-00588eb8)
- 新版 `00588ec0`（命令位置の公開資料なし） · `00588ee8`（命令位置の公開資料なし） · `00588ef8`（命令位置の公開資料なし）

~~~diff
- 00588e80 ["INT_ADD", "register:40f0:8", ["const:588e80:8", "const:4:8"]]
- 00588e80 ["CALL", null, ["callee:00c5a3c0:8"]]
+ 00588ec0 ["INT_ADD", "register:40f0:8", ["const:588ec0:8", "const:4:8"]]
+ 00588ec0 ["CALL", null, ["callee:00c5a3c0:8"]]
- 00588e80 bytes 1c451b94
+ 00588ec0 bytes 40451b94
- 00588ea8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588ea8 ["INT_ADD", "register:40f0:8", ["const:588ea8:8", "const:4:8"]]
- 00588ea8 ["CALLIND", null, ["register:0:8"]]
+ 00588ee8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588ee8 ["INT_ADD", "register:40f0:8", ["const:588ee8:8", "const:4:8"]]
+ 00588ee8 ["CALLIND", null, ["register:0:8"]]
- 00588ea8 bytes 00013fd6
+ 00588ee8 bytes 00013fd6
- 00588eb8 ["INT_ADD", "register:40f0:8", ["const:588eb8:8", "const:4:8"]]
- 00588eb8 ["CALL", null, ["callee:00c58210:8"]]
+ 00588ef8 ["INT_ADD", "register:40f0:8", ["const:588ef8:8", "const:4:8"]]
+ 00588ef8 ["CALL", null, ["callee:00c58210:8"]]
- 00588eb8 bytes a23c1b94
+ 00588ef8 bytes c63c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f5247ca1b96d41a1b1bb2e8e8324757"></a>

### [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) → [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) FUN_00588f0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`00588df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588df8.md) [`00589790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589790.md) [`005897f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005897f4.md) [`00589860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589860.md) [`0058a2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a2b4.md) · 呼出先 3件 [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 11件 [`00588e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588e38.md) [`005897d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005897d0.md) [`00589834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589834.md) [`005898a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005898a0.md) [`0058a2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2f4.md) · 呼出先 3件 [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md)

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
      "definition_site": "00588f38",
      "incomplete_value": false,
      "site": "00588f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00588ef8",
      "incomplete_value": false,
      "site": "00588efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00588f64",
      "incomplete_value": true,
      "site": "00588f64",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00588f24",
      "incomplete_value": true,
      "site": "00588f24",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00588f54",
      "incomplete_value": true,
      "site": "00588f64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
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
      "definition_site": "00588f14",
      "incomplete_value": true,
      "site": "00588f24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:350:8"
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
      "00588f38",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "00588f54",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "00588f70",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00588f38",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "00588f54",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "00588f70",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00588efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md#insn-00588efc) · [`00588f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md#insn-00588f24) · [`00588f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md#insn-00588f34)
- 新版 `00588f3c`（命令位置の公開資料なし） · `00588f64`（命令位置の公開資料なし） · `00588f74`（命令位置の公開資料なし）

~~~diff
- 00588efc ["INT_ADD", "register:40f0:8", ["const:588efc:8", "const:4:8"]]
- 00588efc ["CALL", null, ["callee:00c5a3c0:8"]]
+ 00588f3c ["INT_ADD", "register:40f0:8", ["const:588f3c:8", "const:4:8"]]
+ 00588f3c ["CALL", null, ["callee:00c5a3c0:8"]]
- 00588efc bytes fd441b94
+ 00588f3c bytes 21451b94
- 00588f24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00588f24 ["INT_ADD", "register:40f0:8", ["const:588f24:8", "const:4:8"]]
- 00588f24 ["CALLIND", null, ["register:0:8"]]
+ 00588f64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00588f64 ["INT_ADD", "register:40f0:8", ["const:588f64:8", "const:4:8"]]
+ 00588f64 ["CALLIND", null, ["register:0:8"]]
- 00588f24 bytes 00013fd6
+ 00588f64 bytes 00013fd6
- 00588f34 ["INT_ADD", "register:40f0:8", ["const:588f34:8", "const:4:8"]]
- 00588f34 ["CALL", null, ["callee:00c58210:8"]]
+ 00588f74 ["INT_ADD", "register:40f0:8", ["const:588f74:8", "const:4:8"]]
+ 00588f74 ["CALL", null, ["callee:00c58210:8"]]
- 00588f34 bytes 833c1b94
+ 00588f74 bytes a73c1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-558d108609e78f0ad42e3aade166c6a1"></a>

### [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) → [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) FUN_0058919c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 122件 [`004976a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md) [`004978d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004978d0.md) [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) [`00571800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md) [`0057196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/0057196c.md) · 呼出先 0件 
- 新版 呼出元 122件 [`004976e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md) [`00497910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497910.md) [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00571840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md) [`005719ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005719ac.md) · 呼出先 0件 

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
      "definition_site": "005891a0",
      "incomplete_value": false,
      "site": "005891a4",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589160",
      "incomplete_value": false,
      "site": "00589164",
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
            "const:358:8"
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
      "005891a0",
      "DATA",
      [
        "storage",
        "00ca6358",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005891a0",
      "DATA",
      [
        "storage",
        "00ca6458",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md#insn-00589160)
- 新版 `005891a0`（命令位置の公開資料なし）

~~~diff
- 00589160 ["COPY", "tmp:0:8", ["const:358:8"]]
- 00589160 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00589160 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00589160 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005891a0 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 005891a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005891a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005891a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00589160 bytes 00600d91
+ 005891a0 bytes 00601191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11f009d9b0a4c6e69c8e217f18ac51c4"></a>

### [`00589168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589168.md) → [`005891a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891a8.md) FUN_005891a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0058d170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d170.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0058d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d1b0.md) · 呼出先 0件 

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
      "definition_site": "005891b4",
      "incomplete_value": false,
      "site": "005891b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589174",
      "incomplete_value": false,
      "site": "00589174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "005891b4",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005891b4",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058916c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589168.md#insn-0058916c)
- 新版 `005891ac`（命令位置の公開資料なし）

~~~diff
- 0058916c ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 0058916c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058916c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058916c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005891ac ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 005891ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005891ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005891ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058916c bytes 08a13391
+ 005891ac bytes 08e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f2cc63f1caa876118ce4f238bcace30"></a>

### [`00589190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589190.md) → [`005891d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891d0.md) FUN_005891d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058a260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a260.md) · 呼出先 4件 [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0058a2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2a0.md) · 呼出先 4件 [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00589200",
      "incomplete_value": false,
      "site": "00589200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005891c0",
      "incomplete_value": false,
      "site": "005891c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "00589200",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00589200",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005891bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589190.md#insn-005891bc) · [`005891e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589190.md#insn-005891e4) · [`00589248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589190.md#insn-00589248)
- 新版 `005891fc`（命令位置の公開資料なし） · `00589224`（命令位置の公開資料なし） · `00589288`（命令位置の公開資料なし）

~~~diff
- 005891bc ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 005891bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005891bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005891bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005891fc ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 005891fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005891fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005891fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005891bc bytes 08a13391
+ 005891fc bytes 08e13691
- 005891e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005891e4 ["INT_ADD", "register:40f0:8", ["const:5891e4:8", "const:4:8"]]
- 005891e4 ["CALLIND", null, ["register:0:8"]]
+ 00589224 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589224 ["INT_ADD", "register:40f0:8", ["const:589224:8", "const:4:8"]]
+ 00589224 ["CALLIND", null, ["register:0:8"]]
- 005891e4 bytes 00013fd6
+ 00589224 bytes 00013fd6
- 00589248 ["INT_ADD", "register:40f0:8", ["const:589248:8", "const:4:8"]]
- 00589248 ["CALL", null, ["callee:00589360:8"]]
+ 00589288 ["INT_ADD", "register:40f0:8", ["const:589288:8", "const:4:8"]]
+ 00589288 ["CALL", null, ["callee:00589360:8"]]
- 00589248 bytes 36000094
+ 00589288 bytes 36000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-835df0a75efcf6e4e48fd0aacdd863bb"></a>

### [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) → [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) FUN_00589360

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 130件 [`004976a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004976a4.md) [`004978d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004978d0.md) [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) [`00571800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571800.md) [`0057196c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/0057196c.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0058a9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a9ac.md) [`0058aad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058aad4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 130件 [`004976e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/004976e4.md) [`00497910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497910.md) [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00571840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571840.md) [`005719ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/005719ac.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0058a9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a9ec.md) [`0058ab14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ab14.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00589450",
      "incomplete_value": false,
      "site": "00589454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589410",
      "incomplete_value": false,
      "site": "00589414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00589474",
      "incomplete_value": false,
      "site": "00589478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589434",
      "incomplete_value": false,
      "site": "00589438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "005894a0",
      "incomplete_value": true,
      "site": "005894a0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00589460",
      "incomplete_value": true,
      "site": "00589460",
      "value": [
        "LOAD",
        "8",
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
      "00589450",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "00589474",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "0058948c",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00589450",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "00589474",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "0058948c",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md#insn-00589414) · [`00589438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md#insn-00589438) · [`00589460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md#insn-00589460)
- 新版 `00589454`（命令位置の公開資料なし） · `00589478`（命令位置の公開資料なし） · `005894a0`（命令位置の公開資料なし）

~~~diff
- 00589414 ["INT_ADD", "register:40f0:8", ["const:589414:8", "const:4:8"]]
- 00589414 ["CALL", null, ["callee:00c5a3c0:8"]]
+ 00589454 ["INT_ADD", "register:40f0:8", ["const:589454:8", "const:4:8"]]
+ 00589454 ["CALL", null, ["callee:00c5a3c0:8"]]
- 00589414 bytes b7431b94
+ 00589454 bytes db431b94
- 00589438 ["INT_ADD", "register:40f0:8", ["const:589438:8", "const:4:8"]]
- 00589438 ["CALL", null, ["callee:00c5a3c0:8"]]
+ 00589478 ["INT_ADD", "register:40f0:8", ["const:589478:8", "const:4:8"]]
+ 00589478 ["CALL", null, ["callee:00c5a3c0:8"]]
- 00589438 bytes ae431b94
+ 00589478 bytes d2431b94
- 00589460 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589460 ["INT_ADD", "register:40f0:8", ["const:589460:8", "const:4:8"]]
- 00589460 ["CALLIND", null, ["register:0:8"]]
+ 005894a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005894a0 ["INT_ADD", "register:40f0:8", ["const:5894a0:8", "const:4:8"]]
+ 005894a0 ["CALLIND", null, ["register:0:8"]]
- 00589460 bytes 00013fd6
+ 005894a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bafbf680275ecc24ad5c600a3154848"></a>

### [`00589790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589790.md) → [`005897d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005897d0.md) FUN_005897d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0057e4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e4dc.md) [`0057e834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057e/0057e834.md) [`00581fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00581/00581fbc.md) · 呼出先 1件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md)
- 新版 呼出元 3件 [`0057e51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e51c.md) [`0057e874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057e/0057e874.md) [`00581ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00581/00581ffc.md) · 呼出先 1件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md)

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
      "definition_site": "005897e8",
      "incomplete_value": false,
      "site": "005897e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005897a8",
      "incomplete_value": false,
      "site": "005897a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "005897e8",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005897e8",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005897a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589790.md#insn-005897a0) · [`005897a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589790.md#insn-005897a4) · [`005897cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589790.md#insn-005897cc)
- 新版 `005897e0`（命令位置の公開資料なし） · `0058980c`（命令位置の公開資料なし）

~~~diff
- 005897a0 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 005897a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005897a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005897a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005897e0 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 005897e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005897e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005897e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005897a0 bytes 08a13391
+ 005897e0 bytes 08e13691
- 005897a4 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 005897a4 bytes f40300aa
- 005897cc ["INT_ADD", "register:40f0:8", ["const:5897cc:8", "const:4:8"]]
- 005897cc ["CALL", null, ["callee:00588f0c:8"]]
+ 0058980c ["INT_ADD", "register:40f0:8", ["const:58980c:8", "const:4:8"]]
+ 0058980c ["CALL", null, ["callee:00588f0c:8"]]
- 005897cc bytes c0fdff97
+ 0058980c bytes c0fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-323428579284e4bf5af2833d3d5d2918"></a>

### [`005897f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005897f4.md) → [`00589834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589834.md) FUN_00589834

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00589848",
      "incomplete_value": false,
      "site": "0058984c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589808",
      "incomplete_value": false,
      "site": "0058980c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "0058984c",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058984c",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005897f4.md#insn-00589808) · [`0058981c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005897f4.md#insn-0058981c) · [`00589828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005897f4.md#insn-00589828)
- 新版 `00589848`（命令位置の公開資料なし） · `0058985c`（命令位置の公開資料なし） · `00589868`（命令位置の公開資料なし）

~~~diff
- 00589808 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 00589808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00589808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00589808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00589848 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00589848 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00589848 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00589848 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00589808 bytes 08a13391
+ 00589848 bytes 08e13691
- 0058981c ["INT_ADD", "register:40f0:8", ["const:58981c:8", "const:4:8"]]
- 0058981c ["CALL", null, ["callee:00588f0c:8"]]
+ 0058985c ["INT_ADD", "register:40f0:8", ["const:58985c:8", "const:4:8"]]
+ 0058985c ["CALL", null, ["callee:00588f0c:8"]]
- 0058981c bytes acfdff97
+ 0058985c bytes acfdff97
- 00589828 ["INT_ADD", "register:40f0:8", ["const:589828:8", "const:4:8"]]
- 00589828 ["CALL", null, ["callee:0058a98c:8"]]
+ 00589868 ["INT_ADD", "register:40f0:8", ["const:589868:8", "const:4:8"]]
+ 00589868 ["CALL", null, ["callee:0058a98c:8"]]
- 00589828 bytes 49040094
+ 00589868 bytes 49040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2384fb4ed1157b141781371ceace8559"></a>

### [`005898d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005898d0.md) → [`00589910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589910.md) FUN_00589910

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 55件 [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) [`00571af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md) [`00571e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571e18.md) [`005720f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md) [`005722ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md) · 呼出先 0件 
- 新版 呼出元 55件 [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00571b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571b34.md) [`00571e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571e58.md) [`00572138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572138.md) [`005722ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005722ec.md) · 呼出先 0件 

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
      "definition_site": "00589944",
      "incomplete_value": false,
      "site": "00589944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589904",
      "incomplete_value": false,
      "site": "00589904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "00589944",
      "DATA",
      [
        "storage",
        "00c6cd08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00589944",
      "DATA",
      [
        "storage",
        "00c6cdd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005898d0.md#insn-00589900) · [`00589924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005898d0.md#insn-00589924)
- 新版 `00589940`（命令位置の公開資料なし） · `00589964`（命令位置の公開資料なし）

~~~diff
- 00589900 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00589900 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00589900 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00589900 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00589940 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00589940 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00589940 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00589940 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00589900 bytes 29213491
+ 00589940 bytes 29613791
- 00589924 ["COPY", "register:0:8", ["register:4048:8"]]
- 00589924 ["INT_ADD", "register:40f0:8", ["const:589924:8", "const:4:8"]]
- 00589924 ["CALLIND", null, ["register:0:8"]]
+ 00589964 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00589964 ["INT_ADD", "register:40f0:8", ["const:589964:8", "const:4:8"]]
+ 00589964 ["CALLIND", null, ["register:0:8"]]
- 00589924 bytes 20013fd6
+ 00589964 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9240d57a99022e5ea328ad452da2625e"></a>

### [`00589be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md) → [`00589c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589c28.md) FUN_00589c28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`00580888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580888.md) [`005821d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md) [`00582360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582360.md) [`005824f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005824f4.md) [`00582670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/00582670.md) · 呼出先 0件 
- 新版 呼出元 7件 [`005808c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005808c8.md) [`00582218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582218.md) [`005823a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005823a0.md) [`00582534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582534.md) [`005826b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/005826b0.md) · 呼出先 0件 

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
      "definition_site": "00589c48",
      "incomplete_value": false,
      "site": "00589c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589c08",
      "incomplete_value": false,
      "site": "00589c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "00589c48",
      "DATA",
      [
        "storage",
        "00c6cd28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00589c48",
      "DATA",
      [
        "storage",
        "00c6cdf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md#insn-00589c04) · [`00589c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md#insn-00589c28) · [`00589c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589be8.md#insn-00589c44)
- 新版 `00589c44`（命令位置の公開資料なし） · `00589c68`（命令位置の公開資料なし） · `00589c84`（命令位置の公開資料なし）

~~~diff
- 00589c04 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00589c04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00589c04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00589c04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00589c44 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 00589c44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00589c44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00589c44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00589c04 bytes 08a13491
+ 00589c44 bytes 08e13791
- 00589c28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589c28 ["INT_ADD", "register:40f0:8", ["const:589c28:8", "const:4:8"]]
- 00589c28 ["CALLIND", null, ["register:0:8"]]
+ 00589c68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589c68 ["INT_ADD", "register:40f0:8", ["const:589c68:8", "const:4:8"]]
+ 00589c68 ["CALLIND", null, ["register:0:8"]]
- 00589c28 bytes 00013fd6
+ 00589c68 bytes 00013fd6
- 00589c44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589c44 ["INT_ADD", "register:40f0:8", ["const:589c44:8", "const:4:8"]]
- 00589c44 ["CALLIND", null, ["register:0:8"]]
+ 00589c84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589c84 ["INT_ADD", "register:40f0:8", ["const:589c84:8", "const:4:8"]]
+ 00589c84 ["CALLIND", null, ["register:0:8"]]
- 00589c44 bytes 00013fd6
+ 00589c84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb0cc7c1e317e3fa31d5647b68fe865e"></a>

### [`00589c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589c84.md) → [`00589cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589cc4.md) FUN_00589cc4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00580098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580098.md) · 呼出先 0件 
- 新版 呼出元 1件 [`005800d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/005800d8.md) · 呼出先 0件 

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
      "definition_site": "00589cd8",
      "incomplete_value": false,
      "site": "00589ce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589c98",
      "incomplete_value": false,
      "site": "00589ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "00589ce0",
      "DATA",
      [
        "storage",
        "00c6cd28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00589ce0",
      "DATA",
      [
        "storage",
        "00c6cdf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589c84.md#insn-00589c98) · [`00589cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589c84.md#insn-00589cb4)
- 新版 `00589cd8`（命令位置の公開資料なし） · `00589cf4`（命令位置の公開資料なし）

~~~diff
- 00589c98 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00589c98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00589c98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00589c98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00589cd8 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 00589cd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00589cd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00589cd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00589c98 bytes 29a13491
+ 00589cd8 bytes 29e13791
- 00589cb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589cb4 ["INT_ADD", "register:40f0:8", ["const:589cb4:8", "const:4:8"]]
- 00589cb4 ["CALLIND", null, ["register:0:8"]]
+ 00589cf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589cf4 ["INT_ADD", "register:40f0:8", ["const:589cf4:8", "const:4:8"]]
+ 00589cf4 ["CALLIND", null, ["register:0:8"]]
- 00589cb4 bytes 00013fd6
+ 00589cf4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf32ae2d90804f5e2ed43629a3b5fef6"></a>

### [`00589cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589cc8.md) → [`00589d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589d08.md) FUN_00589d08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005821d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00582/005821d8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00582218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00582/00582218.md) · 呼出先 0件 

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
      "definition_site": "00589d24",
      "incomplete_value": false,
      "site": "00589d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00589ce4",
      "incomplete_value": false,
      "site": "00589ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "00589d24",
      "DATA",
      [
        "storage",
        "00c6cd28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00589d24",
      "DATA",
      [
        "storage",
        "00c6cdf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00589cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589cc8.md#insn-00589cdc) · [`00589d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589cc8.md#insn-00589d14) · [`00589d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589cc8.md#insn-00589d30)
- 新版 `00589d1c`（命令位置の公開資料なし） · `00589d54`（命令位置の公開資料なし） · `00589d70`（命令位置の公開資料なし）

~~~diff
- 00589cdc ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00589cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00589cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00589cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00589d1c ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 00589d1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00589d1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00589d1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00589cdc bytes 08a13491
+ 00589d1c bytes 08e13791
- 00589d14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589d14 ["INT_ADD", "register:40f0:8", ["const:589d14:8", "const:4:8"]]
- 00589d14 ["CALLIND", null, ["register:0:8"]]
+ 00589d54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589d54 ["INT_ADD", "register:40f0:8", ["const:589d54:8", "const:4:8"]]
+ 00589d54 ["CALLIND", null, ["register:0:8"]]
- 00589d14 bytes 00013fd6
+ 00589d54 bytes 00013fd6
- 00589d30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00589d30 ["INT_ADD", "register:40f0:8", ["const:589d30:8", "const:4:8"]]
- 00589d30 ["CALLIND", null, ["register:0:8"]]
+ 00589d70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00589d70 ["INT_ADD", "register:40f0:8", ["const:589d70:8", "const:4:8"]]
+ 00589d70 ["CALLIND", null, ["register:0:8"]]
- 00589d30 bytes 00013fd6
+ 00589d70 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f9afb4f15632716ca5dd5a706721619"></a>

### [`0058a048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a048.md) → [`0058a088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a088.md) FUN_0058a088

採用 · 移動量 `+0x40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00589f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589f08.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00589f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589f48.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "site": "0058a098",
      "value": [
        "leaf",
        "ram:589f48:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0058a058",
      "value": [
        "leaf",
        "ram:589f08:8"
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
      "0058a098",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00589f08"
      ]
    ]
  ],
  "added": [
    [
      "0058a098",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00589f48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a048.md#insn-0058a058)
- 新版 `0058a098`（命令位置の公開資料なし）

~~~diff
- 0058a058 ["INT_ADD", "register:40f0:8", ["const:58a058:8", "const:4:8"]]
- 0058a058 ["CALL", null, ["ram:589f08:8"]]
+ 0058a098 ["INT_ADD", "register:40f0:8", ["const:58a098:8", "const:4:8"]]
+ 0058a098 ["CALL", null, ["ram:589f48:8"]]
- 0058a058 bytes acffff97
+ 0058a098 bytes acffff97
~~~


<a id="compare-208049e659fa0b248bdc4c1a841a2656"></a>

### [`0058a06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a06c.md) → [`0058a0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a0ac.md) FUN_0058a0ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md)

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
      "definition_site": "0058a0c0",
      "incomplete_value": false,
      "site": "0058a0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a080",
      "incomplete_value": false,
      "site": "0058a084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "0058a0ec",
      "incomplete_value": true,
      "site": "0058a0ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058a0ac",
      "incomplete_value": true,
      "site": "0058a0ac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058a0e0",
      "incomplete_value": true,
      "site": "0058a0ec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
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
      "definition_site": "0058a0a0",
      "incomplete_value": true,
      "site": "0058a0ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:350:8"
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
      "0058a0c0",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "0058a0e0",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a0f8",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058a0c0",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "0058a0e0",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a0f8",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a06c.md#insn-0058a084) · [`0058a0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a06c.md#insn-0058a0ac) · [`0058a0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a06c.md#insn-0058a0bc)
- 新版 `0058a0c4`（命令位置の公開資料なし） · `0058a0ec`（命令位置の公開資料なし） · `0058a0fc`（命令位置の公開資料なし）

~~~diff
- 0058a084 ["INT_ADD", "register:40f0:8", ["const:58a084:8", "const:4:8"]]
- 0058a084 ["CALL", null, ["callee:00c5a3c0:8"]]
+ 0058a0c4 ["INT_ADD", "register:40f0:8", ["const:58a0c4:8", "const:4:8"]]
+ 0058a0c4 ["CALL", null, ["callee:00c5a3c0:8"]]
- 0058a084 bytes 9b401b94
+ 0058a0c4 bytes bf401b94
- 0058a0ac ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a0ac ["INT_ADD", "register:40f0:8", ["const:58a0ac:8", "const:4:8"]]
- 0058a0ac ["CALLIND", null, ["register:0:8"]]
+ 0058a0ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a0ec ["INT_ADD", "register:40f0:8", ["const:58a0ec:8", "const:4:8"]]
+ 0058a0ec ["CALLIND", null, ["register:0:8"]]
- 0058a0ac bytes 00013fd6
+ 0058a0ec bytes 00013fd6
- 0058a0bc ["INT_ADD", "register:40f0:8", ["const:58a0bc:8", "const:4:8"]]
- 0058a0bc ["CALL", null, ["callee:00c58210:8"]]
+ 0058a0fc ["INT_ADD", "register:40f0:8", ["const:58a0fc:8", "const:4:8"]]
+ 0058a0fc ["CALL", null, ["callee:00c58210:8"]]
- 0058a0bc bytes 21381b94
+ 0058a0fc bytes 45381b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abbc1f13ab8a1aef5722345488cf38a3"></a>

### [`0058a0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a0dc.md) → [`0058a11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a11c.md) FUN_0058a11c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md)

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
      "definition_site": "0058a130",
      "incomplete_value": false,
      "site": "0058a134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a0f0",
      "incomplete_value": false,
      "site": "0058a0f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca3000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "0058a15c",
      "incomplete_value": true,
      "site": "0058a15c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058a11c",
      "incomplete_value": true,
      "site": "0058a11c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058a150",
      "incomplete_value": true,
      "site": "0058a15c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
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
      "definition_site": "0058a110",
      "incomplete_value": true,
      "site": "0058a11c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:350:8"
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
      "0058a130",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "0058a150",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a168",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058a130",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "0058a150",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a168",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a0dc.md#insn-0058a0f4) · [`0058a11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a0dc.md#insn-0058a11c) · [`0058a12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a0dc.md#insn-0058a12c)
- 新版 `0058a134`（命令位置の公開資料なし） · `0058a15c`（命令位置の公開資料なし） · `0058a16c`（命令位置の公開資料なし）

~~~diff
- 0058a0f4 ["INT_ADD", "register:40f0:8", ["const:58a0f4:8", "const:4:8"]]
- 0058a0f4 ["CALL", null, ["callee:00c5a3c0:8"]]
+ 0058a134 ["INT_ADD", "register:40f0:8", ["const:58a134:8", "const:4:8"]]
+ 0058a134 ["CALL", null, ["callee:00c5a3c0:8"]]
- 0058a0f4 bytes 7f401b94
+ 0058a134 bytes a3401b94
- 0058a11c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a11c ["INT_ADD", "register:40f0:8", ["const:58a11c:8", "const:4:8"]]
- 0058a11c ["CALLIND", null, ["register:0:8"]]
+ 0058a15c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a15c ["INT_ADD", "register:40f0:8", ["const:58a15c:8", "const:4:8"]]
+ 0058a15c ["CALLIND", null, ["register:0:8"]]
- 0058a11c bytes 00013fd6
+ 0058a15c bytes 00013fd6
- 0058a12c ["INT_ADD", "register:40f0:8", ["const:58a12c:8", "const:4:8"]]
- 0058a12c ["CALL", null, ["callee:00c58210:8"]]
+ 0058a16c ["INT_ADD", "register:40f0:8", ["const:58a16c:8", "const:4:8"]]
+ 0058a16c ["CALL", null, ["callee:00c58210:8"]]
- 0058a12c bytes 05381b94
+ 0058a16c bytes 29381b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e85d1cc6681a1c84489180d65194167b"></a>

### [`0058a14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a14c.md) → [`0058a18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a18c.md) FUN_0058a18c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md)

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
      "definition_site": "0058a1d4",
      "incomplete_value": true,
      "site": "0058a1d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058a194",
      "incomplete_value": true,
      "site": "0058a194",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058a1c4",
      "incomplete_value": true,
      "site": "0058a1d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
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
      "definition_site": "0058a184",
      "incomplete_value": true,
      "site": "0058a194",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:350:8"
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
      "definition_site": "0058a1e0",
      "incomplete_value": true,
      "site": "0058a1e4",
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
      "definition_site": "0058a1a0",
      "incomplete_value": true,
      "site": "0058a1a4",
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
      "0058a1a4",
      "PARAM",
      [
        "storage",
        "00ca3e00",
        null,
        null
      ]
    ],
    [
      "0058a1c4",
      "READ",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a1e0",
      "READ",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058a1a4",
      "PARAM",
      [
        "storage",
        "00ca3ed0",
        null,
        null
      ]
    ],
    [
      "0058a1c4",
      "READ",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a1e0",
      "READ",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a14c.md#insn-0058a164) · [`0058a194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a14c.md#insn-0058a194) · [`0058a1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a14c.md#insn-0058a1a4)
- 新版 `0058a1a4`（命令位置の公開資料なし） · `0058a1d4`（命令位置の公開資料なし） · `0058a1e4`（命令位置の公開資料なし）

~~~diff
- 0058a164 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 0058a164 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0058a164 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0058a164 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0058a1a4 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 0058a1a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0058a1a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0058a1a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0058a164 bytes 00003891
+ 0058a1a4 bytes 00403b91
- 0058a194 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a194 ["INT_ADD", "register:40f0:8", ["const:58a194:8", "const:4:8"]]
- 0058a194 ["CALLIND", null, ["register:0:8"]]
+ 0058a1d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a1d4 ["INT_ADD", "register:40f0:8", ["const:58a1d4:8", "const:4:8"]]
+ 0058a1d4 ["CALLIND", null, ["register:0:8"]]
- 0058a194 bytes 00013fd6
+ 0058a1d4 bytes 00013fd6
- 0058a1a4 ["INT_ADD", "register:40f0:8", ["const:58a1a4:8", "const:4:8"]]
- 0058a1a4 ["CALL", null, ["callee:00c58210:8"]]
+ 0058a1e4 ["INT_ADD", "register:40f0:8", ["const:58a1e4:8", "const:4:8"]]
+ 0058a1e4 ["CALL", null, ["callee:00c58210:8"]]
- 0058a1a4 bytes e7371b94
+ 0058a1e4 bytes 0b381b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2f6fa3ae9749e42f02dcbf3a80cb1ed"></a>

### [`0058a260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a260.md) → [`0058a2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2a0.md) FUN_0058a2a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 1件 [`00589190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589190.md)
- 新版 呼出元 2件 [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) · 呼出先 1件 [`005891d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891d0.md)

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
      "definition_site": "0058a2e0",
      "incomplete_value": false,
      "site": "0058a2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a2a0",
      "incomplete_value": false,
      "site": "0058a2a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d60:8"
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
      "definition_site": "0058a2bc",
      "incomplete_value": false,
      "site": "0058a2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:78a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a27c",
      "incomplete_value": false,
      "site": "0058a288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:7e6:8"
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
      "0058a2bc",
      "PARAM",
      [
        "storage",
        "002a67e6",
        null,
        "string"
      ]
    ],
    [
      "0058a2e4",
      "DATA",
      [
        "storage",
        "00c6cd60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a2bc",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "0058a2e4",
      "DATA",
      [
        "storage",
        "00c6ce30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a260.md#insn-0058a288) · [`0058a27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a260.md#insn-0058a27c) · [`0058a298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a260.md#insn-0058a298)
- 新版 `0058a2c8`（命令位置の公開資料なし） · `0058a2bc`（命令位置の公開資料なし） · `0058a2d8`（命令位置の公開資料なし）

~~~diff
- 0058a288 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a288 ["INT_ADD", "register:40f0:8", ["const:58a288:8", "const:4:8"]]
- 0058a288 ["CALLIND", null, ["register:0:8"]]
+ 0058a2c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a2c8 ["INT_ADD", "register:40f0:8", ["const:58a2c8:8", "const:4:8"]]
+ 0058a2c8 ["CALLIND", null, ["register:0:8"]]
- 0058a288 bytes 00013fd6
+ 0058a2c8 bytes 00013fd6
- 0058a27c ["COPY", "tmp:0:8", ["const:7e6:8"]]
- 0058a27c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0058a27c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0058a27c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058a2bc ["COPY", "tmp:0:8", ["const:78a:8"]]
+ 0058a2bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058a2bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058a2bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0058a27c bytes 21981f91
+ 0058a2bc bytes 21281e91
- 0058a298 ["INT_ADD", "register:40f0:8", ["const:58a298:8", "const:4:8"]]
- 0058a298 ["CALL", null, ["callee:005891d0:8"]]
+ 0058a2d8 ["INT_ADD", "register:40f0:8", ["const:58a2d8:8", "const:4:8"]]
+ 0058a2d8 ["CALL", null, ["callee:005891d0:8"]]
- 0058a298 bytes befbff97
+ 0058a2d8 bytes befbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bbbc229a2cbcbd45b0e944ea9307a2a"></a>

### [`0058a2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a2b4.md) → [`0058a2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a2f4.md) FUN_0058a2f4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 7件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) · 呼出先 7件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.71% / 新版 89.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a35c",
      "incomplete_value": true,
      "site": "0058a364",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a31c",
      "incomplete_value": true,
      "site": "0058a324",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058a358",
      "incomplete_value": true,
      "site": "0058a368",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:a8c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a318",
      "incomplete_value": true,
      "site": "0058a328",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
      "definition_site": "0058a358",
      "incomplete_value": true,
      "site": "0058a368",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058a318",
      "incomplete_value": true,
      "site": "0058a328",
      "value": [
        "LOAD",
        "16",
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
      "0058a358",
      "READ",
      [
        "storage",
        "002bdae0",
        null,
        "string"
      ]
    ],
    [
      "0058a358",
      "READ",
      [
        "storage",
        "002bdaf0",
        null,
        "string"
      ]
    ],
    [
      "0058a35c",
      "READ",
      [
        "storage",
        "002c2ba0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058a358",
      "READ",
      [
        "storage",
        "002bda8c",
        null,
        "string"
      ]
    ],
    [
      "0058a358",
      "READ",
      [
        "storage",
        "002bda9c",
        null,
        "string"
      ]
    ],
    [
      "0058a35c",
      "READ",
      [
        "storage",
        "002c2be0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a2b4.md#insn-0058a364) · [`0058a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a2b4.md#insn-0058a308) · [`0058a310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a2b4.md#insn-0058a310)
- 新版 `0058a3a4`（命令位置の公開資料なし） · `0058a348`（命令位置の公開資料なし） · `0058a350`（命令位置の公開資料なし）

~~~diff
- 0058a364 ["INT_ADD", "register:40f0:8", ["const:58a364:8", "const:4:8"]]
- 0058a364 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058a3a4 ["INT_ADD", "register:40f0:8", ["const:58a3a4:8", "const:4:8"]]
+ 0058a3a4 ["CALL", null, ["callee:00c57f80:8"]]
- 0058a364 bytes d3361b94
+ 0058a3a4 bytes f7361b94
- 0058a308 ["INT_ADD", "register:40f0:8", ["const:58a308:8", "const:4:8"]]
- 0058a308 ["CALL", null, ["callee:00c57f60:8"]]
+ 0058a348 ["INT_ADD", "register:40f0:8", ["const:58a348:8", "const:4:8"]]
+ 0058a348 ["CALL", null, ["callee:00c57f60:8"]]
- 0058a308 bytes e2361b94
+ 0058a348 bytes 06371b94
- 0058a310 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0058a310 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a310 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a310 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a350 ["COPY", "tmp:0:8", ["const:a8c:8"]]
+ 0058a350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a310 bytes 08812b91
+ 0058a350 bytes 08312a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48b3c7a541755e240f5271c8616e061e"></a>

### [`0058a544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a544.md) → [`0058a584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a584.md) FUN_0058a584

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00572460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572460.md) [`00578ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00578/00578ebc.md) [`0057b164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057b164.md) [`005838ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00583/005838ac.md) [`005841ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00584/005841ac.md) · 呼出先 1件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md)
- 新版 呼出元 5件 [`005724a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005724a0.md) [`00578efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00578/00578efc.md) [`0057b1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057b1a4.md) [`005838ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00583/005838ec.md) [`005841ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00584/005841ec.md) · 呼出先 1件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md)

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
      "definition_site": "0058a5fc",
      "incomplete_value": false,
      "site": "0058a5fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a5bc",
      "incomplete_value": false,
      "site": "0058a5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "definition_site": "0058a634",
      "incomplete_value": false,
      "site": "0058a638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a5f4",
      "incomplete_value": false,
      "site": "0058a5f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "definition_site": "0058a5a4",
      "incomplete_value": true,
      "site": "0058a5b4",
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
            "const:a44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a564",
      "incomplete_value": true,
      "site": "0058a574",
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
            "const:aa0:8"
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
      "0058a5a4",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "0058a5c4",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "0058a5fc",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a5a4",
      "PARAM",
      [
        "storage",
        "002aea44",
        null,
        "string"
      ]
    ],
    [
      "0058a5c4",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "0058a5fc",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a544.md#insn-0058a574) · [`0058a590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a544.md#insn-0058a590) · [`0058a5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a544.md#insn-0058a5b4)
- 新版 `0058a5b4`（命令位置の公開資料なし） · `0058a5d0`（命令位置の公開資料なし） · `0058a5f4`（命令位置の公開資料なし）

~~~diff
- 0058a574 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a574 ["INT_ADD", "register:40f0:8", ["const:58a574:8", "const:4:8"]]
- 0058a574 ["CALLIND", null, ["register:0:8"]]
+ 0058a5b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a5b4 ["INT_ADD", "register:40f0:8", ["const:58a5b4:8", "const:4:8"]]
+ 0058a5b4 ["CALLIND", null, ["register:0:8"]]
- 0058a574 bytes 00013fd6
+ 0058a5b4 bytes 00013fd6
- 0058a590 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a590 ["INT_ADD", "register:40f0:8", ["const:58a590:8", "const:4:8"]]
- 0058a590 ["CALLIND", null, ["register:0:8"]]
+ 0058a5d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058a5d0 ["INT_ADD", "register:40f0:8", ["const:58a5d0:8", "const:4:8"]]
+ 0058a5d0 ["CALLIND", null, ["register:0:8"]]
- 0058a590 bytes 00013fd6
+ 0058a5d0 bytes 00013fd6
- 0058a5b4 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 0058a5b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a5b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a5b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a5f4 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 0058a5f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a5f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a5f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a5b4 bytes 08a13391
+ 0058a5f4 bytes 08e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff989861fef000b8a79650eab2938f66"></a>

### [`0058a624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a624.md) → [`0058a664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a664.md) FUN_0058a664

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00572c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/00572c68.md) [`00573e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00573/00573e80.md) [`005740e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/005740e0.md) · 呼出先 1件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md)
- 新版 呼出元 3件 [`00572ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572ca8.md) [`00573ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00573/00573ec0.md) [`00574120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574120.md) · 呼出先 1件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md)

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
      "definition_site": "0058a68c",
      "incomplete_value": true,
      "site": "0058a68c",
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
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a64c",
      "incomplete_value": true,
      "site": "0058a64c",
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
            "const:ce8:8"
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
      "definition_site": "0058a6b4",
      "incomplete_value": false,
      "site": "0058a6b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a674",
      "incomplete_value": false,
      "site": "0058a678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "0058a68c",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ],
    [
      "0058a6b8",
      "DATA",
      [
        "storage",
        "00c6cd80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058a68c",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ],
    [
      "0058a6b8",
      "DATA",
      [
        "storage",
        "00c6ce50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a624.md#insn-0058a640) · [`0058a644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a624.md#insn-0058a644) · [`0058a648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a624.md#insn-0058a648)
- 新版 `0058a680`（命令位置の公開資料なし）

~~~diff
- 0058a640 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 0058a640 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058a640 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058a640 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058a680 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 0058a680 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058a680 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058a680 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058a640 bytes 29a13391
+ 0058a680 bytes 29e13691
- 0058a644 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 0058a644 bytes f50300aa
- 0058a648 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0058a648 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1f744d75b77076779cb538af5a48bf5"></a>

### [`0058a7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a7f0.md) → [`0058a830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a830.md) JNI_OnLoad

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058910c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058910c.md) [`00c5a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a300.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058914c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058914c.md) [`00c5a3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058a844",
      "incomplete_value": false,
      "site": "0058a844",
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
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a804",
      "incomplete_value": false,
      "site": "0058a804",
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
            "const:350:8"
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
      "definition_site": "0058a84c",
      "incomplete_value": false,
      "site": "0058a850",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a80c",
      "incomplete_value": false,
      "site": "0058a810",
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
            "const:390:8"
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
      "definition_site": "0058a840",
      "incomplete_value": false,
      "site": "0058a850",
      "value": [
        "leaf",
        "const:58914c:8"
      ]
    },
    "old": {
      "definition_site": "0058a800",
      "incomplete_value": false,
      "site": "0058a810",
      "value": [
        "leaf",
        "const:58910c:8"
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
      "0058a840",
      "PARAM",
      [
        "storage",
        "0058910c",
        null,
        null
      ]
    ],
    [
      "0058a844",
      "WRITE",
      [
        "storage",
        "00ca6350",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a84c",
      "PARAM",
      [
        "storage",
        "00ca6390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058a840",
      "PARAM",
      [
        "storage",
        "0058914c",
        null,
        null
      ]
    ],
    [
      "0058a844",
      "WRITE",
      [
        "storage",
        "00ca6450",
        null,
        "undefined8"
      ]
    ],
    [
      "0058a84c",
      "PARAM",
      [
        "storage",
        "00ca6490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a7f0.md#insn-0058a804) · [`0058a810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a7f0.md#insn-0058a810) · [`0058a800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a7f0.md#insn-0058a800)
- 新版 `0058a844`（命令位置の公開資料なし） · `0058a850`（命令位置の公開資料なし） · `0058a840`（命令位置の公開資料なし）

~~~diff
- 0058a804 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
- 0058a804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 0058a844 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 0058a844 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0058a804 bytes 00a901f9
+ 0058a844 bytes 002902f9
- 0058a810 ["INT_ADD", "register:40f0:8", ["const:58a810:8", "const:4:8"]]
- 0058a810 ["CALL", null, ["callee:00c5a3d0:8"]]
+ 0058a850 ["INT_ADD", "register:40f0:8", ["const:58a850:8", "const:4:8"]]
+ 0058a850 ["CALL", null, ["callee:00c5a3d0:8"]]
- 0058a810 bytes bc3e1b94
+ 0058a850 bytes e03e1b94
- 0058a800 ["COPY", "register:4008:8", ["const:58910c:8"]]
+ 0058a840 ["COPY", "register:4008:8", ["const:58914c:8"]]
- 0058a800 bytes 6148ff10
+ 0058a840 bytes 6148ff10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc9c4a873bab234ceb922d5af867d7a5"></a>

### [`0058a824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a824.md) → [`0058a864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a864.md) FUN_0058a864

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0058a878",
      "incomplete_value": false,
      "site": "0058a87c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a838",
      "incomplete_value": false,
      "site": "0058a83c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "0058a87c",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a87c",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a824.md#insn-0058a838) · [`0058a84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a824.md#insn-0058a84c) · [`0058a858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a824.md#insn-0058a858)
- 新版 `0058a878`（命令位置の公開資料なし） · `0058a88c`（命令位置の公開資料なし） · `0058a898`（命令位置の公開資料なし）

~~~diff
- 0058a838 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 0058a838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a878 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 0058a878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a838 bytes 08a13391
+ 0058a878 bytes 08e13691
- 0058a84c ["INT_ADD", "register:40f0:8", ["const:58a84c:8", "const:4:8"]]
- 0058a84c ["CALL", null, ["callee:00588f0c:8"]]
+ 0058a88c ["INT_ADD", "register:40f0:8", ["const:58a88c:8", "const:4:8"]]
+ 0058a88c ["CALL", null, ["callee:00588f0c:8"]]
- 0058a84c bytes a0f9ff97
+ 0058a88c bytes a0f9ff97
- 0058a858 ["INT_ADD", "register:40f0:8", ["const:58a858:8", "const:4:8"]]
- 0058a858 ["CALL", null, ["callee:0058a98c:8"]]
+ 0058a898 ["INT_ADD", "register:40f0:8", ["const:58a898:8", "const:4:8"]]
+ 0058a898 ["CALL", null, ["callee:0058a98c:8"]]
- 0058a858 bytes 3d000094
+ 0058a898 bytes 3d000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75ef0585f765270e2fd047e59d930c0d"></a>

### [`0058a870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a870.md) → [`0058a8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8b0.md) FUN_0058a8b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0058a8c4",
      "incomplete_value": false,
      "site": "0058a8c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a884",
      "incomplete_value": false,
      "site": "0058a888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "0058a8c8",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a8c8",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a870.md#insn-0058a884) · [`0058a898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a870.md#insn-0058a898) · [`0058a8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a870.md#insn-0058a8a4)
- 新版 `0058a8c4`（命令位置の公開資料なし） · `0058a8d8`（命令位置の公開資料なし） · `0058a8e4`（命令位置の公開資料なし）

~~~diff
- 0058a884 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 0058a884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a8c4 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 0058a8c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a8c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a8c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a884 bytes 08a13391
+ 0058a8c4 bytes 08e13691
- 0058a898 ["INT_ADD", "register:40f0:8", ["const:58a898:8", "const:4:8"]]
- 0058a898 ["CALL", null, ["callee:00588f0c:8"]]
+ 0058a8d8 ["INT_ADD", "register:40f0:8", ["const:58a8d8:8", "const:4:8"]]
+ 0058a8d8 ["CALL", null, ["callee:00588f0c:8"]]
- 0058a898 bytes 8df9ff97
+ 0058a8d8 bytes 8df9ff97
- 0058a8a4 ["INT_ADD", "register:40f0:8", ["const:58a8a4:8", "const:4:8"]]
- 0058a8a4 ["CALL", null, ["callee:0058a98c:8"]]
+ 0058a8e4 ["INT_ADD", "register:40f0:8", ["const:58a8e4:8", "const:4:8"]]
+ 0058a8e4 ["CALL", null, ["callee:0058a98c:8"]]
- 0058a8a4 bytes 2a000094
+ 0058a8e4 bytes 2a000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ff3c9579223636b4fc4277cc81bedc0"></a>

### [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md) → [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md) FUN_0058a8fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 65件 [`0049b1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b1bc.md) [`00571af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571af4.md) [`00571e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00571/00571e18.md) [`005720f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005720f8.md) [`005722ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00572/005722ac.md) · 呼出先 2件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md)
- 新版 呼出元 65件 [`0049b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b1fc.md) [`00571b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571b34.md) [`00571e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00571/00571e58.md) [`00572138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/00572138.md) [`005722ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00572/005722ec.md) · 呼出先 2件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md)

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
      "definition_site": "0058a910",
      "incomplete_value": false,
      "site": "0058a914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a8d0",
      "incomplete_value": false,
      "site": "0058a8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "0058a914",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a914",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md#insn-0058a8d0) · [`0058a8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md#insn-0058a8e4)
- 新版 `0058a910`（命令位置の公開資料なし） · `0058a924`（命令位置の公開資料なし）

~~~diff
- 0058a8d0 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 0058a8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a910 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 0058a910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a8d0 bytes 08a13391
+ 0058a910 bytes 08e13691
- 0058a8e4 ["INT_ADD", "register:40f0:8", ["const:58a8e4:8", "const:4:8"]]
- 0058a8e4 ["CALL", null, ["callee:00588f0c:8"]]
+ 0058a924 ["INT_ADD", "register:40f0:8", ["const:58a924:8", "const:4:8"]]
+ 0058a924 ["CALL", null, ["callee:00588f0c:8"]]
- 0058a8e4 bytes 7af9ff97
+ 0058a924 bytes 7af9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a480697e8075f060aae781a8786b936"></a>

### [`0058a900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a900.md) → [`0058a940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a940.md) FUN_0058a940

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00588ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588ecc.md) [`0058a94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a94c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00588f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588f0c.md) [`0058a98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a98c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0058a954",
      "incomplete_value": false,
      "site": "0058a958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058a914",
      "incomplete_value": false,
      "site": "0058a918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "0058a958",
      "DATA",
      [
        "storage",
        "00c6cce8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0058a958",
      "DATA",
      [
        "storage",
        "00c6cdb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058a914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a900.md#insn-0058a914) · [`0058a928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a900.md#insn-0058a928) · [`0058a934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a900.md#insn-0058a934)
- 新版 `0058a954`（命令位置の公開資料なし） · `0058a968`（命令位置の公開資料なし） · `0058a974`（命令位置の公開資料なし）

~~~diff
- 0058a914 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 0058a914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058a914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058a914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058a954 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 0058a954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058a954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058a914 bytes 08a13391
+ 0058a954 bytes 08e13691
- 0058a928 ["INT_ADD", "register:40f0:8", ["const:58a928:8", "const:4:8"]]
- 0058a928 ["CALL", null, ["callee:00588f0c:8"]]
+ 0058a968 ["INT_ADD", "register:40f0:8", ["const:58a968:8", "const:4:8"]]
+ 0058a968 ["CALL", null, ["callee:00588f0c:8"]]
- 0058a928 bytes 69f9ff97
+ 0058a968 bytes 69f9ff97
- 0058a934 ["INT_ADD", "register:40f0:8", ["const:58a934:8", "const:4:8"]]
- 0058a934 ["CALL", null, ["callee:0058a98c:8"]]
+ 0058a974 ["INT_ADD", "register:40f0:8", ["const:58a974:8", "const:4:8"]]
+ 0058a974 ["CALL", null, ["callee:0058a98c:8"]]
- 0058a934 bytes 06000094
+ 0058a974 bytes 06000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5b4097fb46dad6255eb8914b39c193a"></a>

### [`0058abe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058abe4.md) → [`0058ac24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac24.md) _INIT_33

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058a8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058a8bc.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058a8fc.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)

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
      "definition_site": "0058ac3c",
      "incomplete_value": false,
      "site": "0058ac3c",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058abfc",
      "incomplete_value": false,
      "site": "0058abfc",
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
            "const:358:8"
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
      "definition_site": "0058ac3c",
      "incomplete_value": false,
      "site": "0058ac3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058abfc",
      "incomplete_value": false,
      "site": "0058abfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0058ac3c",
      "incomplete_value": false,
      "site": "0058ac3c",
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
                "const:ca6000:8"
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
      "definition_site": "0058abfc",
      "incomplete_value": false,
      "site": "0058abfc",
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
                "const:ca6000:8"
              ],
              [
                "leaf",
                "const:358:8"
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
      "0058ac28",
      "PARAM",
      [
        "storage",
        "00ca6358",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ac38",
      "PARAM",
      [
        "storage",
        "0058a8bc",
        null,
        null
      ]
    ],
    [
      "0058ac3c",
      "WRITE",
      [
        "storage",
        "00ca6358",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058ac28",
      "PARAM",
      [
        "storage",
        "00ca6458",
        null,
        "undefined8"
      ]
    ],
    [
      "0058ac38",
      "PARAM",
      [
        "storage",
        "0058a8fc",
        null,
        null
      ]
    ],
    [
      "0058ac3c",
      "WRITE",
      [
        "storage",
        "00ca6458",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058abe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058abe4.md#insn-0058abe8) · [`0058abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058abe4.md#insn-0058abf0) · [`0058abf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058abe4.md#insn-0058abf8)
- 新版 `0058ac28`（命令位置の公開資料なし） · `0058ac30`（命令位置の公開資料なし） · `0058ac38`（命令位置の公開資料なし）

~~~diff
- 0058abe8 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0058abe8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0058abe8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0058abe8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0058ac28 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0058ac28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0058ac28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0058ac28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0058abe8 bytes 21600d91
+ 0058ac28 bytes 21601191
- 0058abf0 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 0058abf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058abf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058abf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ac30 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 0058ac30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ac30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ac30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058abf0 bytes 08a13391
+ 0058ac30 bytes 08e13691
- 0058abf8 ["COPY", "register:4000:8", ["const:58a8bc:8"]]
+ 0058ac38 ["COPY", "register:4000:8", ["const:58a8fc:8"]]
- 0058abf8 bytes 20e6ff10
+ 0058ac38 bytes 20e6ff10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a97b67dd8567558fd0da51e36557652"></a>

### [`0058ac24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md) → [`0058ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ac64.md) FUN_0058ac64

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`0057ceb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057ceb8.md) [`0057d494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057d494.md) [`0057de10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057d/0057de10.md) [`00580b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00580/00580b30.md) [`005885f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/005885f8.md) · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 5件 [`0057cef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057cef8.md) [`0057d4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057d4d4.md) [`0057de50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057d/0057de50.md) [`00580b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00580/00580b70.md) [`00588638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588638.md) · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

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
      "definition_site": "0058ac8c",
      "incomplete_value": false,
      "site": "0058ac90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ac4c",
      "incomplete_value": false,
      "site": "0058ac50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "0058ac90",
      "DATA",
      [
        "storage",
        "00c6ce10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058ac90",
      "DATA",
      [
        "storage",
        "00c6cee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ac4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md#insn-0058ac4c) · [`0058ac64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md#insn-0058ac64) · [`0058ac7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ac24.md#insn-0058ac7c)
- 新版 `0058ac8c`（命令位置の公開資料なし） · `0058aca4`（命令位置の公開資料なし） · `0058acbc`（命令位置の公開資料なし）

~~~diff
- 0058ac4c ["COPY", "tmp:0:8", ["const:e10:8"]]
- 0058ac4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ac4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ac4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058ac8c ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 0058ac8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ac8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058ac8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ac4c bytes 08413891
+ 0058ac8c bytes 08813b91
- 0058ac64 ["INT_ADD", "register:40f0:8", ["const:58ac64:8", "const:4:8"]]
- 0058ac64 ["CALL", null, ["callee:00c57f60:8"]]
+ 0058aca4 ["INT_ADD", "register:40f0:8", ["const:58aca4:8", "const:4:8"]]
+ 0058aca4 ["CALL", null, ["callee:00c57f60:8"]]
- 0058ac64 bytes 8b341b94
+ 0058aca4 bytes af341b94
- 0058ac7c ["INT_ADD", "register:40f0:8", ["const:58ac7c:8", "const:4:8"]]
- 0058ac7c ["CALL", null, ["callee:00c580d0:8"]]
+ 0058acbc ["INT_ADD", "register:40f0:8", ["const:58acbc:8", "const:4:8"]]
+ 0058acbc ["CALL", null, ["callee:00c580d0:8"]]
- 0058ac7c bytes e1341b94
+ 0058acbc bytes 05351b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2814a06e18c647c9ff927af5383a0417"></a>

### [`0058b54c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b54c.md) → [`0058b58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b58c.md) FUN_0058b58c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0058b598",
      "incomplete_value": false,
      "site": "0058b59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b558",
      "incomplete_value": false,
      "site": "0058b55c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "0058b59c",
      "DATA",
      [
        "storage",
        "00c6ce10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b59c",
      "DATA",
      [
        "storage",
        "00c6cee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b54c.md#insn-0058b558)
- 新版 `0058b598`（命令位置の公開資料なし）

~~~diff
- 0058b558 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 0058b558 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b558 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b558 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b598 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 0058b598 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b598 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b598 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b558 bytes 29413891
+ 0058b598 bytes 29813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6c0517ac7ef56b0641553e789df2176"></a>

### [`0058b570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b570.md) → [`0058b5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b5b0.md) FUN_0058b5b0

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
      "definition_site": "0058b5b8",
      "incomplete_value": false,
      "site": "0058b5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b578",
      "incomplete_value": false,
      "site": "0058b57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "0058b5bc",
      "DATA",
      [
        "storage",
        "00c6ce10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b5bc",
      "DATA",
      [
        "storage",
        "00c6cee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b570.md#insn-0058b578) · [`0058b59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b570.md#insn-0058b59c)
- 新版 `0058b5b8`（命令位置の公開資料なし） · `0058b5dc`（命令位置の公開資料なし）

~~~diff
- 0058b578 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 0058b578 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b578 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b578 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b5b8 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 0058b5b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b5b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b5b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b578 bytes 29413891
+ 0058b5b8 bytes 29813b91
- 0058b59c ["INT_ADD", "register:40f0:8", ["const:58b59c:8", "const:4:8"]]
- 0058b59c ["CALL", null, ["callee:00c57f80:8"]]
+ 0058b5dc ["INT_ADD", "register:40f0:8", ["const:58b5dc:8", "const:4:8"]]
+ 0058b5dc ["CALL", null, ["callee:00c57f80:8"]]
- 0058b59c bytes 45321b94
+ 0058b5dc bytes 69321b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3fe49a03df2c39b9519b208884b9881"></a>

### [`0058b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b5b0.md) → [`0058b5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b5f0.md) FUN_0058b5f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0058b5fc",
      "incomplete_value": false,
      "site": "0058b600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b5bc",
      "incomplete_value": false,
      "site": "0058b5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "0058b600",
      "DATA",
      [
        "storage",
        "00c6ce48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b600",
      "DATA",
      [
        "storage",
        "00c6cf18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b5b0.md#insn-0058b5bc)
- 新版 `0058b5fc`（命令位置の公開資料なし）

~~~diff
- 0058b5bc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0058b5bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b5bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b5bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b5fc ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 0058b5fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b5fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b5fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b5bc bytes 29213991
+ 0058b5fc bytes 29613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f5404e99e896e148e62cd25c24d3ee2"></a>

### [`0058b5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b5d4.md) → [`0058b614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b614.md) FUN_0058b614

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
      "definition_site": "0058b61c",
      "incomplete_value": false,
      "site": "0058b620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b5dc",
      "incomplete_value": false,
      "site": "0058b5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "0058b620",
      "DATA",
      [
        "storage",
        "00c6ce48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b620",
      "DATA",
      [
        "storage",
        "00c6cf18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b5d4.md#insn-0058b5dc) · [`0058b600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b5d4.md#insn-0058b600)
- 新版 `0058b61c`（命令位置の公開資料なし） · `0058b640`（命令位置の公開資料なし）

~~~diff
- 0058b5dc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0058b5dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058b5dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058b5dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058b61c ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 0058b61c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b61c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058b61c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058b5dc bytes 29213991
+ 0058b61c bytes 29613c91
- 0058b600 ["INT_ADD", "register:40f0:8", ["const:58b600:8", "const:4:8"]]
- 0058b600 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058b640 ["INT_ADD", "register:40f0:8", ["const:58b640:8", "const:4:8"]]
+ 0058b640 ["CALL", null, ["callee:00c57f80:8"]]
- 0058b600 bytes 2c321b94
+ 0058b640 bytes 50321b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f6388397454bc5c50d341332086f557"></a>

### [`0058b614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b614.md) → [`0058b654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b654.md) FUN_0058b654

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0058ad6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058ad6c.md) [`0058adc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058adc8.md) [`0058af3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058a/0058af3c.md) · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 3件 [`0058adac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058adac.md) [`0058ae08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058ae08.md) [`0058af7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058a/0058af7c.md) · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

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
      "definition_site": "0058b67c",
      "incomplete_value": false,
      "site": "0058b684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b63c",
      "incomplete_value": false,
      "site": "0058b644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "definition_site": "0058b690",
      "incomplete_value": false,
      "site": "0058b690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b650",
      "incomplete_value": false,
      "site": "0058b650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "0058b684",
      "DATA",
      [
        "storage",
        "00c6c260",
        null,
        "pointer"
      ]
    ],
    [
      "0058b690",
      "DATA",
      [
        "storage",
        "00c6ce10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b684",
      "DATA",
      [
        "storage",
        "00c6c330",
        null,
        "pointer"
      ]
    ],
    [
      "0058b690",
      "DATA",
      [
        "storage",
        "00c6cee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b614.md#insn-0058b634) · [`0058b63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b614.md#insn-0058b63c) · [`0058b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b614.md#insn-0058b640)
- 新版 `0058b674`（命令位置の公開資料なし） · `0058b67c`（命令位置の公開資料なし）

~~~diff
- 0058b634 ["INT_ADD", "register:40f0:8", ["const:58b634:8", "const:4:8"]]
- 0058b634 ["CALL", null, ["callee:00c57f60:8"]]
+ 0058b674 ["INT_ADD", "register:40f0:8", ["const:58b674:8", "const:4:8"]]
+ 0058b674 ["CALL", null, ["callee:00c57f60:8"]]
- 0058b634 bytes 17321b94
+ 0058b674 bytes 3b321b94
- 0058b63c ["COPY", "tmp:0:8", ["const:260:8"]]
- 0058b63c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058b63c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058b63c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058b67c ["COPY", "tmp:0:8", ["const:330:8"]]
+ 0058b67c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b67c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b67c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058b63c bytes 08810991
+ 0058b67c bytes 08c10c91
- 0058b640 ["COPY", "register:40c0:8", ["register:4000:8"]]
- 0058b640 bytes f80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d5fb8dd972195dbd0ccdd51a44efb78"></a>

### [`0058b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b7f4.md) → [`0058b834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b834.md) FUN_0058b834

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0058b1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b1d0.md) [`0058b274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b274.md) [`0058b3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b3e8.md) · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 3件 [`0058b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b210.md) [`0058b2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b2b4.md) [`0058b428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b428.md) · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

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
      "definition_site": "0058b85c",
      "incomplete_value": false,
      "site": "0058b864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b81c",
      "incomplete_value": false,
      "site": "0058b824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "definition_site": "0058b870",
      "incomplete_value": false,
      "site": "0058b870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b830",
      "incomplete_value": false,
      "site": "0058b830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "0058b864",
      "DATA",
      [
        "storage",
        "00c6cee8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058b870",
      "DATA",
      [
        "storage",
        "00c6ce48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b864",
      "DATA",
      [
        "storage",
        "00c6cfb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0058b870",
      "DATA",
      [
        "storage",
        "00c6cf18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b7f4.md#insn-0058b814) · [`0058b81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b7f4.md#insn-0058b81c) · [`0058b820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b7f4.md#insn-0058b820)
- 新版 `0058b854`（命令位置の公開資料なし） · `0058b85c`（命令位置の公開資料なし）

~~~diff
- 0058b814 ["INT_ADD", "register:40f0:8", ["const:58b814:8", "const:4:8"]]
- 0058b814 ["CALL", null, ["callee:00c57f60:8"]]
+ 0058b854 ["INT_ADD", "register:40f0:8", ["const:58b854:8", "const:4:8"]]
+ 0058b854 ["CALL", null, ["callee:00c57f60:8"]]
- 0058b814 bytes 9f311b94
+ 0058b854 bytes c3311b94
- 0058b81c ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 0058b81c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058b81c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058b81c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058b85c ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0058b85c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b85c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b85c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058b81c bytes 08a13b91
+ 0058b85c bytes 08e13e91
- 0058b820 ["COPY", "register:40c0:8", ["register:4000:8"]]
- 0058b820 bytes f80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f58957de7065565d5515940ce8128cf3"></a>

### [`0058b8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b8cc.md) → [`0058b90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b90c.md) FUN_0058b90c

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
      "definition_site": "0058b910",
      "incomplete_value": false,
      "site": "0058b914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b8d0",
      "incomplete_value": false,
      "site": "0058b8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "0058b914",
      "DATA",
      [
        "storage",
        "00c6cee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b914",
      "DATA",
      [
        "storage",
        "00c6cfb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b8cc.md#insn-0058b8d0)
- 新版 `0058b910`（命令位置の公開資料なし）

~~~diff
- 0058b8d0 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 0058b8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058b8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058b8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058b910 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0058b910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058b8d0 bytes 08a13b91
+ 0058b910 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b9ac3f78bd47a44d92efaf2d1310165"></a>

### [`0058b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b8dc.md) → [`0058b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b91c.md) FUN_0058b91c

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
      "definition_site": "0058b92c",
      "incomplete_value": false,
      "site": "0058b934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b8ec",
      "incomplete_value": false,
      "site": "0058b8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6c000:8"
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
      "0058b934",
      "DATA",
      [
        "storage",
        "00c6cee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0058b934",
      "DATA",
      [
        "storage",
        "00c6cfb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b8dc.md#insn-0058b8ec) · [`0058b8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b8dc.md#insn-0058b8f8)
- 新版 `0058b92c`（命令位置の公開資料なし） · `0058b938`（命令位置の公開資料なし）

~~~diff
- 0058b8ec ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 0058b8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058b8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058b8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058b92c ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0058b92c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b92c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058b92c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058b8ec bytes 08a13b91
+ 0058b92c bytes 08e13e91
- 0058b8f8 ["INT_ADD", "register:40f0:8", ["const:58b8f8:8", "const:4:8"]]
- 0058b8f8 ["CALL", null, ["callee:00c57f70:8"]]
+ 0058b938 ["INT_ADD", "register:40f0:8", ["const:58b938:8", "const:4:8"]]
+ 0058b938 ["CALL", null, ["callee:00c57f70:8"]]
- 0058b8f8 bytes 6a311b94
+ 0058b938 bytes 8e311b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2db227721ea713321d66204fbd279a6b"></a>

### [`0058b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b944.md) → [`0058b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058b984.md) FUN_0058b984

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597620.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00597660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597660.md) · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058b9d8",
      "incomplete_value": true,
      "site": "0058b9d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:4e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b998",
      "incomplete_value": true,
      "site": "0058b998",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:a2:8"
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
      "definition_site": "0058b9e0",
      "incomplete_value": true,
      "site": "0058b9e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058b9a0",
      "incomplete_value": true,
      "site": "0058b9a0",
      "value": [
        "LOAD",
        "8",
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058b9dc",
      "incomplete_value": true,
      "site": "0058b9f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f65:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058b99c",
      "incomplete_value": true,
      "site": "0058b9b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb2:8"
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
      "0058b9c0",
      "READ",
      [
        "storage",
        "002b90a2",
        null,
        "string"
      ]
    ],
    [
      "0058b9c8",
      "READ",
      [
        "storage",
        "002b90a8",
        null,
        "string"
      ]
    ],
    [
      "0058b9dc",
      "READ",
      [
        "storage",
        "002a0fb2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058b9c0",
      "READ",
      [
        "storage",
        "002b904e",
        null,
        "string"
      ]
    ],
    [
      "0058b9c8",
      "READ",
      [
        "storage",
        "002b9054",
        null,
        "string"
      ]
    ],
    [
      "0058b9dc",
      "READ",
      [
        "storage",
        "002a0f65",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b944.md#insn-0058b9e0) · [`0058b968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b944.md#insn-0058b968) · [`0058b970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058b944.md#insn-0058b970)
- 新版 `0058ba20`（命令位置の公開資料なし） · `0058b9a8`（命令位置の公開資料なし） · `0058b9b0`（命令位置の公開資料なし）

~~~diff
- 0058b9e0 ["INT_ADD", "register:40f0:8", ["const:58b9e0:8", "const:4:8"]]
- 0058b9e0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058ba20 ["INT_ADD", "register:40f0:8", ["const:58ba20:8", "const:4:8"]]
+ 0058ba20 ["CALL", null, ["callee:00c57f80:8"]]
- 0058b9e0 bytes 34311b94
+ 0058ba20 bytes 58311b94
- 0058b968 ["INT_ADD", "register:40f0:8", ["const:58b968:8", "const:4:8"]]
- 0058b968 ["CALL", null, ["callee:00588eac:8"]]
+ 0058b9a8 ["INT_ADD", "register:40f0:8", ["const:58b9a8:8", "const:4:8"]]
+ 0058b9a8 ["CALL", null, ["callee:00588eac:8"]]
- 0058b968 bytes 41f5ff97
+ 0058b9a8 bytes 41f5ff97
- 0058b970 ["INT_ADD", "register:40f0:8", ["const:58b970:8", "const:4:8"]]
- 0058b970 ["CALL", null, ["callee:0058919c:8"]]
+ 0058b9b0 ["INT_ADD", "register:40f0:8", ["const:58b9b0:8", "const:4:8"]]
+ 0058b9b0 ["CALL", null, ["callee:0058919c:8"]]
- 0058b970 bytes fbf5ff97
+ 0058b9b0 bytes fbf5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de2e82bab1b101e9a231b3858f9f3b81"></a>

### [`0058badc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058badc.md) → [`0058bb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058bb1c.md) FUN_0058bb1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597624.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00597664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597664.md) · 呼出先 9件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058bb74",
      "incomplete_value": true,
      "site": "0058bb74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bb34",
      "incomplete_value": true,
      "site": "0058bb34",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e9a:8"
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
      "definition_site": "0058bb88",
      "incomplete_value": true,
      "site": "0058bb98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f65:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bb48",
      "incomplete_value": true,
      "site": "0058bb58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb2:8"
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
      "0058bb64",
      "READ",
      [
        "storage",
        "002bee9a",
        null,
        "string"
      ]
    ],
    [
      "0058bb88",
      "READ",
      [
        "storage",
        "002a0fb2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058bb64",
      "READ",
      [
        "storage",
        "002bee46",
        null,
        "string"
      ]
    ],
    [
      "0058bb88",
      "READ",
      [
        "storage",
        "002a0f65",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058bb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058badc.md#insn-0058bb00) · [`0058bb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058badc.md#insn-0058bb08) · [`0058bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058badc.md#insn-0058bb20)
- 新版 `0058bb40`（命令位置の公開資料なし） · `0058bb48`（命令位置の公開資料なし） · `0058bb60`（命令位置の公開資料なし）

~~~diff
- 0058bb00 ["INT_ADD", "register:40f0:8", ["const:58bb00:8", "const:4:8"]]
- 0058bb00 ["CALL", null, ["callee:00588eac:8"]]
+ 0058bb40 ["INT_ADD", "register:40f0:8", ["const:58bb40:8", "const:4:8"]]
+ 0058bb40 ["CALL", null, ["callee:00588eac:8"]]
- 0058bb00 bytes dbf4ff97
+ 0058bb40 bytes dbf4ff97
- 0058bb08 ["INT_ADD", "register:40f0:8", ["const:58bb08:8", "const:4:8"]]
- 0058bb08 ["CALL", null, ["callee:0058919c:8"]]
+ 0058bb48 ["INT_ADD", "register:40f0:8", ["const:58bb48:8", "const:4:8"]]
+ 0058bb48 ["CALL", null, ["callee:0058919c:8"]]
- 0058bb08 bytes 95f5ff97
+ 0058bb48 bytes 95f5ff97
- 0058bb20 ["COPY", "tmp:0:8", ["const:e9a:8"]]
- 0058bb20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058bb20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058bb20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058bb60 ["COPY", "tmp:0:8", ["const:e46:8"]]
+ 0058bb60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058bb60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058bb60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058bb20 bytes 08693a91
+ 0058bb60 bytes 08193991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e052a6cf38a1a441ec10721f35d35f6"></a>

### [`0058bc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058bc78.md) → [`0058bcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058bcb8.md) FUN_0058bcb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597628.md) · 呼出先 11件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00597668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597668.md) · 呼出先 11件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

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
      "definition_site": "0058bd0c",
      "incomplete_value": true,
      "site": "0058bd0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bccc",
      "incomplete_value": true,
      "site": "0058bccc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:402:8"
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
      "definition_site": "0058bd20",
      "incomplete_value": true,
      "site": "0058bd28",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:cc5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058bce0",
      "incomplete_value": true,
      "site": "0058bce8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:c94:8"
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
      "definition_site": "0058bd2c",
      "incomplete_value": true,
      "site": "0058bd2c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058bcec",
      "incomplete_value": true,
      "site": "0058bcec",
      "value": [
        "LOAD",
        "8",
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
      "0058bd00",
      "READ",
      [
        "storage",
        "002a4402",
        null,
        "string"
      ]
    ],
    [
      "0058bd20",
      "READ",
      [
        "storage",
        "002b3c94",
        null,
        "string"
      ]
    ],
    [
      "0058bd24",
      "READ",
      [
        "storage",
        "002b3ca1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058bd00",
      "READ",
      [
        "storage",
        "002a43b5",
        null,
        "string"
      ]
    ],
    [
      "0058bd20",
      "READ",
      [
        "storage",
        "002b3cc5",
        null,
        "string"
      ]
    ],
    [
      "0058bd24",
      "READ",
      [
        "storage",
        "002b3cd2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058bd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058bc78.md#insn-0058bd28) · [`0058bc9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058bc78.md#insn-0058bc9c) · [`0058bca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058bc78.md#insn-0058bca4)
- 新版 `0058bd68`（命令位置の公開資料なし） · `0058bcdc`（命令位置の公開資料なし） · `0058bce4`（命令位置の公開資料なし）

~~~diff
- 0058bd28 ["INT_ADD", "register:40f0:8", ["const:58bd28:8", "const:4:8"]]
- 0058bd28 ["CALL", null, ["callee:00589184:8"]]
+ 0058bd68 ["INT_ADD", "register:40f0:8", ["const:58bd68:8", "const:4:8"]]
+ 0058bd68 ["CALL", null, ["callee:00589184:8"]]
- 0058bd28 bytes 07f5ff97
+ 0058bd68 bytes 07f5ff97
- 0058bc9c ["INT_ADD", "register:40f0:8", ["const:58bc9c:8", "const:4:8"]]
- 0058bc9c ["CALL", null, ["callee:00588eac:8"]]
+ 0058bcdc ["INT_ADD", "register:40f0:8", ["const:58bcdc:8", "const:4:8"]]
+ 0058bcdc ["CALL", null, ["callee:00588eac:8"]]
- 0058bc9c bytes 74f4ff97
+ 0058bcdc bytes 74f4ff97
- 0058bca4 ["INT_ADD", "register:40f0:8", ["const:58bca4:8", "const:4:8"]]
- 0058bca4 ["CALL", null, ["callee:0058919c:8"]]
+ 0058bce4 ["INT_ADD", "register:40f0:8", ["const:58bce4:8", "const:4:8"]]
+ 0058bce4 ["CALL", null, ["callee:0058919c:8"]]
- 0058bca4 bytes 2ef5ff97
+ 0058bce4 bytes 2ef5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-415fbbb7dcef890b6ee2943200439c0f"></a>

### [`0058be3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058be3c.md) → [`0058be7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058b/0058be7c.md) FUN_0058be7c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597630.md) · 呼出先 9件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00597670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597670.md) · 呼出先 9件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.36% / 新版 90.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058bec4",
      "incomplete_value": true,
      "site": "0058bed0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058be84",
      "incomplete_value": true,
      "site": "0058be90",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058bec0",
      "incomplete_value": true,
      "site": "0058bed8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058be80",
      "incomplete_value": true,
      "site": "0058be98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:145:8"
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
      "definition_site": "0058bedc",
      "incomplete_value": true,
      "site": "0058beec",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058be9c",
      "incomplete_value": true,
      "site": "0058beac",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:2a0:8"
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
      "0058bec0",
      "READ",
      [
        "storage",
        "002a2145",
        null,
        "string"
      ]
    ],
    [
      "0058bec4",
      "READ",
      [
        "storage",
        "002a2155",
        null,
        "string"
      ]
    ],
    [
      "0058bedc",
      "READ",
      [
        "storage",
        "002c22a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058bec0",
      "READ",
      [
        "storage",
        "002a20f8",
        null,
        "string"
      ]
    ],
    [
      "0058bec4",
      "READ",
      [
        "storage",
        "002a2108",
        null,
        "string"
      ]
    ],
    [
      "0058bedc",
      "READ",
      [
        "storage",
        "002c22e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058be3c.md#insn-0058bed8) · [`0058be5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058be3c.md#insn-0058be5c) · [`0058be64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058be3c.md#insn-0058be64)
- 新版 `0058bf18`（命令位置の公開資料なし） · `0058be9c`（命令位置の公開資料なし） · `0058bea4`（命令位置の公開資料なし）

~~~diff
- 0058bed8 ["INT_ADD", "register:40f0:8", ["const:58bed8:8", "const:4:8"]]
- 0058bed8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058bf18 ["INT_ADD", "register:40f0:8", ["const:58bf18:8", "const:4:8"]]
+ 0058bf18 ["CALL", null, ["callee:00c57f80:8"]]
- 0058bed8 bytes f62f1b94
+ 0058bf18 bytes 1a301b94
- 0058be5c ["INT_ADD", "register:40f0:8", ["const:58be5c:8", "const:4:8"]]
- 0058be5c ["CALL", null, ["callee:00588eac:8"]]
+ 0058be9c ["INT_ADD", "register:40f0:8", ["const:58be9c:8", "const:4:8"]]
+ 0058be9c ["CALL", null, ["callee:00588eac:8"]]
- 0058be5c bytes 04f4ff97
+ 0058be9c bytes 04f4ff97
- 0058be64 ["INT_ADD", "register:40f0:8", ["const:58be64:8", "const:4:8"]]
- 0058be64 ["CALL", null, ["callee:0058919c:8"]]
+ 0058bea4 ["INT_ADD", "register:40f0:8", ["const:58bea4:8", "const:4:8"]]
+ 0058bea4 ["CALL", null, ["callee:0058919c:8"]]
- 0058be64 bytes bef4ff97
+ 0058bea4 bytes bef4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fe38e200db00ac825125e2e4770687d"></a>

### [`0058bfc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058bfc4.md) → [`0058c004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c004.md) FUN_0058c004

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0059762c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059762c.md) · 呼出先 11件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`0059766c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059766c.md) · 呼出先 11件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

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
      "definition_site": "0058c06c",
      "incomplete_value": true,
      "site": "0058c074",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:cc5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c02c",
      "incomplete_value": true,
      "site": "0058c034",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:c94:8"
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
      "definition_site": "0058c078",
      "incomplete_value": true,
      "site": "0058c078",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058c038",
      "incomplete_value": true,
      "site": "0058c038",
      "value": [
        "LOAD",
        "8",
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
      "0058c06c",
      "READ",
      [
        "storage",
        "002b3c94",
        null,
        "string"
      ]
    ],
    [
      "0058c070",
      "READ",
      [
        "storage",
        "002b3ca1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058c06c",
      "READ",
      [
        "storage",
        "002b3cc5",
        null,
        "string"
      ]
    ],
    [
      "0058c070",
      "READ",
      [
        "storage",
        "002b3cd2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058bfc4.md#insn-0058c074) · [`0058bfe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058bfc4.md#insn-0058bfe8) · [`0058bff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058b/0058bfc4.md#insn-0058bff0)
- 新版 `0058c0b4`（命令位置の公開資料なし） · `0058c028`（命令位置の公開資料なし） · `0058c030`（命令位置の公開資料なし）

~~~diff
- 0058c074 ["INT_ADD", "register:40f0:8", ["const:58c074:8", "const:4:8"]]
- 0058c074 ["CALL", null, ["callee:00589184:8"]]
+ 0058c0b4 ["INT_ADD", "register:40f0:8", ["const:58c0b4:8", "const:4:8"]]
+ 0058c0b4 ["CALL", null, ["callee:00589184:8"]]
- 0058c074 bytes 34f4ff97
+ 0058c0b4 bytes 34f4ff97
- 0058bfe8 ["INT_ADD", "register:40f0:8", ["const:58bfe8:8", "const:4:8"]]
- 0058bfe8 ["CALL", null, ["callee:00588eac:8"]]
+ 0058c028 ["INT_ADD", "register:40f0:8", ["const:58c028:8", "const:4:8"]]
+ 0058c028 ["CALL", null, ["callee:00588eac:8"]]
- 0058bfe8 bytes a1f3ff97
+ 0058c028 bytes a1f3ff97
- 0058bff0 ["INT_ADD", "register:40f0:8", ["const:58bff0:8", "const:4:8"]]
- 0058bff0 ["CALL", null, ["callee:0058919c:8"]]
+ 0058c030 ["INT_ADD", "register:40f0:8", ["const:58c030:8", "const:4:8"]]
+ 0058c030 ["CALL", null, ["callee:0058919c:8"]]
- 0058bff0 bytes 5bf4ff97
+ 0058c030 bytes 5bf4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1ddef40a67f00465060856fc86cc0d6"></a>

### [`0058c188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c188.md) → [`0058c1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c1c8.md) FUN_0058c1c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00597634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597634.md) · 呼出先 11件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00597674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597674.md) · 呼出先 11件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

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
      "definition_site": "0058c204",
      "incomplete_value": true,
      "site": "0058c21c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:d19:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c1c4",
      "incomplete_value": true,
      "site": "0058c1dc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:d75:8"
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
      "definition_site": "0058c220",
      "incomplete_value": true,
      "site": "0058c22c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:48d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c1e0",
      "incomplete_value": true,
      "site": "0058c1ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e1:8"
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
      "definition_site": "0058c230",
      "incomplete_value": true,
      "site": "0058c230",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058c1f0",
      "incomplete_value": true,
      "site": "0058c1f0",
      "value": [
        "LOAD",
        "8",
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
      "0058c204",
      "READ",
      [
        "storage",
        "002b0d75",
        null,
        "string"
      ]
    ],
    [
      "0058c220",
      "READ",
      [
        "storage",
        "002bb4e1",
        null,
        "string"
      ]
    ],
    [
      "0058c224",
      "READ",
      [
        "storage",
        "002bb4ee",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058c204",
      "READ",
      [
        "storage",
        "002b0d19",
        null,
        "string"
      ]
    ],
    [
      "0058c220",
      "READ",
      [
        "storage",
        "002bb48d",
        null,
        "string"
      ]
    ],
    [
      "0058c224",
      "READ",
      [
        "storage",
        "002bb49a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c188.md#insn-0058c1ac) · [`0058c230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c188.md#insn-0058c230) · [`0058c1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c188.md#insn-0058c1b4)
- 新版 `0058c1ec`（命令位置の公開資料なし） · `0058c270`（命令位置の公開資料なし） · `0058c1f4`（命令位置の公開資料なし）

~~~diff
- 0058c1ac ["INT_ADD", "register:40f0:8", ["const:58c1ac:8", "const:4:8"]]
- 0058c1ac ["CALL", null, ["callee:00588eac:8"]]
+ 0058c1ec ["INT_ADD", "register:40f0:8", ["const:58c1ec:8", "const:4:8"]]
+ 0058c1ec ["CALL", null, ["callee:00588eac:8"]]
- 0058c1ac bytes 30f3ff97
+ 0058c1ec bytes 30f3ff97
- 0058c230 ["INT_ADD", "register:40f0:8", ["const:58c230:8", "const:4:8"]]
- 0058c230 ["CALL", null, ["callee:00589184:8"]]
+ 0058c270 ["INT_ADD", "register:40f0:8", ["const:58c270:8", "const:4:8"]]
+ 0058c270 ["CALL", null, ["callee:00589184:8"]]
- 0058c230 bytes c5f3ff97
+ 0058c270 bytes c5f3ff97
- 0058c1b4 ["INT_ADD", "register:40f0:8", ["const:58c1b4:8", "const:4:8"]]
- 0058c1b4 ["CALL", null, ["callee:0058919c:8"]]
+ 0058c1f4 ["INT_ADD", "register:40f0:8", ["const:58c1f4:8", "const:4:8"]]
+ 0058c1f4 ["CALL", null, ["callee:0058919c:8"]]
- 0058c1b4 bytes eaf3ff97
+ 0058c1f4 bytes eaf3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36625062679dc6eb9ef844dd2cdbdc94"></a>

### [`0058c2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c2f0.md) → [`0058c330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c330.md) FUN_0058c330

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00597638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597638.md) · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00597678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597678.md) · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

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
      "definition_site": "0058c380",
      "incomplete_value": true,
      "site": "0058c380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:961:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c340",
      "incomplete_value": true,
      "site": "0058c340",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9bd:8"
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
      "0058c370",
      "READ",
      [
        "storage",
        "002a79bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058c370",
      "READ",
      [
        "storage",
        "002a7961",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c2f0.md#insn-0058c380) · [`0058c314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c2f0.md#insn-0058c314) · [`0058c31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c2f0.md#insn-0058c31c)
- 新版 `0058c3c0`（命令位置の公開資料なし） · `0058c354`（命令位置の公開資料なし） · `0058c35c`（命令位置の公開資料なし）

~~~diff
- 0058c380 ["INT_ADD", "register:40f0:8", ["const:58c380:8", "const:4:8"]]
- 0058c380 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058c3c0 ["INT_ADD", "register:40f0:8", ["const:58c3c0:8", "const:4:8"]]
+ 0058c3c0 ["CALL", null, ["callee:00c57f80:8"]]
- 0058c380 bytes cc2e1b94
+ 0058c3c0 bytes f02e1b94
- 0058c314 ["INT_ADD", "register:40f0:8", ["const:58c314:8", "const:4:8"]]
- 0058c314 ["CALL", null, ["callee:00588eac:8"]]
+ 0058c354 ["INT_ADD", "register:40f0:8", ["const:58c354:8", "const:4:8"]]
+ 0058c354 ["CALL", null, ["callee:00588eac:8"]]
- 0058c314 bytes d6f2ff97
+ 0058c354 bytes d6f2ff97
- 0058c31c ["INT_ADD", "register:40f0:8", ["const:58c31c:8", "const:4:8"]]
- 0058c31c ["CALL", null, ["callee:0058919c:8"]]
+ 0058c35c ["INT_ADD", "register:40f0:8", ["const:58c35c:8", "const:4:8"]]
+ 0058c35c ["CALL", null, ["callee:0058919c:8"]]
- 0058c31c bytes 90f3ff97
+ 0058c35c bytes 90f3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0a9e4fd253b0721020630e82b38bc70"></a>

### [`0058c428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c428.md) → [`0058c468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c468.md) FUN_0058c468

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00597640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597640.md) · 呼出先 9件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`0057c59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057c/0057c59c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 1件 [`00597680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597680.md) · 呼出先 9件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`0057c5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057c/0057c5dc.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

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
      "definition_site": "0058c490",
      "incomplete_value": false,
      "site": "0058c49c",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c450",
      "incomplete_value": false,
      "site": "0058c45c",
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
            "const:398:8"
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
      "definition_site": "0058c498",
      "incomplete_value": true,
      "site": "0058c49c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058c458",
      "incomplete_value": true,
      "site": "0058c45c",
      "value": [
        "LOAD",
        "8",
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
      "0058c490",
      "PARAM",
      [
        "storage",
        "00ca6398",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c498",
      "READ",
      [
        "storage",
        "00ca63a0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c4a0",
      "WRITE",
      [
        "storage",
        "00ca6398",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058c490",
      "PARAM",
      [
        "storage",
        "00ca6498",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c498",
      "READ",
      [
        "storage",
        "00ca64a0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c4a0",
      "WRITE",
      [
        "storage",
        "00ca6498",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c428.md#insn-0058c45c) · [`0058c444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c428.md#insn-0058c444) · [`0058c46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c428.md#insn-0058c46c)
- 新版 `0058c49c`（命令位置の公開資料なし） · `0058c484`（命令位置の公開資料なし） · `0058c4ac`（命令位置の公開資料なし）

~~~diff
- 0058c45c ["INT_ADD", "register:40f0:8", ["const:58c45c:8", "const:4:8"]]
- 0058c45c ["CALL", null, ["callee:0057c5dc:8"]]
+ 0058c49c ["INT_ADD", "register:40f0:8", ["const:58c49c:8", "const:4:8"]]
+ 0058c49c ["CALL", null, ["callee:0057c5dc:8"]]
- 0058c45c bytes 50c0ff97
+ 0058c49c bytes 50c0ff97
- 0058c444 ["COPY", "tmp:0:8", ["const:398:8"]]
- 0058c444 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0058c444 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0058c444 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0058c484 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0058c484 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0058c484 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0058c484 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0058c444 bytes 73620e91
+ 0058c484 bytes 73621291
- 0058c46c ["INT_ADD", "register:40f0:8", ["const:58c46c:8", "const:4:8"]]
- 0058c46c ["CALL", null, ["callee:00588eac:8"]]
+ 0058c4ac ["INT_ADD", "register:40f0:8", ["const:58c4ac:8", "const:4:8"]]
+ 0058c4ac ["CALL", null, ["callee:00588eac:8"]]
- 0058c46c bytes 80f2ff97
+ 0058c4ac bytes 80f2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3c14213d747df0451e970ac626d2bd1"></a>

### [`0058c564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c564.md) → [`0058c5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c5a4.md) FUN_0058c5a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597644.md) · 呼出先 12件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00597684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597684.md) · 呼出先 12件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

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
      "definition_site": "0058c5f4",
      "incomplete_value": true,
      "site": "0058c5f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:40b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c5b4",
      "incomplete_value": true,
      "site": "0058c5b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:45f:8"
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
      "definition_site": "0058c670",
      "incomplete_value": true,
      "site": "0058c670",
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
      "definition_site": "0058c630",
      "incomplete_value": true,
      "site": "0058c630",
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
      "definition_site": "0058c73c",
      "incomplete_value": false,
      "site": "0058c740",
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
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058c6fc",
      "incomplete_value": false,
      "site": "0058c700",
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
            "const:3b0:8"
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
      "0058c5e8",
      "READ",
      [
        "storage",
        "002ba45f",
        null,
        "string"
      ]
    ],
    [
      "0058c658",
      "PARAM",
      [
        "storage",
        "00ca63b0",
        null,
        null
      ]
    ],
    [
      "0058c668",
      "READ",
      [
        "storage",
        "00ca63a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058c5e8",
      "READ",
      [
        "storage",
        "002ba40b",
        null,
        "string"
      ]
    ],
    [
      "0058c658",
      "PARAM",
      [
        "storage",
        "00ca64b0",
        null,
        null
      ]
    ],
    [
      "0058c668",
      "READ",
      [
        "storage",
        "00ca64a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c564.md#insn-0058c5f4) · [`0058c700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c564.md#insn-0058c700) · [`0058c58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c564.md#insn-0058c58c)
- 新版 `0058c634`（命令位置の公開資料なし） · `0058c740`（命令位置の公開資料なし） · `0058c5cc`（命令位置の公開資料なし）

~~~diff
- 0058c5f4 ["INT_ADD", "register:40f0:8", ["const:58c5f4:8", "const:4:8"]]
- 0058c5f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058c634 ["INT_ADD", "register:40f0:8", ["const:58c634:8", "const:4:8"]]
+ 0058c634 ["CALL", null, ["callee:00c57f80:8"]]
- 0058c5f4 bytes 2f2e1b94
+ 0058c634 bytes 532e1b94
- 0058c700 ["INT_ADD", "register:40f0:8", ["const:58c700:8", "const:4:8"]]
- 0058c700 ["CALL", null, ["callee:00c581c0:8"]]
+ 0058c740 ["INT_ADD", "register:40f0:8", ["const:58c740:8", "const:4:8"]]
+ 0058c740 ["CALL", null, ["callee:00c581c0:8"]]
- 0058c700 bytes 7c2e1b94
+ 0058c740 bytes a02e1b94
- 0058c58c ["INT_ADD", "register:40f0:8", ["const:58c58c:8", "const:4:8"]]
- 0058c58c ["CALL", null, ["callee:00588eac:8"]]
+ 0058c5cc ["INT_ADD", "register:40f0:8", ["const:58c5cc:8", "const:4:8"]]
+ 0058c5cc ["CALL", null, ["callee:00588eac:8"]]
- 0058c58c bytes 38f2ff97
+ 0058c5cc bytes 38f2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c652bcd433e6da45680f08b148475323"></a>

### [`0058c7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c7c4.md) → [`0058c804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058c804.md) FUN_0058c804

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00597648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597648.md) · 呼出先 6件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md)
- 新版 呼出元 1件 [`00597688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597688.md) · 呼出先 6件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md)

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
      "definition_site": "0058c95c",
      "incomplete_value": true,
      "site": "0058c95c",
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
      "definition_site": "0058c91c",
      "incomplete_value": true,
      "site": "0058c91c",
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
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0058c848",
      "incomplete_value": true,
      "site": "0058c848",
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
      "definition_site": "0058c808",
      "incomplete_value": true,
      "site": "0058c808",
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
      "definition_site": "0058c958",
      "incomplete_value": true,
      "site": "0058c958",
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
      "definition_site": "0058c918",
      "incomplete_value": true,
      "site": "0058c918",
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
      "0058c834",
      "PARAM",
      [
        "storage",
        "00ca63b0",
        null,
        null
      ]
    ],
    [
      "0058c844",
      "READ",
      [
        "storage",
        "00ca63a0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c89c",
      "READ",
      [
        "storage",
        "00ca63f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0058c834",
      "PARAM",
      [
        "storage",
        "00ca64b0",
        null,
        null
      ]
    ],
    [
      "0058c844",
      "READ",
      [
        "storage",
        "00ca64a0",
        null,
        "undefined8"
      ]
    ],
    [
      "0058c89c",
      "READ",
      [
        "storage",
        "00ca64f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058c7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c7c4.md#insn-0058c7f8) · [`0058c8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c7c4.md#insn-0058c8d8) · [`0058c91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058c7c4.md#insn-0058c91c)
- 新版 `0058c838`（命令位置の公開資料なし） · `0058c918`（命令位置の公開資料なし） · `0058c95c`（命令位置の公開資料なし）

~~~diff
- 0058c7f8 ["INT_ADD", "register:40f0:8", ["const:58c7f8:8", "const:4:8"]]
- 0058c7f8 ["CALL", null, ["callee:00c581b0:8"]]
+ 0058c838 ["INT_ADD", "register:40f0:8", ["const:58c838:8", "const:4:8"]]
+ 0058c838 ["CALL", null, ["callee:00c581b0:8"]]
- 0058c7f8 bytes 3a2e1b94
+ 0058c838 bytes 5e2e1b94
- 0058c8d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0058c8d8 ["INT_ADD", "register:40f0:8", ["const:58c8d8:8", "const:4:8"]]
- 0058c8d8 ["CALLIND", null, ["register:0:8"]]
+ 0058c918 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0058c918 ["INT_ADD", "register:40f0:8", ["const:58c918:8", "const:4:8"]]
+ 0058c918 ["CALLIND", null, ["register:0:8"]]
- 0058c8d8 bytes 00013fd6
+ 0058c918 bytes 00013fd6
- 0058c91c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:398:8"]]
- 0058c91c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0058c95c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:498:8"]]
+ 0058c95c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0058c91c bytes 28cd01f9
+ 0058c95c bytes 284d02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-524d11e78ba80354543c17af6f0acb81"></a>

### [`0058ca4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058ca4c.md) → [`0058ca8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ca8c.md) FUN_0058ca8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0059764c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059764c.md) · 呼出先 13件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)
- 新版 呼出元 1件 [`0059768c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059768c.md) · 呼出先 13件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md)

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
      "definition_site": "0058cae0",
      "incomplete_value": true,
      "site": "0058cae0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:79c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058caa0",
      "incomplete_value": true,
      "site": "0058caa0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f8:8"
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
      "definition_site": "0058caf4",
      "incomplete_value": true,
      "site": "0058cb04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f65:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058cab4",
      "incomplete_value": true,
      "site": "0058cac4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb2:8"
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
      "0058cad4",
      "READ",
      [
        "storage",
        "002a67f8",
        null,
        "string"
      ]
    ],
    [
      "0058caf4",
      "READ",
      [
        "storage",
        "002a0fb2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058cad4",
      "READ",
      [
        "storage",
        "002a679c",
        null,
        "string"
      ]
    ],
    [
      "0058caf4",
      "READ",
      [
        "storage",
        "002a0f65",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058ca70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058ca4c.md#insn-0058ca70) · [`0058ca78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058ca4c.md#insn-0058ca78) · [`0058ca90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058ca4c.md#insn-0058ca90)
- 新版 `0058cab0`（命令位置の公開資料なし） · `0058cab8`（命令位置の公開資料なし） · `0058cad0`（命令位置の公開資料なし）

~~~diff
- 0058ca70 ["INT_ADD", "register:40f0:8", ["const:58ca70:8", "const:4:8"]]
- 0058ca70 ["CALL", null, ["callee:00588eac:8"]]
+ 0058cab0 ["INT_ADD", "register:40f0:8", ["const:58cab0:8", "const:4:8"]]
+ 0058cab0 ["CALL", null, ["callee:00588eac:8"]]
- 0058ca70 bytes fff0ff97
+ 0058cab0 bytes fff0ff97
- 0058ca78 ["INT_ADD", "register:40f0:8", ["const:58ca78:8", "const:4:8"]]
- 0058ca78 ["CALL", null, ["callee:0058919c:8"]]
+ 0058cab8 ["INT_ADD", "register:40f0:8", ["const:58cab8:8", "const:4:8"]]
+ 0058cab8 ["CALL", null, ["callee:0058919c:8"]]
- 0058ca78 bytes b9f1ff97
+ 0058cab8 bytes b9f1ff97
- 0058ca90 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 0058ca90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058ca90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058ca90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058cad0 ["COPY", "tmp:0:8", ["const:79c:8"]]
+ 0058cad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058cad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058cad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058ca90 bytes 08e11f91
+ 0058cad0 bytes 08711e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40d550c7daef6add47d4275c4aa5fc89"></a>

### [`0058ccb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058ccb0.md) → [`0058ccf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058ccf0.md) FUN_0058ccf0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597654.md) · 呼出先 13件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00597694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597694.md) · 呼出先 13件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.79% / 新版 93.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058cd7c",
      "incomplete_value": true,
      "site": "0058cd84",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:fc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058cd3c",
      "incomplete_value": true,
      "site": "0058cd44",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:f80:8"
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
      "definition_site": "0058cd78",
      "incomplete_value": true,
      "site": "0058cd88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5c2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058cd38",
      "incomplete_value": true,
      "site": "0058cd48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:61e:8"
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
      "definition_site": "0058cd78",
      "incomplete_value": true,
      "site": "0058cd88",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058cd38",
      "incomplete_value": true,
      "site": "0058cd48",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058cd78",
      "READ",
      [
        "storage",
        "002ab61e",
        null,
        "string"
      ]
    ],
    [
      "0058cd78",
      "READ",
      [
        "storage",
        "002ab62e",
        null,
        "string"
      ]
    ],
    [
      "0058cd7c",
      "READ",
      [
        "storage",
        "002c2f80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058cd78",
      "READ",
      [
        "storage",
        "002ab5c2",
        null,
        "string"
      ]
    ],
    [
      "0058cd78",
      "READ",
      [
        "storage",
        "002ab5d2",
        null,
        "string"
      ]
    ],
    [
      "0058cd7c",
      "READ",
      [
        "storage",
        "002c2fc0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058cd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058ccb0.md#insn-0058cd94) · [`0058ce14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058ccb0.md#insn-0058ce14) · [`0058ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058ccb0.md#insn-0058ccf8)
- 新版 `0058cdd4`（命令位置の公開資料なし） · `0058ce54`（命令位置の公開資料なし） · `0058cd38`（命令位置の公開資料なし）

~~~diff
- 0058cd94 ["INT_ADD", "register:40f0:8", ["const:58cd94:8", "const:4:8"]]
- 0058cd94 ["CALL", null, ["callee:00589184:8"]]
+ 0058cdd4 ["INT_ADD", "register:40f0:8", ["const:58cdd4:8", "const:4:8"]]
+ 0058cdd4 ["CALL", null, ["callee:00589184:8"]]
- 0058cd94 bytes ecf0ff97
+ 0058cdd4 bytes ecf0ff97
- 0058ce14 ["INT_ADD", "register:40f0:8", ["const:58ce14:8", "const:4:8"]]
- 0058ce14 ["CALL", null, ["callee:0058f474:8"]]
+ 0058ce54 ["INT_ADD", "register:40f0:8", ["const:58ce54:8", "const:4:8"]]
+ 0058ce54 ["CALL", null, ["callee:0058f474:8"]]
- 0058ce14 bytes 88090094
+ 0058ce54 bytes 88090094
- 0058ccf8 ["INT_ADD", "register:40f0:8", ["const:58ccf8:8", "const:4:8"]]
- 0058ccf8 ["CALL", null, ["callee:00588eac:8"]]
+ 0058cd38 ["INT_ADD", "register:40f0:8", ["const:58cd38:8", "const:4:8"]]
+ 0058cd38 ["CALL", null, ["callee:00588eac:8"]]
- 0058ccf8 bytes 5df0ff97
+ 0058cd38 bytes 5df0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fdf3b6ce66db4fdd7b51a21bb178621"></a>

### [`0058cf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058cf58.md) → [`0058cf98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058c/0058cf98.md) FUN_0058cf98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00597658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597658.md) · 呼出先 12件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00597698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597698.md) · 呼出先 12件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

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
      "definition_site": "0058cfec",
      "incomplete_value": true,
      "site": "0058cfec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:28c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058cfac",
      "incomplete_value": true,
      "site": "0058cfac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d9:8"
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
      "definition_site": "0058cff8",
      "incomplete_value": true,
      "site": "0058d008",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:48d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058cfb8",
      "incomplete_value": true,
      "site": "0058cfc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e1:8"
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
      "definition_site": "0058d00c",
      "incomplete_value": true,
      "site": "0058d00c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058cfcc",
      "incomplete_value": true,
      "site": "0058cfcc",
      "value": [
        "LOAD",
        "8",
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
      "0058cfd8",
      "READ",
      [
        "storage",
        "002a12d9",
        null,
        "string"
      ]
    ],
    [
      "0058cff8",
      "READ",
      [
        "storage",
        "002bb4e1",
        null,
        "string"
      ]
    ],
    [
      "0058d000",
      "READ",
      [
        "storage",
        "002bb4ee",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058cfd8",
      "READ",
      [
        "storage",
        "002a128c",
        null,
        "string"
      ]
    ],
    [
      "0058cff8",
      "READ",
      [
        "storage",
        "002bb48d",
        null,
        "string"
      ]
    ],
    [
      "0058d000",
      "READ",
      [
        "storage",
        "002bb49a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058cf88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058cf58.md#insn-0058cf88) · [`0058d008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058cf58.md#insn-0058d008) · [`0058d088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058c/0058cf58.md#insn-0058d088)
- 新版 `0058cfc8`（命令位置の公開資料なし） · `0058d048`（命令位置の公開資料なし） · `0058d0c8`（命令位置の公開資料なし）

~~~diff
- 0058cf88 ["INT_ADD", "register:40f0:8", ["const:58cf88:8", "const:4:8"]]
- 0058cf88 ["CALL", null, ["callee:0058919c:8"]]
+ 0058cfc8 ["INT_ADD", "register:40f0:8", ["const:58cfc8:8", "const:4:8"]]
+ 0058cfc8 ["CALL", null, ["callee:0058919c:8"]]
- 0058cf88 bytes 75f0ff97
+ 0058cfc8 bytes 75f0ff97
- 0058d008 ["INT_ADD", "register:40f0:8", ["const:58d008:8", "const:4:8"]]
- 0058d008 ["CALL", null, ["callee:00589184:8"]]
+ 0058d048 ["INT_ADD", "register:40f0:8", ["const:58d048:8", "const:4:8"]]
+ 0058d048 ["CALL", null, ["callee:00589184:8"]]
- 0058d008 bytes 4ff0ff97
+ 0058d048 bytes 4ff0ff97
- 0058d088 ["INT_ADD", "register:40f0:8", ["const:58d088:8", "const:4:8"]]
- 0058d088 ["CALL", null, ["callee:0058f474:8"]]
+ 0058d0c8 ["INT_ADD", "register:40f0:8", ["const:58d0c8:8", "const:4:8"]]
+ 0058d0c8 ["CALL", null, ["callee:0058f474:8"]]
- 0058d088 bytes eb080094
+ 0058d0c8 bytes eb080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b228aedfd6274a5bbb6af46f8a3049d4"></a>

### [`0058d170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d170.md) → [`0058d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d1b0.md) FUN_0058d1b0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058ecc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058ecc0.md) · 呼出先 15件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589168.md)
- 新版 呼出元 1件 [`0058ed00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058ed00.md) · 呼出先 15件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`005891a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/005891a8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.97% / 新版 92.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d22c",
      "incomplete_value": true,
      "site": "0058d244",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:96e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d1ec",
      "incomplete_value": true,
      "site": "0058d204",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9ca:8"
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
      "definition_site": "0058d264",
      "incomplete_value": true,
      "site": "0058d26c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d224",
      "incomplete_value": true,
      "site": "0058d22c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:ba0:8"
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
      "definition_site": "0058d36c",
      "incomplete_value": true,
      "site": "0058d36c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:18d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d32c",
      "incomplete_value": true,
      "site": "0058d32c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1da:8"
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
      "0058d1ec",
      "DATA",
      [
        "storage",
        "00c6cf38",
        null,
        "undefined *"
      ]
    ],
    [
      "0058d22c",
      "READ",
      [
        "storage",
        "002a79ca",
        null,
        "string"
      ]
    ],
    [
      "0058d260",
      "READ",
      [
        "storage",
        "002a12e3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058d1ec",
      "DATA",
      [
        "storage",
        "00c6d008",
        null,
        "undefined *"
      ]
    ],
    [
      "0058d22c",
      "READ",
      [
        "storage",
        "002a796e",
        null,
        "string"
      ]
    ],
    [
      "0058d260",
      "READ",
      [
        "storage",
        "002a1296",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058d26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d170.md#insn-0058d26c) · [`0058d440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d170.md#insn-0058d440) · [`0058d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d170.md#insn-0058d190)
- 新版 `0058d2ac`（命令位置の公開資料なし） · `0058d480`（命令位置の公開資料なし） · `0058d1d0`（命令位置の公開資料なし）

~~~diff
- 0058d26c ["INT_ADD", "register:40f0:8", ["const:58d26c:8", "const:4:8"]]
- 0058d26c ["CALL", null, ["callee:00c57f80:8"]]
+ 0058d2ac ["INT_ADD", "register:40f0:8", ["const:58d2ac:8", "const:4:8"]]
+ 0058d2ac ["CALL", null, ["callee:00c57f80:8"]]
- 0058d26c bytes 112b1b94
+ 0058d2ac bytes 352b1b94
- 0058d440 ["INT_ADD", "register:40f0:8", ["const:58d440:8", "const:4:8"]]
- 0058d440 ["CALL", null, ["callee:00589880:8"]]
+ 0058d480 ["INT_ADD", "register:40f0:8", ["const:58d480:8", "const:4:8"]]
+ 0058d480 ["CALL", null, ["callee:00589880:8"]]
- 0058d440 bytes 00f1ff97
+ 0058d480 bytes 00f1ff97
- 0058d190 ["COPY", "register:4048:8", ["const:c6c000:8"]]
+ 0058d1d0 ["COPY", "register:4048:8", ["const:c6d000:8"]]
- 0058d190 bytes e93600f0
+ 0058d1d0 bytes 09370090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ded7bb253c59b0baf784e620d6f496c"></a>

### [`0058d604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d604.md) → [`0058d644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d644.md) FUN_0058d644

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058d6b8",
      "incomplete_value": true,
      "site": "0058d6c0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:960:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d678",
      "incomplete_value": true,
      "site": "0058d680",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:920:8"
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
      "definition_site": "0058d6b4",
      "incomplete_value": true,
      "site": "0058d6c4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:fc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d674",
      "incomplete_value": true,
      "site": "0058d684",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:f88:8"
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
      "definition_site": "0058d6b4",
      "incomplete_value": true,
      "site": "0058d6c4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0058d674",
      "incomplete_value": true,
      "site": "0058d684",
      "value": [
        "LOAD",
        "16",
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
      "0058d6b4",
      "READ",
      [
        "storage",
        "002bff88",
        null,
        "string"
      ]
    ],
    [
      "0058d6b4",
      "READ",
      [
        "storage",
        "002bff98",
        null,
        "string"
      ]
    ],
    [
      "0058d6b8",
      "READ",
      [
        "storage",
        "002c2920",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058d6b4",
      "READ",
      [
        "storage",
        "002bffc8",
        null,
        "string"
      ]
    ],
    [
      "0058d6b4",
      "READ",
      [
        "storage",
        "002bffd8",
        null,
        "string"
      ]
    ],
    [
      "0058d6b8",
      "READ",
      [
        "storage",
        "002c2960",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058d6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d604.md#insn-0058d6c0) · [`0058d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d604.md#insn-0058d630) · [`0058d638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d604.md#insn-0058d638)
- 新版 `0058d700`（命令位置の公開資料なし） · `0058d670`（命令位置の公開資料なし） · `0058d678`（命令位置の公開資料なし）

~~~diff
- 0058d6c0 ["INT_ADD", "register:40f0:8", ["const:58d6c0:8", "const:4:8"]]
- 0058d6c0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058d700 ["INT_ADD", "register:40f0:8", ["const:58d700:8", "const:4:8"]]
+ 0058d700 ["CALL", null, ["callee:00c57f80:8"]]
- 0058d6c0 bytes fc291b94
+ 0058d700 bytes 202a1b94
- 0058d630 ["INT_ADD", "register:40f0:8", ["const:58d630:8", "const:4:8"]]
- 0058d630 ["CALL", null, ["callee:00589880:8"]]
+ 0058d670 ["INT_ADD", "register:40f0:8", ["const:58d670:8", "const:4:8"]]
+ 0058d670 ["CALL", null, ["callee:00589880:8"]]
- 0058d630 bytes 84f0ff97
+ 0058d670 bytes 84f0ff97
- 0058d638 ["INT_ADD", "register:40f0:8", ["const:58d638:8", "const:4:8"]]
- 0058d638 ["CALL", null, ["callee:00588eac:8"]]
+ 0058d678 ["INT_ADD", "register:40f0:8", ["const:58d678:8", "const:4:8"]]
+ 0058d678 ["CALL", null, ["callee:00588eac:8"]]
- 0058d638 bytes 0deeff97
+ 0058d678 bytes 0deeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d983a704e21380d6eecdaf65c49117d9"></a>

### [`0058d7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d7d8.md) → [`0058d818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d818.md) FUN_0058d818

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)

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
      "definition_site": "0058d874",
      "incomplete_value": true,
      "site": "0058d874",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058d834",
      "incomplete_value": true,
      "site": "0058d834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:91e:8"
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
      "0058d868",
      "READ",
      [
        "storage",
        "002ad91e",
        null,
        "string"
      ]
    ],
    [
      "0058d888",
      "READ",
      [
        "storage",
        "002afb48",
        null,
        "string"
      ]
    ],
    [
      "0058d88c",
      "READ",
      [
        "storage",
        "002afb56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058d868",
      "READ",
      [
        "storage",
        "002ad8c2",
        null,
        "string"
      ]
    ],
    [
      "0058d888",
      "READ",
      [
        "storage",
        "002afaec",
        null,
        "string"
      ]
    ],
    [
      "0058d88c",
      "READ",
      [
        "storage",
        "002afafa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058d804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d7d8.md#insn-0058d804) · [`0058d80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d7d8.md#insn-0058d80c) · [`0058d824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d7d8.md#insn-0058d824)
- 新版 `0058d844`（命令位置の公開資料なし） · `0058d84c`（命令位置の公開資料なし） · `0058d864`（命令位置の公開資料なし）

~~~diff
- 0058d804 ["INT_ADD", "register:40f0:8", ["const:58d804:8", "const:4:8"]]
- 0058d804 ["CALL", null, ["callee:00589880:8"]]
+ 0058d844 ["INT_ADD", "register:40f0:8", ["const:58d844:8", "const:4:8"]]
+ 0058d844 ["CALL", null, ["callee:00589880:8"]]
- 0058d804 bytes 0ff0ff97
+ 0058d844 bytes 0ff0ff97
- 0058d80c ["INT_ADD", "register:40f0:8", ["const:58d80c:8", "const:4:8"]]
- 0058d80c ["CALL", null, ["callee:00588eac:8"]]
+ 0058d84c ["INT_ADD", "register:40f0:8", ["const:58d84c:8", "const:4:8"]]
+ 0058d84c ["CALL", null, ["callee:00588eac:8"]]
- 0058d80c bytes 98edff97
+ 0058d84c bytes 98edff97
- 0058d824 ["COPY", "tmp:0:8", ["const:91e:8"]]
- 0058d824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0058d824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0058d824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0058d864 ["COPY", "tmp:0:8", ["const:8c2:8"]]
+ 0058d864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0058d864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0058d864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0058d824 bytes 08792491
+ 0058d864 bytes 08092391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09f4981a7690b8c1d0d7f6f65837b0e9"></a>

### [`0058d9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d9b0.md) → [`0058d9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058d9f0.md) FUN_0058d9f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0057be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057be0c.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0057be4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057be4c.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)

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
      "definition_site": "0058da64",
      "incomplete_value": true,
      "site": "0058da70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058da24",
      "incomplete_value": true,
      "site": "0058da30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:547:8"
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
      "definition_site": "0058da74",
      "incomplete_value": true,
      "site": "0058da74",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058da34",
      "incomplete_value": true,
      "site": "0058da34",
      "value": [
        "LOAD",
        "8",
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
      "0058da64",
      "READ",
      [
        "storage",
        "002bb547",
        null,
        "string"
      ]
    ],
    [
      "0058da68",
      "READ",
      [
        "storage",
        "002bb555",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058da64",
      "READ",
      [
        "storage",
        "002bb4f3",
        null,
        "string"
      ]
    ],
    [
      "0058da68",
      "READ",
      [
        "storage",
        "002bb501",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058da74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d9b0.md#insn-0058da74) · [`0058d9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d9b0.md#insn-0058d9e0) · [`0058d9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058d9b0.md#insn-0058d9ec)
- 新版 `0058dab4`（命令位置の公開資料なし） · `0058da20`（命令位置の公開資料なし） · `0058da2c`（命令位置の公開資料なし）

~~~diff
- 0058da74 ["INT_ADD", "register:40f0:8", ["const:58da74:8", "const:4:8"]]
- 0058da74 ["CALL", null, ["callee:00589184:8"]]
+ 0058dab4 ["INT_ADD", "register:40f0:8", ["const:58dab4:8", "const:4:8"]]
+ 0058dab4 ["CALL", null, ["callee:00589184:8"]]
- 0058da74 bytes b4edff97
+ 0058dab4 bytes b4edff97
- 0058d9e0 ["INT_ADD", "register:40f0:8", ["const:58d9e0:8", "const:4:8"]]
- 0058d9e0 ["CALL", null, ["callee:00589880:8"]]
+ 0058da20 ["INT_ADD", "register:40f0:8", ["const:58da20:8", "const:4:8"]]
+ 0058da20 ["CALL", null, ["callee:00589880:8"]]
- 0058d9e0 bytes 98efff97
+ 0058da20 bytes 98efff97
- 0058d9ec ["INT_ADD", "register:40f0:8", ["const:58d9ec:8", "const:4:8"]]
- 0058d9ec ["CALL", null, ["callee:00588eac:8"]]
+ 0058da2c ["INT_ADD", "register:40f0:8", ["const:58da2c:8", "const:4:8"]]
+ 0058da2c ["CALL", null, ["callee:00588eac:8"]]
- 0058d9ec bytes 20edff97
+ 0058da2c bytes 20edff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-837c26f00b503fcfc415d2f2159ff8ce"></a>

### [`0058db8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058db8c.md) → [`0058dbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058dbcc.md) FUN_0058dbcc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md) [`00589850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589850.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md) [`00589890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589890.md)

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
      "definition_site": "0058dc40",
      "incomplete_value": true,
      "site": "0058dc48",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:3c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058dc00",
      "incomplete_value": true,
      "site": "0058dc08",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:40d:8"
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
      "definition_site": "0058dc4c",
      "incomplete_value": true,
      "site": "0058dc4c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058dc0c",
      "incomplete_value": true,
      "site": "0058dc0c",
      "value": [
        "LOAD",
        "8",
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
      "0058dc40",
      "READ",
      [
        "storage",
        "002a440d",
        null,
        "string"
      ]
    ],
    [
      "0058dc44",
      "READ",
      [
        "storage",
        "002a441b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058dc40",
      "READ",
      [
        "storage",
        "002a43c0",
        null,
        "string"
      ]
    ],
    [
      "0058dc44",
      "READ",
      [
        "storage",
        "002a43ce",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058dc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058db8c.md#insn-0058dc4c) · [`0058dbb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058db8c.md#insn-0058dbb8) · [`0058dbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058db8c.md#insn-0058dbc0)
- 新版 `0058dc8c`（命令位置の公開資料なし） · `0058dbf8`（命令位置の公開資料なし） · `0058dc00`（命令位置の公開資料なし）

~~~diff
- 0058dc4c ["INT_ADD", "register:40f0:8", ["const:58dc4c:8", "const:4:8"]]
- 0058dc4c ["CALL", null, ["callee:00589184:8"]]
+ 0058dc8c ["INT_ADD", "register:40f0:8", ["const:58dc8c:8", "const:4:8"]]
+ 0058dc8c ["CALL", null, ["callee:00589184:8"]]
- 0058dc4c bytes 3eedff97
+ 0058dc8c bytes 3eedff97
- 0058dbb8 ["INT_ADD", "register:40f0:8", ["const:58dbb8:8", "const:4:8"]]
- 0058dbb8 ["CALL", null, ["callee:00589880:8"]]
+ 0058dbf8 ["INT_ADD", "register:40f0:8", ["const:58dbf8:8", "const:4:8"]]
+ 0058dbf8 ["CALL", null, ["callee:00589880:8"]]
- 0058dbb8 bytes 22efff97
+ 0058dbf8 bytes 22efff97
- 0058dbc0 ["INT_ADD", "register:40f0:8", ["const:58dbc0:8", "const:4:8"]]
- 0058dbc0 ["CALL", null, ["callee:00588eac:8"]]
+ 0058dc00 ["INT_ADD", "register:40f0:8", ["const:58dc00:8", "const:4:8"]]
+ 0058dc00 ["CALL", null, ["callee:00588eac:8"]]
- 0058dbc0 bytes abecff97
+ 0058dc00 bytes abecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95f5421fc2d6d8228220e93f027d5480"></a>

### [`0058dd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058dd60.md) → [`0058dda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058dda0.md) FUN_0058dda0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)
- 新版 呼出元 0件  · 呼出先 11件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)

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
      "definition_site": "0058de10",
      "incomplete_value": true,
      "site": "0058de18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:983:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058ddd0",
      "incomplete_value": true,
      "site": "0058ddd8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:9df:8"
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
      "definition_site": "0058de1c",
      "incomplete_value": true,
      "site": "0058de1c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0058dddc",
      "incomplete_value": true,
      "site": "0058dddc",
      "value": [
        "LOAD",
        "8",
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
      "0058de10",
      "READ",
      [
        "storage",
        "002a79df",
        null,
        "string"
      ]
    ],
    [
      "0058de14",
      "READ",
      [
        "storage",
        "002a79ed",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058de10",
      "READ",
      [
        "storage",
        "002a7983",
        null,
        "string"
      ]
    ],
    [
      "0058de14",
      "READ",
      [
        "storage",
        "002a7991",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058de1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058dd60.md#insn-0058de1c) · [`0058dd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058dd60.md#insn-0058dd8c) · [`0058dd94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058dd60.md#insn-0058dd94)
- 新版 `0058de5c`（命令位置の公開資料なし） · `0058ddcc`（命令位置の公開資料なし） · `0058ddd4`（命令位置の公開資料なし）

~~~diff
- 0058de1c ["INT_ADD", "register:40f0:8", ["const:58de1c:8", "const:4:8"]]
- 0058de1c ["CALL", null, ["callee:00589184:8"]]
+ 0058de5c ["INT_ADD", "register:40f0:8", ["const:58de5c:8", "const:4:8"]]
+ 0058de5c ["CALL", null, ["callee:00589184:8"]]
- 0058de1c bytes caecff97
+ 0058de5c bytes caecff97
- 0058dd8c ["INT_ADD", "register:40f0:8", ["const:58dd8c:8", "const:4:8"]]
- 0058dd8c ["CALL", null, ["callee:00589880:8"]]
+ 0058ddcc ["INT_ADD", "register:40f0:8", ["const:58ddcc:8", "const:4:8"]]
+ 0058ddcc ["CALL", null, ["callee:00589880:8"]]
- 0058dd8c bytes adeeff97
+ 0058ddcc bytes adeeff97
- 0058dd94 ["INT_ADD", "register:40f0:8", ["const:58dd94:8", "const:4:8"]]
- 0058dd94 ["CALL", null, ["callee:00588eac:8"]]
+ 0058ddd4 ["INT_ADD", "register:40f0:8", ["const:58ddd4:8", "const:4:8"]]
+ 0058ddd4 ["CALL", null, ["callee:00588eac:8"]]
- 0058dd94 bytes 36ecff97
+ 0058ddd4 bytes 36ecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a16edda79cdc5fc71483e786c27c1d7"></a>

### [`0058df30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058df30.md) → [`0058df70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058d/0058df70.md) FUN_0058df70

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.43% / 新版 89.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058dfcc",
      "incomplete_value": true,
      "site": "0058dfcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:99a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058df8c",
      "incomplete_value": true,
      "site": "0058df8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f6:8"
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
      "definition_site": "0058dfec",
      "incomplete_value": true,
      "site": "0058dff4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058dfac",
      "incomplete_value": true,
      "site": "0058dfb4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058dfe8",
      "incomplete_value": true,
      "site": "0058dff8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058dfa8",
      "incomplete_value": true,
      "site": "0058dfb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:943:8"
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
      "0058dfbc",
      "READ",
      [
        "storage",
        "002a79f6",
        null,
        "string"
      ]
    ],
    [
      "0058dfe8",
      "READ",
      [
        "storage",
        "002ac943",
        null,
        "string"
      ]
    ],
    [
      "0058dfe8",
      "READ",
      [
        "storage",
        "002ac953",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058dfbc",
      "READ",
      [
        "storage",
        "002a799a",
        null,
        "string"
      ]
    ],
    [
      "0058dfe8",
      "READ",
      [
        "storage",
        "002ac8e7",
        null,
        "string"
      ]
    ],
    [
      "0058dfe8",
      "READ",
      [
        "storage",
        "002ac8f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058df74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058df30.md#insn-0058df74) · [`0058dff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058df30.md#insn-0058dff4) · [`0058e00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058d/0058df30.md#insn-0058e00c)
- 新版 `0058dfb4`（命令位置の公開資料なし） · `0058e034`（命令位置の公開資料なし） · `0058e04c`（命令位置の公開資料なし）

~~~diff
- 0058df74 ["COPY", "tmp:0:8", ["const:9f6:8"]]
- 0058df74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058df74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058df74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058dfb4 ["COPY", "tmp:0:8", ["const:99a:8"]]
+ 0058dfb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058dfb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058dfb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058df74 bytes 29d92791
+ 0058dfb4 bytes 29692691
- 0058dff4 ["INT_ADD", "register:40f0:8", ["const:58dff4:8", "const:4:8"]]
- 0058dff4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058e034 ["INT_ADD", "register:40f0:8", ["const:58e034:8", "const:4:8"]]
+ 0058e034 ["CALL", null, ["callee:00c57f80:8"]]
- 0058dff4 bytes af271b94
+ 0058e034 bytes d3271b94
- 0058e00c ["INT_ADD", "register:40f0:8", ["const:58e00c:8", "const:4:8"]]
- 0058e00c ["CALL", null, ["callee:00589184:8"]]
+ 0058e04c ["INT_ADD", "register:40f0:8", ["const:58e04c:8", "const:4:8"]]
+ 0058e04c ["CALL", null, ["callee:00589184:8"]]
- 0058e00c bytes 4eecff97
+ 0058e04c bytes 4eecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-328cb805b7e5e0873626b0d9ed96d003"></a>

### [`0058e190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e190.md) → [`0058e1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e1d0.md) FUN_0058e1d0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.13% / 新版 87.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0058e234",
      "incomplete_value": true,
      "site": "0058e234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8cd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e1f4",
      "incomplete_value": true,
      "site": "0058e1f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:929:8"
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
      "definition_site": "0058e250",
      "incomplete_value": true,
      "site": "0058e258",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:3e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e210",
      "incomplete_value": true,
      "site": "0058e218",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c2000:8"
              ],
              [
                "leaf",
                "const:3a0:8"
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
      "definition_site": "0058e24c",
      "incomplete_value": true,
      "site": "0058e25c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f93:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0058e20c",
      "incomplete_value": true,
      "site": "0058e21c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f62:8"
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
      "0058e220",
      "READ",
      [
        "storage",
        "002ad929",
        null,
        "string"
      ]
    ],
    [
      "0058e24c",
      "READ",
      [
        "storage",
        "002b4f62",
        null,
        "string"
      ]
    ],
    [
      "0058e24c",
      "READ",
      [
        "storage",
        "002b4f72",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0058e220",
      "READ",
      [
        "storage",
        "002ad8cd",
        null,
        "string"
      ]
    ],
    [
      "0058e24c",
      "READ",
      [
        "storage",
        "002b4f93",
        null,
        "string"
      ]
    ],
    [
      "0058e24c",
      "READ",
      [
        "storage",
        "002b4fa3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e190.md#insn-0058e1d8) · [`0058e258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e190.md#insn-0058e258) · [`0058e270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e190.md#insn-0058e270)
- 新版 `0058e218`（命令位置の公開資料なし） · `0058e298`（命令位置の公開資料なし） · `0058e2b0`（命令位置の公開資料なし）

~~~diff
- 0058e1d8 ["COPY", "tmp:0:8", ["const:929:8"]]
- 0058e1d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0058e1d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0058e1d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0058e218 ["COPY", "tmp:0:8", ["const:8cd:8"]]
+ 0058e218 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0058e218 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0058e218 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0058e1d8 bytes 29a52491
+ 0058e218 bytes 29352391
- 0058e258 ["INT_ADD", "register:40f0:8", ["const:58e258:8", "const:4:8"]]
- 0058e258 ["CALL", null, ["callee:00c57f80:8"]]
+ 0058e298 ["INT_ADD", "register:40f0:8", ["const:58e298:8", "const:4:8"]]
+ 0058e298 ["CALL", null, ["callee:00c57f80:8"]]
- 0058e258 bytes 16271b94
+ 0058e298 bytes 3a271b94
- 0058e270 ["INT_ADD", "register:40f0:8", ["const:58e270:8", "const:4:8"]]
- 0058e270 ["CALL", null, ["callee:00589184:8"]]
+ 0058e2b0 ["INT_ADD", "register:40f0:8", ["const:58e2b0:8", "const:4:8"]]
+ 0058e2b0 ["CALL", null, ["callee:00589184:8"]]
- 0058e270 bytes b5ebff97
+ 0058e2b0 bytes b5ebff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

