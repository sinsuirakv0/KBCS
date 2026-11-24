# v16.0.1 → v16.0.2 · 最優先の変更候補 (40)

[一覧の目次](README.md)

<a id="compare-2c82816e20dab50c6445272f26bb821a"></a>

### [`007b00f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b00f8.md) → [`007b0150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0150.md) FUN_007b0150

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "007b0168",
      "incomplete_value": false,
      "site": "007b0174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007b0110",
      "incomplete_value": false,
      "site": "007b011c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "007b0174",
      "DATA",
      [
        "storage",
        "00c7aa98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b0174",
      "DATA",
      [
        "storage",
        "00c7ab68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b0110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b00f8.md#insn-007b0110) · [`007b0140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b00f8.md#insn-007b0140)
- 新版 `007b0168`（命令位置の公開資料なし） · `007b0198`（命令位置の公開資料なし）

~~~diff
- 007b0110 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 007b0110 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007b0110 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007b0110 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007b0168 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 007b0168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007b0168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007b0168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007b0110 bytes 08612a91
+ 007b0168 bytes 08a12d91
- 007b0140 ["COPY", "register:0:8", ["register:4040:8"]]
- 007b0140 ["INT_ADD", "register:40f0:8", ["const:7b0140:8", "const:4:8"]]
- 007b0140 ["CALLIND", null, ["register:0:8"]]
+ 007b0198 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007b0198 ["INT_ADD", "register:40f0:8", ["const:7b0198:8", "const:4:8"]]
+ 007b0198 ["CALLIND", null, ["register:0:8"]]
- 007b0140 bytes 00013fd6
+ 007b0198 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11c4590dc862e6101b04dd7d30f82395"></a>

### [`007b0154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0154.md) → [`007b01ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b01ac.md) FUN_007b01ac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007b01d8",
      "incomplete_value": false,
      "site": "007b01d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007b0180",
      "incomplete_value": false,
      "site": "007b0180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "007b01d8",
      "DATA",
      [
        "storage",
        "00c7aa98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b01d8",
      "DATA",
      [
        "storage",
        "00c7ab68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b0168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0154.md#insn-007b0168) · [`007b0178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0154.md#insn-007b0178) · [`007b019c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0154.md#insn-007b019c)
- 新版 `007b01c0`（命令位置の公開資料なし） · `007b01d0`（命令位置の公開資料なし） · `007b01f4`（命令位置の公開資料なし）

~~~diff
- 007b0168 ["INT_ADD", "register:40f0:8", ["const:7b0168:8", "const:4:8"]]
- 007b0168 ["CALL", null, ["callee:00c57f60:8"]]
+ 007b01c0 ["INT_ADD", "register:40f0:8", ["const:7b01c0:8", "const:4:8"]]
+ 007b01c0 ["CALL", null, ["callee:00c57f60:8"]]
- 007b0168 bytes 4a9f1294
+ 007b01c0 bytes 689f1294
- 007b0178 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 007b0178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007b0178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007b0178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007b01d0 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 007b01d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007b01d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007b01d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007b0178 bytes 08612a91
+ 007b01d0 bytes 08a12d91
- 007b019c ["COPY", "register:0:8", ["register:4040:8"]]
- 007b019c ["INT_ADD", "register:40f0:8", ["const:7b019c:8", "const:4:8"]]
- 007b019c ["CALLIND", null, ["register:0:8"]]
+ 007b01f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007b01f4 ["INT_ADD", "register:40f0:8", ["const:7b01f4:8", "const:4:8"]]
+ 007b01f4 ["CALLIND", null, ["register:0:8"]]
- 007b019c bytes 00013fd6
+ 007b01f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-563da611d5e1a319428118f2a6b2ba4b"></a>

### [`007b01dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b01dc.md) → [`007b0234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0234.md) FUN_007b0234

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007b0250",
      "incomplete_value": false,
      "site": "007b0250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007b01f8",
      "incomplete_value": false,
      "site": "007b01f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "007b0250",
      "DATA",
      [
        "storage",
        "00c7aa98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b0250",
      "DATA",
      [
        "storage",
        "00c7ab68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b01f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b01dc.md#insn-007b01f4) · [`007b0218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b01dc.md#insn-007b0218)
- 新版 `007b024c`（命令位置の公開資料なし） · `007b0270`（命令位置の公開資料なし）

~~~diff
- 007b01f4 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 007b01f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007b01f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007b01f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007b024c ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 007b024c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007b024c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007b024c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007b01f4 bytes 29612a91
+ 007b024c bytes 29a12d91
- 007b0218 ["COPY", "register:0:8", ["register:4048:8"]]
- 007b0218 ["INT_ADD", "register:40f0:8", ["const:7b0218:8", "const:4:8"]]
- 007b0218 ["CALLIND", null, ["register:0:8"]]
+ 007b0270 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007b0270 ["INT_ADD", "register:40f0:8", ["const:7b0270:8", "const:4:8"]]
+ 007b0270 ["CALLIND", null, ["register:0:8"]]
- 007b0218 bytes 20013fd6
+ 007b0270 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a50503f2ada27dbdb814a6aa02cf4185"></a>

### [`007b0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0320.md) → [`007b0378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0378.md) FUN_007b0378

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007b0384",
      "incomplete_value": false,
      "site": "007b0390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007b032c",
      "incomplete_value": false,
      "site": "007b0338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "007b0390",
      "DATA",
      [
        "storage",
        "00c7ab18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b0390",
      "DATA",
      [
        "storage",
        "00c7abe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b032c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0320.md#insn-007b032c)
- 新版 `007b0384`（命令位置の公開資料なし）

~~~diff
- 007b032c ["COPY", "tmp:0:8", ["const:b18:8"]]
- 007b032c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007b032c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007b032c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007b0384 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 007b0384 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007b0384 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007b0384 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007b032c bytes 4a612c91
+ 007b0384 bytes 4aa12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2efc9932129623d81c90dcde7e8b7ae3"></a>

### [`007b03c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b03c0.md) → [`007b0418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0418.md) FUN_007b0418

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007b0444",
      "incomplete_value": false,
      "site": "007b0444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007b03ec",
      "incomplete_value": false,
      "site": "007b03ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "007b0444",
      "DATA",
      [
        "storage",
        "00c7ab18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b0444",
      "DATA",
      [
        "storage",
        "00c7abe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b03d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b03c0.md#insn-007b03d4) · [`007b03e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b03c0.md#insn-007b03e4) · [`007b0408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b03c0.md#insn-007b0408)
- 新版 `007b042c`（命令位置の公開資料なし） · `007b043c`（命令位置の公開資料なし） · `007b0460`（命令位置の公開資料なし）

~~~diff
- 007b03d4 ["INT_ADD", "register:40f0:8", ["const:7b03d4:8", "const:4:8"]]
- 007b03d4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007b042c ["INT_ADD", "register:40f0:8", ["const:7b042c:8", "const:4:8"]]
+ 007b042c ["CALL", null, ["callee:00c57f60:8"]]
- 007b03d4 bytes af9e1294
+ 007b042c bytes cd9e1294
- 007b03e4 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 007b03e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007b03e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007b03e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007b043c ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 007b043c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007b043c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007b043c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007b03e4 bytes 08612c91
+ 007b043c bytes 08a12f91
- 007b0408 ["COPY", "register:0:8", ["register:4040:8"]]
- 007b0408 ["INT_ADD", "register:40f0:8", ["const:7b0408:8", "const:4:8"]]
- 007b0408 ["CALLIND", null, ["register:0:8"]]
+ 007b0460 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007b0460 ["INT_ADD", "register:40f0:8", ["const:7b0460:8", "const:4:8"]]
+ 007b0460 ["CALLIND", null, ["register:0:8"]]
- 007b0408 bytes 00013fd6
+ 007b0460 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81fa9fc7547deb93122d8ee86e564584"></a>

### [`007b0448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0448.md) → [`007b04a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b04a0.md) FUN_007b04a0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007b04bc",
      "incomplete_value": false,
      "site": "007b04bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007b0464",
      "incomplete_value": false,
      "site": "007b0464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "007b04bc",
      "DATA",
      [
        "storage",
        "00c7ab18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b04bc",
      "DATA",
      [
        "storage",
        "00c7abe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b0460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0448.md#insn-007b0460) · [`007b0484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0448.md#insn-007b0484)
- 新版 `007b04b8`（命令位置の公開資料なし） · `007b04dc`（命令位置の公開資料なし）

~~~diff
- 007b0460 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 007b0460 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007b0460 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007b0460 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007b04b8 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 007b04b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007b04b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007b04b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007b0460 bytes 29612c91
+ 007b04b8 bytes 29a12f91
- 007b0484 ["COPY", "register:0:8", ["register:4048:8"]]
- 007b0484 ["INT_ADD", "register:40f0:8", ["const:7b0484:8", "const:4:8"]]
- 007b0484 ["CALLIND", null, ["register:0:8"]]
+ 007b04dc ["COPY", "register:0:8", ["register:4048:8"]]
+ 007b04dc ["INT_ADD", "register:40f0:8", ["const:7b04dc:8", "const:4:8"]]
+ 007b04dc ["CALLIND", null, ["register:0:8"]]
- 007b0484 bytes 20013fd6
+ 007b04dc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ab092b04ce1c7decc5e6206b7557a7e"></a>

### [`007b058c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b058c.md) → [`007b05e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b05e4.md) _INIT_145

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "007b0664",
      "incomplete_value": true,
      "site": "007b0680",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007b060c",
      "incomplete_value": true,
      "site": "007b0628",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007b0684",
      "incomplete_value": true,
      "site": "007b069c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007b062c",
      "incomplete_value": true,
      "site": "007b0644",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007b06a0",
      "incomplete_value": true,
      "site": "007b06bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007b0648",
      "incomplete_value": true,
      "site": "007b0664",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007b0620",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "007b0644",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "007b0664",
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
      "007b0620",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "007b0644",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "007b0664",
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

- 旧版 [`007b0680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b058c.md#insn-007b0680) · [`007b07c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b058c.md#insn-007b07c0) · [`007b05b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b058c.md#insn-007b05b4)
- 新版 `007b06d8`（命令位置の公開資料なし） · `007b0818`（命令位置の公開資料なし） · `007b060c`（命令位置の公開資料なし）

~~~diff
- 007b0680 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 007b0680 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007b0680 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007b0680 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007b06d8 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 007b06d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007b06d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007b06d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007b0680 bytes 29253c91
+ 007b06d8 bytes 29f13a91
- 007b07c0 ["INT_ADD", "register:40f0:8", ["const:7b07c0:8", "const:4:8"]]
- 007b07c0 ["CALL", null, ["callee:00c57f00:8"]]
+ 007b0818 ["INT_ADD", "register:40f0:8", ["const:7b0818:8", "const:4:8"]]
+ 007b0818 ["CALL", null, ["callee:00c57f00:8"]]
- 007b07c0 bytes 9c9d1294
+ 007b0818 bytes ba9d1294
- 007b05b4 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 007b060c ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 007b05b4 bytes b32700f0
+ 007b060c bytes d3270090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84fa789a64bfc1661daa0ad1744f844e"></a>

### [`007bbcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbcb0.md) → [`007bbd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbd08.md) FUN_007bbd08

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`006bed5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006be/006bed5c.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00934078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934078.md) · 呼出先 5件 [`008001cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001cc.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`008077f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00807/008077f8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a65dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65dec.md)
- 新版 呼出元 9件 [`006bedb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bedb4.md) [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`009340cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00934/009340cc.md) · 呼出先 5件 [`00800224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800224.md) [`00802f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802f38.md) [`00807850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/00807850.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a65e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a65/00a65e5c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

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
      "site": "007bbd80",
      "value": [
        "leaf",
        "ram:a65e5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007bbd28",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007bbd24",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ],
    [
      "007bbd80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ],
  "added": [
    [
      "007bbd24",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[59]"
      ]
    ],
    [
      "007bbd80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bbcd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbcb0.md#insn-007bbcd0) · [`007bbd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbcb0.md#insn-007bbd28) · [`007bbcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbcb0.md#insn-007bbcc0)
- 新版 `007bbd28`（命令位置の公開資料なし） · `007bbd80`（命令位置の公開資料なし） · `007bbd18`（命令位置の公開資料なし）

~~~diff
- 007bbcd0 ["INT_ADD", "register:40f0:8", ["const:7bbcd0:8", "const:4:8"]]
- 007bbcd0 ["CALL", null, ["callee:00800224:8"]]
+ 007bbd28 ["INT_ADD", "register:40f0:8", ["const:7bbd28:8", "const:4:8"]]
+ 007bbd28 ["CALL", null, ["callee:00800224:8"]]
- 007bbcd0 bytes 3f110194
+ 007bbd28 bytes 3f110194
- 007bbd28 ["INT_ADD", "register:40f0:8", ["const:7bbd28:8", "const:4:8"]]
- 007bbd28 ["CALL", null, ["ram:a65dec:8"]]
+ 007bbd80 ["INT_ADD", "register:40f0:8", ["const:7bbd80:8", "const:4:8"]]
+ 007bbd80 ["CALL", null, ["ram:a65e5c:8"]]
- 007bbd28 bytes 31a80a94
+ 007bbd80 bytes 37a80a94
- 007bbcc0 ["INT_ADD", "register:40f0:8", ["const:7bbcc0:8", "const:4:8"]]
- 007bbcc0 ["CALL", null, ["callee:00851550:8"]]
+ 007bbd18 ["INT_ADD", "register:40f0:8", ["const:7bbd18:8", "const:4:8"]]
+ 007bbd18 ["CALL", null, ["callee:00851550:8"]]
- 007bbcc0 bytes 0e560294
+ 007bbd18 bytes 0e560294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2c48929c0a04b05f835df47a25b02be"></a>

### [`007bbd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbd48.md) → [`007bbda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbda0.md) FUN_007bbda0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 13件 [`006bed5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006be/006bed5c.md) [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 7件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`00805fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805fe4.md)
- 新版 呼出元 13件 [`006bedb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bedb4.md) [`007b0a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0a70.md) [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007cb638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cb/007cb638.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 7件 [`00802710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802710.md) [`00802be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802be4.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00802f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802f38.md) [`0080603c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00806/0080603c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "site": "007bbe24",
      "value": [
        "leaf",
        "ram:a65e5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007bbdcc",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007bbe24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ],
  "added": [
    [
      "007bbe24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bbd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbd48.md#insn-007bbd74) · [`007bbdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbd48.md#insn-007bbdcc) · [`007bbd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbd48.md#insn-007bbd60)
- 新版 `007bbdcc`（命令位置の公開資料なし） · `007bbe24`（命令位置の公開資料なし） · `007bbdb8`（命令位置の公開資料なし）

~~~diff
- 007bbd74 ["INT_ADD", "register:40f0:8", ["const:7bbd74:8", "const:4:8"]]
- 007bbd74 ["CALL", null, ["callee:00802be4:8"]]
+ 007bbdcc ["INT_ADD", "register:40f0:8", ["const:7bbdcc:8", "const:4:8"]]
+ 007bbdcc ["CALL", null, ["callee:00802be4:8"]]
- 007bbd74 bytes 861b0194
+ 007bbdcc bytes 861b0194
- 007bbdcc ["INT_ADD", "register:40f0:8", ["const:7bbdcc:8", "const:4:8"]]
- 007bbdcc ["CALL", null, ["ram:a65dec:8"]]
+ 007bbe24 ["INT_ADD", "register:40f0:8", ["const:7bbe24:8", "const:4:8"]]
+ 007bbe24 ["CALL", null, ["ram:a65e5c:8"]]
- 007bbdcc bytes 08a80a94
+ 007bbe24 bytes 0ea80a94
- 007bbd60 ["INT_ADD", "register:40f0:8", ["const:7bbd60:8", "const:4:8"]]
- 007bbd60 ["CALL", null, ["callee:00802710:8"]]
+ 007bbdb8 ["INT_ADD", "register:40f0:8", ["const:7bbdb8:8", "const:4:8"]]
+ 007bbdb8 ["CALL", null, ["callee:00802710:8"]]
- 007bbd60 bytes 561a0194
+ 007bbdb8 bytes 561a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-309f3ce25412ccb807680e58ffd12eac"></a>

### [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) → [`007bbe74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbe74.md) FUN_007bbe74

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) · 呼出先 30件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md)
- 新版 呼出元 1件 [`007b0a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0a70.md) · 呼出先 30件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007bcce0",
      "incomplete_value": true,
      "site": "007bccf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bcc88",
      "incomplete_value": true,
      "site": "007bcca0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:116:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 316,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007bce2c",
      "incomplete_value": true,
      "site": "007bce40",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:a1b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007bcdd4",
      "incomplete_value": true,
      "site": "007bcde8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:a6f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 330,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007bce44",
      "incomplete_value": true,
      "site": "007bce44",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007bcdec",
      "incomplete_value": true,
      "site": "007bcdec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 331,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007bcccc",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "007bcce0",
      "READ",
      [
        "storage",
        "002bf116",
        null,
        "string"
      ]
    ],
    [
      "007bcd3c",
      "READ",
      [
        "storage",
        "002a908a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007bcccc",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "007bcce0",
      "READ",
      [
        "storage",
        "002bf0c2",
        null,
        "string"
      ]
    ],
    [
      "007bcd3c",
      "READ",
      [
        "storage",
        "002a90b9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bcc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md#insn-007bcc48) · [`007bcd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md#insn-007bcd4c) · [`007bcf54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md#insn-007bcf54)
- 新版 `007bcca0`（命令位置の公開資料なし） · `007bcda4`（命令位置の公開資料なし） · `007bcfac`（命令位置の公開資料なし）

~~~diff
- 007bcc48 ["INT_ADD", "register:40f0:8", ["const:7bcc48:8", "const:4:8"]]
- 007bcc48 ["CALL", null, ["callee:00851550:8"]]
+ 007bcca0 ["INT_ADD", "register:40f0:8", ["const:7bcca0:8", "const:4:8"]]
+ 007bcca0 ["CALL", null, ["callee:00851550:8"]]
- 007bcc48 bytes 2c520294
+ 007bcca0 bytes 2c520294
- 007bcd4c ["INT_ADD", "register:40f0:8", ["const:7bcd4c:8", "const:4:8"]]
- 007bcd4c ["CALL", null, ["callee:0047e64c:8"]]
+ 007bcda4 ["INT_ADD", "register:40f0:8", ["const:7bcda4:8", "const:4:8"]]
+ 007bcda4 ["CALL", null, ["callee:0047e64c:8"]]
- 007bcd4c bytes 3006f397
+ 007bcda4 bytes 2a06f397
- 007bcf54 ["INT_ADD", "register:40f0:8", ["const:7bcf54:8", "const:4:8"]]
- 007bcf54 ["CALL", null, ["callee:007f18ec:8"]]
+ 007bcfac ["INT_ADD", "register:40f0:8", ["const:7bcfac:8", "const:4:8"]]
+ 007bcfac ["CALL", null, ["callee:007f18ec:8"]]
- 007bcf54 bytes 50d20094
+ 007bcfac bytes 50d20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9d5c24f6cf4bd19fba623431ee8f2c3"></a>

### [`007c7bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7bc0.md) → [`007c7c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c7/007c7c18.md) FUN_007c7c18

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 15件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md)
- 新版 呼出元 2件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 15件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`004881b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004881b8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.77% / 新版 94.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c7c50",
      "incomplete_value": false,
      "site": "007c7c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c7bf8",
      "incomplete_value": false,
      "site": "007c7c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "definition_site": "007c7dfc",
      "incomplete_value": true,
      "site": "007c7e00",
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
      "definition_site": "007c7da4",
      "incomplete_value": true,
      "site": "007c7da8",
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
      "007c7c5c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "007c7c64",
      "READ",
      [
        "storage",
        "002a6b3d",
        null,
        "string"
      ]
    ],
    [
      "007c7dc8",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c7c5c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "007c7c64",
      "READ",
      [
        "storage",
        "002a6ae1",
        null,
        "string"
      ]
    ],
    [
      "007c7dc8",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c7bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7bc0.md#insn-007c7bf0) · [`007c7bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7bc0.md#insn-007c7bf8) · [`007c7bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7bc0.md#insn-007c7bfc)
- 新版 `007c7c48`（命令位置の公開資料なし） · `007c7c50`（命令位置の公開資料なし）

~~~diff
- 007c7bf0 ["INT_ADD", "register:40f0:8", ["const:7c7bf0:8", "const:4:8"]]
- 007c7bf0 ["CALL", null, ["callee:00487e60:8"]]
+ 007c7c48 ["INT_ADD", "register:40f0:8", ["const:7c7c48:8", "const:4:8"]]
+ 007c7c48 ["CALL", null, ["callee:00487e60:8"]]
- 007c7bf0 bytes 8c00f397
+ 007c7c48 bytes 8600f397
- 007c7bf8 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 007c7bf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c7bf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c7bf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c7c50 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 007c7c50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7c50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7c50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c7bf8 bytes 08e13491
+ 007c7c50 bytes 08213891
- 007c7bfc ["COPY", "register:4048:8", ["const:2a6000:8"]]
- 007c7bfc bytes e9d6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dc454f48dbabf82854ee46e65b20422"></a>

### [`007c800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c8/007c800c.md) → [`007c8064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c8/007c8064.md) FUN_007c8064

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 24件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0071d034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d034.md)
- 新版 呼出元 2件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 24件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0071d08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d08c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.36% / 新版 93.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 11件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007c8b54",
      "incomplete_value": false,
      "site": "007c8b54",
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
                "const:ca5000:8"
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
      "definition_site": "007c8afc",
      "incomplete_value": false,
      "site": "007c8afc",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
    "ordinal": 89,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007c8b58",
      "incomplete_value": false,
      "site": "007c8b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c8b00",
      "incomplete_value": false,
      "site": "007c8b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "ordinal": 90,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c8b54",
      "incomplete_value": false,
      "site": "007c8b58",
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
                "const:ca5000:8"
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
      "definition_site": "007c8afc",
      "incomplete_value": false,
      "site": "007c8b00",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007c80ac",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007c80c0",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c80c8",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c80ac",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c80c0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c80c8",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c8/007c800c.md#insn-007c8488) · [`007c89f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c8/007c800c.md#insn-007c89f0) · [`007c8a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c8/007c800c.md#insn-007c8a38)
- 新版 `007c84e0`（命令位置の公開資料なし） · `007c8a48`（命令位置の公開資料なし） · `007c8a90`（命令位置の公開資料なし）

~~~diff
- 007c8488 ["INT_ADD", "register:40f0:8", ["const:7c8488:8", "const:4:8"]]
- 007c8488 ["CALL", null, ["callee:0047e91c:8"]]
+ 007c84e0 ["INT_ADD", "register:40f0:8", ["const:7c84e0:8", "const:4:8"]]
+ 007c84e0 ["CALL", null, ["callee:0047e91c:8"]]
- 007c8488 bytes 15d9f297
+ 007c84e0 bytes 0fd9f297
- 007c89f0 ["INT_ADD", "register:40f0:8", ["const:7c89f0:8", "const:4:8"]]
- 007c89f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 007c8a48 ["INT_ADD", "register:40f0:8", ["const:7c8a48:8", "const:4:8"]]
+ 007c8a48 ["CALL", null, ["callee:00c57f80:8"]]
- 007c89f0 bytes 303d1294
+ 007c8a48 bytes 4e3d1294
- 007c8a38 ["INT_ADD", "register:40f0:8", ["const:7c8a38:8", "const:4:8"]]
- 007c8a38 ["CALL", null, ["callee:00c58180:8"]]
+ 007c8a90 ["INT_ADD", "register:40f0:8", ["const:7c8a90:8", "const:4:8"]]
+ 007c8a90 ["CALL", null, ["callee:00c58180:8"]]
- 007c8a38 bytes 9e3d1294
+ 007c8a90 bytes bc3d1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3e2872d99b13b9f46e4c27527f9c26d"></a>

### [`007c8cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c8/007c8cf0.md) → [`007c8d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c8/007c8d48.md) FUN_007c8d48

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 24件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ab40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab40.md) [`0048ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab48.md)
- 新版 呼出元 2件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 24件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ab80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab80.md) [`0048ab88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab88.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.35% / 新版 87.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 9件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007c9094",
      "incomplete_value": false,
      "site": "007c9094",
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
                "const:ca5000:8"
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
      "definition_site": "007c903c",
      "incomplete_value": false,
      "site": "007c903c",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007c9098",
      "incomplete_value": false,
      "site": "007c9098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c9040",
      "incomplete_value": false,
      "site": "007c9040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c9094",
      "incomplete_value": false,
      "site": "007c9098",
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
                "const:ca5000:8"
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
      "definition_site": "007c903c",
      "incomplete_value": false,
      "site": "007c9040",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
      "007c8da4",
      "DATA",
      [
        "storage",
        "0039badc",
        null,
        "uleb128"
      ]
    ],
    [
      "007c8dc4",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ],
    [
      "007c8dec",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "007c8da4",
      "DATA",
      [
        "storage",
        "0039badc",
        null,
        "qword"
      ]
    ],
    [
      "007c8dc4",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[59]"
      ]
    ],
    [
      "007c8dec",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[59]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c8/007c8cf0.md#insn-007c8db8) · [`007c8e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c8/007c8cf0.md#insn-007c8e10) · [`007c8f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c8/007c8cf0.md#insn-007c8f58)
- 新版 `007c8e10`（命令位置の公開資料なし） · `007c8e68`（命令位置の公開資料なし） · `007c8fb0`（命令位置の公開資料なし）

~~~diff
- 007c8db8 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 007c8db8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c8db8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c8db8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c8e10 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 007c8e10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8e10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c8e10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c8db8 bytes 08e13c91
+ 007c8e10 bytes 08e10091
- 007c8e10 ["INT_ADD", "register:40f0:8", ["const:7c8e10:8", "const:4:8"]]
- 007c8e10 ["CALL", null, ["callee:0047e91c:8"]]
+ 007c8e68 ["INT_ADD", "register:40f0:8", ["const:7c8e68:8", "const:4:8"]]
+ 007c8e68 ["CALL", null, ["callee:0047e91c:8"]]
- 007c8e10 bytes b3d6f297
+ 007c8e68 bytes add6f297
- 007c8f58 ["INT_ADD", "register:40f0:8", ["const:7c8f58:8", "const:4:8"]]
- 007c8f58 ["CALL", null, ["callee:0047e91c:8"]]
+ 007c8fb0 ["INT_ADD", "register:40f0:8", ["const:7c8fb0:8", "const:4:8"]]
+ 007c8fb0 ["CALL", null, ["callee:0047e91c:8"]]
- 007c8f58 bytes 61d6f297
+ 007c8fb0 bytes 5bd6f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1989e31b747c9165174bb20f2dcb54d4"></a>

### [`007c911c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c911c.md) → [`007c9174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c9/007c9174.md) FUN_007c9174

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 22件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`007ff194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff194.md)
- 新版 呼出元 1件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) · 呼出先 22件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`007ff1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ff/007ff1ec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.59% / 新版 97.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c9508",
      "incomplete_value": false,
      "site": "007c9508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007c94b0",
      "incomplete_value": false,
      "site": "007c94b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007c95c4",
      "incomplete_value": false,
      "site": "007c95c8",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:870:8"
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
      "definition_site": "007c956c",
      "incomplete_value": false,
      "site": "007c9570",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:7a0:8"
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
    "ordinal": 58,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007c91bc",
      "incomplete_value": true,
      "site": "007c91bc",
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
      "definition_site": "007c9164",
      "incomplete_value": true,
      "site": "007c9164",
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
      "007c91b0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007c91c4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c91cc",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c91b0",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c91c4",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c91cc",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c917c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c911c.md#insn-007c917c) · [`007c9158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c911c.md#insn-007c9158) · [`007c916c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c911c.md#insn-007c916c)
- 新版 `007c91d4`（命令位置の公開資料なし） · `007c91b0`（命令位置の公開資料なし） · `007c91c4`（命令位置の公開資料なし）

~~~diff
- 007c917c ["INT_ADD", "register:40f0:8", ["const:7c917c:8", "const:4:8"]]
- 007c917c ["CALL", null, ["callee:00c586e0:8"]]
+ 007c91d4 ["INT_ADD", "register:40f0:8", ["const:7c91d4:8", "const:4:8"]]
+ 007c91d4 ["CALL", null, ["callee:00c586e0:8"]]
- 007c917c bytes 253d1294
+ 007c91d4 bytes 433d1294
- 007c9158 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
- 007c9158 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c91b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 007c91b0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c9158 bytes 00bd44f9
+ 007c91b0 bytes 003d45f9
- 007c916c ["COPY", "tmp:0:8", ["const:e58:8"]]
- 007c916c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007c916c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007c916c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007c91c4 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 007c91c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007c91c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007c91c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007c916c bytes 21603991
+ 007c91c4 bytes 21a03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b9c0e0afa0257c0a2e36985f4a7805b"></a>

### [`007c974c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c974c.md) → [`007c97a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007c9/007c97a4.md) FUN_007c97a4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 30件 [`0046da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da5c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 2件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007efd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efd00.md) · 呼出先 30件 [`0046da9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da9c.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 89.54% / 新版 89.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `store_destination` 7件, `store_value` 11件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c9a68",
      "incomplete_value": true,
      "site": "007c9a68",
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
      "definition_site": "007c9a10",
      "incomplete_value": true,
      "site": "007c9a10",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c9ad4",
      "incomplete_value": true,
      "site": "007c9ad4",
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
      "definition_site": "007c9a7c",
      "incomplete_value": true,
      "site": "007c9a7c",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007c9c20",
      "incomplete_value": true,
      "site": "007c9c20",
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
      "definition_site": "007c9bc8",
      "incomplete_value": true,
      "site": "007c9bc8",
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
      "007c97f4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007c9800",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c9808",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c97f4",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007c9800",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c9808",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c97b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c974c.md#insn-007c97b8) · [`007c9a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c974c.md#insn-007c9a68) · [`007c9a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c974c.md#insn-007c9a88)
- 新版 `007c9810`（命令位置の公開資料なし） · `007c9ac0`（命令位置の公開資料なし） · `007c9ae0`（命令位置の公開資料なし）

~~~diff
- 007c97b8 ["INT_ADD", "register:40f0:8", ["const:7c97b8:8", "const:4:8"]]
- 007c97b8 ["CALL", null, ["callee:00c586e0:8"]]
+ 007c9810 ["INT_ADD", "register:40f0:8", ["const:7c9810:8", "const:4:8"]]
+ 007c9810 ["CALL", null, ["callee:00c586e0:8"]]
- 007c97b8 bytes 963b1294
+ 007c9810 bytes b43b1294
- 007c9a68 ["INT_ADD", "register:40f0:8", ["const:7c9a68:8", "const:4:8"]]
- 007c9a68 ["CALL", null, ["callee:00c57f50:8"]]
+ 007c9ac0 ["INT_ADD", "register:40f0:8", ["const:7c9ac0:8", "const:4:8"]]
+ 007c9ac0 ["CALL", null, ["callee:00c57f50:8"]]
- 007c9a68 bytes 06391294
+ 007c9ac0 bytes 24391294
- 007c9a88 ["INT_ADD", "register:40f0:8", ["const:7c9a88:8", "const:4:8"]]
- 007c9a88 ["CALL", null, ["callee:00c57f80:8"]]
+ 007c9ae0 ["INT_ADD", "register:40f0:8", ["const:7c9ae0:8", "const:4:8"]]
+ 007c9ae0 ["CALL", null, ["callee:00c57f80:8"]]
- 007c9a88 bytes 0a391294
+ 007c9ae0 bytes 28391294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b65598a23aeff022168fedb2887281a7"></a>

### [`007ca06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca06c.md) → [`007ca0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ca/007ca0c4.md) FUN_007ca0c4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 22件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md)
- 新版 呼出元 2件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007efd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efd00.md) · 呼出先 22件 [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 90.84% / 新版 90.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_destination` 7件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ca36c",
      "incomplete_value": false,
      "site": "007ca36c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca314",
      "incomplete_value": false,
      "site": "007ca314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007ca4ac",
      "incomplete_value": false,
      "site": "007ca4ac",
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
                "const:ca5000:8"
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
      "definition_site": "007ca454",
      "incomplete_value": false,
      "site": "007ca454",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007ca4b0",
      "incomplete_value": false,
      "site": "007ca4b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca458",
      "incomplete_value": false,
      "site": "007ca458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007ca104",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007ca110",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ca118",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007ca104",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007ca110",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ca118",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca06c.md#insn-007ca0c8) · [`007ca1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca06c.md#insn-007ca1a0) · [`007ca430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca06c.md#insn-007ca430)
- 新版 `007ca120`（命令位置の公開資料なし） · `007ca1f8`（命令位置の公開資料なし） · `007ca488`（命令位置の公開資料なし）

~~~diff
- 007ca0c8 ["INT_ADD", "register:40f0:8", ["const:7ca0c8:8", "const:4:8"]]
- 007ca0c8 ["CALL", null, ["callee:00c586e0:8"]]
+ 007ca120 ["INT_ADD", "register:40f0:8", ["const:7ca120:8", "const:4:8"]]
+ 007ca120 ["CALL", null, ["callee:00c586e0:8"]]
- 007ca0c8 bytes 52391294
+ 007ca120 bytes 70391294
- 007ca1a0 ["INT_ADD", "register:40f0:8", ["const:7ca1a0:8", "const:4:8"]]
- 007ca1a0 ["CALL", null, ["callee:0047e91c:8"]]
+ 007ca1f8 ["INT_ADD", "register:40f0:8", ["const:7ca1f8:8", "const:4:8"]]
+ 007ca1f8 ["CALL", null, ["callee:0047e91c:8"]]
- 007ca1a0 bytes cfd1f297
+ 007ca1f8 bytes c9d1f297
- 007ca430 ["INT_ADD", "register:40f0:8", ["const:7ca430:8", "const:4:8"]]
- 007ca430 ["CALL", null, ["callee:00c57f20:8"]]
+ 007ca488 ["INT_ADD", "register:40f0:8", ["const:7ca488:8", "const:4:8"]]
+ 007ca488 ["CALL", null, ["callee:00c57f20:8"]]
- 007ca430 bytes 88361294
+ 007ca488 bytes a6361294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f916c01357b5ef5851fa16b666545fb4"></a>

### [`007ca528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca528.md) → [`007ca580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ca/007ca580.md) FUN_007ca580

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 20件 [`0046da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da5c.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`007ff95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff95c.md) [`007ff960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff960.md)
- 新版 呼出元 2件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007efd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efd00.md) · 呼出先 20件 [`0046da9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da9c.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`007ff9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ff/007ff9b4.md) [`007ff9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ff/007ff9b8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.60% / 新版 92.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007ca8b8",
      "incomplete_value": true,
      "site": "007ca8b8",
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
      "definition_site": "007ca860",
      "incomplete_value": true,
      "site": "007ca860",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007ca928",
      "incomplete_value": false,
      "site": "007ca928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007ca8d0",
      "incomplete_value": false,
      "site": "007ca8d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "definition_site": "007ca9a8",
      "incomplete_value": true,
      "site": "007ca9a8",
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
      "definition_site": "007ca950",
      "incomplete_value": true,
      "site": "007ca950",
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
      "007ca5c4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007ca5d0",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ca5d8",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007ca5c4",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007ca5d0",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ca5d8",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca528.md#insn-007ca588) · [`007ca808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca528.md#insn-007ca808) · [`007ca9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca528.md#insn-007ca9a8)
- 新版 `007ca5e0`（命令位置の公開資料なし） · `007ca860`（命令位置の公開資料なし） · `007caa00`（命令位置の公開資料なし）

~~~diff
- 007ca588 ["INT_ADD", "register:40f0:8", ["const:7ca588:8", "const:4:8"]]
- 007ca588 ["CALL", null, ["callee:00c586e0:8"]]
+ 007ca5e0 ["INT_ADD", "register:40f0:8", ["const:7ca5e0:8", "const:4:8"]]
+ 007ca5e0 ["CALL", null, ["callee:00c586e0:8"]]
- 007ca588 bytes 22381294
+ 007ca5e0 bytes 40381294
- 007ca808 ["INT_ADD", "register:40f0:8", ["const:7ca808:8", "const:4:8"]]
- 007ca808 ["CALL", null, ["callee:00a47014:8"]]
+ 007ca860 ["INT_ADD", "register:40f0:8", ["const:7ca860:8", "const:4:8"]]
+ 007ca860 ["CALL", null, ["callee:00a47014:8"]]
- 007ca808 bytes eef10994
+ 007ca860 bytes edf10994
- 007ca9a8 ["INT_ADD", "register:40f0:8", ["const:7ca9a8:8", "const:4:8"]]
- 007ca9a8 ["CALL", null, ["callee:00c57f50:8"]]
+ 007caa00 ["INT_ADD", "register:40f0:8", ["const:7caa00:8", "const:4:8"]]
+ 007caa00 ["CALL", null, ["callee:00c57f50:8"]]
- 007ca9a8 bytes 36351294
+ 007caa00 bytes 54351294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ff56a2b6444ac90fa3191746bbc8dee"></a>

### [`007caac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md) → [`007cab20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ca/007cab20.md) FUN_007cab20

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 30件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00727d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727d1c.md)
- 新版 呼出元 2件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007efd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efd00.md) · 呼出先 30件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00727d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727d74.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.69% / 新版 95.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007cad80",
      "incomplete_value": false,
      "site": "007cad84",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:870:8"
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
      "definition_site": "007cad28",
      "incomplete_value": false,
      "site": "007cad2c",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:7a0:8"
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
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007cb164",
      "incomplete_value": false,
      "site": "007cb168",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:870:8"
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
      "definition_site": "007cb10c",
      "incomplete_value": false,
      "site": "007cb110",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:7a0:8"
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
    "ordinal": 60,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007cb1e8",
      "incomplete_value": false,
      "site": "007cb1ec",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:870:8"
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
      "definition_site": "007cb190",
      "incomplete_value": false,
      "site": "007cb194",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:7a0:8"
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
    "ordinal": 65,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007cab88",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007cab94",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007cab9c",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007cab88",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007cab94",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007cab9c",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cab4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md#insn-007cab4c) · [`007cab8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md#insn-007cab8c) · [`007cb0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md#insn-007cb0b8)
- 新版 `007caba4`（命令位置の公開資料なし） · `007cabe4`（命令位置の公開資料なし） · `007cb110`（命令位置の公開資料なし）

~~~diff
- 007cab4c ["INT_ADD", "register:40f0:8", ["const:7cab4c:8", "const:4:8"]]
- 007cab4c ["CALL", null, ["callee:00c586e0:8"]]
+ 007caba4 ["INT_ADD", "register:40f0:8", ["const:7caba4:8", "const:4:8"]]
+ 007caba4 ["CALL", null, ["callee:00c586e0:8"]]
- 007cab4c bytes b1361294
+ 007caba4 bytes cf361294
- 007cab8c ["INT_ADD", "register:40f0:8", ["const:7cab8c:8", "const:4:8"]]
- 007cab8c ["CALL", null, ["callee:00489f8c:8"]]
+ 007cabe4 ["INT_ADD", "register:40f0:8", ["const:7cabe4:8", "const:4:8"]]
+ 007cabe4 ["CALL", null, ["callee:00489f8c:8"]]
- 007cab8c bytes f0fcf297
+ 007cabe4 bytes eafcf297
- 007cb0b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007cb0b8 ["INT_ADD", "register:40f0:8", ["const:7cb0b8:8", "const:4:8"]]
- 007cb0b8 ["CALLIND", null, ["register:0:8"]]
+ 007cb110 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007cb110 ["INT_ADD", "register:40f0:8", ["const:7cb110:8", "const:4:8"]]
+ 007cb110 ["CALLIND", null, ["register:0:8"]]
- 007cb0b8 bytes 00013fd6
+ 007cb110 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46e881a0bd6cdb24e64475d977b660a8"></a>

### [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) → [`007cb638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cb/007cb638.md) FUN_007cb638

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`009fb44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md) · 呼出先 67件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md)
- 新版 呼出元 3件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`009fb4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fb/009fb4a0.md) · 呼出先 67件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.60% / 新版 92.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 12件, `call_target` 12件, `store_value` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007cb690",
      "incomplete_value": true,
      "site": "007cb69c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7ed:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cb638",
      "incomplete_value": true,
      "site": "007cb644",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7ad:8"
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
      "definition_site": "007cbb1c",
      "incomplete_value": true,
      "site": "007cbb30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7cf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbac4",
      "incomplete_value": true,
      "site": "007cbad8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:823:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007cbc60",
      "incomplete_value": true,
      "site": "007cbc7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:564:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cbc08",
      "incomplete_value": true,
      "site": "007cbc24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:524:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007cb690",
      "READ",
      [
        "storage",
        "002b77ad",
        null,
        "string"
      ]
    ],
    [
      "007cb6b0",
      "PARAM",
      [
        "storage",
        "002a151b",
        null,
        "string"
      ]
    ],
    [
      "007cb7a0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "007cb690",
      "READ",
      [
        "storage",
        "002b77ed",
        null,
        "string"
      ]
    ],
    [
      "007cb6b0",
      "PARAM",
      [
        "storage",
        "002a14ce",
        null,
        "string"
      ]
    ],
    [
      "007cb7a0",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cb660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md#insn-007cb660) · [`007cb778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md#insn-007cb778) · [`007cbd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md#insn-007cbd00)
- 新版 `007cb6b8`（命令位置の公開資料なし） · `007cb7d0`（命令位置の公開資料なし） · `007cbd58`（命令位置の公開資料なし）

~~~diff
- 007cb660 ["INT_ADD", "register:40f0:8", ["const:7cb660:8", "const:4:8"]]
- 007cb660 ["CALL", null, ["callee:00c58040:8"]]
+ 007cb6b8 ["INT_ADD", "register:40f0:8", ["const:7cb6b8:8", "const:4:8"]]
+ 007cb6b8 ["CALL", null, ["callee:00c58040:8"]]
- 007cb660 bytes 44321294
+ 007cb6b8 bytes 62321294
- 007cb778 ["INT_ADD", "register:40f0:8", ["const:7cb778:8", "const:4:8"]]
- 007cb778 ["CALL", null, ["callee:00c586e0:8"]]
+ 007cb7d0 ["INT_ADD", "register:40f0:8", ["const:7cb7d0:8", "const:4:8"]]
+ 007cb7d0 ["CALL", null, ["callee:00c586e0:8"]]
- 007cb778 bytes a6331294
+ 007cb7d0 bytes c4331294
- 007cbd00 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 007cbd00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007cbd00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007cbd00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007cbd58 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 007cbd58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007cbd58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007cbd58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007cbd00 bytes 00e03c91
+ 007cbd58 bytes 00e00091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ffe3c60fe9eda35c974517156a4cd59"></a>

### [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) → [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) FUN_007ccf44

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 432件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 432件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0043e868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e868.md) [`00440b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440b40.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.18% / 新版 96.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 147件, `call_target` 93件, `store_destination` 14件, `store_value` 78件

アドレスに依存する影響 `branch_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007cd49c",
      "incomplete_value": true,
      "site": "007cd49c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:49d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cd444",
      "incomplete_value": true,
      "site": "007cd444",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4ea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007cd4a0",
      "incomplete_value": true,
      "site": "007cd4a0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007cd448",
      "incomplete_value": true,
      "site": "007cd448",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 64,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007cd57c",
      "incomplete_value": false,
      "site": "007cd57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007cd524",
      "incomplete_value": false,
      "site": "007cd524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:330:8"
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
      "007ccffc",
      "DATA",
      [
        "storage",
        "003c80e4",
        "fde_003c80e4",
        "dword"
      ]
    ],
    [
      "007cd00c",
      "DATA",
      [
        "storage",
        "003c80d8",
        null,
        "uleb128"
      ]
    ],
    [
      "007cd014",
      "DATA",
      [
        "storage",
        "003c80d8",
        null,
        "uleb128"
      ]
    ]
  ],
  "added": [
    [
      "007ccffc",
      "DATA",
      [
        "storage",
        "003c80e4",
        null,
        "byte[11]"
      ]
    ],
    [
      "007cd00c",
      "DATA",
      [
        "storage",
        "003c80d8",
        null,
        "dword"
      ]
    ],
    [
      "007cd014",
      "DATA",
      [
        "storage",
        "003c80d8",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cd3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/assembly/007cc/007cceec-007cceec-007d834c.md#insn-007cd3ec) · [`007cd51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/assembly/007cc/007cceec-007cceec-007d834c.md#insn-007cd51c) · [`007cd6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/assembly/007cc/007cceec-007cceec-007d834c.md#insn-007cd6a4)
- 新版 `007cd444`（命令位置の公開資料なし） · `007cd574`（命令位置の公開資料なし） · `007cd6fc`（命令位置の公開資料なし）

~~~diff
- 007cd3ec ["INT_ADD", "register:40f0:8", ["const:7cd3ec:8", "const:4:8"]]
- 007cd3ec ["CALL", null, ["callee:00acebcc:8"]]
+ 007cd444 ["INT_ADD", "register:40f0:8", ["const:7cd444:8", "const:4:8"]]
+ 007cd444 ["CALL", null, ["callee:00acebcc:8"]]
- 007cd3ec bytes dc050c94
+ 007cd444 bytes e2050c94
- 007cd51c ["COPY", "tmp:0:8", ["const:330:8"]]
- 007cd51c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007cd51c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007cd51c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007cd574 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 007cd574 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007cd574 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007cd574 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007cd51c bytes 08c10c91
+ 007cd574 bytes 08011091
- 007cd6a4 ["INT_ADD", "register:40f0:8", ["const:7cd6a4:8", "const:4:8"]]
- 007cd6a4 ["CALL", null, ["callee:0052dd40:8"]]
+ 007cd6fc ["INT_ADD", "register:40f0:8", ["const:7cd6fc:8", "const:4:8"]]
+ 007cd6fc ["CALL", null, ["callee:0052dd40:8"]]
- 007cd6a4 bytes 9781f597
+ 007cd6fc bytes 9181f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6106f763f084985bce91f30c200bba12"></a>

### [`007dd7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd7a0.md) → [`007dd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dd/007dd7f8.md) FUN_007dd7f8

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 31件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 31件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.65% / 新版 89.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 29件, `store_destination` 14件, `store_value` 11件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007dd930",
      "incomplete_value": true,
      "site": "007dd940",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3db:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007dd8d8",
      "incomplete_value": true,
      "site": "007dd8e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:428:8"
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
      "definition_site": "007dd934",
      "incomplete_value": true,
      "site": "007dd944",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007dd8dc",
      "incomplete_value": true,
      "site": "007dd8ec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007dd938",
      "incomplete_value": true,
      "site": "007dd948",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "007dd8e0",
      "incomplete_value": true,
      "site": "007dd8f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "007dd848",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007dd854",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007dd85c",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007dd848",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007dd854",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007dd85c",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007dd80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd7a0.md#insn-007dd80c) · [`007dd894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd7a0.md#insn-007dd894) · [`007dd930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd7a0.md#insn-007dd930)
- 新版 `007dd864`（命令位置の公開資料なし） · `007dd8ec`（命令位置の公開資料なし） · `007dd988`（命令位置の公開資料なし）

~~~diff
- 007dd80c ["INT_ADD", "register:40f0:8", ["const:7dd80c:8", "const:4:8"]]
- 007dd80c ["CALL", null, ["callee:00c586e0:8"]]
+ 007dd864 ["INT_ADD", "register:40f0:8", ["const:7dd864:8", "const:4:8"]]
+ 007dd864 ["CALL", null, ["callee:00c586e0:8"]]
- 007dd80c bytes 81eb1194
+ 007dd864 bytes 9feb1194
- 007dd894 ["INT_ADD", "register:40f0:8", ["const:7dd894:8", "const:4:8"]]
- 007dd894 ["CALL", null, ["callee:00800244:8"]]
+ 007dd8ec ["INT_ADD", "register:40f0:8", ["const:7dd8ec:8", "const:4:8"]]
+ 007dd8ec ["CALL", null, ["callee:00800244:8"]]
- 007dd894 bytes 568a0094
+ 007dd8ec bytes 568a0094
- 007dd930 ["INT_ADD", "register:40f0:8", ["const:7dd930:8", "const:4:8"]]
- 007dd930 ["CALL", null, ["callee:0047e91c:8"]]
+ 007dd988 ["INT_ADD", "register:40f0:8", ["const:7dd988:8", "const:4:8"]]
+ 007dd988 ["CALL", null, ["callee:0047e91c:8"]]
- 007dd930 bytes eb83f297
+ 007dd988 bytes e583f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e9aecc5a8069967e1e878f7f366eaea"></a>

### [`007ef684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef684.md) → [`007ef6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007ef6dc.md) FUN_007ef6dc

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) · 呼出先 16件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0067674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067674c.md) [`007bbd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbd48.md) [`007de674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de674.md) [`008001cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001cc.md)
- 新版 呼出元 2件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`007cb638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cb/007cb638.md) · 呼出先 16件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0067678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/0067678c.md) [`007bbda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbda0.md) [`007de6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007de/007de6cc.md) [`00800224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800224.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.60% / 新版 99.60%

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
      "site": "007ef9d8",
      "value": [
        "leaf",
        "ram:a65e5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ef980",
      "value": [
        "leaf",
        "ram:a65dec:8"
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
      "007ef930",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ],
    [
      "007ef984",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ],
    [
      "007ef9d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ],
  "added": [
    [
      "007ef930",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[59]"
      ]
    ],
    [
      "007ef984",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[59]"
      ]
    ],
    [
      "007ef9d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ef980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef684.md#insn-007ef980) · [`007ef6b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef684.md#insn-007ef6b4) · [`007ef718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef684.md#insn-007ef718)
- 新版 `007ef9d8`（命令位置の公開資料なし） · `007ef70c`（命令位置の公開資料なし） · `007ef770`（命令位置の公開資料なし）

~~~diff
- 007ef980 ["INT_ADD", "register:40f0:8", ["const:7ef980:8", "const:4:8"]]
- 007ef980 ["CALL", null, ["ram:a65dec:8"]]
+ 007ef9d8 ["INT_ADD", "register:40f0:8", ["const:7ef9d8:8", "const:4:8"]]
+ 007ef9d8 ["CALL", null, ["ram:a65e5c:8"]]
- 007ef980 bytes 1bd90994
+ 007ef9d8 bytes 21d90994
- 007ef6b4 ["INT_ADD", "register:40f0:8", ["const:7ef6b4:8", "const:4:8"]]
- 007ef6b4 ["CALL", null, ["callee:00802d00:8"]]
+ 007ef70c ["INT_ADD", "register:40f0:8", ["const:7ef70c:8", "const:4:8"]]
+ 007ef70c ["CALL", null, ["callee:00802d00:8"]]
- 007ef6b4 bytes 7d4d0094
+ 007ef70c bytes 7d4d0094
- 007ef718 ["INT_ADD", "register:40f0:8", ["const:7ef718:8", "const:4:8"]]
- 007ef718 ["CALL", null, ["callee:00c57f60:8"]]
+ 007ef770 ["INT_ADD", "register:40f0:8", ["const:7ef770:8", "const:4:8"]]
+ 007ef770 ["CALL", null, ["callee:00c57f60:8"]]
- 007ef718 bytes dea11194
+ 007ef770 bytes fca11194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01cb2d0a0925aab965440516499becfc"></a>

### [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) → [`007efd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efd00.md) FUN_007efd00

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007fceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fceec.md) [`007fcfdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcfdc.md) · 呼出先 33件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`005e48ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e48ac.md) [`005e4b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4b88.md) [`005e4ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4ee4.md) [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md)
- 新版 呼出元 2件 [`007fcf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcf44.md) [`007fd034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd034.md) · 呼出先 33件 [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`005e48ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e48ec.md) [`005e4bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4bc8.md) [`005e4f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4f24.md) [`005e81d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e8/005e81d8.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.75% / 新版 91.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007efdd4",
      "incomplete_value": false,
      "site": "007efddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007efd7c",
      "incomplete_value": false,
      "site": "007efd84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:af4:8"
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
      "definition_site": "007efdfc",
      "incomplete_value": false,
      "site": "007efe08",
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
            "const:5ae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007efda4",
      "incomplete_value": false,
      "site": "007efdb0",
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
            "const:56e:8"
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
      "definition_site": "007efe34",
      "incomplete_value": false,
      "site": "007efe38",
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
            "const:e79:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007efddc",
      "incomplete_value": false,
      "site": "007efde0",
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
            "const:e48:8"
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
      "007efd48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007dd364"
      ]
    ],
    [
      "007efd70",
      "DATA",
      [
        "storage",
        "003870a0",
        null,
        "byte[23]"
      ]
    ],
    [
      "007efda0",
      "DATA",
      [
        "storage",
        "003870a0",
        null,
        "byte[23]"
      ]
    ]
  ],
  "added": [
    [
      "007efd48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007dd3bc"
      ]
    ],
    [
      "007efd70",
      "DATA",
      [
        "storage",
        "003870a0",
        "fde_003870a0",
        "dword"
      ]
    ],
    [
      "007efda0",
      "DATA",
      [
        "storage",
        "003870a0",
        "fde_003870a0",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007efcf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md#insn-007efcf0) · [`007efd2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md#insn-007efd2c) · [`007efddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md#insn-007efddc)
- 新版 `007efd48`（命令位置の公開資料なし） · `007efd84`（命令位置の公開資料なし） · `007efe34`（命令位置の公開資料なし）

~~~diff
- 007efcf0 ["INT_ADD", "register:40f0:8", ["const:7efcf0:8", "const:4:8"]]
- 007efcf0 ["CALL", null, ["ram:7dd364:8"]]
+ 007efd48 ["INT_ADD", "register:40f0:8", ["const:7efd48:8", "const:4:8"]]
+ 007efd48 ["CALL", null, ["ram:7dd3bc:8"]]
- 007efcf0 bytes 9db5ff97
+ 007efd48 bytes 9db5ff97
- 007efd2c ["INT_ADD", "register:40f0:8", ["const:7efd2c:8", "const:4:8"]]
- 007efd2c ["CALL", null, ["callee:00802f38:8"]]
+ 007efd84 ["INT_ADD", "register:40f0:8", ["const:7efd84:8", "const:4:8"]]
+ 007efd84 ["CALL", null, ["callee:00802f38:8"]]
- 007efd2c bytes 6d4c0094
+ 007efd84 bytes 6d4c0094
- 007efddc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 007efddc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007efddc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007efddc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007efe34 ["COPY", "tmp:0:8", ["const:e79:8"]]
+ 007efe34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007efe34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007efe34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007efddc bytes 08213991
+ 007efe34 bytes 08e53991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a30dffdee40309b0ea16aa4691bf1830"></a>

### [`007f0574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0574.md) → [`007f05cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f05cc.md) FUN_007f05cc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007caac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md) · 呼出先 7件 [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00a46784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46784.md) [`00a46cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46cc8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`007cab20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ca/007cab20.md) · 呼出先 7件 [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00a467d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a467d8.md) [`00a46d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a46d1c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.29% / 新版 95.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f0680",
      "incomplete_value": false,
      "site": "007f0684",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:870:8"
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
      "definition_site": "007f0628",
      "incomplete_value": false,
      "site": "007f062c",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:7a0:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f0644",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "007f0658",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ],
    [
      "007f0684",
      "DATA",
      [
        "storage",
        "00c8b7b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f0644",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "007f0658",
      "DATA",
      [
        "storage",
        "00c8b828",
        null,
        "undefined *"
      ]
    ],
    [
      "007f0684",
      "DATA",
      [
        "storage",
        "00c8b880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f0684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0574.md#insn-007f0684) · [`007f05c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0574.md#insn-007f05c8) · [`007f05dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0574.md#insn-007f05dc)
- 新版 `007f06dc`（命令位置の公開資料なし） · `007f0620`（命令位置の公開資料なし） · `007f0634`（命令位置の公開資料なし）

~~~diff
- 007f0684 ["COPY", "register:0:8", ["register:4040:8"]]
- 007f0684 ["INT_ADD", "register:40f0:8", ["const:7f0684:8", "const:4:8"]]
- 007f0684 ["CALLIND", null, ["register:0:8"]]
+ 007f06dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 007f06dc ["INT_ADD", "register:40f0:8", ["const:7f06dc:8", "const:4:8"]]
+ 007f06dc ["CALLIND", null, ["register:0:8"]]
- 007f0684 bytes 00013fd6
+ 007f06dc bytes 00013fd6
- 007f05c8 ["INT_ADD", "register:40f0:8", ["const:7f05c8:8", "const:4:8"]]
- 007f05c8 ["CALL", null, ["callee:00a46d1c:8"]]
+ 007f0620 ["INT_ADD", "register:40f0:8", ["const:7f0620:8", "const:4:8"]]
+ 007f0620 ["CALL", null, ["callee:00a46d1c:8"]]
- 007f05c8 bytes c0590994
+ 007f0620 bytes bf590994
- 007f05dc ["INT_ADD", "register:40f0:8", ["const:7f05dc:8", "const:4:8"]]
- 007f05dc ["CALL", null, ["callee:00a467d8:8"]]
+ 007f0634 ["INT_ADD", "register:40f0:8", ["const:7f0634:8", "const:4:8"]]
+ 007f0634 ["CALL", null, ["callee:00a467d8:8"]]
- 007f05dc bytes 6a580994
+ 007f0634 bytes 69580994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19dcdbe2b2a3fe81c006cbe28b74c189"></a>

### [`007f06f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f06f4.md) → [`007f074c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f074c.md) FUN_007f074c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f0c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c74.md) · 呼出先 10件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00672748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672748.md) [`0067e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e5e8.md) [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md)
- 新版 呼出元 1件 [`007f0ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f0ccc.md) · 呼出先 10件 [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) [`00672788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00672/00672788.md) [`0067e628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e628.md) [`00682364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.30% / 新版 98.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f0768",
      "incomplete_value": false,
      "site": "007f076c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f0710",
      "incomplete_value": false,
      "site": "007f0714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "definition_site": "007f0c48",
      "incomplete_value": false,
      "site": "007f0c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f0bf0",
      "incomplete_value": false,
      "site": "007f0bf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:330:8"
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
      "definition_site": "007f0c84",
      "incomplete_value": false,
      "site": "007f0c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f0c2c",
      "incomplete_value": false,
      "site": "007f0c30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      "007f076c",
      "DATA",
      [
        "storage",
        "00c7ab98",
        null,
        "pointer"
      ]
    ],
    [
      "007f0c4c",
      "DATA",
      [
        "storage",
        "00c78330",
        null,
        "pointer"
      ]
    ],
    [
      "007f0c88",
      "DATA",
      [
        "storage",
        "00c74810",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007f076c",
      "DATA",
      [
        "storage",
        "00c7ac68",
        null,
        "pointer"
      ]
    ],
    [
      "007f0c4c",
      "DATA",
      [
        "storage",
        "00c78400",
        null,
        "pointer"
      ]
    ],
    [
      "007f0c88",
      "DATA",
      [
        "storage",
        "00c748e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f0710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f06f4.md#insn-007f0710) · [`007f0724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f06f4.md#insn-007f0724) · [`007f0738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f06f4.md#insn-007f0738)
- 新版 `007f0768`（命令位置の公開資料なし） · `007f077c`（命令位置の公開資料なし） · `007f0790`（命令位置の公開資料なし）

~~~diff
- 007f0710 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 007f0710 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f0710 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f0710 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f0768 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 007f0768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f0768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f0768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f0710 bytes 08612e91
+ 007f0768 bytes 08a13191
- 007f0724 ["INT_ADD", "register:40f0:8", ["const:7f0724:8", "const:4:8"]]
- 007f0724 ["CALL", null, ["callee:00c53da0:8"]]
+ 007f077c ["INT_ADD", "register:40f0:8", ["const:7f077c:8", "const:4:8"]]
+ 007f077c ["CALL", null, ["callee:00c53da0:8"]]
- 007f0724 bytes 778d1194
+ 007f077c bytes 898d1194
- 007f0738 ["COPY", "register:0:8", ["register:4040:8"]]
- 007f0738 ["INT_ADD", "register:40f0:8", ["const:7f0738:8", "const:4:8"]]
- 007f0738 ["CALLIND", null, ["register:0:8"]]
+ 007f0790 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007f0790 ["INT_ADD", "register:40f0:8", ["const:7f0790:8", "const:4:8"]]
+ 007f0790 ["CALLIND", null, ["register:0:8"]]
- 007f0738 bytes 00013fd6
+ 007f0790 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-467221c112b6f7d7eda87f4a3acc0001"></a>

### [`007f0dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0dd4.md) → [`007f0e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f0e2c.md) FUN_007f0e2c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007f0c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c98.md) [`007f0dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0dd4.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 2件 [`007f0cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f0cf0.md) [`007f0e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f0e2c.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.83% / 新版 98.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f0f90",
      "incomplete_value": false,
      "site": "007f0f98",
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
            "const:f93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f0f38",
      "incomplete_value": false,
      "site": "007f0f40",
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
            "const:f53:8"
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
      "definition_site": "007f0fb4",
      "incomplete_value": false,
      "site": "007f0fc0",
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
            "const:f29:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f0f5c",
      "incomplete_value": false,
      "site": "007f0f68",
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
            "const:ee9:8"
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
      "definition_site": "007f10e8",
      "incomplete_value": false,
      "site": "007f10f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:e27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f1090",
      "incomplete_value": false,
      "site": "007f1098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:de7:8"
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
      "007f0f90",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "007f0fb4",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "007f10e8",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007f0f90",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "007f0fb4",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "007f10e8",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f0f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0dd4.md#insn-007f0f40) · [`007f0f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0dd4.md#insn-007f0f68) · [`007f1098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0dd4.md#insn-007f1098)
- 新版 `007f0f98`（命令位置の公開資料なし） · `007f0fc0`（命令位置の公開資料なし） · `007f10f0`（命令位置の公開資料なし）

~~~diff
- 007f0f40 ["INT_ADD", "register:40f0:8", ["const:7f0f40:8", "const:4:8"]]
- 007f0f40 ["CALL", null, ["callee:00441ed4:8"]]
+ 007f0f98 ["INT_ADD", "register:40f0:8", ["const:7f0f98:8", "const:4:8"]]
+ 007f0f98 ["CALL", null, ["callee:00441ed4:8"]]
- 007f0f40 bytes d543f197
+ 007f0f98 bytes cf43f197
- 007f0f68 ["INT_ADD", "register:40f0:8", ["const:7f0f68:8", "const:4:8"]]
- 007f0f68 ["CALL", null, ["callee:00442834:8"]]
+ 007f0fc0 ["INT_ADD", "register:40f0:8", ["const:7f0fc0:8", "const:4:8"]]
+ 007f0fc0 ["CALL", null, ["callee:00442834:8"]]
- 007f0f68 bytes 2346f197
+ 007f0fc0 bytes 1d46f197
- 007f1098 ["INT_ADD", "register:40f0:8", ["const:7f1098:8", "const:4:8"]]
- 007f1098 ["CALL", null, ["callee:00441ed4:8"]]
+ 007f10f0 ["INT_ADD", "register:40f0:8", ["const:7f10f0:8", "const:4:8"]]
+ 007f10f0 ["CALL", null, ["callee:00441ed4:8"]]
- 007f1098 bytes 7f43f197
+ 007f10f0 bytes 7943f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1122b1792ee2fe5654db700db31734c2"></a>

### [`007f1e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1e90.md) → [`007f1ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1ee8.md) FUN_007f1ee8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007f1894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1894.md) [`009012d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009012d8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`007f18ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f18ec.md) [`0090132c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00901/0090132c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "007f1ef4",
      "incomplete_value": false,
      "site": "007f1ef8",
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
      "definition_site": "007f1e9c",
      "incomplete_value": false,
      "site": "007f1ea0",
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
      "007f1ef4",
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
      "007f1ef4",
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

- 旧版 [`007f1ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1e90.md#insn-007f1ea0) · [`007f1e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1e90.md#insn-007f1e9c)
- 新版 `007f1ef8`（命令位置の公開資料なし） · `007f1ef4`（命令位置の公開資料なし）

~~~diff
- 007f1ea0 ["INT_ADD", "register:40f0:8", ["const:7f1ea0:8", "const:4:8"]]
- 007f1ea0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 007f1ef8 ["INT_ADD", "register:40f0:8", ["const:7f1ef8:8", "const:4:8"]]
+ 007f1ef8 ["CALL", null, ["callee:0043b7b8:8"]]
- 007f1ea0 bytes 3626f197
+ 007f1ef8 bytes 3026f197
- 007f1e9c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 007f1e9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007f1e9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007f1e9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007f1ef4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 007f1ef4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007f1ef4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007f1ef4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007f1e9c bytes 00303d91
+ 007f1ef4 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe7057dd3a3cbd0cc5fecf9249d66291"></a>

### [`007f1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ea4.md) → [`007f1efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1efc.md) FUN_007f1efc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`0080eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080eef0.md) [`00810888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810888.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 3件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`0080ef48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080e/0080ef48.md) [`008108e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00810/008108e0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "007f1f08",
      "incomplete_value": false,
      "site": "007f1f0c",
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
      "definition_site": "007f1eb0",
      "incomplete_value": false,
      "site": "007f1eb4",
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
      "007f1f08",
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
      "007f1f08",
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

- 旧版 [`007f1eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ea4.md#insn-007f1eb4) · [`007f1eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ea4.md#insn-007f1eb0)
- 新版 `007f1f0c`（命令位置の公開資料なし） · `007f1f08`（命令位置の公開資料なし）

~~~diff
- 007f1eb4 ["INT_ADD", "register:40f0:8", ["const:7f1eb4:8", "const:4:8"]]
- 007f1eb4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 007f1f0c ["INT_ADD", "register:40f0:8", ["const:7f1f0c:8", "const:4:8"]]
+ 007f1f0c ["CALL", null, ["callee:0043b7b8:8"]]
- 007f1eb4 bytes 3126f197
+ 007f1f0c bytes 2b26f197
- 007f1eb0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 007f1eb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007f1eb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007f1eb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007f1f08 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 007f1f08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007f1f08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007f1f08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007f1eb0 bytes 00303d91
+ 007f1f08 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad9a59fb310f94887967fc6c5568425a"></a>

### [`007f1ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ed0.md) → [`007f1f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1f28.md) FUN_007f1f28

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f1f3c",
      "incomplete_value": false,
      "site": "007f1f40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f1ee4",
      "incomplete_value": false,
      "site": "007f1ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
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
      "007f1f40",
      "DATA",
      [
        "storage",
        "00c7abb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f1f40",
      "DATA",
      [
        "storage",
        "00c7ac88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f1edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ed0.md#insn-007f1edc) · [`007f1ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ed0.md#insn-007f1ee4)
- 新版 `007f1f34`（命令位置の公開資料なし） · `007f1f3c`（命令位置の公開資料なし）

~~~diff
- 007f1edc ["INT_ADD", "register:40f0:8", ["const:7f1edc:8", "const:4:8"]]
- 007f1edc ["CALL", null, ["callee:00c57f60:8"]]
+ 007f1f34 ["INT_ADD", "register:40f0:8", ["const:7f1f34:8", "const:4:8"]]
+ 007f1f34 ["CALL", null, ["callee:00c57f60:8"]]
- 007f1edc bytes ed971194
+ 007f1f34 bytes 0b981194
- 007f1ee4 ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 007f1ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f1ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f1ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f1f3c ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 007f1f3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f1f3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f1f3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f1ee4 bytes 08e12e91
+ 007f1f3c bytes 08213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-716a85483bcc8efeee7acb299e8c1f50"></a>

### [`007f1f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1f0c.md) → [`007f1f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1f64.md) FUN_007f1f64

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043e868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e868.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.38% / 新版 94.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f2050",
      "incomplete_value": true,
      "site": "007f2064",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f1ff8",
      "incomplete_value": true,
      "site": "007f200c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f2b:8"
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
      "definition_site": "007f2068",
      "incomplete_value": true,
      "site": "007f2068",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007f2010",
      "incomplete_value": true,
      "site": "007f2010",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f2130",
      "incomplete_value": false,
      "site": "007f2130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f20d8",
      "incomplete_value": false,
      "site": "007f20d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "007f1f9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f1fb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f2000",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "007f1f9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f1fb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f2000",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[59]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f1f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1f0c.md#insn-007f1f44) · [`007f1f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1f0c.md#insn-007f1f60) · [`007f1f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1f0c.md#insn-007f1f9c)
- 新版 `007f1f9c`（命令位置の公開資料なし） · `007f1fb8`（命令位置の公開資料なし） · `007f1ff4`（命令位置の公開資料なし）

~~~diff
- 007f1f44 ["INT_ADD", "register:40f0:8", ["const:7f1f44:8", "const:4:8"]]
- 007f1f44 ["CALL", null, ["ram:47acf4:8"]]
+ 007f1f9c ["INT_ADD", "register:40f0:8", ["const:7f1f9c:8", "const:4:8"]]
+ 007f1f9c ["CALL", null, ["ram:47ad34:8"]]
- 007f1f44 bytes 6c23f297
+ 007f1f9c bytes 6623f297
- 007f1f60 ["INT_ADD", "register:40f0:8", ["const:7f1f60:8", "const:4:8"]]
- 007f1f60 ["CALL", null, ["ram:47acf4:8"]]
+ 007f1fb8 ["INT_ADD", "register:40f0:8", ["const:7f1fb8:8", "const:4:8"]]
+ 007f1fb8 ["CALL", null, ["ram:47ad34:8"]]
- 007f1f60 bytes 6523f297
+ 007f1fb8 bytes 5f23f297
- 007f1f9c ["INT_ADD", "register:40f0:8", ["const:7f1f9c:8", "const:4:8"]]
- 007f1f9c ["CALL", null, ["callee:00851550:8"]]
+ 007f1ff4 ["INT_ADD", "register:40f0:8", ["const:7f1ff4:8", "const:4:8"]]
+ 007f1ff4 ["CALL", null, ["callee:00851550:8"]]
- 007f1f9c bytes 577d0194
+ 007f1ff4 bytes 577d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0e222af083ef0e53efd0160c342fb6f"></a>

### [`007f2338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2338.md) → [`007f2390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f2390.md) FUN_007f2390

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f23a4",
      "incomplete_value": false,
      "site": "007f23a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f234c",
      "incomplete_value": false,
      "site": "007f2350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "007f23a8",
      "DATA",
      [
        "storage",
        "00c7ac28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f23a8",
      "DATA",
      [
        "storage",
        "00c7acf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2338.md#insn-007f2344) · [`007f234c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2338.md#insn-007f234c)
- 新版 `007f239c`（命令位置の公開資料なし） · `007f23a4`（命令位置の公開資料なし）

~~~diff
- 007f2344 ["INT_ADD", "register:40f0:8", ["const:7f2344:8", "const:4:8"]]
- 007f2344 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f239c ["INT_ADD", "register:40f0:8", ["const:7f239c:8", "const:4:8"]]
+ 007f239c ["CALL", null, ["callee:00c57f60:8"]]
- 007f2344 bytes d3961194
+ 007f239c bytes f1961194
- 007f234c ["COPY", "tmp:0:8", ["const:c28:8"]]
- 007f234c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f234c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f234c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f23a4 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 007f23a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f23a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f23a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f234c bytes 08a13091
+ 007f23a4 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f22558dd0e30fbbfb579235b963f68e8"></a>

### [`007f235c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f235c.md) → [`007f23b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f23b4.md) FUN_007f23b4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f23b8",
      "incomplete_value": false,
      "site": "007f23bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f2360",
      "incomplete_value": false,
      "site": "007f2364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007f23bc",
      "DATA",
      [
        "storage",
        "00c7ac28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f23bc",
      "DATA",
      [
        "storage",
        "00c7acf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f235c.md#insn-007f2360)
- 新版 `007f23b8`（命令位置の公開資料なし）

~~~diff
- 007f2360 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 007f2360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f23b8 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 007f23b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f23b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f23b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2360 bytes 08a13091
+ 007f23b8 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b0770ed47e665839a137605e9f85a77"></a>

### [`007f2374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2374.md) → [`007f23cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f23cc.md) FUN_007f23cc

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.16% / 新版 94.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f2494",
      "incomplete_value": true,
      "site": "007f24a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:383:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f243c",
      "incomplete_value": true,
      "site": "007f244c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3d0:8"
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
      "definition_site": "007f24a8",
      "incomplete_value": true,
      "site": "007f24a8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007f2450",
      "incomplete_value": true,
      "site": "007f2450",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f2514",
      "incomplete_value": true,
      "site": "007f2524",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:383:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f24bc",
      "incomplete_value": true,
      "site": "007f24cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3d0:8"
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
      "007f2418",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ],
    [
      "007f2474",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f2494",
      "READ",
      [
        "storage",
        "002a03d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f2418",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[59]"
      ]
    ],
    [
      "007f2474",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f2494",
      "READ",
      [
        "storage",
        "002a0383",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f23c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2374.md#insn-007f23c4) · [`007f241c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2374.md#insn-007f241c) · [`007f2478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2374.md#insn-007f2478)
- 新版 `007f241c`（命令位置の公開資料なし） · `007f2474`（命令位置の公開資料なし） · `007f24d0`（命令位置の公開資料なし）

~~~diff
- 007f23c4 ["INT_ADD", "register:40f0:8", ["const:7f23c4:8", "const:4:8"]]
- 007f23c4 ["CALL", null, ["callee:00800224:8"]]
+ 007f241c ["INT_ADD", "register:40f0:8", ["const:7f241c:8", "const:4:8"]]
+ 007f241c ["CALL", null, ["callee:00800224:8"]]
- 007f23c4 bytes 82370094
+ 007f241c bytes 82370094
- 007f241c ["INT_ADD", "register:40f0:8", ["const:7f241c:8", "const:4:8"]]
- 007f241c ["CALL", null, ["ram:47acf4:8"]]
+ 007f2474 ["INT_ADD", "register:40f0:8", ["const:7f2474:8", "const:4:8"]]
+ 007f2474 ["CALL", null, ["ram:47ad34:8"]]
- 007f241c bytes 3622f297
+ 007f2474 bytes 3022f297
- 007f2478 ["INT_ADD", "register:40f0:8", ["const:7f2478:8", "const:4:8"]]
- 007f2478 ["CALL", null, ["callee:00597668:8"]]
+ 007f24d0 ["INT_ADD", "register:40f0:8", ["const:7f24d0:8", "const:4:8"]]
+ 007f24d0 ["CALL", null, ["callee:00597668:8"]]
- 007f2478 bytes 6c94f697
+ 007f24d0 bytes 6694f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-652807b8506b7f9ed515bb9e80c607a6"></a>

### [`007f2930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2930.md) → [`007f2988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f2988.md) FUN_007f2988

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f299c",
      "incomplete_value": false,
      "site": "007f29a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f2944",
      "incomplete_value": false,
      "site": "007f2948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
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
      "007f29a0",
      "DATA",
      [
        "storage",
        "00c7acb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f29a0",
      "DATA",
      [
        "storage",
        "00c7ad88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f293c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2930.md#insn-007f293c) · [`007f2944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2930.md#insn-007f2944)
- 新版 `007f2994`（命令位置の公開資料なし） · `007f299c`（命令位置の公開資料なし）

~~~diff
- 007f293c ["INT_ADD", "register:40f0:8", ["const:7f293c:8", "const:4:8"]]
- 007f293c ["CALL", null, ["callee:00c57f60:8"]]
+ 007f2994 ["INT_ADD", "register:40f0:8", ["const:7f2994:8", "const:4:8"]]
+ 007f2994 ["CALL", null, ["callee:00c57f60:8"]]
- 007f293c bytes 55951194
+ 007f2994 bytes 73951194
- 007f2944 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 007f2944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f299c ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 007f299c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f299c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f299c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2944 bytes 08e13291
+ 007f299c bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97dd2ecc99a4cab42d09ee10b86057d5"></a>

### [`007f296c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f296c.md) → [`007f29c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f29c4.md) FUN_007f29c4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`007df024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df024.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`007df07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df07c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f29e4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f298c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f29f0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2998",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f29e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f29f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f29e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f29f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f298c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f296c.md#insn-007f298c) · [`007f2998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f296c.md#insn-007f2998) · [`007f29ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f296c.md#insn-007f29ac)
- 新版 `007f29e4`（命令位置の公開資料なし） · `007f29f0`（命令位置の公開資料なし） · `007f2a04`（命令位置の公開資料なし）

~~~diff
- 007f298c ["INT_ADD", "register:40f0:8", ["const:7f298c:8", "const:4:8"]]
- 007f298c ["CALL", null, ["ram:47acf4:8"]]
+ 007f29e4 ["INT_ADD", "register:40f0:8", ["const:7f29e4:8", "const:4:8"]]
+ 007f29e4 ["CALL", null, ["ram:47ad34:8"]]
- 007f298c bytes da20f297
+ 007f29e4 bytes d420f297
- 007f2998 ["INT_ADD", "register:40f0:8", ["const:7f2998:8", "const:4:8"]]
- 007f2998 ["CALL", null, ["ram:47acf4:8"]]
+ 007f29f0 ["INT_ADD", "register:40f0:8", ["const:7f29f0:8", "const:4:8"]]
+ 007f29f0 ["CALL", null, ["ram:47ad34:8"]]
- 007f2998 bytes d720f297
+ 007f29f0 bytes d120f297
- 007f29ac ["INT_ADD", "register:40f0:8", ["const:7f29ac:8", "const:4:8"]]
- 007f29ac ["CALL", null, ["callee:00851550:8"]]
+ 007f2a04 ["INT_ADD", "register:40f0:8", ["const:7f2a04:8", "const:4:8"]]
+ 007f2a04 ["CALL", null, ["callee:00851550:8"]]
- 007f29ac bytes d37a0194
+ 007f2a04 bytes d37a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d25127ecbec3d106e201d128397a240d"></a>

### [`007f2a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2a10.md) → [`007f2a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f2a68.md) FUN_007f2a68

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f2a8c",
      "incomplete_value": false,
      "site": "007f2a8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f2a34",
      "incomplete_value": false,
      "site": "007f2a34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007f2a8c",
      "DATA",
      [
        "storage",
        "00c7ad38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f2a8c",
      "DATA",
      [
        "storage",
        "00c7ae08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2a10.md#insn-007f2a24) · [`007f2a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2a10.md#insn-007f2a30)
- 新版 `007f2a7c`（命令位置の公開資料なし） · `007f2a88`（命令位置の公開資料なし）

~~~diff
- 007f2a24 ["INT_ADD", "register:40f0:8", ["const:7f2a24:8", "const:4:8"]]
- 007f2a24 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f2a7c ["INT_ADD", "register:40f0:8", ["const:7f2a7c:8", "const:4:8"]]
+ 007f2a7c ["CALL", null, ["callee:00c57f60:8"]]
- 007f2a24 bytes 1b951194
+ 007f2a7c bytes 39951194
- 007f2a30 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 007f2a30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2a30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2a30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2a88 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 007f2a88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2a88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2a88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2a30 bytes 08e13491
+ 007f2a88 bytes 08213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce04bfdd1d72435f77be5ee78404ed5b"></a>

### [`007f2a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2a60.md) → [`007f2ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f2ab8.md) FUN_007f2ab8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f2bbc",
      "incomplete_value": false,
      "site": "007f2bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f2b64",
      "incomplete_value": false,
      "site": "007f2b64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:da8:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2af0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2a98",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2b0c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2ab4",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f2af0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f2b0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f2b48",
      "READ",
      [
        "storage",
        "002a7d01",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f2af0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f2b0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f2b48",
      "READ",
      [
        "storage",
        "002a7ca5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2a60.md#insn-007f2a98) · [`007f2ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2a60.md#insn-007f2ab4) · [`007f2c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2a60.md#insn-007f2c44)
- 新版 `007f2af0`（命令位置の公開資料なし） · `007f2b0c`（命令位置の公開資料なし） · `007f2c9c`（命令位置の公開資料なし）

~~~diff
- 007f2a98 ["INT_ADD", "register:40f0:8", ["const:7f2a98:8", "const:4:8"]]
- 007f2a98 ["CALL", null, ["ram:47acf4:8"]]
+ 007f2af0 ["INT_ADD", "register:40f0:8", ["const:7f2af0:8", "const:4:8"]]
+ 007f2af0 ["CALL", null, ["ram:47ad34:8"]]
- 007f2a98 bytes 9720f297
+ 007f2af0 bytes 9120f297
- 007f2ab4 ["INT_ADD", "register:40f0:8", ["const:7f2ab4:8", "const:4:8"]]
- 007f2ab4 ["CALL", null, ["ram:47acf4:8"]]
+ 007f2b0c ["INT_ADD", "register:40f0:8", ["const:7f2b0c:8", "const:4:8"]]
+ 007f2b0c ["CALL", null, ["ram:47ad34:8"]]
- 007f2ab4 bytes 9020f297
+ 007f2b0c bytes 8a20f297
- 007f2c44 ["INT_ADD", "register:40f0:8", ["const:7f2c44:8", "const:4:8"]]
- 007f2c44 ["CALL", null, ["callee:00442970:8"]]
+ 007f2c9c ["INT_ADD", "register:40f0:8", ["const:7f2c9c:8", "const:4:8"]]
+ 007f2c9c ["CALL", null, ["callee:00442970:8"]]
- 007f2c44 bytes 3b3ff197
+ 007f2c9c bytes 353ff197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-840f9ab3964d9c9df39563509dab4594"></a>

### [`007f2d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2d30.md) → [`007f2d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f2d88.md) FUN_007f2d88

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f2d9c",
      "incomplete_value": false,
      "site": "007f2da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f2d44",
      "incomplete_value": false,
      "site": "007f2d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "007f2da0",
      "DATA",
      [
        "storage",
        "00c7ada8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f2da0",
      "DATA",
      [
        "storage",
        "00c7ae78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2d30.md#insn-007f2d3c) · [`007f2d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2d30.md#insn-007f2d44)
- 新版 `007f2d94`（命令位置の公開資料なし） · `007f2d9c`（命令位置の公開資料なし）

~~~diff
- 007f2d3c ["INT_ADD", "register:40f0:8", ["const:7f2d3c:8", "const:4:8"]]
- 007f2d3c ["CALL", null, ["callee:00c57f60:8"]]
+ 007f2d94 ["INT_ADD", "register:40f0:8", ["const:7f2d94:8", "const:4:8"]]
+ 007f2d94 ["CALL", null, ["callee:00c57f60:8"]]
- 007f2d3c bytes 55941194
+ 007f2d94 bytes 73941194
- 007f2d44 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 007f2d44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2d44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2d9c ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 007f2d9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2d9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2d9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2d44 bytes 08a13691
+ 007f2d9c bytes 08e13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3d4a8f6648b4ac28c6b9003538ac901"></a>

### [`007f2d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2d54.md) → [`007f2dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f2dac.md) FUN_007f2dac

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f2db0",
      "incomplete_value": false,
      "site": "007f2db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f2d58",
      "incomplete_value": false,
      "site": "007f2d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:da8:8"
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
      "007f2db4",
      "DATA",
      [
        "storage",
        "00c7ada8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f2db4",
      "DATA",
      [
        "storage",
        "00c7ae78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2d54.md#insn-007f2d58)
- 新版 `007f2db0`（命令位置の公開資料なし）

~~~diff
- 007f2d58 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 007f2d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2db0 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 007f2db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2d58 bytes 08a13691
+ 007f2db0 bytes 08e13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0330557e69c358d07f7b33d9b861b81b"></a>

### [`007f2d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2d6c.md) → [`007f2dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f2dc4.md) FUN_007f2dc4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "site": "007f2de8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2d90",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f2de8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f2de8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2d6c.md#insn-007f2d90) · [`007f2d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2d6c.md#insn-007f2d9c)
- 新版 `007f2de8`（命令位置の公開資料なし） · `007f2df4`（命令位置の公開資料なし）

~~~diff
- 007f2d90 ["INT_ADD", "register:40f0:8", ["const:7f2d90:8", "const:4:8"]]
- 007f2d90 ["CALL", null, ["ram:47acf4:8"]]
+ 007f2de8 ["INT_ADD", "register:40f0:8", ["const:7f2de8:8", "const:4:8"]]
+ 007f2de8 ["CALL", null, ["ram:47ad34:8"]]
- 007f2d90 bytes d91ff297
+ 007f2de8 bytes d31ff297
- 007f2d9c ["INT_ADD", "register:40f0:8", ["const:7f2d9c:8", "const:4:8"]]
- 007f2d9c ["CALL", null, ["callee:0047ce14:8"]]
+ 007f2df4 ["INT_ADD", "register:40f0:8", ["const:7f2df4:8", "const:4:8"]]
+ 007f2df4 ["CALL", null, ["callee:0047ce14:8"]]
- 007f2d9c bytes 0e28f297
+ 007f2df4 bytes 0828f297
~~~


<a id="compare-c095d8dff192da1b5d94ae9a4526aa2d"></a>

### [`007f2de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2de0.md) → [`007f2e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f2e38.md) FUN_007f2e38

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f2e5c",
      "incomplete_value": false,
      "site": "007f2e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f2e04",
      "incomplete_value": false,
      "site": "007f2e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007f2e5c",
      "DATA",
      [
        "storage",
        "00c7ae38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f2e5c",
      "DATA",
      [
        "storage",
        "00c7af08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2de0.md#insn-007f2df4) · [`007f2e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2de0.md#insn-007f2e00)
- 新版 `007f2e4c`（命令位置の公開資料なし） · `007f2e58`（命令位置の公開資料なし）

~~~diff
- 007f2df4 ["INT_ADD", "register:40f0:8", ["const:7f2df4:8", "const:4:8"]]
- 007f2df4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f2e4c ["INT_ADD", "register:40f0:8", ["const:7f2e4c:8", "const:4:8"]]
+ 007f2e4c ["CALL", null, ["callee:00c57f60:8"]]
- 007f2df4 bytes 27941194
+ 007f2e4c bytes 45941194
- 007f2e00 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 007f2e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2e58 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 007f2e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2e00 bytes 08e13891
+ 007f2e58 bytes 08213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd130a3db0f41709e5810e570590493"></a>

### [`007f2e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2e30.md) → [`007f2e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f2/007f2e88.md) FUN_007f2e88

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`008b6f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f50.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`008b6fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2f4c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2ef4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2f68",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2f10",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f2f4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f2f68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f2f4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f2f68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2e30.md#insn-007f2eb8) · [`007f2ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2e30.md#insn-007f2ef4) · [`007f2f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2e30.md#insn-007f2f10)
- 新版 `007f2f10`（命令位置の公開資料なし） · `007f2f4c`（命令位置の公開資料なし） · `007f2f68`（命令位置の公開資料なし）

~~~diff
- 007f2eb8 ["INT_ADD", "register:40f0:8", ["const:7f2eb8:8", "const:4:8"]]
- 007f2eb8 ["CALL", null, ["callee:008b6efc:8"]]
+ 007f2f10 ["INT_ADD", "register:40f0:8", ["const:7f2f10:8", "const:4:8"]]
+ 007f2f10 ["CALL", null, ["callee:008b6efc:8"]]
- 007f2eb8 bytes fb0f0394
+ 007f2f10 bytes fb0f0394
- 007f2ef4 ["INT_ADD", "register:40f0:8", ["const:7f2ef4:8", "const:4:8"]]
- 007f2ef4 ["CALL", null, ["ram:47acf4:8"]]
+ 007f2f4c ["INT_ADD", "register:40f0:8", ["const:7f2f4c:8", "const:4:8"]]
+ 007f2f4c ["CALL", null, ["ram:47ad34:8"]]
- 007f2ef4 bytes 801ff297
+ 007f2f4c bytes 7a1ff297
- 007f2f10 ["INT_ADD", "register:40f0:8", ["const:7f2f10:8", "const:4:8"]]
- 007f2f10 ["CALL", null, ["ram:47acf4:8"]]
+ 007f2f68 ["INT_ADD", "register:40f0:8", ["const:7f2f68:8", "const:4:8"]]
+ 007f2f68 ["CALL", null, ["ram:47ad34:8"]]
- 007f2f10 bytes 791ff297
+ 007f2f68 bytes 731ff297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-748f7869e896357c15abc0cacc02507d"></a>

### [`007f3000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3000.md) → [`007f3058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3058.md) FUN_007f3058

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f307c",
      "incomplete_value": false,
      "site": "007f307c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f3024",
      "incomplete_value": false,
      "site": "007f3024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007f307c",
      "DATA",
      [
        "storage",
        "00c7aeb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f307c",
      "DATA",
      [
        "storage",
        "00c7af88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3000.md#insn-007f3014) · [`007f3020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3000.md#insn-007f3020)
- 新版 `007f306c`（命令位置の公開資料なし） · `007f3078`（命令位置の公開資料なし）

~~~diff
- 007f3014 ["INT_ADD", "register:40f0:8", ["const:7f3014:8", "const:4:8"]]
- 007f3014 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f306c ["INT_ADD", "register:40f0:8", ["const:7f306c:8", "const:4:8"]]
+ 007f306c ["CALL", null, ["callee:00c57f60:8"]]
- 007f3014 bytes 9f931194
+ 007f306c bytes bd931194
- 007f3020 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 007f3020 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3020 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3020 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3078 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 007f3078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3020 bytes 08e13a91
+ 007f3078 bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01ec48b5f411b67854ee4f43eccaeb73"></a>

### [`007f3050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3050.md) → [`007f30a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f30a8.md) FUN_007f30a8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00674724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00674/00674724.md) [`00675b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/00675b40.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00674764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00674/00674764.md) [`00675b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00675/00675b80.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f30e8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3090",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3104",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f30ac",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f30e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f3104",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f30e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f3104",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3050.md#insn-007f3090) · [`007f30ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3050.md#insn-007f30ac) · [`007f310c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3050.md#insn-007f310c)
- 新版 `007f30e8`（命令位置の公開資料なし） · `007f3104`（命令位置の公開資料なし） · `007f3164`（命令位置の公開資料なし）

~~~diff
- 007f3090 ["INT_ADD", "register:40f0:8", ["const:7f3090:8", "const:4:8"]]
- 007f3090 ["CALL", null, ["ram:47acf4:8"]]
+ 007f30e8 ["INT_ADD", "register:40f0:8", ["const:7f30e8:8", "const:4:8"]]
+ 007f30e8 ["CALL", null, ["ram:47ad34:8"]]
- 007f3090 bytes 191ff297
+ 007f30e8 bytes 131ff297
- 007f30ac ["INT_ADD", "register:40f0:8", ["const:7f30ac:8", "const:4:8"]]
- 007f30ac ["CALL", null, ["ram:47acf4:8"]]
+ 007f3104 ["INT_ADD", "register:40f0:8", ["const:7f3104:8", "const:4:8"]]
+ 007f3104 ["CALL", null, ["ram:47ad34:8"]]
- 007f30ac bytes 121ff297
+ 007f3104 bytes 0c1ff297
- 007f310c ["INT_ADD", "register:40f0:8", ["const:7f310c:8", "const:4:8"]]
- 007f310c ["CALL", null, ["callee:00675b80:8"]]
+ 007f3164 ["INT_ADD", "register:40f0:8", ["const:7f3164:8", "const:4:8"]]
+ 007f3164 ["CALL", null, ["callee:00675b80:8"]]
- 007f310c bytes 8d0afa97
+ 007f3164 bytes 870afa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-337044d047d8d7bd00782d1ab7ca69e9"></a>

### [`007f3244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3244.md) → [`007f329c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f329c.md) FUN_007f329c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f32c0",
      "incomplete_value": false,
      "site": "007f32c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f3268",
      "incomplete_value": false,
      "site": "007f3268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "007f32c0",
      "DATA",
      [
        "storage",
        "00c7af38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f32c0",
      "DATA",
      [
        "storage",
        "00c7b008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3244.md#insn-007f3258) · [`007f3260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3244.md#insn-007f3260) · [`007f3264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3244.md#insn-007f3264)
- 新版 `007f32b0`（命令位置の公開資料なし） · `007f32b8`（命令位置の公開資料なし） · `007f32bc`（命令位置の公開資料なし）

~~~diff
- 007f3258 ["INT_ADD", "register:40f0:8", ["const:7f3258:8", "const:4:8"]]
- 007f3258 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f32b0 ["INT_ADD", "register:40f0:8", ["const:7f32b0:8", "const:4:8"]]
+ 007f32b0 ["CALL", null, ["callee:00c57f60:8"]]
- 007f3258 bytes 0e931194
+ 007f32b0 bytes 2c931194
- 007f3260 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 007f32b8 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 007f3260 bytes 282400f0
+ 007f32b8 bytes 48240090
- 007f3264 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 007f3264 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3264 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3264 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f32bc ["COPY", "tmp:0:8", ["const:8:8"]]
+ 007f32bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f32bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f32bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3264 bytes 08e13c91
+ 007f32bc bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a00303ed8836787f4c45d646222541b"></a>

### [`007f3294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3294.md) → [`007f32ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f32ec.md) FUN_007f32ec

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007f3518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3518.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce90.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`007f3570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3570.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f33dc",
      "incomplete_value": false,
      "site": "007f33e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f3384",
      "incomplete_value": false,
      "site": "007f338c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3320",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f32c8",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f3320",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f33b0",
      "READ",
      [
        "storage",
        "002b4baa",
        null,
        "string"
      ]
    ],
    [
      "007f33e4",
      "DATA",
      [
        "storage",
        "00c7afa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3320",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f33b0",
      "READ",
      [
        "storage",
        "002b4bdb",
        null,
        "string"
      ]
    ],
    [
      "007f33e4",
      "DATA",
      [
        "storage",
        "00c7b078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f32c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3294.md#insn-007f32c8) · [`007f32fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3294.md#insn-007f32fc) · [`007f3350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3294.md#insn-007f3350)
- 新版 `007f3320`（命令位置の公開資料なし） · `007f3354`（命令位置の公開資料なし） · `007f33a8`（命令位置の公開資料なし）

~~~diff
- 007f32c8 ["INT_ADD", "register:40f0:8", ["const:7f32c8:8", "const:4:8"]]
- 007f32c8 ["CALL", null, ["ram:47acf4:8"]]
+ 007f3320 ["INT_ADD", "register:40f0:8", ["const:7f3320:8", "const:4:8"]]
+ 007f3320 ["CALL", null, ["ram:47ad34:8"]]
- 007f32c8 bytes 8b1ef297
+ 007f3320 bytes 851ef297
- 007f32fc ["INT_ADD", "register:40f0:8", ["const:7f32fc:8", "const:4:8"]]
- 007f32fc ["CALL", null, ["callee:0048ce90:8"]]
+ 007f3354 ["INT_ADD", "register:40f0:8", ["const:7f3354:8", "const:4:8"]]
+ 007f3354 ["CALL", null, ["callee:0048ce90:8"]]
- 007f32fc bytes d566f297
+ 007f3354 bytes cf66f297
- 007f3350 ["COPY", "tmp:0:8", ["const:baa:8"]]
- 007f3350 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f3350 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f3350 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f33a8 ["COPY", "tmp:0:8", ["const:bdb:8"]]
+ 007f33a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f33a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f33a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f3350 bytes 29a92e91
+ 007f33a8 bytes 296d2f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14e6fe53bc7a3eed7644d2675d3b16e5"></a>

### [`007f34e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f34e4.md) → [`007f353c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f353c.md) FUN_007f353c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f3550",
      "incomplete_value": false,
      "site": "007f3554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f34f8",
      "incomplete_value": false,
      "site": "007f34fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "007f3554",
      "DATA",
      [
        "storage",
        "00c7afa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3554",
      "DATA",
      [
        "storage",
        "00c7b078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f34f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f34e4.md#insn-007f34f0) · [`007f34f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f34e4.md#insn-007f34f4) · [`007f34f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f34e4.md#insn-007f34f8)
- 新版 `007f3548`（命令位置の公開資料なし） · `007f354c`（命令位置の公開資料なし） · `007f3550`（命令位置の公開資料なし）

~~~diff
- 007f34f0 ["INT_ADD", "register:40f0:8", ["const:7f34f0:8", "const:4:8"]]
- 007f34f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f3548 ["INT_ADD", "register:40f0:8", ["const:7f3548:8", "const:4:8"]]
+ 007f3548 ["CALL", null, ["callee:00c57f60:8"]]
- 007f34f0 bytes 68921194
+ 007f3548 bytes 86921194
- 007f34f4 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 007f354c ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 007f34f4 bytes 282400f0
+ 007f354c bytes 48240090
- 007f34f8 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 007f34f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f34f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f34f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3550 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007f3550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f34f8 bytes 08a13e91
+ 007f3550 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1837c1101cb7c02d74f8359bb33db9f7"></a>

### [`007f3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3508.md) → [`007f3560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3560.md) FUN_007f3560

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f3564",
      "incomplete_value": false,
      "site": "007f3568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f350c",
      "incomplete_value": false,
      "site": "007f3510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "007f3568",
      "DATA",
      [
        "storage",
        "00c7afa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3568",
      "DATA",
      [
        "storage",
        "00c7b078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3508.md#insn-007f3508) · [`007f350c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3508.md#insn-007f350c)
- 新版 `007f3560`（命令位置の公開資料なし） · `007f3564`（命令位置の公開資料なし）

~~~diff
- 007f3508 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 007f3560 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 007f3508 bytes 282400f0
+ 007f3560 bytes 48240090
- 007f350c ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 007f350c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f350c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f350c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3564 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007f3564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f350c bytes 08a13e91
+ 007f3564 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ada60208da67d5a78032467e4c9a8469"></a>

### [`007f3564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3564.md) → [`007f35bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f35bc.md) FUN_007f35bc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f35e0",
      "incomplete_value": false,
      "site": "007f35e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f3588",
      "incomplete_value": false,
      "site": "007f3588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f35e0",
      "DATA",
      [
        "storage",
        "00c7b038",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f35e0",
      "DATA",
      [
        "storage",
        "00c7b108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3564.md#insn-007f3578) · [`007f3584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3564.md#insn-007f3584)
- 新版 `007f35d0`（命令位置の公開資料なし） · `007f35dc`（命令位置の公開資料なし）

~~~diff
- 007f3578 ["INT_ADD", "register:40f0:8", ["const:7f3578:8", "const:4:8"]]
- 007f3578 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f35d0 ["INT_ADD", "register:40f0:8", ["const:7f35d0:8", "const:4:8"]]
+ 007f35d0 ["CALL", null, ["callee:00c57f60:8"]]
- 007f3578 bytes 46921194
+ 007f35d0 bytes 64921194
- 007f3584 ["COPY", "tmp:0:8", ["const:38:8"]]
- 007f3584 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3584 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3584 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f35dc ["COPY", "tmp:0:8", ["const:108:8"]]
+ 007f35dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f35dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f35dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3584 bytes 08e10091
+ 007f35dc bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5441a445a958effc654939915d575db5"></a>

### [`007f35b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f35b4.md) → [`007f360c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f360c.md) FUN_007f360c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b7a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a68.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f362c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f35d4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3638",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f35e0",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f362c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f3638",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f362c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f3638",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f35d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f35b4.md#insn-007f35d4) · [`007f35e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f35b4.md#insn-007f35e0)
- 新版 `007f362c`（命令位置の公開資料なし） · `007f3638`（命令位置の公開資料なし）

~~~diff
- 007f35d4 ["INT_ADD", "register:40f0:8", ["const:7f35d4:8", "const:4:8"]]
- 007f35d4 ["CALL", null, ["ram:47acf4:8"]]
+ 007f362c ["INT_ADD", "register:40f0:8", ["const:7f362c:8", "const:4:8"]]
+ 007f362c ["CALL", null, ["ram:47ad34:8"]]
- 007f35d4 bytes c81df297
+ 007f362c bytes c21df297
- 007f35e0 ["INT_ADD", "register:40f0:8", ["const:7f35e0:8", "const:4:8"]]
- 007f35e0 ["CALL", null, ["ram:47acf4:8"]]
+ 007f3638 ["INT_ADD", "register:40f0:8", ["const:7f3638:8", "const:4:8"]]
+ 007f3638 ["CALL", null, ["ram:47ad34:8"]]
- 007f35e0 bytes c51df297
+ 007f3638 bytes bf1df297
~~~


<a id="compare-5915429715cd4411a8d587427800c13d"></a>

### [`007f3658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3658.md) → [`007f36b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f36b0.md) FUN_007f36b0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f36d4",
      "incomplete_value": false,
      "site": "007f36d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f367c",
      "incomplete_value": false,
      "site": "007f367c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f36d4",
      "DATA",
      [
        "storage",
        "00c7b0b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f36d4",
      "DATA",
      [
        "storage",
        "00c7b188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f366c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3658.md#insn-007f366c) · [`007f3678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3658.md#insn-007f3678)
- 新版 `007f36c4`（命令位置の公開資料なし） · `007f36d0`（命令位置の公開資料なし）

~~~diff
- 007f366c ["INT_ADD", "register:40f0:8", ["const:7f366c:8", "const:4:8"]]
- 007f366c ["CALL", null, ["callee:00c57f60:8"]]
+ 007f36c4 ["INT_ADD", "register:40f0:8", ["const:7f36c4:8", "const:4:8"]]
+ 007f36c4 ["CALL", null, ["callee:00c57f60:8"]]
- 007f366c bytes 09921194
+ 007f36c4 bytes 27921194
- 007f3678 ["COPY", "tmp:0:8", ["const:b8:8"]]
- 007f3678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f36d0 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 007f36d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f36d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f36d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3678 bytes 08e10291
+ 007f36d0 bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00bd12c32da6a56d7b581f03834af141"></a>

### [`007f36a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f36a8.md) → [`007f3700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3700.md) FUN_007f3700

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007f39d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f39d8.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce90.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`007f3a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3a30.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.14% / 新版 95.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f3830",
      "incomplete_value": false,
      "site": "007f3838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f37d8",
      "incomplete_value": false,
      "site": "007f37e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:128:8"
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
      "site": "007f3738",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f36e0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3754",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f36fc",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f3738",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f3754",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f3804",
      "READ",
      [
        "storage",
        "002b4baa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f3738",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f3754",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f3804",
      "READ",
      [
        "storage",
        "002b4bdb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f36e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f36a8.md#insn-007f36e0) · [`007f36fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f36a8.md#insn-007f36fc) · [`007f38a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f36a8.md#insn-007f38a4)
- 新版 `007f3738`（命令位置の公開資料なし） · `007f3754`（命令位置の公開資料なし） · `007f38fc`（命令位置の公開資料なし）

~~~diff
- 007f36e0 ["INT_ADD", "register:40f0:8", ["const:7f36e0:8", "const:4:8"]]
- 007f36e0 ["CALL", null, ["ram:47acf4:8"]]
+ 007f3738 ["INT_ADD", "register:40f0:8", ["const:7f3738:8", "const:4:8"]]
+ 007f3738 ["CALL", null, ["ram:47ad34:8"]]
- 007f36e0 bytes 851df297
+ 007f3738 bytes 7f1df297
- 007f36fc ["INT_ADD", "register:40f0:8", ["const:7f36fc:8", "const:4:8"]]
- 007f36fc ["CALL", null, ["ram:47acf4:8"]]
+ 007f3754 ["INT_ADD", "register:40f0:8", ["const:7f3754:8", "const:4:8"]]
+ 007f3754 ["CALL", null, ["ram:47ad34:8"]]
- 007f36fc bytes 7e1df297
+ 007f3754 bytes 781df297
- 007f38a4 ["INT_ADD", "register:40f0:8", ["const:7f38a4:8", "const:4:8"]]
- 007f38a4 ["CALL", null, ["ram:803d7c:8"]]
+ 007f38fc ["INT_ADD", "register:40f0:8", ["const:7f38fc:8", "const:4:8"]]
+ 007f38fc ["CALL", null, ["ram:803dd4:8"]]
- 007f38a4 bytes 36410094
+ 007f38fc bytes 36410094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61e4f48376596616168bba565d4792d1"></a>

### [`007f39a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f39a4.md) → [`007f39fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f39fc.md) FUN_007f39fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f3a10",
      "incomplete_value": false,
      "site": "007f3a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f39b8",
      "incomplete_value": false,
      "site": "007f39bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:128:8"
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
      "007f3a14",
      "DATA",
      [
        "storage",
        "00c7b128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3a14",
      "DATA",
      [
        "storage",
        "00c7b1f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f39b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f39a4.md#insn-007f39b0) · [`007f39b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f39a4.md#insn-007f39b8)
- 新版 `007f3a08`（命令位置の公開資料なし） · `007f3a10`（命令位置の公開資料なし）

~~~diff
- 007f39b0 ["INT_ADD", "register:40f0:8", ["const:7f39b0:8", "const:4:8"]]
- 007f39b0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f3a08 ["INT_ADD", "register:40f0:8", ["const:7f3a08:8", "const:4:8"]]
+ 007f3a08 ["CALL", null, ["callee:00c57f60:8"]]
- 007f39b0 bytes 38911194
+ 007f3a08 bytes 56911194
- 007f39b8 ["COPY", "tmp:0:8", ["const:128:8"]]
- 007f39b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f39b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f39b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3a10 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 007f3a10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3a10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3a10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f39b8 bytes 08a10491
+ 007f3a10 bytes 08e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46b82b4b4a7846bad520921d84bb815a"></a>

### [`007f39c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f39c8.md) → [`007f3a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3a20.md) FUN_007f3a20

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f3a24",
      "incomplete_value": false,
      "site": "007f3a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f39cc",
      "incomplete_value": false,
      "site": "007f39d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:128:8"
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
      "007f3a28",
      "DATA",
      [
        "storage",
        "00c7b128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3a28",
      "DATA",
      [
        "storage",
        "00c7b1f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f39cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f39c8.md#insn-007f39cc)
- 新版 `007f3a24`（命令位置の公開資料なし）

~~~diff
- 007f39cc ["COPY", "tmp:0:8", ["const:128:8"]]
- 007f39cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f39cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f39cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3a24 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 007f3a24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3a24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3a24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f39cc bytes 08a10491
+ 007f3a24 bytes 08e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-683672cda9e871305746fc185b51a9a0"></a>

### [`007f3a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3a24.md) → [`007f3a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3a7c.md) FUN_007f3a7c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f3aa0",
      "incomplete_value": false,
      "site": "007f3aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f3a48",
      "incomplete_value": false,
      "site": "007f3a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
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
      "007f3aa0",
      "DATA",
      [
        "storage",
        "00c7b1b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3aa0",
      "DATA",
      [
        "storage",
        "00c7b288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3a24.md#insn-007f3a38) · [`007f3a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3a24.md#insn-007f3a44)
- 新版 `007f3a90`（命令位置の公開資料なし） · `007f3a9c`（命令位置の公開資料なし）

~~~diff
- 007f3a38 ["INT_ADD", "register:40f0:8", ["const:7f3a38:8", "const:4:8"]]
- 007f3a38 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f3a90 ["INT_ADD", "register:40f0:8", ["const:7f3a90:8", "const:4:8"]]
+ 007f3a90 ["CALL", null, ["callee:00c57f60:8"]]
- 007f3a38 bytes 16911194
+ 007f3a90 bytes 34911194
- 007f3a44 ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 007f3a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3a9c ["COPY", "tmp:0:8", ["const:288:8"]]
+ 007f3a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3a44 bytes 08e10691
+ 007f3a9c bytes 08210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e13815d0f18af2fb7a3e0dd04dd63244"></a>

### [`007f3a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3a74.md) → [`007f3acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3acc.md) FUN_007f3acc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f3c44",
      "incomplete_value": false,
      "site": "007f3c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f3bec",
      "incomplete_value": false,
      "site": "007f3bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3b08",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3ab0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3b24",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3acc",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f3b08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f3b24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f3bd0",
      "READ",
      [
        "storage",
        "002aeccb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f3b08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f3b24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f3bd0",
      "READ",
      [
        "storage",
        "002aec6f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3a74.md#insn-007f3ab0) · [`007f3acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3a74.md#insn-007f3acc) · [`007f3cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3a74.md#insn-007f3cd0)
- 新版 `007f3b08`（命令位置の公開資料なし） · `007f3b24`（命令位置の公開資料なし） · `007f3d28`（命令位置の公開資料なし）

~~~diff
- 007f3ab0 ["INT_ADD", "register:40f0:8", ["const:7f3ab0:8", "const:4:8"]]
- 007f3ab0 ["CALL", null, ["ram:47acf4:8"]]
+ 007f3b08 ["INT_ADD", "register:40f0:8", ["const:7f3b08:8", "const:4:8"]]
+ 007f3b08 ["CALL", null, ["ram:47ad34:8"]]
- 007f3ab0 bytes 911cf297
+ 007f3b08 bytes 8b1cf297
- 007f3acc ["INT_ADD", "register:40f0:8", ["const:7f3acc:8", "const:4:8"]]
- 007f3acc ["CALL", null, ["ram:47acf4:8"]]
+ 007f3b24 ["INT_ADD", "register:40f0:8", ["const:7f3b24:8", "const:4:8"]]
+ 007f3b24 ["CALL", null, ["ram:47ad34:8"]]
- 007f3acc bytes 8a1cf297
+ 007f3b24 bytes 841cf297
- 007f3cd0 ["INT_ADD", "register:40f0:8", ["const:7f3cd0:8", "const:4:8"]]
- 007f3cd0 ["CALL", null, ["callee:00442970:8"]]
+ 007f3d28 ["INT_ADD", "register:40f0:8", ["const:7f3d28:8", "const:4:8"]]
+ 007f3d28 ["CALL", null, ["callee:00442970:8"]]
- 007f3cd0 bytes 183bf197
+ 007f3d28 bytes 123bf197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19347e53fac29a0f80d950a7549297e8"></a>

### [`007f3dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3dbc.md) → [`007f3e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3e14.md) FUN_007f3e14

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f3e28",
      "incomplete_value": false,
      "site": "007f3e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f3dd0",
      "incomplete_value": false,
      "site": "007f3dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "007f3e2c",
      "DATA",
      [
        "storage",
        "00c7b228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3e2c",
      "DATA",
      [
        "storage",
        "00c7b2f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3dbc.md#insn-007f3dc8) · [`007f3dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3dbc.md#insn-007f3dd0)
- 新版 `007f3e20`（命令位置の公開資料なし） · `007f3e28`（命令位置の公開資料なし）

~~~diff
- 007f3dc8 ["INT_ADD", "register:40f0:8", ["const:7f3dc8:8", "const:4:8"]]
- 007f3dc8 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f3e20 ["INT_ADD", "register:40f0:8", ["const:7f3e20:8", "const:4:8"]]
+ 007f3e20 ["CALL", null, ["callee:00c57f60:8"]]
- 007f3dc8 bytes 32901194
+ 007f3e20 bytes 50901194
- 007f3dd0 ["COPY", "tmp:0:8", ["const:228:8"]]
- 007f3dd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3dd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3dd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3e28 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 007f3e28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3e28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3e28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3dd0 bytes 08a10891
+ 007f3e28 bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e43a0b86e38fb586d2e445891829e73"></a>

### [`007f3de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3de0.md) → [`007f3e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3e38.md) FUN_007f3e38

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f3e3c",
      "incomplete_value": false,
      "site": "007f3e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f3de4",
      "incomplete_value": false,
      "site": "007f3de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f3e40",
      "DATA",
      [
        "storage",
        "00c7b228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3e40",
      "DATA",
      [
        "storage",
        "00c7b2f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3de0.md#insn-007f3de4)
- 新版 `007f3e3c`（命令位置の公開資料なし）

~~~diff
- 007f3de4 ["COPY", "tmp:0:8", ["const:228:8"]]
- 007f3de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3e3c ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 007f3e3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3e3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3e3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3de4 bytes 08a10891
+ 007f3e3c bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c712cf15fc11aa9f997dcb6068993be"></a>

### [`007f3df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3df8.md) → [`007f3e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3e50.md) FUN_007f3e50

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "site": "007f3e74",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3e1c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f3e74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f3e74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3df8.md#insn-007f3e1c) · [`007f3e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3df8.md#insn-007f3e28)
- 新版 `007f3e74`（命令位置の公開資料なし） · `007f3e80`（命令位置の公開資料なし）

~~~diff
- 007f3e1c ["INT_ADD", "register:40f0:8", ["const:7f3e1c:8", "const:4:8"]]
- 007f3e1c ["CALL", null, ["ram:47acf4:8"]]
+ 007f3e74 ["INT_ADD", "register:40f0:8", ["const:7f3e74:8", "const:4:8"]]
+ 007f3e74 ["CALL", null, ["ram:47ad34:8"]]
- 007f3e1c bytes b61bf297
+ 007f3e74 bytes b01bf297
- 007f3e28 ["INT_ADD", "register:40f0:8", ["const:7f3e28:8", "const:4:8"]]
- 007f3e28 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f3e80 ["INT_ADD", "register:40f0:8", ["const:7f3e80:8", "const:4:8"]]
+ 007f3e80 ["CALL", null, ["callee:0047ce14:8"]]
- 007f3e28 bytes eb23f297
+ 007f3e80 bytes e523f297
~~~


<a id="compare-fa7102ae4c709074e7f0059c4e82ffbe"></a>

### [`007f3e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3e8c.md) → [`007f3ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f3/007f3ee4.md) FUN_007f3ee4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 10件 [`006d738c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d738c.md) [`006d7650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7650.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`006d76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76e4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 1件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) · 呼出先 10件 [`006d73e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d73e4.md) [`006d76a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76a8.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`006d773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d773c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.48% / 新版 99.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f41a4",
      "incomplete_value": false,
      "site": "007f41a8",
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
            "const:f75:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f414c",
      "incomplete_value": false,
      "site": "007f4150",
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
            "const:fd1:8"
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
      "007f41a4",
      "PARAM",
      [
        "storage",
        "002a9fd1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f41a4",
      "PARAM",
      [
        "storage",
        "002a9f75",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f4150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3e8c.md#insn-007f4150) · [`007f3f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3e8c.md#insn-007f3f0c) · [`007f3f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3e8c.md#insn-007f3f2c)
- 新版 `007f41a8`（命令位置の公開資料なし） · `007f3f64`（命令位置の公開資料なし） · `007f3f84`（命令位置の公開資料なし）

~~~diff
- 007f4150 ["INT_ADD", "register:40f0:8", ["const:7f4150:8", "const:4:8"]]
- 007f4150 ["CALL", null, ["callee:006d76a8:8"]]
+ 007f41a8 ["INT_ADD", "register:40f0:8", ["const:7f41a8:8", "const:4:8"]]
+ 007f41a8 ["CALL", null, ["callee:006d76a8:8"]]
- 007f4150 bytes 408dfb97
+ 007f41a8 bytes 408dfb97
- 007f3f0c ["INT_ADD", "register:40f0:8", ["const:7f3f0c:8", "const:4:8"]]
- 007f3f0c ["CALL", null, ["callee:00c57f60:8"]]
+ 007f3f64 ["INT_ADD", "register:40f0:8", ["const:7f3f64:8", "const:4:8"]]
+ 007f3f64 ["CALL", null, ["callee:00c57f60:8"]]
- 007f3f0c bytes e18f1194
+ 007f3f64 bytes ff8f1194
- 007f3f2c ["INT_ADD", "register:40f0:8", ["const:7f3f2c:8", "const:4:8"]]
- 007f3f2c ["CALL", null, ["callee:00c58160:8"]]
+ 007f3f84 ["INT_ADD", "register:40f0:8", ["const:7f3f84:8", "const:4:8"]]
+ 007f3f84 ["CALL", null, ["callee:00c58160:8"]]
- 007f3f2c bytes 59901194
+ 007f3f84 bytes 77901194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15aba7a4a2e48817f8246467e78a0f88"></a>

### [`007f4190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4190.md) → [`007f41e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f41e8.md) FUN_007f41e8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`006d7650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7650.md) [`006d7b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7b90.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) · 呼出先 9件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`006d76a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76a8.md) [`006d7be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d7be8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.59% / 新版 99.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007f4590",
      "incomplete_value": false,
      "site": "007f4594",
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
            "const:b7b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f4538",
      "incomplete_value": false,
      "site": "007f453c",
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
            "const:bd7:8"
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
      "007f4590",
      "PARAM",
      [
        "storage",
        "002a7bd7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f4590",
      "PARAM",
      [
        "storage",
        "002a7b7b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f453c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4190.md#insn-007f453c) · [`007f4220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4190.md#insn-007f4220) · [`007f4240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4190.md#insn-007f4240)
- 新版 `007f4594`（命令位置の公開資料なし） · `007f4278`（命令位置の公開資料なし） · `007f4298`（命令位置の公開資料なし）

~~~diff
- 007f453c ["INT_ADD", "register:40f0:8", ["const:7f453c:8", "const:4:8"]]
- 007f453c ["CALL", null, ["callee:006d76a8:8"]]
+ 007f4594 ["INT_ADD", "register:40f0:8", ["const:7f4594:8", "const:4:8"]]
+ 007f4594 ["CALL", null, ["callee:006d76a8:8"]]
- 007f453c bytes 458cfb97
+ 007f4594 bytes 458cfb97
- 007f4220 ["INT_ADD", "register:40f0:8", ["const:7f4220:8", "const:4:8"]]
- 007f4220 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f4278 ["INT_ADD", "register:40f0:8", ["const:7f4278:8", "const:4:8"]]
+ 007f4278 ["CALL", null, ["callee:00c57f60:8"]]
- 007f4220 bytes 1c8f1194
+ 007f4278 bytes 3a8f1194
- 007f4240 ["INT_ADD", "register:40f0:8", ["const:7f4240:8", "const:4:8"]]
- 007f4240 ["CALL", null, ["callee:00c58160:8"]]
+ 007f4298 ["INT_ADD", "register:40f0:8", ["const:7f4298:8", "const:4:8"]]
+ 007f4298 ["CALL", null, ["callee:00c58160:8"]]
- 007f4240 bytes 948f1194
+ 007f4298 bytes b28f1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9521374f01b5d7f071ababa36e1ef88f"></a>

### [`007f45a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f45a8.md) → [`007f4600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f4600.md) FUN_007f4600

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f4624",
      "incomplete_value": false,
      "site": "007f4624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f45cc",
      "incomplete_value": false,
      "site": "007f45cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:330:8"
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
      "007f4624",
      "DATA",
      [
        "storage",
        "00c7b330",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f4624",
      "DATA",
      [
        "storage",
        "00c7b400",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f45bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f45a8.md#insn-007f45bc) · [`007f45c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f45a8.md#insn-007f45c8)
- 新版 `007f4614`（命令位置の公開資料なし） · `007f4620`（命令位置の公開資料なし）

~~~diff
- 007f45bc ["INT_ADD", "register:40f0:8", ["const:7f45bc:8", "const:4:8"]]
- 007f45bc ["CALL", null, ["callee:00c57f60:8"]]
+ 007f4614 ["INT_ADD", "register:40f0:8", ["const:7f4614:8", "const:4:8"]]
+ 007f4614 ["CALL", null, ["callee:00c57f60:8"]]
- 007f45bc bytes 358e1194
+ 007f4614 bytes 538e1194
- 007f45c8 ["COPY", "tmp:0:8", ["const:330:8"]]
- 007f45c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f45c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f45c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f4620 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 007f4620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f45c8 bytes 08c10c91
+ 007f4620 bytes 08011091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-244ad096f7b22f330328584cfa549f32"></a>

### [`007f45dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f45dc.md) → [`007f4634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f4634.md) FUN_007f4634

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f4640",
      "incomplete_value": false,
      "site": "007f4640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f45e8",
      "incomplete_value": false,
      "site": "007f45e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:330:8"
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
      "007f4640",
      "DATA",
      [
        "storage",
        "00c7b330",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f4640",
      "DATA",
      [
        "storage",
        "00c7b400",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f45e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f45dc.md#insn-007f45e4)
- 新版 `007f463c`（命令位置の公開資料なし）

~~~diff
- 007f45e4 ["COPY", "tmp:0:8", ["const:330:8"]]
- 007f45e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f45e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f45e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f463c ["COPY", "tmp:0:8", ["const:400:8"]]
+ 007f463c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f463c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f463c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f45e4 bytes 29c10c91
+ 007f463c bytes 29011091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f79dcd7a87aa8f3680273be720d59c67"></a>

### [`007f46a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f46a8.md) → [`007f4700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f4700.md) FUN_007f4700

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f4724",
      "incomplete_value": false,
      "site": "007f4724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f46cc",
      "incomplete_value": false,
      "site": "007f46cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "007f4724",
      "DATA",
      [
        "storage",
        "00c7b3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f4724",
      "DATA",
      [
        "storage",
        "00c7b480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f46bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f46a8.md#insn-007f46bc) · [`007f46c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f46a8.md#insn-007f46c8)
- 新版 `007f4714`（命令位置の公開資料なし） · `007f4720`（命令位置の公開資料なし）

~~~diff
- 007f46bc ["INT_ADD", "register:40f0:8", ["const:7f46bc:8", "const:4:8"]]
- 007f46bc ["CALL", null, ["callee:00c57f60:8"]]
+ 007f4714 ["INT_ADD", "register:40f0:8", ["const:7f4714:8", "const:4:8"]]
+ 007f4714 ["CALL", null, ["callee:00c57f60:8"]]
- 007f46bc bytes f58d1194
+ 007f4714 bytes 138e1194
- 007f46c8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 007f46c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f46c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f46c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f4720 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 007f4720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f46c8 bytes 08c10e91
+ 007f4720 bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-369f196f4a84c02ceeb711978d7c761d"></a>

### [`007f46dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f46dc.md) → [`007f4734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f4734.md) FUN_007f4734

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f4740",
      "incomplete_value": false,
      "site": "007f4740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f46e8",
      "incomplete_value": false,
      "site": "007f46e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "007f4740",
      "DATA",
      [
        "storage",
        "00c7b3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f4740",
      "DATA",
      [
        "storage",
        "00c7b480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f46e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f46dc.md#insn-007f46e4)
- 新版 `007f473c`（命令位置の公開資料なし）

~~~diff
- 007f46e4 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 007f46e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f46e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f46e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f473c ["COPY", "tmp:0:8", ["const:480:8"]]
+ 007f473c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f473c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f473c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f46e4 bytes 29c10e91
+ 007f473c bytes 29011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f263c974f09720ff061c863c2c99188"></a>

### [`007f4790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4790.md) → [`007f47e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f47e8.md) FUN_007f47e8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f480c",
      "incomplete_value": false,
      "site": "007f480c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f47b4",
      "incomplete_value": false,
      "site": "007f47b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:430:8"
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
      "007f480c",
      "DATA",
      [
        "storage",
        "00c7b430",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f480c",
      "DATA",
      [
        "storage",
        "00c7b500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f47a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4790.md#insn-007f47a4) · [`007f47b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4790.md#insn-007f47b0)
- 新版 `007f47fc`（命令位置の公開資料なし） · `007f4808`（命令位置の公開資料なし）

~~~diff
- 007f47a4 ["INT_ADD", "register:40f0:8", ["const:7f47a4:8", "const:4:8"]]
- 007f47a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f47fc ["INT_ADD", "register:40f0:8", ["const:7f47fc:8", "const:4:8"]]
+ 007f47fc ["CALL", null, ["callee:00c57f60:8"]]
- 007f47a4 bytes bb8d1194
+ 007f47fc bytes d98d1194
- 007f47b0 ["COPY", "tmp:0:8", ["const:430:8"]]
- 007f47b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f47b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f47b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f4808 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 007f4808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f47b0 bytes 08c11091
+ 007f4808 bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cac3884737d174ffeee8cb265d750eec"></a>

### [`007f47c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f47c4.md) → [`007f481c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f481c.md) FUN_007f481c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f4828",
      "incomplete_value": false,
      "site": "007f4828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f47d0",
      "incomplete_value": false,
      "site": "007f47d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:430:8"
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
      "007f4828",
      "DATA",
      [
        "storage",
        "00c7b430",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f4828",
      "DATA",
      [
        "storage",
        "00c7b500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f47cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f47c4.md#insn-007f47cc)
- 新版 `007f4824`（命令位置の公開資料なし）

~~~diff
- 007f47cc ["COPY", "tmp:0:8", ["const:430:8"]]
- 007f47cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f47cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f47cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f4824 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 007f4824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f4824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f4824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f47cc bytes 29c11091
+ 007f4824 bytes 29011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-459f97c73c43d2a9597ef4b4aeb623b8"></a>

### [`007f4898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4898.md) → [`007f48f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f48f0.md) FUN_007f48f0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f4914",
      "incomplete_value": false,
      "site": "007f4914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f48bc",
      "incomplete_value": false,
      "site": "007f48bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
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
      "007f4914",
      "DATA",
      [
        "storage",
        "00c7b4b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f4914",
      "DATA",
      [
        "storage",
        "00c7b580",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f48ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4898.md#insn-007f48ac) · [`007f48b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4898.md#insn-007f48b8)
- 新版 `007f4904`（命令位置の公開資料なし） · `007f4910`（命令位置の公開資料なし）

~~~diff
- 007f48ac ["INT_ADD", "register:40f0:8", ["const:7f48ac:8", "const:4:8"]]
- 007f48ac ["CALL", null, ["callee:00c57f60:8"]]
+ 007f4904 ["INT_ADD", "register:40f0:8", ["const:7f4904:8", "const:4:8"]]
+ 007f4904 ["CALL", null, ["callee:00c57f60:8"]]
- 007f48ac bytes 798d1194
+ 007f4904 bytes 978d1194
- 007f48b8 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 007f48b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f48b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f48b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f4910 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 007f4910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f48b8 bytes 08c11291
+ 007f4910 bytes 08011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2926d08d300511ec53059e1a0decac32"></a>

### [`007f4a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4a04.md) → [`007f4a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f4a5c.md) FUN_007f4a5c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f4a80",
      "incomplete_value": false,
      "site": "007f4a80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f4a28",
      "incomplete_value": false,
      "site": "007f4a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:530:8"
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
      "007f4a80",
      "DATA",
      [
        "storage",
        "00c7b530",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f4a80",
      "DATA",
      [
        "storage",
        "00c7b600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f4a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4a04.md#insn-007f4a18) · [`007f4a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4a04.md#insn-007f4a24)
- 新版 `007f4a70`（命令位置の公開資料なし） · `007f4a7c`（命令位置の公開資料なし）

~~~diff
- 007f4a18 ["INT_ADD", "register:40f0:8", ["const:7f4a18:8", "const:4:8"]]
- 007f4a18 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f4a70 ["INT_ADD", "register:40f0:8", ["const:7f4a70:8", "const:4:8"]]
+ 007f4a70 ["CALL", null, ["callee:00c57f60:8"]]
- 007f4a18 bytes 1e8d1194
+ 007f4a70 bytes 3c8d1194
- 007f4a24 ["COPY", "tmp:0:8", ["const:530:8"]]
- 007f4a24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f4a24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f4a24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f4a7c ["COPY", "tmp:0:8", ["const:600:8"]]
+ 007f4a7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4a7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4a7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f4a24 bytes 08c11491
+ 007f4a7c bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-106e954dbf42752e7958ebada2f8e3cc"></a>

### [`007f4acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4acc.md) → [`007f4b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f4b24.md) FUN_007f4b24

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f4b48",
      "incomplete_value": false,
      "site": "007f4b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f4af0",
      "incomplete_value": false,
      "site": "007f4af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "007f4b4c",
      "DATA",
      [
        "storage",
        "00c7b5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f4b4c",
      "DATA",
      [
        "storage",
        "00c7b680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f4ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4acc.md#insn-007f4ae0) · [`007f4af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4acc.md#insn-007f4af0)
- 新版 `007f4b38`（命令位置の公開資料なし） · `007f4b48`（命令位置の公開資料なし）

~~~diff
- 007f4ae0 ["INT_ADD", "register:40f0:8", ["const:7f4ae0:8", "const:4:8"]]
- 007f4ae0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f4b38 ["INT_ADD", "register:40f0:8", ["const:7f4b38:8", "const:4:8"]]
+ 007f4b38 ["CALL", null, ["callee:00c57f60:8"]]
- 007f4ae0 bytes ec8c1194
+ 007f4b38 bytes 0a8d1194
- 007f4af0 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 007f4af0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f4af0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f4af0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f4b48 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 007f4b48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4b48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4b48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f4af0 bytes 08c11691
+ 007f4b48 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-619e7e9161e3495a5165cf5f5210f3a6"></a>

### [`007f4b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4b0c.md) → [`007f4b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f4b64.md) FUN_007f4b64

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f4b68",
      "incomplete_value": false,
      "site": "007f4b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f4b10",
      "incomplete_value": false,
      "site": "007f4b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
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
      "007f4b6c",
      "DATA",
      [
        "storage",
        "00c7b5b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f4b6c",
      "DATA",
      [
        "storage",
        "00c7b680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f4b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4b0c.md#insn-007f4b10)
- 新版 `007f4b68`（命令位置の公開資料なし）

~~~diff
- 007f4b10 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 007f4b10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f4b10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f4b10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f4b68 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 007f4b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f4b10 bytes 08c11691
+ 007f4b68 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ef29b42f48dd359c12e11c1949040ea"></a>

### [`007f4b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4b34.md) → [`007f4b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f4/007f4b8c.md) FUN_007f4b8c

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.36% / 新版 95.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f4c90",
      "incomplete_value": true,
      "site": "007f4ca0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:92f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f4c38",
      "incomplete_value": true,
      "site": "007f4c48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:98b:8"
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
      "definition_site": "007f4c94",
      "incomplete_value": true,
      "site": "007f4ca4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007f4c3c",
      "incomplete_value": true,
      "site": "007f4c4c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007f4e9c",
      "incomplete_value": true,
      "site": "007f4e9c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:2fd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f4e44",
      "incomplete_value": true,
      "site": "007f4e44",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:34a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007f4be4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f4bf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "007f4c90",
      "READ",
      [
        "storage",
        "002ab98b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f4be4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f4bf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "007f4c90",
      "READ",
      [
        "storage",
        "002ab92f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f4b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4b34.md#insn-007f4b8c) · [`007f4b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4b34.md#insn-007f4b9c) · [`007f4e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4b34.md#insn-007f4e28)
- 新版 `007f4be4`（命令位置の公開資料なし） · `007f4bf4`（命令位置の公開資料なし） · `007f4e80`（命令位置の公開資料なし）

~~~diff
- 007f4b8c ["INT_ADD", "register:40f0:8", ["const:7f4b8c:8", "const:4:8"]]
- 007f4b8c ["CALL", null, ["ram:47acf4:8"]]
+ 007f4be4 ["INT_ADD", "register:40f0:8", ["const:7f4be4:8", "const:4:8"]]
+ 007f4be4 ["CALL", null, ["ram:47ad34:8"]]
- 007f4b8c bytes 5a18f297
+ 007f4be4 bytes 5418f297
- 007f4b9c ["INT_ADD", "register:40f0:8", ["const:7f4b9c:8", "const:4:8"]]
- 007f4b9c ["CALL", null, ["ram:71bed8:8"]]
+ 007f4bf4 ["INT_ADD", "register:40f0:8", ["const:7f4bf4:8", "const:4:8"]]
+ 007f4bf4 ["CALL", null, ["ram:71bf30:8"]]
- 007f4b9c bytes cf9cfc97
+ 007f4bf4 bytes cf9cfc97
- 007f4e28 ["COPY", "tmp:0:8", ["const:34a:8"]]
- 007f4e28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f4e28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f4e28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f4e80 ["COPY", "tmp:0:8", ["const:2fd:8"]]
+ 007f4e80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f4e80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f4e80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f4e28 bytes 29290d91
+ 007f4e80 bytes 29f50b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b0785b2cccb21a0c8a0055221afa94c"></a>

### [`007f5214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5214.md) → [`007f526c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f526c.md) FUN_007f526c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f528c",
      "incomplete_value": true,
      "site": "007f5290",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5234",
      "incomplete_value": true,
      "site": "007f5238",
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
            "const:620:8"
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
      "007f5290",
      "DATA",
      [
        "storage",
        "00c7b620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5290",
      "DATA",
      [
        "storage",
        "00c7b6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5214.md#insn-007f5228) · [`007f5234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5214.md#insn-007f5234)
- 新版 `007f5280`（命令位置の公開資料なし） · `007f528c`（命令位置の公開資料なし）

~~~diff
- 007f5228 ["INT_ADD", "register:40f0:8", ["const:7f5228:8", "const:4:8"]]
- 007f5228 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f5280 ["INT_ADD", "register:40f0:8", ["const:7f5280:8", "const:4:8"]]
+ 007f5280 ["CALL", null, ["callee:00c57f60:8"]]
- 007f5228 bytes 1a8b1194
+ 007f5280 bytes 388b1194
- 007f5234 ["COPY", "tmp:0:8", ["const:620:8"]]
- 007f5234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f5234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f5234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f528c ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 007f528c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f528c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f528c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f5234 bytes 08811891
+ 007f528c bytes 08c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-073f40c3953fc5365c344cbc6a014890"></a>

### [`007f524c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f524c.md) → [`007f52a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f52a4.md) FUN_007f52a4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f52a8",
      "incomplete_value": false,
      "site": "007f52ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5250",
      "incomplete_value": false,
      "site": "007f5254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "007f52ac",
      "DATA",
      [
        "storage",
        "00c7b620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f52ac",
      "DATA",
      [
        "storage",
        "00c7b6f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f524c.md#insn-007f5250)
- 新版 `007f52a8`（命令位置の公開資料なし）

~~~diff
- 007f5250 ["COPY", "tmp:0:8", ["const:620:8"]]
- 007f5250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f5250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f5250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f52a8 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 007f52a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f52a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f52a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f5250 bytes 08811891
+ 007f52a8 bytes 08c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0964fb3603c0c37cafd21b01848bbee3"></a>

### [`007f569c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f569c.md) → [`007f56f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f56f4.md) FUN_007f56f4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f5708",
      "incomplete_value": false,
      "site": "007f570c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f56b0",
      "incomplete_value": false,
      "site": "007f56b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "007f570c",
      "DATA",
      [
        "storage",
        "00c7b6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f570c",
      "DATA",
      [
        "storage",
        "00c7b780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f56a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f569c.md#insn-007f56a8) · [`007f56b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f569c.md#insn-007f56b0)
- 新版 `007f5700`（命令位置の公開資料なし） · `007f5708`（命令位置の公開資料なし）

~~~diff
- 007f56a8 ["INT_ADD", "register:40f0:8", ["const:7f56a8:8", "const:4:8"]]
- 007f56a8 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f5700 ["INT_ADD", "register:40f0:8", ["const:7f5700:8", "const:4:8"]]
+ 007f5700 ["CALL", null, ["callee:00c57f60:8"]]
- 007f56a8 bytes fa891194
+ 007f5700 bytes 188a1194
- 007f56b0 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 007f56b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f56b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f56b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f5708 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 007f5708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f56b0 bytes 08c11a91
+ 007f5708 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cc7d3d62543a0e6b59aa86683f3c75e"></a>

### [`007f56c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f56c0.md) → [`007f5718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5718.md) FUN_007f5718

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f571c",
      "incomplete_value": false,
      "site": "007f5720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f56c4",
      "incomplete_value": false,
      "site": "007f56c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "007f5720",
      "DATA",
      [
        "storage",
        "00c7b6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5720",
      "DATA",
      [
        "storage",
        "00c7b780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f56c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f56c0.md#insn-007f56c4)
- 新版 `007f571c`（命令位置の公開資料なし）

~~~diff
- 007f56c4 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 007f56c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f56c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f56c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f571c ["COPY", "tmp:0:8", ["const:780:8"]]
+ 007f571c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f571c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f571c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f56c4 bytes 08c11a91
+ 007f571c bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f4b56cb5a7059e03400aa1ee258f6f2"></a>

### [`007f56d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f56d8.md) → [`007f5730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5730.md) FUN_007f5730

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046af4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af4c.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md) [`008b92e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92e8.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f5778",
      "incomplete_value": true,
      "site": "007f5778",
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
      "definition_site": "007f5720",
      "incomplete_value": true,
      "site": "007f5720",
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
      "definition_site": "007f5780",
      "incomplete_value": false,
      "site": "007f5790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5728",
      "incomplete_value": false,
      "site": "007f5738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "definition_site": "007f5788",
      "incomplete_value": false,
      "site": "007f5790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5730",
      "incomplete_value": false,
      "site": "007f5738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "007f5774",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5780",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5788",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f5774",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5780",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5788",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f56d8.md#insn-007f5738) · [`007f5844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f56d8.md#insn-007f5844) · [`007f5710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f56d8.md#insn-007f5710)
- 新版 `007f5790`（命令位置の公開資料なし） · `007f589c`（命令位置の公開資料なし） · `007f5768`（命令位置の公開資料なし）

~~~diff
- 007f5738 ["INT_ADD", "register:40f0:8", ["const:7f5738:8", "const:4:8"]]
- 007f5738 ["CALL", null, ["callee:00c586e0:8"]]
+ 007f5790 ["INT_ADD", "register:40f0:8", ["const:7f5790:8", "const:4:8"]]
+ 007f5790 ["CALL", null, ["callee:00c586e0:8"]]
- 007f5738 bytes b68b1194
+ 007f5790 bytes d48b1194
- 007f5844 ["INT_ADD", "register:40f0:8", ["const:7f5844:8", "const:4:8"]]
- 007f5844 ["CALL", null, ["ram:71bed8:8"]]
+ 007f589c ["INT_ADD", "register:40f0:8", ["const:7f589c:8", "const:4:8"]]
+ 007f589c ["CALL", null, ["ram:71bf30:8"]]
- 007f5844 bytes a599fc97
+ 007f589c bytes a599fc97
- 007f5710 ["INT_ADD", "register:40f0:8", ["const:7f5710:8", "const:4:8"]]
- 007f5710 ["CALL", null, ["callee:008b92e8:8"]]
+ 007f5768 ["INT_ADD", "register:40f0:8", ["const:7f5768:8", "const:4:8"]]
+ 007f5768 ["CALL", null, ["callee:008b92e8:8"]]
- 007f5710 bytes e00e0394
+ 007f5768 bytes e00e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4278316fbb862c68fdca282690e30adb"></a>

### [`007f58dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f58dc.md) → [`007f5934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5934.md) FUN_007f5934

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f5958",
      "incomplete_value": false,
      "site": "007f5958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5900",
      "incomplete_value": false,
      "site": "007f5900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f5958",
      "DATA",
      [
        "storage",
        "00c7b730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5958",
      "DATA",
      [
        "storage",
        "00c7b800",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f58f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f58dc.md#insn-007f58f0) · [`007f58fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f58dc.md#insn-007f58fc)
- 新版 `007f5948`（命令位置の公開資料なし） · `007f5954`（命令位置の公開資料なし）

~~~diff
- 007f58f0 ["INT_ADD", "register:40f0:8", ["const:7f58f0:8", "const:4:8"]]
- 007f58f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f5948 ["INT_ADD", "register:40f0:8", ["const:7f5948:8", "const:4:8"]]
+ 007f5948 ["CALL", null, ["callee:00c57f60:8"]]
- 007f58f0 bytes 68891194
+ 007f5948 bytes 86891194
- 007f58fc ["COPY", "tmp:0:8", ["const:730:8"]]
- 007f58fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f58fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f58fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f5954 ["COPY", "tmp:0:8", ["const:800:8"]]
+ 007f5954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f58fc bytes 08c11c91
+ 007f5954 bytes 08012091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b1e2f019d816cc4622abb344d05353e"></a>

### [`007f5910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5910.md) → [`007f5968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5968.md) FUN_007f5968

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f5974",
      "incomplete_value": false,
      "site": "007f5974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:800:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f591c",
      "incomplete_value": false,
      "site": "007f591c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f5974",
      "DATA",
      [
        "storage",
        "00c7b730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5974",
      "DATA",
      [
        "storage",
        "00c7b800",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5910.md#insn-007f5918)
- 新版 `007f5970`（命令位置の公開資料なし）

~~~diff
- 007f5918 ["COPY", "tmp:0:8", ["const:730:8"]]
- 007f5918 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f5918 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f5918 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f5970 ["COPY", "tmp:0:8", ["const:800:8"]]
+ 007f5970 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f5970 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f5970 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f5918 bytes 29c11c91
+ 007f5970 bytes 29012091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b944a72e06e787a3e8bcd4a86abf9d4"></a>

### [`007f592c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f592c.md) → [`007f5984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5984.md) FUN_007f5984

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

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
      "site": "007f59e0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f5988",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f59e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f59e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f592c.md#insn-007f5988) · [`007f5994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f592c.md#insn-007f5994)
- 新版 `007f59e0`（命令位置の公開資料なし） · `007f59ec`（命令位置の公開資料なし）

~~~diff
- 007f5988 ["INT_ADD", "register:40f0:8", ["const:7f5988:8", "const:4:8"]]
- 007f5988 ["CALL", null, ["ram:47acf4:8"]]
+ 007f59e0 ["INT_ADD", "register:40f0:8", ["const:7f59e0:8", "const:4:8"]]
+ 007f59e0 ["CALL", null, ["ram:47ad34:8"]]
- 007f5988 bytes db14f297
+ 007f59e0 bytes d514f297
- 007f5994 ["INT_ADD", "register:40f0:8", ["const:7f5994:8", "const:4:8"]]
- 007f5994 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f59ec ["INT_ADD", "register:40f0:8", ["const:7f59ec:8", "const:4:8"]]
+ 007f59ec ["CALL", null, ["callee:0047ce14:8"]]
- 007f5994 bytes 101df297
+ 007f59ec bytes 0a1df297
~~~


<a id="compare-7ad2e70d9dc96a1cb414de25d863153d"></a>

### [`007f59e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f59e0.md) → [`007f5a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5a38.md) FUN_007f5a38

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f5a4c",
      "incomplete_value": false,
      "site": "007f5a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f59f4",
      "incomplete_value": false,
      "site": "007f59f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
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
      "007f5a50",
      "DATA",
      [
        "storage",
        "00c7b7b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5a50",
      "DATA",
      [
        "storage",
        "00c7b880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f59ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f59e0.md#insn-007f59ec) · [`007f59f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f59e0.md#insn-007f59f4)
- 新版 `007f5a44`（命令位置の公開資料なし） · `007f5a4c`（命令位置の公開資料なし）

~~~diff
- 007f59ec ["INT_ADD", "register:40f0:8", ["const:7f59ec:8", "const:4:8"]]
- 007f59ec ["CALL", null, ["callee:00c57f60:8"]]
+ 007f5a44 ["INT_ADD", "register:40f0:8", ["const:7f5a44:8", "const:4:8"]]
+ 007f5a44 ["CALL", null, ["callee:00c57f60:8"]]
- 007f59ec bytes 29891194
+ 007f5a44 bytes 47891194
- 007f59f4 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 007f59f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f59f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f59f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f5a4c ["COPY", "tmp:0:8", ["const:880:8"]]
+ 007f5a4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5a4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5a4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f59f4 bytes 08c11e91
+ 007f5a4c bytes 08012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdad4b4973d6bbbfca295af31fcb1853"></a>

### [`007f5a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5a04.md) → [`007f5a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5a5c.md) FUN_007f5a5c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f5a60",
      "incomplete_value": false,
      "site": "007f5a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5a08",
      "incomplete_value": false,
      "site": "007f5a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f5a64",
      "DATA",
      [
        "storage",
        "00c7b7b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5a64",
      "DATA",
      [
        "storage",
        "00c7b880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5a04.md#insn-007f5a08)
- 新版 `007f5a60`（命令位置の公開資料なし）

~~~diff
- 007f5a08 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 007f5a08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f5a08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f5a08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f5a60 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 007f5a60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5a60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5a60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f5a08 bytes 08c11e91
+ 007f5a60 bytes 08012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1218a78922e6f12eb76c083c5145c5f"></a>

### [`007f5a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5a1c.md) → [`007f5a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5a74.md) FUN_007f5a74

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "site": "007f5a98",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f5a40",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f5a98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f5a98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5a1c.md#insn-007f5a40) · [`007f5a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5a1c.md#insn-007f5a4c)
- 新版 `007f5a98`（命令位置の公開資料なし） · `007f5aa4`（命令位置の公開資料なし）

~~~diff
- 007f5a40 ["INT_ADD", "register:40f0:8", ["const:7f5a40:8", "const:4:8"]]
- 007f5a40 ["CALL", null, ["ram:47acf4:8"]]
+ 007f5a98 ["INT_ADD", "register:40f0:8", ["const:7f5a98:8", "const:4:8"]]
+ 007f5a98 ["CALL", null, ["ram:47ad34:8"]]
- 007f5a40 bytes ad14f297
+ 007f5a98 bytes a714f297
- 007f5a4c ["INT_ADD", "register:40f0:8", ["const:7f5a4c:8", "const:4:8"]]
- 007f5a4c ["CALL", null, ["callee:0047ce14:8"]]
+ 007f5aa4 ["INT_ADD", "register:40f0:8", ["const:7f5aa4:8", "const:4:8"]]
+ 007f5aa4 ["CALL", null, ["callee:0047ce14:8"]]
- 007f5a4c bytes e21cf297
+ 007f5aa4 bytes dc1cf297
~~~


<a id="compare-5e310818e95beaece6b4a579440d9c81"></a>

### [`007f5a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5a90.md) → [`007f5ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5ae8.md) FUN_007f5ae8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f5b0c",
      "incomplete_value": false,
      "site": "007f5b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5ab4",
      "incomplete_value": false,
      "site": "007f5ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "007f5b0c",
      "DATA",
      [
        "storage",
        "00c7b830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5b0c",
      "DATA",
      [
        "storage",
        "00c7b900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5a90.md#insn-007f5aa4) · [`007f5ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5a90.md#insn-007f5ab0)
- 新版 `007f5afc`（命令位置の公開資料なし） · `007f5b08`（命令位置の公開資料なし）

~~~diff
- 007f5aa4 ["INT_ADD", "register:40f0:8", ["const:7f5aa4:8", "const:4:8"]]
- 007f5aa4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f5afc ["INT_ADD", "register:40f0:8", ["const:7f5afc:8", "const:4:8"]]
+ 007f5afc ["CALL", null, ["callee:00c57f60:8"]]
- 007f5aa4 bytes fb881194
+ 007f5afc bytes 19891194
- 007f5ab0 ["COPY", "tmp:0:8", ["const:830:8"]]
- 007f5ab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f5ab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f5ab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f5b08 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 007f5b08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5b08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5b08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f5ab0 bytes 08c12091
+ 007f5b08 bytes 08012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b70a40a17d22b65ef5897af6a653df58"></a>

### [`007f5ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5ac4.md) → [`007f5b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5b1c.md) FUN_007f5b1c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f5b28",
      "incomplete_value": false,
      "site": "007f5b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5ad0",
      "incomplete_value": false,
      "site": "007f5ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "007f5b28",
      "DATA",
      [
        "storage",
        "00c7b830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5b28",
      "DATA",
      [
        "storage",
        "00c7b900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5ac4.md#insn-007f5acc)
- 新版 `007f5b24`（命令位置の公開資料なし）

~~~diff
- 007f5acc ["COPY", "tmp:0:8", ["const:830:8"]]
- 007f5acc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f5acc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f5acc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f5b24 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 007f5b24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f5b24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f5b24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f5acc bytes 29c12091
+ 007f5b24 bytes 29012491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e944bb3089f145ea8fa6bd90ff73b08f"></a>

### [`007f5ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5ae0.md) → [`007f5b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5b38.md) FUN_007f5b38

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00468c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468c1c.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046af4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af4c.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.20% / 新版 97.20%

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
      "definition_site": "007f5b7c",
      "incomplete_value": true,
      "site": "007f5b7c",
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
      "definition_site": "007f5b24",
      "incomplete_value": true,
      "site": "007f5b24",
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
      "definition_site": "007f5b84",
      "incomplete_value": false,
      "site": "007f5b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5b2c",
      "incomplete_value": false,
      "site": "007f5b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "definition_site": "007f5b8c",
      "incomplete_value": false,
      "site": "007f5b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5b34",
      "incomplete_value": false,
      "site": "007f5b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "007f5b70",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5b84",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5b8c",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f5b70",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5b84",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5b8c",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5ae0.md#insn-007f5b3c) · [`007f5b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5ae0.md#insn-007f5b18) · [`007f5b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5ae0.md#insn-007f5b2c)
- 新版 `007f5b94`（命令位置の公開資料なし） · `007f5b70`（命令位置の公開資料なし） · `007f5b84`（命令位置の公開資料なし）

~~~diff
- 007f5b3c ["INT_ADD", "register:40f0:8", ["const:7f5b3c:8", "const:4:8"]]
- 007f5b3c ["CALL", null, ["callee:00c586e0:8"]]
+ 007f5b94 ["INT_ADD", "register:40f0:8", ["const:7f5b94:8", "const:4:8"]]
+ 007f5b94 ["CALL", null, ["callee:00c586e0:8"]]
- 007f5b3c bytes b58a1194
+ 007f5b94 bytes d38a1194
- 007f5b18 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:978:8"]]
- 007f5b18 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f5b70 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 007f5b70 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007f5b18 bytes 20bd44f9
+ 007f5b70 bytes 203d45f9
- 007f5b2c ["COPY", "tmp:0:8", ["const:e58:8"]]
- 007f5b2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f5b2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f5b2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f5b84 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 007f5b84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f5b84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f5b84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f5b2c bytes 21603991
+ 007f5b84 bytes 21a03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2f6201a7bf94e25e752836dee4dd08f"></a>

### [`007f5e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5e64.md) → [`007f5ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5ebc.md) FUN_007f5ebc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f5ee0",
      "incomplete_value": false,
      "site": "007f5ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5e88",
      "incomplete_value": false,
      "site": "007f5e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
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
      "007f5ee0",
      "DATA",
      [
        "storage",
        "00c7b8b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5ee0",
      "DATA",
      [
        "storage",
        "00c7b980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5e64.md#insn-007f5e78) · [`007f5e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5e64.md#insn-007f5e84)
- 新版 `007f5ed0`（命令位置の公開資料なし） · `007f5edc`（命令位置の公開資料なし）

~~~diff
- 007f5e78 ["INT_ADD", "register:40f0:8", ["const:7f5e78:8", "const:4:8"]]
- 007f5e78 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f5ed0 ["INT_ADD", "register:40f0:8", ["const:7f5ed0:8", "const:4:8"]]
+ 007f5ed0 ["CALL", null, ["callee:00c57f60:8"]]
- 007f5e78 bytes 06881194
+ 007f5ed0 bytes 24881194
- 007f5e84 ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 007f5e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f5e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f5e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f5edc ["COPY", "tmp:0:8", ["const:980:8"]]
+ 007f5edc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5edc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5edc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f5e84 bytes 08c12291
+ 007f5edc bytes 08012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-827e91c73c962b4dc423c63b91a22b44"></a>

### [`007f5e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5e98.md) → [`007f5ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5ef0.md) FUN_007f5ef0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f5efc",
      "incomplete_value": false,
      "site": "007f5efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5ea4",
      "incomplete_value": false,
      "site": "007f5ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
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
      "007f5efc",
      "DATA",
      [
        "storage",
        "00c7b8b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5efc",
      "DATA",
      [
        "storage",
        "00c7b980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5e98.md#insn-007f5ea0)
- 新版 `007f5ef8`（命令位置の公開資料なし）

~~~diff
- 007f5ea0 ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 007f5ea0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f5ea0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f5ea0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f5ef8 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 007f5ef8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f5ef8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f5ef8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f5ea0 bytes 29c12291
+ 007f5ef8 bytes 29012691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36f1f346d31c4abb1e274ca93fd5f7c5"></a>

### [`007f5eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5eb4.md) → [`007f5f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5f0c.md) FUN_007f5f0c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

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
      "site": "007f5f54",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f5efc",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f5f54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f5f54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5eb4.md#insn-007f5efc) · [`007f5f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5eb4.md#insn-007f5f08)
- 新版 `007f5f54`（命令位置の公開資料なし） · `007f5f60`（命令位置の公開資料なし）

~~~diff
- 007f5efc ["INT_ADD", "register:40f0:8", ["const:7f5efc:8", "const:4:8"]]
- 007f5efc ["CALL", null, ["ram:47acf4:8"]]
+ 007f5f54 ["INT_ADD", "register:40f0:8", ["const:7f5f54:8", "const:4:8"]]
+ 007f5f54 ["CALL", null, ["ram:47ad34:8"]]
- 007f5efc bytes 7e13f297
+ 007f5f54 bytes 7813f297
- 007f5f08 ["INT_ADD", "register:40f0:8", ["const:7f5f08:8", "const:4:8"]]
- 007f5f08 ["CALL", null, ["callee:0047ce14:8"]]
+ 007f5f60 ["INT_ADD", "register:40f0:8", ["const:7f5f60:8", "const:4:8"]]
+ 007f5f60 ["CALL", null, ["callee:0047ce14:8"]]
- 007f5f08 bytes b31bf297
+ 007f5f60 bytes ad1bf297
~~~


<a id="compare-a26e3569c76fce3dad0476d88b0d266f"></a>

### [`007f5f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5f48.md) → [`007f5fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5fa0.md) FUN_007f5fa0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f5fc4",
      "incomplete_value": false,
      "site": "007f5fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f5f6c",
      "incomplete_value": false,
      "site": "007f5f6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "007f5fc4",
      "DATA",
      [
        "storage",
        "00c7b930",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5fc4",
      "DATA",
      [
        "storage",
        "00c7ba00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5f48.md#insn-007f5f5c) · [`007f5f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5f48.md#insn-007f5f68)
- 新版 `007f5fb4`（命令位置の公開資料なし） · `007f5fc0`（命令位置の公開資料なし）

~~~diff
- 007f5f5c ["INT_ADD", "register:40f0:8", ["const:7f5f5c:8", "const:4:8"]]
- 007f5f5c ["CALL", null, ["callee:00c57f60:8"]]
+ 007f5fb4 ["INT_ADD", "register:40f0:8", ["const:7f5fb4:8", "const:4:8"]]
+ 007f5fb4 ["CALL", null, ["callee:00c57f60:8"]]
- 007f5f5c bytes cd871194
+ 007f5fb4 bytes eb871194
- 007f5f68 ["COPY", "tmp:0:8", ["const:930:8"]]
- 007f5f68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f5f68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f5f68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f5fc0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 007f5fc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5fc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5fc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f5f68 bytes 08c12491
+ 007f5fc0 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b9018f3b30fde1d60b49c35e0c9d1de"></a>

### [`007f5f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5f98.md) → [`007f5ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f5/007f5ff0.md) FUN_007f5ff0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00468c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468c1c.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007f6014",
      "incomplete_value": true,
      "site": "007f6014",
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
      "definition_site": "007f5fbc",
      "incomplete_value": true,
      "site": "007f5fbc",
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
      "007f600c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007f601c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6024",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f600c",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "007f601c",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f6024",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5f98.md#insn-007f5fb4) · [`007f5fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5f98.md#insn-007f5fc4) · [`007f5fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5f98.md#insn-007f5fcc)
- 新版 `007f600c`（命令位置の公開資料なし） · `007f601c`（命令位置の公開資料なし） · `007f6024`（命令位置の公開資料なし）

~~~diff
- 007f5fb4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:978:8"]]
- 007f5fb4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f600c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 007f600c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007f5fb4 bytes 20bd44f9
+ 007f600c bytes 203d45f9
- 007f5fc4 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 007f5fc4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007f5fc4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007f5fc4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007f601c ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 007f601c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007f601c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007f601c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007f5fc4 bytes 21603991
+ 007f601c bytes 21a03c91
- 007f5fcc ["COPY", "tmp:0:8", ["const:990:8"]]
- 007f5fcc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007f5fcc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007f5fcc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007f6024 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 007f6024 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007f6024 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007f6024 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007f5fcc bytes 42402691
+ 007f6024 bytes 42802991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fbe891c4ad3cb05bad0f84e53f47aac"></a>

### [`007f60e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f60e8.md) → [`007f6140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6140.md) FUN_007f6140

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f6154",
      "incomplete_value": false,
      "site": "007f6158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f60fc",
      "incomplete_value": false,
      "site": "007f6100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
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
      "007f6158",
      "DATA",
      [
        "storage",
        "00c7b9b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f6158",
      "DATA",
      [
        "storage",
        "00c7ba80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f60f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f60e8.md#insn-007f60f4) · [`007f60fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f60e8.md#insn-007f60fc)
- 新版 `007f614c`（命令位置の公開資料なし） · `007f6154`（命令位置の公開資料なし）

~~~diff
- 007f60f4 ["INT_ADD", "register:40f0:8", ["const:7f60f4:8", "const:4:8"]]
- 007f60f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f614c ["INT_ADD", "register:40f0:8", ["const:7f614c:8", "const:4:8"]]
+ 007f614c ["CALL", null, ["callee:00c57f60:8"]]
- 007f60f4 bytes 67871194
+ 007f614c bytes 85871194
- 007f60fc ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 007f60fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f60fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f60fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f6154 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 007f6154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f60fc bytes 08c12691
+ 007f6154 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edb8e5582b301a9ae542b0860443a95d"></a>

### [`007f610c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f610c.md) → [`007f6164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6164.md) FUN_007f6164

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f6168",
      "incomplete_value": false,
      "site": "007f616c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6110",
      "incomplete_value": false,
      "site": "007f6114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
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
      "007f616c",
      "DATA",
      [
        "storage",
        "00c7b9b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f616c",
      "DATA",
      [
        "storage",
        "00c7ba80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f610c.md#insn-007f6110)
- 新版 `007f6168`（命令位置の公開資料なし）

~~~diff
- 007f6110 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 007f6110 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f6110 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f6110 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f6168 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 007f6168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f6110 bytes 08c12691
+ 007f6168 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29569994868cc4de4ba708a0d736f7ac"></a>

### [`007f6124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6124.md) → [`007f617c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f617c.md) FUN_007f617c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "007f6198",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f6140",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f6198",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "007f6198",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6124.md#insn-007f6140) · [`007f614c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6124.md#insn-007f614c)
- 新版 `007f6198`（命令位置の公開資料なし） · `007f61a4`（命令位置の公開資料なし）

~~~diff
- 007f6140 ["INT_ADD", "register:40f0:8", ["const:7f6140:8", "const:4:8"]]
- 007f6140 ["CALL", null, ["ram:47acf4:8"]]
+ 007f6198 ["INT_ADD", "register:40f0:8", ["const:7f6198:8", "const:4:8"]]
+ 007f6198 ["CALL", null, ["ram:47ad34:8"]]
- 007f6140 bytes ed12f297
+ 007f6198 bytes e712f297
- 007f614c ["INT_ADD", "register:40f0:8", ["const:7f614c:8", "const:4:8"]]
- 007f614c ["CALL", null, ["callee:0047ce14:8"]]
+ 007f61a4 ["INT_ADD", "register:40f0:8", ["const:7f61a4:8", "const:4:8"]]
+ 007f61a4 ["CALL", null, ["callee:0047ce14:8"]]
- 007f614c bytes 221bf297
+ 007f61a4 bytes 1c1bf297
~~~


<a id="compare-bb738a74d75da4d886ca2f4aead80c2b"></a>

### [`007f6190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6190.md) → [`007f61e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f61e8.md) FUN_007f61e8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f620c",
      "incomplete_value": false,
      "site": "007f620c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f61b4",
      "incomplete_value": false,
      "site": "007f61b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f620c",
      "DATA",
      [
        "storage",
        "00c7ba30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f620c",
      "DATA",
      [
        "storage",
        "00c7bb00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f61a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6190.md#insn-007f61a4) · [`007f61b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6190.md#insn-007f61b0)
- 新版 `007f61fc`（命令位置の公開資料なし） · `007f6208`（命令位置の公開資料なし）

~~~diff
- 007f61a4 ["INT_ADD", "register:40f0:8", ["const:7f61a4:8", "const:4:8"]]
- 007f61a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f61fc ["INT_ADD", "register:40f0:8", ["const:7f61fc:8", "const:4:8"]]
+ 007f61fc ["CALL", null, ["callee:00c57f60:8"]]
- 007f61a4 bytes 3b871194
+ 007f61fc bytes 59871194
- 007f61b0 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 007f61b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f61b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f61b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f6208 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 007f6208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f6208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f61b0 bytes 08c12891
+ 007f6208 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c86eb52e93971d1686c7fae5d33a955"></a>

### [`007f61c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f61c4.md) → [`007f621c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f621c.md) FUN_007f621c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f6228",
      "incomplete_value": false,
      "site": "007f6228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f61d0",
      "incomplete_value": false,
      "site": "007f61d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f6228",
      "DATA",
      [
        "storage",
        "00c7ba30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f6228",
      "DATA",
      [
        "storage",
        "00c7bb00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f61cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f61c4.md#insn-007f61cc)
- 新版 `007f6224`（命令位置の公開資料なし）

~~~diff
- 007f61cc ["COPY", "tmp:0:8", ["const:a30:8"]]
- 007f61cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f61cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f61cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f6224 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 007f6224 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f6224 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f6224 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f61cc bytes 29c12891
+ 007f6224 bytes 29012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18b18b8d012cd15ee306ba92260b0877"></a>

### [`007f61e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f61e0.md) → [`007f6238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6238.md) FUN_007f6238

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007f64fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f64fc.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`007f6554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6554.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.28% / 新版 93.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007f634c",
      "incomplete_value": true,
      "site": "007f6360",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:536:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f62f4",
      "incomplete_value": true,
      "site": "007f6308",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6380",
      "incomplete_value": false,
      "site": "007f6380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f6328",
      "incomplete_value": false,
      "site": "007f6328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f6278",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f6220",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f6278",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f6294",
      "READ",
      [
        "storage",
        "00c9b4d0",
        null,
        "pointer"
      ]
    ],
    [
      "007f62ac",
      "READ",
      [
        "storage",
        "00ca418c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "007f6278",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f6294",
      "READ",
      [
        "storage",
        "00c9b5a0",
        null,
        "pointer"
      ]
    ],
    [
      "007f62ac",
      "READ",
      [
        "storage",
        "00ca425c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f61e0.md#insn-007f6220) · [`007f622c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f61e0.md#insn-007f622c) · [`007f623c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f61e0.md#insn-007f623c)
- 新版 `007f6278`（命令位置の公開資料なし） · `007f6284`（命令位置の公開資料なし） · `007f6294`（命令位置の公開資料なし）

~~~diff
- 007f6220 ["INT_ADD", "register:40f0:8", ["const:7f6220:8", "const:4:8"]]
- 007f6220 ["CALL", null, ["ram:47acf4:8"]]
+ 007f6278 ["INT_ADD", "register:40f0:8", ["const:7f6278:8", "const:4:8"]]
+ 007f6278 ["CALL", null, ["ram:47ad34:8"]]
- 007f6220 bytes b512f297
+ 007f6278 bytes af12f297
- 007f622c ["INT_ADD", "register:40f0:8", ["const:7f622c:8", "const:4:8"]]
- 007f622c ["CALL", null, ["callee:0047ce14:8"]]
+ 007f6284 ["INT_ADD", "register:40f0:8", ["const:7f6284:8", "const:4:8"]]
+ 007f6284 ["CALL", null, ["callee:0047ce14:8"]]
- 007f622c bytes ea1af297
+ 007f6284 bytes e41af297
- 007f623c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4d0:8"]]
- 007f623c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f6294 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5a0:8"]]
+ 007f6294 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 007f623c bytes 296942f9
+ 007f6294 bytes 29d142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841accf75de06cb832fbb51b85b759a3"></a>

### [`007f64b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f64b4.md) → [`007f650c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f650c.md) FUN_007f650c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "007f6530",
      "incomplete_value": false,
      "site": "007f6530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f64d8",
      "incomplete_value": false,
      "site": "007f64d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
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
      "007f6530",
      "DATA",
      [
        "storage",
        "00c7baa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f6530",
      "DATA",
      [
        "storage",
        "00c7bb70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f64c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f64b4.md#insn-007f64c8) · [`007f64d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f64b4.md#insn-007f64d4)
- 新版 `007f6520`（命令位置の公開資料なし） · `007f652c`（命令位置の公開資料なし）

~~~diff
- 007f64c8 ["INT_ADD", "register:40f0:8", ["const:7f64c8:8", "const:4:8"]]
- 007f64c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f6520 ["INT_ADD", "register:40f0:8", ["const:7f6520:8", "const:4:8"]]
+ 007f6520 ["CALL", null, ["callee:00c57f60:8"]]
- 007f64c8 bytes 72861194
+ 007f6520 bytes 90861194
- 007f64d4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 007f64d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f64d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f64d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f652c ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 007f652c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f652c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f652c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f64d4 bytes 08812a91
+ 007f652c bytes 08c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea7abd18316f750906a22417cdc1ea1e"></a>

### [`007f64e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f64e8.md) → [`007f6540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f6540.md) FUN_007f6540

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007f654c",
      "incomplete_value": false,
      "site": "007f654c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f64f4",
      "incomplete_value": false,
      "site": "007f64f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
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
      "007f654c",
      "DATA",
      [
        "storage",
        "00c7baa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f654c",
      "DATA",
      [
        "storage",
        "00c7bb70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f64f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f64e8.md#insn-007f64f0)
- 新版 `007f6548`（命令位置の公開資料なし）

~~~diff
- 007f64f0 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 007f64f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f64f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f64f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f6548 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 007f6548 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f6548 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f6548 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f64f0 bytes 29812a91
+ 007f6548 bytes 29c12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1270191590f58ebce7bb124d5c9cf54"></a>

### [`007f6504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6504.md) → [`007f655c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f655c.md) FUN_007f655c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007f6798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6798.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`007f67f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f6/007f67f0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007f6618",
      "incomplete_value": false,
      "site": "007f6618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007f65c0",
      "incomplete_value": false,
      "site": "007f65c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:b10:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f6598",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f6540",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "007f6598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f65e8",
      "READ",
      [
        "storage",
        "002ba74b",
        null,
        "string"
      ]
    ],
    [
      "007f6618",
      "DATA",
      [
        "storage",
        "00c7bb10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f6598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "007f65e8",
      "READ",
      [
        "storage",
        "002ba6f7",
        null,
        "string"
      ]
    ],
    [
      "007f6618",
      "DATA",
      [
        "storage",
        "00c7bbe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6504.md#insn-007f6540) · [`007f6618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6504.md#insn-007f6618) · [`007f654c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6504.md#insn-007f654c)
- 新版 `007f6598`（命令位置の公開資料なし） · `007f6670`（命令位置の公開資料なし） · `007f65a4`（命令位置の公開資料なし）

~~~diff
- 007f6540 ["INT_ADD", "register:40f0:8", ["const:7f6540:8", "const:4:8"]]
- 007f6540 ["CALL", null, ["ram:47acf4:8"]]
+ 007f6598 ["INT_ADD", "register:40f0:8", ["const:7f6598:8", "const:4:8"]]
+ 007f6598 ["CALL", null, ["ram:47ad34:8"]]
- 007f6540 bytes ed11f297
+ 007f6598 bytes e711f297
- 007f6618 ["INT_ADD", "register:40f0:8", ["const:7f6618:8", "const:4:8"]]
- 007f6618 ["CALL", null, ["callee:008b9558:8"]]
+ 007f6670 ["INT_ADD", "register:40f0:8", ["const:7f6670:8", "const:4:8"]]
+ 007f6670 ["CALL", null, ["callee:008b9558:8"]]
- 007f6618 bytes ba0b0394
+ 007f6670 bytes ba0b0394
- 007f654c ["INT_ADD", "register:40f0:8", ["const:7f654c:8", "const:4:8"]]
- 007f654c ["CALL", null, ["callee:0047ce14:8"]]
+ 007f65a4 ["INT_ADD", "register:40f0:8", ["const:7f65a4:8", "const:4:8"]]
+ 007f65a4 ["CALL", null, ["callee:0047ce14:8"]]
- 007f654c bytes 221af297
+ 007f65a4 bytes 1c1af297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

