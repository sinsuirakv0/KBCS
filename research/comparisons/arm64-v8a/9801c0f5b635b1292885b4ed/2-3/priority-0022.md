# v16.0.1 → v16.0.2 · 最優先の変更候補 (22)

[一覧の目次](README.md)

<a id="compare-4780df5e4b468996107095302fd5d424"></a>

### [`005a8788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8788.md) → [`005a87c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a87c8.md) FUN_005a87c8

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
      "definition_site": "005a87e4",
      "incomplete_value": false,
      "site": "005a87ec",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a87a4",
      "incomplete_value": false,
      "site": "005a87ac",
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
            "const:60:8"
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
      "definition_site": "005a87fc",
      "incomplete_value": false,
      "site": "005a87fc",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a87bc",
      "incomplete_value": false,
      "site": "005a87bc",
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
            "const:fb0:8"
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
      "005a87ec",
      "DATA",
      [
        "storage",
        "00c6f060",
        null,
        "undefined *"
      ]
    ],
    [
      "005a87fc",
      "DATA",
      [
        "storage",
        "00c6efb0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a87ec",
      "DATA",
      [
        "storage",
        "00c6f130",
        null,
        "undefined *"
      ]
    ],
    [
      "005a87fc",
      "DATA",
      [
        "storage",
        "00c6f080",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a879c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8788.md#insn-005a879c) · [`005a87a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8788.md#insn-005a87a4) · [`005a87b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8788.md#insn-005a87b0)
- 新版 `005a87dc`（命令位置の公開資料なし） · `005a87e4`（命令位置の公開資料なし）

~~~diff
- 005a879c ["INT_ADD", "register:40f0:8", ["const:5a879c:8", "const:4:8"]]
- 005a879c ["CALL", null, ["callee:00c57f60:8"]]
+ 005a87dc ["INT_ADD", "register:40f0:8", ["const:5a87dc:8", "const:4:8"]]
+ 005a87dc ["CALL", null, ["callee:00c57f60:8"]]
- 005a879c bytes bdbd1a94
+ 005a87dc bytes e1bd1a94
- 005a87a4 ["COPY", "tmp:0:8", ["const:60:8"]]
- 005a87a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a87a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a87a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a87e4 ["COPY", "tmp:0:8", ["const:130:8"]]
+ 005a87e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a87e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a87e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a87a4 bytes 08810191
+ 005a87e4 bytes 08c10491
- 005a87b0 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 005a87b0 bytes 283600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c382c1ff806dcb4cf75e7db821d3e98"></a>

### [`005a87d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a87d0.md) → [`005a8810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8810.md) FUN_005a8810

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
      "definition_site": "005a882c",
      "incomplete_value": true,
      "site": "005a8830",
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
      "definition_site": "005a87ec",
      "incomplete_value": true,
      "site": "005a87f0",
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
      "005a8824",
      "READ",
      [
        "storage",
        "00c9b320",
        null,
        "pointer"
      ]
    ],
    [
      "005a8830",
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
      "005a8824",
      "READ",
      [
        "storage",
        "00c9b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "005a8830",
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

- 旧版 [`005a87e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a87d0.md#insn-005a87e4) · [`005a87fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a87d0.md#insn-005a87fc) · [`005a880c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a87d0.md#insn-005a880c)
- 新版 `005a8824`（命令位置の公開資料なし） · `005a883c`（命令位置の公開資料なし） · `005a884c`（命令位置の公開資料なし）

~~~diff
- 005a87e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
- 005a87e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005a8824 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3f0:8"]]
+ 005a8824 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005a87e4 bytes 089141f9
+ 005a8824 bytes 08f941f9
- 005a87fc ["INT_ADD", "register:40f0:8", ["const:5a87fc:8", "const:4:8"]]
- 005a87fc ["CALL", null, ["callee:00c57f80:8"]]
+ 005a883c ["INT_ADD", "register:40f0:8", ["const:5a883c:8", "const:4:8"]]
+ 005a883c ["CALL", null, ["callee:00c57f80:8"]]
- 005a87fc bytes adbd1a94
+ 005a883c bytes d1bd1a94
- 005a880c ["INT_ADD", "register:40f0:8", ["const:5a880c:8", "const:4:8"]]
- 005a880c ["CALL", null, ["callee:00c57f80:8"]]
+ 005a884c ["INT_ADD", "register:40f0:8", ["const:5a884c:8", "const:4:8"]]
+ 005a884c ["CALL", null, ["callee:00c57f80:8"]]
- 005a880c bytes a9bd1a94
+ 005a884c bytes cdbd1a94
~~~


<a id="compare-234b23c631887f2ad7e0171426373c44"></a>

### [`005a8820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8820.md) → [`005a8860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8860.md) FUN_005a8860

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
      "definition_site": "005a8868",
      "incomplete_value": false,
      "site": "005a886c",
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
      "definition_site": "005a8828",
      "incomplete_value": false,
      "site": "005a882c",
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
      "005a886c",
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
      "005a886c",
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

- 旧版 [`005a8828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8820.md#insn-005a8828) · [`005a884c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8820.md#insn-005a884c)
- 新版 `005a8868`（命令位置の公開資料なし） · `005a888c`（命令位置の公開資料なし）

~~~diff
- 005a8828 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a8828 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a8828 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a8828 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a8868 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a8868 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a8868 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a8868 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a8828 bytes 29012891
+ 005a8868 bytes 29412b91
- 005a884c ["INT_ADD", "register:40f0:8", ["const:5a884c:8", "const:4:8"]]
- 005a884c ["CALL", null, ["callee:00c57f80:8"]]
+ 005a888c ["INT_ADD", "register:40f0:8", ["const:5a888c:8", "const:4:8"]]
+ 005a888c ["CALL", null, ["callee:00c57f80:8"]]
- 005a884c bytes 99bd1a94
+ 005a888c bytes bdbd1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92159516224b126ea1f64d97e331a726"></a>

### [`005a88a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a88a0.md) → [`005a88e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a88e0.md) FUN_005a88e0

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
      "definition_site": "005a88e8",
      "incomplete_value": false,
      "site": "005a88ec",
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
      "definition_site": "005a88a8",
      "incomplete_value": false,
      "site": "005a88ac",
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
      "005a88ec",
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
      "005a88ec",
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

- 旧版 [`005a88a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a88a0.md#insn-005a88a8)
- 新版 `005a88e8`（命令位置の公開資料なし）

~~~diff
- 005a88a8 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 005a88a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a88a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a88a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a88e8 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 005a88e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a88e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a88e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a88a8 bytes 29012891
+ 005a88e8 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c38cf4b08983492cd5b91e170ff23dfa"></a>

### [`005a88c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a88c4.md) → [`005a8904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8904.md) FUN_005a8904

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
      "definition_site": "005a8908",
      "incomplete_value": false,
      "site": "005a890c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a88c8",
      "incomplete_value": false,
      "site": "005a88cc",
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
      "005a890c",
      "DATA",
      [
        "storage",
        "00c6f060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a890c",
      "DATA",
      [
        "storage",
        "00c6f130",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a88c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a88c4.md#insn-005a88c8)
- 新版 `005a8908`（命令位置の公開資料なし）

~~~diff
- 005a88c8 ["COPY", "tmp:0:8", ["const:60:8"]]
- 005a88c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a88c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a88c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a8908 ["COPY", "tmp:0:8", ["const:130:8"]]
+ 005a8908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a8908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a8908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a88c8 bytes 08810191
+ 005a8908 bytes 08c10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de988e773c07aae424c9e1c652bc23f4"></a>

### [`005a890c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a890c.md) → [`005a894c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a894c.md) _INIT_54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a89ac",
      "incomplete_value": true,
      "site": "005a89c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a896c",
      "incomplete_value": true,
      "site": "005a8988",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a89cc",
      "incomplete_value": true,
      "site": "005a89e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a898c",
      "incomplete_value": true,
      "site": "005a89a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a89ec",
      "incomplete_value": true,
      "site": "005a8a04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005a89ac",
      "incomplete_value": true,
      "site": "005a89c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005a8988",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005a89ac",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005a89cc",
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
      "005a8988",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005a89ac",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005a89cc",
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

- 旧版 [`005a8984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a890c.md#insn-005a8984) · [`005a89a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a890c.md#insn-005a89a4) · [`005a8b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a890c.md#insn-005a8b40)
- 新版 `005a89c4`（命令位置の公開資料なし） · `005a89e4`（命令位置の公開資料なし） · `005a8b80`（命令位置の公開資料なし）

~~~diff
- 005a8984 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 005a8984 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a8984 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a8984 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a89c4 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 005a89c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a89c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a89c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a8984 bytes 4a093791
+ 005a89c4 bytes 4ab93591
- 005a89a4 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005a89a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005a89a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005a89a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005a89e4 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005a89e4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005a89e4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005a89e4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005a89a4 bytes 4a893d91
+ 005a89e4 bytes 4a553c91
- 005a8b40 ["INT_ADD", "register:40f0:8", ["const:5a8b40:8", "const:4:8"]]
- 005a8b40 ["CALL", null, ["callee:00c57f00:8"]]
+ 005a8b80 ["INT_ADD", "register:40f0:8", ["const:5a8b80:8", "const:4:8"]]
+ 005a8b80 ["CALL", null, ["callee:00c57f00:8"]]
- 005a8b40 bytes bcbc1a94
+ 005a8b80 bytes e0bc1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0812fa037525236f4147ce876df8050b"></a>

### [`005a8c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8c9c.md) → [`005a8cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8cdc.md) FUN_005a8cdc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005a8e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md) · 呼出先 2件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`005a9d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md)
- 新版 呼出元 1件 [`005a8e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8e68.md) · 呼出先 2件 [`0059b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b91c.md) [`005a9d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9d64.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a8d28",
      "incomplete_value": false,
      "site": "005a8d30",
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
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a8ce8",
      "incomplete_value": false,
      "site": "005a8cf0",
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
            "const:b0:8"
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
      "005a8d30",
      "DATA",
      [
        "storage",
        "00c6f0b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005a8d30",
      "DATA",
      [
        "storage",
        "00c6f180",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a8ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8c9c.md#insn-005a8ce0) · [`005a8ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8c9c.md#insn-005a8ce8) · [`005a8d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8c9c.md#insn-005a8d84)
- 新版 `005a8d20`（命令位置の公開資料なし） · `005a8d28`（命令位置の公開資料なし） · `005a8dc4`（命令位置の公開資料なし）

~~~diff
- 005a8ce0 ["INT_ADD", "register:40f0:8", ["const:5a8ce0:8", "const:4:8"]]
- 005a8ce0 ["CALL", null, ["callee:0059b91c:8"]]
+ 005a8d20 ["INT_ADD", "register:40f0:8", ["const:5a8d20:8", "const:4:8"]]
+ 005a8d20 ["CALL", null, ["callee:0059b91c:8"]]
- 005a8ce0 bytes ffcaff97
+ 005a8d20 bytes ffcaff97
- 005a8ce8 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 005a8ce8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a8ce8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a8ce8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a8d28 ["COPY", "tmp:0:8", ["const:180:8"]]
+ 005a8d28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a8d28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a8d28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a8ce8 bytes 08c10291
+ 005a8d28 bytes 08010691
- 005a8d84 ["INT_ADD", "register:40f0:8", ["const:5a8d84:8", "const:4:8"]]
- 005a8d84 ["CALL", null, ["callee:005a9d64:8"]]
+ 005a8dc4 ["INT_ADD", "register:40f0:8", ["const:5a8dc4:8", "const:4:8"]]
+ 005a8dc4 ["CALL", null, ["callee:005a9d64:8"]]
- 005a8d84 bytes e8030094
+ 005a8dc4 bytes e8030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3abb5b513debb5405bdffd42ddbae578"></a>

### [`005a8e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md) → [`005a8e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8e68.md) FUN_005a8e68

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005a8c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8c9c.md) [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md) [`009b3134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3134.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`005a8cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8cdc.md) [`005aa1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1c4.md) [`009b3188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3188.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.51% / 新版 95.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a8ec4",
      "incomplete_value": true,
      "site": "005a8ec4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005a8e84",
      "incomplete_value": true,
      "site": "005a8e84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a905c",
      "incomplete_value": true,
      "site": "005a905c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7bf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a901c",
      "incomplete_value": true,
      "site": "005a901c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:81b:8"
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
      "definition_site": "005a92c0",
      "incomplete_value": true,
      "site": "005a92c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:32f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9280",
      "incomplete_value": true,
      "site": "005a9280",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 76,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005a8eb4",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005a9048",
      "READ",
      [
        "storage",
        "002a681b",
        null,
        "string"
      ]
    ],
    [
      "005a90cc",
      "READ",
      [
        "storage",
        "002a9e65",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a8eb4",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "005a9048",
      "READ",
      [
        "storage",
        "002a67bf",
        null,
        "string"
      ]
    ],
    [
      "005a90cc",
      "READ",
      [
        "storage",
        "002a9e09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a931c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md#insn-005a931c) · [`005a8e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md#insn-005a8e70) · [`005a8e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md#insn-005a8e90)
- 新版 `005a935c`（命令位置の公開資料なし） · `005a8eb0`（命令位置の公開資料なし） · `005a8ed0`（命令位置の公開資料なし）

~~~diff
- 005a931c ["COPY", "tmp:0:8", ["const:475:8"]]
- 005a931c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a931c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a931c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a935c ["COPY", "tmp:0:8", ["const:421:8"]]
+ 005a935c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a935c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a935c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a931c bytes 29d51191
+ 005a935c bytes 29851091
- 005a8e70 ["COPY", "tmp:0:8", ["const:1a5:8"]]
- 005a8e70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005a8e70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005a8e70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005a8eb0 ["COPY", "tmp:0:8", ["const:1e5:8"]]
+ 005a8eb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005a8eb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005a8eb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005a8e70 bytes 29950691
+ 005a8eb0 bytes 29950791
- 005a8e90 ["INT_ADD", "register:40f0:8", ["const:5a8e90:8", "const:4:8"]]
- 005a8e90 ["CALL", null, ["callee:004410cc:8"]]
+ 005a8ed0 ["INT_ADD", "register:40f0:8", ["const:5a8ed0:8", "const:4:8"]]
+ 005a8ed0 ["CALL", null, ["callee:004410cc:8"]]
- 005a8e90 bytes 7f60fa97
+ 005a8ed0 bytes 7f60fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b154f9fd3194af117deef1aaad3e9233"></a>

### [`005a9760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9760.md) → [`005a97a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a97a0.md) FUN_005a97a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009b53bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b53bc.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)
- 新版 呼出元 1件 [`009b5410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5410.md) · 呼出先 1件 [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a97c4",
      "incomplete_value": true,
      "site": "005a97cc",
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
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9784",
      "incomplete_value": true,
      "site": "005a978c",
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
            "const:d0:8"
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
      "005a97cc",
      "DATA",
      [
        "storage",
        "00c6f0d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005a97cc",
      "DATA",
      [
        "storage",
        "00c6f1a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a977c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9760.md#insn-005a977c) · [`005a9784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9760.md#insn-005a9784)
- 新版 `005a97bc`（命令位置の公開資料なし） · `005a97c4`（命令位置の公開資料なし）

~~~diff
- 005a977c ["INT_ADD", "register:40f0:8", ["const:5a977c:8", "const:4:8"]]
- 005a977c ["CALL", null, ["callee:0059b948:8"]]
+ 005a97bc ["INT_ADD", "register:40f0:8", ["const:5a97bc:8", "const:4:8"]]
+ 005a97bc ["CALL", null, ["callee:0059b948:8"]]
- 005a977c bytes 63c8ff97
+ 005a97bc bytes 63c8ff97
- 005a9784 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 005a9784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a9784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a9784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a97c4 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 005a97c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a97c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a97c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a9784 bytes 08410391
+ 005a97c4 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62406d4183297a33f6c28d7223eca0c2"></a>

### [`005a97bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a97bc.md) → [`005a97fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a97fc.md) FUN_005a97fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58020.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005a9834",
      "incomplete_value": false,
      "site": "005a9840",
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
            "const:d2a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a97f4",
      "incomplete_value": false,
      "site": "005a9800",
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
            "const:d86:8"
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
      "definition_site": "005a9860",
      "incomplete_value": false,
      "site": "005a9868",
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
            "const:6c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9820",
      "incomplete_value": false,
      "site": "005a9828",
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
            "const:722:8"
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
      "005a9834",
      "PARAM",
      [
        "storage",
        "002b0d86",
        null,
        "string"
      ]
    ],
    [
      "005a9860",
      "PARAM",
      [
        "storage",
        "002a5722",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a9834",
      "PARAM",
      [
        "storage",
        "002b0d2a",
        null,
        "string"
      ]
    ],
    [
      "005a9860",
      "PARAM",
      [
        "storage",
        "002a56c6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a97bc.md#insn-005a9800) · [`005a9828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a97bc.md#insn-005a9828) · [`005a97ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a97bc.md#insn-005a97ec)
- 新版 `005a9840`（命令位置の公開資料なし） · `005a9868`（命令位置の公開資料なし） · `005a982c`（命令位置の公開資料なし）

~~~diff
- 005a9800 ["INT_ADD", "register:40f0:8", ["const:5a9800:8", "const:4:8"]]
- 005a9800 ["CALL", null, ["callee:00c58030:8"]]
+ 005a9840 ["INT_ADD", "register:40f0:8", ["const:5a9840:8", "const:4:8"]]
+ 005a9840 ["CALL", null, ["callee:00c58030:8"]]
- 005a9800 bytes d8b91a94
+ 005a9840 bytes fcb91a94
- 005a9828 ["INT_ADD", "register:40f0:8", ["const:5a9828:8", "const:4:8"]]
- 005a9828 ["CALL", null, ["callee:00c58040:8"]]
+ 005a9868 ["INT_ADD", "register:40f0:8", ["const:5a9868:8", "const:4:8"]]
+ 005a9868 ["CALL", null, ["callee:00c58040:8"]]
- 005a9828 bytes d2b91a94
+ 005a9868 bytes f6b91a94
- 005a97ec ["INT_ADD", "register:40f0:8", ["const:5a97ec:8", "const:4:8"]]
- 005a97ec ["CALL", null, ["callee:00c58020:8"]]
+ 005a982c ["INT_ADD", "register:40f0:8", ["const:5a982c:8", "const:4:8"]]
+ 005a982c ["CALL", null, ["callee:00c58020:8"]]
- 005a97ec bytes d9b91a94
+ 005a982c bytes fdb91a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fd9a6082554b09db07c0b5068b7bba7"></a>

### [`005a996c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a996c.md) → [`005a99ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a99ac.md) FUN_005a99ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`00597110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597110.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md) [`00597150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597150.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a99dc",
      "incomplete_value": false,
      "site": "005a99e4",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a999c",
      "incomplete_value": false,
      "site": "005a99a4",
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
            "const:a90:8"
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
      "definition_site": "005a99fc",
      "incomplete_value": false,
      "site": "005a99fc",
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
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a99bc",
      "incomplete_value": false,
      "site": "005a99bc",
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
            "const:ae0:8"
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
      "definition_site": "005a9a38",
      "incomplete_value": true,
      "site": "005a9a38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:93f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a99f8",
      "incomplete_value": true,
      "site": "005a99f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:90e:8"
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
      "005a99e4",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "005a99fc",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "005a9a18",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005a99e4",
      "DATA",
      [
        "storage",
        "00c63b60",
        null,
        "pointer"
      ]
    ],
    [
      "005a99fc",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ],
    [
      "005a9a18",
      "READ",
      [
        "storage",
        "002b393f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a99b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a996c.md#insn-005a99b8) · [`005a9a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a996c.md#insn-005a9a38) · [`005a9994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a996c.md#insn-005a9994)
- 新版 `005a99f8`（命令位置の公開資料なし） · `005a9a78`（命令位置の公開資料なし） · `005a99d4`（命令位置の公開資料なし）

~~~diff
- 005a99b8 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 005a99b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a99b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a99b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a99f8 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 005a99f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a99f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a99f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a99b8 bytes 08812b91
+ 005a99f8 bytes 08c12e91
- 005a9a38 ["INT_ADD", "register:40f0:8", ["const:5a9a38:8", "const:4:8"]]
- 005a9a38 ["CALL", null, ["callee:0045986c:8"]]
+ 005a9a78 ["INT_ADD", "register:40f0:8", ["const:5a9a78:8", "const:4:8"]]
+ 005a9a78 ["CALL", null, ["callee:0045986c:8"]]
- 005a9a38 bytes 7dbffa97
+ 005a9a78 bytes 7dbffa97
- 005a9994 ["INT_ADD", "register:40f0:8", ["const:5a9994:8", "const:4:8"]]
- 005a9994 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a99d4 ["INT_ADD", "register:40f0:8", ["const:5a99d4:8", "const:4:8"]]
+ 005a99d4 ["CALL", null, ["callee:00c57f60:8"]]
- 005a9994 bytes 3fb91a94
+ 005a99d4 bytes 63b91a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83c124de46b699b9b5838ae6dbcc6bfb"></a>

### [`005a9b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b10.md) → [`005a9b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9b50.md) FUN_005a9b50

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
      "definition_site": "005a9b6c",
      "incomplete_value": false,
      "site": "005a9b74",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9b2c",
      "incomplete_value": false,
      "site": "005a9b34",
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
            "const:1d8:8"
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
      "definition_site": "005a9b84",
      "incomplete_value": false,
      "site": "005a9b84",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005a9b44",
      "incomplete_value": false,
      "site": "005a9b44",
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
            "const:128:8"
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
      "005a9b74",
      "DATA",
      [
        "storage",
        "00c6f1d8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a9b84",
      "DATA",
      [
        "storage",
        "00c6f128",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005a9b74",
      "DATA",
      [
        "storage",
        "00c6f2a8",
        null,
        "undefined *"
      ]
    ],
    [
      "005a9b84",
      "DATA",
      [
        "storage",
        "00c6f1f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a9b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b10.md#insn-005a9b24) · [`005a9b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b10.md#insn-005a9b2c) · [`005a9b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b10.md#insn-005a9b38)
- 新版 `005a9b64`（命令位置の公開資料なし） · `005a9b6c`（命令位置の公開資料なし）

~~~diff
- 005a9b24 ["INT_ADD", "register:40f0:8", ["const:5a9b24:8", "const:4:8"]]
- 005a9b24 ["CALL", null, ["callee:00c57f60:8"]]
+ 005a9b64 ["INT_ADD", "register:40f0:8", ["const:5a9b64:8", "const:4:8"]]
+ 005a9b64 ["CALL", null, ["callee:00c57f60:8"]]
- 005a9b24 bytes dbb81a94
+ 005a9b64 bytes ffb81a94
- 005a9b2c ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 005a9b2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a9b2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a9b2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a9b6c ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 005a9b6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9b6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9b6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a9b2c bytes 08610791
+ 005a9b6c bytes 08a10a91
- 005a9b38 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005a9b38 bytes 283600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2f023d225d027e43ffcaa74f9bc7213"></a>

### [`005a9b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b58.md) → [`005a9b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9b98.md) FUN_005a9b98

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
      "definition_site": "005a9bc4",
      "incomplete_value": false,
      "site": "005a9bc8",
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
      "definition_site": "005a9b84",
      "incomplete_value": false,
      "site": "005a9b88",
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
      "005a9bc8",
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
      "005a9bc8",
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

- 旧版 [`005a9b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b58.md#insn-005a9b74) · [`005a9b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b58.md#insn-005a9b7c) · [`005a9b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9b58.md#insn-005a9b94)
- 新版 `005a9bb4`（命令位置の公開資料なし） · `005a9bbc`（命令位置の公開資料なし） · `005a9bd4`（命令位置の公開資料なし）

~~~diff
- 005a9b74 ["INT_ADD", "register:40f0:8", ["const:5a9b74:8", "const:4:8"]]
- 005a9b74 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a9bb4 ["INT_ADD", "register:40f0:8", ["const:5a9bb4:8", "const:4:8"]]
+ 005a9bb4 ["CALL", null, ["callee:00c57f80:8"]]
- 005a9b74 bytes cfb81a94
+ 005a9bb4 bytes f3b81a94
- 005a9b7c ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005a9b7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a9b7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a9b7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a9bbc ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005a9bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a9b7c bytes 08412891
+ 005a9bbc bytes 08812b91
- 005a9b94 ["INT_ADD", "register:40f0:8", ["const:5a9b94:8", "const:4:8"]]
- 005a9b94 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a9bd4 ["INT_ADD", "register:40f0:8", ["const:5a9bd4:8", "const:4:8"]]
+ 005a9bd4 ["CALL", null, ["callee:00c57f80:8"]]
- 005a9b94 bytes c7b81a94
+ 005a9bd4 bytes ebb81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35424ce6356baff0bdd25d378aa9c7ee"></a>

### [`005a9bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9bbc.md) → [`005a9bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9bfc.md) FUN_005a9bfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005a9c28",
      "incomplete_value": true,
      "site": "005a9c2c",
      "value": [
        "INT_ADD",
        "8",
        [
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
      "definition_site": "005a9be8",
      "incomplete_value": true,
      "site": "005a9bec",
      "value": [
        "INT_ADD",
        "8",
        [
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
      "005a9c2c",
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
      "005a9c2c",
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

- 旧版 [`005a9bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9bbc.md#insn-005a9bd8) · [`005a9be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9bbc.md#insn-005a9be0) · [`005a9bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9bbc.md#insn-005a9bf8)
- 新版 `005a9c18`（命令位置の公開資料なし） · `005a9c20`（命令位置の公開資料なし） · `005a9c38`（命令位置の公開資料なし）

~~~diff
- 005a9bd8 ["INT_ADD", "register:40f0:8", ["const:5a9bd8:8", "const:4:8"]]
- 005a9bd8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a9c18 ["INT_ADD", "register:40f0:8", ["const:5a9c18:8", "const:4:8"]]
+ 005a9c18 ["CALL", null, ["callee:00c57f80:8"]]
- 005a9bd8 bytes b6b81a94
+ 005a9c18 bytes dab81a94
- 005a9be0 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005a9be0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005a9be0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005a9be0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005a9c20 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005a9c20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9c20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005a9c20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005a9be0 bytes 08412891
+ 005a9c20 bytes 08812b91
- 005a9bf8 ["INT_ADD", "register:40f0:8", ["const:5a9bf8:8", "const:4:8"]]
- 005a9bf8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a9c38 ["INT_ADD", "register:40f0:8", ["const:5a9c38:8", "const:4:8"]]
+ 005a9c38 ["CALL", null, ["callee:00c57f80:8"]]
- 005a9bf8 bytes aeb81a94
+ 005a9c38 bytes d2b81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-379a97043147f27039f2c574436b4e36"></a>

### [`005a9c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9c1c.md) → [`005a9c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9c5c.md) FUN_005a9c5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`005a9d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d00.md) [`005aa254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa254.md) · 呼出先 2件 [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`005a9d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9d40.md) [`005aa294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa294.md) · 呼出先 2件 [`005aa1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1c4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005a9cdc",
      "incomplete_value": false,
      "site": "005a9ce0",
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
      "definition_site": "005a9c9c",
      "incomplete_value": false,
      "site": "005a9ca0",
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
      "005a9ce0",
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
      "005a9ce0",
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

- 旧版 [`005a9c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9c1c.md#insn-005a9c54) · [`005a9c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9c1c.md#insn-005a9c68) · [`005a9c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9c1c.md#insn-005a9c90)
- 新版 `005a9c94`（命令位置の公開資料なし） · `005a9ca8`（命令位置の公開資料なし） · `005a9cd0`（命令位置の公開資料なし）

~~~diff
- 005a9c54 ["INT_ADD", "register:40f0:8", ["const:5a9c54:8", "const:4:8"]]
- 005a9c54 ["CALL", null, ["callee:005aa1c4:8"]]
+ 005a9c94 ["INT_ADD", "register:40f0:8", ["const:5a9c94:8", "const:4:8"]]
+ 005a9c94 ["CALL", null, ["callee:005aa1c4:8"]]
- 005a9c54 bytes 4c010094
+ 005a9c94 bytes 4c010094
- 005a9c68 ["INT_ADD", "register:40f0:8", ["const:5a9c68:8", "const:4:8"]]
- 005a9c68 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a9ca8 ["INT_ADD", "register:40f0:8", ["const:5a9ca8:8", "const:4:8"]]
+ 005a9ca8 ["CALL", null, ["callee:00c57f80:8"]]
- 005a9c68 bytes 92b81a94
+ 005a9ca8 bytes b6b81a94
- 005a9c90 ["INT_ADD", "register:40f0:8", ["const:5a9c90:8", "const:4:8"]]
- 005a9c90 ["CALL", null, ["callee:00c57f80:8"]]
+ 005a9cd0 ["INT_ADD", "register:40f0:8", ["const:5a9cd0:8", "const:4:8"]]
+ 005a9cd0 ["CALL", null, ["callee:00c57f80:8"]]
- 005a9c90 bytes 88b81a94
+ 005a9cd0 bytes acb81a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07c00e37a0a8f2f1a88b61463c5ffede"></a>

### [`005a9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ee4.md) → [`005a9f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9f24.md) FUN_005a9f24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005a9d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9d24.md) [`009b5d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5d84.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`005a9d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9d64.md) [`009b5dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5dd8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "005a9f30",
      "incomplete_value": false,
      "site": "005a9f34",
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
      "definition_site": "005a9ef0",
      "incomplete_value": false,
      "site": "005a9ef4",
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
      "005a9f30",
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
      "005a9f30",
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

- 旧版 [`005a9ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ee4.md#insn-005a9ef4) · [`005a9ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ee4.md#insn-005a9ef0)
- 新版 `005a9f34`（命令位置の公開資料なし） · `005a9f30`（命令位置の公開資料なし）

~~~diff
- 005a9ef4 ["INT_ADD", "register:40f0:8", ["const:5a9ef4:8", "const:4:8"]]
- 005a9ef4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 005a9f34 ["INT_ADD", "register:40f0:8", ["const:5a9f34:8", "const:4:8"]]
+ 005a9f34 ["CALL", null, ["callee:0043b7b8:8"]]
- 005a9ef4 bytes 2146fa97
+ 005a9f34 bytes 2146fa97
- 005a9ef0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 005a9ef0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005a9ef0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005a9ef0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005a9f30 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 005a9f30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005a9f30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005a9f30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005a9ef0 bytes 00303d91
+ 005a9f30 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b38d195b8cf0b0a6b65e8dd467e4000"></a>

### [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) → [`005aa1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1b0.md) FUN_005aa1b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 12件 [`005a9f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md) [`005aa638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa638.md) [`005ab7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab7a0.md) [`00747ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/00747ab0.md) [`0074820c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00748/0074820c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 12件 [`005a9f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9f94.md) [`005aa678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa678.md) [`005ab7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab7e0.md) [`00747b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747b08.md) [`00748264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00748/00748264.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "005aa1bc",
      "incomplete_value": false,
      "site": "005aa1c0",
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
      "definition_site": "005aa17c",
      "incomplete_value": false,
      "site": "005aa180",
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
      "005aa1bc",
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
      "005aa1bc",
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

- 旧版 [`005aa180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md#insn-005aa180) · [`005aa17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md#insn-005aa17c)
- 新版 `005aa1c0`（命令位置の公開資料なし） · `005aa1bc`（命令位置の公開資料なし）

~~~diff
- 005aa180 ["INT_ADD", "register:40f0:8", ["const:5aa180:8", "const:4:8"]]
- 005aa180 ["CALL", null, ["callee:0043b7b8:8"]]
+ 005aa1c0 ["INT_ADD", "register:40f0:8", ["const:5aa1c0:8", "const:4:8"]]
+ 005aa1c0 ["CALL", null, ["callee:0043b7b8:8"]]
- 005aa180 bytes 7e45fa97
+ 005aa1c0 bytes 7e45fa97
- 005aa17c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 005aa17c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005aa17c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005aa17c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005aa1bc ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 005aa1bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005aa1bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005aa1bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005aa17c bytes 00303d91
+ 005aa1bc bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aaa3572476ee1e370e3e6c5fce5e481"></a>

### [`005aa214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa214.md) → [`005aa254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa254.md) FUN_005aa254

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
      "definition_site": "005aa258",
      "incomplete_value": false,
      "site": "005aa25c",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa218",
      "incomplete_value": false,
      "site": "005aa21c",
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
            "const:188:8"
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
      "005aa25c",
      "DATA",
      [
        "storage",
        "00c6f188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aa25c",
      "DATA",
      [
        "storage",
        "00c6f258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa214.md#insn-005aa218)
- 新版 `005aa258`（命令位置の公開資料なし）

~~~diff
- 005aa218 ["COPY", "tmp:0:8", ["const:188:8"]]
- 005aa218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aa218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aa218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aa258 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 005aa258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aa218 bytes 08210691
+ 005aa258 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73327477cec0a0d7462adf601db9f4c4"></a>

### [`005aa224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa224.md) → [`005aa264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa264.md) FUN_005aa264

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
      "definition_site": "005aa274",
      "incomplete_value": false,
      "site": "005aa27c",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa234",
      "incomplete_value": false,
      "site": "005aa23c",
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
            "const:188:8"
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
      "005aa27c",
      "DATA",
      [
        "storage",
        "00c6f188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aa27c",
      "DATA",
      [
        "storage",
        "00c6f258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa224.md#insn-005aa234) · [`005aa240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa224.md#insn-005aa240)
- 新版 `005aa274`（命令位置の公開資料なし） · `005aa280`（命令位置の公開資料なし）

~~~diff
- 005aa234 ["COPY", "tmp:0:8", ["const:188:8"]]
- 005aa234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aa234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aa234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aa274 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 005aa274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aa234 bytes 08210691
+ 005aa274 bytes 08610991
- 005aa240 ["INT_ADD", "register:40f0:8", ["const:5aa240:8", "const:4:8"]]
- 005aa240 ["CALL", null, ["callee:00c57f70:8"]]
+ 005aa280 ["INT_ADD", "register:40f0:8", ["const:5aa280:8", "const:4:8"]]
+ 005aa280 ["CALL", null, ["callee:00c57f70:8"]]
- 005aa240 bytes 18b71a94
+ 005aa280 bytes 3cb71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdbe0ca39b20bc49ff8776832ed4d4c9"></a>

### [`005aa260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa260.md) → [`005aa2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa2a0.md) FUN_005aa2a0

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
      "definition_site": "005aa2a4",
      "incomplete_value": false,
      "site": "005aa2a8",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa264",
      "incomplete_value": false,
      "site": "005aa268",
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
            "const:1d8:8"
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
      "005aa2a8",
      "DATA",
      [
        "storage",
        "00c6f1d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aa2a8",
      "DATA",
      [
        "storage",
        "00c6f2a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa260.md#insn-005aa264)
- 新版 `005aa2a4`（命令位置の公開資料なし）

~~~diff
- 005aa264 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 005aa264 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aa264 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aa264 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aa2a4 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 005aa2a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa2a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa2a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aa264 bytes 08610791
+ 005aa2a4 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a256867e8850e5d7c95506fec8fed0d6"></a>

### [`005aa270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa270.md) → [`005aa2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa2b0.md) FUN_005aa2b0

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
      "definition_site": "005aa2c0",
      "incomplete_value": false,
      "site": "005aa2c8",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa280",
      "incomplete_value": false,
      "site": "005aa288",
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
            "const:1d8:8"
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
      "005aa2c8",
      "DATA",
      [
        "storage",
        "00c6f1d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aa2c8",
      "DATA",
      [
        "storage",
        "00c6f2a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa270.md#insn-005aa280) · [`005aa28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa270.md#insn-005aa28c)
- 新版 `005aa2c0`（命令位置の公開資料なし） · `005aa2cc`（命令位置の公開資料なし）

~~~diff
- 005aa280 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 005aa280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aa280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aa280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aa2c0 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 005aa2c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa2c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa2c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aa280 bytes 08610791
+ 005aa2c0 bytes 08a10a91
- 005aa28c ["INT_ADD", "register:40f0:8", ["const:5aa28c:8", "const:4:8"]]
- 005aa28c ["CALL", null, ["callee:00c57f70:8"]]
+ 005aa2cc ["INT_ADD", "register:40f0:8", ["const:5aa2cc:8", "const:4:8"]]
+ 005aa2cc ["CALL", null, ["callee:00c57f70:8"]]
- 005aa28c bytes 05b71a94
+ 005aa2cc bytes 29b71a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6bfbfaeb1ccfb67b92c4da834ba2c35"></a>

### [`005aa2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa2a8.md) → [`005aa2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa2e8.md) _INIT_55

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005aa324",
      "incomplete_value": true,
      "site": "005aa340",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005aa2e4",
      "incomplete_value": true,
      "site": "005aa300",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005aa348",
      "incomplete_value": true,
      "site": "005aa364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005aa308",
      "incomplete_value": true,
      "site": "005aa324",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005aa368",
      "incomplete_value": true,
      "site": "005aa384",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005aa328",
      "incomplete_value": true,
      "site": "005aa344",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005aa324",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005aa348",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005aa368",
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
      "005aa324",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005aa348",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005aa368",
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

- 旧版 [`005aa320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa2a8.md#insn-005aa320) · [`005aa340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa2a8.md#insn-005aa340) · [`005aa408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa2a8.md#insn-005aa408)
- 新版 `005aa360`（命令位置の公開資料なし） · `005aa380`（命令位置の公開資料なし） · `005aa448`（命令位置の公開資料なし）

~~~diff
- 005aa320 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 005aa320 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005aa320 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005aa320 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005aa360 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 005aa360 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005aa360 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005aa360 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005aa320 bytes 4a093791
+ 005aa360 bytes 4ab93591
- 005aa340 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005aa340 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005aa340 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005aa340 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005aa380 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005aa380 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005aa380 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005aa380 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005aa340 bytes 4a893d91
+ 005aa380 bytes 4a553c91
- 005aa408 ["INT_ADD", "register:40f0:8", ["const:5aa408:8", "const:4:8"]]
- 005aa408 ["CALL", null, ["callee:0043b838:8"]]
+ 005aa448 ["INT_ADD", "register:40f0:8", ["const:5aa448:8", "const:4:8"]]
+ 005aa448 ["CALL", null, ["callee:0043b838:8"]]
- 005aa408 bytes fc44fa97
+ 005aa448 bytes fc44fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54b2ab786ad3ed623a5a3ca9a1d986e9"></a>

### [`005aa638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa638.md) → [`005aa678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa678.md) FUN_005aa678

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005aa7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa7ac.md) · 呼出先 6件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005aa7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa7ec.md) · 呼出先 6件 [`0059b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b91c.md) [`005aa1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1b0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.70% / 新版 95.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005aa6ac",
      "incomplete_value": false,
      "site": "005aa6b0",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa66c",
      "incomplete_value": false,
      "site": "005aa670",
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
            "const:228:8"
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
      "definition_site": "005aa7a8",
      "incomplete_value": false,
      "site": "005aa7ac",
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
      "definition_site": "005aa768",
      "incomplete_value": false,
      "site": "005aa76c",
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
      "005aa6b0",
      "DATA",
      [
        "storage",
        "00c6f228",
        null,
        "pointer"
      ]
    ],
    [
      "005aa7ac",
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
      "005aa6b0",
      "DATA",
      [
        "storage",
        "00c6f2f8",
        null,
        "pointer"
      ]
    ],
    [
      "005aa7ac",
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

- 旧版 [`005aa664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa638.md#insn-005aa664) · [`005aa66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa638.md#insn-005aa66c) · [`005aa6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa638.md#insn-005aa6e8)
- 新版 `005aa6a4`（命令位置の公開資料なし） · `005aa6ac`（命令位置の公開資料なし） · `005aa728`（命令位置の公開資料なし）

~~~diff
- 005aa664 ["INT_ADD", "register:40f0:8", ["const:5aa664:8", "const:4:8"]]
- 005aa664 ["CALL", null, ["callee:0059b91c:8"]]
+ 005aa6a4 ["INT_ADD", "register:40f0:8", ["const:5aa6a4:8", "const:4:8"]]
+ 005aa6a4 ["CALL", null, ["callee:0059b91c:8"]]
- 005aa664 bytes 9ec4ff97
+ 005aa6a4 bytes 9ec4ff97
- 005aa66c ["COPY", "tmp:0:8", ["const:228:8"]]
- 005aa66c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aa66c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aa66c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aa6ac ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 005aa6ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa6ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aa6ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aa66c bytes 08a10891
+ 005aa6ac bytes 08e10b91
- 005aa6e8 ["INT_ADD", "register:40f0:8", ["const:5aa6e8:8", "const:4:8"]]
- 005aa6e8 ["CALL", null, ["callee:00c57f60:8"]]
+ 005aa728 ["INT_ADD", "register:40f0:8", ["const:5aa728:8", "const:4:8"]]
+ 005aa728 ["CALL", null, ["callee:00c57f60:8"]]
- 005aa6e8 bytes eab51a94
+ 005aa728 bytes 0eb61a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48495c1cb94e8ef2e8114812efa99dc3"></a>

### [`005aa7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa7ac.md) → [`005aa7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa7ec.md) FUN_005aa7ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005aa638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa638.md) [`009b3798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3798.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`005aa678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa678.md) [`009b37ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b37ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.76% / 新版 95.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005aa848",
      "incomplete_value": true,
      "site": "005aa848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005aa808",
      "incomplete_value": true,
      "site": "005aa808",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005aa980",
      "incomplete_value": true,
      "site": "005aa980",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aa940",
      "incomplete_value": true,
      "site": "005aa940",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f2d:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005aaab4",
      "incomplete_value": true,
      "site": "005aaab4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aaa74",
      "incomplete_value": true,
      "site": "005aaa74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d2:8"
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
      "005aa838",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005aa96c",
      "READ",
      [
        "storage",
        "0029ff2d",
        null,
        "string"
      ]
    ],
    [
      "005aaaa4",
      "READ",
      [
        "storage",
        "002b90d2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005aa838",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "005aa96c",
      "READ",
      [
        "storage",
        "0029fee0",
        null,
        "string"
      ]
    ],
    [
      "005aaaa4",
      "READ",
      [
        "storage",
        "002b907e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa7ac.md#insn-005aa900) · [`005aa980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa7ac.md#insn-005aa980) · [`005aa7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa7ac.md#insn-005aa7f4)
- 新版 `005aa940`（命令位置の公開資料なし） · `005aa9c0`（命令位置の公開資料なし） · `005aa834`（命令位置の公開資料なし）

~~~diff
- 005aa900 ["INT_ADD", "register:40f0:8", ["const:5aa900:8", "const:4:8"]]
- 005aa900 ["CALL", null, ["callee:00c57f80:8"]]
+ 005aa940 ["INT_ADD", "register:40f0:8", ["const:5aa940:8", "const:4:8"]]
+ 005aa940 ["CALL", null, ["callee:00c57f80:8"]]
- 005aa900 bytes 6cb51a94
+ 005aa940 bytes 90b51a94
- 005aa980 ["INT_ADD", "register:40f0:8", ["const:5aa980:8", "const:4:8"]]
- 005aa980 ["CALL", null, ["callee:00c57f80:8"]]
+ 005aa9c0 ["INT_ADD", "register:40f0:8", ["const:5aa9c0:8", "const:4:8"]]
+ 005aa9c0 ["CALL", null, ["callee:00c57f80:8"]]
- 005aa980 bytes 4cb51a94
+ 005aa9c0 bytes 70b51a94
- 005aa7f4 ["COPY", "tmp:0:8", ["const:1a5:8"]]
- 005aa7f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005aa7f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005aa7f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005aa834 ["COPY", "tmp:0:8", ["const:1e5:8"]]
+ 005aa834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005aa834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005aa834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005aa7f4 bytes 29950691
+ 005aa834 bytes 29950791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc24f5f1756fd8d13766cd6b1d150a22"></a>

### [`005aae88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aae88.md) → [`005aaec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aaec8.md) FUN_005aaec8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009b4900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4900.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)
- 新版 呼出元 1件 [`009b4954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b4954.md) · 呼出先 1件 [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md)

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
      "definition_site": "005aaeec",
      "incomplete_value": false,
      "site": "005aaef4",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aaeac",
      "incomplete_value": false,
      "site": "005aaeb4",
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
            "const:248:8"
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
      "005aaef4",
      "DATA",
      [
        "storage",
        "00c6f248",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aaef4",
      "DATA",
      [
        "storage",
        "00c6f318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aaea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aae88.md#insn-005aaea4) · [`005aaeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aae88.md#insn-005aaeac)
- 新版 `005aaee4`（命令位置の公開資料なし） · `005aaeec`（命令位置の公開資料なし）

~~~diff
- 005aaea4 ["INT_ADD", "register:40f0:8", ["const:5aaea4:8", "const:4:8"]]
- 005aaea4 ["CALL", null, ["callee:0059b948:8"]]
+ 005aaee4 ["INT_ADD", "register:40f0:8", ["const:5aaee4:8", "const:4:8"]]
+ 005aaee4 ["CALL", null, ["callee:0059b948:8"]]
- 005aaea4 bytes 99c2ff97
+ 005aaee4 bytes 99c2ff97
- 005aaeac ["COPY", "tmp:0:8", ["const:248:8"]]
- 005aaeac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aaeac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aaeac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aaeec ["COPY", "tmp:0:8", ["const:318:8"]]
+ 005aaeec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aaeec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aaeec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aaeac bytes 08210991
+ 005aaeec bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-056c49a413f29442b2336f4bb41fd731"></a>

### [`005aaee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aaee4.md) → [`005aaf24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aaf24.md) FUN_005aaf24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58020.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.74% / 新版 96.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005aaf5c",
      "incomplete_value": false,
      "site": "005aaf68",
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
            "const:d2a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aaf1c",
      "incomplete_value": false,
      "site": "005aaf28",
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
            "const:d86:8"
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
      "definition_site": "005aaf88",
      "incomplete_value": false,
      "site": "005aaf90",
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
            "const:6c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aaf48",
      "incomplete_value": false,
      "site": "005aaf50",
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
            "const:722:8"
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
      "definition_site": "005aafec",
      "incomplete_value": false,
      "site": "005aaff4",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aafac",
      "incomplete_value": false,
      "site": "005aafb4",
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
            "const:d94:8"
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
      "005aaf5c",
      "PARAM",
      [
        "storage",
        "002b0d86",
        null,
        "string"
      ]
    ],
    [
      "005aaf88",
      "PARAM",
      [
        "storage",
        "002a5722",
        null,
        "string"
      ]
    ],
    [
      "005aafec",
      "PARAM",
      [
        "storage",
        "002b0d94",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005aaf5c",
      "PARAM",
      [
        "storage",
        "002b0d2a",
        null,
        "string"
      ]
    ],
    [
      "005aaf88",
      "PARAM",
      [
        "storage",
        "002a56c6",
        null,
        "string"
      ]
    ],
    [
      "005aafec",
      "PARAM",
      [
        "storage",
        "002b0d38",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aaf28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aaee4.md#insn-005aaf28) · [`005aaf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aaee4.md#insn-005aaf50) · [`005aafb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aaee4.md#insn-005aafb4)
- 新版 `005aaf68`（命令位置の公開資料なし） · `005aaf90`（命令位置の公開資料なし） · `005aaff4`（命令位置の公開資料なし）

~~~diff
- 005aaf28 ["INT_ADD", "register:40f0:8", ["const:5aaf28:8", "const:4:8"]]
- 005aaf28 ["CALL", null, ["callee:00c58030:8"]]
+ 005aaf68 ["INT_ADD", "register:40f0:8", ["const:5aaf68:8", "const:4:8"]]
+ 005aaf68 ["CALL", null, ["callee:00c58030:8"]]
- 005aaf28 bytes 0eb41a94
+ 005aaf68 bytes 32b41a94
- 005aaf50 ["INT_ADD", "register:40f0:8", ["const:5aaf50:8", "const:4:8"]]
- 005aaf50 ["CALL", null, ["callee:00c58040:8"]]
+ 005aaf90 ["INT_ADD", "register:40f0:8", ["const:5aaf90:8", "const:4:8"]]
+ 005aaf90 ["CALL", null, ["callee:00c58040:8"]]
- 005aaf50 bytes 08b41a94
+ 005aaf90 bytes 2cb41a94
- 005aafb4 ["INT_ADD", "register:40f0:8", ["const:5aafb4:8", "const:4:8"]]
- 005aafb4 ["CALL", null, ["callee:00c58040:8"]]
+ 005aaff4 ["INT_ADD", "register:40f0:8", ["const:5aaff4:8", "const:4:8"]]
+ 005aaff4 ["CALL", null, ["callee:00c58040:8"]]
- 005aafb4 bytes efb31a94
+ 005aaff4 bytes 13b41a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b3bf05765bdc3d026b805fbebff1719"></a>

### [`005ab12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab12c.md) → [`005ab16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab16c.md) FUN_005ab16c

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
      "definition_site": "005ab188",
      "incomplete_value": false,
      "site": "005ab190",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab148",
      "incomplete_value": false,
      "site": "005ab150",
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
            "const:350:8"
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
      "definition_site": "005ab1a0",
      "incomplete_value": false,
      "site": "005ab1a0",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab160",
      "incomplete_value": false,
      "site": "005ab160",
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
            "const:2a0:8"
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
      "005ab190",
      "DATA",
      [
        "storage",
        "00c6f350",
        null,
        "undefined *"
      ]
    ],
    [
      "005ab1a0",
      "DATA",
      [
        "storage",
        "00c6f2a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005ab190",
      "DATA",
      [
        "storage",
        "00c6f420",
        null,
        "undefined *"
      ]
    ],
    [
      "005ab1a0",
      "DATA",
      [
        "storage",
        "00c6f370",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab12c.md#insn-005ab140) · [`005ab148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab12c.md#insn-005ab148) · [`005ab154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab12c.md#insn-005ab154)
- 新版 `005ab180`（命令位置の公開資料なし） · `005ab188`（命令位置の公開資料なし）

~~~diff
- 005ab140 ["INT_ADD", "register:40f0:8", ["const:5ab140:8", "const:4:8"]]
- 005ab140 ["CALL", null, ["callee:00c57f60:8"]]
+ 005ab180 ["INT_ADD", "register:40f0:8", ["const:5ab180:8", "const:4:8"]]
+ 005ab180 ["CALL", null, ["callee:00c57f60:8"]]
- 005ab140 bytes 54b31a94
+ 005ab180 bytes 78b31a94
- 005ab148 ["COPY", "tmp:0:8", ["const:350:8"]]
- 005ab148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab188 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 005ab188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab148 bytes 08410d91
+ 005ab188 bytes 08811091
- 005ab154 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005ab154 bytes 28360090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d119719d42351f8211db09ff18c72573"></a>

### [`005ab174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab174.md) → [`005ab1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab1b4.md) FUN_005ab1b4

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
      "definition_site": "005ab1e0",
      "incomplete_value": false,
      "site": "005ab1e4",
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
      "definition_site": "005ab1a0",
      "incomplete_value": false,
      "site": "005ab1a4",
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
      "005ab1e4",
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
      "005ab1e4",
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

- 旧版 [`005ab190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab174.md#insn-005ab190) · [`005ab198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab174.md#insn-005ab198) · [`005ab1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab174.md#insn-005ab1b0)
- 新版 `005ab1d0`（命令位置の公開資料なし） · `005ab1d8`（命令位置の公開資料なし） · `005ab1f0`（命令位置の公開資料なし）

~~~diff
- 005ab190 ["INT_ADD", "register:40f0:8", ["const:5ab190:8", "const:4:8"]]
- 005ab190 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab1d0 ["INT_ADD", "register:40f0:8", ["const:5ab1d0:8", "const:4:8"]]
+ 005ab1d0 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab190 bytes 48b31a94
+ 005ab1d0 bytes 6cb31a94
- 005ab198 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005ab198 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab198 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab198 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab1d8 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005ab1d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab1d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab1d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab198 bytes 08412891
+ 005ab1d8 bytes 08812b91
- 005ab1b0 ["INT_ADD", "register:40f0:8", ["const:5ab1b0:8", "const:4:8"]]
- 005ab1b0 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab1f0 ["INT_ADD", "register:40f0:8", ["const:5ab1f0:8", "const:4:8"]]
+ 005ab1f0 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab1b0 bytes 40b31a94
+ 005ab1f0 bytes 64b31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad07583cbab95de23c7b031076e8bf7b"></a>

### [`005ab1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab1d8.md) → [`005ab218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab218.md) FUN_005ab218

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
      "definition_site": "005ab244",
      "incomplete_value": false,
      "site": "005ab248",
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
      "definition_site": "005ab204",
      "incomplete_value": false,
      "site": "005ab208",
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
      "005ab248",
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
      "005ab248",
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

- 旧版 [`005ab1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab1d8.md#insn-005ab1f4) · [`005ab1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab1d8.md#insn-005ab1fc) · [`005ab214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab1d8.md#insn-005ab214)
- 新版 `005ab234`（命令位置の公開資料なし） · `005ab23c`（命令位置の公開資料なし） · `005ab254`（命令位置の公開資料なし）

~~~diff
- 005ab1f4 ["INT_ADD", "register:40f0:8", ["const:5ab1f4:8", "const:4:8"]]
- 005ab1f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab234 ["INT_ADD", "register:40f0:8", ["const:5ab234:8", "const:4:8"]]
+ 005ab234 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab1f4 bytes 2fb31a94
+ 005ab234 bytes 53b31a94
- 005ab1fc ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005ab1fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab1fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab1fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab23c ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005ab23c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab23c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab23c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab1fc bytes 08412891
+ 005ab23c bytes 08812b91
- 005ab214 ["INT_ADD", "register:40f0:8", ["const:5ab214:8", "const:4:8"]]
- 005ab214 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab254 ["INT_ADD", "register:40f0:8", ["const:5ab254:8", "const:4:8"]]
+ 005ab254 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab214 bytes 27b31a94
+ 005ab254 bytes 4bb31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a853509a2c873ead3138b4ca99778ef1"></a>

### [`005ab238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab238.md) → [`005ab278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab278.md) FUN_005ab278

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005ab2c0",
      "incomplete_value": false,
      "site": "005ab2c4",
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
      "definition_site": "005ab280",
      "incomplete_value": false,
      "site": "005ab284",
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
      "005ab2c4",
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
      "005ab2c4",
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

- 旧版 [`005ab254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab238.md#insn-005ab254) · [`005ab264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab238.md#insn-005ab264) · [`005ab274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab238.md#insn-005ab274)
- 新版 `005ab294`（命令位置の公開資料なし） · `005ab2a4`（命令位置の公開資料なし） · `005ab2b4`（命令位置の公開資料なし）

~~~diff
- 005ab254 ["INT_ADD", "register:40f0:8", ["const:5ab254:8", "const:4:8"]]
- 005ab254 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab294 ["INT_ADD", "register:40f0:8", ["const:5ab294:8", "const:4:8"]]
+ 005ab294 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab254 bytes 17b31a94
+ 005ab294 bytes 3bb31a94
- 005ab264 ["INT_ADD", "register:40f0:8", ["const:5ab264:8", "const:4:8"]]
- 005ab264 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab2a4 ["INT_ADD", "register:40f0:8", ["const:5ab2a4:8", "const:4:8"]]
+ 005ab2a4 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab264 bytes 13b31a94
+ 005ab2a4 bytes 37b31a94
- 005ab274 ["INT_ADD", "register:40f0:8", ["const:5ab274:8", "const:4:8"]]
- 005ab274 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab2b4 ["INT_ADD", "register:40f0:8", ["const:5ab2b4:8", "const:4:8"]]
+ 005ab2b4 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab274 bytes 0fb31a94
+ 005ab2b4 bytes 33b31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80365f3a13d8ea5e116b001388b9c5e1"></a>

### [`005ab2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab2a8.md) → [`005ab2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab2e8.md) FUN_005ab2e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005ab330",
      "incomplete_value": false,
      "site": "005ab334",
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
      "definition_site": "005ab2f0",
      "incomplete_value": false,
      "site": "005ab2f4",
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
      "005ab334",
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
      "005ab334",
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

- 旧版 [`005ab2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab2a8.md#insn-005ab2c4) · [`005ab2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab2a8.md#insn-005ab2d4) · [`005ab2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab2a8.md#insn-005ab2e4)
- 新版 `005ab304`（命令位置の公開資料なし） · `005ab314`（命令位置の公開資料なし） · `005ab324`（命令位置の公開資料なし）

~~~diff
- 005ab2c4 ["INT_ADD", "register:40f0:8", ["const:5ab2c4:8", "const:4:8"]]
- 005ab2c4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab304 ["INT_ADD", "register:40f0:8", ["const:5ab304:8", "const:4:8"]]
+ 005ab304 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab2c4 bytes fbb21a94
+ 005ab304 bytes 1fb31a94
- 005ab2d4 ["INT_ADD", "register:40f0:8", ["const:5ab2d4:8", "const:4:8"]]
- 005ab2d4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab314 ["INT_ADD", "register:40f0:8", ["const:5ab314:8", "const:4:8"]]
+ 005ab314 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab2d4 bytes f7b21a94
+ 005ab314 bytes 1bb31a94
- 005ab2e4 ["INT_ADD", "register:40f0:8", ["const:5ab2e4:8", "const:4:8"]]
- 005ab2e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab324 ["INT_ADD", "register:40f0:8", ["const:5ab324:8", "const:4:8"]]
+ 005ab324 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab2e4 bytes f3b21a94
+ 005ab324 bytes 17b31a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e7fdd3286d2ef8fb75889609016397c"></a>

### [`005ab314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab314.md) → [`005ab354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab354.md) FUN_005ab354

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
      "definition_site": "005ab358",
      "incomplete_value": false,
      "site": "005ab35c",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab318",
      "incomplete_value": false,
      "site": "005ab31c",
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
            "const:300:8"
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
      "005ab35c",
      "DATA",
      [
        "storage",
        "00c6f300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ab35c",
      "DATA",
      [
        "storage",
        "00c6f3d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab314.md#insn-005ab318)
- 新版 `005ab358`（命令位置の公開資料なし）

~~~diff
- 005ab318 ["COPY", "tmp:0:8", ["const:300:8"]]
- 005ab318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab358 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 005ab358 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab358 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab358 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab318 bytes 08010c91
+ 005ab358 bytes 08410f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25a8e5bce3fb6b1f11a855379d6447e8"></a>

### [`005ab324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab324.md) → [`005ab364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab364.md) FUN_005ab364

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
      "definition_site": "005ab374",
      "incomplete_value": false,
      "site": "005ab37c",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab334",
      "incomplete_value": false,
      "site": "005ab33c",
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
            "const:300:8"
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
      "005ab37c",
      "DATA",
      [
        "storage",
        "00c6f300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ab37c",
      "DATA",
      [
        "storage",
        "00c6f3d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab324.md#insn-005ab334) · [`005ab340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab324.md#insn-005ab340)
- 新版 `005ab374`（命令位置の公開資料なし） · `005ab380`（命令位置の公開資料なし）

~~~diff
- 005ab334 ["COPY", "tmp:0:8", ["const:300:8"]]
- 005ab334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab374 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 005ab374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab334 bytes 08010c91
+ 005ab374 bytes 08410f91
- 005ab340 ["INT_ADD", "register:40f0:8", ["const:5ab340:8", "const:4:8"]]
- 005ab340 ["CALL", null, ["callee:00c57f70:8"]]
+ 005ab380 ["INT_ADD", "register:40f0:8", ["const:5ab380:8", "const:4:8"]]
+ 005ab380 ["CALL", null, ["callee:00c57f70:8"]]
- 005ab340 bytes d8b21a94
+ 005ab380 bytes fcb21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0d5fa74d5ec94075134c6414f020ad0"></a>

### [`005ab354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab354.md) → [`005ab394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab394.md) FUN_005ab394

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005ab3dc",
      "incomplete_value": false,
      "site": "005ab3e0",
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
      "definition_site": "005ab39c",
      "incomplete_value": false,
      "site": "005ab3a0",
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
      "005ab3e0",
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
      "005ab3e0",
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

- 旧版 [`005ab370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab354.md#insn-005ab370) · [`005ab380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab354.md#insn-005ab380) · [`005ab390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab354.md#insn-005ab390)
- 新版 `005ab3b0`（命令位置の公開資料なし） · `005ab3c0`（命令位置の公開資料なし） · `005ab3d0`（命令位置の公開資料なし）

~~~diff
- 005ab370 ["INT_ADD", "register:40f0:8", ["const:5ab370:8", "const:4:8"]]
- 005ab370 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab3b0 ["INT_ADD", "register:40f0:8", ["const:5ab3b0:8", "const:4:8"]]
+ 005ab3b0 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab370 bytes d0b21a94
+ 005ab3b0 bytes f4b21a94
- 005ab380 ["INT_ADD", "register:40f0:8", ["const:5ab380:8", "const:4:8"]]
- 005ab380 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab3c0 ["INT_ADD", "register:40f0:8", ["const:5ab3c0:8", "const:4:8"]]
+ 005ab3c0 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab380 bytes ccb21a94
+ 005ab3c0 bytes f0b21a94
- 005ab390 ["INT_ADD", "register:40f0:8", ["const:5ab390:8", "const:4:8"]]
- 005ab390 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ab3d0 ["INT_ADD", "register:40f0:8", ["const:5ab3d0:8", "const:4:8"]]
+ 005ab3d0 ["CALL", null, ["callee:00c57f80:8"]]
- 005ab390 bytes c8b21a94
+ 005ab3d0 bytes ecb21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6ba26d160c9deb36b6d5aedcaf74551"></a>

### [`005ab3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab3c8.md) → [`005ab408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab408.md) FUN_005ab408

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
      "definition_site": "005ab40c",
      "incomplete_value": false,
      "site": "005ab410",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab3cc",
      "incomplete_value": false,
      "site": "005ab3d0",
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
            "const:350:8"
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
      "005ab410",
      "DATA",
      [
        "storage",
        "00c6f350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ab410",
      "DATA",
      [
        "storage",
        "00c6f420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab3c8.md#insn-005ab3cc)
- 新版 `005ab40c`（命令位置の公開資料なし）

~~~diff
- 005ab3cc ["COPY", "tmp:0:8", ["const:350:8"]]
- 005ab3cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab3cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab3cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab40c ["COPY", "tmp:0:8", ["const:420:8"]]
+ 005ab40c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab40c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab40c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab3cc bytes 08410d91
+ 005ab40c bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c23222472b567d1904b3bf7a153af43"></a>

### [`005ab3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab3d8.md) → [`005ab418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab418.md) FUN_005ab418

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
      "definition_site": "005ab428",
      "incomplete_value": false,
      "site": "005ab430",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab3e8",
      "incomplete_value": false,
      "site": "005ab3f0",
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
            "const:350:8"
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
      "005ab430",
      "DATA",
      [
        "storage",
        "00c6f350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ab430",
      "DATA",
      [
        "storage",
        "00c6f420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab3d8.md#insn-005ab3e8) · [`005ab3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab3d8.md#insn-005ab3f4)
- 新版 `005ab428`（命令位置の公開資料なし） · `005ab434`（命令位置の公開資料なし）

~~~diff
- 005ab3e8 ["COPY", "tmp:0:8", ["const:350:8"]]
- 005ab3e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab3e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab3e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab428 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 005ab428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab3e8 bytes 08410d91
+ 005ab428 bytes 08811091
- 005ab3f4 ["INT_ADD", "register:40f0:8", ["const:5ab3f4:8", "const:4:8"]]
- 005ab3f4 ["CALL", null, ["callee:00c57f70:8"]]
+ 005ab434 ["INT_ADD", "register:40f0:8", ["const:5ab434:8", "const:4:8"]]
+ 005ab434 ["CALL", null, ["callee:00c57f70:8"]]
- 005ab3f4 bytes abb21a94
+ 005ab434 bytes cfb21a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9b1178154d1ada9a4a0d842feafd636"></a>

### [`005ab410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab410.md) → [`005ab450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab450.md) _INIT_56

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ab48c",
      "incomplete_value": true,
      "site": "005ab4a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ab44c",
      "incomplete_value": true,
      "site": "005ab468",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ab4b0",
      "incomplete_value": true,
      "site": "005ab4cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ab470",
      "incomplete_value": true,
      "site": "005ab48c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ab4d0",
      "incomplete_value": true,
      "site": "005ab4ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ab490",
      "incomplete_value": true,
      "site": "005ab4ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005ab48c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005ab4b0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005ab4d0",
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
      "005ab48c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005ab4b0",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005ab4d0",
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

- 旧版 [`005ab488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab410.md#insn-005ab488) · [`005ab4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab410.md#insn-005ab4a8) · [`005ab570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab410.md#insn-005ab570)
- 新版 `005ab4c8`（命令位置の公開資料なし） · `005ab4e8`（命令位置の公開資料なし） · `005ab5b0`（命令位置の公開資料なし）

~~~diff
- 005ab488 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 005ab488 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005ab488 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005ab488 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005ab4c8 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 005ab4c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005ab4c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005ab4c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005ab488 bytes 4a093791
+ 005ab4c8 bytes 4ab93591
- 005ab4a8 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005ab4a8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005ab4a8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005ab4a8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005ab4e8 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005ab4e8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005ab4e8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005ab4e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005ab4a8 bytes 4a893d91
+ 005ab4e8 bytes 4a553c91
- 005ab570 ["INT_ADD", "register:40f0:8", ["const:5ab570:8", "const:4:8"]]
- 005ab570 ["CALL", null, ["callee:0043b838:8"]]
+ 005ab5b0 ["INT_ADD", "register:40f0:8", ["const:5ab5b0:8", "const:4:8"]]
+ 005ab5b0 ["CALL", null, ["callee:0043b838:8"]]
- 005ab570 bytes a240fa97
+ 005ab5b0 bytes a240fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9202913abe9bc453232b464c0709e52c"></a>

### [`005ab7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab7a0.md) → [`005ab7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab7e0.md) FUN_005ab7e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005ab914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab914.md) · 呼出先 6件 [`0059b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b8dc.md) [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005ab954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab954.md) · 呼出先 6件 [`0059b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b91c.md) [`005aa1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1b0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.70% / 新版 95.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ab814",
      "incomplete_value": false,
      "site": "005ab818",
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
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ab7d4",
      "incomplete_value": false,
      "site": "005ab7d8",
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
            "const:3a0:8"
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
      "definition_site": "005ab910",
      "incomplete_value": false,
      "site": "005ab914",
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
      "definition_site": "005ab8d0",
      "incomplete_value": false,
      "site": "005ab8d4",
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
      "005ab818",
      "DATA",
      [
        "storage",
        "00c6f3a0",
        null,
        "pointer"
      ]
    ],
    [
      "005ab914",
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
      "005ab818",
      "DATA",
      [
        "storage",
        "00c6f470",
        null,
        "pointer"
      ]
    ],
    [
      "005ab914",
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

- 旧版 [`005ab7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab7a0.md#insn-005ab7cc) · [`005ab7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab7a0.md#insn-005ab7d4) · [`005ab850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab7a0.md#insn-005ab850)
- 新版 `005ab80c`（命令位置の公開資料なし） · `005ab814`（命令位置の公開資料なし） · `005ab890`（命令位置の公開資料なし）

~~~diff
- 005ab7cc ["INT_ADD", "register:40f0:8", ["const:5ab7cc:8", "const:4:8"]]
- 005ab7cc ["CALL", null, ["callee:0059b91c:8"]]
+ 005ab80c ["INT_ADD", "register:40f0:8", ["const:5ab80c:8", "const:4:8"]]
+ 005ab80c ["CALL", null, ["callee:0059b91c:8"]]
- 005ab7cc bytes 44c0ff97
+ 005ab80c bytes 44c0ff97
- 005ab7d4 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 005ab7d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ab7d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ab7d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ab814 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 005ab814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ab814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ab7d4 bytes 08810e91
+ 005ab814 bytes 08c11191
- 005ab850 ["INT_ADD", "register:40f0:8", ["const:5ab850:8", "const:4:8"]]
- 005ab850 ["CALL", null, ["callee:00c57f60:8"]]
+ 005ab890 ["INT_ADD", "register:40f0:8", ["const:5ab890:8", "const:4:8"]]
+ 005ab890 ["CALL", null, ["callee:00c57f60:8"]]
- 005ab850 bytes 90b11a94
+ 005ab890 bytes b4b11a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63404bbbd14151696b57f17379cd352b"></a>

### [`005ab914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab914.md) → [`005ab954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab954.md) FUN_005ab954

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005ab7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab7a0.md) [`009b3798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3798.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`005ab7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab7e0.md) [`009b37ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b37ec.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.76% / 新版 95.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ab9b0",
      "incomplete_value": true,
      "site": "005ab9b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "005ab970",
      "incomplete_value": true,
      "site": "005ab970",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005abae8",
      "incomplete_value": true,
      "site": "005abae8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005abaa8",
      "incomplete_value": true,
      "site": "005abaa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f2d:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005abc1c",
      "incomplete_value": true,
      "site": "005abc1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005abbdc",
      "incomplete_value": true,
      "site": "005abbdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d2:8"
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
      "005ab9a0",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "005abad4",
      "READ",
      [
        "storage",
        "0029ff2d",
        null,
        "string"
      ]
    ],
    [
      "005abc0c",
      "READ",
      [
        "storage",
        "002b90d2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005ab9a0",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "005abad4",
      "READ",
      [
        "storage",
        "0029fee0",
        null,
        "string"
      ]
    ],
    [
      "005abc0c",
      "READ",
      [
        "storage",
        "002b907e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aba68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab914.md#insn-005aba68) · [`005abae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab914.md#insn-005abae8) · [`005ab95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab914.md#insn-005ab95c)
- 新版 `005abaa8`（命令位置の公開資料なし） · `005abb28`（命令位置の公開資料なし） · `005ab99c`（命令位置の公開資料なし）

~~~diff
- 005aba68 ["INT_ADD", "register:40f0:8", ["const:5aba68:8", "const:4:8"]]
- 005aba68 ["CALL", null, ["callee:00c57f80:8"]]
+ 005abaa8 ["INT_ADD", "register:40f0:8", ["const:5abaa8:8", "const:4:8"]]
+ 005abaa8 ["CALL", null, ["callee:00c57f80:8"]]
- 005aba68 bytes 12b11a94
+ 005abaa8 bytes 36b11a94
- 005abae8 ["INT_ADD", "register:40f0:8", ["const:5abae8:8", "const:4:8"]]
- 005abae8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005abb28 ["INT_ADD", "register:40f0:8", ["const:5abb28:8", "const:4:8"]]
+ 005abb28 ["CALL", null, ["callee:00c57f80:8"]]
- 005abae8 bytes f2b01a94
+ 005abb28 bytes 16b11a94
- 005ab95c ["COPY", "tmp:0:8", ["const:1a5:8"]]
- 005ab95c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ab95c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ab95c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ab99c ["COPY", "tmp:0:8", ["const:1e5:8"]]
+ 005ab99c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ab99c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ab99c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ab95c bytes 29950691
+ 005ab99c bytes 29950791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a8ce43faf120205445ecf02222d9ab0"></a>

### [`005abff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005abff0.md) → [`005ac030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac030.md) FUN_005ac030

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009b4164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4164.md) · 呼出先 1件 [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md)
- 新版 呼出元 1件 [`009b41b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b41b8.md) · 呼出先 1件 [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md)

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
      "definition_site": "005ac058",
      "incomplete_value": false,
      "site": "005ac060",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac018",
      "incomplete_value": false,
      "site": "005ac020",
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
            "const:3c0:8"
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
      "005ac060",
      "DATA",
      [
        "storage",
        "00c6f3c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ac060",
      "DATA",
      [
        "storage",
        "00c6f490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005abff0.md#insn-005ac010) · [`005ac018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005abff0.md#insn-005ac018)
- 新版 `005ac050`（命令位置の公開資料なし） · `005ac058`（命令位置の公開資料なし）

~~~diff
- 005ac010 ["INT_ADD", "register:40f0:8", ["const:5ac010:8", "const:4:8"]]
- 005ac010 ["CALL", null, ["callee:0059b948:8"]]
+ 005ac050 ["INT_ADD", "register:40f0:8", ["const:5ac050:8", "const:4:8"]]
+ 005ac050 ["CALL", null, ["callee:0059b948:8"]]
- 005ac010 bytes 3ebeff97
+ 005ac050 bytes 3ebeff97
- 005ac018 ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 005ac018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac058 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 005ac058 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac058 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac058 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac018 bytes 08010f91
+ 005ac058 bytes 08411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3194ed0aa112a2b95a6f94da29105d95"></a>

### [`005ac054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac054.md) → [`005ac094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac094.md) FUN_005ac094

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58020.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.74% / 新版 96.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005ac0f8",
      "incomplete_value": false,
      "site": "005ac100",
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
            "const:6c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac0b8",
      "incomplete_value": false,
      "site": "005ac0c0",
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
            "const:722:8"
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
      "definition_site": "005ac15c",
      "incomplete_value": false,
      "site": "005ac164",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac11c",
      "incomplete_value": false,
      "site": "005ac124",
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
            "const:d94:8"
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
      "005ac0cc",
      "PARAM",
      [
        "storage",
        "002b0d86",
        null,
        "string"
      ]
    ],
    [
      "005ac0f8",
      "PARAM",
      [
        "storage",
        "002a5722",
        null,
        "string"
      ]
    ],
    [
      "005ac15c",
      "PARAM",
      [
        "storage",
        "002b0d94",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005ac0cc",
      "PARAM",
      [
        "storage",
        "002b0d2a",
        null,
        "string"
      ]
    ],
    [
      "005ac0f8",
      "PARAM",
      [
        "storage",
        "002a56c6",
        null,
        "string"
      ]
    ],
    [
      "005ac15c",
      "PARAM",
      [
        "storage",
        "002b0d38",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac054.md#insn-005ac0c0) · [`005ac124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac054.md#insn-005ac124) · [`005ac164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac054.md#insn-005ac164)
- 新版 `005ac100`（命令位置の公開資料なし） · `005ac164`（命令位置の公開資料なし） · `005ac1a4`（命令位置の公開資料なし）

~~~diff
- 005ac0c0 ["INT_ADD", "register:40f0:8", ["const:5ac0c0:8", "const:4:8"]]
- 005ac0c0 ["CALL", null, ["callee:00c58040:8"]]
+ 005ac100 ["INT_ADD", "register:40f0:8", ["const:5ac100:8", "const:4:8"]]
+ 005ac100 ["CALL", null, ["callee:00c58040:8"]]
- 005ac0c0 bytes acaf1a94
+ 005ac100 bytes d0af1a94
- 005ac124 ["INT_ADD", "register:40f0:8", ["const:5ac124:8", "const:4:8"]]
- 005ac124 ["CALL", null, ["callee:00c58040:8"]]
+ 005ac164 ["INT_ADD", "register:40f0:8", ["const:5ac164:8", "const:4:8"]]
+ 005ac164 ["CALL", null, ["callee:00c58040:8"]]
- 005ac124 bytes 93af1a94
+ 005ac164 bytes b7af1a94
- 005ac164 ["INT_ADD", "register:40f0:8", ["const:5ac164:8", "const:4:8"]]
- 005ac164 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ac1a4 ["INT_ADD", "register:40f0:8", ["const:5ac1a4:8", "const:4:8"]]
+ 005ac1a4 ["CALL", null, ["callee:00c57f80:8"]]
- 005ac164 bytes 53af1a94
+ 005ac1a4 bytes 77af1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dff312e4bdc36248368f7555d7d0888"></a>

### [`005ac39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac39c.md) → [`005ac3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac3dc.md) FUN_005ac3dc

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
      "definition_site": "005ac3f8",
      "incomplete_value": false,
      "site": "005ac400",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac3b8",
      "incomplete_value": false,
      "site": "005ac3c0",
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
            "const:4c8:8"
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
      "definition_site": "005ac410",
      "incomplete_value": false,
      "site": "005ac410",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac3d0",
      "incomplete_value": false,
      "site": "005ac3d0",
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
            "const:418:8"
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
      "005ac400",
      "DATA",
      [
        "storage",
        "00c6f4c8",
        null,
        "undefined *"
      ]
    ],
    [
      "005ac410",
      "DATA",
      [
        "storage",
        "00c6f418",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005ac400",
      "DATA",
      [
        "storage",
        "00c6f598",
        null,
        "undefined *"
      ]
    ],
    [
      "005ac410",
      "DATA",
      [
        "storage",
        "00c6f4e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac39c.md#insn-005ac3b0) · [`005ac3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac39c.md#insn-005ac3b8) · [`005ac3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac39c.md#insn-005ac3c4)
- 新版 `005ac3f0`（命令位置の公開資料なし） · `005ac3f8`（命令位置の公開資料なし）

~~~diff
- 005ac3b0 ["INT_ADD", "register:40f0:8", ["const:5ac3b0:8", "const:4:8"]]
- 005ac3b0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005ac3f0 ["INT_ADD", "register:40f0:8", ["const:5ac3f0:8", "const:4:8"]]
+ 005ac3f0 ["CALL", null, ["callee:00c57f60:8"]]
- 005ac3b0 bytes b8ae1a94
+ 005ac3f0 bytes dcae1a94
- 005ac3b8 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 005ac3b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac3b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac3f8 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 005ac3f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac3f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac3f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac3b8 bytes 08211391
+ 005ac3f8 bytes 08611691
- 005ac3c4 ["COPY", "register:4040:8", ["const:c6f000:8"]]
- 005ac3c4 bytes 083600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fe3f423f7a2ad015922f4c718f41ed4"></a>

### [`005ac3e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac3e4.md) → [`005ac424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac424.md) FUN_005ac424

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
      "definition_site": "005ac450",
      "incomplete_value": false,
      "site": "005ac454",
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
      "definition_site": "005ac410",
      "incomplete_value": false,
      "site": "005ac414",
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
      "005ac454",
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
      "005ac454",
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

- 旧版 [`005ac400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac3e4.md#insn-005ac400) · [`005ac408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac3e4.md#insn-005ac408) · [`005ac420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac3e4.md#insn-005ac420)
- 新版 `005ac440`（命令位置の公開資料なし） · `005ac448`（命令位置の公開資料なし） · `005ac460`（命令位置の公開資料なし）

~~~diff
- 005ac400 ["INT_ADD", "register:40f0:8", ["const:5ac400:8", "const:4:8"]]
- 005ac400 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ac440 ["INT_ADD", "register:40f0:8", ["const:5ac440:8", "const:4:8"]]
+ 005ac440 ["CALL", null, ["callee:00c57f80:8"]]
- 005ac400 bytes acae1a94
+ 005ac440 bytes d0ae1a94
- 005ac408 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005ac408 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac408 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac448 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005ac448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac408 bytes 08412891
+ 005ac448 bytes 08812b91
- 005ac420 ["INT_ADD", "register:40f0:8", ["const:5ac420:8", "const:4:8"]]
- 005ac420 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ac460 ["INT_ADD", "register:40f0:8", ["const:5ac460:8", "const:4:8"]]
+ 005ac460 ["CALL", null, ["callee:00c57f80:8"]]
- 005ac420 bytes a4ae1a94
+ 005ac460 bytes c8ae1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d930d47dbedacb12b755fd7dfb7c72d5"></a>

### [`005ac4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac4a8.md) → [`005ac4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac4e8.md) FUN_005ac4e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005ac530",
      "incomplete_value": false,
      "site": "005ac534",
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
      "definition_site": "005ac4f0",
      "incomplete_value": false,
      "site": "005ac4f4",
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
      "005ac534",
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
      "005ac534",
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

- 旧版 [`005ac4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac4a8.md#insn-005ac4c4) · [`005ac4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac4a8.md#insn-005ac4d4) · [`005ac4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac4a8.md#insn-005ac4e4)
- 新版 `005ac504`（命令位置の公開資料なし） · `005ac514`（命令位置の公開資料なし） · `005ac524`（命令位置の公開資料なし）

~~~diff
- 005ac4c4 ["INT_ADD", "register:40f0:8", ["const:5ac4c4:8", "const:4:8"]]
- 005ac4c4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ac504 ["INT_ADD", "register:40f0:8", ["const:5ac504:8", "const:4:8"]]
+ 005ac504 ["CALL", null, ["callee:00c57f80:8"]]
- 005ac4c4 bytes 7bae1a94
+ 005ac504 bytes 9fae1a94
- 005ac4d4 ["INT_ADD", "register:40f0:8", ["const:5ac4d4:8", "const:4:8"]]
- 005ac4d4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ac514 ["INT_ADD", "register:40f0:8", ["const:5ac514:8", "const:4:8"]]
+ 005ac514 ["CALL", null, ["callee:00c57f80:8"]]
- 005ac4d4 bytes 77ae1a94
+ 005ac514 bytes 9bae1a94
- 005ac4e4 ["INT_ADD", "register:40f0:8", ["const:5ac4e4:8", "const:4:8"]]
- 005ac4e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ac524 ["INT_ADD", "register:40f0:8", ["const:5ac524:8", "const:4:8"]]
+ 005ac524 ["CALL", null, ["callee:00c57f80:8"]]
- 005ac4e4 bytes 73ae1a94
+ 005ac524 bytes 97ae1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d735d9f8f9c7b36577b6613b9cf86b3c"></a>

### [`005ac518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac518.md) → [`005ac558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac558.md) FUN_005ac558

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005ac5a0",
      "incomplete_value": false,
      "site": "005ac5a4",
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
      "definition_site": "005ac560",
      "incomplete_value": false,
      "site": "005ac564",
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
      "005ac5a4",
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
      "005ac5a4",
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

- 旧版 [`005ac534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac518.md#insn-005ac534) · [`005ac544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac518.md#insn-005ac544) · [`005ac554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac518.md#insn-005ac554)
- 新版 `005ac574`（命令位置の公開資料なし） · `005ac584`（命令位置の公開資料なし） · `005ac594`（命令位置の公開資料なし）

~~~diff
- 005ac534 ["INT_ADD", "register:40f0:8", ["const:5ac534:8", "const:4:8"]]
- 005ac534 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ac574 ["INT_ADD", "register:40f0:8", ["const:5ac574:8", "const:4:8"]]
+ 005ac574 ["CALL", null, ["callee:00c57f80:8"]]
- 005ac534 bytes 5fae1a94
+ 005ac574 bytes 83ae1a94
- 005ac544 ["INT_ADD", "register:40f0:8", ["const:5ac544:8", "const:4:8"]]
- 005ac544 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ac584 ["INT_ADD", "register:40f0:8", ["const:5ac584:8", "const:4:8"]]
+ 005ac584 ["CALL", null, ["callee:00c57f80:8"]]
- 005ac544 bytes 5bae1a94
+ 005ac584 bytes 7fae1a94
- 005ac554 ["INT_ADD", "register:40f0:8", ["const:5ac554:8", "const:4:8"]]
- 005ac554 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ac594 ["INT_ADD", "register:40f0:8", ["const:5ac594:8", "const:4:8"]]
+ 005ac594 ["CALL", null, ["callee:00c57f80:8"]]
- 005ac554 bytes 57ae1a94
+ 005ac594 bytes 7bae1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef68031bf65c1c310b3ea29389d54929"></a>

### [`005ac584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac584.md) → [`005ac5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac5c4.md) FUN_005ac5c4

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
      "definition_site": "005ac5c8",
      "incomplete_value": false,
      "site": "005ac5cc",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac588",
      "incomplete_value": false,
      "site": "005ac58c",
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
      "005ac5cc",
      "DATA",
      [
        "storage",
        "00c6f478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ac5cc",
      "DATA",
      [
        "storage",
        "00c6f548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac584.md#insn-005ac588)
- 新版 `005ac5c8`（命令位置の公開資料なし）

~~~diff
- 005ac588 ["COPY", "tmp:0:8", ["const:478:8"]]
- 005ac588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac5c8 ["COPY", "tmp:0:8", ["const:548:8"]]
+ 005ac5c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac5c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac5c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac588 bytes 08e11191
+ 005ac5c8 bytes 08211591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b27dd0bc9604d27b40fd701c0726c42"></a>

### [`005ac594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac594.md) → [`005ac5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac5d4.md) FUN_005ac5d4

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
      "definition_site": "005ac5e4",
      "incomplete_value": false,
      "site": "005ac5ec",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac5a4",
      "incomplete_value": false,
      "site": "005ac5ac",
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
      "005ac5ec",
      "DATA",
      [
        "storage",
        "00c6f478",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ac5ec",
      "DATA",
      [
        "storage",
        "00c6f548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac594.md#insn-005ac5a4) · [`005ac5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac594.md#insn-005ac5b0)
- 新版 `005ac5e4`（命令位置の公開資料なし） · `005ac5f0`（命令位置の公開資料なし）

~~~diff
- 005ac5a4 ["COPY", "tmp:0:8", ["const:478:8"]]
- 005ac5a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac5a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac5a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac5e4 ["COPY", "tmp:0:8", ["const:548:8"]]
+ 005ac5e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac5e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac5e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac5a4 bytes 08e11191
+ 005ac5e4 bytes 08211591
- 005ac5b0 ["INT_ADD", "register:40f0:8", ["const:5ac5b0:8", "const:4:8"]]
- 005ac5b0 ["CALL", null, ["callee:00c57f70:8"]]
+ 005ac5f0 ["INT_ADD", "register:40f0:8", ["const:5ac5f0:8", "const:4:8"]]
+ 005ac5f0 ["CALL", null, ["callee:00c57f70:8"]]
- 005ac5b0 bytes 3cae1a94
+ 005ac5f0 bytes 60ae1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41585118724ad5c58cef5f0eec73792a"></a>

### [`005ac5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac5c4.md) → [`005ac604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac604.md) FUN_005ac604

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005ac64c",
      "incomplete_value": false,
      "site": "005ac650",
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
      "definition_site": "005ac60c",
      "incomplete_value": false,
      "site": "005ac610",
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
      "005ac650",
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
      "005ac650",
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

- 旧版 [`005ac5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac5c4.md#insn-005ac5e0) · [`005ac5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac5c4.md#insn-005ac5f0) · [`005ac600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac5c4.md#insn-005ac600)
- 新版 `005ac620`（命令位置の公開資料なし） · `005ac630`（命令位置の公開資料なし） · `005ac640`（命令位置の公開資料なし）

~~~diff
- 005ac5e0 ["INT_ADD", "register:40f0:8", ["const:5ac5e0:8", "const:4:8"]]
- 005ac5e0 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ac620 ["INT_ADD", "register:40f0:8", ["const:5ac620:8", "const:4:8"]]
+ 005ac620 ["CALL", null, ["callee:00c57f80:8"]]
- 005ac5e0 bytes 34ae1a94
+ 005ac620 bytes 58ae1a94
- 005ac5f0 ["INT_ADD", "register:40f0:8", ["const:5ac5f0:8", "const:4:8"]]
- 005ac5f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ac630 ["INT_ADD", "register:40f0:8", ["const:5ac630:8", "const:4:8"]]
+ 005ac630 ["CALL", null, ["callee:00c57f80:8"]]
- 005ac5f0 bytes 30ae1a94
+ 005ac630 bytes 54ae1a94
- 005ac600 ["INT_ADD", "register:40f0:8", ["const:5ac600:8", "const:4:8"]]
- 005ac600 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ac640 ["INT_ADD", "register:40f0:8", ["const:5ac640:8", "const:4:8"]]
+ 005ac640 ["CALL", null, ["callee:00c57f80:8"]]
- 005ac600 bytes 2cae1a94
+ 005ac640 bytes 50ae1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e4646c36fd1857822b861c7a16eb5d6"></a>

### [`005ac638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac638.md) → [`005ac678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac678.md) FUN_005ac678

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
      "definition_site": "005ac67c",
      "incomplete_value": false,
      "site": "005ac680",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac63c",
      "incomplete_value": false,
      "site": "005ac640",
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
      "005ac680",
      "DATA",
      [
        "storage",
        "00c6f4c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ac680",
      "DATA",
      [
        "storage",
        "00c6f598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac638.md#insn-005ac63c)
- 新版 `005ac67c`（命令位置の公開資料なし）

~~~diff
- 005ac63c ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 005ac63c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac63c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac63c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac67c ["COPY", "tmp:0:8", ["const:598:8"]]
+ 005ac67c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac67c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac67c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac63c bytes 08211391
+ 005ac67c bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9308569c2a295f291cda1b01c614a8ee"></a>

### [`005ac648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac648.md) → [`005ac688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac688.md) FUN_005ac688

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
      "definition_site": "005ac698",
      "incomplete_value": false,
      "site": "005ac6a0",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ac658",
      "incomplete_value": false,
      "site": "005ac660",
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
      "005ac6a0",
      "DATA",
      [
        "storage",
        "00c6f4c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ac6a0",
      "DATA",
      [
        "storage",
        "00c6f598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac648.md#insn-005ac658) · [`005ac664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac648.md#insn-005ac664)
- 新版 `005ac698`（命令位置の公開資料なし） · `005ac6a4`（命令位置の公開資料なし）

~~~diff
- 005ac658 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 005ac658 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ac658 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ac658 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ac698 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 005ac698 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac698 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ac698 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ac658 bytes 08211391
+ 005ac698 bytes 08611691
- 005ac664 ["INT_ADD", "register:40f0:8", ["const:5ac664:8", "const:4:8"]]
- 005ac664 ["CALL", null, ["callee:00c57f70:8"]]
+ 005ac6a4 ["INT_ADD", "register:40f0:8", ["const:5ac6a4:8", "const:4:8"]]
+ 005ac6a4 ["CALL", null, ["callee:00c57f70:8"]]
- 005ac664 bytes 0fae1a94
+ 005ac6a4 bytes 33ae1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff9635f354bd551b4eaaf41a7e05083e"></a>

### [`005ac680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac680.md) → [`005ac6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac6c0.md) _INIT_57

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ac6fc",
      "incomplete_value": true,
      "site": "005ac718",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ac6bc",
      "incomplete_value": true,
      "site": "005ac6d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ac740",
      "incomplete_value": true,
      "site": "005ac75c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005ac700",
      "incomplete_value": true,
      "site": "005ac71c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005ac8e0",
      "incomplete_value": false,
      "site": "005ac8f4",
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
      "definition_site": "005ac8a0",
      "incomplete_value": false,
      "site": "005ac8b4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005ac6fc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005ac720",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005ac740",
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
      "005ac6fc",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005ac720",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005ac740",
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

- 旧版 [`005ac718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac680.md#insn-005ac718) · [`005ac8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac680.md#insn-005ac8b4) · [`005ac6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ac680.md#insn-005ac6ac)
- 新版 `005ac758`（命令位置の公開資料なし） · `005ac8f4`（命令位置の公開資料なし） · `005ac6ec`（命令位置の公開資料なし）

~~~diff
- 005ac718 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005ac718 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005ac718 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005ac718 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005ac758 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005ac758 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005ac758 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005ac758 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005ac718 bytes 4a893d91
+ 005ac758 bytes 4a553c91
- 005ac8b4 ["INT_ADD", "register:40f0:8", ["const:5ac8b4:8", "const:4:8"]]
- 005ac8b4 ["CALL", null, ["callee:00c57f00:8"]]
+ 005ac8f4 ["INT_ADD", "register:40f0:8", ["const:5ac8f4:8", "const:4:8"]]
+ 005ac8f4 ["CALL", null, ["callee:00c57f00:8"]]
- 005ac8b4 bytes 5fad1a94
+ 005ac8f4 bytes 83ad1a94
- 005ac6ac ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 005ac6ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005ac6ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005ac6ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005ac6ec ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 005ac6ec ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005ac6ec ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005ac6ec ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005ac6ac bytes 73821f91
+ 005ac6ec bytes 73822391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91c0e9ea77983baf4391fbc06b87d594"></a>

### [`005aca10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca10.md) → [`005aca50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005aca50.md) FUN_005aca50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b8a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8a64.md) · 呼出先 1件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md)
- 新版 呼出元 1件 [`005b8aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8aa4.md) · 呼出先 1件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md)

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
      "definition_site": "005aca68",
      "incomplete_value": false,
      "site": "005aca70",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aca28",
      "incomplete_value": false,
      "site": "005aca30",
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
            "const:518:8"
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
      "005aca70",
      "DATA",
      [
        "storage",
        "00c6f518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005aca70",
      "DATA",
      [
        "storage",
        "00c6f5e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aca20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca10.md#insn-005aca20) · [`005aca28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca10.md#insn-005aca28)
- 新版 `005aca60`（命令位置の公開資料なし） · `005aca68`（命令位置の公開資料なし）

~~~diff
- 005aca20 ["INT_ADD", "register:40f0:8", ["const:5aca20:8", "const:4:8"]]
- 005aca20 ["CALL", null, ["callee:00597f10:8"]]
+ 005aca60 ["INT_ADD", "register:40f0:8", ["const:5aca60:8", "const:4:8"]]
+ 005aca60 ["CALL", null, ["callee:00597f10:8"]]
- 005aca20 bytes 2cadff97
+ 005aca60 bytes 2cadff97
- 005aca28 ["COPY", "tmp:0:8", ["const:518:8"]]
- 005aca28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005aca28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005aca28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005aca68 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 005aca68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005aca68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005aca68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005aca28 bytes 08611491
+ 005aca68 bytes 08a11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-113a818bbbd209d5e005986b5426af51"></a>

### [`005aca44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md) → [`005aca84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005aca84.md) FUN_005aca84

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00597efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md) [`0059a498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a498.md) [`005ace80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005ace80.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00597f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md) [`0059a4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a4d8.md) [`005acec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005acec0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005acc90",
      "incomplete_value": false,
      "site": "005acc98",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005acc50",
      "incomplete_value": false,
      "site": "005acc58",
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
            "const:560:8"
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
      "005acc98",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ],
    [
      "005acd20",
      "READ",
      [
        "storage",
        "00c6f588",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005acc98",
      "DATA",
      [
        "storage",
        "00c6f630",
        null,
        "undefined *"
      ]
    ],
    [
      "005acd20",
      "READ",
      [
        "storage",
        "00c6f658",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aca70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md#insn-005aca70) · [`005aca90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md#insn-005aca90) · [`005acaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca44.md#insn-005acaa4)
- 新版 `005acab0`（命令位置の公開資料なし） · `005acad0`（命令位置の公開資料なし） · `005acae4`（命令位置の公開資料なし）

~~~diff
- 005aca70 ["INT_ADD", "register:40f0:8", ["const:5aca70:8", "const:4:8"]]
- 005aca70 ["CALL", null, ["callee:00597f3c:8"]]
+ 005acab0 ["INT_ADD", "register:40f0:8", ["const:5acab0:8", "const:4:8"]]
+ 005acab0 ["CALL", null, ["callee:00597f3c:8"]]
- 005aca70 bytes 23adff97
+ 005acab0 bytes 23adff97
- 005aca90 ["INT_ADD", "register:40f0:8", ["const:5aca90:8", "const:4:8"]]
- 005aca90 ["CALL", null, ["callee:00c53da0:8"]]
+ 005acad0 ["INT_ADD", "register:40f0:8", ["const:5acad0:8", "const:4:8"]]
+ 005acad0 ["CALL", null, ["callee:00c53da0:8"]]
- 005aca90 bytes 9c9c1a94
+ 005acad0 bytes b49c1a94
- 005acaa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005acaa4 ["INT_ADD", "register:40f0:8", ["const:5acaa4:8", "const:4:8"]]
- 005acaa4 ["CALLIND", null, ["register:0:8"]]
+ 005acae4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005acae4 ["INT_ADD", "register:40f0:8", ["const:5acae4:8", "const:4:8"]]
+ 005acae4 ["CALLIND", null, ["register:0:8"]]
- 005acaa4 bytes 00013fd6
+ 005acae4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12f08ddaca225af78ed0018cf5cc6f4c"></a>

### [`005acec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005acec0.md) → [`005acf00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005acf00.md) FUN_005acf00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00597efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597efc.md) [`005ae884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae884.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00597f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f3c.md) [`005ae8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae8c4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ad0c4",
      "incomplete_value": false,
      "site": "005ad0cc",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad084",
      "incomplete_value": false,
      "site": "005ad08c",
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
            "const:5e0:8"
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
      "005ad0cc",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ],
    [
      "005ad14c",
      "READ",
      [
        "storage",
        "00c6f608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad0cc",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005ad14c",
      "READ",
      [
        "storage",
        "00c6f6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005acef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005acec0.md#insn-005acef0) · [`005acf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005acec0.md#insn-005acf10) · [`005acf24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005acec0.md#insn-005acf24)
- 新版 `005acf30`（命令位置の公開資料なし） · `005acf50`（命令位置の公開資料なし） · `005acf64`（命令位置の公開資料なし）

~~~diff
- 005acef0 ["INT_ADD", "register:40f0:8", ["const:5acef0:8", "const:4:8"]]
- 005acef0 ["CALL", null, ["callee:00597f3c:8"]]
+ 005acf30 ["INT_ADD", "register:40f0:8", ["const:5acf30:8", "const:4:8"]]
+ 005acf30 ["CALL", null, ["callee:00597f3c:8"]]
- 005acef0 bytes 03acff97
+ 005acf30 bytes 03acff97
- 005acf10 ["INT_ADD", "register:40f0:8", ["const:5acf10:8", "const:4:8"]]
- 005acf10 ["CALL", null, ["callee:00c53da0:8"]]
+ 005acf50 ["INT_ADD", "register:40f0:8", ["const:5acf50:8", "const:4:8"]]
+ 005acf50 ["CALL", null, ["callee:00c53da0:8"]]
- 005acf10 bytes 7c9b1a94
+ 005acf50 bytes 949b1a94
- 005acf24 ["COPY", "register:0:8", ["register:4040:8"]]
- 005acf24 ["INT_ADD", "register:40f0:8", ["const:5acf24:8", "const:4:8"]]
- 005acf24 ["CALLIND", null, ["register:0:8"]]
+ 005acf64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005acf64 ["INT_ADD", "register:40f0:8", ["const:5acf64:8", "const:4:8"]]
+ 005acf64 ["CALLIND", null, ["register:0:8"]]
- 005acf24 bytes 00013fd6
+ 005acf64 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5847b14bf352031b52b677f08f1643a"></a>

### [`005ad484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad484.md) → [`005ad4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad4c4.md) FUN_005ad4c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00599e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e54.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00599e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599e94.md)

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
      "definition_site": "005ad4dc",
      "incomplete_value": false,
      "site": "005ad4e8",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad49c",
      "incomplete_value": false,
      "site": "005ad4a8",
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
      "005ad4e8",
      "DATA",
      [
        "storage",
        "00c6f518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad4e8",
      "DATA",
      [
        "storage",
        "00c6f5e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ad49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad484.md#insn-005ad49c) · [`005ad4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad484.md#insn-005ad4cc) · [`005ad4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad484.md#insn-005ad4fc)
- 新版 `005ad4dc`（命令位置の公開資料なし） · `005ad50c`（命令位置の公開資料なし） · `005ad53c`（命令位置の公開資料なし）

~~~diff
- 005ad49c ["COPY", "tmp:0:8", ["const:518:8"]]
- 005ad49c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ad49c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ad49c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ad4dc ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 005ad4dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ad4dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ad4dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ad49c bytes 08611491
+ 005ad4dc bytes 08a11791
- 005ad4cc ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad4cc ["INT_ADD", "register:40f0:8", ["const:5ad4cc:8", "const:4:8"]]
- 005ad4cc ["CALLIND", null, ["register:0:8"]]
+ 005ad50c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad50c ["INT_ADD", "register:40f0:8", ["const:5ad50c:8", "const:4:8"]]
+ 005ad50c ["CALLIND", null, ["register:0:8"]]
- 005ad4cc bytes 00013fd6
+ 005ad50c bytes 00013fd6
- 005ad4fc ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad4fc ["INT_ADD", "register:40f0:8", ["const:5ad4fc:8", "const:4:8"]]
- 005ad4fc ["CALLIND", null, ["register:0:8"]]
+ 005ad53c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad53c ["INT_ADD", "register:40f0:8", ["const:5ad53c:8", "const:4:8"]]
+ 005ad53c ["CALLIND", null, ["register:0:8"]]
- 005ad4fc bytes 00013fd6
+ 005ad53c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-182341b168a6beecd93ad5f6a5745b73"></a>

### [`005ad510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad510.md) → [`005ad550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad550.md) FUN_005ad550

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00599e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599e54.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00599e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599e94.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005ad568",
      "incomplete_value": false,
      "site": "005ad574",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad528",
      "incomplete_value": false,
      "site": "005ad534",
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
      "005ad574",
      "DATA",
      [
        "storage",
        "00c6f518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad574",
      "DATA",
      [
        "storage",
        "00c6f5e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ad528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad510.md#insn-005ad528) · [`005ad558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad510.md#insn-005ad558) · [`005ad588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad510.md#insn-005ad588)
- 新版 `005ad568`（命令位置の公開資料なし） · `005ad598`（命令位置の公開資料なし） · `005ad5c8`（命令位置の公開資料なし）

~~~diff
- 005ad528 ["COPY", "tmp:0:8", ["const:518:8"]]
- 005ad528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ad528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ad528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ad568 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 005ad568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ad568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ad568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ad528 bytes 08611491
+ 005ad568 bytes 08a11791
- 005ad558 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad558 ["INT_ADD", "register:40f0:8", ["const:5ad558:8", "const:4:8"]]
- 005ad558 ["CALLIND", null, ["register:0:8"]]
+ 005ad598 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad598 ["INT_ADD", "register:40f0:8", ["const:5ad598:8", "const:4:8"]]
+ 005ad598 ["CALLIND", null, ["register:0:8"]]
- 005ad558 bytes 00013fd6
+ 005ad598 bytes 00013fd6
- 005ad588 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad588 ["INT_ADD", "register:40f0:8", ["const:5ad588:8", "const:4:8"]]
- 005ad588 ["CALLIND", null, ["register:0:8"]]
+ 005ad5c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ad5c8 ["INT_ADD", "register:40f0:8", ["const:5ad5c8:8", "const:4:8"]]
+ 005ad5c8 ["CALLIND", null, ["register:0:8"]]
- 005ad588 bytes 00013fd6
+ 005ad5c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-403efb0100f239a0f2100c80c1f7d87a"></a>

### [`005ad5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5a4.md) → [`005ad5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad5e4.md) FUN_005ad5e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005ad5fc",
      "incomplete_value": false,
      "site": "005ad600",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad5bc",
      "incomplete_value": false,
      "site": "005ad5c0",
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
      "005ad600",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad600",
      "DATA",
      [
        "storage",
        "00c6f630",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ad5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5a4.md#insn-005ad5bc) · [`005ad5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5a4.md#insn-005ad5cc)
- 新版 `005ad5fc`（命令位置の公開資料なし） · `005ad60c`（命令位置の公開資料なし）

~~~diff
- 005ad5bc ["COPY", "tmp:0:8", ["const:560:8"]]
- 005ad5bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ad5bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ad5bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ad5fc ["COPY", "tmp:0:8", ["const:630:8"]]
+ 005ad5fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad5fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad5fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ad5bc bytes 29811591
+ 005ad5fc bytes 29c11891
- 005ad5cc ["INT_ADD", "register:40f0:8", ["const:5ad5cc:8", "const:4:8"]]
- 005ad5cc ["CALL", null, ["callee:00c57f80:8"]]
+ 005ad60c ["INT_ADD", "register:40f0:8", ["const:5ad60c:8", "const:4:8"]]
+ 005ad60c ["CALL", null, ["callee:00c57f80:8"]]
- 005ad5cc bytes 39aa1a94
+ 005ad60c bytes 5daa1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6974241dbcfb54acff9376bb2cfd69f1"></a>

### [`005ad5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5f0.md) → [`005ad630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad630.md) FUN_005ad630

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005ad648",
      "incomplete_value": false,
      "site": "005ad64c",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad608",
      "incomplete_value": false,
      "site": "005ad60c",
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
      "005ad64c",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad64c",
      "DATA",
      [
        "storage",
        "00c6f630",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ad608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5f0.md#insn-005ad608) · [`005ad618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5f0.md#insn-005ad618) · [`005ad624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad5f0.md#insn-005ad624)
- 新版 `005ad648`（命令位置の公開資料なし） · `005ad658`（命令位置の公開資料なし） · `005ad664`（命令位置の公開資料なし）

~~~diff
- 005ad608 ["COPY", "tmp:0:8", ["const:560:8"]]
- 005ad608 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ad608 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ad608 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ad648 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 005ad648 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad648 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad648 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ad608 bytes 29811591
+ 005ad648 bytes 29c11891
- 005ad618 ["INT_ADD", "register:40f0:8", ["const:5ad618:8", "const:4:8"]]
- 005ad618 ["CALL", null, ["callee:00c57f80:8"]]
+ 005ad658 ["INT_ADD", "register:40f0:8", ["const:5ad658:8", "const:4:8"]]
+ 005ad658 ["CALL", null, ["callee:00c57f80:8"]]
- 005ad618 bytes 26aa1a94
+ 005ad658 bytes 4aaa1a94
- 005ad624 ["INT_ADD", "register:40f0:8", ["const:5ad624:8", "const:4:8"]]
- 005ad624 ["CALL", null, ["callee:00c57f50:8"]]
+ 005ad664 ["INT_ADD", "register:40f0:8", ["const:5ad664:8", "const:4:8"]]
+ 005ad664 ["CALL", null, ["callee:00c57f50:8"]]
- 005ad624 bytes 17aa1a94
+ 005ad664 bytes 3baa1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a6f8487b3908c3a234fb6790dbee69b"></a>

### [`005ad638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad638.md) → [`005ad678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad678.md) FUN_005ad678

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "005ad6a0",
      "incomplete_value": false,
      "site": "005ad6a0",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad660",
      "incomplete_value": false,
      "site": "005ad660",
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
            "const:560:8"
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
      "005ad6a0",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad6a0",
      "DATA",
      [
        "storage",
        "00c6f630",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ad6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad638.md#insn-005ad6a0) · [`005ad64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad638.md#insn-005ad64c) · [`005ad65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad638.md#insn-005ad65c)
- 新版 `005ad6e0`（命令位置の公開資料なし） · `005ad68c`（命令位置の公開資料なし） · `005ad69c`（命令位置の公開資料なし）

~~~diff
- 005ad6a0 ["INT_ADD", "register:40f0:8", ["const:5ad6a0:8", "const:4:8"]]
- 005ad6a0 ["CALL", null, ["callee:0043bb60:8"]]
+ 005ad6e0 ["INT_ADD", "register:40f0:8", ["const:5ad6e0:8", "const:4:8"]]
+ 005ad6e0 ["CALL", null, ["callee:0043bb60:8"]]
- 005ad6a0 bytes 2039fa97
+ 005ad6e0 bytes 2039fa97
- 005ad64c ["INT_ADD", "register:40f0:8", ["const:5ad64c:8", "const:4:8"]]
- 005ad64c ["CALL", null, ["callee:00c57f60:8"]]
+ 005ad68c ["INT_ADD", "register:40f0:8", ["const:5ad68c:8", "const:4:8"]]
+ 005ad68c ["CALL", null, ["callee:00c57f60:8"]]
- 005ad64c bytes 11aa1a94
+ 005ad68c bytes 35aa1a94
- 005ad65c ["COPY", "tmp:0:8", ["const:560:8"]]
- 005ad65c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ad65c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ad65c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ad69c ["COPY", "tmp:0:8", ["const:630:8"]]
+ 005ad69c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad69c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad69c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ad65c bytes 29811591
+ 005ad69c bytes 29c11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f13db13e5cf82e7a32db95980f913299"></a>

### [`005ad6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad6d8.md) → [`005ad718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad718.md) FUN_005ad718

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "005ad738",
      "incomplete_value": false,
      "site": "005ad738",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad6f8",
      "incomplete_value": false,
      "site": "005ad6f8",
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
            "const:560:8"
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
      "005ad738",
      "DATA",
      [
        "storage",
        "00c6f560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ad738",
      "DATA",
      [
        "storage",
        "00c6f630",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ad738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad6d8.md#insn-005ad738) · [`005ad6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad6d8.md#insn-005ad6f4) · [`005ad70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad6d8.md#insn-005ad70c)
- 新版 `005ad778`（命令位置の公開資料なし） · `005ad734`（命令位置の公開資料なし） · `005ad74c`（命令位置の公開資料なし）

~~~diff
- 005ad738 ["INT_ADD", "register:40f0:8", ["const:5ad738:8", "const:4:8"]]
- 005ad738 ["CALL", null, ["callee:0043bb60:8"]]
+ 005ad778 ["INT_ADD", "register:40f0:8", ["const:5ad778:8", "const:4:8"]]
+ 005ad778 ["CALL", null, ["callee:0043bb60:8"]]
- 005ad738 bytes fa38fa97
+ 005ad778 bytes fa38fa97
- 005ad6f4 ["COPY", "tmp:0:8", ["const:560:8"]]
- 005ad6f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ad6f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ad6f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ad734 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 005ad734 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad734 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ad734 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ad6f4 bytes 29811591
+ 005ad734 bytes 29c11891
- 005ad70c ["INT_ADD", "register:40f0:8", ["const:5ad70c:8", "const:4:8"]]
- 005ad70c ["CALL", null, ["callee:00c53d70:8"]]
+ 005ad74c ["INT_ADD", "register:40f0:8", ["const:5ad74c:8", "const:4:8"]]
+ 005ad74c ["CALL", null, ["callee:00c53d70:8"]]
- 005ad70c bytes 71991a94
+ 005ad74c bytes 89991a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6c5e92d2ae8298323e63df9706acf64"></a>

### [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) → [`005ad820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad820.md) FUN_005ad820

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 27件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) [`00450750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044fcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fcfc.md) [`004501c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004501c0.md) [`00450790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/00450790.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.53% / 新版 96.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ad924",
      "incomplete_value": true,
      "site": "005ad924",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:93f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ad8e4",
      "incomplete_value": true,
      "site": "005ad8e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:90e:8"
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
      "definition_site": "005addd0",
      "incomplete_value": true,
      "site": "005addd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:702:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005add90",
      "incomplete_value": true,
      "site": "005add90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:756:8"
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
      "definition_site": "005addc4",
      "incomplete_value": true,
      "site": "005addd4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005add84",
      "incomplete_value": true,
      "site": "005add94",
      "value": [
        "LOAD",
        "8",
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
      "005ad910",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ],
    [
      "005ad9d8",
      "READ",
      [
        "storage",
        "002b1993",
        null,
        "string"
      ]
    ],
    [
      "005add20",
      "PARAM",
      [
        "storage",
        "002a8ad9",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005ad910",
      "READ",
      [
        "storage",
        "002b393f",
        null,
        "string"
      ]
    ],
    [
      "005ad9d8",
      "READ",
      [
        "storage",
        "002b1937",
        null,
        "string"
      ]
    ],
    [
      "005add20",
      "PARAM",
      [
        "storage",
        "002a8a7d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005adce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md#insn-005adce8) · [`005add54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md#insn-005add54) · [`005addac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md#insn-005addac)
- 新版 `005add28`（命令位置の公開資料なし） · `005add94`（命令位置の公開資料なし） · `005addec`（命令位置の公開資料なし）

~~~diff
- 005adce8 ["INT_ADD", "register:40f0:8", ["const:5adce8:8", "const:4:8"]]
- 005adce8 ["CALL", null, ["callee:00c58040:8"]]
+ 005add28 ["INT_ADD", "register:40f0:8", ["const:5add28:8", "const:4:8"]]
+ 005add28 ["CALL", null, ["callee:00c58040:8"]]
- 005adce8 bytes a2a81a94
+ 005add28 bytes c6a81a94
- 005add54 ["INT_ADD", "register:40f0:8", ["const:5add54:8", "const:4:8"]]
- 005add54 ["CALL", null, ["callee:00c53da0:8"]]
+ 005add94 ["INT_ADD", "register:40f0:8", ["const:5add94:8", "const:4:8"]]
+ 005add94 ["CALL", null, ["callee:00c53da0:8"]]
- 005add54 bytes eb971a94
+ 005add94 bytes 03981a94
- 005addac ["COPY", "register:0:8", ["register:4048:8"]]
- 005addac ["INT_ADD", "register:40f0:8", ["const:5addac:8", "const:4:8"]]
- 005addac ["CALLIND", null, ["register:0:8"]]
+ 005addec ["COPY", "register:0:8", ["register:4048:8"]]
+ 005addec ["INT_ADD", "register:40f0:8", ["const:5addec:8", "const:4:8"]]
+ 005addec ["CALLIND", null, ["register:0:8"]]
- 005addac bytes 20013fd6
+ 005addec bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bb4d35d77def2d4079b26f79b145fbf"></a>

### [`005ae604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae604.md) → [`005ae644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae644.md) FUN_005ae644

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005ae65c",
      "incomplete_value": false,
      "site": "005ae660",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ae61c",
      "incomplete_value": false,
      "site": "005ae620",
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
            "const:5e0:8"
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
      "005ae660",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ae660",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae604.md#insn-005ae660) · [`005ae61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae604.md#insn-005ae61c) · [`005ae62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae604.md#insn-005ae62c)
- 新版 `005ae6a0`（命令位置の公開資料なし） · `005ae65c`（命令位置の公開資料なし） · `005ae66c`（命令位置の公開資料なし）

~~~diff
- 005ae660 ["COPY", "register:0:8", ["register:4040:8"]]
- 005ae660 ["INT_ADD", "register:40f0:8", ["const:5ae660:8", "const:4:8"]]
- 005ae660 ["CALLIND", null, ["register:0:8"]]
+ 005ae6a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ae6a0 ["INT_ADD", "register:40f0:8", ["const:5ae6a0:8", "const:4:8"]]
+ 005ae6a0 ["CALLIND", null, ["register:0:8"]]
- 005ae660 bytes 00013fd6
+ 005ae6a0 bytes 00013fd6
- 005ae61c ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 005ae61c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ae61c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ae61c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ae65c ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 005ae65c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ae65c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ae65c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ae61c bytes 29811791
+ 005ae65c bytes 29c11a91
- 005ae62c ["INT_ADD", "register:40f0:8", ["const:5ae62c:8", "const:4:8"]]
- 005ae62c ["CALL", null, ["callee:00c57f80:8"]]
+ 005ae66c ["INT_ADD", "register:40f0:8", ["const:5ae66c:8", "const:4:8"]]
+ 005ae66c ["CALL", null, ["callee:00c57f80:8"]]
- 005ae62c bytes 21a61a94
+ 005ae66c bytes 45a61a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13d867f9305b614a547a2835ce231aa0"></a>

### [`005ae674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae674.md) → [`005ae6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae6b4.md) FUN_005ae6b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005ae6cc",
      "incomplete_value": false,
      "site": "005ae6d0",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ae68c",
      "incomplete_value": false,
      "site": "005ae690",
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
            "const:5e0:8"
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
      "005ae6d0",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ae6d0",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae674.md#insn-005ae68c) · [`005ae69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae674.md#insn-005ae69c) · [`005ae6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae674.md#insn-005ae6b0)
- 新版 `005ae6cc`（命令位置の公開資料なし） · `005ae6dc`（命令位置の公開資料なし） · `005ae6f0`（命令位置の公開資料なし）

~~~diff
- 005ae68c ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 005ae68c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005ae68c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005ae68c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005ae6cc ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 005ae6cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005ae6cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005ae6cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005ae68c bytes 29811791
+ 005ae6cc bytes 29c11a91
- 005ae69c ["INT_ADD", "register:40f0:8", ["const:5ae69c:8", "const:4:8"]]
- 005ae69c ["CALL", null, ["callee:00c57f80:8"]]
+ 005ae6dc ["INT_ADD", "register:40f0:8", ["const:5ae6dc:8", "const:4:8"]]
+ 005ae6dc ["CALL", null, ["callee:00c57f80:8"]]
- 005ae69c bytes 05a61a94
+ 005ae6dc bytes 29a61a94
- 005ae6b0 ["INT_ADD", "register:40f0:8", ["const:5ae6b0:8", "const:4:8"]]
- 005ae6b0 ["CALL", null, ["callee:00c53da0:8"]]
+ 005ae6f0 ["INT_ADD", "register:40f0:8", ["const:5ae6f0:8", "const:4:8"]]
+ 005ae6f0 ["CALL", null, ["callee:00c53da0:8"]]
- 005ae6b0 bytes 94951a94
+ 005ae6f0 bytes ac951a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-078bc17a69130a43cf2a8ab04492c232"></a>

### [`005ae6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae6e0.md) → [`005ae720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae720.md) FUN_005ae720

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005ae740",
      "incomplete_value": false,
      "site": "005ae748",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ae700",
      "incomplete_value": false,
      "site": "005ae708",
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
            "const:5e0:8"
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
      "005ae748",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ae748",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae6e0.md#insn-005ae6f8) · [`005ae700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae6e0.md#insn-005ae700) · [`005ae704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae6e0.md#insn-005ae704)
- 新版 `005ae738`（命令位置の公開資料なし） · `005ae740`（命令位置の公開資料なし）

~~~diff
- 005ae6f8 ["INT_ADD", "register:40f0:8", ["const:5ae6f8:8", "const:4:8"]]
- 005ae6f8 ["CALL", null, ["callee:00c57f60:8"]]
+ 005ae738 ["INT_ADD", "register:40f0:8", ["const:5ae738:8", "const:4:8"]]
+ 005ae738 ["CALL", null, ["callee:00c57f60:8"]]
- 005ae6f8 bytes e6a51a94
+ 005ae738 bytes 0aa61a94
- 005ae700 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 005ae700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ae700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ae700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ae740 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 005ae740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ae740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ae740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ae700 bytes 08811791
+ 005ae740 bytes 08c11a91
- 005ae704 ["COPY", "register:4098:8", ["register:4000:8"]]
- 005ae704 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00f375b76a6258f9376e85cb426aa456"></a>

### [`005ae788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae788.md) → [`005ae7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae7c8.md) FUN_005ae7c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "005ae7dc",
      "incomplete_value": false,
      "site": "005ae7e4",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005ae79c",
      "incomplete_value": false,
      "site": "005ae7a4",
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
            "const:5e0:8"
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
      "005ae7e4",
      "DATA",
      [
        "storage",
        "00c6f5e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005ae7e4",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ae79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae788.md#insn-005ae79c) · [`005ae7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae788.md#insn-005ae7cc) · [`005ae7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae788.md#insn-005ae7f8)
- 新版 `005ae7dc`（命令位置の公開資料なし） · `005ae80c`（命令位置の公開資料なし） · `005ae838`（命令位置の公開資料なし）

~~~diff
- 005ae79c ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 005ae79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005ae79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005ae79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005ae7dc ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 005ae7dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005ae7dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005ae7dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005ae79c bytes 08811791
+ 005ae7dc bytes 08c11a91
- 005ae7cc ["INT_ADD", "register:40f0:8", ["const:5ae7cc:8", "const:4:8"]]
- 005ae7cc ["CALL", null, ["callee:00c53d70:8"]]
+ 005ae80c ["INT_ADD", "register:40f0:8", ["const:5ae80c:8", "const:4:8"]]
+ 005ae80c ["CALL", null, ["callee:00c53d70:8"]]
- 005ae7cc bytes 41951a94
+ 005ae80c bytes 59951a94
- 005ae7f8 ["INT_ADD", "register:40f0:8", ["const:5ae7f8:8", "const:4:8"]]
- 005ae7f8 ["CALL", null, ["callee:0043bb60:8"]]
+ 005ae838 ["INT_ADD", "register:40f0:8", ["const:5ae838:8", "const:4:8"]]
+ 005ae838 ["CALL", null, ["callee:0043bb60:8"]]
- 005ae7f8 bytes ca34fa97
+ 005ae838 bytes ca34fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40c85042d34410dfa9c6971d1167700a"></a>

### [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) → [`005ae924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae924.md) FUN_005ae924

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) [`00450750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0045b610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b610.md)
- 新版 呼出元 0件  · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`004501c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004501c0.md) [`00450790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/00450790.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0045b650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b650.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.58% / 新版 96.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005aead8",
      "incomplete_value": true,
      "site": "005aead8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b1000:8"
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
    "old": {
      "definition_site": "005aea98",
      "incomplete_value": true,
      "site": "005aea98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:993:8"
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
      "definition_site": "005aeed8",
      "incomplete_value": true,
      "site": "005aeed8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:702:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005aee98",
      "incomplete_value": true,
      "site": "005aee98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:756:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005aeecc",
      "incomplete_value": true,
      "site": "005aeedc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005aee8c",
      "incomplete_value": true,
      "site": "005aee9c",
      "value": [
        "LOAD",
        "8",
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
      "005ae9f0",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ],
    [
      "005aeac0",
      "READ",
      [
        "storage",
        "002b1993",
        null,
        "string"
      ]
    ],
    [
      "005aee28",
      "PARAM",
      [
        "storage",
        "002a8ad9",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005ae9f0",
      "READ",
      [
        "storage",
        "002b393f",
        null,
        "string"
      ]
    ],
    [
      "005aeac0",
      "READ",
      [
        "storage",
        "002b1937",
        null,
        "string"
      ]
    ],
    [
      "005aee28",
      "PARAM",
      [
        "storage",
        "002a8a7d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aedf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md#insn-005aedf0) · [`005aee5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md#insn-005aee5c) · [`005aeeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md#insn-005aeeb4)
- 新版 `005aee30`（命令位置の公開資料なし） · `005aee9c`（命令位置の公開資料なし） · `005aeef4`（命令位置の公開資料なし）

~~~diff
- 005aedf0 ["INT_ADD", "register:40f0:8", ["const:5aedf0:8", "const:4:8"]]
- 005aedf0 ["CALL", null, ["callee:00c58040:8"]]
+ 005aee30 ["INT_ADD", "register:40f0:8", ["const:5aee30:8", "const:4:8"]]
+ 005aee30 ["CALL", null, ["callee:00c58040:8"]]
- 005aedf0 bytes 60a41a94
+ 005aee30 bytes 84a41a94
- 005aee5c ["INT_ADD", "register:40f0:8", ["const:5aee5c:8", "const:4:8"]]
- 005aee5c ["CALL", null, ["callee:00c53da0:8"]]
+ 005aee9c ["INT_ADD", "register:40f0:8", ["const:5aee9c:8", "const:4:8"]]
+ 005aee9c ["CALL", null, ["callee:00c53da0:8"]]
- 005aee5c bytes a9931a94
+ 005aee9c bytes c1931a94
- 005aeeb4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005aeeb4 ["INT_ADD", "register:40f0:8", ["const:5aeeb4:8", "const:4:8"]]
- 005aeeb4 ["CALLIND", null, ["register:0:8"]]
+ 005aeef4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005aeef4 ["INT_ADD", "register:40f0:8", ["const:5aeef4:8", "const:4:8"]]
+ 005aeef4 ["CALLIND", null, ["register:0:8"]]
- 005aeeb4 bytes 20013fd6
+ 005aeef4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b32c50f14d2256d971d1e4649e9691eb"></a>

### [`005af8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af8e8.md) → [`005af928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005af928.md) _INIT_58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005af9e4",
      "incomplete_value": true,
      "site": "005afa00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:576:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005af9a4",
      "incomplete_value": true,
      "site": "005af9c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5d2:8"
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
      "definition_site": "005afa04",
      "incomplete_value": true,
      "site": "005afa20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005af9c4",
      "incomplete_value": true,
      "site": "005af9e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005af964",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005af988",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005af9a8",
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
      "005af964",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005af988",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005af9a8",
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

- 旧版 [`005af980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af8e8.md#insn-005af980) · [`005af914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af8e8.md#insn-005af914) · [`005af920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005af8e8.md#insn-005af920)
- 新版 `005af9c0`（命令位置の公開資料なし） · `005af954`（命令位置の公開資料なし） · `005af960`（命令位置の公開資料なし）

~~~diff
- 005af980 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005af980 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005af980 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005af980 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005af9c0 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005af9c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005af9c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005af9c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005af980 bytes 4a893d91
+ 005af9c0 bytes 4a553c91
- 005af914 ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 005af914 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005af914 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005af914 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005af954 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 005af954 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005af954 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005af954 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005af914 bytes 73e21f91
+ 005af954 bytes 73e22391
- 005af920 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 005af920 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005af920 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005af920 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005af960 ["COPY", "tmp:0:8", ["const:f66:8"]]
+ 005af960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005af960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005af960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005af920 bytes 29993c91
+ 005af960 bytes 29993d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23918a4f6dacdb3461dbed044e731fd7"></a>

### [`005b0140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0140.md) → [`005b0180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0180.md) FUN_005b0180

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 8件 [`0046dad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dad4.md) [`005afc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005af/005afc78.md) [`005e4f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4f3c.md) [`008001cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001cc.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) · 呼出先 8件 [`0046db14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db14.md) [`005afcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005af/005afcb8.md) [`005e4f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4f7c.md) [`00800224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800224.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.62% / 新版 99.62%

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
      "site": "005b03a8",
      "value": [
        "leaf",
        "ram:a65e5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b0368",
      "value": [
        "leaf",
        "ram:a65dec:8"
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
      "005b0220",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ],
    [
      "005b035c",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ],
    [
      "005b03a0",
      "DATA",
      [
        "storage",
        "0039badc",
        null,
        "uleb128"
      ]
    ]
  ],
  "added": [
    [
      "005b0220",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[59]"
      ]
    ],
    [
      "005b035c",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[59]"
      ]
    ],
    [
      "005b03a0",
      "DATA",
      [
        "storage",
        "0039badc",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0140.md#insn-005b0328) · [`005b0368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0140.md#insn-005b0368) · [`005b0150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0140.md#insn-005b0150)
- 新版 `005b0368`（命令位置の公開資料なし） · `005b03a8`（命令位置の公開資料なし） · `005b0190`（命令位置の公開資料なし）

~~~diff
- 005b0328 ["INT_ADD", "register:40f0:8", ["const:5b0328:8", "const:4:8"]]
- 005b0328 ["CALL", null, ["callee:00851550:8"]]
+ 005b0368 ["INT_ADD", "register:40f0:8", ["const:5b0368:8", "const:4:8"]]
+ 005b0368 ["CALL", null, ["callee:00851550:8"]]
- 005b0328 bytes 74840a94
+ 005b0368 bytes 7a840a94
- 005b0368 ["INT_ADD", "register:40f0:8", ["const:5b0368:8", "const:4:8"]]
- 005b0368 ["CALL", null, ["ram:a65dec:8"]]
+ 005b03a8 ["INT_ADD", "register:40f0:8", ["const:5b03a8:8", "const:4:8"]]
+ 005b03a8 ["CALL", null, ["ram:a65e5c:8"]]
- 005b0368 bytes a1d61294
+ 005b03a8 bytes add61294
- 005b0150 ["INT_ADD", "register:40f0:8", ["const:5b0150:8", "const:4:8"]]
- 005b0150 ["CALL", null, ["callee:00851550:8"]]
+ 005b0190 ["INT_ADD", "register:40f0:8", ["const:5b0190:8", "const:4:8"]]
+ 005b0190 ["CALL", null, ["callee:00851550:8"]]
- 005b0150 bytes ea840a94
+ 005b0190 bytes f0840a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a62be175cdb20d430a0286110b74d76"></a>

### [`005b084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b084c.md) → [`005b088c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b088c.md) _INIT_59

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b08c8",
      "incomplete_value": true,
      "site": "005b08e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b0888",
      "incomplete_value": true,
      "site": "005b08a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b092c",
      "incomplete_value": true,
      "site": "005b0944",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b08ec",
      "incomplete_value": true,
      "site": "005b0904",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005b08c8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005b08ec",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005b090c",
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
      "005b08c8",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005b08ec",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005b090c",
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

- 旧版 [`005b08c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b084c.md#insn-005b08c4) · [`005b08e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b084c.md#insn-005b08e4) · [`005b0878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b084c.md#insn-005b0878)
- 新版 `005b0904`（命令位置の公開資料なし） · `005b0924`（命令位置の公開資料なし） · `005b08b8`（命令位置の公開資料なし）

~~~diff
- 005b08c4 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 005b08c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b08c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b08c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b0904 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 005b0904 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b0904 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b0904 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b08c4 bytes 4a093791
+ 005b0904 bytes 4ab93591
- 005b08e4 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005b08e4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b08e4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b08e4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b0924 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005b0924 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b0924 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b0924 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b08e4 bytes 4a893d91
+ 005b0924 bytes 4a553c91
- 005b0878 ["COPY", "tmp:0:8", ["const:810:8"]]
- 005b0878 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 005b0878 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 005b0878 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 005b08b8 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 005b08b8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 005b08b8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 005b08b8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 005b0878 bytes 73422091
+ 005b08b8 bytes 73422491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d8532529054e0c86c0fa1359393b378"></a>

### [`005b0c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0c48.md) → [`005b0c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0c88.md) FUN_005b0c88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005b0bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0bdc.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`005b0c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0c1c.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58020.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005b0cbc",
      "incomplete_value": false,
      "site": "005b0cc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:e45:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0c7c",
      "incomplete_value": false,
      "site": "005b0c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:e14:8"
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
      "definition_site": "005b0ce8",
      "incomplete_value": false,
      "site": "005b0cf0",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0ca8",
      "incomplete_value": false,
      "site": "005b0cb0",
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
            "const:25c:8"
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
      "definition_site": "005b0d58",
      "incomplete_value": false,
      "site": "005b0d60",
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
            "const:1a6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b0d18",
      "incomplete_value": false,
      "site": "005b0d20",
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
            "const:1f3:8"
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
      "005b0cbc",
      "PARAM",
      [
        "storage",
        "002b1e14",
        null,
        "string"
      ]
    ],
    [
      "005b0ce8",
      "PARAM",
      [
        "storage",
        "002a025c",
        null,
        "string"
      ]
    ],
    [
      "005b0d58",
      "PARAM",
      [
        "storage",
        "0029f1f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005b0cbc",
      "PARAM",
      [
        "storage",
        "002b1e45",
        null,
        "string"
      ]
    ],
    [
      "005b0ce8",
      "PARAM",
      [
        "storage",
        "002a020f",
        null,
        "string"
      ]
    ],
    [
      "005b0d58",
      "PARAM",
      [
        "storage",
        "0029f1a6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b0c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0c48.md#insn-005b0c88) · [`005b0cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0c48.md#insn-005b0cb0) · [`005b0d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0c48.md#insn-005b0d20)
- 新版 `005b0cc8`（命令位置の公開資料なし） · `005b0cf0`（命令位置の公開資料なし） · `005b0d60`（命令位置の公開資料なし）

~~~diff
- 005b0c88 ["INT_ADD", "register:40f0:8", ["const:5b0c88:8", "const:4:8"]]
- 005b0c88 ["CALL", null, ["callee:00c58030:8"]]
+ 005b0cc8 ["INT_ADD", "register:40f0:8", ["const:5b0cc8:8", "const:4:8"]]
+ 005b0cc8 ["CALL", null, ["callee:00c58030:8"]]
- 005b0c88 bytes b69c1a94
+ 005b0cc8 bytes da9c1a94
- 005b0cb0 ["INT_ADD", "register:40f0:8", ["const:5b0cb0:8", "const:4:8"]]
- 005b0cb0 ["CALL", null, ["callee:00c58040:8"]]
+ 005b0cf0 ["INT_ADD", "register:40f0:8", ["const:5b0cf0:8", "const:4:8"]]
+ 005b0cf0 ["CALL", null, ["callee:00c58040:8"]]
- 005b0cb0 bytes b09c1a94
+ 005b0cf0 bytes d49c1a94
- 005b0d20 ["INT_ADD", "register:40f0:8", ["const:5b0d20:8", "const:4:8"]]
- 005b0d20 ["CALL", null, ["callee:00c58040:8"]]
+ 005b0d60 ["INT_ADD", "register:40f0:8", ["const:5b0d60:8", "const:4:8"]]
+ 005b0d60 ["CALL", null, ["callee:00c58040:8"]]
- 005b0d20 bytes 949c1a94
+ 005b0d60 bytes b89c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97156ed4211fc5cb04996d550e518883"></a>

### [`005b0fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0fa8.md) → [`005b0fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0fe8.md) _INIT_60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.44% / 新版 86.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b1024",
      "incomplete_value": true,
      "site": "005b1040",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b0fe4",
      "incomplete_value": true,
      "site": "005b1000",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b1068",
      "incomplete_value": true,
      "site": "005b1084",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b1028",
      "incomplete_value": true,
      "site": "005b1044",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b1088",
      "incomplete_value": true,
      "site": "005b10a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "005b1048",
      "incomplete_value": true,
      "site": "005b1060",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "005b1024",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "005b1048",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "005b1068",
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
      "005b1024",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "005b1048",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "005b1068",
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

- 旧版 [`005b1020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0fa8.md#insn-005b1020) · [`005b1040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0fa8.md#insn-005b1040) · [`005b11dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0fa8.md#insn-005b11dc)
- 新版 `005b1060`（命令位置の公開資料なし） · `005b1080`（命令位置の公開資料なし） · `005b121c`（命令位置の公開資料なし）

~~~diff
- 005b1020 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 005b1020 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b1020 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b1020 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b1060 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 005b1060 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b1060 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b1060 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b1020 bytes 4a093791
+ 005b1060 bytes 4ab93591
- 005b1040 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 005b1040 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b1040 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b1040 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b1080 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 005b1080 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b1080 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b1080 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b1040 bytes 4a893d91
+ 005b1080 bytes 4a553c91
- 005b11dc ["INT_ADD", "register:40f0:8", ["const:5b11dc:8", "const:4:8"]]
- 005b11dc ["CALL", null, ["callee:00c57f00:8"]]
+ 005b121c ["INT_ADD", "register:40f0:8", ["const:5b121c:8", "const:4:8"]]
+ 005b121c ["CALL", null, ["callee:00c57f00:8"]]
- 005b11dc bytes 159b1a94
+ 005b121c bytes 399b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f4836812e6617a69f6e6758db13e3c6"></a>

### [`005b1514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md) → [`005b1554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1554.md) FUN_005b1554

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`005b14e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b14e4.md) [`005b2b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md) · 呼出先 8件 [`005b534c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b534c.md) [`005b5350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5350.md) [`005b53d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b53d0.md) [`005b53d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b53d4.md) [`00b368d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b368d4.md)
- 新版 呼出元 2件 [`005b1524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1524.md) [`005b2b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2b48.md) · 呼出先 8件 [`005b538c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b538c.md) [`005b5390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5390.md) [`005b5410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5410.md) [`005b5414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5414.md) [`00b36970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b36/00b36970.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b1584",
      "incomplete_value": false,
      "site": "005b1584",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1544",
      "incomplete_value": false,
      "site": "005b1544",
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
            "const:6b0:8"
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
      "definition_site": "005b15c8",
      "incomplete_value": false,
      "site": "005b15c8",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1588",
      "incomplete_value": false,
      "site": "005b1588",
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
            "const:740:8"
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
      "005b1584",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b15b8",
      "READ",
      [
        "storage",
        "00c6f6d0",
        null,
        "pointer"
      ]
    ],
    [
      "005b15b8",
      "READ",
      [
        "storage",
        "00c6f6d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b1584",
      "DATA",
      [
        "storage",
        "00c6f780",
        null,
        "undefined *"
      ]
    ],
    [
      "005b15b8",
      "READ",
      [
        "storage",
        "00c6f7a0",
        null,
        "pointer"
      ]
    ],
    [
      "005b15b8",
      "READ",
      [
        "storage",
        "00c6f7a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b1584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md#insn-005b1584) · [`005b15c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md#insn-005b15c8) · [`005b1540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md#insn-005b1540)
- 新版 `005b15c4`（命令位置の公開資料なし） · `005b1608`（命令位置の公開資料なし） · `005b1580`（命令位置の公開資料なし）

~~~diff
- 005b1584 ["COPY", "tmp:0:8", ["const:740:8"]]
- 005b1584 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b1584 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b1584 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b15c4 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 005b15c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b15c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b15c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b1584 bytes 08011d91
+ 005b15c4 bytes 08412091
- 005b15c8 ["INT_ADD", "register:40f0:8", ["const:5b15c8:8", "const:4:8"]]
- 005b15c8 ["CALL", null, ["callee:00b36970:8"]]
+ 005b1608 ["INT_ADD", "register:40f0:8", ["const:5b1608:8", "const:4:8"]]
+ 005b1608 ["CALL", null, ["callee:00b36970:8"]]
- 005b15c8 bytes c3141694
+ 005b1608 bytes da141694
- 005b1540 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 005b1540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b1540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b1540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b1580 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 005b1580 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1580 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1580 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b1540 bytes 08c11a91
+ 005b1580 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0527754f7af59525abe92513a2dbd9b3"></a>

### [`005b1650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md) → [`005b1690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1690.md) FUN_005b1690

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005b14e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b14e4.md) [`005b2b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md) · 呼出先 11件 [`005b56d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b56d4.md) [`005b56d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b56d8.md) [`005b5758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5758.md) [`005b575c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b575c.md) [`00879d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d80.md)
- 新版 呼出元 2件 [`005b1524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1524.md) [`005b2b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2b48.md) · 呼出先 11件 [`005b5714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5714.md) [`005b5718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5718.md) [`005b5798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5798.md) [`005b579c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b579c.md) [`00879dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879dd8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b16e8",
      "incomplete_value": false,
      "site": "005b16e8",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b16a8",
      "incomplete_value": false,
      "site": "005b16a8",
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
            "const:8e0:8"
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
      "definition_site": "005b172c",
      "incomplete_value": true,
      "site": "005b172c",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b16ec",
      "incomplete_value": true,
      "site": "005b16ec",
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
      "005b16b0",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "005b16e8",
      "DATA",
      [
        "storage",
        "00c6f8e0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b171c",
      "READ",
      [
        "storage",
        "00c6f900",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b16b0",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "005b16e8",
      "DATA",
      [
        "storage",
        "00c6f9b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b171c",
      "READ",
      [
        "storage",
        "00c6f9d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b16e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md#insn-005b16e8) · [`005b1670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md#insn-005b1670) · [`005b1680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md#insn-005b1680)
- 新版 `005b1728`（命令位置の公開資料なし） · `005b16b0`（命令位置の公開資料なし） · `005b16c0`（命令位置の公開資料なし）

~~~diff
- 005b16e8 ["COPY", "tmp:0:8", ["const:960:8"]]
- 005b16e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b16e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b16e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b1728 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 005b1728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b16e8 bytes 08812591
+ 005b1728 bytes 08c12891
- 005b1670 ["COPY", "tmp:0:8", ["const:3ea:8"]]
- 005b1670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005b1670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005b1670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005b16b0 ["COPY", "tmp:0:8", ["const:38e:8"]]
+ 005b16b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005b16b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005b16b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005b1670 bytes 21a80f91
+ 005b16b0 bytes 21380e91
- 005b1680 ["INT_ADD", "register:40f0:8", ["const:5b1680:8", "const:4:8"]]
- 005b1680 ["CALL", null, ["callee:00c58260:8"]]
+ 005b16c0 ["INT_ADD", "register:40f0:8", ["const:5b16c0:8", "const:4:8"]]
+ 005b16c0 ["CALL", null, ["callee:00c58260:8"]]
- 005b1680 bytes c49a1a94
+ 005b16c0 bytes e89a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db2feaaf0a52e9a15de7cb13d99d7d9d"></a>

### [`005b17b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md) → [`005b17f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b17f8.md) FUN_005b17f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b5354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5354.md) · 呼出先 6件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00493690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493690.md) [`005b18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005b5394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5394.md) · 呼出先 6件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`004936d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004936d0.md) [`005b1910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1910.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b1850",
      "incomplete_value": true,
      "site": "005b1850",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:33a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1810",
      "incomplete_value": true,
      "site": "005b1810",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2fa:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b1828",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b17e8",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "005b1828",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "005b183c",
      "READ",
      [
        "storage",
        "002c12fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005b1828",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "005b183c",
      "READ",
      [
        "storage",
        "002c133a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b17e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md#insn-005b17e8) · [`005b1828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md#insn-005b1828) · [`005b17f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md#insn-005b17f4)
- 新版 `005b1828`（命令位置の公開資料なし） · `005b1868`（命令位置の公開資料なし） · `005b1834`（命令位置の公開資料なし）

~~~diff
- 005b17e8 ["INT_ADD", "register:40f0:8", ["const:5b17e8:8", "const:4:8"]]
- 005b17e8 ["CALL", null, ["ram:48ccf8:8"]]
+ 005b1828 ["INT_ADD", "register:40f0:8", ["const:5b1828:8", "const:4:8"]]
+ 005b1828 ["CALL", null, ["ram:48cd38:8"]]
- 005b17e8 bytes 446dfb97
+ 005b1828 bytes 446dfb97
- 005b1828 ["INT_ADD", "register:40f0:8", ["const:5b1828:8", "const:4:8"]]
- 005b1828 ["CALL", null, ["callee:004936d0:8"]]
+ 005b1868 ["INT_ADD", "register:40f0:8", ["const:5b1868:8", "const:4:8"]]
+ 005b1868 ["CALL", null, ["callee:004936d0:8"]]
- 005b1828 bytes 9a87fb97
+ 005b1868 bytes 9a87fb97
- 005b17f4 ["COPY", "tmp:0:8", ["const:2fa:8"]]
- 005b17f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b17f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b17f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b1834 ["COPY", "tmp:0:8", ["const:33a:8"]]
+ 005b1834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b1834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b1834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b17f4 bytes 29e90b91
+ 005b1834 bytes 29e90c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7caae2359ae6d8a6f484cad05e22ea7f"></a>

### [`005b18d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md) → [`005b1910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1910.md) FUN_005b1910

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b17b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b17b8.md) · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005b5564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5564.md) [`005b561c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b561c.md) [`005b5620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5620.md) [`00879d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879d88.md)
- 新版 呼出元 1件 [`005b17f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b17f8.md) · 呼出先 8件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005b55a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b55a4.md) [`005b565c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b565c.md) [`005b5660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5660.md) [`00879de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879de0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.52% / 新版 96.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b19d4",
      "incomplete_value": false,
      "site": "005b19d4",
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
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1994",
      "incomplete_value": false,
      "site": "005b1994",
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
            "const:7d0:8"
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
      "definition_site": "005b1a08",
      "incomplete_value": false,
      "site": "005b1a08",
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
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b19c8",
      "incomplete_value": false,
      "site": "005b19c8",
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
            "const:860:8"
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
      "005b19d4",
      "DATA",
      [
        "storage",
        "00c6f7d0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1a08",
      "DATA",
      [
        "storage",
        "00c6f860",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1a54",
      "READ",
      [
        "storage",
        "00c6f880",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b19d4",
      "DATA",
      [
        "storage",
        "00c6f8a0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1a08",
      "DATA",
      [
        "storage",
        "00c6f930",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1a54",
      "READ",
      [
        "storage",
        "00c6f950",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b1934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md#insn-005b1934) · [`005b1970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md#insn-005b1970) · [`005b197c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b18d0.md#insn-005b197c)
- 新版 `005b1974`（命令位置の公開資料なし） · `005b19b0`（命令位置の公開資料なし） · `005b19bc`（命令位置の公開資料なし）

~~~diff
- 005b1934 ["INT_ADD", "register:40f0:8", ["const:5b1934:8", "const:4:8"]]
- 005b1934 ["CALL", null, ["callee:0043bb60:8"]]
+ 005b1974 ["INT_ADD", "register:40f0:8", ["const:5b1974:8", "const:4:8"]]
+ 005b1974 ["CALL", null, ["callee:0043bb60:8"]]
- 005b1934 bytes 7b28fa97
+ 005b1974 bytes 7b28fa97
- 005b1970 ["INT_ADD", "register:40f0:8", ["const:5b1970:8", "const:4:8"]]
- 005b1970 ["CALL", null, ["callee:0043bb60:8"]]
+ 005b19b0 ["INT_ADD", "register:40f0:8", ["const:5b19b0:8", "const:4:8"]]
+ 005b19b0 ["CALL", null, ["callee:0043bb60:8"]]
- 005b1970 bytes 6c28fa97
+ 005b19b0 bytes 6c28fa97
- 005b197c ["INT_ADD", "register:40f0:8", ["const:5b197c:8", "const:4:8"]]
- 005b197c ["CALL", null, ["callee:00c57f60:8"]]
+ 005b19bc ["INT_ADD", "register:40f0:8", ["const:5b19bc:8", "const:4:8"]]
+ 005b19bc ["CALL", null, ["callee:00c57f60:8"]]
- 005b197c bytes 45991a94
+ 005b19bc bytes 69991a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7aeeb0a70ee09b9d2045ac4df6aae18"></a>

### [`005b1b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md) → [`005b1bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1bc4.md) FUN_005b1bc4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b56dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b56dc.md) · 呼出先 7件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00493690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493690.md) [`005b1cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1cd0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005b571c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b571c.md) · 呼出先 7件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`004936d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004936d0.md) [`005b1d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1d10.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.44% / 新版 93.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b1c1c",
      "incomplete_value": true,
      "site": "005b1c1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:33a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1bdc",
      "incomplete_value": true,
      "site": "005b1bdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2fa:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b1bf4",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b1bb4",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "005b1bf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "005b1c08",
      "READ",
      [
        "storage",
        "002c12fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005b1bf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "005b1c08",
      "READ",
      [
        "storage",
        "002c133a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b1bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md#insn-005b1bb4) · [`005b1bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md#insn-005b1bf4) · [`005b1bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md#insn-005b1bc0)
- 新版 `005b1bf4`（命令位置の公開資料なし） · `005b1c34`（命令位置の公開資料なし） · `005b1c00`（命令位置の公開資料なし）

~~~diff
- 005b1bb4 ["INT_ADD", "register:40f0:8", ["const:5b1bb4:8", "const:4:8"]]
- 005b1bb4 ["CALL", null, ["ram:48ccf8:8"]]
+ 005b1bf4 ["INT_ADD", "register:40f0:8", ["const:5b1bf4:8", "const:4:8"]]
+ 005b1bf4 ["CALL", null, ["ram:48cd38:8"]]
- 005b1bb4 bytes 516cfb97
+ 005b1bf4 bytes 516cfb97
- 005b1bf4 ["INT_ADD", "register:40f0:8", ["const:5b1bf4:8", "const:4:8"]]
- 005b1bf4 ["CALL", null, ["callee:004936d0:8"]]
+ 005b1c34 ["INT_ADD", "register:40f0:8", ["const:5b1c34:8", "const:4:8"]]
+ 005b1c34 ["CALL", null, ["callee:004936d0:8"]]
- 005b1bf4 bytes a786fb97
+ 005b1c34 bytes a786fb97
- 005b1bc0 ["COPY", "tmp:0:8", ["const:2fa:8"]]
- 005b1bc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b1bc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b1bc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b1c00 ["COPY", "tmp:0:8", ["const:33a:8"]]
+ 005b1c00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b1c00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b1c00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b1bc0 bytes 29e90b91
+ 005b1c00 bytes 29e90c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88f3bb4e73ee9a79d039133db75a4558"></a>

### [`005b1cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1cd0.md) → [`005b1d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1d10.md) FUN_005b1d10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`005b1b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1b84.md) [`005b5598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5598.md) · 呼出先 6件 [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) [`005b580c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b580c.md) [`005b5810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5810.md) [`005b5ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ad8.md) [`005b5adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5adc.md)
- 新版 呼出元 2件 [`005b1bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1bc4.md) [`005b55d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b55d8.md) · 呼出先 6件 [`005b1e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1e64.md) [`005b584c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b584c.md) [`005b5850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5850.md) [`005b5b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b18.md) [`005b5b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b1c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b1d3c",
      "incomplete_value": false,
      "site": "005b1d3c",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1cfc",
      "incomplete_value": false,
      "site": "005b1cfc",
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
            "const:9e0:8"
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
      "definition_site": "005b1d54",
      "incomplete_value": false,
      "site": "005b1d54",
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
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b1d14",
      "incomplete_value": false,
      "site": "005b1d14",
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
            "const:ab0:8"
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
      "005b1d3c",
      "DATA",
      [
        "storage",
        "00c6f9e0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1d54",
      "DATA",
      [
        "storage",
        "00c6fab0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1d8c",
      "READ",
      [
        "storage",
        "00c6fad0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b1d3c",
      "DATA",
      [
        "storage",
        "00c6fab0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1d54",
      "DATA",
      [
        "storage",
        "00c6fb80",
        null,
        "undefined *"
      ]
    ],
    [
      "005b1d8c",
      "READ",
      [
        "storage",
        "00c6fba0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b1cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1cd0.md#insn-005b1cf8) · [`005b1d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1cd0.md#insn-005b1d10) · [`005b1d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1cd0.md#insn-005b1d24)
- 新版 `005b1d38`（命令位置の公開資料なし） · `005b1d50`（命令位置の公開資料なし） · `005b1d64`（命令位置の公開資料なし）

~~~diff
- 005b1cf8 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 005b1cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b1cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b1cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b1d38 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 005b1d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b1cf8 bytes 08812791
+ 005b1d38 bytes 08c12a91
- 005b1d10 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 005b1d10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b1d10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b1d10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b1d50 ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 005b1d50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1d50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b1d50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b1d10 bytes 08c12a91
+ 005b1d50 bytes 08012e91
- 005b1d24 ["INT_ADD", "register:40f0:8", ["const:5b1d24:8", "const:4:8"]]
- 005b1d24 ["CALL", null, ["callee:005b1e64:8"]]
+ 005b1d64 ["INT_ADD", "register:40f0:8", ["const:5b1d64:8", "const:4:8"]]
+ 005b1d64 ["CALL", null, ["callee:005b1e64:8"]]
- 005b1d24 bytes 40000094
+ 005b1d64 bytes 40000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cbc98ff7e116f1b231a9661ff5641ac"></a>

### [`005b212c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b212c.md) → [`005b216c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b216c.md) FUN_005b216c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`005b22f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22f0.md) [`005b53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b53d8.md) [`005b5624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5624.md) [`005b5760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5760.md) [`005b5c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c4c.md) · 呼出先 7件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005b0bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0bdc.md) [`005b5214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5214.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 7件 [`005b2330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2330.md) [`005b5418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5418.md) [`005b5664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5664.md) [`005b57a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b57a0.md) [`005b5c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c8c.md) · 呼出先 7件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`005b0c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0c1c.md) [`005b5254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5254.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b21ec",
      "incomplete_value": false,
      "site": "005b2200",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b21ac",
      "incomplete_value": false,
      "site": "005b21c0",
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
            "const:660:8"
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
      "005b2200",
      "DATA",
      [
        "storage",
        "00c6f660",
        null,
        "pointer"
      ]
    ],
    [
      "005b2250",
      "READ",
      [
        "storage",
        "00c6f670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b2200",
      "DATA",
      [
        "storage",
        "00c6f730",
        null,
        "pointer"
      ]
    ],
    [
      "005b2250",
      "READ",
      [
        "storage",
        "00c6f740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b2200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b212c.md#insn-005b2200) · [`005b21a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b212c.md#insn-005b21a0) · [`005b21ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b212c.md#insn-005b21ac)
- 新版 `005b2240`（命令位置の公開資料なし） · `005b21e0`（命令位置の公開資料なし） · `005b21ec`（命令位置の公開資料なし）

~~~diff
- 005b2200 ["INT_ADD", "register:40f0:8", ["const:5b2200:8", "const:4:8"]]
- 005b2200 ["CALL", null, ["callee:00c53da0:8"]]
+ 005b2240 ["INT_ADD", "register:40f0:8", ["const:5b2240:8", "const:4:8"]]
+ 005b2240 ["CALL", null, ["callee:00c53da0:8"]]
- 005b2200 bytes c0861a94
+ 005b2240 bytes d8861a94
- 005b21a0 ["INT_ADD", "register:40f0:8", ["const:5b21a0:8", "const:4:8"]]
- 005b21a0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b21e0 ["INT_ADD", "register:40f0:8", ["const:5b21e0:8", "const:4:8"]]
+ 005b21e0 ["CALL", null, ["callee:00c57f60:8"]]
- 005b21a0 bytes 3c971a94
+ 005b21e0 bytes 60971a94
- 005b21ac ["COPY", "tmp:0:8", ["const:660:8"]]
- 005b21ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b21ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b21ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b21ec ["COPY", "tmp:0:8", ["const:730:8"]]
+ 005b21ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b21ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b21ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b21ac bytes 08811991
+ 005b21ec bytes 08c11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4c69b9f5568f1afd236d14536b3bac7"></a>

### [`005b22f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22f0.md) → [`005b2330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2330.md) FUN_005b2330

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`005b5ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ae0.md) [`005b5e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e08.md) [`005b63d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b63d0.md) [`005b6760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6760.md) [`005b6880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6880.md) · 呼出先 6件 [`005b212c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b212c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)
- 新版 呼出元 6件 [`005b5b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b20.md) [`005b5e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5e48.md) [`005b6410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6410.md) [`005b67a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b67a0.md) [`005b68c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b68c0.md) · 呼出先 6件 [`005b216c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b216c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58020.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.70% / 新版 95.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005b2380",
      "incomplete_value": false,
      "site": "005b2388",
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
            "const:6d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b2340",
      "incomplete_value": false,
      "site": "005b2348",
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
            "const:72e:8"
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
      "definition_site": "005b2398",
      "incomplete_value": false,
      "site": "005b23a0",
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
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b2358",
      "incomplete_value": false,
      "site": "005b2360",
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
            "const:26d:8"
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
      "definition_site": "005b23cc",
      "incomplete_value": false,
      "site": "005b23d8",
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
            "const:dcb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b238c",
      "incomplete_value": false,
      "site": "005b2398",
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
            "const:d9c:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005b2380",
      "PARAM",
      [
        "storage",
        "002a572e",
        null,
        null
      ]
    ],
    [
      "005b2398",
      "PARAM",
      [
        "storage",
        "002a026d",
        null,
        null
      ]
    ],
    [
      "005b23cc",
      "PARAM",
      [
        "storage",
        "002a8d9c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005b2380",
      "PARAM",
      [
        "storage",
        "002a56d2",
        null,
        null
      ]
    ],
    [
      "005b2398",
      "PARAM",
      [
        "storage",
        "002a0220",
        null,
        null
      ]
    ],
    [
      "005b23cc",
      "PARAM",
      [
        "storage",
        "002a8dcb",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b2348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22f0.md#insn-005b2348) · [`005b2358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22f0.md#insn-005b2358) · [`005b2360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22f0.md#insn-005b2360)
- 新版 `005b2388`（命令位置の公開資料なし） · `005b2398`（命令位置の公開資料なし） · `005b23a0`（命令位置の公開資料なし）

~~~diff
- 005b2348 ["INT_ADD", "register:40f0:8", ["const:5b2348:8", "const:4:8"]]
- 005b2348 ["CALL", null, ["callee:00c58260:8"]]
+ 005b2388 ["INT_ADD", "register:40f0:8", ["const:5b2388:8", "const:4:8"]]
+ 005b2388 ["CALL", null, ["callee:00c58260:8"]]
- 005b2348 bytes 92971a94
+ 005b2388 bytes b6971a94
- 005b2358 ["COPY", "tmp:0:8", ["const:26d:8"]]
- 005b2358 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005b2358 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005b2358 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005b2398 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 005b2398 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005b2398 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005b2398 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005b2358 bytes 21b40991
+ 005b2398 bytes 21800891
- 005b2360 ["INT_ADD", "register:40f0:8", ["const:5b2360:8", "const:4:8"]]
- 005b2360 ["CALL", null, ["callee:00c58260:8"]]
+ 005b23a0 ["INT_ADD", "register:40f0:8", ["const:5b23a0:8", "const:4:8"]]
+ 005b23a0 ["CALL", null, ["callee:00c58260:8"]]
- 005b2360 bytes 8c971a94
+ 005b23a0 bytes b0971a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17d9c155eaa5f9937651f0b2347cae31"></a>

### [`005b24b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b24b4.md) → [`005b24f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b24f4.md) FUN_005b24f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005b24ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b24ac.md) [`005b3ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3ecc.md) · 呼出先 6件 [`005b5ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ba4.md) [`005b5ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ba8.md) [`005b5c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c44.md) [`005b5c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c48.md) [`0087a5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087a5e4.md)
- 新版 呼出元 2件 [`005b24ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b24ec.md) [`005b3f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3f0c.md) · 呼出先 6件 [`005b5be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5be4.md) [`005b5be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5be8.md) [`005b5c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c84.md) [`005b5c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c88.md) [`0087a63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087a63c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b2520",
      "incomplete_value": false,
      "site": "005b2520",
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
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b24e0",
      "incomplete_value": false,
      "site": "005b24e0",
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
            "const:b40:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b2550",
      "value": [
        "leaf",
        "ram:87a63c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b2510",
      "value": [
        "leaf",
        "ram:87a5e4:8"
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
      "005b2520",
      "DATA",
      [
        "storage",
        "00c6fb40",
        null,
        "undefined *"
      ]
    ],
    [
      "005b2534",
      "DATA",
      [
        "storage",
        "00c6fbc0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b2550",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0087a5e4"
      ]
    ]
  ],
  "added": [
    [
      "005b2520",
      "DATA",
      [
        "storage",
        "00c6fc10",
        null,
        "undefined *"
      ]
    ],
    [
      "005b2534",
      "DATA",
      [
        "storage",
        "00c6fc90",
        null,
        "undefined *"
      ]
    ],
    [
      "005b2550",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0087a63c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b2510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b24b4.md#insn-005b2510) · [`005b24cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b24b4.md#insn-005b24cc) · [`005b24f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b24b4.md#insn-005b24f0)
- 新版 `005b2550`（命令位置の公開資料なし） · `005b250c`（命令位置の公開資料なし） · `005b2530`（命令位置の公開資料なし）

~~~diff
- 005b2510 ["INT_ADD", "register:40f0:8", ["const:5b2510:8", "const:4:8"]]
- 005b2510 ["CALL", null, ["ram:87a5e4:8"]]
+ 005b2550 ["INT_ADD", "register:40f0:8", ["const:5b2550:8", "const:4:8"]]
+ 005b2550 ["CALL", null, ["ram:87a63c:8"]]
- 005b2510 bytes 35200b94
+ 005b2550 bytes 3b200b94
- 005b24cc ["COPY", "tmp:0:8", ["const:b40:8"]]
- 005b24cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b24cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b24cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b250c ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 005b250c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b250c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b250c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b24cc bytes 29012d91
+ 005b250c bytes 29413091
- 005b24f0 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 005b24f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b24f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b24f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b2530 ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 005b2530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b24f0 bytes 08012f91
+ 005b2530 bytes 08413291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29a5b3f203ffe5c217fceffd39689126"></a>

### [`005b2610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2610.md) → [`005b2650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2650.md) FUN_005b2650

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b5bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5bac.md) · 呼出先 6件 [`005b275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md) [`005b5cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5cd8.md) [`005b5cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5cdc.md) [`005b5e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e00.md) [`005b5e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e04.md)
- 新版 呼出元 1件 [`005b5bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5bec.md) · 呼出先 6件 [`005b279c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b279c.md) [`005b5d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5d18.md) [`005b5d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5d1c.md) [`005b5e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5e40.md) [`005b5e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5e44.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b2678",
      "incomplete_value": false,
      "site": "005b2678",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b2638",
      "incomplete_value": false,
      "site": "005b2638",
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
            "const:c40:8"
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
      "definition_site": "005b268c",
      "incomplete_value": false,
      "site": "005b268c",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b264c",
      "incomplete_value": false,
      "site": "005b264c",
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
            "const:cc0:8"
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
      "005b2678",
      "DATA",
      [
        "storage",
        "00c6fc40",
        null,
        "undefined *"
      ]
    ],
    [
      "005b268c",
      "DATA",
      [
        "storage",
        "00c6fcc0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b26c4",
      "READ",
      [
        "storage",
        "00c6fce0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b2678",
      "DATA",
      [
        "storage",
        "00c6fd10",
        null,
        "undefined *"
      ]
    ],
    [
      "005b268c",
      "DATA",
      [
        "storage",
        "00c6fd90",
        null,
        "undefined *"
      ]
    ],
    [
      "005b26c4",
      "READ",
      [
        "storage",
        "00c6fdb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b2634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2610.md#insn-005b2634) · [`005b2648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2610.md#insn-005b2648) · [`005b265c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2610.md#insn-005b265c)
- 新版 `005b2674`（命令位置の公開資料なし） · `005b2688`（命令位置の公開資料なし） · `005b269c`（命令位置の公開資料なし）

~~~diff
- 005b2634 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 005b2634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b2634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b2634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b2674 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 005b2674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b2634 bytes 08013191
+ 005b2674 bytes 08413491
- 005b2648 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 005b2648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b2648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b2648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b2688 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 005b2688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b2648 bytes 08013391
+ 005b2688 bytes 08413691
- 005b265c ["INT_ADD", "register:40f0:8", ["const:5b265c:8", "const:4:8"]]
- 005b265c ["CALL", null, ["callee:005b279c:8"]]
+ 005b269c ["INT_ADD", "register:40f0:8", ["const:5b269c:8", "const:4:8"]]
+ 005b269c ["CALL", null, ["callee:005b279c:8"]]
- 005b265c bytes 40000094
+ 005b269c bytes 40000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-017aee16d52594115f85f8e46e61398d"></a>

### [`005b275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md) → [`005b279c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b279c.md) FUN_005b279c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b2610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2610.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059f500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059f/0059f500.md) [`005b80dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b80dc.md)
- 新版 呼出元 1件 [`005b2650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2650.md) · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`0059f540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059f/0059f540.md) [`005b811c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b811c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.71% / 新版 97.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b28e8",
      "incomplete_value": false,
      "site": "005b28e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b28a8",
      "incomplete_value": false,
      "site": "005b28a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "005b285c",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "005b28e8",
      "DATA",
      [
        "storage",
        "00c707a0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b295c",
      "READ",
      [
        "storage",
        "00c707c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b285c",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b28e8",
      "DATA",
      [
        "storage",
        "00c70870",
        null,
        "undefined *"
      ]
    ],
    [
      "005b295c",
      "READ",
      [
        "storage",
        "00c70898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b2790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md#insn-005b2790) · [`005b27bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md#insn-005b27bc) · [`005b27c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md#insn-005b27c8)
- 新版 `005b27d0`（命令位置の公開資料なし） · `005b27fc`（命令位置の公開資料なし） · `005b2808`（命令位置の公開資料なし）

~~~diff
- 005b2790 ["INT_ADD", "register:40f0:8", ["const:5b2790:8", "const:4:8"]]
- 005b2790 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b27d0 ["INT_ADD", "register:40f0:8", ["const:5b27d0:8", "const:4:8"]]
+ 005b27d0 ["CALL", null, ["callee:00c57f60:8"]]
- 005b2790 bytes c0951a94
+ 005b27d0 bytes e4951a94
- 005b27bc ["INT_ADD", "register:40f0:8", ["const:5b27bc:8", "const:4:8"]]
- 005b27bc ["CALL", null, ["callee:0043bb60:8"]]
+ 005b27fc ["INT_ADD", "register:40f0:8", ["const:5b27fc:8", "const:4:8"]]
+ 005b27fc ["CALL", null, ["callee:0043bb60:8"]]
- 005b27bc bytes d924fa97
+ 005b27fc bytes d924fa97
- 005b27c8 ["INT_ADD", "register:40f0:8", ["const:5b27c8:8", "const:4:8"]]
- 005b27c8 ["CALL", null, ["callee:0059f540:8"]]
+ 005b2808 ["INT_ADD", "register:40f0:8", ["const:5b2808:8", "const:4:8"]]
+ 005b2808 ["CALL", null, ["callee:0059f540:8"]]
- 005b27c8 bytes 4eb3ff97
+ 005b2808 bytes 4eb3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf06dbad7e797d3928416ad33cdaf824"></a>

### [`005b2b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md) → [`005b2b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2b48.md) FUN_005b2b48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) · 呼出先 9件 [`005b1514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md) [`005b1650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1650.md) [`005b2c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2c90.md) [`005b2ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2ee8.md) [`005b5ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ea0.md)
- 新版 呼出元 1件 [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) · 呼出先 9件 [`005b1554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1554.md) [`005b1690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1690.md) [`005b2cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2cd0.md) [`005b2f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2f28.md) [`005b5ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b2b84",
      "incomplete_value": false,
      "site": "005b2b84",
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
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b2b44",
      "incomplete_value": false,
      "site": "005b2b44",
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
            "const:d40:8"
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
      "definition_site": "005b2bd4",
      "incomplete_value": true,
      "site": "005b2bd4",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b2b94",
      "incomplete_value": true,
      "site": "005b2b94",
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
            "const:dd0:8"
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
      "005b2b84",
      "DATA",
      [
        "storage",
        "00c6fd40",
        null,
        "undefined *"
      ]
    ],
    [
      "005b2bc0",
      "READ",
      [
        "storage",
        "00c6fd60",
        null,
        "pointer"
      ]
    ],
    [
      "005b2bc0",
      "READ",
      [
        "storage",
        "00c6fd68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b2b84",
      "DATA",
      [
        "storage",
        "00c6fe10",
        null,
        "undefined *"
      ]
    ],
    [
      "005b2bc0",
      "READ",
      [
        "storage",
        "00c6fe30",
        null,
        "pointer"
      ]
    ],
    [
      "005b2bc0",
      "READ",
      [
        "storage",
        "00c6fe38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b2b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md#insn-005b2b84) · [`005b2b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md#insn-005b2b40) · [`005b2b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b2b08.md#insn-005b2b58)
- 新版 `005b2bc4`（命令位置の公開資料なし） · `005b2b80`（命令位置の公開資料なし） · `005b2b98`（命令位置の公開資料なし）

~~~diff
- 005b2b84 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b2b84 ["INT_ADD", "register:40f0:8", ["const:5b2b84:8", "const:4:8"]]
- 005b2b84 ["CALLIND", null, ["register:0:8"]]
+ 005b2bc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b2bc4 ["INT_ADD", "register:40f0:8", ["const:5b2bc4:8", "const:4:8"]]
+ 005b2bc4 ["CALLIND", null, ["register:0:8"]]
- 005b2b84 bytes 00013fd6
+ 005b2bc4 bytes 00013fd6
- 005b2b40 ["COPY", "tmp:0:8", ["const:d40:8"]]
- 005b2b40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b2b40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b2b40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b2b80 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 005b2b80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2b80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b2b80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b2b40 bytes 08013591
+ 005b2b80 bytes 08413891
- 005b2b58 ["INT_ADD", "register:40f0:8", ["const:5b2b58:8", "const:4:8"]]
- 005b2b58 ["CALL", null, ["callee:005b2cd0:8"]]
+ 005b2b98 ["INT_ADD", "register:40f0:8", ["const:5b2b98:8", "const:4:8"]]
+ 005b2b98 ["CALL", null, ["callee:005b2cd0:8"]]
- 005b2b58 bytes 4e000094
+ 005b2b98 bytes 4e000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a336748952815742896d2b442a30eac2"></a>

### [`005b3348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3348.md) → [`005b3388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3388.md) FUN_005b3388

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005b3140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3140.md) [`005b3344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3344.md) [`005b5ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ffc.md) · 呼出先 6件 [`005b615c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b615c.md) [`005b6160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6160.md) [`005b61ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b61ec.md) [`005b61f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b61f0.md) [`0087ac58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087a/0087ac58.md)
- 新版 呼出元 3件 [`005b3180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3180.md) [`005b3384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3384.md) [`005b603c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b603c.md) · 呼出先 6件 [`005b619c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b619c.md) [`005b61a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b61a0.md) [`005b622c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b622c.md) [`005b6230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6230.md) [`0087acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087a/0087acb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b33b4",
      "incomplete_value": false,
      "site": "005b33b4",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3374",
      "incomplete_value": false,
      "site": "005b3374",
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
            "const:e60:8"
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
      "definition_site": "005b33c8",
      "incomplete_value": false,
      "site": "005b33c8",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3388",
      "incomplete_value": false,
      "site": "005b3388",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b33e4",
      "value": [
        "leaf",
        "ram:87acb0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b33a4",
      "value": [
        "leaf",
        "ram:87ac58:8"
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
      "005b33b4",
      "DATA",
      [
        "storage",
        "00c6fe60",
        null,
        "undefined *"
      ]
    ],
    [
      "005b33c8",
      "DATA",
      [
        "storage",
        "00c6fee0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b33e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0087ac58"
      ]
    ]
  ],
  "added": [
    [
      "005b33b4",
      "DATA",
      [
        "storage",
        "00c6ff30",
        null,
        "undefined *"
      ]
    ],
    [
      "005b33c8",
      "DATA",
      [
        "storage",
        "00c6ffb0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b33e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0087acb0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b33a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3348.md#insn-005b33a4) · [`005b3370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3348.md#insn-005b3370) · [`005b3384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3348.md#insn-005b3384)
- 新版 `005b33e4`（命令位置の公開資料なし） · `005b33b0`（命令位置の公開資料なし） · `005b33c4`（命令位置の公開資料なし）

~~~diff
- 005b33a4 ["INT_ADD", "register:40f0:8", ["const:5b33a4:8", "const:4:8"]]
- 005b33a4 ["CALL", null, ["ram:87ac58:8"]]
+ 005b33e4 ["INT_ADD", "register:40f0:8", ["const:5b33e4:8", "const:4:8"]]
+ 005b33e4 ["CALL", null, ["ram:87acb0:8"]]
- 005b33a4 bytes 2d1e0b94
+ 005b33e4 bytes 331e0b94
- 005b3370 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 005b3370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b33b0 ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 005b33b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b33b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b33b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3370 bytes 08813991
+ 005b33b0 bytes 08c13c91
- 005b3384 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 005b3384 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3384 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3384 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b33c4 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 005b33c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b33c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b33c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3384 bytes 08813b91
+ 005b33c4 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4b46a8ba00a44ec2b7ea89d97aeb7d4"></a>

### [`005b34a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b34a4.md) → [`005b34e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b34e4.md) FUN_005b34e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b6164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6164.md) · 呼出先 6件 [`005b35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md) [`005b62a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b62a0.md) [`005b62a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b62a4.md) [`005b63c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b63c8.md) [`005b63cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b63cc.md)
- 新版 呼出元 1件 [`005b61a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b61a4.md) · 呼出先 6件 [`005b3638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3638.md) [`005b62e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b62e0.md) [`005b62e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b62e4.md) [`005b6408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6408.md) [`005b640c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b640c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b350c",
      "incomplete_value": false,
      "site": "005b350c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b34cc",
      "incomplete_value": false,
      "site": "005b34cc",
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
            "const:f60:8"
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
      "definition_site": "005b3524",
      "incomplete_value": false,
      "site": "005b3524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b34e4",
      "incomplete_value": false,
      "site": "005b34e4",
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
            "const:fe0:8"
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
      "005b350c",
      "DATA",
      [
        "storage",
        "00c6ff60",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3524",
      "DATA",
      [
        "storage",
        "00c6ffe0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3560",
      "READ",
      [
        "storage",
        "00c70000",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b350c",
      "DATA",
      [
        "storage",
        "00c70030",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3524",
      "DATA",
      [
        "storage",
        "00c700b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3560",
      "READ",
      [
        "storage",
        "00c700d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b34a4.md#insn-005b3524) · [`005b34c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b34a4.md#insn-005b34c4) · [`005b34c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b34a4.md#insn-005b34c8)
- 新版 `005b3564`（命令位置の公開資料なし） · `005b3504`（命令位置の公開資料なし） · `005b3508`（命令位置の公開資料なし）

~~~diff
- 005b3524 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b3524 ["INT_ADD", "register:40f0:8", ["const:5b3524:8", "const:4:8"]]
- 005b3524 ["CALLIND", null, ["register:0:8"]]
+ 005b3564 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b3564 ["INT_ADD", "register:40f0:8", ["const:5b3564:8", "const:4:8"]]
+ 005b3564 ["CALLIND", null, ["register:0:8"]]
- 005b3524 bytes 00013fd6
+ 005b3564 bytes 00013fd6
- 005b34c4 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b3504 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b34c4 bytes e8350090
+ 005b3504 bytes e83500b0
- 005b34c8 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 005b34c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b34c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b34c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b3508 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 005b3508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b34c8 bytes 08813d91
+ 005b3508 bytes 08c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-986c5494032e8c4a2c6c762e5f9650f6"></a>

### [`005b35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md) → [`005b3638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3638.md) FUN_005b3638

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b34a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b34a4.md) · 呼出先 13件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059d354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059d/0059d354.md) [`005b7cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7cf8.md) [`005b8044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8044.md)
- 新版 呼出元 1件 [`005b34e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b34e4.md) · 呼出先 13件 [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`0059d394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059d/0059d394.md) [`005b7d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7d38.md) [`005b8084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8084.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.60% / 新版 97.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b3774",
      "incomplete_value": false,
      "site": "005b3778",
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
      "definition_site": "005b3734",
      "incomplete_value": false,
      "site": "005b3738",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b3808",
      "incomplete_value": false,
      "site": "005b3808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b37c8",
      "incomplete_value": false,
      "site": "005b37c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "005b3778",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3808",
      "DATA",
      [
        "storage",
        "00c70720",
        null,
        "undefined *"
      ]
    ],
    [
      "005b387c",
      "READ",
      [
        "storage",
        "00c70748",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b3778",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3808",
      "DATA",
      [
        "storage",
        "00c707f0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b387c",
      "READ",
      [
        "storage",
        "00c70818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b36f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md#insn-005b36f8) · [`005b36a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md#insn-005b36a8) · [`005b36e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md#insn-005b36e4)
- 新版 `005b3738`（命令位置の公開資料なし） · `005b36e8`（命令位置の公開資料なし） · `005b3724`（命令位置の公開資料なし）

~~~diff
- 005b36f8 ["INT_ADD", "register:40f0:8", ["const:5b36f8:8", "const:4:8"]]
- 005b36f8 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b3738 ["INT_ADD", "register:40f0:8", ["const:5b3738:8", "const:4:8"]]
+ 005b3738 ["CALL", null, ["callee:00c57f80:8"]]
- 005b36f8 bytes ee911a94
+ 005b3738 bytes 12921a94
- 005b36a8 ["INT_ADD", "register:40f0:8", ["const:5b36a8:8", "const:4:8"]]
- 005b36a8 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b36e8 ["INT_ADD", "register:40f0:8", ["const:5b36e8:8", "const:4:8"]]
+ 005b36e8 ["CALL", null, ["callee:00c57f60:8"]]
- 005b36a8 bytes fa911a94
+ 005b36e8 bytes 1e921a94
- 005b36e4 ["INT_ADD", "register:40f0:8", ["const:5b36e4:8", "const:4:8"]]
- 005b36e4 ["CALL", null, ["callee:0059d394:8"]]
+ 005b3724 ["INT_ADD", "register:40f0:8", ["const:5b3724:8", "const:4:8"]]
+ 005b3724 ["CALL", null, ["callee:0059d394:8"]]
- 005b36e4 bytes 1ca7ff97
+ 005b3724 bytes 1ca7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceb25846c3496ce367e82cc40ee1db63"></a>

### [`005b3a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3a28.md) → [`005b3a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3a68.md) FUN_005b3a68

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) · 呼出先 6件 [`005b3b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md) [`005b6460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6460.md) [`005b6464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6464.md) [`005b6758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6758.md) [`005b675c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b675c.md)
- 新版 呼出元 1件 [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) · 呼出先 6件 [`005b3bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3bb4.md) [`005b64a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b64a0.md) [`005b64a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b64a4.md) [`005b6798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6798.md) [`005b679c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b679c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b3a90",
      "incomplete_value": false,
      "site": "005b3a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3a50",
      "incomplete_value": false,
      "site": "005b3a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "definition_site": "005b3aa4",
      "incomplete_value": true,
      "site": "005b3aa4",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3a64",
      "incomplete_value": true,
      "site": "005b3a64",
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
            "const:140:8"
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
      "005b3a90",
      "DATA",
      [
        "storage",
        "00c70060",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3aa4",
      "DATA",
      [
        "storage",
        "00c70140",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3adc",
      "READ",
      [
        "storage",
        "00c70160",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b3a90",
      "DATA",
      [
        "storage",
        "00c70130",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3aa4",
      "DATA",
      [
        "storage",
        "00c70210",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3adc",
      "READ",
      [
        "storage",
        "00c70230",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3a28.md#insn-005b3a4c) · [`005b3a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3a28.md#insn-005b3a60) · [`005b3a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3a28.md#insn-005b3a74)
- 新版 `005b3a8c`（命令位置の公開資料なし） · `005b3aa0`（命令位置の公開資料なし） · `005b3ab4`（命令位置の公開資料なし）

~~~diff
- 005b3a4c ["COPY", "tmp:0:8", ["const:60:8"]]
- 005b3a4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3a4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3a4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b3a8c ["COPY", "tmp:0:8", ["const:130:8"]]
+ 005b3a8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3a8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3a8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3a4c bytes 08810191
+ 005b3a8c bytes 08c10491
- 005b3a60 ["COPY", "tmp:0:8", ["const:140:8"]]
- 005b3a60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3a60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3a60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b3aa0 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 005b3aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3a60 bytes 08010591
+ 005b3aa0 bytes 08410891
- 005b3a74 ["INT_ADD", "register:40f0:8", ["const:5b3a74:8", "const:4:8"]]
- 005b3a74 ["CALL", null, ["callee:005b3bb4:8"]]
+ 005b3ab4 ["INT_ADD", "register:40f0:8", ["const:5b3ab4:8", "const:4:8"]]
+ 005b3ab4 ["CALL", null, ["callee:005b3bb4:8"]]
- 005b3a74 bytes 40000094
+ 005b3ab4 bytes 40000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42f95e0c19ba04018b0288615a6a7ea9"></a>

### [`005b3b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md) → [`005b3bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3bb4.md) FUN_005b3bb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b3a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3a28.md) · 呼出先 13件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md) [`005b7184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7184.md) [`005b7520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7520.md)
- 新版 呼出元 1件 [`005b3a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3a68.md) · 呼出先 13件 [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md) [`005b71c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b71c4.md) [`005b7560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7560.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.25% / 新版 96.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b3c84",
      "incomplete_value": false,
      "site": "005b3c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3c44",
      "incomplete_value": false,
      "site": "005b3c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:610:8"
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
      "definition_site": "005b3de0",
      "incomplete_value": false,
      "site": "005b3de4",
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
      "definition_site": "005b3da0",
      "incomplete_value": false,
      "site": "005b3da4",
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
      "005b3c0c",
      "DATA",
      [
        "storage",
        "00c6dde8",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3c84",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3cf8",
      "READ",
      [
        "storage",
        "00c70638",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b3c0c",
      "DATA",
      [
        "storage",
        "00c6deb8",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3c84",
      "DATA",
      [
        "storage",
        "00c706e0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3cf8",
      "READ",
      [
        "storage",
        "00c70708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md#insn-005b3ba0) · [`005b3bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md#insn-005b3bb8) · [`005b3bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md#insn-005b3bc0)
- 新版 `005b3be0`（命令位置の公開資料なし） · `005b3bf8`（命令位置の公開資料なし） · `005b3c00`（命令位置の公開資料なし）

~~~diff
- 005b3ba0 ["INT_ADD", "register:40f0:8", ["const:5b3ba0:8", "const:4:8"]]
- 005b3ba0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b3be0 ["INT_ADD", "register:40f0:8", ["const:5b3be0:8", "const:4:8"]]
+ 005b3be0 ["CALL", null, ["callee:00c57f60:8"]]
- 005b3ba0 bytes bc901a94
+ 005b3be0 bytes e0901a94
- 005b3bb8 ["INT_ADD", "register:40f0:8", ["const:5b3bb8:8", "const:4:8"]]
- 005b3bb8 ["CALL", null, ["callee:0059b948:8"]]
+ 005b3bf8 ["INT_ADD", "register:40f0:8", ["const:5b3bf8:8", "const:4:8"]]
+ 005b3bf8 ["CALL", null, ["callee:0059b948:8"]]
- 005b3bb8 bytes 549fff97
+ 005b3bf8 bytes 549fff97
- 005b3bc0 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 005b3bc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3bc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3bc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b3c00 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 005b3c00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3c00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3c00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3bc0 bytes 08613791
+ 005b3c00 bytes 08a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5ed9db34c3b94c960647a3e92bb8dff"></a>

### [`005b3ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3ed4.md) → [`005b3f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3f14.md) FUN_005b3f14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b5bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5bac.md) · 呼出先 6件 [`005b4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md) [`005b67f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67f0.md) [`005b67f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67f4.md) [`005b6878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6878.md) [`005b687c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b687c.md)
- 新版 呼出元 1件 [`005b5bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5bec.md) · 呼出先 6件 [`005b4060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4060.md) [`005b6830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6830.md) [`005b6834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6834.md) [`005b68b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b68b8.md) [`005b68bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b68bc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b3f3c",
      "incomplete_value": false,
      "site": "005b3f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3efc",
      "incomplete_value": false,
      "site": "005b3efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
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
      "definition_site": "005b3f50",
      "incomplete_value": false,
      "site": "005b3f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b3f10",
      "incomplete_value": false,
      "site": "005b3f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:250:8"
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
      "005b3f3c",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3f50",
      "DATA",
      [
        "storage",
        "00c70250",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3f88",
      "READ",
      [
        "storage",
        "00c70270",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b3f3c",
      "DATA",
      [
        "storage",
        "00c70290",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3f50",
      "DATA",
      [
        "storage",
        "00c70320",
        null,
        "undefined *"
      ]
    ],
    [
      "005b3f88",
      "READ",
      [
        "storage",
        "00c70340",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3ed4.md#insn-005b3ef8) · [`005b3f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3ed4.md#insn-005b3f0c) · [`005b3f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3ed4.md#insn-005b3f20)
- 新版 `005b3f38`（命令位置の公開資料なし） · `005b3f4c`（命令位置の公開資料なし） · `005b3f60`（命令位置の公開資料なし）

~~~diff
- 005b3ef8 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 005b3ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b3f38 ["COPY", "tmp:0:8", ["const:290:8"]]
+ 005b3f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3ef8 bytes 08010791
+ 005b3f38 bytes 08410a91
- 005b3f0c ["COPY", "tmp:0:8", ["const:250:8"]]
- 005b3f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b3f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b3f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b3f4c ["COPY", "tmp:0:8", ["const:320:8"]]
+ 005b3f4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3f4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b3f4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b3f0c bytes 08410991
+ 005b3f4c bytes 08810c91
- 005b3f20 ["INT_ADD", "register:40f0:8", ["const:5b3f20:8", "const:4:8"]]
- 005b3f20 ["CALL", null, ["callee:005b4060:8"]]
+ 005b3f60 ["INT_ADD", "register:40f0:8", ["const:5b3f60:8", "const:4:8"]]
+ 005b3f60 ["CALL", null, ["callee:005b4060:8"]]
- 005b3f20 bytes 40000094
+ 005b3f60 bytes 40000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-216cce88860d4e7cfc5b64b244ab3561"></a>

### [`005b4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md) → [`005b4060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4060.md) FUN_005b4060

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b3ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3ed4.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059eb60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059e/0059eb60.md) [`005b84c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b84c0.md)
- 新版 呼出元 1件 [`005b3f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3f14.md) · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`0059eba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059e/0059eba0.md) [`005b8500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8500.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b411c",
      "incomplete_value": false,
      "site": "005b4120",
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
      "definition_site": "005b40dc",
      "incomplete_value": false,
      "site": "005b40e0",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b41ac",
      "incomplete_value": true,
      "site": "005b41ac",
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
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b416c",
      "incomplete_value": true,
      "site": "005b416c",
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
            "const:820:8"
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
      "005b4120",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "005b41ac",
      "DATA",
      [
        "storage",
        "00c70820",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4220",
      "READ",
      [
        "storage",
        "00c70848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4120",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b41ac",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4220",
      "READ",
      [
        "storage",
        "00c70918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b40a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md#insn-005b40a0) · [`005b4054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md#insn-005b4054) · [`005b4080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md#insn-005b4080)
- 新版 `005b40e0`（命令位置の公開資料なし） · `005b4094`（命令位置の公開資料なし） · `005b40c0`（命令位置の公開資料なし）

~~~diff
- 005b40a0 ["INT_ADD", "register:40f0:8", ["const:5b40a0:8", "const:4:8"]]
- 005b40a0 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b40e0 ["INT_ADD", "register:40f0:8", ["const:5b40e0:8", "const:4:8"]]
+ 005b40e0 ["CALL", null, ["callee:00c57f80:8"]]
- 005b40a0 bytes 848f1a94
+ 005b40e0 bytes a88f1a94
- 005b4054 ["INT_ADD", "register:40f0:8", ["const:5b4054:8", "const:4:8"]]
- 005b4054 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b4094 ["INT_ADD", "register:40f0:8", ["const:5b4094:8", "const:4:8"]]
+ 005b4094 ["CALL", null, ["callee:00c57f60:8"]]
- 005b4054 bytes 8f8f1a94
+ 005b4094 bytes b38f1a94
- 005b4080 ["INT_ADD", "register:40f0:8", ["const:5b4080:8", "const:4:8"]]
- 005b4080 ["CALL", null, ["callee:0043bb60:8"]]
+ 005b40c0 ["INT_ADD", "register:40f0:8", ["const:5b40c0:8", "const:4:8"]]
+ 005b40c0 ["CALL", null, ["callee:0043bb60:8"]]
- 005b4080 bytes a81efa97
+ 005b40c0 bytes a81efa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2f758123a76aa2192651c18329b30ae"></a>

### [`005b43cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b43cc.md) → [`005b440c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b440c.md) FUN_005b440c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b67f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67f8.md) · 呼出先 8件 [`005b4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md) [`005b6910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6910.md) [`005b6914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6914.md) [`005b6b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6b30.md) [`005b6b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6b34.md)
- 新版 呼出元 1件 [`005b6838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6838.md) · 呼出先 8件 [`005b45d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b45d0.md) [`005b6950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6950.md) [`005b6954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6954.md) [`005b6b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b70.md) [`005b6b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b74.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4434",
      "incomplete_value": false,
      "site": "005b4434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b43f4",
      "incomplete_value": false,
      "site": "005b43f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
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
      "definition_site": "005b4448",
      "incomplete_value": false,
      "site": "005b4448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4408",
      "incomplete_value": false,
      "site": "005b4408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:360:8"
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
      "definition_site": "005b445c",
      "incomplete_value": false,
      "site": "005b445c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b441c",
      "incomplete_value": false,
      "site": "005b441c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
      "005b4434",
      "DATA",
      [
        "storage",
        "00c702d0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4448",
      "DATA",
      [
        "storage",
        "00c70360",
        null,
        "undefined *"
      ]
    ],
    [
      "005b445c",
      "DATA",
      [
        "storage",
        "00c70440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4434",
      "DATA",
      [
        "storage",
        "00c703a0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4448",
      "DATA",
      [
        "storage",
        "00c70430",
        null,
        "undefined *"
      ]
    ],
    [
      "005b445c",
      "DATA",
      [
        "storage",
        "00c70510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b445c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b43cc.md#insn-005b445c) · [`005b43f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b43cc.md#insn-005b43f0) · [`005b4404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b43cc.md#insn-005b4404)
- 新版 `005b449c`（命令位置の公開資料なし） · `005b4430`（命令位置の公開資料なし） · `005b4444`（命令位置の公開資料なし）

~~~diff
- 005b445c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b445c ["INT_ADD", "register:40f0:8", ["const:5b445c:8", "const:4:8"]]
- 005b445c ["CALLIND", null, ["register:0:8"]]
+ 005b449c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b449c ["INT_ADD", "register:40f0:8", ["const:5b449c:8", "const:4:8"]]
+ 005b449c ["CALLIND", null, ["register:0:8"]]
- 005b445c bytes 00013fd6
+ 005b449c bytes 00013fd6
- 005b43f0 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 005b43f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b43f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b43f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4430 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 005b4430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b43f0 bytes 08410b91
+ 005b4430 bytes 08810e91
- 005b4404 ["COPY", "tmp:0:8", ["const:360:8"]]
- 005b4404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4444 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 005b4444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4404 bytes 08810d91
+ 005b4444 bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe1fcfc552055edbf763eb9a117ff914"></a>

### [`005b4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md) → [`005b45d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b45d0.md) FUN_005b45d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b43cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b43cc.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`005a0668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a0/005a0668.md) [`005ad2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad2ec.md) [`005ad3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad3b8.md)
- 新版 呼出元 1件 [`005b440c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b440c.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`005a06a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a0/005a06a8.md) [`005ad32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad32c.md) [`005ad3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad3f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.21% / 新版 97.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4690",
      "incomplete_value": false,
      "site": "005b4694",
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
      "definition_site": "005b4650",
      "incomplete_value": false,
      "site": "005b4654",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4720",
      "incomplete_value": false,
      "site": "005b4720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b46e0",
      "incomplete_value": false,
      "site": "005b46e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "005b4694",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4720",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4794",
      "READ",
      [
        "storage",
        "00c70918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4694",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4720",
      "DATA",
      [
        "storage",
        "00c709c0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4794",
      "READ",
      [
        "storage",
        "00c709e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md#insn-005b4614) · [`005b45c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md#insn-005b45c8) · [`005b45f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md#insn-005b45f4)
- 新版 `005b4654`（命令位置の公開資料なし） · `005b4608`（命令位置の公開資料なし） · `005b4634`（命令位置の公開資料なし）

~~~diff
- 005b4614 ["INT_ADD", "register:40f0:8", ["const:5b4614:8", "const:4:8"]]
- 005b4614 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b4654 ["INT_ADD", "register:40f0:8", ["const:5b4654:8", "const:4:8"]]
+ 005b4654 ["CALL", null, ["callee:00c57f80:8"]]
- 005b4614 bytes 278e1a94
+ 005b4654 bytes 4b8e1a94
- 005b45c8 ["INT_ADD", "register:40f0:8", ["const:5b45c8:8", "const:4:8"]]
- 005b45c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b4608 ["INT_ADD", "register:40f0:8", ["const:5b4608:8", "const:4:8"]]
+ 005b4608 ["CALL", null, ["callee:00c57f60:8"]]
- 005b45c8 bytes 328e1a94
+ 005b4608 bytes 568e1a94
- 005b45f4 ["INT_ADD", "register:40f0:8", ["const:5b45f4:8", "const:4:8"]]
- 005b45f4 ["CALL", null, ["callee:0043bb60:8"]]
+ 005b4634 ["INT_ADD", "register:40f0:8", ["const:5b4634:8", "const:4:8"]]
+ 005b4634 ["CALL", null, ["callee:0043bb60:8"]]
- 005b45f4 bytes 4b1dfa97
+ 005b4634 bytes 4b1dfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c91addf01564adb5e786f3304d6d94b"></a>

### [`005b494c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b494c.md) → [`005b498c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b498c.md) FUN_005b498c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`008a72a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a72a8.md) · 呼出先 6件 [`005b4a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4a98.md) [`005b7010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7010.md) [`005b7014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7014.md) [`005b713c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b713c.md) [`005b7140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7140.md)
- 新版 呼出元 1件 [`008a7300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a7/008a7300.md) · 呼出先 6件 [`005b4ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4ad8.md) [`005b7050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7050.md) [`005b7054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7054.md) [`005b717c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b717c.md) [`005b7180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b49b4",
      "incomplete_value": false,
      "site": "005b49b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:590:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4974",
      "incomplete_value": false,
      "site": "005b4974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
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
      "definition_site": "005b49c8",
      "incomplete_value": false,
      "site": "005b49c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4988",
      "incomplete_value": false,
      "site": "005b4988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "005b49b4",
      "DATA",
      [
        "storage",
        "00c704c0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b49c8",
      "DATA",
      [
        "storage",
        "00c70540",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4a00",
      "READ",
      [
        "storage",
        "00c70560",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b49b4",
      "DATA",
      [
        "storage",
        "00c70590",
        null,
        "undefined *"
      ]
    ],
    [
      "005b49c8",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4a00",
      "READ",
      [
        "storage",
        "00c70630",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b494c.md#insn-005b4970) · [`005b4984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b494c.md#insn-005b4984) · [`005b4998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b494c.md#insn-005b4998)
- 新版 `005b49b0`（命令位置の公開資料なし） · `005b49c4`（命令位置の公開資料なし） · `005b49d8`（命令位置の公開資料なし）

~~~diff
- 005b4970 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 005b4970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b49b0 ["COPY", "tmp:0:8", ["const:590:8"]]
+ 005b49b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b49b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b49b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4970 bytes 08011391
+ 005b49b0 bytes 08411691
- 005b4984 ["COPY", "tmp:0:8", ["const:540:8"]]
- 005b4984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b49c4 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 005b49c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b49c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b49c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4984 bytes 08011591
+ 005b49c4 bytes 08411891
- 005b4998 ["INT_ADD", "register:40f0:8", ["const:5b4998:8", "const:4:8"]]
- 005b4998 ["CALL", null, ["callee:005b4ad8:8"]]
+ 005b49d8 ["INT_ADD", "register:40f0:8", ["const:5b49d8:8", "const:4:8"]]
+ 005b49d8 ["CALL", null, ["callee:005b4ad8:8"]]
- 005b4998 bytes 40000094
+ 005b49d8 bytes 40000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b986276509f27d82dc33c3703a15f5fd"></a>

### [`005b4a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4a98.md) → [`005b4ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4ad8.md) FUN_005b4ad8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b494c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b494c.md) · 呼出先 13件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md) [`005b8fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8fb4.md) [`005b9300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9300.md)
- 新版 呼出元 1件 [`005b498c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b498c.md) · 呼出先 13件 [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md) [`005b8ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8ff4.md) [`005b9340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9340.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4b2c",
      "incomplete_value": false,
      "site": "005b4b30",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:328:8"
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
      "definition_site": "005b4aec",
      "incomplete_value": false,
      "site": "005b4af0",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:258:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4b5c",
      "incomplete_value": false,
      "site": "005b4b60",
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
      "definition_site": "005b4b1c",
      "incomplete_value": false,
      "site": "005b4b20",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4bec",
      "incomplete_value": false,
      "site": "005b4bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b4bac",
      "incomplete_value": false,
      "site": "005b4bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c70000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "005b4b30",
      "DATA",
      [
        "storage",
        "00c6e268",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4b60",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4bec",
      "DATA",
      [
        "storage",
        "00c70970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b4b30",
      "DATA",
      [
        "storage",
        "00c6e338",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4b60",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "005b4bec",
      "DATA",
      [
        "storage",
        "00c70a40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b4ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4a98.md#insn-005b4ac4) · [`005b4adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4a98.md#insn-005b4adc) · [`005b4ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4a98.md#insn-005b4ae4)
- 新版 `005b4b04`（命令位置の公開資料なし） · `005b4b1c`（命令位置の公開資料なし） · `005b4b24`（命令位置の公開資料なし）

~~~diff
- 005b4ac4 ["INT_ADD", "register:40f0:8", ["const:5b4ac4:8", "const:4:8"]]
- 005b4ac4 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b4b04 ["INT_ADD", "register:40f0:8", ["const:5b4b04:8", "const:4:8"]]
+ 005b4b04 ["CALL", null, ["callee:00c57f60:8"]]
- 005b4ac4 bytes f38c1a94
+ 005b4b04 bytes 178d1a94
- 005b4adc ["INT_ADD", "register:40f0:8", ["const:5b4adc:8", "const:4:8"]]
- 005b4adc ["CALL", null, ["callee:0059b948:8"]]
+ 005b4b1c ["INT_ADD", "register:40f0:8", ["const:5b4b1c:8", "const:4:8"]]
+ 005b4b1c ["CALL", null, ["callee:0059b948:8"]]
- 005b4adc bytes 8b9bff97
+ 005b4b1c bytes 8b9bff97
- 005b4ae4 ["COPY", "tmp:0:8", ["const:258:8"]]
- 005b4ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4b24 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 005b4b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4ae4 bytes 08610991
+ 005b4b24 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2adbe7bcfe5c64faea05654a64fdf250"></a>

### [`005b4df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4df0.md) → [`005b4e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4e30.md) FUN_005b4e30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b4e54",
      "incomplete_value": true,
      "site": "005b4e58",
      "value": [
        "INT_ADD",
        "8",
        [
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
      "definition_site": "005b4e14",
      "incomplete_value": true,
      "site": "005b4e18",
      "value": [
        "INT_ADD",
        "8",
        [
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
      "005b4e58",
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
      "005b4e58",
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

- 旧版 [`005b4e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4df0.md#insn-005b4e0c) · [`005b4e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4df0.md#insn-005b4e24) · [`005b4e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4df0.md#insn-005b4e34)
- 新版 `005b4e4c`（命令位置の公開資料なし） · `005b4e64`（命令位置の公開資料なし） · `005b4e74`（命令位置の公開資料なし）

~~~diff
- 005b4e0c ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005b4e0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b4e0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b4e0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b4e4c ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005b4e4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4e4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b4e4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b4e0c bytes 08412891
+ 005b4e4c bytes 08812b91
- 005b4e24 ["INT_ADD", "register:40f0:8", ["const:5b4e24:8", "const:4:8"]]
- 005b4e24 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b4e64 ["INT_ADD", "register:40f0:8", ["const:5b4e64:8", "const:4:8"]]
+ 005b4e64 ["CALL", null, ["callee:00c57f80:8"]]
- 005b4e24 bytes 238c1a94
+ 005b4e64 bytes 478c1a94
- 005b4e34 ["INT_ADD", "register:40f0:8", ["const:5b4e34:8", "const:4:8"]]
- 005b4e34 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b4e74 ["INT_ADD", "register:40f0:8", ["const:5b4e74:8", "const:4:8"]]
+ 005b4e74 ["CALL", null, ["callee:00c57f80:8"]]
- 005b4e34 bytes 1f8c1a94
+ 005b4e74 bytes 438c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf327c65aa8b64c1895f190b848f9b02"></a>

### [`005b5014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5014.md) → [`005b5054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5054.md) FUN_005b5054

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b5088",
      "incomplete_value": false,
      "site": "005b508c",
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
      "definition_site": "005b5048",
      "incomplete_value": false,
      "site": "005b504c",
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
      "005b508c",
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
      "005b508c",
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

- 旧版 [`005b5038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5014.md#insn-005b5038) · [`005b5040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5014.md#insn-005b5040) · [`005b5058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5014.md#insn-005b5058)
- 新版 `005b5078`（命令位置の公開資料なし） · `005b5080`（命令位置の公開資料なし） · `005b5098`（命令位置の公開資料なし）

~~~diff
- 005b5038 ["INT_ADD", "register:40f0:8", ["const:5b5038:8", "const:4:8"]]
- 005b5038 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b5078 ["INT_ADD", "register:40f0:8", ["const:5b5078:8", "const:4:8"]]
+ 005b5078 ["CALL", null, ["callee:00c57f80:8"]]
- 005b5038 bytes 9e8b1a94
+ 005b5078 bytes c28b1a94
- 005b5040 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005b5040 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5040 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5040 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5080 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005b5080 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5080 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5080 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5040 bytes 08412891
+ 005b5080 bytes 08812b91
- 005b5058 ["INT_ADD", "register:40f0:8", ["const:5b5058:8", "const:4:8"]]
- 005b5058 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b5098 ["INT_ADD", "register:40f0:8", ["const:5b5098:8", "const:4:8"]]
+ 005b5098 ["CALL", null, ["callee:00c57f80:8"]]
- 005b5058 bytes 968b1a94
+ 005b5098 bytes ba8b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0298a3d5c0f46ba0afe36a005cd9b1e"></a>

### [`005b5088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5088.md) → [`005b50c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b50c8.md) FUN_005b50c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b50fc",
      "incomplete_value": false,
      "site": "005b5100",
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
      "definition_site": "005b50bc",
      "incomplete_value": false,
      "site": "005b50c0",
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
      "005b5100",
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
      "005b5100",
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

- 旧版 [`005b50ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5088.md#insn-005b50ac) · [`005b50b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5088.md#insn-005b50b4) · [`005b50cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5088.md#insn-005b50cc)
- 新版 `005b50ec`（命令位置の公開資料なし） · `005b50f4`（命令位置の公開資料なし） · `005b510c`（命令位置の公開資料なし）

~~~diff
- 005b50ac ["INT_ADD", "register:40f0:8", ["const:5b50ac:8", "const:4:8"]]
- 005b50ac ["CALL", null, ["callee:00c57f80:8"]]
+ 005b50ec ["INT_ADD", "register:40f0:8", ["const:5b50ec:8", "const:4:8"]]
+ 005b50ec ["CALL", null, ["callee:00c57f80:8"]]
- 005b50ac bytes 818b1a94
+ 005b50ec bytes a58b1a94
- 005b50b4 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005b50b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b50b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b50b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b50f4 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005b50f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b50f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b50f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b50b4 bytes 08412891
+ 005b50f4 bytes 08812b91
- 005b50cc ["INT_ADD", "register:40f0:8", ["const:5b50cc:8", "const:4:8"]]
- 005b50cc ["CALL", null, ["callee:00c57f80:8"]]
+ 005b510c ["INT_ADD", "register:40f0:8", ["const:5b510c:8", "const:4:8"]]
+ 005b510c ["CALL", null, ["callee:00c57f80:8"]]
- 005b50cc bytes 798b1a94
+ 005b510c bytes 9d8b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3083ae5db8472086bce3600ad1f72533"></a>

### [`005b50fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b50fc.md) → [`005b513c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b513c.md) FUN_005b513c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b5170",
      "incomplete_value": false,
      "site": "005b5174",
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
      "definition_site": "005b5130",
      "incomplete_value": false,
      "site": "005b5134",
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
      "005b5174",
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
      "005b5174",
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

- 旧版 [`005b5120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b50fc.md#insn-005b5120) · [`005b5128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b50fc.md#insn-005b5128) · [`005b5140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b50fc.md#insn-005b5140)
- 新版 `005b5160`（命令位置の公開資料なし） · `005b5168`（命令位置の公開資料なし） · `005b5180`（命令位置の公開資料なし）

~~~diff
- 005b5120 ["INT_ADD", "register:40f0:8", ["const:5b5120:8", "const:4:8"]]
- 005b5120 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b5160 ["INT_ADD", "register:40f0:8", ["const:5b5160:8", "const:4:8"]]
+ 005b5160 ["CALL", null, ["callee:00c57f80:8"]]
- 005b5120 bytes 648b1a94
+ 005b5160 bytes 888b1a94
- 005b5128 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005b5128 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5128 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5128 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5168 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005b5168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5128 bytes 08412891
+ 005b5168 bytes 08812b91
- 005b5140 ["INT_ADD", "register:40f0:8", ["const:5b5140:8", "const:4:8"]]
- 005b5140 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b5180 ["INT_ADD", "register:40f0:8", ["const:5b5180:8", "const:4:8"]]
+ 005b5180 ["CALL", null, ["callee:00c57f80:8"]]
- 005b5140 bytes 5c8b1a94
+ 005b5180 bytes 808b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8112891cc8891f8597488dafabf8d59c"></a>

### [`005b5170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5170.md) → [`005b51b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b51b0.md) FUN_005b51b0

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
      "definition_site": "005b51d4",
      "incomplete_value": false,
      "site": "005b51d8",
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
      "definition_site": "005b5194",
      "incomplete_value": false,
      "site": "005b5198",
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
      "005b51d8",
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
      "005b51d8",
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

- 旧版 [`005b518c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5170.md#insn-005b518c) · [`005b51a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5170.md#insn-005b51a4) · [`005b51b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5170.md#insn-005b51b4)
- 新版 `005b51cc`（命令位置の公開資料なし） · `005b51e4`（命令位置の公開資料なし） · `005b51f4`（命令位置の公開資料なし）

~~~diff
- 005b518c ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005b518c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b518c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b518c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b51cc ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005b51cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b51cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b51cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b518c bytes 08412891
+ 005b51cc bytes 08812b91
- 005b51a4 ["INT_ADD", "register:40f0:8", ["const:5b51a4:8", "const:4:8"]]
- 005b51a4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b51e4 ["INT_ADD", "register:40f0:8", ["const:5b51e4:8", "const:4:8"]]
+ 005b51e4 ["CALL", null, ["callee:00c57f80:8"]]
- 005b51a4 bytes 438b1a94
+ 005b51e4 bytes 678b1a94
- 005b51b4 ["INT_ADD", "register:40f0:8", ["const:5b51b4:8", "const:4:8"]]
- 005b51b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b51f4 ["INT_ADD", "register:40f0:8", ["const:5b51f4:8", "const:4:8"]]
+ 005b51f4 ["CALL", null, ["callee:00c57f80:8"]]
- 005b51b4 bytes 3f8b1a94
+ 005b51f4 bytes 638b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e39aa86e509209418e540bf44c5f8a97"></a>

### [`005b51d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b51d4.md) → [`005b5214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5214.md) FUN_005b5214

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
      "definition_site": "005b5218",
      "incomplete_value": false,
      "site": "005b521c",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b51d8",
      "incomplete_value": false,
      "site": "005b51dc",
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
            "const:660:8"
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
      "005b521c",
      "DATA",
      [
        "storage",
        "00c6f660",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b521c",
      "DATA",
      [
        "storage",
        "00c6f730",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b51d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b51d4.md#insn-005b51d8)
- 新版 `005b5218`（命令位置の公開資料なし）

~~~diff
- 005b51d8 ["COPY", "tmp:0:8", ["const:660:8"]]
- 005b51d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b51d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b51d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5218 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 005b5218 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5218 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5218 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b51d8 bytes 08811991
+ 005b5218 bytes 08c11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

