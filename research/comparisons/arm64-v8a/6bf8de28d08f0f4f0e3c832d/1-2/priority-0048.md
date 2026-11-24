# v16.0.1 → v16.0.2 · 最優先の変更候補 (48)

[一覧の目次](README.md)

<a id="compare-f6ef3d71264dcd1c55584da1a0674231"></a>

### [`00886914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886914.md) → [`0088696c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/0088696c.md) FUN_0088696c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00886984",
      "incomplete_value": false,
      "site": "00886988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088692c",
      "incomplete_value": false,
      "site": "00886930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "00886988",
      "DATA",
      [
        "storage",
        "00c80f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886988",
      "DATA",
      [
        "storage",
        "00c81008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886914.md#insn-00886928) · [`0088692c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886914.md#insn-0088692c) · [`00886940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886914.md#insn-00886940)
- 新版 [`00886980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/0088696c.md#insn-00886980) · [`00886984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/0088696c.md#insn-00886984) · [`00886998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/0088696c.md#insn-00886998)

~~~diff
- 00886928 ["COPY", "register:4040:8", ["const:c80000:8"]]
+ 00886980 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 00886928 bytes c81f00d0
+ 00886980 bytes c81f00f0
- 0088692c ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0088692c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088692c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088692c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00886984 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 00886984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00886984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00886984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088692c bytes 08e13c91
+ 00886984 bytes 08210091
- 00886940 ["INT_ADD", "register:40f0:8", ["const:886940:8", "const:4:8"]]
- 00886940 ["CALL", null, ["callee:00c53da0:8"]]
+ 00886998 ["INT_ADD", "register:40f0:8", ["const:886998:8", "const:4:8"]]
+ 00886998 ["CALL", null, ["callee:00c53da0:8"]]
- 00886940 bytes f0340f94
+ 00886998 bytes 02350f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3c0450f3246186ef8b58a62b3b2bf24"></a>

### [`00886970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886970.md) → [`008869c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008869c8.md) FUN_008869c8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "008869ec",
      "incomplete_value": true,
      "site": "008869f0",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886994",
      "incomplete_value": true,
      "site": "00886998",
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
      "008869f0",
      "DATA",
      [
        "storage",
        "00c80f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008869f0",
      "DATA",
      [
        "storage",
        "00c81008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886970.md#insn-00886984) · [`00886990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886970.md#insn-00886990) · [`00886994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886970.md#insn-00886994)
- 新版 [`008869dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008869c8.md#insn-008869dc) · [`008869e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008869c8.md#insn-008869e8) · [`008869ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/008869c8.md#insn-008869ec)

~~~diff
- 00886984 ["INT_ADD", "register:40f0:8", ["const:886984:8", "const:4:8"]]
- 00886984 ["CALL", null, ["callee:00c57f60:8"]]
+ 008869dc ["INT_ADD", "register:40f0:8", ["const:8869dc:8", "const:4:8"]]
+ 008869dc ["CALL", null, ["callee:00c57f60:8"]]
- 00886984 bytes 43450f94
+ 008869dc bytes 61450f94
- 00886990 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 008869e8 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00886990 bytes c91f00d0
+ 008869e8 bytes c91f00f0
- 00886994 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 00886994 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886994 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886994 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008869ec ["COPY", "tmp:0:8", ["const:8:8"]]
+ 008869ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008869ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008869ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886994 bytes 29e13c91
+ 008869ec bytes 29210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd013f861626530c78343e561fded90"></a>

### [`008869c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008869c8.md) → [`00886a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886a20.md) FUN_00886a20

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "00886a28",
      "incomplete_value": false,
      "site": "00886a2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008869d0",
      "incomplete_value": false,
      "site": "008869d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "00886a2c",
      "DATA",
      [
        "storage",
        "00c80f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886a2c",
      "DATA",
      [
        "storage",
        "00c81008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008869cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008869c8.md#insn-008869cc) · [`008869d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008869c8.md#insn-008869d0) · [`008869f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/008869c8.md#insn-008869f8)
- 新版 [`00886a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886a20.md#insn-00886a24) · [`00886a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886a20.md#insn-00886a28) · [`00886a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886a20.md#insn-00886a50)

~~~diff
- 008869cc ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00886a24 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 008869cc bytes c91f00d0
+ 00886a24 bytes c91f00f0
- 008869d0 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 008869d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008869d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008869d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00886a28 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 00886a28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00886a28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00886a28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008869d0 bytes 29e13c91
+ 00886a28 bytes 29210091
- 008869f8 ["INT_ADD", "register:40f0:8", ["const:8869f8:8", "const:4:8"]]
- 008869f8 ["CALL", null, ["callee:00c53d70:8"]]
+ 00886a50 ["INT_ADD", "register:40f0:8", ["const:886a50:8", "const:4:8"]]
+ 00886a50 ["CALL", null, ["callee:00c53d70:8"]]
- 008869f8 bytes b6340f94
+ 00886a50 bytes c8340f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f32a84a8f631e667eab1a6e00fcd05d8"></a>

### [`00886aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886aa4.md) → [`00886afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886afc.md) FUN_00886afc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md) [`00886f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f10.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00456848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md) [`004647dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/004647dc.md) [`00886f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f68.md)

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
      "definition_site": "00886c8c",
      "incomplete_value": false,
      "site": "00886c8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886c34",
      "incomplete_value": false,
      "site": "00886c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "00886c8c",
      "DATA",
      [
        "storage",
        "00c80fa8",
        null,
        "undefined *"
      ]
    ],
    [
      "00886ce0",
      "READ",
      [
        "storage",
        "00c80fd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886c8c",
      "DATA",
      [
        "storage",
        "00c81078",
        null,
        "undefined *"
      ]
    ],
    [
      "00886ce0",
      "READ",
      [
        "storage",
        "00c810a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886aa4.md#insn-00886bdc) · [`00886c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886aa4.md#insn-00886c8c) · [`00886bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886aa4.md#insn-00886bc8)
- 新版 [`00886c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886afc.md#insn-00886c34) · [`00886ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886afc.md#insn-00886ce4) · [`00886c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886afc.md#insn-00886c20)

~~~diff
- 00886bdc ["INT_ADD", "register:40f0:8", ["const:886bdc:8", "const:4:8"]]
- 00886bdc ["CALL", null, ["callee:0044f920:8"]]
+ 00886c34 ["INT_ADD", "register:40f0:8", ["const:886c34:8", "const:4:8"]]
+ 00886c34 ["CALL", null, ["callee:0044f920:8"]]
- 00886bdc bytes 4123ef97
+ 00886c34 bytes 3b23ef97
- 00886c8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00886c8c ["INT_ADD", "register:40f0:8", ["const:886c8c:8", "const:4:8"]]
- 00886c8c ["CALLIND", null, ["register:0:8"]]
+ 00886ce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886ce4 ["INT_ADD", "register:40f0:8", ["const:886ce4:8", "const:4:8"]]
+ 00886ce4 ["CALLIND", null, ["register:0:8"]]
- 00886c8c bytes 00013fd6
+ 00886ce4 bytes 00013fd6
- 00886bc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00886bc8 ["INT_ADD", "register:40f0:8", ["const:886bc8:8", "const:4:8"]]
- 00886bc8 ["CALLIND", null, ["register:0:8"]]
+ 00886c20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886c20 ["INT_ADD", "register:40f0:8", ["const:886c20:8", "const:4:8"]]
+ 00886c20 ["CALLIND", null, ["register:0:8"]]
- 00886bc8 bytes 00013fd6
+ 00886c20 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69f3246411a64c1d61594d5f878a5171"></a>

### [`00886de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886de0.md) → [`00886e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e38.md) FUN_00886e38

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00886e40",
      "incomplete_value": false,
      "site": "00886e44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886de8",
      "incomplete_value": false,
      "site": "00886dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "00886e44",
      "DATA",
      [
        "storage",
        "00c80fa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886e44",
      "DATA",
      [
        "storage",
        "00c81078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886de0.md#insn-00886de4) · [`00886de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886de0.md#insn-00886de8)
- 新版 [`00886e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e38.md#insn-00886e3c) · [`00886e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e38.md#insn-00886e40)

~~~diff
- 00886de4 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00886e3c ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00886de4 bytes c91f00d0
+ 00886e3c bytes c91f00f0
- 00886de8 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 00886de8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886de8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886de8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00886e40 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00886e40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00886e40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00886e40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886de8 bytes 29a13e91
+ 00886e40 bytes 29e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6803d8c2d811d1653a4c596797de697a"></a>

### [`00886e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886e00.md) → [`00886e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e58.md) FUN_00886e58

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00886e60",
      "incomplete_value": false,
      "site": "00886e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886e08",
      "incomplete_value": false,
      "site": "00886e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "00886e64",
      "DATA",
      [
        "storage",
        "00c80fa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886e64",
      "DATA",
      [
        "storage",
        "00c81078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886e00.md#insn-00886e04) · [`00886e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886e00.md#insn-00886e08) · [`00886e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886e00.md#insn-00886e2c)
- 新版 [`00886e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e58.md#insn-00886e5c) · [`00886e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e58.md#insn-00886e60) · [`00886e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886e58.md#insn-00886e84)

~~~diff
- 00886e04 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00886e5c ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00886e04 bytes c91f00d0
+ 00886e5c bytes c91f00f0
- 00886e08 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 00886e08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886e08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886e08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00886e60 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00886e60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00886e60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00886e60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886e08 bytes 29a13e91
+ 00886e60 bytes 29e10191
- 00886e2c ["INT_ADD", "register:40f0:8", ["const:886e2c:8", "const:4:8"]]
- 00886e2c ["CALL", null, ["callee:00c57f80:8"]]
+ 00886e84 ["INT_ADD", "register:40f0:8", ["const:886e84:8", "const:4:8"]]
+ 00886e84 ["CALL", null, ["callee:00c57f80:8"]]
- 00886e2c bytes 21440f94
+ 00886e84 bytes 3f440f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d13d10ec26832ab4ea00b6804fc192d"></a>

### [`00886ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886ebc.md) → [`00886f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f14.md) FUN_00886f14

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

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
      "definition_site": "00886f20",
      "incomplete_value": false,
      "site": "00886f20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00886ec8",
      "incomplete_value": false,
      "site": "00886ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
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
      "00886f20",
      "DATA",
      [
        "storage",
        "00c80fa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886f20",
      "DATA",
      [
        "storage",
        "00c81078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886ebc.md#insn-00886ec0) · [`00886ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886ebc.md#insn-00886ec4)
- 新版 [`00886f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f14.md#insn-00886f18) · [`00886f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f14.md#insn-00886f1c)

~~~diff
- 00886ec0 ["COPY", "register:4048:8", ["const:c80000:8"]]
+ 00886f18 ["COPY", "register:4048:8", ["const:c81000:8"]]
- 00886ec0 bytes c91f00d0
+ 00886f18 bytes c91f00f0
- 00886ec4 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 00886ec4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00886ec4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00886ec4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00886f1c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00886f1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00886f1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00886f1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00886ec4 bytes 29a13e91
+ 00886f1c bytes 29e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8286d736a2d0f7a024fdd618f5ae38e0"></a>

### [`008870e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008870e8.md) → [`00887140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887140.md) _INIT_164

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008871a0",
      "incomplete_value": true,
      "site": "008871bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00887148",
      "incomplete_value": true,
      "site": "00887164",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008871c0",
      "incomplete_value": true,
      "site": "008871dc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00887168",
      "incomplete_value": true,
      "site": "00887184",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008871e0",
      "incomplete_value": true,
      "site": "008871f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00887188",
      "incomplete_value": true,
      "site": "008871a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0088717c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "008871a0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "008871c0",
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
      "0088717c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "008871a0",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "008871c0",
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

- 旧版 [`008871bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008870e8.md#insn-008871bc) · [`008871dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008870e8.md#insn-008871dc) · [`0088731c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008870e8.md#insn-0088731c)
- 新版 [`00887214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887140.md#insn-00887214) · [`00887234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887140.md#insn-00887234) · [`00887374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887140.md#insn-00887374)

~~~diff
- 008871bc ["COPY", "tmp:0:8", ["const:f5d:8"]]
- 008871bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008871bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008871bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00887214 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 00887214 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00887214 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00887214 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008871bc bytes 29753d91
+ 00887214 bytes 29413c91
- 008871dc ["COPY", "tmp:0:8", ["const:f09:8"]]
- 008871dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008871dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008871dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00887234 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00887234 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00887234 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00887234 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008871dc bytes 29253c91
+ 00887234 bytes 29f13a91
- 0088731c ["INT_ADD", "register:40f0:8", ["const:88731c:8", "const:4:8"]]
- 0088731c ["CALL", null, ["callee:00c57f00:8"]]
+ 00887374 ["INT_ADD", "register:40f0:8", ["const:887374:8", "const:4:8"]]
+ 00887374 ["CALL", null, ["callee:00c57f00:8"]]
- 0088731c bytes c5420f94
+ 00887374 bytes e3420f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05754447324d87e762d33e28a142eb9d"></a>

### [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) → [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) FUN_008874d0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 10件 [`0088a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a7d0.md) [`0088ad68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ad68.md) [`0088ae8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae8c.md) [`0088afb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088afb0.md) [`0088b0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b0d4.md) · 呼出先 12件 [`00888e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e30.md) [`00888e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e34.md) [`00888e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e7c.md) [`00889030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889030.md) [`00889034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889034.md)
- 新版 呼出元 10件 [`0088a828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a828.md) [`0088adc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088adc0.md) [`0088aee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aee4.md) [`0088b008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b008.md) [`0088b12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b12c.md) · 呼出先 12件 [`00888e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e88.md) [`00888e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e8c.md) [`00888ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888ed4.md) [`00889088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889088.md) [`0088908c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/0088908c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00887504",
      "incomplete_value": false,
      "site": "00887508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008874ac",
      "incomplete_value": false,
      "site": "008874b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "definition_site": "00887540",
      "incomplete_value": false,
      "site": "00887540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008874e8",
      "incomplete_value": false,
      "site": "008874e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "definition_site": "00887590",
      "incomplete_value": false,
      "site": "00887590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00887538",
      "incomplete_value": false,
      "site": "00887538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:280:8"
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
      "00887508",
      "DATA",
      [
        "storage",
        "00c81038",
        null,
        "pointer"
      ]
    ],
    [
      "00887540",
      "DATA",
      [
        "storage",
        "00c811f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00887574",
      "READ",
      [
        "storage",
        "00c81210",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00887508",
      "DATA",
      [
        "storage",
        "00c81108",
        null,
        "pointer"
      ]
    ],
    [
      "00887540",
      "DATA",
      [
        "storage",
        "00c812c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00887574",
      "READ",
      [
        "storage",
        "00c812e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00887540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md#insn-00887540) · [`008874ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md#insn-008874ac) · [`008874b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md#insn-008874b4)
- 新版 [`00887598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md#insn-00887598) · [`00887504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md#insn-00887504)

~~~diff
- 00887540 ["INT_ADD", "register:40f0:8", ["const:887540:8", "const:4:8"]]
- 00887540 ["CALL", null, ["callee:008890c8:8"]]
+ 00887598 ["INT_ADD", "register:40f0:8", ["const:887598:8", "const:4:8"]]
+ 00887598 ["CALL", null, ["callee:008890c8:8"]]
- 00887540 bytes cc060094
+ 00887598 bytes cc060094
- 008874ac ["COPY", "tmp:0:8", ["const:38:8"]]
- 008874ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008874ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008874ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00887504 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00887504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00887504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00887504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008874ac bytes 08e10091
+ 00887504 bytes 08210491
- 008874b4 ["COPY", "register:4040:8", ["const:c81000:8"]]
- 008874b4 bytes c81f00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7f818699575c6470be60a7701202848"></a>

### [`008876f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008876f0.md) → [`00887748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887748.md) FUN_00887748

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 0件 

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
      "definition_site": "0088775c",
      "incomplete_value": false,
      "site": "00887760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:862:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00887704",
      "incomplete_value": false,
      "site": "00887708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:8b6:8"
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
      "00887760",
      "DATA",
      [
        "storage",
        "002ba8b6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00887760",
      "DATA",
      [
        "storage",
        "002ba862",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00887704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008876f0.md#insn-00887704)
- 新版 [`0088775c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887748.md#insn-0088775c)

~~~diff
- 00887704 ["COPY", "tmp:0:8", ["const:8b6:8"]]
- 00887704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00887704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00887704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088775c ["COPY", "tmp:0:8", ["const:862:8"]]
+ 0088775c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088775c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088775c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00887704 bytes 08d92291
+ 0088775c bytes 08892191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf5b95c80d7e036cf4828448f2c3e1e2"></a>

### [`008877e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008877e0.md) → [`00887838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887838.md) FUN_00887838

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00a9add8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9a/00a9add8.md) · 呼出先 4件 [`00889b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889b9c.md) [`00889ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889ba0.md) [`00b373dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b373dc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a9ae48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a9a/00a9ae48.md) · 呼出先 4件 [`00889bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bf4.md) [`00889bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bf8.md) [`00b37478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37478.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "0088786c",
      "incomplete_value": false,
      "site": "0088786c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00887814",
      "incomplete_value": false,
      "site": "00887814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      "0088786c",
      "DATA",
      [
        "storage",
        "00c81410",
        null,
        "undefined *"
      ]
    ],
    [
      "008878ac",
      "READ",
      [
        "storage",
        "00c81430",
        null,
        "pointer"
      ]
    ],
    [
      "008878ac",
      "READ",
      [
        "storage",
        "00c81438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088786c",
      "DATA",
      [
        "storage",
        "00c814e0",
        null,
        "undefined *"
      ]
    ],
    [
      "008878ac",
      "READ",
      [
        "storage",
        "00c81500",
        null,
        "pointer"
      ]
    ],
    [
      "008878ac",
      "READ",
      [
        "storage",
        "00c81508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088780c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008877e0.md#insn-0088780c) · [`0088782c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008877e0.md#insn-0088782c) · [`00887858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008877e0.md#insn-00887858)
- 新版 [`00887864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887838.md#insn-00887864) · [`00887884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887838.md#insn-00887884) · [`008878b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887838.md#insn-008878b0)

~~~diff
- 0088780c ["COPY", "tmp:0:8", ["const:410:8"]]
- 0088780c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088780c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088780c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00887864 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00887864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00887864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00887864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088780c bytes 08411091
+ 00887864 bytes 08811391
- 0088782c ["INT_ADD", "register:40f0:8", ["const:88782c:8", "const:4:8"]]
- 0088782c ["CALL", null, ["callee:00b37478:8"]]
+ 00887884 ["INT_ADD", "register:40f0:8", ["const:887884:8", "const:4:8"]]
+ 00887884 ["CALL", null, ["callee:00b37478:8"]]
- 0088782c bytes ecbe0a94
+ 00887884 bytes fdbe0a94
- 00887858 ["COPY", "register:0:8", ["register:4040:8"]]
- 00887858 ["INT_ADD", "register:40f0:8", ["const:887858:8", "const:4:8"]]
- 00887858 ["CALLIND", null, ["register:0:8"]]
+ 008878b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008878b0 ["INT_ADD", "register:40f0:8", ["const:8878b0:8", "const:4:8"]]
+ 008878b0 ["CALLIND", null, ["register:0:8"]]
- 00887858 bytes 00013fd6
+ 008878b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-977ac19dff8709a0ecc60d762809a4e6"></a>

### [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) → [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) FUN_00887930

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`006b380c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b380c.md) [`0073c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c938.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 24件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`00597a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a8c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0087eac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087eac0.md) [`0088802c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/0088802c.md)
- 新版 呼出元 7件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`006b3864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3864.md) [`0073c990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073c/0073c990.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 24件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`00597acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597acc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0087eb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087e/0087eb18.md) [`00888084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888084.md)

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
      "definition_site": "00887a80",
      "incomplete_value": true,
      "site": "00887a88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:750:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00887a28",
      "incomplete_value": true,
      "site": "00887a30",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:680:8"
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
      "00887a80",
      "READ",
      [
        "storage",
        "00c9b680",
        null,
        "pointer"
      ]
    ],
    [
      "00887a80",
      "PARAM",
      [
        "storage",
        "011236a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00887a80",
      "READ",
      [
        "storage",
        "00c9b750",
        null,
        "pointer"
      ]
    ],
    [
      "00887a80",
      "PARAM",
      [
        "storage",
        "011237a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00887a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md#insn-00887a30) · [`008879ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md#insn-008879ec) · [`00887a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md#insn-00887a10)
- 新版 [`00887a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md#insn-00887a88) · [`00887a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md#insn-00887a44) · [`00887a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md#insn-00887a68)

~~~diff
- 00887a30 ["INT_ADD", "register:40f0:8", ["const:887a30:8", "const:4:8"]]
- 00887a30 ["CALL", null, ["callee:0087eb18:8"]]
+ 00887a88 ["INT_ADD", "register:40f0:8", ["const:887a88:8", "const:4:8"]]
+ 00887a88 ["CALL", null, ["callee:0087eb18:8"]]
- 00887a30 bytes 24dcff97
+ 00887a88 bytes 24dcff97
- 008879ec ["INT_ADD", "register:40f0:8", ["const:8879ec:8", "const:4:8"]]
- 008879ec ["CALL", null, ["callee:0088adc0:8"]]
+ 00887a44 ["INT_ADD", "register:40f0:8", ["const:887a44:8", "const:4:8"]]
+ 00887a44 ["CALL", null, ["callee:0088adc0:8"]]
- 008879ec bytes df0c0094
+ 00887a44 bytes df0c0094
- 00887a10 ["INT_ADD", "register:40f0:8", ["const:887a10:8", "const:4:8"]]
- 00887a10 ["CALL", null, ["callee:0088a948:8"]]
+ 00887a68 ["INT_ADD", "register:40f0:8", ["const:887a68:8", "const:4:8"]]
+ 00887a68 ["CALL", null, ["callee:0088a948:8"]]
- 00887a10 bytes b80b0094
+ 00887a68 bytes b80b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ce469ecdde152481ca02e6a03cd1028"></a>

### [`00888428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888428.md) → [`00888480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888480.md) FUN_00888480

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0061671c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/0061671c.md) [`0062626c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/0062626c.md) [`006ff318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff318.md) [`0074140c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/0074140c.md) [`007fd37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd37c.md) · 呼出先 11件 [`0058f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md) [`0088b938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b938.md) [`0088b93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b93c.md) [`0088ba48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba48.md) [`0088ba4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba4c.md)
- 新版 呼出元 6件 [`0061675c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/0061675c.md) [`006262ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00626/006262ac.md) [`006ff370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff370.md) [`00741464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00741/00741464.md) [`007fd3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd3d4.md) · 呼出先 11件 [`0058f474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f474.md) [`0088b990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b990.md) [`0088b994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b994.md) [`0088baa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088baa0.md) [`0088baa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088baa4.md)

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
      "definition_site": "008885e0",
      "incomplete_value": false,
      "site": "008885e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888588",
      "incomplete_value": false,
      "site": "00888588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "definition_site": "00888604",
      "incomplete_value": false,
      "site": "00888604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008885ac",
      "incomplete_value": false,
      "site": "008885ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "definition_site": "0088861c",
      "incomplete_value": false,
      "site": "0088861c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008885c4",
      "incomplete_value": false,
      "site": "008885c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "008885e0",
      "DATA",
      [
        "storage",
        "00c81840",
        null,
        "undefined *"
      ]
    ],
    [
      "00888604",
      "DATA",
      [
        "storage",
        "00c818c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088861c",
      "DATA",
      [
        "storage",
        "00c81940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008885e0",
      "DATA",
      [
        "storage",
        "00c81910",
        null,
        "undefined *"
      ]
    ],
    [
      "00888604",
      "DATA",
      [
        "storage",
        "00c81990",
        null,
        "undefined *"
      ]
    ],
    [
      "0088861c",
      "DATA",
      [
        "storage",
        "00c81a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888428.md#insn-00888584) · [`00888510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888428.md#insn-00888510) · [`0088853c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888428.md#insn-0088853c)
- 新版 [`008885dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888480.md#insn-008885dc) · [`00888568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888480.md#insn-00888568) · [`00888594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888480.md#insn-00888594)

~~~diff
- 00888584 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00888584 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00888584 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00888584 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008885dc ["COPY", "tmp:0:8", ["const:910:8"]]
+ 008885dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008885dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008885dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00888584 bytes 29012191
+ 008885dc bytes 29412491
- 00888510 ["COPY", "register:0:8", ["register:4040:8"]]
- 00888510 ["INT_ADD", "register:40f0:8", ["const:888510:8", "const:4:8"]]
- 00888510 ["CALLIND", null, ["register:0:8"]]
+ 00888568 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888568 ["INT_ADD", "register:40f0:8", ["const:888568:8", "const:4:8"]]
+ 00888568 ["CALLIND", null, ["register:0:8"]]
- 00888510 bytes 00013fd6
+ 00888568 bytes 00013fd6
- 0088853c ["COPY", "register:0:8", ["register:4040:8"]]
- 0088853c ["INT_ADD", "register:40f0:8", ["const:88853c:8", "const:4:8"]]
- 0088853c ["CALLIND", null, ["register:0:8"]]
+ 00888594 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00888594 ["INT_ADD", "register:40f0:8", ["const:888594:8", "const:4:8"]]
+ 00888594 ["CALLIND", null, ["register:0:8"]]
- 0088853c bytes 00013fd6
+ 00888594 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d33ffab78ff411c44dc2f08963ea2c6c"></a>

### [`00888854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888854.md) → [`008888ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008888ac.md) FUN_008888ac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007fd5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fd5f0.md) · 呼出先 4件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)
- 新版 呼出元 1件 [`007fd648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd648.md) · 呼出先 4件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)

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
      "definition_site": "0088898c",
      "incomplete_value": false,
      "site": "0088899c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888934",
      "incomplete_value": false,
      "site": "00888944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00888994",
      "incomplete_value": false,
      "site": "0088899c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088893c",
      "incomplete_value": false,
      "site": "00888944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "0088898c",
      "PARAM",
      [
        "storage",
        "00c81128",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00888994",
      "PARAM",
      [
        "storage",
        "00c81138",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0088898c",
      "PARAM",
      [
        "storage",
        "00c811f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00888994",
      "PARAM",
      [
        "storage",
        "00c81208",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888854.md#insn-00888944) · [`00888934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888854.md#insn-00888934) · [`0088893c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888854.md#insn-0088893c)
- 新版 [`0088899c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008888ac.md#insn-0088899c) · [`0088898c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008888ac.md#insn-0088898c) · [`00888994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/008888ac.md#insn-00888994)

~~~diff
- 00888944 ["INT_ADD", "register:40f0:8", ["const:888944:8", "const:4:8"]]
- 00888944 ["CALL", null, ["callee:00c586e0:8"]]
+ 0088899c ["INT_ADD", "register:40f0:8", ["const:88899c:8", "const:4:8"]]
+ 0088899c ["CALL", null, ["callee:00c586e0:8"]]
- 00888944 bytes 333f0f94
+ 0088899c bytes 513f0f94
- 00888934 ["COPY", "tmp:0:8", ["const:128:8"]]
- 00888934 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00888934 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00888934 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0088898c ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 0088898c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0088898c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0088898c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00888934 bytes 21a00491
+ 0088898c bytes 21e00791
- 0088893c ["COPY", "tmp:0:8", ["const:138:8"]]
- 0088893c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0088893c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0088893c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00888994 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 00888994 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00888994 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00888994 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0088893c bytes 42e00491
+ 00888994 bytes 42200891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccc2656b01db64e12776e0ff6980f32c"></a>

### [`008889b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008889b0.md) → [`00888a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888a08.md) FUN_00888a08

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006ff640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff640.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 5件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)
- 新版 呼出元 2件 [`006ff698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ff/006ff698.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 5件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00888c74",
      "incomplete_value": false,
      "site": "00888c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888c1c",
      "incomplete_value": false,
      "site": "00888c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00888c7c",
      "incomplete_value": false,
      "site": "00888c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888c24",
      "incomplete_value": false,
      "site": "00888c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00888ccc",
      "incomplete_value": false,
      "site": "00888cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888c74",
      "incomplete_value": false,
      "site": "00888c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:128:8"
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
      "00888c74",
      "PARAM",
      [
        "storage",
        "00c81128",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00888c7c",
      "PARAM",
      [
        "storage",
        "00c811b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00888ccc",
      "PARAM",
      [
        "storage",
        "00c81128",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00888c74",
      "PARAM",
      [
        "storage",
        "00c811f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00888c7c",
      "PARAM",
      [
        "storage",
        "00c81280",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00888ccc",
      "PARAM",
      [
        "storage",
        "00c811f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008889b0.md#insn-00888c2c) · [`00888c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008889b0.md#insn-00888c84) · [`00888c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008889b0.md#insn-00888c1c)
- 新版 [`00888c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888a08.md#insn-00888c84) · [`00888cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888a08.md#insn-00888cdc) · [`00888c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888a08.md#insn-00888c74)

~~~diff
- 00888c2c ["INT_ADD", "register:40f0:8", ["const:888c2c:8", "const:4:8"]]
- 00888c2c ["CALL", null, ["callee:00c586e0:8"]]
+ 00888c84 ["INT_ADD", "register:40f0:8", ["const:888c84:8", "const:4:8"]]
+ 00888c84 ["CALL", null, ["callee:00c586e0:8"]]
- 00888c2c bytes 793e0f94
+ 00888c84 bytes 973e0f94
- 00888c84 ["INT_ADD", "register:40f0:8", ["const:888c84:8", "const:4:8"]]
- 00888c84 ["CALL", null, ["callee:00c586e0:8"]]
+ 00888cdc ["INT_ADD", "register:40f0:8", ["const:888cdc:8", "const:4:8"]]
+ 00888cdc ["CALL", null, ["callee:00c586e0:8"]]
- 00888c84 bytes 633e0f94
+ 00888cdc bytes 813e0f94
- 00888c1c ["COPY", "tmp:0:8", ["const:128:8"]]
- 00888c1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00888c1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00888c1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00888c74 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 00888c74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00888c74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00888c74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00888c1c bytes 21a00491
+ 00888c74 bytes 21e00791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33ba02ed43d55ed94a8db5cc77082fe9"></a>

### [`00888de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888de8.md) → [`00888e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e40.md) FUN_00888e40

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
      "definition_site": "00888e64",
      "incomplete_value": false,
      "site": "00888e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888e0c",
      "incomplete_value": false,
      "site": "00888e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      "00888e64",
      "DATA",
      [
        "storage",
        "00c811f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00888e64",
      "DATA",
      [
        "storage",
        "00c812c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888de8.md#insn-00888dfc) · [`00888e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888de8.md#insn-00888e08)
- 新版 [`00888e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e40.md#insn-00888e54) · [`00888e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e40.md#insn-00888e60)

~~~diff
- 00888dfc ["INT_ADD", "register:40f0:8", ["const:888dfc:8", "const:4:8"]]
- 00888dfc ["CALL", null, ["callee:00c57f60:8"]]
+ 00888e54 ["INT_ADD", "register:40f0:8", ["const:888e54:8", "const:4:8"]]
+ 00888e54 ["CALL", null, ["callee:00c57f60:8"]]
- 00888dfc bytes 253c0f94
+ 00888e54 bytes 433c0f94
- 00888e08 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 00888e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00888e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00888e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00888e60 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 00888e60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00888e60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00888e60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00888e08 bytes 08c10791
+ 00888e60 bytes 08010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b201827a54355a59c6d669356f034d6c"></a>

### [`00888e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e1c.md) → [`00888e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e74.md) FUN_00888e74

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
      "definition_site": "00888e80",
      "incomplete_value": false,
      "site": "00888e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00888e28",
      "incomplete_value": false,
      "site": "00888e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "00888e80",
      "DATA",
      [
        "storage",
        "00c811f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00888e80",
      "DATA",
      [
        "storage",
        "00c812c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888e1c.md#insn-00888e24)
- 新版 [`00888e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00888/00888e74.md#insn-00888e7c)

~~~diff
- 00888e24 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 00888e24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00888e24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00888e24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00888e7c ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 00888e7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00888e7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00888e7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00888e24 bytes 29c10791
+ 00888e7c bytes 29010b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2268cf7d19abe44474f22dccdf5d9394"></a>

### [`00888fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888fe8.md) → [`00889040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889040.md) FUN_00889040

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
      "definition_site": "00889064",
      "incomplete_value": false,
      "site": "00889064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088900c",
      "incomplete_value": false,
      "site": "0088900c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:280:8"
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
      "00889064",
      "DATA",
      [
        "storage",
        "00c81280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889064",
      "DATA",
      [
        "storage",
        "00c81350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00888ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888fe8.md#insn-00888ffc) · [`00889008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888fe8.md#insn-00889008)
- 新版 [`00889054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889040.md#insn-00889054) · [`00889060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889040.md#insn-00889060)

~~~diff
- 00888ffc ["INT_ADD", "register:40f0:8", ["const:888ffc:8", "const:4:8"]]
- 00888ffc ["CALL", null, ["callee:00c57f60:8"]]
+ 00889054 ["INT_ADD", "register:40f0:8", ["const:889054:8", "const:4:8"]]
+ 00889054 ["CALL", null, ["callee:00c57f60:8"]]
- 00888ffc bytes a53b0f94
+ 00889054 bytes c33b0f94
- 00889008 ["COPY", "tmp:0:8", ["const:280:8"]]
- 00889008 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00889008 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00889008 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00889060 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 00889060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00889060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00889060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00889008 bytes 08010a91
+ 00889060 bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fc2fe29ef1c634a197e472151ff19b2"></a>

### [`0088901c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/0088901c.md) → [`00889074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889074.md) FUN_00889074

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
      "definition_site": "00889080",
      "incomplete_value": false,
      "site": "00889080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889028",
      "incomplete_value": false,
      "site": "00889028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:280:8"
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
      "00889080",
      "DATA",
      [
        "storage",
        "00c81280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889080",
      "DATA",
      [
        "storage",
        "00c81350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/0088901c.md#insn-00889024)
- 新版 [`0088907c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889074.md#insn-0088907c)

~~~diff
- 00889024 ["COPY", "tmp:0:8", ["const:280:8"]]
- 00889024 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00889024 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00889024 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088907c ["COPY", "tmp:0:8", ["const:350:8"]]
+ 0088907c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088907c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088907c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00889024 bytes 29010a91
+ 0088907c bytes 29410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbbcebee5c0b25649e0b611d92c6c92e"></a>

### [`008891dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/008891dc.md) → [`00889234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889234.md) FUN_00889234

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
      "definition_site": "00889248",
      "incomplete_value": false,
      "site": "0088924c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008891f0",
      "incomplete_value": false,
      "site": "008891f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:310:8"
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
      "0088924c",
      "DATA",
      [
        "storage",
        "00c81310",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088924c",
      "DATA",
      [
        "storage",
        "00c813e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008891e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/008891dc.md#insn-008891e8) · [`008891f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/008891dc.md#insn-008891f0)
- 新版 [`00889240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889234.md#insn-00889240) · [`00889248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889234.md#insn-00889248)

~~~diff
- 008891e8 ["INT_ADD", "register:40f0:8", ["const:8891e8:8", "const:4:8"]]
- 008891e8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00889240 ["INT_ADD", "register:40f0:8", ["const:889240:8", "const:4:8"]]
+ 00889240 ["CALL", null, ["callee:00c57f60:8"]]
- 008891e8 bytes 2a3b0f94
+ 00889240 bytes 483b0f94
- 008891f0 ["COPY", "tmp:0:8", ["const:310:8"]]
- 008891f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008891f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008891f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00889248 ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 00889248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00889248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00889248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008891f0 bytes 08410c91
+ 00889248 bytes 08810f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c16bbd5674e888573883a6fb5d6fc56c"></a>

### [`00889200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889200.md) → [`00889258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889258.md) FUN_00889258

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
      "definition_site": "0088925c",
      "incomplete_value": false,
      "site": "00889260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889204",
      "incomplete_value": false,
      "site": "00889208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:310:8"
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
      "00889260",
      "DATA",
      [
        "storage",
        "00c81310",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889260",
      "DATA",
      [
        "storage",
        "00c813e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889200.md#insn-00889204)
- 新版 [`0088925c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889258.md#insn-0088925c)

~~~diff
- 00889204 ["COPY", "tmp:0:8", ["const:310:8"]]
- 00889204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00889204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00889204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088925c ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 0088925c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088925c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088925c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00889204 bytes 08410c91
+ 0088925c bytes 08810f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b659cf79e32d77be12d33aff0af92105"></a>

### [`008896d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/008896d8.md) → [`00889730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889730.md) FUN_00889730

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
      "definition_site": "00889754",
      "incomplete_value": false,
      "site": "00889754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008896fc",
      "incomplete_value": false,
      "site": "008896fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "00889754",
      "DATA",
      [
        "storage",
        "00c81390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889754",
      "DATA",
      [
        "storage",
        "00c81460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008896ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/008896d8.md#insn-008896ec) · [`008896f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/008896d8.md#insn-008896f8)
- 新版 [`00889744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889730.md#insn-00889744) · [`00889750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889730.md#insn-00889750)

~~~diff
- 008896ec ["INT_ADD", "register:40f0:8", ["const:8896ec:8", "const:4:8"]]
- 008896ec ["CALL", null, ["callee:00c57f60:8"]]
+ 00889744 ["INT_ADD", "register:40f0:8", ["const:889744:8", "const:4:8"]]
+ 00889744 ["CALL", null, ["callee:00c57f60:8"]]
- 008896ec bytes e9390f94
+ 00889744 bytes 073a0f94
- 008896f8 ["COPY", "tmp:0:8", ["const:390:8"]]
- 008896f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008896f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008896f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00889750 ["COPY", "tmp:0:8", ["const:460:8"]]
+ 00889750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00889750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00889750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008896f8 bytes 08410e91
+ 00889750 bytes 08811191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24265c08a3acd7486f211217afe4a14b"></a>

### [`0088970c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/0088970c.md) → [`00889764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889764.md) FUN_00889764

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
      "definition_site": "00889770",
      "incomplete_value": false,
      "site": "00889770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889718",
      "incomplete_value": false,
      "site": "00889718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:390:8"
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
      "00889770",
      "DATA",
      [
        "storage",
        "00c81390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889770",
      "DATA",
      [
        "storage",
        "00c81460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/0088970c.md#insn-00889714)
- 新版 [`0088976c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889764.md#insn-0088976c)

~~~diff
- 00889714 ["COPY", "tmp:0:8", ["const:390:8"]]
- 00889714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00889714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00889714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088976c ["COPY", "tmp:0:8", ["const:460:8"]]
+ 0088976c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088976c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088976c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00889714 bytes 29410e91
+ 0088976c bytes 29811191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eb53f6061e6cbffac568388f1812ff4"></a>

### [`00889b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889b88.md) → [`00889be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889be0.md) FUN_00889be0

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
      "definition_site": "00889bec",
      "incomplete_value": false,
      "site": "00889bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889b94",
      "incomplete_value": false,
      "site": "00889b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      "00889bec",
      "DATA",
      [
        "storage",
        "00c81410",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889bec",
      "DATA",
      [
        "storage",
        "00c814e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889b88.md#insn-00889b90)
- 新版 [`00889be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889be0.md#insn-00889be8)

~~~diff
- 00889b90 ["COPY", "tmp:0:8", ["const:410:8"]]
- 00889b90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00889b90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00889b90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00889be8 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00889be8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00889be8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00889be8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00889b90 bytes 29411091
+ 00889be8 bytes 29811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-361e742147fe6041e4257225714dd5be"></a>

### [`00889ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889ba4.md) → [`00889bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bfc.md) FUN_00889bfc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00889d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d68.md) [`00889d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d6c.md) [`0088a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a164.md) [`0088a168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a168.md) [`00b37b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37b88.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00889dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dc0.md) [`00889dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dc4.md) [`0088a1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1bc.md) [`0088a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1c0.md) [`00b37c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b37/00b37c24.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.34% / 新版 94.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00889c40",
      "incomplete_value": false,
      "site": "00889c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889be8",
      "incomplete_value": false,
      "site": "00889be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "00889c34",
      "DATA",
      [
        "storage",
        "00c81480",
        null,
        "undefined *"
      ]
    ],
    [
      "00889c40",
      "DATA",
      [
        "storage",
        "00c81500",
        null,
        "undefined *"
      ]
    ],
    [
      "00889c74",
      "READ",
      [
        "storage",
        "00c81520",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00889c34",
      "DATA",
      [
        "storage",
        "00c81550",
        null,
        "undefined *"
      ]
    ],
    [
      "00889c40",
      "DATA",
      [
        "storage",
        "00c815d0",
        null,
        "undefined *"
      ]
    ],
    [
      "00889c74",
      "READ",
      [
        "storage",
        "00c815f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889ba4.md#insn-00889bbc) · [`00889be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889ba4.md#insn-00889be4) · [`00889bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889ba4.md#insn-00889bf4)
- 新版 [`00889c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bfc.md#insn-00889c14) · [`00889c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bfc.md#insn-00889c3c) · [`00889c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889bfc.md#insn-00889c4c)

~~~diff
- 00889bbc ["COPY", "tmp:0:8", ["const:480:8"]]
- 00889bbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00889bbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00889bbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00889c14 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00889c14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00889c14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00889c14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00889bbc bytes 29011291
+ 00889c14 bytes 29411591
- 00889be4 ["COPY", "tmp:0:8", ["const:500:8"]]
- 00889be4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00889be4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00889be4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00889c3c ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 00889c3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00889c3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00889c3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00889be4 bytes 29011491
+ 00889c3c bytes 29411791
- 00889bf4 ["INT_ADD", "register:40f0:8", ["const:889bf4:8", "const:4:8"]]
- 00889bf4 ["CALL", null, ["callee:00b37c24:8"]]
+ 00889c4c ["INT_ADD", "register:40f0:8", ["const:889c4c:8", "const:4:8"]]
+ 00889c4c ["CALL", null, ["callee:00b37c24:8"]]
- 00889bf4 bytes e5b70a94
+ 00889c4c bytes f6b70a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-827d7bc4c0540df3c2824b4244e8dd33"></a>

### [`00889d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d20.md) → [`00889d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889d78.md) FUN_00889d78

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
      "definition_site": "00889d9c",
      "incomplete_value": false,
      "site": "00889d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889d44",
      "incomplete_value": false,
      "site": "00889d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "00889d9c",
      "DATA",
      [
        "storage",
        "00c81480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889d9c",
      "DATA",
      [
        "storage",
        "00c81550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d20.md#insn-00889d34) · [`00889d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d20.md#insn-00889d40)
- 新版 [`00889d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889d78.md#insn-00889d8c) · [`00889d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889d78.md#insn-00889d98)

~~~diff
- 00889d34 ["INT_ADD", "register:40f0:8", ["const:889d34:8", "const:4:8"]]
- 00889d34 ["CALL", null, ["callee:00c57f60:8"]]
+ 00889d8c ["INT_ADD", "register:40f0:8", ["const:889d8c:8", "const:4:8"]]
+ 00889d8c ["CALL", null, ["callee:00c57f60:8"]]
- 00889d34 bytes 57380f94
+ 00889d8c bytes 75380f94
- 00889d40 ["COPY", "tmp:0:8", ["const:480:8"]]
- 00889d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00889d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00889d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00889d98 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00889d98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00889d98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00889d98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00889d40 bytes 08011291
+ 00889d98 bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-333a7b9670028c919a7769db5888fcc3"></a>

### [`00889d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d54.md) → [`00889dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dac.md) FUN_00889dac

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
      "definition_site": "00889db8",
      "incomplete_value": false,
      "site": "00889db8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889d60",
      "incomplete_value": false,
      "site": "00889d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "00889db8",
      "DATA",
      [
        "storage",
        "00c81480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00889db8",
      "DATA",
      [
        "storage",
        "00c81550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d54.md#insn-00889d5c)
- 新版 [`00889db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dac.md#insn-00889db4)

~~~diff
- 00889d5c ["COPY", "tmp:0:8", ["const:480:8"]]
- 00889d5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00889d5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00889d5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00889db4 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00889db4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00889db4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00889db4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00889d5c bytes 29011291
+ 00889db4 bytes 29411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c357b07cc6b719f55968139778a77a1"></a>

### [`00889d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d70.md) → [`00889dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dc8.md) FUN_00889dc8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md) [`0066d0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d0fc.md) [`006a2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md)
- 新版 呼出元 0件  · 呼出先 10件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) [`0066d13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066d/0066d13c.md) [`006a2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2bd0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.41% / 新版 96.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00889e60",
      "incomplete_value": true,
      "site": "00889e60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:662:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889e08",
      "incomplete_value": true,
      "site": "00889e08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6af:8"
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
      "definition_site": "00889ee8",
      "incomplete_value": true,
      "site": "00889ee8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:942:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00889e90",
      "incomplete_value": true,
      "site": "00889e90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:996:8"
              ]
            ]
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
      "00889e50",
      "READ",
      [
        "storage",
        "002a06af",
        null,
        "string"
      ]
    ],
    [
      "00889ec4",
      "READ",
      [
        "storage",
        "002bb996",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00889e50",
      "READ",
      [
        "storage",
        "002a0662",
        null,
        "string"
      ]
    ],
    [
      "00889ec4",
      "READ",
      [
        "storage",
        "002bb942",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00889da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d70.md#insn-00889da8) · [`00889db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d70.md#insn-00889db4) · [`00889dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00889/00889d70.md#insn-00889dbc)
- 新版 [`00889e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dc8.md#insn-00889e00) · [`00889e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dc8.md#insn-00889e0c) · [`00889e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00889/00889dc8.md#insn-00889e14)

~~~diff
- 00889da8 ["INT_ADD", "register:40f0:8", ["const:889da8:8", "const:4:8"]]
- 00889da8 ["CALL", null, ["callee:00c581b0:8"]]
+ 00889e00 ["INT_ADD", "register:40f0:8", ["const:889e00:8", "const:4:8"]]
+ 00889e00 ["CALL", null, ["callee:00c581b0:8"]]
- 00889da8 bytes ce380f94
+ 00889e00 bytes ec380f94
- 00889db4 ["INT_ADD", "register:40f0:8", ["const:889db4:8", "const:4:8"]]
- 00889db4 ["CALL", null, ["callee:00c58450:8"]]
+ 00889e0c ["INT_ADD", "register:40f0:8", ["const:889e0c:8", "const:4:8"]]
+ 00889e0c ["CALL", null, ["callee:00c58450:8"]]
- 00889db4 bytes 73390f94
+ 00889e0c bytes 91390f94
- 00889dbc ["INT_ADD", "register:40f0:8", ["const:889dbc:8", "const:4:8"]]
- 00889dbc ["CALL", null, ["callee:00c581c0:8"]]
+ 00889e14 ["INT_ADD", "register:40f0:8", ["const:889e14:8", "const:4:8"]]
+ 00889e14 ["CALL", null, ["callee:00c581c0:8"]]
- 00889dbc bytes cd380f94
+ 00889e14 bytes eb380f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac3635418b41b6b4b4765d120c60339d"></a>

### [`0088a11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a11c.md) → [`0088a174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a174.md) FUN_0088a174

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
      "definition_site": "0088a198",
      "incomplete_value": false,
      "site": "0088a198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a140",
      "incomplete_value": false,
      "site": "0088a140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "0088a198",
      "DATA",
      [
        "storage",
        "00c81500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a198",
      "DATA",
      [
        "storage",
        "00c815d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a11c.md#insn-0088a130) · [`0088a13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a11c.md#insn-0088a13c)
- 新版 [`0088a188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a174.md#insn-0088a188) · [`0088a194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a174.md#insn-0088a194)

~~~diff
- 0088a130 ["INT_ADD", "register:40f0:8", ["const:88a130:8", "const:4:8"]]
- 0088a130 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088a188 ["INT_ADD", "register:40f0:8", ["const:88a188:8", "const:4:8"]]
+ 0088a188 ["CALL", null, ["callee:00c57f60:8"]]
- 0088a130 bytes 58370f94
+ 0088a188 bytes 76370f94
- 0088a13c ["COPY", "tmp:0:8", ["const:500:8"]]
- 0088a13c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a13c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a13c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a194 ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 0088a194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a13c bytes 08011491
+ 0088a194 bytes 08411791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4d71eeae74af6244ed97b064b590e30"></a>

### [`0088a150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a150.md) → [`0088a1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1a8.md) FUN_0088a1a8

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
      "definition_site": "0088a1b4",
      "incomplete_value": false,
      "site": "0088a1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a15c",
      "incomplete_value": false,
      "site": "0088a15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "0088a1b4",
      "DATA",
      [
        "storage",
        "00c81500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a1b4",
      "DATA",
      [
        "storage",
        "00c815d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a150.md#insn-0088a158)
- 新版 [`0088a1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1a8.md#insn-0088a1b0)

~~~diff
- 0088a158 ["COPY", "tmp:0:8", ["const:500:8"]]
- 0088a158 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088a158 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088a158 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088a1b0 ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 0088a1b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088a1b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088a1b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088a158 bytes 29011491
+ 0088a1b0 bytes 29411791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea69ada3b7a484a9b44c68cd79ea3efa"></a>

### [`0088a16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a16c.md) → [`0088a1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1c4.md) FUN_0088a1c4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0069ef14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069ef14.md) [`006a2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md) [`006a2d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2d48.md) [`006a2d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2d4c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0048ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce90.md) [`0069ef6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069ef6c.md) [`006a2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2bd0.md) [`006a2da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2da0.md) [`006a2da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2da4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088a260",
      "incomplete_value": false,
      "site": "0088a26c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a208",
      "incomplete_value": false,
      "site": "0088a214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "definition_site": "0088a220",
      "incomplete_value": false,
      "site": "0088a22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:6a2000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a1c8",
      "incomplete_value": false,
      "site": "0088a1d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:6a2000:8"
          ],
          [
            "leaf",
            "const:d48:8"
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
      "0088a220",
      "PARAM",
      [
        "storage",
        "006a2d48",
        null,
        null
      ]
    ],
    [
      "0088a26c",
      "DATA",
      [
        "storage",
        "00c81570",
        null,
        "undefined *"
      ]
    ],
    [
      "0088a2b8",
      "READ",
      [
        "storage",
        "00c81590",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0088a220",
      "PARAM",
      [
        "storage",
        "006a2da0",
        null,
        null
      ]
    ],
    [
      "0088a26c",
      "DATA",
      [
        "storage",
        "00c81640",
        null,
        "undefined *"
      ]
    ],
    [
      "0088a2b8",
      "READ",
      [
        "storage",
        "00c81660",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a16c.md#insn-0088a1d4) · [`0088a19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a16c.md#insn-0088a19c) · [`0088a1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a16c.md#insn-0088a1c8)
- 新版 [`0088a22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1c4.md#insn-0088a22c) · [`0088a1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1c4.md#insn-0088a1f4) · [`0088a220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1c4.md#insn-0088a220)

~~~diff
- 0088a1d4 ["INT_ADD", "register:40f0:8", ["const:88a1d4:8", "const:4:8"]]
- 0088a1d4 ["CALL", null, ["callee:006a2da4:8"]]
+ 0088a22c ["INT_ADD", "register:40f0:8", ["const:88a22c:8", "const:4:8"]]
+ 0088a22c ["CALL", null, ["callee:006a2da4:8"]]
- 0088a1d4 bytes de62f897
+ 0088a22c bytes de62f897
- 0088a19c ["INT_ADD", "register:40f0:8", ["const:88a19c:8", "const:4:8"]]
- 0088a19c ["CALL", null, ["callee:00c57f60:8"]]
+ 0088a1f4 ["INT_ADD", "register:40f0:8", ["const:88a1f4:8", "const:4:8"]]
+ 0088a1f4 ["CALL", null, ["callee:00c57f60:8"]]
- 0088a19c bytes 3d370f94
+ 0088a1f4 bytes 5b370f94
- 0088a1c8 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 0088a1c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0088a1c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0088a1c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0088a220 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 0088a220 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0088a220 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0088a220 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0088a1c8 bytes 21203591
+ 0088a220 bytes 21803691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fcdce60dc1f087d8a093d1e44b00fdb"></a>

### [`0088a34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a34c.md) → [`0088a3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3a4.md) FUN_0088a3a4

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
      "definition_site": "0088a3b8",
      "incomplete_value": false,
      "site": "0088a3bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a360",
      "incomplete_value": false,
      "site": "0088a364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "0088a3bc",
      "DATA",
      [
        "storage",
        "00c81570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a3bc",
      "DATA",
      [
        "storage",
        "00c81640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a34c.md#insn-0088a358) · [`0088a360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a34c.md#insn-0088a360)
- 新版 [`0088a3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3a4.md#insn-0088a3b0) · [`0088a3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3a4.md#insn-0088a3b8)

~~~diff
- 0088a358 ["INT_ADD", "register:40f0:8", ["const:88a358:8", "const:4:8"]]
- 0088a358 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088a3b0 ["INT_ADD", "register:40f0:8", ["const:88a3b0:8", "const:4:8"]]
+ 0088a3b0 ["CALL", null, ["callee:00c57f60:8"]]
- 0088a358 bytes ce360f94
+ 0088a3b0 bytes ec360f94
- 0088a360 ["COPY", "tmp:0:8", ["const:570:8"]]
- 0088a360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a3b8 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 0088a3b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a3b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a360 bytes 08c11591
+ 0088a3b8 bytes 08011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a55d374a4cf38126f39b18459eeeb84"></a>

### [`0088a370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a370.md) → [`0088a3c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3c8.md) FUN_0088a3c8

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
      "definition_site": "0088a3cc",
      "incomplete_value": false,
      "site": "0088a3d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a374",
      "incomplete_value": false,
      "site": "0088a378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "0088a3d0",
      "DATA",
      [
        "storage",
        "00c81570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a3d0",
      "DATA",
      [
        "storage",
        "00c81640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a370.md#insn-0088a374)
- 新版 [`0088a3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a3c8.md#insn-0088a3cc)

~~~diff
- 0088a374 ["COPY", "tmp:0:8", ["const:570:8"]]
- 0088a374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a3cc ["COPY", "tmp:0:8", ["const:640:8"]]
+ 0088a3cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a3cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a3cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a374 bytes 08c11591
+ 0088a3cc bytes 08011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4235f0634fc9f73b6ac1bb098b0bdf6b"></a>

### [`0088a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a7d0.md) → [`0088a828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a828.md) FUN_0088a828

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088a880",
      "incomplete_value": false,
      "site": "0088a884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a828",
      "incomplete_value": false,
      "site": "0088a82c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "definition_site": "0088a89c",
      "incomplete_value": false,
      "site": "0088a8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:35:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a844",
      "incomplete_value": false,
      "site": "0088a84c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:4:8"
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
      "definition_site": "0088a8ac",
      "incomplete_value": false,
      "site": "0088a8b4",
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
            "const:ea7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a854",
      "incomplete_value": false,
      "site": "0088a85c",
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
            "const:e76:8"
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
      "0088a86c",
      "DATA",
      [
        "storage",
        "00c81610",
        null,
        "undefined *"
      ]
    ],
    [
      "0088a884",
      "DATA",
      [
        "storage",
        "00c81058",
        null,
        "pointer"
      ]
    ],
    [
      "0088a89c",
      "PARAM",
      [
        "storage",
        "002b3004",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088a86c",
      "DATA",
      [
        "storage",
        "00c816e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088a884",
      "DATA",
      [
        "storage",
        "00c81128",
        null,
        "pointer"
      ]
    ],
    [
      "0088a89c",
      "PARAM",
      [
        "storage",
        "002b3035",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a7d0.md#insn-0088a7f4) · [`0088a84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a7d0.md#insn-0088a84c) · [`0088a85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a7d0.md#insn-0088a85c)
- 新版 [`0088a84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a828.md#insn-0088a84c) · [`0088a8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a828.md#insn-0088a8a4) · [`0088a8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a828.md#insn-0088a8b4)

~~~diff
- 0088a7f4 ["INT_ADD", "register:40f0:8", ["const:88a7f4:8", "const:4:8"]]
- 0088a7f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088a84c ["INT_ADD", "register:40f0:8", ["const:88a84c:8", "const:4:8"]]
+ 0088a84c ["CALL", null, ["callee:00c57f60:8"]]
- 0088a7f4 bytes a7350f94
+ 0088a84c bytes c5350f94
- 0088a84c ["INT_ADD", "register:40f0:8", ["const:88a84c:8", "const:4:8"]]
- 0088a84c ["CALL", null, ["callee:00c58260:8"]]
+ 0088a8a4 ["INT_ADD", "register:40f0:8", ["const:88a8a4:8", "const:4:8"]]
+ 0088a8a4 ["CALL", null, ["callee:00c58260:8"]]
- 0088a84c bytes 51360f94
+ 0088a8a4 bytes 6f360f94
- 0088a85c ["INT_ADD", "register:40f0:8", ["const:88a85c:8", "const:4:8"]]
- 0088a85c ["CALL", null, ["callee:00c58260:8"]]
+ 0088a8b4 ["INT_ADD", "register:40f0:8", ["const:88a8b4:8", "const:4:8"]]
+ 0088a8b4 ["CALL", null, ["callee:00c58260:8"]]
- 0088a85c bytes 4d360f94
+ 0088a8b4 bytes 6b360f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8ba16b9e3f7b408618c2f1953e4d8ca"></a>

### [`0088a8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8a4.md) → [`0088a8fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a8fc.md) FUN_0088a8fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088a900",
      "incomplete_value": false,
      "site": "0088a904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a8a8",
      "incomplete_value": false,
      "site": "0088a8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:610:8"
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
      "0088a904",
      "DATA",
      [
        "storage",
        "00c81610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a904",
      "DATA",
      [
        "storage",
        "00c816e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8a4.md#insn-0088a8a8)
- 新版 [`0088a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a8fc.md#insn-0088a900)

~~~diff
- 0088a8a8 ["COPY", "tmp:0:8", ["const:610:8"]]
- 0088a8a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a8a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a8a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a900 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 0088a900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a8a8 bytes 08411891
+ 0088a900 bytes 08811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff89253fe610c6ad7c83c6248bd23778"></a>

### [`0088a8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8b4.md) → [`0088a90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a90c.md) FUN_0088a90c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088a91c",
      "incomplete_value": false,
      "site": "0088a924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088a8c4",
      "incomplete_value": false,
      "site": "0088a8cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:610:8"
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
      "0088a924",
      "DATA",
      [
        "storage",
        "00c81610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088a924",
      "DATA",
      [
        "storage",
        "00c816e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088a8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8b4.md#insn-0088a8c4) · [`0088a8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8b4.md#insn-0088a8d0)
- 新版 [`0088a91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a90c.md#insn-0088a91c) · [`0088a928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a90c.md#insn-0088a928)

~~~diff
- 0088a8c4 ["COPY", "tmp:0:8", ["const:610:8"]]
- 0088a8c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088a8c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088a8c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088a91c ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 0088a91c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a91c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088a91c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088a8c4 bytes 08411891
+ 0088a91c bytes 08811b91
- 0088a8d0 ["INT_ADD", "register:40f0:8", ["const:88a8d0:8", "const:4:8"]]
- 0088a8d0 ["CALL", null, ["callee:00c57f70:8"]]
+ 0088a928 ["INT_ADD", "register:40f0:8", ["const:88a928:8", "const:4:8"]]
+ 0088a928 ["CALL", null, ["callee:00c57f70:8"]]
- 0088a8d0 bytes 74350f94
+ 0088a928 bytes 92350f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e659d4b1ea885c49e6edf05de77f66d2"></a>

### [`0088ad68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ad68.md) → [`0088adc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088adc0.md) FUN_0088adc0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

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
      "definition_site": "0088adf8",
      "incomplete_value": false,
      "site": "0088ae04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ada0",
      "incomplete_value": false,
      "site": "0088adac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "definition_site": "0088ae18",
      "incomplete_value": false,
      "site": "0088ae1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088adc0",
      "incomplete_value": false,
      "site": "0088adc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "definition_site": "0088ae38",
      "incomplete_value": false,
      "site": "0088ae40",
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
            "const:dd9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ade0",
      "incomplete_value": false,
      "site": "0088ade8",
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
            "const:e35:8"
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
      "0088ae04",
      "DATA",
      [
        "storage",
        "00c81660",
        null,
        "undefined *"
      ]
    ],
    [
      "0088ae1c",
      "DATA",
      [
        "storage",
        "00c81078",
        null,
        "pointer"
      ]
    ],
    [
      "0088ae38",
      "PARAM",
      [
        "storage",
        "002a7e35",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088ae04",
      "DATA",
      [
        "storage",
        "00c81730",
        null,
        "undefined *"
      ]
    ],
    [
      "0088ae1c",
      "DATA",
      [
        "storage",
        "00c81148",
        null,
        "pointer"
      ]
    ],
    [
      "0088ae38",
      "PARAM",
      [
        "storage",
        "002a7dd9",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ad68.md#insn-0088ada0) · [`0088ade8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ad68.md#insn-0088ade8) · [`0088adf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ad68.md#insn-0088adf8)
- 新版 [`0088adf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088adc0.md#insn-0088adf8) · [`0088ae40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088adc0.md#insn-0088ae40) · [`0088ae50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088adc0.md#insn-0088ae50)

~~~diff
- 0088ada0 ["COPY", "tmp:0:8", ["const:660:8"]]
- 0088ada0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088ada0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088ada0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088adf8 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 0088adf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088adf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088adf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088ada0 bytes 08811991
+ 0088adf8 bytes 08c11c91
- 0088ade8 ["INT_ADD", "register:40f0:8", ["const:88ade8:8", "const:4:8"]]
- 0088ade8 ["CALL", null, ["callee:00c58260:8"]]
+ 0088ae40 ["INT_ADD", "register:40f0:8", ["const:88ae40:8", "const:4:8"]]
+ 0088ae40 ["CALL", null, ["callee:00c58260:8"]]
- 0088ade8 bytes ea340f94
+ 0088ae40 bytes 08350f94
- 0088adf8 ["INT_ADD", "register:40f0:8", ["const:88adf8:8", "const:4:8"]]
- 0088adf8 ["CALL", null, ["callee:00c58260:8"]]
+ 0088ae50 ["INT_ADD", "register:40f0:8", ["const:88ae50:8", "const:4:8"]]
+ 0088ae50 ["CALL", null, ["callee:00c58260:8"]]
- 0088adf8 bytes e6340f94
+ 0088ae50 bytes 04350f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baabbf70f617f317aab1452ce4f3c126"></a>

### [`0088ae40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae40.md) → [`0088ae98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088ae98.md) FUN_0088ae98

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088ae9c",
      "incomplete_value": false,
      "site": "0088aea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ae44",
      "incomplete_value": false,
      "site": "0088ae48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088aea0",
      "DATA",
      [
        "storage",
        "00c81660",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088aea0",
      "DATA",
      [
        "storage",
        "00c81730",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ae44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae40.md#insn-0088ae44)
- 新版 [`0088ae9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088ae98.md#insn-0088ae9c)

~~~diff
- 0088ae44 ["COPY", "tmp:0:8", ["const:660:8"]]
- 0088ae44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088ae44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088ae44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088ae9c ["COPY", "tmp:0:8", ["const:730:8"]]
+ 0088ae9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088ae9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088ae9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088ae44 bytes 08811991
+ 0088ae9c bytes 08c11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e05f8bb523ad41d943c81630c1d752c"></a>

### [`0088ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae50.md) → [`0088aea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aea8.md) FUN_0088aea8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088aeb8",
      "incomplete_value": false,
      "site": "0088aec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ae60",
      "incomplete_value": false,
      "site": "0088ae68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "0088aec0",
      "DATA",
      [
        "storage",
        "00c81660",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088aec0",
      "DATA",
      [
        "storage",
        "00c81730",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae50.md#insn-0088ae60) · [`0088ae6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae50.md#insn-0088ae6c)
- 新版 [`0088aeb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aea8.md#insn-0088aeb8) · [`0088aec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aea8.md#insn-0088aec4)

~~~diff
- 0088ae60 ["COPY", "tmp:0:8", ["const:660:8"]]
- 0088ae60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088ae60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088ae60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088aeb8 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 0088aeb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088aeb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088aeb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088ae60 bytes 08811991
+ 0088aeb8 bytes 08c11c91
- 0088ae6c ["INT_ADD", "register:40f0:8", ["const:88ae6c:8", "const:4:8"]]
- 0088ae6c ["CALL", null, ["callee:00c57f70:8"]]
+ 0088aec4 ["INT_ADD", "register:40f0:8", ["const:88aec4:8", "const:4:8"]]
+ 0088aec4 ["CALL", null, ["callee:00c57f70:8"]]
- 0088ae6c bytes 0d340f94
+ 0088aec4 bytes 2b340f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a67d450d91ac165e5993afb4688e37ab"></a>

### [`0088ae8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae8c.md) → [`0088aee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aee4.md) FUN_0088aee4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088af1c",
      "incomplete_value": false,
      "site": "0088af28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088aec4",
      "incomplete_value": false,
      "site": "0088aed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "definition_site": "0088af3c",
      "incomplete_value": false,
      "site": "0088af40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088aee4",
      "incomplete_value": false,
      "site": "0088aee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "definition_site": "0088af6c",
      "incomplete_value": false,
      "site": "0088af74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:a66:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088af14",
      "incomplete_value": false,
      "site": "0088af1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:ac2:8"
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
      "0088af28",
      "DATA",
      [
        "storage",
        "00c816b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088af40",
      "DATA",
      [
        "storage",
        "00c81098",
        null,
        "pointer"
      ]
    ],
    [
      "0088af5c",
      "PARAM",
      [
        "storage",
        "002b41db",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088af28",
      "DATA",
      [
        "storage",
        "00c81780",
        null,
        "undefined *"
      ]
    ],
    [
      "0088af40",
      "DATA",
      [
        "storage",
        "00c81168",
        null,
        "pointer"
      ]
    ],
    [
      "0088af5c",
      "PARAM",
      [
        "storage",
        "002b420c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088aec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae8c.md#insn-0088aec4) · [`0088af1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae8c.md#insn-0088af1c) · [`0088aeb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae8c.md#insn-0088aeb0)
- 新版 [`0088af1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aee4.md#insn-0088af1c) · [`0088af74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aee4.md#insn-0088af74) · [`0088af08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aee4.md#insn-0088af08)

~~~diff
- 0088aec4 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 0088aec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088aec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088aec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088af1c ["COPY", "tmp:0:8", ["const:780:8"]]
+ 0088af1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088af1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088af1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088aec4 bytes 08c11a91
+ 0088af1c bytes 08011e91
- 0088af1c ["INT_ADD", "register:40f0:8", ["const:88af1c:8", "const:4:8"]]
- 0088af1c ["CALL", null, ["callee:00c58260:8"]]
+ 0088af74 ["INT_ADD", "register:40f0:8", ["const:88af74:8", "const:4:8"]]
+ 0088af74 ["CALL", null, ["callee:00c58260:8"]]
- 0088af1c bytes 9d340f94
+ 0088af74 bytes bb340f94
- 0088aeb0 ["INT_ADD", "register:40f0:8", ["const:88aeb0:8", "const:4:8"]]
- 0088aeb0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088af08 ["INT_ADD", "register:40f0:8", ["const:88af08:8", "const:4:8"]]
+ 0088af08 ["CALL", null, ["callee:00c57f60:8"]]
- 0088aeb0 bytes f8330f94
+ 0088af08 bytes 16340f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b055f1e88c85e22275590a57fcc1733"></a>

### [`0088af64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088af64.md) → [`0088afbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088afbc.md) FUN_0088afbc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088afc0",
      "incomplete_value": false,
      "site": "0088afc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088af68",
      "incomplete_value": false,
      "site": "0088af6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088afc4",
      "DATA",
      [
        "storage",
        "00c816b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088afc4",
      "DATA",
      [
        "storage",
        "00c81780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088af68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088af64.md#insn-0088af68)
- 新版 [`0088afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088afbc.md#insn-0088afc0)

~~~diff
- 0088af68 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 0088af68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088af68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088af68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088afc0 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 0088afc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088afc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088afc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088af68 bytes 08c11a91
+ 0088afc0 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fcbcdee460cb9e6461448b80ea6f136"></a>

### [`0088af74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088af74.md) → [`0088afcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088afcc.md) FUN_0088afcc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088afdc",
      "incomplete_value": false,
      "site": "0088afe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088af84",
      "incomplete_value": false,
      "site": "0088af8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "0088afe4",
      "DATA",
      [
        "storage",
        "00c816b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088afe4",
      "DATA",
      [
        "storage",
        "00c81780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088af84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088af74.md#insn-0088af84) · [`0088af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088af74.md#insn-0088af90)
- 新版 [`0088afdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088afcc.md#insn-0088afdc) · [`0088afe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088afcc.md#insn-0088afe8)

~~~diff
- 0088af84 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 0088af84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088af84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088af84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088afdc ["COPY", "tmp:0:8", ["const:780:8"]]
+ 0088afdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088afdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088afdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088af84 bytes 08c11a91
+ 0088afdc bytes 08011e91
- 0088af90 ["INT_ADD", "register:40f0:8", ["const:88af90:8", "const:4:8"]]
- 0088af90 ["CALL", null, ["callee:00c57f70:8"]]
+ 0088afe8 ["INT_ADD", "register:40f0:8", ["const:88afe8:8", "const:4:8"]]
+ 0088afe8 ["CALL", null, ["callee:00c57f70:8"]]
- 0088af90 bytes c4330f94
+ 0088afe8 bytes e2330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07bf3a777bff9561bb027575f9051f5d"></a>

### [`0088afb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088afb0.md) → [`0088b008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b008.md) FUN_0088b008

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

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
      "definition_site": "0088b040",
      "incomplete_value": false,
      "site": "0088b04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088afe8",
      "incomplete_value": false,
      "site": "0088aff4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "0088b060",
      "incomplete_value": false,
      "site": "0088b064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b008",
      "incomplete_value": false,
      "site": "0088b00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:b8:8"
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
      "definition_site": "0088b080",
      "incomplete_value": false,
      "site": "0088b088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:a74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b028",
      "incomplete_value": false,
      "site": "0088b030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "0088b04c",
      "DATA",
      [
        "storage",
        "00c81700",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b064",
      "DATA",
      [
        "storage",
        "00c810b8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b080",
      "PARAM",
      [
        "storage",
        "002abad0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b04c",
      "DATA",
      [
        "storage",
        "00c817d0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b064",
      "DATA",
      [
        "storage",
        "00c81188",
        null,
        "pointer"
      ]
    ],
    [
      "0088b080",
      "PARAM",
      [
        "storage",
        "002aba74",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088afe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088afb0.md#insn-0088afe8) · [`0088b030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088afb0.md#insn-0088b030) · [`0088b040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088afb0.md#insn-0088b040)
- 新版 [`0088b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b008.md#insn-0088b040) · [`0088b088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b008.md#insn-0088b088) · [`0088b098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b008.md#insn-0088b098)

~~~diff
- 0088afe8 ["COPY", "tmp:0:8", ["const:700:8"]]
- 0088afe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088afe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088afe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b040 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 0088b040 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b040 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b040 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088afe8 bytes 08011c91
+ 0088b040 bytes 08411f91
- 0088b030 ["INT_ADD", "register:40f0:8", ["const:88b030:8", "const:4:8"]]
- 0088b030 ["CALL", null, ["callee:00c58260:8"]]
+ 0088b088 ["INT_ADD", "register:40f0:8", ["const:88b088:8", "const:4:8"]]
+ 0088b088 ["CALL", null, ["callee:00c58260:8"]]
- 0088b030 bytes 58340f94
+ 0088b088 bytes 76340f94
- 0088b040 ["INT_ADD", "register:40f0:8", ["const:88b040:8", "const:4:8"]]
- 0088b040 ["CALL", null, ["callee:00c58260:8"]]
+ 0088b098 ["INT_ADD", "register:40f0:8", ["const:88b098:8", "const:4:8"]]
+ 0088b098 ["CALL", null, ["callee:00c58260:8"]]
- 0088b040 bytes 54340f94
+ 0088b098 bytes 72340f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c85337733c1682596c3df5665b4f18b1"></a>

### [`0088b088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b088.md) → [`0088b0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b0e0.md) FUN_0088b0e0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b0e4",
      "incomplete_value": false,
      "site": "0088b0e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b08c",
      "incomplete_value": false,
      "site": "0088b090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "0088b0e8",
      "DATA",
      [
        "storage",
        "00c81700",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b0e8",
      "DATA",
      [
        "storage",
        "00c817d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b088.md#insn-0088b08c)
- 新版 [`0088b0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b0e0.md#insn-0088b0e4)

~~~diff
- 0088b08c ["COPY", "tmp:0:8", ["const:700:8"]]
- 0088b08c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b08c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b08c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b0e4 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 0088b0e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b0e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b0e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b08c bytes 08011c91
+ 0088b0e4 bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6397e37465b8cd77573f9d9e07b0531"></a>

### [`0088b098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b098.md) → [`0088b0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b0f0.md) FUN_0088b0f0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b100",
      "incomplete_value": false,
      "site": "0088b108",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b0a8",
      "incomplete_value": false,
      "site": "0088b0b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "0088b108",
      "DATA",
      [
        "storage",
        "00c81700",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b108",
      "DATA",
      [
        "storage",
        "00c817d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b098.md#insn-0088b0a8) · [`0088b0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b098.md#insn-0088b0b4)
- 新版 [`0088b100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b0f0.md#insn-0088b100) · [`0088b10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b0f0.md#insn-0088b10c)

~~~diff
- 0088b0a8 ["COPY", "tmp:0:8", ["const:700:8"]]
- 0088b0a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b0a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b0a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b100 ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 0088b100 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b100 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b100 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b0a8 bytes 08011c91
+ 0088b100 bytes 08411f91
- 0088b0b4 ["INT_ADD", "register:40f0:8", ["const:88b0b4:8", "const:4:8"]]
- 0088b0b4 ["CALL", null, ["callee:00c57f70:8"]]
+ 0088b10c ["INT_ADD", "register:40f0:8", ["const:88b10c:8", "const:4:8"]]
+ 0088b10c ["CALL", null, ["callee:00c57f70:8"]]
- 0088b0b4 bytes 7b330f94
+ 0088b10c bytes 99330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86333ec49beb1fe8534960afccf9f26a"></a>

### [`0088b0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b0d4.md) → [`0088b12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b12c.md) FUN_0088b12c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

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
      "definition_site": "0088b164",
      "incomplete_value": false,
      "site": "0088b170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b10c",
      "incomplete_value": false,
      "site": "0088b118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "definition_site": "0088b184",
      "incomplete_value": false,
      "site": "0088b188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b12c",
      "incomplete_value": false,
      "site": "0088b130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "definition_site": "0088b1a0",
      "incomplete_value": false,
      "site": "0088b1a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:52d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b148",
      "incomplete_value": false,
      "site": "0088b150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:581:8"
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
      "0088b170",
      "DATA",
      [
        "storage",
        "00c81750",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b188",
      "DATA",
      [
        "storage",
        "00c810f8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b1a0",
      "PARAM",
      [
        "storage",
        "002b9581",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b170",
      "DATA",
      [
        "storage",
        "00c81820",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b188",
      "DATA",
      [
        "storage",
        "00c811c8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b1a0",
      "PARAM",
      [
        "storage",
        "002b952d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b0d4.md#insn-0088b0f8) · [`0088b150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b0d4.md#insn-0088b150) · [`0088b160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b0d4.md#insn-0088b160)
- 新版 [`0088b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b12c.md#insn-0088b150) · [`0088b1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b12c.md#insn-0088b1a8) · [`0088b1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b12c.md#insn-0088b1b8)

~~~diff
- 0088b0f8 ["INT_ADD", "register:40f0:8", ["const:88b0f8:8", "const:4:8"]]
- 0088b0f8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088b150 ["INT_ADD", "register:40f0:8", ["const:88b150:8", "const:4:8"]]
+ 0088b150 ["CALL", null, ["callee:00c57f60:8"]]
- 0088b0f8 bytes 66330f94
+ 0088b150 bytes 84330f94
- 0088b150 ["INT_ADD", "register:40f0:8", ["const:88b150:8", "const:4:8"]]
- 0088b150 ["CALL", null, ["callee:00c58260:8"]]
+ 0088b1a8 ["INT_ADD", "register:40f0:8", ["const:88b1a8:8", "const:4:8"]]
+ 0088b1a8 ["CALL", null, ["callee:00c58260:8"]]
- 0088b150 bytes 10340f94
+ 0088b1a8 bytes 2e340f94
- 0088b160 ["INT_ADD", "register:40f0:8", ["const:88b160:8", "const:4:8"]]
- 0088b160 ["CALL", null, ["callee:00c58260:8"]]
+ 0088b1b8 ["INT_ADD", "register:40f0:8", ["const:88b1b8:8", "const:4:8"]]
+ 0088b1b8 ["CALL", null, ["callee:00c58260:8"]]
- 0088b160 bytes 0c340f94
+ 0088b1b8 bytes 2a340f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff043abc124322e33f527a992f97f180"></a>

### [`0088b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1a8.md) → [`0088b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b200.md) FUN_0088b200

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b204",
      "incomplete_value": false,
      "site": "0088b208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b1ac",
      "incomplete_value": false,
      "site": "0088b1b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "0088b208",
      "DATA",
      [
        "storage",
        "00c81750",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b208",
      "DATA",
      [
        "storage",
        "00c81820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1a8.md#insn-0088b1ac)
- 新版 [`0088b204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b200.md#insn-0088b204)

~~~diff
- 0088b1ac ["COPY", "tmp:0:8", ["const:750:8"]]
- 0088b1ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b1ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b1ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b204 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 0088b204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b1ac bytes 08411d91
+ 0088b204 bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6dd6bd895aa7d60c56d5002cb3b786f"></a>

### [`0088b1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1b8.md) → [`0088b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b210.md) FUN_0088b210

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b220",
      "incomplete_value": false,
      "site": "0088b228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b1c8",
      "incomplete_value": false,
      "site": "0088b1d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "0088b228",
      "DATA",
      [
        "storage",
        "00c81750",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b228",
      "DATA",
      [
        "storage",
        "00c81820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1b8.md#insn-0088b1c8) · [`0088b1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1b8.md#insn-0088b1d4)
- 新版 [`0088b220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b210.md#insn-0088b220) · [`0088b22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b210.md#insn-0088b22c)

~~~diff
- 0088b1c8 ["COPY", "tmp:0:8", ["const:750:8"]]
- 0088b1c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b1c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b1c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b220 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 0088b220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b1c8 bytes 08411d91
+ 0088b220 bytes 08812091
- 0088b1d4 ["INT_ADD", "register:40f0:8", ["const:88b1d4:8", "const:4:8"]]
- 0088b1d4 ["CALL", null, ["callee:00c57f70:8"]]
+ 0088b22c ["INT_ADD", "register:40f0:8", ["const:88b22c:8", "const:4:8"]]
+ 0088b22c ["CALL", null, ["callee:00c57f70:8"]]
- 0088b1d4 bytes 33330f94
+ 0088b22c bytes 51330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-243c81ada51909492026dda7b09f02c3"></a>

### [`0088b1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1f4.md) → [`0088b24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b24c.md) FUN_0088b24c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

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
      "definition_site": "0088b284",
      "incomplete_value": false,
      "site": "0088b290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b22c",
      "incomplete_value": false,
      "site": "0088b238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "definition_site": "0088b2a4",
      "incomplete_value": false,
      "site": "0088b2a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b24c",
      "incomplete_value": false,
      "site": "0088b250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "definition_site": "0088b2c0",
      "incomplete_value": false,
      "site": "0088b2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:6a3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b268",
      "incomplete_value": false,
      "site": "0088b270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:6f7:8"
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
      "0088b290",
      "DATA",
      [
        "storage",
        "00c817a0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b2a8",
      "DATA",
      [
        "storage",
        "00c810d8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b2c0",
      "PARAM",
      [
        "storage",
        "002b86f7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b290",
      "DATA",
      [
        "storage",
        "00c81870",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b2a8",
      "DATA",
      [
        "storage",
        "00c811a8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b2c0",
      "PARAM",
      [
        "storage",
        "002b86a3",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1f4.md#insn-0088b218) · [`0088b270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1f4.md#insn-0088b270) · [`0088b280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1f4.md#insn-0088b280)
- 新版 [`0088b270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b24c.md#insn-0088b270) · [`0088b2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b24c.md#insn-0088b2c8) · [`0088b2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b24c.md#insn-0088b2d8)

~~~diff
- 0088b218 ["INT_ADD", "register:40f0:8", ["const:88b218:8", "const:4:8"]]
- 0088b218 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088b270 ["INT_ADD", "register:40f0:8", ["const:88b270:8", "const:4:8"]]
+ 0088b270 ["CALL", null, ["callee:00c57f60:8"]]
- 0088b218 bytes 1e330f94
+ 0088b270 bytes 3c330f94
- 0088b270 ["INT_ADD", "register:40f0:8", ["const:88b270:8", "const:4:8"]]
- 0088b270 ["CALL", null, ["callee:00c58260:8"]]
+ 0088b2c8 ["INT_ADD", "register:40f0:8", ["const:88b2c8:8", "const:4:8"]]
+ 0088b2c8 ["CALL", null, ["callee:00c58260:8"]]
- 0088b270 bytes c8330f94
+ 0088b2c8 bytes e6330f94
- 0088b280 ["INT_ADD", "register:40f0:8", ["const:88b280:8", "const:4:8"]]
- 0088b280 ["CALL", null, ["callee:00c58260:8"]]
+ 0088b2d8 ["INT_ADD", "register:40f0:8", ["const:88b2d8:8", "const:4:8"]]
+ 0088b2d8 ["CALL", null, ["callee:00c58260:8"]]
- 0088b280 bytes c4330f94
+ 0088b2d8 bytes e2330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eee2bd81e9d08c0cfe8a4911f94c7d9"></a>

### [`0088b2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b2c8.md) → [`0088b320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b320.md) FUN_0088b320

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b324",
      "incomplete_value": false,
      "site": "0088b328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b2cc",
      "incomplete_value": false,
      "site": "0088b2d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "0088b328",
      "DATA",
      [
        "storage",
        "00c817a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b328",
      "DATA",
      [
        "storage",
        "00c81870",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b2c8.md#insn-0088b2cc)
- 新版 [`0088b324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b320.md#insn-0088b324)

~~~diff
- 0088b2cc ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 0088b2cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b2cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b2cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b324 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 0088b324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b2cc bytes 08811e91
+ 0088b324 bytes 08c12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8412e8a3d9dd60e26192e65868daaed0"></a>

### [`0088b2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b2d8.md) → [`0088b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b330.md) FUN_0088b330

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b340",
      "incomplete_value": false,
      "site": "0088b348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b2e8",
      "incomplete_value": false,
      "site": "0088b2f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "0088b348",
      "DATA",
      [
        "storage",
        "00c817a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b348",
      "DATA",
      [
        "storage",
        "00c81870",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b2d8.md#insn-0088b2e8) · [`0088b2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b2d8.md#insn-0088b2f4)
- 新版 [`0088b340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b330.md#insn-0088b340) · [`0088b34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b330.md#insn-0088b34c)

~~~diff
- 0088b2e8 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 0088b2e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b2e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b2e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b340 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 0088b340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b2e8 bytes 08811e91
+ 0088b340 bytes 08c12191
- 0088b2f4 ["INT_ADD", "register:40f0:8", ["const:88b2f4:8", "const:4:8"]]
- 0088b2f4 ["CALL", null, ["callee:00c57f70:8"]]
+ 0088b34c ["INT_ADD", "register:40f0:8", ["const:88b34c:8", "const:4:8"]]
+ 0088b34c ["CALL", null, ["callee:00c57f70:8"]]
- 0088b2f4 bytes eb320f94
+ 0088b34c bytes 09330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5bf9f95045d64f3da83c48b467988b7"></a>

### [`0088b314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b314.md) → [`0088b36c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b36c.md) FUN_0088b36c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`0088a8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a8e4.md) [`0088ae80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088ae80.md) [`0088afa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088afa4.md) [`0088b0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b0c8.md) [`0088b1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b1e8.md) · 呼出先 3件 [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 7件 [`0088a93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a93c.md) [`0088aed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088aed8.md) [`0088affc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088affc.md) [`0088b120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b120.md) [`0088b240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b240.md) · 呼出先 3件 [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "0088b390",
      "incomplete_value": false,
      "site": "0088b394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b338",
      "incomplete_value": false,
      "site": "0088b33c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:38:8"
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
      "0088b394",
      "DATA",
      [
        "storage",
        "00c81038",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0088b394",
      "DATA",
      [
        "storage",
        "00c81108",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b314.md#insn-0088b338) · [`0088b34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b314.md#insn-0088b34c) · [`0088b35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b314.md#insn-0088b35c)
- 新版 [`0088b390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b36c.md#insn-0088b390) · [`0088b3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b36c.md#insn-0088b3a4) · [`0088b3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b36c.md#insn-0088b3b4)

~~~diff
- 0088b338 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0088b338 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b338 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b338 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b390 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 0088b390 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b390 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b390 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b338 bytes 08e10091
+ 0088b390 bytes 08210491
- 0088b34c ["INT_ADD", "register:40f0:8", ["const:88b34c:8", "const:4:8"]]
- 0088b34c ["CALL", null, ["callee:00597f0c:8"]]
+ 0088b3a4 ["INT_ADD", "register:40f0:8", ["const:88b3a4:8", "const:4:8"]]
+ 0088b3a4 ["CALL", null, ["callee:00597f0c:8"]]
- 0088b34c bytes e032f497
+ 0088b3a4 bytes da32f497
- 0088b35c ["INT_ADD", "register:40f0:8", ["const:88b35c:8", "const:4:8"]]
- 0088b35c ["CALL", null, ["callee:00c57f80:8"]]
+ 0088b3b4 ["INT_ADD", "register:40f0:8", ["const:88b3b4:8", "const:4:8"]]
+ 0088b3b4 ["CALL", null, ["callee:00c57f80:8"]]
- 0088b35c bytes d5320f94
+ 0088b3b4 bytes f3320f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa9bb0428bba60de40ba5527dab6d7ae"></a>

### [`0088b498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b498.md) → [`0088b4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b4f0.md) FUN_0088b4f0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

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
      "definition_site": "0088b53c",
      "incomplete_value": false,
      "site": "0088b548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b4e4",
      "incomplete_value": false,
      "site": "0088b4f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
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
      "definition_site": "0088b558",
      "incomplete_value": false,
      "site": "0088b560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b500",
      "incomplete_value": false,
      "site": "0088b508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "definition_site": "0088b57c",
      "incomplete_value": false,
      "site": "0088b584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b524",
      "incomplete_value": false,
      "site": "0088b52c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:704:8"
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
      "0088b548",
      "DATA",
      [
        "storage",
        "00c817f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b560",
      "DATA",
      [
        "storage",
        "00c81118",
        null,
        "pointer"
      ]
    ],
    [
      "0088b57c",
      "PARAM",
      [
        "storage",
        "002b8704",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b548",
      "DATA",
      [
        "storage",
        "00c818c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b560",
      "DATA",
      [
        "storage",
        "00c811e8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b57c",
      "PARAM",
      [
        "storage",
        "002b86b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b498.md#insn-0088b4e4) · [`0088b52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b498.md#insn-0088b52c) · [`0088b53c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b498.md#insn-0088b53c)
- 新版 [`0088b53c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b4f0.md#insn-0088b53c) · [`0088b584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b4f0.md#insn-0088b584) · [`0088b594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b4f0.md#insn-0088b594)

~~~diff
- 0088b4e4 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 0088b4e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b4e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b4e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b53c ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 0088b53c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b53c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b53c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b4e4 bytes 08c11f91
+ 0088b53c bytes 08012391
- 0088b52c ["INT_ADD", "register:40f0:8", ["const:88b52c:8", "const:4:8"]]
- 0088b52c ["CALL", null, ["callee:00c58260:8"]]
+ 0088b584 ["INT_ADD", "register:40f0:8", ["const:88b584:8", "const:4:8"]]
+ 0088b584 ["CALL", null, ["callee:00c58260:8"]]
- 0088b52c bytes 19330f94
+ 0088b584 bytes 37330f94
- 0088b53c ["INT_ADD", "register:40f0:8", ["const:88b53c:8", "const:4:8"]]
- 0088b53c ["CALL", null, ["callee:00c58260:8"]]
+ 0088b594 ["INT_ADD", "register:40f0:8", ["const:88b594:8", "const:4:8"]]
+ 0088b594 ["CALL", null, ["callee:00c58260:8"]]
- 0088b53c bytes 15330f94
+ 0088b594 bytes 33330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06f0c07e8f93ca1be556888ac029ebb9"></a>

### [`0088b588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b588.md) → [`0088b5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b5e0.md) FUN_0088b5e0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b5e4",
      "incomplete_value": false,
      "site": "0088b5e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b58c",
      "incomplete_value": false,
      "site": "0088b590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
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
      "0088b5e8",
      "DATA",
      [
        "storage",
        "00c817f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b5e8",
      "DATA",
      [
        "storage",
        "00c818c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b588.md#insn-0088b58c)
- 新版 [`0088b5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b5e0.md#insn-0088b5e4)

~~~diff
- 0088b58c ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 0088b58c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b58c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b58c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b5e4 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 0088b5e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b5e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b5e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b58c bytes 08c11f91
+ 0088b5e4 bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fe9e7ed5b69c0503b097df63f25e2ec"></a>

### [`0088b598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b598.md) → [`0088b5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b5f0.md) FUN_0088b5f0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088b600",
      "incomplete_value": false,
      "site": "0088b608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b5a8",
      "incomplete_value": false,
      "site": "0088b5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088b608",
      "DATA",
      [
        "storage",
        "00c817f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b608",
      "DATA",
      [
        "storage",
        "00c818c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b598.md#insn-0088b5a8) · [`0088b5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b598.md#insn-0088b5b4)
- 新版 [`0088b600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b5f0.md#insn-0088b600) · [`0088b60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b5f0.md#insn-0088b60c)

~~~diff
- 0088b5a8 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 0088b5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b600 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 0088b600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b5a8 bytes 08c11f91
+ 0088b600 bytes 08012391
- 0088b5b4 ["INT_ADD", "register:40f0:8", ["const:88b5b4:8", "const:4:8"]]
- 0088b5b4 ["CALL", null, ["callee:00c57f70:8"]]
+ 0088b60c ["INT_ADD", "register:40f0:8", ["const:88b60c:8", "const:4:8"]]
+ 0088b60c ["CALL", null, ["callee:00c57f70:8"]]
- 0088b5b4 bytes 3b320f94
+ 0088b60c bytes 59320f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d18008c0466f28a1fd9a393a3e467db9"></a>

### [`0088b5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b5c8.md) → [`0088b620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b620.md) FUN_0088b620

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`0088b314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b314.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md) [`0088b36c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b36c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "0088b648",
      "incomplete_value": false,
      "site": "0088b648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b5f0",
      "incomplete_value": false,
      "site": "0088b5f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "0088b648",
      "DATA",
      [
        "storage",
        "00c81118",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0088b648",
      "DATA",
      [
        "storage",
        "00c811e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b5c8.md#insn-0088b5e4) · [`0088b600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b5c8.md#insn-0088b600) · [`0088b610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b5c8.md#insn-0088b610)
- 新版 [`0088b63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b620.md#insn-0088b63c) · [`0088b658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b620.md#insn-0088b658) · [`0088b668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b620.md#insn-0088b668)

~~~diff
- 0088b5e4 ["COPY", "tmp:0:8", ["const:118:8"]]
- 0088b5e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088b5e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088b5e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088b63c ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 0088b63c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088b63c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088b63c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088b5e4 bytes 29610491
+ 0088b63c bytes 29a10791
- 0088b600 ["INT_ADD", "register:40f0:8", ["const:88b600:8", "const:4:8"]]
- 0088b600 ["CALL", null, ["callee:00597f0c:8"]]
+ 0088b658 ["INT_ADD", "register:40f0:8", ["const:88b658:8", "const:4:8"]]
+ 0088b658 ["CALL", null, ["callee:00597f0c:8"]]
- 0088b600 bytes 3332f497
+ 0088b658 bytes 2d32f497
- 0088b610 ["INT_ADD", "register:40f0:8", ["const:88b610:8", "const:4:8"]]
- 0088b610 ["CALL", null, ["callee:00c57f80:8"]]
+ 0088b668 ["INT_ADD", "register:40f0:8", ["const:88b668:8", "const:4:8"]]
+ 0088b668 ["CALL", null, ["callee:00c57f80:8"]]
- 0088b610 bytes 28320f94
+ 0088b668 bytes 46320f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52c0770e8736968980753de78200b7af"></a>

### [`0088b648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b648.md) → [`0088b6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b6a0.md) FUN_0088b6a0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

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
      "definition_site": "0088b6d8",
      "incomplete_value": false,
      "site": "0088b6e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b680",
      "incomplete_value": false,
      "site": "0088b68c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "definition_site": "0088b6f8",
      "incomplete_value": false,
      "site": "0088b6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b6a0",
      "incomplete_value": false,
      "site": "0088b6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "definition_site": "0088b718",
      "incomplete_value": false,
      "site": "0088b720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:52d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b6c0",
      "incomplete_value": false,
      "site": "0088b6c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:581:8"
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
      "0088b6e4",
      "DATA",
      [
        "storage",
        "00c81750",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b6fc",
      "DATA",
      [
        "storage",
        "00c810f8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b718",
      "PARAM",
      [
        "storage",
        "002b9581",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b6e4",
      "DATA",
      [
        "storage",
        "00c81820",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b6fc",
      "DATA",
      [
        "storage",
        "00c811c8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b718",
      "PARAM",
      [
        "storage",
        "002b952d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b648.md#insn-0088b680) · [`0088b6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b648.md#insn-0088b6c8) · [`0088b6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b648.md#insn-0088b6d8)
- 新版 [`0088b6d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b6a0.md#insn-0088b6d8) · [`0088b720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b6a0.md#insn-0088b720) · [`0088b730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b6a0.md#insn-0088b730)

~~~diff
- 0088b680 ["COPY", "tmp:0:8", ["const:750:8"]]
- 0088b680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b6d8 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 0088b6d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b6d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b6d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b680 bytes 08411d91
+ 0088b6d8 bytes 08812091
- 0088b6c8 ["INT_ADD", "register:40f0:8", ["const:88b6c8:8", "const:4:8"]]
- 0088b6c8 ["CALL", null, ["callee:00c58260:8"]]
+ 0088b720 ["INT_ADD", "register:40f0:8", ["const:88b720:8", "const:4:8"]]
+ 0088b720 ["CALL", null, ["callee:00c58260:8"]]
- 0088b6c8 bytes b2320f94
+ 0088b720 bytes d0320f94
- 0088b6d8 ["INT_ADD", "register:40f0:8", ["const:88b6d8:8", "const:4:8"]]
- 0088b6d8 ["CALL", null, ["callee:00c58260:8"]]
+ 0088b730 ["INT_ADD", "register:40f0:8", ["const:88b730:8", "const:4:8"]]
+ 0088b730 ["CALL", null, ["callee:00c58260:8"]]
- 0088b6d8 bytes ae320f94
+ 0088b730 bytes cc320f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf7bae65a9bc4e686708dec2a03a514b"></a>

### [`0088b720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b720.md) → [`0088b778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b778.md) FUN_0088b778

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

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
      "definition_site": "0088b7b0",
      "incomplete_value": false,
      "site": "0088b7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b758",
      "incomplete_value": false,
      "site": "0088b764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "definition_site": "0088b7d0",
      "incomplete_value": false,
      "site": "0088b7d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b778",
      "incomplete_value": false,
      "site": "0088b77c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "definition_site": "0088b7f0",
      "incomplete_value": false,
      "site": "0088b7f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:6a3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b798",
      "incomplete_value": false,
      "site": "0088b7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:6f7:8"
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
      "0088b7bc",
      "DATA",
      [
        "storage",
        "00c817a0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b7d4",
      "DATA",
      [
        "storage",
        "00c810d8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b7f0",
      "PARAM",
      [
        "storage",
        "002b86f7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b7bc",
      "DATA",
      [
        "storage",
        "00c81870",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b7d4",
      "DATA",
      [
        "storage",
        "00c811a8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b7f0",
      "PARAM",
      [
        "storage",
        "002b86a3",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b720.md#insn-0088b758) · [`0088b7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b720.md#insn-0088b7a0) · [`0088b7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b720.md#insn-0088b7b0)
- 新版 [`0088b7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b778.md#insn-0088b7b0) · [`0088b7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b778.md#insn-0088b7f8) · [`0088b808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b778.md#insn-0088b808)

~~~diff
- 0088b758 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 0088b758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b7b0 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 0088b7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b758 bytes 08811e91
+ 0088b7b0 bytes 08c12191
- 0088b7a0 ["INT_ADD", "register:40f0:8", ["const:88b7a0:8", "const:4:8"]]
- 0088b7a0 ["CALL", null, ["callee:00c58260:8"]]
+ 0088b7f8 ["INT_ADD", "register:40f0:8", ["const:88b7f8:8", "const:4:8"]]
+ 0088b7f8 ["CALL", null, ["callee:00c58260:8"]]
- 0088b7a0 bytes 7c320f94
+ 0088b7f8 bytes 9a320f94
- 0088b7b0 ["INT_ADD", "register:40f0:8", ["const:88b7b0:8", "const:4:8"]]
- 0088b7b0 ["CALL", null, ["callee:00c58260:8"]]
+ 0088b808 ["INT_ADD", "register:40f0:8", ["const:88b808:8", "const:4:8"]]
+ 0088b808 ["CALL", null, ["callee:00c58260:8"]]
- 0088b7b0 bytes 78320f94
+ 0088b808 bytes 96320f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d27d86da963b9925e00ea37087dc0841"></a>

### [`0088b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b7f8.md) → [`0088b850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b850.md) FUN_0088b850

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008878d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/008878d8.md) · 呼出先 3件 [`00887478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00887/00887478.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00887930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/00887930.md) · 呼出先 3件 [`008874d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00887/008874d0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

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
      "definition_site": "0088b89c",
      "incomplete_value": false,
      "site": "0088b8a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b844",
      "incomplete_value": false,
      "site": "0088b850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
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
      "definition_site": "0088b8b8",
      "incomplete_value": false,
      "site": "0088b8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b860",
      "incomplete_value": false,
      "site": "0088b868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "definition_site": "0088b8dc",
      "incomplete_value": false,
      "site": "0088b8e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b884",
      "incomplete_value": false,
      "site": "0088b88c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:704:8"
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
      "0088b8a8",
      "DATA",
      [
        "storage",
        "00c817f0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b8c0",
      "DATA",
      [
        "storage",
        "00c81118",
        null,
        "pointer"
      ]
    ],
    [
      "0088b8dc",
      "PARAM",
      [
        "storage",
        "002b8704",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088b8a8",
      "DATA",
      [
        "storage",
        "00c818c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0088b8c0",
      "DATA",
      [
        "storage",
        "00c811e8",
        null,
        "pointer"
      ]
    ],
    [
      "0088b8dc",
      "PARAM",
      [
        "storage",
        "002b86b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b7f8.md#insn-0088b844) · [`0088b88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b7f8.md#insn-0088b88c) · [`0088b89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b7f8.md#insn-0088b89c)
- 新版 [`0088b89c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b850.md#insn-0088b89c) · [`0088b8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b850.md#insn-0088b8e4) · [`0088b8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b850.md#insn-0088b8f4)

~~~diff
- 0088b844 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 0088b844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b89c ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 0088b89c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b89c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b89c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b844 bytes 08c11f91
+ 0088b89c bytes 08012391
- 0088b88c ["INT_ADD", "register:40f0:8", ["const:88b88c:8", "const:4:8"]]
- 0088b88c ["CALL", null, ["callee:00c58260:8"]]
+ 0088b8e4 ["INT_ADD", "register:40f0:8", ["const:88b8e4:8", "const:4:8"]]
+ 0088b8e4 ["CALL", null, ["callee:00c58260:8"]]
- 0088b88c bytes 41320f94
+ 0088b8e4 bytes 5f320f94
- 0088b89c ["INT_ADD", "register:40f0:8", ["const:88b89c:8", "const:4:8"]]
- 0088b89c ["CALL", null, ["callee:00c58260:8"]]
+ 0088b8f4 ["INT_ADD", "register:40f0:8", ["const:88b8f4:8", "const:4:8"]]
+ 0088b8f4 ["CALL", null, ["callee:00c58260:8"]]
- 0088b89c bytes 3d320f94
+ 0088b8f4 bytes 5b320f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-646077c9be47de16f1f5aeda9d6bf1b3"></a>

### [`0088b8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b8f0.md) → [`0088b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b948.md) FUN_0088b948

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
      "definition_site": "0088b96c",
      "incomplete_value": false,
      "site": "0088b96c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b914",
      "incomplete_value": false,
      "site": "0088b914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088b96c",
      "DATA",
      [
        "storage",
        "00c81840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b96c",
      "DATA",
      [
        "storage",
        "00c81910",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b8f0.md#insn-0088b904) · [`0088b910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b8f0.md#insn-0088b910)
- 新版 [`0088b95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b948.md#insn-0088b95c) · [`0088b968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b948.md#insn-0088b968)

~~~diff
- 0088b904 ["INT_ADD", "register:40f0:8", ["const:88b904:8", "const:4:8"]]
- 0088b904 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088b95c ["INT_ADD", "register:40f0:8", ["const:88b95c:8", "const:4:8"]]
+ 0088b95c ["CALL", null, ["callee:00c57f60:8"]]
- 0088b904 bytes 63310f94
+ 0088b95c bytes 81310f94
- 0088b910 ["COPY", "tmp:0:8", ["const:840:8"]]
- 0088b910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088b910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088b910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088b968 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 0088b968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088b968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088b910 bytes 08012191
+ 0088b968 bytes 08412491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afc70b93151a9007ba29f6f25312fa0a"></a>

### [`0088b924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b924.md) → [`0088b97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b97c.md) FUN_0088b97c

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
      "definition_site": "0088b988",
      "incomplete_value": false,
      "site": "0088b988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088b930",
      "incomplete_value": false,
      "site": "0088b930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088b988",
      "DATA",
      [
        "storage",
        "00c81840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088b988",
      "DATA",
      [
        "storage",
        "00c81910",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088b92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088b924.md#insn-0088b92c)
- 新版 [`0088b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088b97c.md#insn-0088b984)

~~~diff
- 0088b92c ["COPY", "tmp:0:8", ["const:840:8"]]
- 0088b92c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088b92c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088b92c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088b984 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 0088b984 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088b984 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088b984 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088b92c bytes 29012191
+ 0088b984 bytes 29412491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66b37d144a09395efd6b5bb56866c4c7"></a>

### [`0088ba34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba34.md) → [`0088ba8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088ba8c.md) FUN_0088ba8c

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
      "definition_site": "0088ba98",
      "incomplete_value": false,
      "site": "0088ba98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088ba40",
      "incomplete_value": false,
      "site": "0088ba40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088ba98",
      "DATA",
      [
        "storage",
        "00c818c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088ba98",
      "DATA",
      [
        "storage",
        "00c81990",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088ba3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088ba34.md#insn-0088ba3c)
- 新版 [`0088ba94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088ba8c.md#insn-0088ba94)

~~~diff
- 0088ba3c ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 0088ba3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088ba3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088ba3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088ba94 ["COPY", "tmp:0:8", ["const:990:8"]]
+ 0088ba94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088ba94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088ba94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088ba3c bytes 29012391
+ 0088ba94 bytes 29412691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24c521058cf0e39bd86b2b826751184c"></a>

### [`0088bb2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bb2c.md) → [`0088bb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bb84.md) FUN_0088bb84

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
      "definition_site": "0088bb90",
      "incomplete_value": false,
      "site": "0088bb90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088bb38",
      "incomplete_value": false,
      "site": "0088bb38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:940:8"
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
      "0088bb90",
      "DATA",
      [
        "storage",
        "00c81940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088bb90",
      "DATA",
      [
        "storage",
        "00c81a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088bb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bb2c.md#insn-0088bb34)
- 新版 [`0088bb8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bb84.md#insn-0088bb8c)

~~~diff
- 0088bb34 ["COPY", "tmp:0:8", ["const:940:8"]]
- 0088bb34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088bb34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088bb34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088bb8c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0088bb8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088bb8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088bb8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088bb34 bytes 29012591
+ 0088bb8c bytes 29412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d82753f564456475dc51c906fb0bb3e6"></a>

### [`0088bd90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bd90.md) → [`0088bde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bde8.md) _INIT_165

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088be48",
      "incomplete_value": true,
      "site": "0088be64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0088bdf0",
      "incomplete_value": true,
      "site": "0088be0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0088be88",
      "incomplete_value": true,
      "site": "0088bea0",
      "value": [
        "LOAD",
        "16",
        [
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
      "definition_site": "0088be30",
      "incomplete_value": true,
      "site": "0088be48",
      "value": [
        "LOAD",
        "16",
        [
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
      "definition_site": "0088bee4",
      "incomplete_value": true,
      "site": "0088bf28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0088be8c",
      "incomplete_value": true,
      "site": "0088bed0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0088be24",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0088be48",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0088be68",
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
      "0088be24",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0088be48",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0088be68",
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

- 旧版 [`0088be64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bd90.md#insn-0088be64) · [`0088bdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bd90.md#insn-0088bdbc) · [`0088bdc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bd90.md#insn-0088bdc4)
- 新版 [`0088bebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bde8.md#insn-0088bebc) · [`0088be14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088b/0088bde8.md#insn-0088be14)

~~~diff
- 0088be64 ["COPY", "tmp:0:8", ["const:f5d:8"]]
- 0088be64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088be64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088be64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088bebc ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 0088bebc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088bebc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088bebc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088be64 bytes 29753d91
+ 0088bebc bytes 29413c91
- 0088bdbc ["COPY", "tmp:0:8", ["const:858:8"]]
- 0088bdbc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0088bdbc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0088bdbc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0088be14 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 0088be14 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0088be14 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0088be14 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0088bdbc bytes 73622191
+ 0088be14 bytes 73622591
- 0088bdc4 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 0088bdc4 bytes 69d1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6bf59342528b6f2dc129e6626aea062"></a>

### [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) → [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) FUN_0088c178

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`00472af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472af8.md) [`00472bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bac.md) [`00472bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472bbc.md) [`00472da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md) [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md)
- 新版 呼出元 0件  · 呼出先 25件 [`00472b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472b38.md) [`00472bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472bec.md) [`00472bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472bfc.md) [`00472de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472de4.md) [`004737bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004737bc.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.65% / 新版 94.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088c2c0",
      "incomplete_value": false,
      "site": "0088c2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088c268",
      "incomplete_value": false,
      "site": "0088c270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "definition_site": "0088c38c",
      "incomplete_value": false,
      "site": "0088c38c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088c334",
      "incomplete_value": false,
      "site": "0088c334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "definition_site": "0088c3d8",
      "incomplete_value": false,
      "site": "0088c3d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088c380",
      "incomplete_value": false,
      "site": "0088c380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "0088c1c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00472bac"
      ]
    ],
    [
      "0088c24c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683d8"
      ]
    ],
    [
      "0088c27c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ]
  ],
  "added": [
    [
      "0088c1c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00472bec"
      ]
    ],
    [
      "0088c24c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768430"
      ]
    ],
    [
      "0088c27c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088c168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md#insn-0088c168) · [`0088c1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md#insn-0088c1c0) · [`0088c1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md#insn-0088c1f4)
- 新版 [`0088c1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md#insn-0088c1c0) · [`0088c218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md#insn-0088c218) · [`0088c24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md#insn-0088c24c)

~~~diff
- 0088c168 ["INT_ADD", "register:40f0:8", ["const:88c168:8", "const:4:8"]]
- 0088c168 ["CALL", null, ["ram:472bac:8"]]
+ 0088c1c0 ["INT_ADD", "register:40f0:8", ["const:88c1c0:8", "const:4:8"]]
+ 0088c1c0 ["CALL", null, ["ram:472bec:8"]]
- 0088c168 bytes 919aef97
+ 0088c1c0 bytes 8b9aef97
- 0088c1c0 ["INT_ADD", "register:40f0:8", ["const:88c1c0:8", "const:4:8"]]
- 0088c1c0 ["CALL", null, ["callee:00851550:8"]]
+ 0088c218 ["INT_ADD", "register:40f0:8", ["const:88c218:8", "const:4:8"]]
+ 0088c218 ["CALL", null, ["callee:00851550:8"]]
- 0088c1c0 bytes ce14ff97
+ 0088c218 bytes ce14ff97
- 0088c1f4 ["INT_ADD", "register:40f0:8", ["const:88c1f4:8", "const:4:8"]]
- 0088c1f4 ["CALL", null, ["ram:7683d8:8"]]
+ 0088c24c ["INT_ADD", "register:40f0:8", ["const:88c24c:8", "const:4:8"]]
+ 0088c24c ["CALL", null, ["ram:768430:8"]]
- 0088c1f4 bytes 7970fb97
+ 0088c24c bytes 7970fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dac600f7bccb9e4b5cf8176b7a99d697"></a>

### [`0088c4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c4ac.md) → [`0088c504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c504.md) FUN_0088c504

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) [`0088f49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f49c.md) [`0088f674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f674.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044c7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c7d4.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md)
- 新版 呼出元 3件 [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) [`0088f4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f4f4.md) [`0088f6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f6cc.md) · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044c814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c814.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088c624",
      "incomplete_value": true,
      "site": "0088c624",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088c5cc",
      "incomplete_value": true,
      "site": "0088c5cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:54d:8"
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
      "definition_site": "0088c628",
      "incomplete_value": true,
      "site": "0088c628",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0088c5d0",
      "incomplete_value": true,
      "site": "0088c5d0",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0088c528",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0088c4d0",
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
      "0088c528",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0088c530",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0088c548",
      "READ",
      [
        "storage",
        "00ca5150",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0088c528",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0088c530",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0088c548",
      "READ",
      [
        "storage",
        "00ca5250",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088c4d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c4ac.md#insn-0088c4d0) · [`0088c4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c4ac.md#insn-0088c4d8) · [`0088c530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c4ac.md#insn-0088c530)
- 新版 [`0088c528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c504.md#insn-0088c528) · [`0088c530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c504.md#insn-0088c530) · [`0088c588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c504.md#insn-0088c588)

~~~diff
- 0088c4d0 ["INT_ADD", "register:40f0:8", ["const:88c4d0:8", "const:4:8"]]
- 0088c4d0 ["CALL", null, ["ram:48ccf8:8"]]
+ 0088c528 ["INT_ADD", "register:40f0:8", ["const:88c528:8", "const:4:8"]]
+ 0088c528 ["CALL", null, ["ram:48cd38:8"]]
- 0088c4d0 bytes 0a02f097
+ 0088c528 bytes 0402f097
- 0088c4d8 ["INT_ADD", "register:40f0:8", ["const:88c4d8:8", "const:4:8"]]
- 0088c4d8 ["CALL", null, ["ram:48ccf8:8"]]
+ 0088c530 ["INT_ADD", "register:40f0:8", ["const:88c530:8", "const:4:8"]]
+ 0088c530 ["CALL", null, ["ram:48cd38:8"]]
- 0088c4d8 bytes 0802f097
+ 0088c530 bytes 0202f097
- 0088c530 ["COPY", "tmp:0:8", ["const:43b:8"]]
- 0088c530 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088c530 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088c530 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088c588 ["COPY", "tmp:0:8", ["const:3e7:8"]]
+ 0088c588 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088c588 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088c588 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088c530 bytes 29ed1091
+ 0088c588 bytes 299d0f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27dbbf90af5804dc5d0208f949384513"></a>

### [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) → [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) FUN_0088c8c8

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 93件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md)
- 新版 呼出元 0件  · 呼出先 93件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0043e868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e868.md) [`00440b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440b40.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.45% / 新版 97.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 21件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088c940",
      "incomplete_value": true,
      "site": "0088c94c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a7d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088c8e8",
      "incomplete_value": true,
      "site": "0088c8f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ad9:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088cd68",
      "incomplete_value": false,
      "site": "0088cd68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088cd10",
      "incomplete_value": false,
      "site": "0088cd10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "definition_site": "0088d010",
      "incomplete_value": true,
      "site": "0088d020",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:52f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088cfb8",
      "incomplete_value": true,
      "site": "0088cfc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:57c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 72,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0088c91c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0088c92c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0088c940",
      "READ",
      [
        "storage",
        "002a5ad9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0088c91c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0088c92c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0088c940",
      "READ",
      [
        "storage",
        "002a5a7d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088c8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md#insn-0088c8c4) · [`0088c8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md#insn-0088c8d4) · [`0088cc18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md#insn-0088cc18)
- 新版 [`0088c91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md#insn-0088c91c) · [`0088c92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md#insn-0088c92c) · [`0088cc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md#insn-0088cc70)

~~~diff
- 0088c8c4 ["INT_ADD", "register:40f0:8", ["const:88c8c4:8", "const:4:8"]]
- 0088c8c4 ["CALL", null, ["ram:48ccf8:8"]]
+ 0088c91c ["INT_ADD", "register:40f0:8", ["const:88c91c:8", "const:4:8"]]
+ 0088c91c ["CALL", null, ["ram:48cd38:8"]]
- 0088c8c4 bytes 0d01f097
+ 0088c91c bytes 0701f097
- 0088c8d4 ["INT_ADD", "register:40f0:8", ["const:88c8d4:8", "const:4:8"]]
- 0088c8d4 ["CALL", null, ["ram:48ccf8:8"]]
+ 0088c92c ["INT_ADD", "register:40f0:8", ["const:88c92c:8", "const:4:8"]]
+ 0088c92c ["CALL", null, ["ram:48cd38:8"]]
- 0088c8d4 bytes 0901f097
+ 0088c92c bytes 0301f097
- 0088cc18 ["INT_ADD", "register:40f0:8", ["const:88cc18:8", "const:4:8"]]
- 0088cc18 ["CALL", null, ["callee:005cd6a0:8"]]
+ 0088cc70 ["INT_ADD", "register:40f0:8", ["const:88cc70:8", "const:4:8"]]
+ 0088cc70 ["CALL", null, ["callee:005cd6a0:8"]]
- 0088cc18 bytes 9202f597
+ 0088cc70 bytes 8c02f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f32dad8d34a16eba2cfd3d52ee23b91a"></a>

### [`0088f280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f280.md) → [`0088f2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f2d8.md) FUN_0088f2d8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 3件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 3件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0088f340",
      "incomplete_value": false,
      "site": "0088f344",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088f2e8",
      "incomplete_value": false,
      "site": "0088f2ec",
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
            "const:1bd:8"
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
      "0088f340",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0088f340",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088f2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f280.md#insn-0088f2ec) · [`0088f2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f280.md#insn-0088f2a4) · [`0088f2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f280.md#insn-0088f2e8)
- 新版 [`0088f344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f2d8.md#insn-0088f344) · [`0088f2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f2d8.md#insn-0088f2fc) · [`0088f340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f2d8.md#insn-0088f340)

~~~diff
- 0088f2ec ["INT_ADD", "register:40f0:8", ["const:88f2ec:8", "const:4:8"]]
- 0088f2ec ["CALL", null, ["callee:00442970:8"]]
+ 0088f344 ["INT_ADD", "register:40f0:8", ["const:88f344:8", "const:4:8"]]
+ 0088f344 ["CALL", null, ["callee:00442970:8"]]
- 0088f2ec bytes 91cdee97
+ 0088f344 bytes 8bcdee97
- 0088f2a4 ["INT_ADD", "register:40f0:8", ["const:88f2a4:8", "const:4:8"]]
- 0088f2a4 ["CALL", null, ["callee:0046d5e8:8"]]
+ 0088f2fc ["INT_ADD", "register:40f0:8", ["const:88f2fc:8", "const:4:8"]]
+ 0088f2fc ["CALL", null, ["callee:0046d5e8:8"]]
- 0088f2a4 bytes c178ef97
+ 0088f2fc bytes bb78ef97
- 0088f2e8 ["COPY", "tmp:0:8", ["const:1bd:8"]]
- 0088f2e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0088f2e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0088f2e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0088f340 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 0088f340 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0088f340 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0088f340 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0088f2e8 bytes 00f40691
+ 0088f340 bytes 00c00591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-234f5f5bbce174c79b04c7080e022191"></a>

### [`0088f444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f444.md) → [`0088f49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f49c.md) FUN_0088f49c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088f4bc",
      "incomplete_value": false,
      "site": "0088f4c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088f464",
      "incomplete_value": false,
      "site": "0088f468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "0088f4c0",
      "DATA",
      [
        "storage",
        "00c81a88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088f4c0",
      "DATA",
      [
        "storage",
        "00c81b58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088f458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f444.md#insn-0088f458) · [`0088f464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f444.md#insn-0088f464)
- 新版 [`0088f4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f49c.md#insn-0088f4b0) · [`0088f4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f49c.md#insn-0088f4bc)

~~~diff
- 0088f458 ["INT_ADD", "register:40f0:8", ["const:88f458:8", "const:4:8"]]
- 0088f458 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088f4b0 ["INT_ADD", "register:40f0:8", ["const:88f4b0:8", "const:4:8"]]
+ 0088f4b0 ["CALL", null, ["callee:00c57f60:8"]]
- 0088f458 bytes 8e220f94
+ 0088f4b0 bytes ac220f94
- 0088f464 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 0088f464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088f464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088f464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088f4bc ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 0088f4bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f4bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f4bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088f464 bytes 08212a91
+ 0088f4bc bytes 08612d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6de0d1f059e0574fc055d9a812d15a82"></a>

### [`0088f47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f47c.md) → [`0088f4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f4d4.md) FUN_0088f4d4

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
      "definition_site": "0088f4d8",
      "incomplete_value": false,
      "site": "0088f4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088f480",
      "incomplete_value": false,
      "site": "0088f484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "0088f4dc",
      "DATA",
      [
        "storage",
        "00c81a88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088f4dc",
      "DATA",
      [
        "storage",
        "00c81b58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088f480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f47c.md#insn-0088f480)
- 新版 [`0088f4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f4d4.md#insn-0088f4d8)

~~~diff
- 0088f480 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 0088f480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088f480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088f480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088f4d8 ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 0088f4d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f4d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f4d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088f480 bytes 08212a91
+ 0088f4d8 bytes 08612d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f11db09888630c3c912ec9aac49c37d"></a>

### [`0088f624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f624.md) → [`0088f67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f67c.md) FUN_0088f67c

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
      "definition_site": "0088f6a0",
      "incomplete_value": false,
      "site": "0088f6a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088f648",
      "incomplete_value": false,
      "site": "0088f648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088f6a0",
      "DATA",
      [
        "storage",
        "00c81b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088f6a0",
      "DATA",
      [
        "storage",
        "00c81be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088f638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f624.md#insn-0088f638) · [`0088f644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f624.md#insn-0088f644)
- 新版 [`0088f690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f67c.md#insn-0088f690) · [`0088f69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f67c.md#insn-0088f69c)

~~~diff
- 0088f638 ["INT_ADD", "register:40f0:8", ["const:88f638:8", "const:4:8"]]
- 0088f638 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088f690 ["INT_ADD", "register:40f0:8", ["const:88f690:8", "const:4:8"]]
+ 0088f690 ["CALL", null, ["callee:00c57f60:8"]]
- 0088f638 bytes 16220f94
+ 0088f690 bytes 34220f94
- 0088f644 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 0088f644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088f644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088f644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088f69c ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 0088f69c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f69c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f69c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088f644 bytes 08612c91
+ 0088f69c bytes 08a12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fb60fe8b013546a72964da8efb5da83"></a>

### [`0088f658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f658.md) → [`0088f6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f6b0.md) FUN_0088f6b0

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
      "definition_site": "0088f6bc",
      "incomplete_value": false,
      "site": "0088f6bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088f664",
      "incomplete_value": false,
      "site": "0088f664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "0088f6bc",
      "DATA",
      [
        "storage",
        "00c81b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088f6bc",
      "DATA",
      [
        "storage",
        "00c81be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088f660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f658.md#insn-0088f660)
- 新版 [`0088f6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f6b0.md#insn-0088f6b8)

~~~diff
- 0088f660 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 0088f660 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088f660 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088f660 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088f6b8 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 0088f6b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088f6b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088f6b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088f660 bytes 29612c91
+ 0088f6b8 bytes 29a12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-435e3828ceba8d05c0e3841226a0bf69"></a>

### [`0088f6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6a4.md) → [`0088f6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f6fc.md) FUN_0088f6fc

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
      "definition_site": "0088f710",
      "incomplete_value": false,
      "site": "0088f714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088f6b8",
      "incomplete_value": false,
      "site": "0088f6bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "0088f714",
      "DATA",
      [
        "storage",
        "00c81b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088f714",
      "DATA",
      [
        "storage",
        "00c81c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088f6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6a4.md#insn-0088f6b0) · [`0088f6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6a4.md#insn-0088f6b8)
- 新版 [`0088f708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f6fc.md#insn-0088f708) · [`0088f710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f6fc.md#insn-0088f710)

~~~diff
- 0088f6b0 ["INT_ADD", "register:40f0:8", ["const:88f6b0:8", "const:4:8"]]
- 0088f6b0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088f708 ["INT_ADD", "register:40f0:8", ["const:88f708:8", "const:4:8"]]
+ 0088f708 ["CALL", null, ["callee:00c57f60:8"]]
- 0088f6b0 bytes f8210f94
+ 0088f708 bytes 16220f94
- 0088f6b8 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 0088f6b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088f6b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088f6b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088f710 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 0088f710 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f710 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f710 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088f6b8 bytes 08612e91
+ 0088f710 bytes 08a13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26fabfa3f8dee5af421927474d0d4f3b"></a>

### [`0088f6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6c8.md) → [`0088f720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f720.md) FUN_0088f720

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
      "definition_site": "0088f724",
      "incomplete_value": false,
      "site": "0088f728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088f6cc",
      "incomplete_value": false,
      "site": "0088f6d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "0088f728",
      "DATA",
      [
        "storage",
        "00c81b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088f728",
      "DATA",
      [
        "storage",
        "00c81c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088f6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6c8.md#insn-0088f6cc)
- 新版 [`0088f724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f720.md#insn-0088f724)

~~~diff
- 0088f6cc ["COPY", "tmp:0:8", ["const:b98:8"]]
- 0088f6cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088f6cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088f6cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088f724 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 0088f724 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f724 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f724 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088f6cc bytes 08612e91
+ 0088f724 bytes 08a13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a46cee5fb7d3b3cd6d2cfec92278d586"></a>

### [`0088f6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6e0.md) → [`0088f738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f738.md) FUN_0088f738

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00550a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a14.md) [`0088fc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fc64.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00550a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a54.md) [`0088fcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fcbc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.08% / 新版 94.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088f76c",
      "incomplete_value": true,
      "site": "0088f77c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:67f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088f714",
      "incomplete_value": true,
      "site": "0088f724",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6cc:8"
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
      "definition_site": "0088f780",
      "incomplete_value": true,
      "site": "0088f780",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0088f728",
      "incomplete_value": true,
      "site": "0088f728",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088f774",
      "incomplete_value": true,
      "site": "0088f784",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088f71c",
      "incomplete_value": true,
      "site": "0088f72c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:450:8"
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
      "0088f76c",
      "READ",
      [
        "storage",
        "002a46cc",
        null,
        "string"
      ]
    ],
    [
      "0088f770",
      "READ",
      [
        "storage",
        "002a46db",
        null,
        "string"
      ]
    ],
    [
      "0088f774",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088f76c",
      "READ",
      [
        "storage",
        "002a467f",
        null,
        "string"
      ]
    ],
    [
      "0088f770",
      "READ",
      [
        "storage",
        "002a468e",
        null,
        "string"
      ]
    ],
    [
      "0088f774",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088f704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6e0.md#insn-0088f704) · [`0088f70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6e0.md#insn-0088f70c) · [`0088f710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f6e0.md#insn-0088f710)
- 新版 [`0088f75c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f738.md#insn-0088f75c) · [`0088f764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088f738.md#insn-0088f764)

~~~diff
- 0088f704 ["INT_ADD", "register:40f0:8", ["const:88f704:8", "const:4:8"]]
- 0088f704 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088f75c ["INT_ADD", "register:40f0:8", ["const:88f75c:8", "const:4:8"]]
+ 0088f75c ["CALL", null, ["callee:00c57f60:8"]]
- 0088f704 bytes e3210f94
+ 0088f75c bytes 01220f94
- 0088f70c ["COPY", "tmp:0:8", ["const:6cc:8"]]
- 0088f70c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088f70c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088f70c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088f764 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 0088f764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088f764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088f70c bytes 08311b91
+ 0088f764 bytes 08fd1991
- 0088f710 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0088f710 bytes 89d1fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75c63dec6a756bd1283ad3430d59c5b9"></a>

### [`0088fb28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb28.md) → [`0088fb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fb80.md) FUN_0088fb80

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0088fb94",
      "incomplete_value": false,
      "site": "0088fb98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fb3c",
      "incomplete_value": false,
      "site": "0088fb40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c08:8"
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
      "0088fb98",
      "DATA",
      [
        "storage",
        "00c81c08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fb98",
      "DATA",
      [
        "storage",
        "00c81cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb28.md#insn-0088fb3c) · [`0088fb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb28.md#insn-0088fb50) · [`0088fb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb28.md#insn-0088fb70)
- 新版 [`0088fb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fb80.md#insn-0088fb94) · [`0088fba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fb80.md#insn-0088fba8) · [`0088fbc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fb80.md#insn-0088fbc8)

~~~diff
- 0088fb3c ["COPY", "tmp:0:8", ["const:c08:8"]]
- 0088fb3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088fb3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088fb3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088fb94 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 0088fb94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fb94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fb94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088fb3c bytes 08213091
+ 0088fb94 bytes 08613391
- 0088fb50 ["INT_ADD", "register:40f0:8", ["const:88fb50:8", "const:4:8"]]
- 0088fb50 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088fba8 ["INT_ADD", "register:40f0:8", ["const:88fba8:8", "const:4:8"]]
+ 0088fba8 ["CALL", null, ["callee:00c53da0:8"]]
- 0088fb50 bytes 6c100f94
+ 0088fba8 bytes 7e100f94
- 0088fb70 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088fb70 ["INT_ADD", "register:40f0:8", ["const:88fb70:8", "const:4:8"]]
- 0088fb70 ["CALLIND", null, ["register:0:8"]]
+ 0088fbc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088fbc8 ["INT_ADD", "register:40f0:8", ["const:88fbc8:8", "const:4:8"]]
+ 0088fbc8 ["CALLIND", null, ["register:0:8"]]
- 0088fb70 bytes 00013fd6
+ 0088fbc8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19d0209757a62199f6474db154689dc0"></a>

### [`0088fb84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb84.md) → [`0088fbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fbdc.md) FUN_0088fbdc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0088fbf4",
      "incomplete_value": false,
      "site": "0088fbf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fb9c",
      "incomplete_value": false,
      "site": "0088fba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c08:8"
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
      "0088fbf8",
      "DATA",
      [
        "storage",
        "00c81c08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fbf8",
      "DATA",
      [
        "storage",
        "00c81cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb84.md#insn-0088fb9c) · [`0088fbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb84.md#insn-0088fbb0) · [`0088fbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fb84.md#insn-0088fbc4)
- 新版 [`0088fbf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fbdc.md#insn-0088fbf4) · [`0088fc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fbdc.md#insn-0088fc08) · [`0088fc1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fbdc.md#insn-0088fc1c)

~~~diff
- 0088fb9c ["COPY", "tmp:0:8", ["const:c08:8"]]
- 0088fb9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088fb9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088fb9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088fbf4 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 0088fbf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fbf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fbf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088fb9c bytes 08213091
+ 0088fbf4 bytes 08613391
- 0088fbb0 ["INT_ADD", "register:40f0:8", ["const:88fbb0:8", "const:4:8"]]
- 0088fbb0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0088fc08 ["INT_ADD", "register:40f0:8", ["const:88fc08:8", "const:4:8"]]
+ 0088fc08 ["CALL", null, ["callee:00c53da0:8"]]
- 0088fbb0 bytes 54100f94
+ 0088fc08 bytes 66100f94
- 0088fbc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0088fbc4 ["INT_ADD", "register:40f0:8", ["const:88fbc4:8", "const:4:8"]]
- 0088fbc4 ["CALLIND", null, ["register:0:8"]]
+ 0088fc1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088fc1c ["INT_ADD", "register:40f0:8", ["const:88fc1c:8", "const:4:8"]]
+ 0088fc1c ["CALLIND", null, ["register:0:8"]]
- 0088fbc4 bytes 00013fd6
+ 0088fc1c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cdd7fe718e80272c3b2f09a9c117973"></a>

### [`0088fbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fbe0.md) → [`0088fc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fc38.md) FUN_0088fc38

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088fc5c",
      "incomplete_value": false,
      "site": "0088fc5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fc04",
      "incomplete_value": false,
      "site": "0088fc04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c08:8"
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
      "0088fc5c",
      "DATA",
      [
        "storage",
        "00c81c08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fc5c",
      "DATA",
      [
        "storage",
        "00c81cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fbf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fbe0.md#insn-0088fbf4) · [`0088fc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fbe0.md#insn-0088fc00) · [`0088fc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fbe0.md#insn-0088fc1c)
- 新版 [`0088fc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fc38.md#insn-0088fc4c) · [`0088fc58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fc38.md#insn-0088fc58) · [`0088fc74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fc38.md#insn-0088fc74)

~~~diff
- 0088fbf4 ["INT_ADD", "register:40f0:8", ["const:88fbf4:8", "const:4:8"]]
- 0088fbf4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0088fc4c ["INT_ADD", "register:40f0:8", ["const:88fc4c:8", "const:4:8"]]
+ 0088fc4c ["CALL", null, ["callee:00c57f60:8"]]
- 0088fbf4 bytes a7200f94
+ 0088fc4c bytes c5200f94
- 0088fc00 ["COPY", "tmp:0:8", ["const:c08:8"]]
- 0088fc00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088fc00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088fc00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088fc58 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 0088fc58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088fc58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088fc58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088fc00 bytes 29213091
+ 0088fc58 bytes 29613391
- 0088fc1c ["INT_ADD", "register:40f0:8", ["const:88fc1c:8", "const:4:8"]]
- 0088fc1c ["CALL", null, ["callee:00c53d70:8"]]
+ 0088fc74 ["INT_ADD", "register:40f0:8", ["const:88fc74:8", "const:4:8"]]
+ 0088fc74 ["CALL", null, ["callee:00c53d70:8"]]
- 0088fc1c bytes 2d100f94
+ 0088fc74 bytes 3f100f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6610ba2c751962a2c0f2b777da7af6c1"></a>

### [`0088fc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fc30.md) → [`0088fc88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fc88.md) FUN_0088fc88

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088fc94",
      "incomplete_value": false,
      "site": "0088fc94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fc3c",
      "incomplete_value": false,
      "site": "0088fc3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c08:8"
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
      "0088fc94",
      "DATA",
      [
        "storage",
        "00c81c08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fc94",
      "DATA",
      [
        "storage",
        "00c81cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fc30.md#insn-0088fc38) · [`0088fc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fc30.md#insn-0088fc58)
- 新版 [`0088fc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fc88.md#insn-0088fc90) · [`0088fcb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fc88.md#insn-0088fcb0)

~~~diff
- 0088fc38 ["COPY", "tmp:0:8", ["const:c08:8"]]
- 0088fc38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088fc38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088fc38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088fc90 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 0088fc90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088fc90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088fc90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088fc38 bytes 29213091
+ 0088fc90 bytes 29613391
- 0088fc58 ["INT_ADD", "register:40f0:8", ["const:88fc58:8", "const:4:8"]]
- 0088fc58 ["CALL", null, ["callee:00c53d70:8"]]
+ 0088fcb0 ["INT_ADD", "register:40f0:8", ["const:88fcb0:8", "const:4:8"]]
+ 0088fcb0 ["CALL", null, ["callee:00c53d70:8"]]
- 0088fc58 bytes 1e100f94
+ 0088fcb0 bytes 30100f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f091b0b511bc91d87e154b06c7d9f1e"></a>

### [`0088fd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd04.md) → [`0088fd5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd5c.md) FUN_0088fd5c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048dc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc4c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048dc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dc8c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "site": "0088fd64",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0088fd0c",
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
      "0088fd64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "0088fd64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd04.md#insn-0088fd0c) · [`0088fd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd04.md#insn-0088fd10) · [`0088fd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd04.md#insn-0088fd18)
- 新版 [`0088fd64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd5c.md#insn-0088fd64) · [`0088fd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd5c.md#insn-0088fd68) · [`0088fd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fd5c.md#insn-0088fd70)

~~~diff
- 0088fd0c ["INT_ADD", "register:40f0:8", ["const:88fd0c:8", "const:4:8"]]
- 0088fd0c ["CALL", null, ["ram:48ccf8:8"]]
+ 0088fd64 ["INT_ADD", "register:40f0:8", ["const:88fd64:8", "const:4:8"]]
+ 0088fd64 ["CALL", null, ["ram:48cd38:8"]]
- 0088fd0c bytes fbf3ef97
+ 0088fd64 bytes f5f3ef97
- 0088fd10 ["INT_ADD", "register:40f0:8", ["const:88fd10:8", "const:4:8"]]
- 0088fd10 ["CALL", null, ["callee:0048dc8c:8"]]
+ 0088fd68 ["INT_ADD", "register:40f0:8", ["const:88fd68:8", "const:4:8"]]
+ 0088fd68 ["CALL", null, ["callee:0048dc8c:8"]]
- 0088fd10 bytes cff7ef97
+ 0088fd68 bytes c9f7ef97
- 0088fd18 ["INT_ADD", "register:40f0:8", ["const:88fd18:8", "const:4:8"]]
- 0088fd18 ["CALL", null, ["callee:00851550:8"]]
+ 0088fd70 ["INT_ADD", "register:40f0:8", ["const:88fd70:8", "const:4:8"]]
+ 0088fd70 ["CALL", null, ["callee:00851550:8"]]
- 0088fd18 bytes f805ff97
+ 0088fd70 bytes f805ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e083badccb8bb86f481005024868221"></a>

### [`0088fd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd60.md) → [`0088fdb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdb8.md) FUN_0088fdb8

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
      "definition_site": "0088fdcc",
      "incomplete_value": false,
      "site": "0088fdd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fd74",
      "incomplete_value": false,
      "site": "0088fd78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "0088fdd0",
      "DATA",
      [
        "storage",
        "00c81c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fdd0",
      "DATA",
      [
        "storage",
        "00c81d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd60.md#insn-0088fd6c) · [`0088fd74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd60.md#insn-0088fd74)
- 新版 [`0088fdc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdb8.md#insn-0088fdc4) · [`0088fdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdb8.md#insn-0088fdcc)

~~~diff
- 0088fd6c ["INT_ADD", "register:40f0:8", ["const:88fd6c:8", "const:4:8"]]
- 0088fd6c ["CALL", null, ["callee:00c57f60:8"]]
+ 0088fdc4 ["INT_ADD", "register:40f0:8", ["const:88fdc4:8", "const:4:8"]]
+ 0088fdc4 ["CALL", null, ["callee:00c57f60:8"]]
- 0088fd6c bytes 49200f94
+ 0088fdc4 bytes 67200f94
- 0088fd74 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0088fd74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088fd74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088fd74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088fdcc ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 0088fdcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fdcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fdcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088fd74 bytes 08613291
+ 0088fdcc bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dee562cdd40de82b4b8794d2b463b2a"></a>

### [`0088fd84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd84.md) → [`0088fddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fddc.md) FUN_0088fddc

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
      "definition_site": "0088fde0",
      "incomplete_value": false,
      "site": "0088fde4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fd88",
      "incomplete_value": false,
      "site": "0088fd8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "0088fde4",
      "DATA",
      [
        "storage",
        "00c81c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fde4",
      "DATA",
      [
        "storage",
        "00c81d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd84.md#insn-0088fd88)
- 新版 [`0088fde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fddc.md#insn-0088fde0)

~~~diff
- 0088fd88 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0088fd88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0088fd88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0088fd88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088fde0 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 0088fde0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fde0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088fde0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0088fd88 bytes 08613291
+ 0088fde0 bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec0dd1af65e588c336a853d85a9dffaa"></a>

### [`0088fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd9c.md) → [`0088fdf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdf4.md) FUN_0088fdf4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00550a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a14.md) [`008901b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008901b4.md) [`00890204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890204.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00550a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a54.md) [`0089020c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089020c.md) [`0089025c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089025c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.40% / 新版 93.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088fe2c",
      "incomplete_value": true,
      "site": "0088fe2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:90e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fdd4",
      "incomplete_value": true,
      "site": "0088fdd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8ce:8"
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
      "definition_site": "0088fe24",
      "incomplete_value": true,
      "site": "0088fe30",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0088fdcc",
      "incomplete_value": true,
      "site": "0088fdd8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088fec0",
      "incomplete_value": false,
      "site": "0088fec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0088fe68",
      "incomplete_value": false,
      "site": "0088fe68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "0088fe18",
      "READ",
      [
        "storage",
        "002b78ce",
        null,
        "string"
      ]
    ],
    [
      "0088fe24",
      "READ",
      [
        "storage",
        "002b78d5",
        null,
        "string"
      ]
    ],
    [
      "0088fec0",
      "DATA",
      [
        "storage",
        "00c81d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088fe18",
      "READ",
      [
        "storage",
        "002b790e",
        null,
        "string"
      ]
    ],
    [
      "0088fe24",
      "READ",
      [
        "storage",
        "002b7915",
        null,
        "string"
      ]
    ],
    [
      "0088fec0",
      "DATA",
      [
        "storage",
        "00c81dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0088fdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd9c.md#insn-0088fdb8) · [`0088fde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd9c.md#insn-0088fde8) · [`0088fdf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd9c.md#insn-0088fdf4)
- 新版 [`0088fe10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdf4.md#insn-0088fe10) · [`0088fe40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdf4.md#insn-0088fe40) · [`0088fe4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088f/0088fdf4.md#insn-0088fe4c)

~~~diff
- 0088fdb8 ["COPY", "tmp:0:8", ["const:8ce:8"]]
- 0088fdb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0088fdb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0088fdb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088fe10 ["COPY", "tmp:0:8", ["const:90e:8"]]
+ 0088fe10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088fe10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088fe10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0088fdb8 bytes 29392391
+ 0088fe10 bytes 29392491
- 0088fde8 ["INT_ADD", "register:40f0:8", ["const:88fde8:8", "const:4:8"]]
- 0088fde8 ["CALL", null, ["callee:0048ce94:8"]]
+ 0088fe40 ["INT_ADD", "register:40f0:8", ["const:88fe40:8", "const:4:8"]]
+ 0088fe40 ["CALL", null, ["callee:0048ce94:8"]]
- 0088fde8 bytes 1bf4ef97
+ 0088fe40 bytes 15f4ef97
- 0088fdf4 ["INT_ADD", "register:40f0:8", ["const:88fdf4:8", "const:4:8"]]
- 0088fdf4 ["CALL", null, ["callee:00550a54:8"]]
+ 0088fe4c ["INT_ADD", "register:40f0:8", ["const:88fe4c:8", "const:4:8"]]
+ 0088fe4c ["CALL", null, ["callee:00550a54:8"]]
- 0088fdf4 bytes 0803f397
+ 0088fe4c bytes 0203f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f7a1581ea4edba0c17cf74771dbe211"></a>

### [`00890078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890078.md) → [`008900d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008900d0.md) FUN_008900d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "008900e4",
      "incomplete_value": false,
      "site": "008900e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089008c",
      "incomplete_value": false,
      "site": "00890090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "008900e8",
      "DATA",
      [
        "storage",
        "00c81d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008900e8",
      "DATA",
      [
        "storage",
        "00c81dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089008c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890078.md#insn-0089008c) · [`008900a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890078.md#insn-008900a0) · [`008900c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890078.md#insn-008900c0)
- 新版 [`008900e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008900d0.md#insn-008900e4) · [`008900f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008900d0.md#insn-008900f8) · [`00890118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008900d0.md#insn-00890118)

~~~diff
- 0089008c ["COPY", "tmp:0:8", ["const:d08:8"]]
- 0089008c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0089008c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0089008c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008900e4 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 008900e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008900e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008900e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0089008c bytes 08213491
+ 008900e4 bytes 08613791
- 008900a0 ["INT_ADD", "register:40f0:8", ["const:8900a0:8", "const:4:8"]]
- 008900a0 ["CALL", null, ["callee:00c53da0:8"]]
+ 008900f8 ["INT_ADD", "register:40f0:8", ["const:8900f8:8", "const:4:8"]]
+ 008900f8 ["CALL", null, ["callee:00c53da0:8"]]
- 008900a0 bytes 180f0f94
+ 008900f8 bytes 2a0f0f94
- 008900c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 008900c0 ["INT_ADD", "register:40f0:8", ["const:8900c0:8", "const:4:8"]]
- 008900c0 ["CALLIND", null, ["register:0:8"]]
+ 00890118 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00890118 ["INT_ADD", "register:40f0:8", ["const:890118:8", "const:4:8"]]
+ 00890118 ["CALLIND", null, ["register:0:8"]]
- 008900c0 bytes 00013fd6
+ 00890118 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6683d34ead430fce17e3389fdd822070"></a>

### [`008900d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008900d4.md) → [`0089012c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089012c.md) FUN_0089012c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00890144",
      "incomplete_value": false,
      "site": "00890148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008900ec",
      "incomplete_value": false,
      "site": "008900f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "00890148",
      "DATA",
      [
        "storage",
        "00c81d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00890148",
      "DATA",
      [
        "storage",
        "00c81dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008900ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008900d4.md#insn-008900ec) · [`00890100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008900d4.md#insn-00890100) · [`00890114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008900d4.md#insn-00890114)
- 新版 [`00890144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089012c.md#insn-00890144) · [`00890158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089012c.md#insn-00890158) · [`0089016c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/0089012c.md#insn-0089016c)

~~~diff
- 008900ec ["COPY", "tmp:0:8", ["const:d08:8"]]
- 008900ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008900ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008900ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00890144 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00890144 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00890144 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00890144 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008900ec bytes 08213491
+ 00890144 bytes 08613791
- 00890100 ["INT_ADD", "register:40f0:8", ["const:890100:8", "const:4:8"]]
- 00890100 ["CALL", null, ["callee:00c53da0:8"]]
+ 00890158 ["INT_ADD", "register:40f0:8", ["const:890158:8", "const:4:8"]]
+ 00890158 ["CALL", null, ["callee:00c53da0:8"]]
- 00890100 bytes 000f0f94
+ 00890158 bytes 120f0f94
- 00890114 ["COPY", "register:0:8", ["register:4040:8"]]
- 00890114 ["INT_ADD", "register:40f0:8", ["const:890114:8", "const:4:8"]]
- 00890114 ["CALLIND", null, ["register:0:8"]]
+ 0089016c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0089016c ["INT_ADD", "register:40f0:8", ["const:89016c:8", "const:4:8"]]
+ 0089016c ["CALLIND", null, ["register:0:8"]]
- 00890114 bytes 00013fd6
+ 0089016c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1706cc77027b06e40531ddecb704daff"></a>

### [`00890130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890130.md) → [`00890188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890188.md) FUN_00890188

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008901ac",
      "incomplete_value": false,
      "site": "008901ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00890154",
      "incomplete_value": false,
      "site": "00890154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "008901ac",
      "DATA",
      [
        "storage",
        "00c81d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008901ac",
      "DATA",
      [
        "storage",
        "00c81dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00890144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890130.md#insn-00890144) · [`00890150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890130.md#insn-00890150) · [`0089016c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890130.md#insn-0089016c)
- 新版 [`0089019c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890188.md#insn-0089019c) · [`008901a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890188.md#insn-008901a8) · [`008901c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890188.md#insn-008901c4)

~~~diff
- 00890144 ["INT_ADD", "register:40f0:8", ["const:890144:8", "const:4:8"]]
- 00890144 ["CALL", null, ["callee:00c57f60:8"]]
+ 0089019c ["INT_ADD", "register:40f0:8", ["const:89019c:8", "const:4:8"]]
+ 0089019c ["CALL", null, ["callee:00c57f60:8"]]
- 00890144 bytes 531f0f94
+ 0089019c bytes 711f0f94
- 00890150 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00890150 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00890150 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00890150 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008901a8 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 008901a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008901a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008901a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00890150 bytes 29213491
+ 008901a8 bytes 29613791
- 0089016c ["INT_ADD", "register:40f0:8", ["const:89016c:8", "const:4:8"]]
- 0089016c ["CALL", null, ["callee:00c53d70:8"]]
+ 008901c4 ["INT_ADD", "register:40f0:8", ["const:8901c4:8", "const:4:8"]]
+ 008901c4 ["CALL", null, ["callee:00c53d70:8"]]
- 0089016c bytes d90e0f94
+ 008901c4 bytes eb0e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9a9681d4740485ee37c4144d221b8d0"></a>

### [`00890180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890180.md) → [`008901d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008901d8.md) FUN_008901d8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008901e4",
      "incomplete_value": false,
      "site": "008901e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089018c",
      "incomplete_value": false,
      "site": "0089018c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "008901e4",
      "DATA",
      [
        "storage",
        "00c81d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008901e4",
      "DATA",
      [
        "storage",
        "00c81dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00890188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890180.md#insn-00890188) · [`008901a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890180.md#insn-008901a8)
- 新版 [`008901e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008901d8.md#insn-008901e0) · [`00890200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008901d8.md#insn-00890200)

~~~diff
- 00890188 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00890188 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00890188 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00890188 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008901e0 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 008901e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008901e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008901e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00890188 bytes 29213491
+ 008901e0 bytes 29613791
- 008901a8 ["INT_ADD", "register:40f0:8", ["const:8901a8:8", "const:4:8"]]
- 008901a8 ["CALL", null, ["callee:00c53d70:8"]]
+ 00890200 ["INT_ADD", "register:40f0:8", ["const:890200:8", "const:4:8"]]
+ 00890200 ["CALL", null, ["callee:00c53d70:8"]]
- 008901a8 bytes ca0e0f94
+ 00890200 bytes dc0e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fccd7dd4311e7415f0cabd872098c9e8"></a>

### [`00890280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890280.md) → [`008902d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008902d8.md) _INIT_166

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00890338",
      "incomplete_value": true,
      "site": "00890354",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "008902e0",
      "incomplete_value": true,
      "site": "008902fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00890358",
      "incomplete_value": true,
      "site": "00890374",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00890300",
      "incomplete_value": true,
      "site": "0089031c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00890378",
      "incomplete_value": true,
      "site": "00890390",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00890320",
      "incomplete_value": true,
      "site": "00890338",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00890314",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00890338",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00890358",
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
      "00890314",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00890338",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00890358",
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

- 旧版 [`00890354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890280.md#insn-00890354) · [`00890374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890280.md#insn-00890374) · [`008904b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890280.md#insn-008904b4)
- 新版 [`008903ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008902d8.md#insn-008903ac) · [`008903cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008902d8.md#insn-008903cc) · [`0089050c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008902d8.md#insn-0089050c)

~~~diff
- 00890354 ["COPY", "tmp:0:8", ["const:f5d:8"]]
- 00890354 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00890354 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00890354 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008903ac ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 008903ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008903ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008903ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00890354 bytes 29753d91
+ 008903ac bytes 29413c91
- 00890374 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 00890374 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00890374 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00890374 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008903cc ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 008903cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008903cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008903cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00890374 bytes 29253c91
+ 008903cc bytes 29f13a91
- 008904b4 ["INT_ADD", "register:40f0:8", ["const:8904b4:8", "const:4:8"]]
- 008904b4 ["CALL", null, ["callee:00c57f00:8"]]
+ 0089050c ["INT_ADD", "register:40f0:8", ["const:89050c:8", "const:4:8"]]
+ 0089050c ["CALL", null, ["callee:00c57f00:8"]]
- 008904b4 bytes 5f1e0f94
+ 0089050c bytes 7d1e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1ad375764557f7d8566caf33f4d7ba7"></a>

### [`00890754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md) → [`008907ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008907ac.md) FUN_008907ac

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00890bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890bd0.md) [`00890d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890d8c.md) [`008925c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925c4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00890c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890c28.md) [`00890de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/00890de4.md) [`0089261c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/0089261c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 79.63% / 新版 79.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00890814",
      "incomplete_value": true,
      "site": "00890814",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2f3000:8"
              ],
              [
                "leaf",
                "const:23f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008907bc",
      "incomplete_value": true,
      "site": "008907bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2f3000:8"
              ],
              [
                "leaf",
                "const:1ff:8"
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
      "definition_site": "00890870",
      "incomplete_value": true,
      "site": "00890870",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2f3000:8"
              ],
              [
                "leaf",
                "const:263:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00890818",
      "incomplete_value": true,
      "site": "00890818",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2f3000:8"
              ],
              [
                "leaf",
                "const:223:8"
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
      "definition_site": "00890890",
      "incomplete_value": true,
      "site": "00890890",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2f3000:8"
              ],
              [
                "leaf",
                "const:26f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00890838",
      "incomplete_value": true,
      "site": "00890838",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2f3000:8"
              ],
              [
                "leaf",
                "const:22f:8"
              ]
            ]
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
      "00890800",
      "READ",
      [
        "storage",
        "002f31ff",
        null,
        "string"
      ]
    ],
    [
      "0089081c",
      "READ",
      [
        "storage",
        "002f320b",
        null,
        "string"
      ]
    ],
    [
      "0089083c",
      "READ",
      [
        "storage",
        "002f3217",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00890800",
      "READ",
      [
        "storage",
        "002f323f",
        null,
        "string"
      ]
    ],
    [
      "0089081c",
      "READ",
      [
        "storage",
        "002f324b",
        null,
        "string"
      ]
    ],
    [
      "0089083c",
      "READ",
      [
        "storage",
        "002f3257",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008907e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md#insn-008907e0) · [`00890890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md#insn-00890890) · [`00890904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md#insn-00890904)
- 新版 [`00890838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008907ac.md#insn-00890838)

~~~diff
- 008907e0 ["COPY", "tmp:0:8", ["const:217:8"]]
- 008907e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008907e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008907e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00890838 ["COPY", "tmp:0:8", ["const:257:8"]]
+ 00890838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00890838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00890838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008907e0 bytes 295d0891
+ 00890838 bytes 295d0991
- 00890890 ["COPY", "register:4048:8", ["const:2f3000:8"]]
- 00890890 bytes 09d3fff0
- 00890904 ["COPY", "register:4048:8", ["const:2f3000:8"]]
- 00890904 bytes 09d3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ed19c38b1c63c0bf0eea909f00b9d4a"></a>

### [`00891304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891304.md) → [`0089135c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md) FUN_0089135c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00891f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md) · 呼出先 23件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00891fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md) · 呼出先 23件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.59% / 新版 96.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00891634",
      "incomplete_value": true,
      "site": "00891634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "008915dc",
      "incomplete_value": true,
      "site": "008915dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008916a0",
      "incomplete_value": false,
      "site": "008916a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00891648",
      "incomplete_value": false,
      "site": "00891648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00891760",
      "incomplete_value": false,
      "site": "00891760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00891708",
      "incomplete_value": false,
      "site": "00891708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
      "00891620",
      "READ",
      [
        "storage",
        "002c12fa",
        null,
        "string"
      ]
    ],
    [
      "008916a0",
      "DATA",
      [
        "storage",
        "00c82028",
        null,
        "undefined *"
      ]
    ],
    [
      "00891720",
      "READ",
      [
        "storage",
        "00c82050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00891620",
      "READ",
      [
        "storage",
        "002c133a",
        null,
        "string"
      ]
    ],
    [
      "008916a0",
      "DATA",
      [
        "storage",
        "00c820f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00891720",
      "READ",
      [
        "storage",
        "00c82120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008916a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891304.md#insn-008916a0) · [`00891340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891304.md#insn-00891340) · [`0089137c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891304.md#insn-0089137c)
- 新版 [`008916f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md#insn-008916f8) · [`00891398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md#insn-00891398) · [`008913d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md#insn-008913d4)

~~~diff
- 008916a0 ["INT_ADD", "register:40f0:8", ["const:8916a0:8", "const:4:8"]]
- 008916a0 ["CALL", null, ["callee:008ba8c0:8"]]
+ 008916f8 ["INT_ADD", "register:40f0:8", ["const:8916f8:8", "const:4:8"]]
+ 008916f8 ["CALL", null, ["callee:008ba8c0:8"]]
- 008916a0 bytes 72a40094
+ 008916f8 bytes 72a40094
- 00891340 ["INT_ADD", "register:40f0:8", ["const:891340:8", "const:4:8"]]
- 00891340 ["CALL", null, ["callee:00b391b0:8"]]
+ 00891398 ["INT_ADD", "register:40f0:8", ["const:891398:8", "const:4:8"]]
+ 00891398 ["CALL", null, ["callee:00b391b0:8"]]
- 00891340 bytes 759f0a94
+ 00891398 bytes 869f0a94
- 0089137c ["INT_ADD", "register:40f0:8", ["const:89137c:8", "const:4:8"]]
- 0089137c ["CALL", null, ["callee:00c58120:8"]]
+ 008913d4 ["INT_ADD", "register:40f0:8", ["const:8913d4:8", "const:4:8"]]
+ 008913d4 ["CALL", null, ["callee:00c58120:8"]]
- 0089137c bytes 351b0f94
+ 008913d4 bytes 531b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ade0057ca37d20d87699a2cda608d98"></a>

### [`00891b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891b6c.md) → [`00891bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891bc4.md) FUN_00891bc4

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00891f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md) [`0089243c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/0089243c.md) [`0089314c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089314c.md) [`0089329c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089329c.md) · 呼出先 9件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00892c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892c90.md) [`00892c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892c94.md) [`008b9858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9858.md)
- 新版 呼出元 4件 [`00891fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md) [`00892494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892494.md) [`008931a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008931a4.md) [`008932f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/008932f4.md) · 呼出先 9件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00892ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892ce8.md) [`00892cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892cec.md) [`008b98b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b98b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.93% / 新版 87.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00891c18",
      "incomplete_value": true,
      "site": "00891c28",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00891bc0",
      "incomplete_value": true,
      "site": "00891bd0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:2a0:8"
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
      "definition_site": "00891c90",
      "incomplete_value": true,
      "site": "00891ca0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00891c38",
      "incomplete_value": true,
      "site": "00891c48",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:2a0:8"
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
      "definition_site": "00891d00",
      "incomplete_value": false,
      "site": "00891d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00891ca8",
      "incomplete_value": false,
      "site": "00891ca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "00891c10",
      "READ",
      [
        "storage",
        "002a5aea",
        null,
        "string"
      ]
    ],
    [
      "00891c14",
      "READ",
      [
        "storage",
        "002a5afa",
        null,
        "string"
      ]
    ],
    [
      "00891c18",
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
      "00891c10",
      "READ",
      [
        "storage",
        "002a5a8e",
        null,
        "string"
      ]
    ],
    [
      "00891c14",
      "READ",
      [
        "storage",
        "002a5a9e",
        null,
        "string"
      ]
    ],
    [
      "00891c18",
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

- 旧版 [`00891c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891b6c.md#insn-00891c28) · [`00891ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891b6c.md#insn-00891ca0) · [`00891ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891b6c.md#insn-00891ba8)
- 新版 [`00891c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891bc4.md#insn-00891c80) · [`00891cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891bc4.md#insn-00891cf8) · [`00891c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891bc4.md#insn-00891c00)

~~~diff
- 00891c28 ["COPY", "tmp:0:8", ["const:aea:8"]]
- 00891c28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00891c28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00891c28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00891c80 ["COPY", "tmp:0:8", ["const:a8e:8"]]
+ 00891c80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00891c80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00891c80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00891c28 bytes 08a92b91
+ 00891c80 bytes 08392a91
- 00891ca0 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 00891ca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00891ca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00891ca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00891cf8 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00891cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00891cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00891cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00891ca0 bytes 08a13e91
+ 00891cf8 bytes 08e10191
- 00891ba8 ["INT_ADD", "register:40f0:8", ["const:891ba8:8", "const:4:8"]]
- 00891ba8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00891c00 ["INT_ADD", "register:40f0:8", ["const:891c00:8", "const:4:8"]]
+ 00891c00 ["CALL", null, ["callee:00c57f60:8"]]
- 00891ba8 bytes ba180f94
+ 00891c00 bytes d8180f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd4ad223269b5f09eed1ba0d2e80ff0d"></a>

### [`00891f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md) → [`00891fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md) FUN_00891fb8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00892eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892eac.md) [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 16件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047ce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce20.md) [`0047ce28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md) [`0058f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058f434.md)
- 新版 呼出元 3件 [`00892f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892f04.md) [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) · 呼出先 16件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce60.md) [`0047ce68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce68.md) [`0058f474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f474.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.05% / 新版 97.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008922e8",
      "incomplete_value": false,
      "site": "008922f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892290",
      "incomplete_value": false,
      "site": "00892298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "definition_site": "008922fc",
      "incomplete_value": false,
      "site": "008922fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008922a4",
      "incomplete_value": false,
      "site": "008922a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c82000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008922d0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00892278",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "008922d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "008922d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0089228c"
      ]
    ],
    [
      "008922dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "008922d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "008922d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008922e4"
      ]
    ],
    [
      "008922dc",
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

- 旧版 [`0089222c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md#insn-0089222c) · [`00892278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md#insn-00892278) · [`00892284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891f60.md#insn-00892284)
- 新版 [`00892284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md#insn-00892284) · [`008922d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md#insn-008922d0) · [`008922dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/00891fb8.md#insn-008922dc)

~~~diff
- 0089222c ["INT_ADD", "register:40f0:8", ["const:89222c:8", "const:4:8"]]
- 0089222c ["CALL", null, ["callee:0058f474:8"]]
+ 00892284 ["INT_ADD", "register:40f0:8", ["const:892284:8", "const:4:8"]]
+ 00892284 ["CALL", null, ["callee:0058f474:8"]]
- 0089222c bytes 82f4f397
+ 00892284 bytes 7cf4f397
- 00892278 ["INT_ADD", "register:40f0:8", ["const:892278:8", "const:4:8"]]
- 00892278 ["CALL", null, ["ram:47acf4:8"]]
+ 008922d0 ["INT_ADD", "register:40f0:8", ["const:8922d0:8", "const:4:8"]]
+ 008922d0 ["CALL", null, ["ram:47ad34:8"]]
- 00892278 bytes 9fa2ef97
+ 008922d0 bytes 99a2ef97
- 00892284 ["INT_ADD", "register:40f0:8", ["const:892284:8", "const:4:8"]]
- 00892284 ["CALL", null, ["ram:47acf4:8"]]
+ 008922dc ["INT_ADD", "register:40f0:8", ["const:8922dc:8", "const:4:8"]]
+ 008922dc ["CALL", null, ["ram:47ad34:8"]]
- 00892284 bytes 9ca2ef97
+ 008922dc bytes 96a2ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7bcab90325d0db73d142efe34f38cff"></a>

### [`008925c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925c4.md) → [`0089261c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/0089261c.md) FUN_0089261c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00890754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890754.md) [`00891304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00891/00891304.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`008907ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00890/008907ac.md) [`0089135c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00891/0089135c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00892628",
      "incomplete_value": false,
      "site": "0089262c",
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
      "definition_site": "008925d0",
      "incomplete_value": false,
      "site": "008925d4",
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
      "00892628",
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
      "00892628",
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

- 旧版 [`008925d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925c4.md#insn-008925d4) · [`008925d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925c4.md#insn-008925d0)
- 新版 [`0089262c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/0089261c.md#insn-0089262c) · [`00892628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/0089261c.md#insn-00892628)

~~~diff
- 008925d4 ["INT_ADD", "register:40f0:8", ["const:8925d4:8", "const:4:8"]]
- 008925d4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0089262c ["INT_ADD", "register:40f0:8", ["const:89262c:8", "const:4:8"]]
+ 0089262c ["CALL", null, ["callee:0043b7b8:8"]]
- 008925d4 bytes 69a4ee97
+ 0089262c bytes 63a4ee97
- 008925d0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 008925d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008925d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008925d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00892628 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00892628 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00892628 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00892628 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008925d0 bytes 00303d91
+ 00892628 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae71db0f1641cdd6d53006c45940d7fe"></a>

### [`008925dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925dc.md) → [`00892634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892634.md) FUN_00892634

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
      "definition_site": "00892648",
      "incomplete_value": false,
      "site": "0089264c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008925f0",
      "incomplete_value": false,
      "site": "008925f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0089264c",
      "DATA",
      [
        "storage",
        "00c81d98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0089264c",
      "DATA",
      [
        "storage",
        "00c81e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008925e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925dc.md#insn-008925e8) · [`008925f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/008925dc.md#insn-008925f0)
- 新版 [`00892640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892634.md#insn-00892640) · [`00892648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892634.md#insn-00892648)

~~~diff
- 008925e8 ["INT_ADD", "register:40f0:8", ["const:8925e8:8", "const:4:8"]]
- 008925e8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00892640 ["INT_ADD", "register:40f0:8", ["const:892640:8", "const:4:8"]]
+ 00892640 ["CALL", null, ["callee:00c57f60:8"]]
- 008925e8 bytes 2a160f94
+ 00892640 bytes 48160f94
- 008925f0 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008925f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008925f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008925f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00892648 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00892648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00892648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00892648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008925f0 bytes 08613691
+ 00892648 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0af2d8225fe8bd4134fc609d0df35789"></a>

### [`00892618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892618.md) → [`00892670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892670.md) FUN_00892670

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0089275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/0089275c.md) [`00892760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892760.md) [`00b3a5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3a5b8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008927b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927b4.md) [`008927b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927b8.md) [`00b3a654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3a654.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "0089269c",
      "incomplete_value": false,
      "site": "008926a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892644",
      "incomplete_value": false,
      "site": "0089264c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:e18:8"
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
      "008926a4",
      "DATA",
      [
        "storage",
        "00c81e18",
        null,
        "undefined *"
      ]
    ],
    [
      "008926d8",
      "READ",
      [
        "storage",
        "00c81e38",
        null,
        "pointer"
      ]
    ],
    [
      "008926d8",
      "READ",
      [
        "storage",
        "00c81e40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008926a4",
      "DATA",
      [
        "storage",
        "00c81ee8",
        null,
        "undefined *"
      ]
    ],
    [
      "008926d8",
      "READ",
      [
        "storage",
        "00c81f08",
        null,
        "pointer"
      ]
    ],
    [
      "008926d8",
      "READ",
      [
        "storage",
        "00c81f10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892618.md#insn-00892644) · [`00892658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892618.md#insn-00892658) · [`00892684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892618.md#insn-00892684)
- 新版 [`0089269c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892670.md#insn-0089269c) · [`008926b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892670.md#insn-008926b0) · [`008926dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892670.md#insn-008926dc)

~~~diff
- 00892644 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 00892644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00892644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00892644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0089269c ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0089269c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0089269c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0089269c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00892644 bytes 08613891
+ 0089269c bytes 08a13b91
- 00892658 ["INT_ADD", "register:40f0:8", ["const:892658:8", "const:4:8"]]
- 00892658 ["CALL", null, ["callee:00b3a654:8"]]
+ 008926b0 ["INT_ADD", "register:40f0:8", ["const:8926b0:8", "const:4:8"]]
+ 008926b0 ["CALL", null, ["callee:00b3a654:8"]]
- 00892658 bytes d89f0a94
+ 008926b0 bytes e99f0a94
- 00892684 ["COPY", "register:0:8", ["register:4040:8"]]
- 00892684 ["INT_ADD", "register:40f0:8", ["const:892684:8", "const:4:8"]]
- 00892684 ["CALLIND", null, ["register:0:8"]]
+ 008926dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008926dc ["INT_ADD", "register:40f0:8", ["const:8926dc:8", "const:4:8"]]
+ 008926dc ["CALLIND", null, ["register:0:8"]]
- 00892684 bytes 00013fd6
+ 008926dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-259fd4e7452c09fce0049fcd934065ca"></a>

### [`00892728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892728.md) → [`00892780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892780.md) FUN_00892780

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
      "definition_site": "00892794",
      "incomplete_value": false,
      "site": "00892798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0089273c",
      "incomplete_value": false,
      "site": "00892740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:e18:8"
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
      "00892798",
      "DATA",
      [
        "storage",
        "00c81e18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892798",
      "DATA",
      [
        "storage",
        "00c81ee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892728.md#insn-00892734) · [`0089273c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892728.md#insn-0089273c)
- 新版 [`0089278c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892780.md#insn-0089278c) · [`00892794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892780.md#insn-00892794)

~~~diff
- 00892734 ["INT_ADD", "register:40f0:8", ["const:892734:8", "const:4:8"]]
- 00892734 ["CALL", null, ["callee:00c57f60:8"]]
+ 0089278c ["INT_ADD", "register:40f0:8", ["const:89278c:8", "const:4:8"]]
+ 0089278c ["CALL", null, ["callee:00c57f60:8"]]
- 00892734 bytes d7150f94
+ 0089278c bytes f5150f94
- 0089273c ["COPY", "tmp:0:8", ["const:e18:8"]]
- 0089273c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0089273c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0089273c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00892794 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 00892794 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00892794 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00892794 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0089273c bytes 08613891
+ 00892794 bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dc6a78f46c2de65ac64e55a7ba8c835"></a>

### [`0089274c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/0089274c.md) → [`008927a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927a4.md) FUN_008927a4

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
      "definition_site": "008927a8",
      "incomplete_value": false,
      "site": "008927ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892750",
      "incomplete_value": false,
      "site": "00892754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:e18:8"
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
      "008927ac",
      "DATA",
      [
        "storage",
        "00c81e18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008927ac",
      "DATA",
      [
        "storage",
        "00c81ee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/0089274c.md#insn-00892750)
- 新版 [`008927a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927a4.md#insn-008927a8)

~~~diff
- 00892750 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 00892750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00892750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00892750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008927a8 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 008927a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008927a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008927a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00892750 bytes 08613891
+ 008927a8 bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84c5e5c05c2c4e53fa9f13a3a48e3e64"></a>

### [`00892764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892764.md) → [`008927bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927bc.md) FUN_008927bc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0089282c",
      "incomplete_value": true,
      "site": "0089283c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:40f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008927d4",
      "incomplete_value": true,
      "site": "008927e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:45c:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00892904",
      "incomplete_value": false,
      "site": "00892904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008928ac",
      "incomplete_value": false,
      "site": "008928ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:e88:8"
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
      "0089282c",
      "READ",
      [
        "storage",
        "002a345c",
        null,
        "string"
      ]
    ],
    [
      "00892904",
      "DATA",
      [
        "storage",
        "00c81e88",
        null,
        "undefined *"
      ]
    ],
    [
      "0089295c",
      "READ",
      [
        "storage",
        "00c81ea8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0089282c",
      "READ",
      [
        "storage",
        "002a340f",
        null,
        "string"
      ]
    ],
    [
      "00892904",
      "DATA",
      [
        "storage",
        "00c81f58",
        null,
        "undefined *"
      ]
    ],
    [
      "0089295c",
      "READ",
      [
        "storage",
        "00c81f78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089283c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892764.md#insn-0089283c) · [`0089279c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892764.md#insn-0089279c) · [`008927a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892764.md#insn-008927a0)
- 新版 [`00892894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927bc.md#insn-00892894) · [`008927f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927bc.md#insn-008927f4) · [`008927f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/008927bc.md#insn-008927f8)

~~~diff
- 0089283c ["INT_ADD", "register:40f0:8", ["const:89283c:8", "const:4:8"]]
- 0089283c ["CALL", null, ["callee:0043bb60:8"]]
+ 00892894 ["INT_ADD", "register:40f0:8", ["const:892894:8", "const:4:8"]]
+ 00892894 ["CALL", null, ["callee:0043bb60:8"]]
- 0089283c bytes b9a4ee97
+ 00892894 bytes b3a4ee97
- 0089279c ["INT_ADD", "register:40f0:8", ["const:89279c:8", "const:4:8"]]
- 0089279c ["CALL", null, ["callee:0071c4b8:8"]]
+ 008927f4 ["INT_ADD", "register:40f0:8", ["const:8927f4:8", "const:4:8"]]
+ 008927f4 ["CALL", null, ["callee:0071c4b8:8"]]
- 0089279c bytes 3127fa97
+ 008927f4 bytes 3127fa97
- 008927a0 ["INT_ADD", "register:40f0:8", ["const:8927a0:8", "const:4:8"]]
- 008927a0 ["CALL", null, ["callee:00851550:8"]]
+ 008927f8 ["INT_ADD", "register:40f0:8", ["const:8927f8:8", "const:4:8"]]
+ 008927f8 ["CALL", null, ["callee:00851550:8"]]
- 008927a0 bytes 56fbfe97
+ 008927f8 bytes 56fbfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88b3199854d5bdda8c24aa1512dc2c2a"></a>

### [`00892b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b0c.md) → [`00892b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892b64.md) FUN_00892b64

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
      "definition_site": "00892b78",
      "incomplete_value": false,
      "site": "00892b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892b20",
      "incomplete_value": false,
      "site": "00892b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:e88:8"
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
      "00892b7c",
      "DATA",
      [
        "storage",
        "00c81e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892b7c",
      "DATA",
      [
        "storage",
        "00c81f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b0c.md#insn-00892b18) · [`00892b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b0c.md#insn-00892b20)
- 新版 [`00892b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892b64.md#insn-00892b70) · [`00892b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892b64.md#insn-00892b78)

~~~diff
- 00892b18 ["INT_ADD", "register:40f0:8", ["const:892b18:8", "const:4:8"]]
- 00892b18 ["CALL", null, ["callee:00c57f60:8"]]
+ 00892b70 ["INT_ADD", "register:40f0:8", ["const:892b70:8", "const:4:8"]]
+ 00892b70 ["CALL", null, ["callee:00c57f60:8"]]
- 00892b18 bytes de140f94
+ 00892b70 bytes fc140f94
- 00892b20 ["COPY", "tmp:0:8", ["const:e88:8"]]
- 00892b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00892b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00892b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00892b78 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00892b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00892b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00892b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00892b20 bytes 08213a91
+ 00892b78 bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-521bfd0c9478561510dd510f60ebae5b"></a>

### [`00892b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b30.md) → [`00892b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892b88.md) FUN_00892b88

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
      "definition_site": "00892b8c",
      "incomplete_value": false,
      "site": "00892b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00892b34",
      "incomplete_value": false,
      "site": "00892b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c81000:8"
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
      "00892b90",
      "DATA",
      [
        "storage",
        "00c81e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892b90",
      "DATA",
      [
        "storage",
        "00c81f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892b30.md#insn-00892b34)
- 新版 [`00892b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00892/00892b88.md#insn-00892b8c)

~~~diff
- 00892b34 ["COPY", "tmp:0:8", ["const:e88:8"]]
- 00892b34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00892b34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00892b34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00892b8c ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00892b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00892b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00892b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00892b34 bytes 08213a91
+ 00892b8c bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

