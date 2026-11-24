# v16.0.1 → v16.0.2 · 最優先の変更候補 (12)

[一覧の目次](README.md)

<a id="compare-26c8c079b196275215842e421ce1555d"></a>

### [`00516900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516900.md) → [`00516940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516940.md) FUN_00516940

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516978",
      "incomplete_value": true,
      "site": "00516978",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516938",
      "incomplete_value": true,
      "site": "00516938",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:741:8"
              ]
            ]
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
      "00516968",
      "READ",
      [
        "storage",
        "002ad741",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516968",
      "READ",
      [
        "storage",
        "002ad6e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051691c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516900.md#insn-0051691c) · [`00516944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516900.md#insn-00516944) · [`00516954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516900.md#insn-00516954)
- 新版 [`0051695c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516940.md#insn-0051695c) · [`00516984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516940.md#insn-00516984) · [`00516994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516940.md#insn-00516994)

~~~diff
- 0051691c ["COPY", "tmp:0:8", ["const:741:8"]]
- 0051691c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051691c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051691c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051695c ["COPY", "tmp:0:8", ["const:6e5:8"]]
+ 0051695c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051695c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051695c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051691c bytes 29051d91
+ 0051695c bytes 29951b91
- 00516944 ["INT_ADD", "register:40f0:8", ["const:516944:8", "const:4:8"]]
- 00516944 ["CALL", null, ["callee:00c58760:8"]]
+ 00516984 ["INT_ADD", "register:40f0:8", ["const:516984:8", "const:4:8"]]
+ 00516984 ["CALL", null, ["callee:00c58760:8"]]
- 00516944 bytes 53071d94
+ 00516984 bytes 77071d94
- 00516954 ["INT_ADD", "register:40f0:8", ["const:516954:8", "const:4:8"]]
- 00516954 ["CALL", null, ["callee:00c57f80:8"]]
+ 00516994 ["INT_ADD", "register:40f0:8", ["const:516994:8", "const:4:8"]]
+ 00516994 ["CALL", null, ["callee:00c57f80:8"]]
- 00516954 bytes 57051d94
+ 00516994 bytes 7b051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee0783c0eac723056e66023f373d1bf7"></a>

### [`005169a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/005169a8.md) → [`005169e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005169e8.md) FUN_005169e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516a20",
      "incomplete_value": true,
      "site": "00516a20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3bb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005169e0",
      "incomplete_value": true,
      "site": "005169e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:417:8"
              ]
            ]
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
      "00516a10",
      "READ",
      [
        "storage",
        "002ab417",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516a10",
      "READ",
      [
        "storage",
        "002ab3bb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005169c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/005169a8.md#insn-005169c4) · [`005169ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/005169a8.md#insn-005169ec) · [`005169fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/005169a8.md#insn-005169fc)
- 新版 [`00516a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005169e8.md#insn-00516a04) · [`00516a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005169e8.md#insn-00516a2c) · [`00516a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005169e8.md#insn-00516a3c)

~~~diff
- 005169c4 ["COPY", "tmp:0:8", ["const:417:8"]]
- 005169c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005169c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005169c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516a04 ["COPY", "tmp:0:8", ["const:3bb:8"]]
+ 00516a04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516a04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516a04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005169c4 bytes 295d1091
+ 00516a04 bytes 29ed0e91
- 005169ec ["INT_ADD", "register:40f0:8", ["const:5169ec:8", "const:4:8"]]
- 005169ec ["CALL", null, ["callee:00c58760:8"]]
+ 00516a2c ["INT_ADD", "register:40f0:8", ["const:516a2c:8", "const:4:8"]]
+ 00516a2c ["CALL", null, ["callee:00c58760:8"]]
- 005169ec bytes 29071d94
+ 00516a2c bytes 4d071d94
- 005169fc ["INT_ADD", "register:40f0:8", ["const:5169fc:8", "const:4:8"]]
- 005169fc ["CALL", null, ["callee:00c57f80:8"]]
+ 00516a3c ["INT_ADD", "register:40f0:8", ["const:516a3c:8", "const:4:8"]]
+ 00516a3c ["CALL", null, ["callee:00c57f80:8"]]
- 005169fc bytes 2d051d94
+ 00516a3c bytes 51051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aecef851b1842fc6dad6166caf1f283"></a>

### [`00516a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516a50.md) → [`00516a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516a90.md) FUN_00516a90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516ab8",
      "incomplete_value": true,
      "site": "00516ac8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a3b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516a78",
      "incomplete_value": true,
      "site": "00516a88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a97:8"
              ]
            ]
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
      "00516ab8",
      "READ",
      [
        "storage",
        "002b0a97",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516ab8",
      "READ",
      [
        "storage",
        "002b0a3b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516a50.md#insn-00516a6c) · [`00516a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516a50.md#insn-00516a94) · [`00516aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516a50.md#insn-00516aa4)
- 新版 [`00516aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516a90.md#insn-00516aac) · [`00516ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516a90.md#insn-00516ad4) · [`00516ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516a90.md#insn-00516ae4)

~~~diff
- 00516a6c ["COPY", "tmp:0:8", ["const:a97:8"]]
- 00516a6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00516a6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00516a6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516aac ["COPY", "tmp:0:8", ["const:a3b:8"]]
+ 00516aac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516aac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516aac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00516a6c bytes 295d2a91
+ 00516aac bytes 29ed2891
- 00516a94 ["INT_ADD", "register:40f0:8", ["const:516a94:8", "const:4:8"]]
- 00516a94 ["CALL", null, ["callee:00c58760:8"]]
+ 00516ad4 ["INT_ADD", "register:40f0:8", ["const:516ad4:8", "const:4:8"]]
+ 00516ad4 ["CALL", null, ["callee:00c58760:8"]]
- 00516a94 bytes ff061d94
+ 00516ad4 bytes 23071d94
- 00516aa4 ["INT_ADD", "register:40f0:8", ["const:516aa4:8", "const:4:8"]]
- 00516aa4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00516ae4 ["INT_ADD", "register:40f0:8", ["const:516ae4:8", "const:4:8"]]
+ 00516ae4 ["CALL", null, ["callee:00c57f80:8"]]
- 00516aa4 bytes 03051d94
+ 00516ae4 bytes 27051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13bc40facd7d6c21c5e301dfb4213392"></a>

### [`00516af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516af8.md) → [`00516b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516b38.md) FUN_00516b38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 5件 [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 5件 [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516b80",
      "incomplete_value": true,
      "site": "00516b80",
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
      "definition_site": "00516b40",
      "incomplete_value": true,
      "site": "00516b40",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516b80",
      "incomplete_value": true,
      "site": "00516b80",
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
      "definition_site": "00516b40",
      "incomplete_value": true,
      "site": "00516b40",
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
      "00516b60",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "00516b6c",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00516b80",
      "DATA",
      [
        "storage",
        "00c68ee8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00516b60",
      "READ",
      [
        "storage",
        "00c9b2b0",
        null,
        "pointer"
      ]
    ],
    [
      "00516b6c",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00516b80",
      "DATA",
      [
        "storage",
        "00c68fb8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516af8.md#insn-00516b20) · [`00516b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516af8.md#insn-00516b28) · [`00516b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516af8.md#insn-00516b2c)
- 新版 [`00516b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516b38.md#insn-00516b60) · [`00516b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516b38.md#insn-00516b6c)

~~~diff
- 00516b20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e0:8"]]
- 00516b20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00516b60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
+ 00516b60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00516b20 bytes 08f140f9
+ 00516b60 bytes 085941f9
- 00516b28 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00516b28 bytes f30300aa
- 00516b2c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
- 00516b2c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00516b6c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
+ 00516b6c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00516b2c bytes 29a146f9
+ 00516b6c bytes 290947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-530b49053cd8dcf6b2ae4f6eeeb62603"></a>

### [`00516dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516dec.md) → [`00516e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516e2c.md) _ZNK5Botan10Extensions20get_extension_objectERKNS_3OIDE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ac0.md) · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 1件 [`00c59b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b90.md) · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.37% / 新版 94.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00516f24",
      "incomplete_value": false,
      "site": "00516f44",
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
            "const:cd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516ee4",
      "incomplete_value": false,
      "site": "00516f04",
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
            "const:d32:8"
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
      "definition_site": "00516f2c",
      "incomplete_value": false,
      "site": "00516f44",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516eec",
      "incomplete_value": false,
      "site": "00516f04",
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
            "const:3ea:8"
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
      "definition_site": "00516f34",
      "incomplete_value": false,
      "site": "00516f44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:2f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516ef4",
      "incomplete_value": false,
      "site": "00516f04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:2b7:8"
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
      "00516f24",
      "PARAM",
      [
        "storage",
        "002a9d32",
        null,
        "string"
      ]
    ],
    [
      "00516f2c",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00516f34",
      "PARAM",
      [
        "storage",
        "002c12b7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00516f24",
      "PARAM",
      [
        "storage",
        "002a9cd6",
        null,
        "string"
      ]
    ],
    [
      "00516f2c",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00516f34",
      "PARAM",
      [
        "storage",
        "002c12f7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516dec.md#insn-00516f04) · [`00516ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516dec.md#insn-00516ee4) · [`00516eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516dec.md#insn-00516eec)
- 新版 [`00516f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516e2c.md#insn-00516f44) · [`00516f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516e2c.md#insn-00516f24) · [`00516f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516e2c.md#insn-00516f2c)

~~~diff
- 00516f04 ["INT_ADD", "register:40f0:8", ["const:516f04:8", "const:4:8"]]
- 00516f04 ["CALL", null, ["callee:00c58720:8"]]
+ 00516f44 ["INT_ADD", "register:40f0:8", ["const:516f44:8", "const:4:8"]]
+ 00516f44 ["CALL", null, ["callee:00c58720:8"]]
- 00516f04 bytes d3051d94
+ 00516f44 bytes f7051d94
- 00516ee4 ["COPY", "tmp:0:8", ["const:d32:8"]]
- 00516ee4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00516ee4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00516ee4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00516f24 ["COPY", "tmp:0:8", ["const:cd6:8"]]
+ 00516f24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00516f24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00516f24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00516ee4 bytes 00c83491
+ 00516f24 bytes 00583391
- 00516eec ["COPY", "tmp:0:8", ["const:3ea:8"]]
- 00516eec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00516eec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00516eec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00516f2c ["COPY", "tmp:0:8", ["const:38e:8"]]
+ 00516f2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00516f2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00516f2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00516eec bytes 21a80f91
+ 00516f2c bytes 21380e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40cf3fbb6b74b290965b34280defdf80"></a>

### [`00516f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516f08.md) → [`00516f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516f48.md) _ZNK5Botan10Extensions10extensionsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e00.md) · 呼出先 3件 [`0054c0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054c0ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 1件 [`00c59ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ed0.md) · 呼出先 3件 [`0054c12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054c/0054c12c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.06% / 新版 95.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517064",
      "incomplete_value": false,
      "site": "00517084",
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
            "const:cd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517024",
      "incomplete_value": false,
      "site": "00517044",
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
            "const:d32:8"
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
      "definition_site": "0051706c",
      "incomplete_value": false,
      "site": "00517084",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051702c",
      "incomplete_value": false,
      "site": "00517044",
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
            "const:3ea:8"
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
      "definition_site": "00517074",
      "incomplete_value": false,
      "site": "00517084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:2f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517034",
      "incomplete_value": false,
      "site": "00517044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:2b7:8"
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
      "00517064",
      "PARAM",
      [
        "storage",
        "002a9d32",
        null,
        "string"
      ]
    ],
    [
      "0051706c",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00517074",
      "PARAM",
      [
        "storage",
        "002c12b7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00517064",
      "PARAM",
      [
        "storage",
        "002a9cd6",
        null,
        "string"
      ]
    ],
    [
      "0051706c",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00517074",
      "PARAM",
      [
        "storage",
        "002c12f7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516f08.md#insn-00517044) · [`00516f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516f08.md#insn-00516f84) · [`00516fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516f08.md#insn-00516fbc)
- 新版 [`00517084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516f48.md#insn-00517084) · [`00516fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516f48.md#insn-00516fc4) · [`00516ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516f48.md#insn-00516ffc)

~~~diff
- 00517044 ["INT_ADD", "register:40f0:8", ["const:517044:8", "const:4:8"]]
- 00517044 ["CALL", null, ["callee:00c58720:8"]]
+ 00517084 ["INT_ADD", "register:40f0:8", ["const:517084:8", "const:4:8"]]
+ 00517084 ["CALL", null, ["callee:00c58720:8"]]
- 00517044 bytes 83051d94
+ 00517084 bytes a7051d94
- 00516f84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00516f84 ["INT_ADD", "register:40f0:8", ["const:516f84:8", "const:4:8"]]
- 00516f84 ["CALLIND", null, ["register:0:8"]]
+ 00516fc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00516fc4 ["INT_ADD", "register:40f0:8", ["const:516fc4:8", "const:4:8"]]
+ 00516fc4 ["CALLIND", null, ["register:0:8"]]
- 00516f84 bytes 00013fd6
+ 00516fc4 bytes 00013fd6
- 00516fbc ["INT_ADD", "register:40f0:8", ["const:516fbc:8", "const:4:8"]]
- 00516fbc ["CALL", null, ["callee:0054c12c:8"]]
+ 00516ffc ["INT_ADD", "register:40f0:8", ["const:516ffc:8", "const:4:8"]]
+ 00516ffc ["CALL", null, ["callee:0054c12c:8"]]
- 00516fbc bytes 4cd40094
+ 00516ffc bytes 4cd40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a95d9660410bbfa69e99eddca4b95cc8"></a>

### [`00517290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517290.md) → [`005172d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005172d0.md) _ZNK5Botan10Extensions11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005120dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005120dc.md) · 呼出先 9件 [`00517488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517488.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0051211c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/0051211c.md) · 呼出先 9件 [`005174c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005174c8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517470",
      "incomplete_value": false,
      "site": "00517490",
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
            "const:cd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517430",
      "incomplete_value": false,
      "site": "00517450",
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
            "const:d32:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517478",
      "incomplete_value": false,
      "site": "00517490",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517438",
      "incomplete_value": false,
      "site": "00517450",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517480",
      "incomplete_value": false,
      "site": "00517490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:2f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517440",
      "incomplete_value": false,
      "site": "00517450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:2b7:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00517470",
      "PARAM",
      [
        "storage",
        "002a9d32",
        null,
        "string"
      ]
    ],
    [
      "00517478",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00517480",
      "PARAM",
      [
        "storage",
        "002c12b7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00517470",
      "PARAM",
      [
        "storage",
        "002a9cd6",
        null,
        "string"
      ]
    ],
    [
      "00517478",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00517480",
      "PARAM",
      [
        "storage",
        "002c12f7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517290.md#insn-00517450) · [`005172e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517290.md#insn-005172e0) · [`005172f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517290.md#insn-005172f4)
- 新版 [`00517490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005172d0.md#insn-00517490) · [`00517320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005172d0.md#insn-00517320) · [`00517334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005172d0.md#insn-00517334)

~~~diff
- 00517450 ["INT_ADD", "register:40f0:8", ["const:517450:8", "const:4:8"]]
- 00517450 ["CALL", null, ["callee:00c58720:8"]]
+ 00517490 ["INT_ADD", "register:40f0:8", ["const:517490:8", "const:4:8"]]
+ 00517490 ["CALL", null, ["callee:00c58720:8"]]
- 00517450 bytes 80041d94
+ 00517490 bytes a4041d94
- 005172e0 ["INT_ADD", "register:40f0:8", ["const:5172e0:8", "const:4:8"]]
- 005172e0 ["CALL", null, ["callee:005174c8:8"]]
+ 00517320 ["INT_ADD", "register:40f0:8", ["const:517320:8", "const:4:8"]]
+ 00517320 ["CALL", null, ["callee:005174c8:8"]]
- 005172e0 bytes 6a000094
+ 00517320 bytes 6a000094
- 005172f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005172f4 ["INT_ADD", "register:40f0:8", ["const:5172f4:8", "const:4:8"]]
- 005172f4 ["CALLIND", null, ["register:0:8"]]
+ 00517334 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00517334 ["INT_ADD", "register:40f0:8", ["const:517334:8", "const:4:8"]]
+ 00517334 ["CALLIND", null, ["register:0:8"]]
- 005172f4 bytes 00013fd6
+ 00517334 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9dfe23d6c950f1dc488e57c1c3a30df"></a>

### [`00517488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517488.md) → [`005174c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005174c8.md) FUN_005174c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00517290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517290.md) [`0053c40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c40c.md) [`0054a2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054a2c4.md) · 呼出先 5件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 3件 [`005172d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005172d0.md) [`0053c44c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c44c.md) [`0054a304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054a304.md) · 呼出先 5件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00517504",
      "incomplete_value": true,
      "site": "00517508",
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
      "definition_site": "005174c4",
      "incomplete_value": true,
      "site": "005174c8",
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
      "005174f4",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00517508",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005174f4",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00517508",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005174b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517488.md#insn-005174b4) · [`005174dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517488.md#insn-005174dc) · [`005174f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517488.md#insn-005174f4)
- 新版 [`005174f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005174c8.md#insn-005174f4) · [`0051751c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005174c8.md#insn-0051751c) · [`00517534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005174c8.md#insn-00517534)

~~~diff
- 005174b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
- 005174b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005174f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 005174f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005174b4 bytes 08a146f9
+ 005174f4 bytes 080947f9
- 005174dc ["INT_ADD", "register:40f0:8", ["const:5174dc:8", "const:4:8"]]
- 005174dc ["CALL", null, ["callee:00c57f60:8"]]
+ 0051751c ["INT_ADD", "register:40f0:8", ["const:51751c:8", "const:4:8"]]
+ 0051751c ["CALL", null, ["callee:00c57f60:8"]]
- 005174dc bytes 6d021d94
+ 0051751c bytes 91021d94
- 005174f4 ["INT_ADD", "register:40f0:8", ["const:5174f4:8", "const:4:8"]]
- 005174f4 ["CALL", null, ["callee:00c580d0:8"]]
+ 00517534 ["INT_ADD", "register:40f0:8", ["const:517534:8", "const:4:8"]]
+ 00517534 ["CALL", null, ["callee:00c580d0:8"]]
- 005174f4 bytes c3021d94
+ 00517534 bytes e7021d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06c4842178d255811dedbed111e36da4"></a>

### [`00517650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517650.md) → [`00517690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md) _ZN5Botan10Extensions11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0050376c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/0050376c.md) [`005132b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/005132b0.md) · 呼出先 21件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00517c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517c34.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`0054b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md)
- 新版 呼出元 2件 [`005037ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/005037ac.md) [`005132f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md) · 呼出先 21件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00517c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517c74.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`0053b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b464.md) [`0054b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b984.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00517800",
      "incomplete_value": true,
      "site": "00517800",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005177c0",
      "incomplete_value": true,
      "site": "005177c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051799c",
      "incomplete_value": true,
      "site": "0051799c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051795c",
      "incomplete_value": true,
      "site": "0051795c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00517718",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "005177f0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00517848",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00517718",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "005177f0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00517848",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517650.md#insn-00517780) · [`005177c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517650.md#insn-005177c0) · [`0051795c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517650.md#insn-0051795c)
- 新版 [`005177c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md#insn-005177c0) · [`00517800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md#insn-00517800) · [`0051799c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md#insn-0051799c)

~~~diff
- 00517780 ["INT_ADD", "register:40f0:8", ["const:517780:8", "const:4:8"]]
- 00517780 ["CALL", null, ["callee:00c58970:8"]]
+ 005177c0 ["INT_ADD", "register:40f0:8", ["const:5177c0:8", "const:4:8"]]
+ 005177c0 ["CALL", null, ["callee:00c58970:8"]]
- 00517780 bytes 48041d94
+ 005177c0 bytes 6c041d94
- 005177c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005177c0 ["INT_ADD", "register:40f0:8", ["const:5177c0:8", "const:4:8"]]
- 005177c0 ["CALLIND", null, ["register:0:8"]]
+ 00517800 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00517800 ["INT_ADD", "register:40f0:8", ["const:517800:8", "const:4:8"]]
+ 00517800 ["CALLIND", null, ["register:0:8"]]
- 005177c0 bytes 20013fd6
+ 00517800 bytes 20013fd6
- 0051795c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051795c ["INT_ADD", "register:40f0:8", ["const:51795c:8", "const:4:8"]]
- 0051795c ["CALLIND", null, ["register:0:8"]]
+ 0051799c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051799c ["INT_ADD", "register:40f0:8", ["const:51799c:8", "const:4:8"]]
+ 0051799c ["CALLIND", null, ["register:0:8"]]
- 0051795c bytes 20013fd6
+ 0051799c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee730966123132b3bbab8f72120f5fab"></a>

### [`00517c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517c34.md) → [`00517c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517c74.md) FUN_00517c74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00517650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517650.md) · 呼出先 3件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00517690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md) · 呼出先 3件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00517cc4",
      "incomplete_value": true,
      "site": "00517cc4",
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
      "definition_site": "00517c84",
      "incomplete_value": true,
      "site": "00517c84",
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
      "00517cb0",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ],
    [
      "00517cc4",
      "DATA",
      [
        "storage",
        "00c6a438",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00517cb0",
      "READ",
      [
        "storage",
        "00c9b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "00517cc4",
      "DATA",
      [
        "storage",
        "00c6a508",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517c34.md#insn-00517c60) · [`00517c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517c34.md#insn-00517c70) · [`00517c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517c34.md#insn-00517c9c)
- 新版 [`00517ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517c74.md#insn-00517ca0) · [`00517cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517c74.md#insn-00517cb0) · [`00517cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517c74.md#insn-00517cdc)

~~~diff
- 00517c60 ["INT_ADD", "register:40f0:8", ["const:517c60:8", "const:4:8"]]
- 00517c60 ["CALL", null, ["callee:00c57f60:8"]]
+ 00517ca0 ["INT_ADD", "register:40f0:8", ["const:517ca0:8", "const:4:8"]]
+ 00517ca0 ["CALL", null, ["callee:00c57f60:8"]]
- 00517c60 bytes 8c001d94
+ 00517ca0 bytes b0001d94
- 00517c70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:120:8"]]
- 00517c70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00517cb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
+ 00517cb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00517c70 bytes 089140f9
+ 00517cb0 bytes 08f940f9
- 00517c9c ["INT_ADD", "register:40f0:8", ["const:517c9c:8", "const:4:8"]]
- 00517c9c ["CALL", null, ["callee:00c57f60:8"]]
+ 00517cdc ["INT_ADD", "register:40f0:8", ["const:517cdc:8", "const:4:8"]]
+ 00517cdc ["CALL", null, ["callee:00c57f60:8"]]
- 00517c9c bytes 7d001d94
+ 00517cdc bytes a1001d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f813e38ef01eab530d8eea5d0cf40dd"></a>

### [`00517d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517d28.md) → [`00517d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517d68.md) _ZNK5Botan10Extensions11contents_toERNS_10Data_StoreES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e20.md) · 呼出先 6件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 1件 [`00c59ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ef0.md) · 呼出先 6件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517ee8",
      "incomplete_value": false,
      "site": "00517f08",
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
            "const:cd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517ea8",
      "incomplete_value": false,
      "site": "00517ec8",
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
            "const:d32:8"
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
      "definition_site": "00517ef0",
      "incomplete_value": false,
      "site": "00517f08",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517eb0",
      "incomplete_value": false,
      "site": "00517ec8",
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
            "const:3ea:8"
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
      "definition_site": "00517ef8",
      "incomplete_value": false,
      "site": "00517f08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:2f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00517eb8",
      "incomplete_value": false,
      "site": "00517ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:2b7:8"
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
      "00517df4",
      "PARAM",
      [
        "storage",
        "002b617e",
        null,
        "string"
      ]
    ],
    [
      "00517ee8",
      "PARAM",
      [
        "storage",
        "002a9d32",
        null,
        "string"
      ]
    ],
    [
      "00517ef0",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00517df4",
      "PARAM",
      [
        "storage",
        "002b61be",
        null,
        "string"
      ]
    ],
    [
      "00517ee8",
      "PARAM",
      [
        "storage",
        "002a9cd6",
        null,
        "string"
      ]
    ],
    [
      "00517ef0",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00517ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517d28.md#insn-00517ec8) · [`00517d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517d28.md#insn-00517d68) · [`00517d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517d28.md#insn-00517d94)
- 新版 [`00517f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517d68.md#insn-00517f08) · [`00517da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517d68.md#insn-00517da8) · [`00517dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517d68.md#insn-00517dd4)

~~~diff
- 00517ec8 ["INT_ADD", "register:40f0:8", ["const:517ec8:8", "const:4:8"]]
- 00517ec8 ["CALL", null, ["callee:00c58720:8"]]
+ 00517f08 ["INT_ADD", "register:40f0:8", ["const:517f08:8", "const:4:8"]]
+ 00517f08 ["CALL", null, ["callee:00c58720:8"]]
- 00517ec8 bytes e2011d94
+ 00517f08 bytes 06021d94
- 00517d68 ["COPY", "tmp:0:8", ["const:17e:8"]]
- 00517d68 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00517d68 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00517d68 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00517da8 ["COPY", "tmp:0:8", ["const:1be:8"]]
+ 00517da8 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00517da8 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00517da8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00517d68 bytes b5fa0591
+ 00517da8 bytes b5fa0691
- 00517d94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00517d94 ["INT_ADD", "register:40f0:8", ["const:517d94:8", "const:4:8"]]
- 00517d94 ["CALLIND", null, ["register:0:8"]]
+ 00517dd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00517dd4 ["INT_ADD", "register:40f0:8", ["const:517dd4:8", "const:4:8"]]
+ 00517dd4 ["CALLIND", null, ["register:0:8"]]
- 00517d94 bytes 00013fd6
+ 00517dd4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d167a7a453340b692795c7860683c716"></a>

### [`005181a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/005181a0.md) → [`005181e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005181e0.md) _ZN5Botan14Cert_Extension17Basic_Constraints12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 8件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58710.md) [`00c58880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58880.md)
- 新版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 8件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587d0.md) [`00c587e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587e0.md) [`00c58950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58950.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00518240",
      "incomplete_value": false,
      "site": "00518250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ce000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518200",
      "incomplete_value": false,
      "site": "00518210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ce000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 5
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00518294",
      "incomplete_value": true,
      "site": "00518294",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518254",
      "incomplete_value": true,
      "site": "00518254",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005182d8",
      "incomplete_value": true,
      "site": "005182d8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518298",
      "incomplete_value": true,
      "site": "00518298",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
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
      "00518240",
      "PARAM",
      [
        "storage",
        "002ce4c0",
        null,
        null
      ]
    ],
    [
      "00518284",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "005182c8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00518240",
      "PARAM",
      [
        "storage",
        "002ce500",
        null,
        null
      ]
    ],
    [
      "00518284",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005182c8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00518210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/005181a0.md#insn-00518210) · [`00518214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/005181a0.md#insn-00518214) · [`00518254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/005181a0.md#insn-00518254)
- 新版 [`00518250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005181e0.md#insn-00518250) · [`00518254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005181e0.md#insn-00518254) · [`00518294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005181e0.md#insn-00518294)

~~~diff
- 00518210 ["INT_ADD", "register:40f0:8", ["const:518210:8", "const:4:8"]]
- 00518210 ["CALL", null, ["callee:00c59530:8"]]
+ 00518250 ["INT_ADD", "register:40f0:8", ["const:518250:8", "const:4:8"]]
+ 00518250 ["CALL", null, ["callee:00c59530:8"]]
- 00518210 bytes 94041d94
+ 00518250 bytes b8041d94
- 00518214 ["INT_ADD", "register:40f0:8", ["const:518214:8", "const:4:8"]]
- 00518214 ["CALL", null, ["callee:00c587e0:8"]]
+ 00518254 ["INT_ADD", "register:40f0:8", ["const:518254:8", "const:4:8"]]
+ 00518254 ["CALL", null, ["callee:00c587e0:8"]]
- 00518214 bytes 3f011d94
+ 00518254 bytes 63011d94
- 00518254 ["COPY", "register:0:8", ["register:4048:8"]]
- 00518254 ["INT_ADD", "register:40f0:8", ["const:518254:8", "const:4:8"]]
- 00518254 ["CALLIND", null, ["register:0:8"]]
+ 00518294 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00518294 ["INT_ADD", "register:40f0:8", ["const:518294:8", "const:4:8"]]
+ 00518294 ["CALLIND", null, ["register:0:8"]]
- 00518254 bytes 20013fd6
+ 00518294 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e143778edd5273a68d8222d5352ba294"></a>

### [`00518314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518314.md) → [`00518354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518354.md) _ZNK5Botan14Cert_Extension17Basic_Constraints11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58790.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58860.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 79.49% / 新版 79.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00518390",
      "incomplete_value": true,
      "site": "005183a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:416:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518350",
      "incomplete_value": true,
      "site": "00518364",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46a:8"
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
      "definition_site": "00518394",
      "incomplete_value": true,
      "site": "005183a8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00518354",
      "incomplete_value": true,
      "site": "00518368",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00518398",
      "incomplete_value": true,
      "site": "005183ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518358",
      "incomplete_value": true,
      "site": "0051836c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b50:8"
              ]
            ]
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
      "00518390",
      "READ",
      [
        "storage",
        "002bb46a",
        null,
        "string"
      ]
    ],
    [
      "00518394",
      "READ",
      [
        "storage",
        "002bb477",
        null,
        "string"
      ]
    ],
    [
      "00518398",
      "READ",
      [
        "storage",
        "002c2b50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00518390",
      "READ",
      [
        "storage",
        "002bb416",
        null,
        "string"
      ]
    ],
    [
      "00518394",
      "READ",
      [
        "storage",
        "002bb423",
        null,
        "string"
      ]
    ],
    [
      "00518398",
      "READ",
      [
        "storage",
        "002c2b90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051839c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518314.md#insn-0051839c) · [`005183ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518314.md#insn-005183ac) · [`00518420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518314.md#insn-00518420)
- 新版 [`005183dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518354.md#insn-005183dc) · [`005183ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518354.md#insn-005183ec) · [`00518460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518354.md#insn-00518460)

~~~diff
- 0051839c ["INT_ADD", "register:40f0:8", ["const:51839c:8", "const:4:8"]]
- 0051839c ["CALL", null, ["callee:00c57f80:8"]]
+ 005183dc ["INT_ADD", "register:40f0:8", ["const:5183dc:8", "const:4:8"]]
+ 005183dc ["CALL", null, ["callee:00c57f80:8"]]
- 0051839c bytes c5fe1c94
+ 005183dc bytes e9fe1c94
- 005183ac ["INT_ADD", "register:40f0:8", ["const:5183ac:8", "const:4:8"]]
- 005183ac ["CALL", null, ["callee:00c57f80:8"]]
+ 005183ec ["INT_ADD", "register:40f0:8", ["const:5183ec:8", "const:4:8"]]
+ 005183ec ["CALL", null, ["callee:00c57f80:8"]]
- 005183ac bytes c1fe1c94
+ 005183ec bytes e5fe1c94
- 00518420 ["INT_ADD", "register:40f0:8", ["const:518420:8", "const:4:8"]]
- 00518420 ["CALL", null, ["callee:00c57f80:8"]]
+ 00518460 ["INT_ADD", "register:40f0:8", ["const:518460:8", "const:4:8"]]
+ 00518460 ["CALL", null, ["callee:00c57f80:8"]]
- 00518420 bytes a4fe1c94
+ 00518460 bytes c8fe1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12b0edf7f3e8b434b9b2295887d5aac0"></a>

### [`00518498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518498.md) → [`005184d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005184d8.md) _ZNK5Botan14Cert_Extension9Key_Usage12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005187a0",
      "incomplete_value": false,
      "site": "005187a8",
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
            "const:c6e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518760",
      "incomplete_value": false,
      "site": "00518768",
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
            "const:cca:8"
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
      "definition_site": "005187d8",
      "incomplete_value": true,
      "site": "005187e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518798",
      "incomplete_value": true,
      "site": "005187a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
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
      "definition_site": "005187d4",
      "incomplete_value": false,
      "site": "005187e4",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "00518794",
      "incomplete_value": false,
      "site": "005187a4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "ordinal": 15,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005187a0",
      "PARAM",
      [
        "storage",
        "002b0cca",
        null,
        "string"
      ]
    ],
    [
      "005187d4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "005187d8",
      "READ",
      [
        "storage",
        "00c9ad98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005187a0",
      "PARAM",
      [
        "storage",
        "002b0c6e",
        null,
        "string"
      ]
    ],
    [
      "005187d4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "005187d8",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00518768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518498.md#insn-00518768) · [`005187a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518498.md#insn-005187a4) · [`005184fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518498.md#insn-005184fc)
- 新版 [`005187a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005184d8.md#insn-005187a8) · [`005187e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005184d8.md#insn-005187e4) · [`0051853c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005184d8.md#insn-0051853c)

~~~diff
- 00518768 ["INT_ADD", "register:40f0:8", ["const:518768:8", "const:4:8"]]
- 00518768 ["CALL", null, ["callee:0043de18:8"]]
+ 005187a8 ["INT_ADD", "register:40f0:8", ["const:5187a8:8", "const:4:8"]]
+ 005187a8 ["CALL", null, ["callee:0043de18:8"]]
- 00518768 bytes 9c95fc97
+ 005187a8 bytes 9c95fc97
- 005187a4 ["INT_ADD", "register:40f0:8", ["const:5187a4:8", "const:4:8"]]
- 005187a4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 005187e4 ["INT_ADD", "register:40f0:8", ["const:5187e4:8", "const:4:8"]]
+ 005187e4 ["CALL", null, ["callee:00c57fe0:8"]]
- 005187a4 bytes dbfd1c94
+ 005187e4 bytes fffd1c94
- 005184fc ["INT_ADD", "register:40f0:8", ["const:5184fc:8", "const:4:8"]]
- 005184fc ["CALL", null, ["callee:00c57f60:8"]]
+ 0051853c ["INT_ADD", "register:40f0:8", ["const:51853c:8", "const:4:8"]]
+ 0051853c ["CALL", null, ["callee:00c57f60:8"]]
- 005184fc bytes 65fe1c94
+ 0051853c bytes 89fe1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-586087aad633f0a68dbf0ff352329572"></a>

### [`0051886c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/0051886c.md) → [`005188ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005188ac.md) _ZN5Botan14Cert_Extension9Key_Usage12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 11件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 11件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.14% / 新版 91.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00518b64",
      "incomplete_value": true,
      "site": "00518b64",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518b24",
      "incomplete_value": true,
      "site": "00518b24",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00518ba8",
      "incomplete_value": true,
      "site": "00518ba8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518b68",
      "incomplete_value": true,
      "site": "00518b68",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
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
      "definition_site": "00518be8",
      "incomplete_value": false,
      "site": "00518bf0",
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
            "const:8fa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518ba8",
      "incomplete_value": false,
      "site": "00518bb0",
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
            "const:956:8"
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
      "00518998",
      "READ",
      [
        "storage",
        "002c22b0",
        null,
        null
      ]
    ],
    [
      "005189a0",
      "READ",
      [
        "storage",
        "002c2460",
        null,
        null
      ]
    ],
    [
      "005189a8",
      "READ",
      [
        "storage",
        "002c2840",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00518998",
      "READ",
      [
        "storage",
        "002c22f0",
        null,
        null
      ]
    ],
    [
      "005189a0",
      "READ",
      [
        "storage",
        "002c24a0",
        null,
        null
      ]
    ],
    [
      "005189a8",
      "READ",
      [
        "storage",
        "002c2880",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00518b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/0051886c.md#insn-00518b24) · [`00518b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/0051886c.md#insn-00518b68) · [`00518b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/0051886c.md#insn-00518b70)
- 新版 [`00518b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005188ac.md#insn-00518b64) · [`00518ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005188ac.md#insn-00518ba8) · [`00518bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/005188ac.md#insn-00518bb0)

~~~diff
- 00518b24 ["COPY", "register:0:8", ["register:4048:8"]]
- 00518b24 ["INT_ADD", "register:40f0:8", ["const:518b24:8", "const:4:8"]]
- 00518b24 ["CALLIND", null, ["register:0:8"]]
+ 00518b64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00518b64 ["INT_ADD", "register:40f0:8", ["const:518b64:8", "const:4:8"]]
+ 00518b64 ["CALLIND", null, ["register:0:8"]]
- 00518b24 bytes 20013fd6
+ 00518b64 bytes 20013fd6
- 00518b68 ["COPY", "register:0:8", ["register:4048:8"]]
- 00518b68 ["INT_ADD", "register:40f0:8", ["const:518b68:8", "const:4:8"]]
- 00518b68 ["CALLIND", null, ["register:0:8"]]
+ 00518ba8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00518ba8 ["INT_ADD", "register:40f0:8", ["const:518ba8:8", "const:4:8"]]
+ 00518ba8 ["CALLIND", null, ["register:0:8"]]
- 00518b68 bytes 20013fd6
+ 00518ba8 bytes 20013fd6
- 00518b70 ["INT_ADD", "register:40f0:8", ["const:518b70:8", "const:4:8"]]
- 00518b70 ["CALL", null, ["callee:00c58730:8"]]
+ 00518bb0 ["INT_ADD", "register:40f0:8", ["const:518bb0:8", "const:4:8"]]
+ 00518bb0 ["CALL", null, ["callee:00c58730:8"]]
- 00518b70 bytes bcfe1c94
+ 00518bb0 bytes e0fe1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8865f039b6cd854208d49ec31b031a5"></a>

### [`00518d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518d20.md) → [`00518d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518d60.md) _ZNK5Botan14Cert_Extension9Key_Usage11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58790.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58860.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00518d98",
      "incomplete_value": true,
      "site": "00518d98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b89:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00518d58",
      "incomplete_value": true,
      "site": "00518d58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b5a:8"
              ]
            ]
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
      "definition_site": "00518d90",
      "incomplete_value": true,
      "site": "00518d9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00518d50",
      "incomplete_value": true,
      "site": "00518d5c",
      "value": [
        "LOAD",
        "8",
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
      "00518d80",
      "READ",
      [
        "storage",
        "002a9b5a",
        null,
        "string"
      ]
    ],
    [
      "00518d90",
      "READ",
      [
        "storage",
        "002a9b61",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00518d80",
      "READ",
      [
        "storage",
        "002a9b89",
        null,
        "string"
      ]
    ],
    [
      "00518d90",
      "READ",
      [
        "storage",
        "002a9b90",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00518d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518d20.md#insn-00518d9c) · [`00518d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518d20.md#insn-00518d38) · [`00518d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518d20.md#insn-00518d6c)
- 新版 [`00518ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518d60.md#insn-00518ddc) · [`00518d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518d60.md#insn-00518d78) · [`00518dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00518/00518d60.md#insn-00518dac)

~~~diff
- 00518d9c ["INT_ADD", "register:40f0:8", ["const:518d9c:8", "const:4:8"]]
- 00518d9c ["CALL", null, ["callee:00c57f80:8"]]
+ 00518ddc ["INT_ADD", "register:40f0:8", ["const:518ddc:8", "const:4:8"]]
+ 00518ddc ["CALL", null, ["callee:00c57f80:8"]]
- 00518d9c bytes 45fc1c94
+ 00518ddc bytes 69fc1c94
- 00518d38 ["COPY", "tmp:0:8", ["const:b5a:8"]]
- 00518d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00518d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00518d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00518d78 ["COPY", "tmp:0:8", ["const:b89:8"]]
+ 00518d78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00518d78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00518d78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00518d38 bytes 29692d91
+ 00518d78 bytes 29252e91
- 00518d6c ["INT_ADD", "register:40f0:8", ["const:518d6c:8", "const:4:8"]]
- 00518d6c ["CALL", null, ["callee:00c58860:8"]]
+ 00518dac ["INT_ADD", "register:40f0:8", ["const:518dac:8", "const:4:8"]]
+ 00518dac ["CALL", null, ["callee:00c58860:8"]]
- 00518d6c bytes 89fe1c94
+ 00518dac bytes adfe1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-044722fe23bd9d356bb262572cdfac9a"></a>

### [`00518ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518ff0.md) → [`00519030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519030.md) _ZNK5Botan14Cert_Extension14Subject_Key_ID11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59af0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 80.49% / 新版 80.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051906c",
      "incomplete_value": true,
      "site": "0051907c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:a66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051902c",
      "incomplete_value": true,
      "site": "0051903c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:a35:8"
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
      "definition_site": "00519070",
      "incomplete_value": true,
      "site": "00519080",
      "value": [
        "LOAD",
        "16",
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
                "const:b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00519030",
      "incomplete_value": true,
      "site": "00519040",
      "value": [
        "LOAD",
        "16",
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
                "const:b:8"
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
      "definition_site": "00519074",
      "incomplete_value": true,
      "site": "00519084",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00519034",
      "incomplete_value": true,
      "site": "00519044",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:680:8"
              ]
            ]
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
      "0051906c",
      "READ",
      [
        "storage",
        "002b2a35",
        null,
        "string"
      ]
    ],
    [
      "00519070",
      "READ",
      [
        "storage",
        "002b2a40",
        null,
        "string"
      ]
    ],
    [
      "00519074",
      "READ",
      [
        "storage",
        "002c2680",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051906c",
      "READ",
      [
        "storage",
        "002b2a66",
        null,
        "string"
      ]
    ],
    [
      "00519070",
      "READ",
      [
        "storage",
        "002b2a71",
        null,
        "string"
      ]
    ],
    [
      "00519074",
      "READ",
      [
        "storage",
        "002c26c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051901c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518ff0.md#insn-0051901c) · [`00519024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518ff0.md#insn-00519024) · [`00519028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00518/00518ff0.md#insn-00519028)
- 新版 [`0051905c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519030.md#insn-0051905c) · [`00519064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519030.md#insn-00519064)

~~~diff
- 0051901c ["INT_ADD", "register:40f0:8", ["const:51901c:8", "const:4:8"]]
- 0051901c ["CALL", null, ["callee:00c57f60:8"]]
+ 0051905c ["INT_ADD", "register:40f0:8", ["const:51905c:8", "const:4:8"]]
+ 0051905c ["CALL", null, ["callee:00c57f60:8"]]
- 0051901c bytes 9dfb1c94
+ 0051905c bytes c1fb1c94
- 00519024 ["COPY", "tmp:0:8", ["const:a35:8"]]
- 00519024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00519024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00519024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00519064 ["COPY", "tmp:0:8", ["const:a66:8"]]
+ 00519064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00519064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00519064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00519024 bytes 08d52891
+ 00519064 bytes 08992991
- 00519028 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 00519028 bytes 49edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea6a5ebe2e573b09c79eaf19387713e6"></a>

### [`005190c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/005190c0.md) → [`00519100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519100.md) _ZN5Botan14Cert_Extension14Subject_Key_IDC2ERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEERKNS2_12basic_stringIcNS2_11char_traitsIcEENS4_IcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d40.md) · 呼出先 7件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c59e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e10.md) · 呼出先 7件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00519140",
      "incomplete_value": true,
      "site": "00519148",
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
      "definition_site": "00519100",
      "incomplete_value": true,
      "site": "00519108",
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
      "0051913c",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ],
    [
      "00519148",
      "DATA",
      [
        "storage",
        "00c67a28",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "0051913c",
      "READ",
      [
        "storage",
        "00c9b280",
        null,
        "pointer"
      ]
    ],
    [
      "00519148",
      "DATA",
      [
        "storage",
        "00c67af8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00519148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/005190c0.md#insn-00519148) · [`005190fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/005190c0.md#insn-005190fc) · [`00519124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/005190c0.md#insn-00519124)
- 新版 [`00519188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519100.md#insn-00519188) · [`0051913c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519100.md#insn-0051913c) · [`00519164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519100.md#insn-00519164)

~~~diff
- 00519148 ["COPY", "register:0:8", ["register:4040:8"]]
- 00519148 ["INT_ADD", "register:40f0:8", ["const:519148:8", "const:4:8"]]
- 00519148 ["CALLIND", null, ["register:0:8"]]
+ 00519188 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00519188 ["INT_ADD", "register:40f0:8", ["const:519188:8", "const:4:8"]]
+ 00519188 ["CALLIND", null, ["register:0:8"]]
- 00519148 bytes 00013fd6
+ 00519188 bytes 00013fd6
- 005190fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1b0:8"]]
- 005190fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051913c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:280:8"]]
+ 0051913c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005190fc bytes 29d940f9
+ 0051913c bytes 294141f9
- 00519124 ["INT_ADD", "register:40f0:8", ["const:519124:8", "const:4:8"]]
- 00519124 ["CALL", null, ["callee:00c58f40:8"]]
+ 00519164 ["INT_ADD", "register:40f0:8", ["const:519164:8", "const:4:8"]]
+ 00519164 ["CALL", null, ["callee:00c58f40:8"]]
- 00519124 bytes 53ff1c94
+ 00519164 bytes 77ff1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deab9a20aa0fbada533551ffbe83f719"></a>

### [`00519420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519420.md) → [`00519460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519460.md) _ZN5Botan14Cert_Extension16Authority_Key_ID12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0050acb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050acb8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58880.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0050acf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050acf8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587d0.md) [`00c58950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58950.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.03% / 新版 94.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005194f4",
      "incomplete_value": true,
      "site": "005194f4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005194b4",
      "incomplete_value": true,
      "site": "005194b4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00519538",
      "incomplete_value": true,
      "site": "00519538",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005194f8",
      "incomplete_value": true,
      "site": "005194f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005194e4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00519528",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005194e4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00519528",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00519474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519420.md#insn-00519474) · [`005194b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519420.md#insn-005194b4) · [`005194f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519420.md#insn-005194f8)
- 新版 [`005194b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519460.md#insn-005194b4) · [`005194f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519460.md#insn-005194f4) · [`00519538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/00519460.md#insn-00519538)

~~~diff
- 00519474 ["INT_ADD", "register:40f0:8", ["const:519474:8", "const:4:8"]]
- 00519474 ["CALL", null, ["callee:0050acf8:8"]]
+ 005194b4 ["INT_ADD", "register:40f0:8", ["const:5194b4:8", "const:4:8"]]
+ 005194b4 ["CALL", null, ["callee:0050acf8:8"]]
- 00519474 bytes 11c6ff97
+ 005194b4 bytes 11c6ff97
- 005194b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005194b4 ["INT_ADD", "register:40f0:8", ["const:5194b4:8", "const:4:8"]]
- 005194b4 ["CALLIND", null, ["register:0:8"]]
+ 005194f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005194f4 ["INT_ADD", "register:40f0:8", ["const:5194f4:8", "const:4:8"]]
+ 005194f4 ["CALLIND", null, ["register:0:8"]]
- 005194b4 bytes 20013fd6
+ 005194f4 bytes 20013fd6
- 005194f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005194f8 ["INT_ADD", "register:40f0:8", ["const:5194f8:8", "const:4:8"]]
- 005194f8 ["CALLIND", null, ["register:0:8"]]
+ 00519538 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00519538 ["INT_ADD", "register:40f0:8", ["const:519538:8", "const:4:8"]]
+ 00519538 ["CALLIND", null, ["register:0:8"]]
- 005194f8 bytes 20013fd6
+ 00519538 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcdd570ee0d8379667b99c5bcb3fe9f1"></a>

### [`00519568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519568.md) → [`005195a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/005195a8.md) _ZNK5Botan14Cert_Extension16Authority_Key_ID11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59af0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005195f0",
      "incomplete_value": true,
      "site": "00519600",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:493:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005195b0",
      "incomplete_value": true,
      "site": "005195c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e7:8"
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
      "definition_site": "005195f4",
      "incomplete_value": true,
      "site": "00519604",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "005195b4",
      "incomplete_value": true,
      "site": "005195c4",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005195f8",
      "incomplete_value": true,
      "site": "00519608",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005195b8",
      "incomplete_value": true,
      "site": "005195c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b50:8"
              ]
            ]
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
      "005195f0",
      "READ",
      [
        "storage",
        "002bc4e7",
        null,
        "string"
      ]
    ],
    [
      "005195f4",
      "READ",
      [
        "storage",
        "002bc4f4",
        null,
        "string"
      ]
    ],
    [
      "005195f8",
      "READ",
      [
        "storage",
        "002c2b50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005195f0",
      "READ",
      [
        "storage",
        "002bc493",
        null,
        "string"
      ]
    ],
    [
      "005195f4",
      "READ",
      [
        "storage",
        "002bc4a0",
        null,
        "string"
      ]
    ],
    [
      "005195f8",
      "READ",
      [
        "storage",
        "002c2b90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005195a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519568.md#insn-005195a0) · [`005195a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519568.md#insn-005195a8) · [`005195ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00519/00519568.md#insn-005195ac)
- 新版 [`005195e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/005195a8.md#insn-005195e0) · [`005195e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00519/005195a8.md#insn-005195e8)

~~~diff
- 005195a0 ["INT_ADD", "register:40f0:8", ["const:5195a0:8", "const:4:8"]]
- 005195a0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005195e0 ["INT_ADD", "register:40f0:8", ["const:5195e0:8", "const:4:8"]]
+ 005195e0 ["CALL", null, ["callee:00c57f60:8"]]
- 005195a0 bytes 3cfa1c94
+ 005195e0 bytes 60fa1c94
- 005195a8 ["COPY", "tmp:0:8", ["const:4e7:8"]]
- 005195a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005195a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005195a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005195e8 ["COPY", "tmp:0:8", ["const:493:8"]]
+ 005195e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005195e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005195e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005195a8 bytes 089d1391
+ 005195e8 bytes 084d1291
- 005195ac ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 005195ac bytes 49edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff2e492d45f497ea13e2e9e6300ff55f"></a>

### [`0051a048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a048.md) → [`0051a088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a088.md) _ZNK5Botan14Cert_Extension18Extended_Key_Usage11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58800.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.54% / 新版 92.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051a0cc",
      "incomplete_value": true,
      "site": "0051a0e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a08c",
      "incomplete_value": true,
      "site": "0051a0a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1f9:8"
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
      "definition_site": "0051a0c8",
      "incomplete_value": true,
      "site": "0051a0e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0051a088",
      "incomplete_value": true,
      "site": "0051a0a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0051a0c8",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ],
    [
      "0051a0cc",
      "READ",
      [
        "storage",
        "002ba1f9",
        null,
        "string"
      ]
    ],
    [
      "0051a0d0",
      "READ",
      [
        "storage",
        "002ba208",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051a0c8",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ],
    [
      "0051a0cc",
      "READ",
      [
        "storage",
        "002ba1a5",
        null,
        "string"
      ]
    ],
    [
      "0051a0d0",
      "READ",
      [
        "storage",
        "002ba1b4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051a084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a048.md#insn-0051a084) · [`0051a088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a048.md#insn-0051a088) · [`0051a0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a048.md#insn-0051a0c8)
- 新版 [`0051a0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a088.md#insn-0051a0c4) · [`0051a0c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a088.md#insn-0051a0c8) · [`0051a108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a088.md#insn-0051a108)

~~~diff
- 0051a084 ["COPY", "tmp:0:8", ["const:1f9:8"]]
- 0051a084 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051a084 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051a084 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051a0c4 ["COPY", "tmp:0:8", ["const:1a5:8"]]
+ 0051a0c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051a0c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051a0c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051a084 bytes 29e50791
+ 0051a0c4 bytes 29950691
- 0051a088 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
- 0051a088 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0051a088 ["COPY", "register:5030:8", ["const:0:8"]]
- 0051a088 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0051a0c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:490:8"]]
+ 0051a0c8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0051a0c8 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0051a0c8 ["COPY", "register:5038:8", ["const:0:8"]]
- 0051a088 bytes 0115c13d
+ 0051a0c8 bytes 0125c13d
- 0051a0c8 ["INT_ADD", "register:40f0:8", ["const:51a0c8:8", "const:4:8"]]
- 0051a0c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0051a108 ["INT_ADD", "register:40f0:8", ["const:51a108:8", "const:4:8"]]
+ 0051a108 ["CALL", null, ["callee:00c57f60:8"]]
- 0051a0c8 bytes 72f71c94
+ 0051a108 bytes 96f71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f8f92ebdf540ca62eac39490b2ef8c4"></a>

### [`0051a198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a198.md) → [`0051a1d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a1d8.md) _ZNK5Botan14Cert_Extension16Name_Constraints12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051a218",
      "incomplete_value": true,
      "site": "0051a22c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:600:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a1d8",
      "incomplete_value": true,
      "site": "0051a1ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:65c:8"
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
      "definition_site": "0051a21c",
      "incomplete_value": true,
      "site": "0051a230",
      "value": [
        "LOAD",
        "16",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a1dc",
      "incomplete_value": true,
      "site": "0051a1f0",
      "value": [
        "LOAD",
        "16",
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
                "const:9:8"
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
      "definition_site": "0051a220",
      "incomplete_value": true,
      "site": "0051a234",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a1e0",
      "incomplete_value": true,
      "site": "0051a1f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:790:8"
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
      "0051a218",
      "READ",
      [
        "storage",
        "002a565c",
        null,
        "string"
      ]
    ],
    [
      "0051a21c",
      "READ",
      [
        "storage",
        "002a5665",
        null,
        "string"
      ]
    ],
    [
      "0051a220",
      "READ",
      [
        "storage",
        "002c2790",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051a218",
      "READ",
      [
        "storage",
        "002a5600",
        null,
        "string"
      ]
    ],
    [
      "0051a21c",
      "READ",
      [
        "storage",
        "002a5609",
        null,
        "string"
      ]
    ],
    [
      "0051a220",
      "READ",
      [
        "storage",
        "002c27d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051a230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a198.md#insn-0051a230) · [`0051a1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a198.md#insn-0051a1bc) · [`0051a1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a198.md#insn-0051a1c8)
- 新版 [`0051a270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a1d8.md#insn-0051a270) · [`0051a1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a1d8.md#insn-0051a1fc) · [`0051a208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a1d8.md#insn-0051a208)

~~~diff
- 0051a230 ["INT_ADD", "register:40f0:8", ["const:51a230:8", "const:4:8"]]
- 0051a230 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0051a270 ["INT_ADD", "register:40f0:8", ["const:51a270:8", "const:4:8"]]
+ 0051a270 ["CALL", null, ["callee:00c57fe0:8"]]
- 0051a230 bytes 38f71c94
+ 0051a270 bytes 5cf71c94
- 0051a1bc ["INT_ADD", "register:40f0:8", ["const:51a1bc:8", "const:4:8"]]
- 0051a1bc ["CALL", null, ["callee:00c57fc0:8"]]
+ 0051a1fc ["INT_ADD", "register:40f0:8", ["const:51a1fc:8", "const:4:8"]]
+ 0051a1fc ["CALL", null, ["callee:00c57fc0:8"]]
- 0051a1bc bytes 4df71c94
+ 0051a1fc bytes 71f71c94
- 0051a1c8 ["INT_ADD", "register:40f0:8", ["const:51a1c8:8", "const:4:8"]]
- 0051a1c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0051a208 ["INT_ADD", "register:40f0:8", ["const:51a208:8", "const:4:8"]]
+ 0051a208 ["CALL", null, ["callee:00c57f60:8"]]
- 0051a1c8 bytes 32f71c94
+ 0051a208 bytes 56f71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d651ff210ecea450d344a7266b42dd8"></a>

### [`0051a280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a280.md) → [`0051a2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md) _ZN5Botan14Cert_Extension16Name_Constraints12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 18件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0051a9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a9d4.md) [`0051ab9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ab9c.md) [`0051acc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051acc4.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)
- 新版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 18件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0051aa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051aa14.md) [`0051abdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051abdc.md) [`0051ad04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ad04.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.51% / 新版 94.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 4件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051a418",
      "incomplete_value": true,
      "site": "0051a418",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a3d8",
      "incomplete_value": true,
      "site": "0051a3d8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051a444",
      "incomplete_value": true,
      "site": "0051a444",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a404",
      "incomplete_value": true,
      "site": "0051a404",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051a488",
      "incomplete_value": true,
      "site": "0051a488",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051a448",
      "incomplete_value": true,
      "site": "0051a448",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
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
      "0051a408",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051a434",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051a478",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051a408",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051a434",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051a478",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051a3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a280.md#insn-0051a3d8) · [`0051a404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a280.md#insn-0051a404) · [`0051a448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051a280.md#insn-0051a448)
- 新版 [`0051a418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md#insn-0051a418) · [`0051a444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md#insn-0051a444) · [`0051a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051a2c0.md#insn-0051a488)

~~~diff
- 0051a3d8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051a3d8 ["INT_ADD", "register:40f0:8", ["const:51a3d8:8", "const:4:8"]]
- 0051a3d8 ["CALLIND", null, ["register:0:8"]]
+ 0051a418 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051a418 ["INT_ADD", "register:40f0:8", ["const:51a418:8", "const:4:8"]]
+ 0051a418 ["CALLIND", null, ["register:0:8"]]
- 0051a3d8 bytes 20013fd6
+ 0051a418 bytes 20013fd6
- 0051a404 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051a404 ["INT_ADD", "register:40f0:8", ["const:51a404:8", "const:4:8"]]
- 0051a404 ["CALLIND", null, ["register:0:8"]]
+ 0051a444 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051a444 ["INT_ADD", "register:40f0:8", ["const:51a444:8", "const:4:8"]]
+ 0051a444 ["CALLIND", null, ["register:0:8"]]
- 0051a404 bytes 20013fd6
+ 0051a444 bytes 20013fd6
- 0051a448 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051a448 ["INT_ADD", "register:40f0:8", ["const:51a448:8", "const:4:8"]]
- 0051a448 ["CALLIND", null, ["register:0:8"]]
+ 0051a488 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051a488 ["INT_ADD", "register:40f0:8", ["const:51a488:8", "const:4:8"]]
+ 0051a488 ["CALLIND", null, ["register:0:8"]]
- 0051a448 bytes 20013fd6
+ 0051a488 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f4aac1296202d6f18ebed748eabe4d8"></a>

### [`0051ae2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ae2c.md) → [`0051ae6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ae6c.md) _ZNK5Botan14Cert_Extension16Name_Constraints11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`005093f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005093f8.md) [`00548258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548258.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00509438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509438.md) [`00548298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548298.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.50% / 新版 91.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051aec0",
      "incomplete_value": true,
      "site": "0051aec4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051ae80",
      "incomplete_value": true,
      "site": "0051ae84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:780:8"
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
      "definition_site": "0051af8c",
      "incomplete_value": true,
      "site": "0051af90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051af4c",
      "incomplete_value": true,
      "site": "0051af50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a00:8"
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
      "definition_site": "0051b050",
      "incomplete_value": true,
      "site": "0051b058",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051b010",
      "incomplete_value": true,
      "site": "0051b018",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
      "0051aec0",
      "READ",
      [
        "storage",
        "002c2780",
        null,
        null
      ]
    ],
    [
      "0051aefc",
      "READ",
      [
        "storage",
        "002a8cce",
        null,
        "string"
      ]
    ],
    [
      "0051aefc",
      "READ",
      [
        "storage",
        "002a8cde",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051aec0",
      "READ",
      [
        "storage",
        "002c27c0",
        null,
        null
      ]
    ],
    [
      "0051aefc",
      "READ",
      [
        "storage",
        "002a8c72",
        null,
        "string"
      ]
    ],
    [
      "0051aefc",
      "READ",
      [
        "storage",
        "002a8c82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ae2c.md#insn-0051af10) · [`0051ae64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ae2c.md#insn-0051ae64) · [`0051ae7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ae2c.md#insn-0051ae7c)
- 新版 [`0051af50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ae6c.md#insn-0051af50) · [`0051aea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ae6c.md#insn-0051aea4) · [`0051aebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ae6c.md#insn-0051aebc)

~~~diff
- 0051af10 ["INT_ADD", "register:40f0:8", ["const:51af10:8", "const:4:8"]]
- 0051af10 ["CALL", null, ["callee:00c58500:8"]]
+ 0051af50 ["INT_ADD", "register:40f0:8", ["const:51af50:8", "const:4:8"]]
+ 0051af50 ["CALL", null, ["callee:00c58500:8"]]
- 0051af10 bytes 48f51c94
+ 0051af50 bytes 6cf51c94
- 0051ae64 ["INT_ADD", "register:40f0:8", ["const:51ae64:8", "const:4:8"]]
- 0051ae64 ["CALL", null, ["callee:004518f0:8"]]
+ 0051aea4 ["INT_ADD", "register:40f0:8", ["const:51aea4:8", "const:4:8"]]
+ 0051aea4 ["CALL", null, ["callee:004518f0:8"]]
- 0051ae64 bytes 93dafc97
+ 0051aea4 bytes 93dafc97
- 0051ae7c ["COPY", "tmp:0:8", ["const:cce:8"]]
- 0051ae7c ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 0051ae7c ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 0051ae7c ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 0051aebc ["COPY", "tmp:0:8", ["const:c72:8"]]
+ 0051aebc ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 0051aebc ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 0051aebc ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 0051ae7c bytes 393b3391
+ 0051aebc bytes 39cb3191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cd1a6b11e2fde3dc3031630942c27e6"></a>

### [`0051b11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b11c.md) → [`0051b15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b15c.md) _ZN5Botan14Cert_Extension16Name_Constraints8validateERKNS_16X509_CertificateES4_RKNSt6__ndk16vectorINS5_10shared_ptrIS3_EENS5_9allocatorIS8_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005408bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408bc.md) [`0054cb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cb9c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005408fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005408fc.md) [`0054cbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054c/0054cbdc.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.95% / 新版 97.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051b344",
      "incomplete_value": true,
      "site": "0051b344",
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
      "definition_site": "0051b304",
      "incomplete_value": true,
      "site": "0051b304",
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
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051b344",
      "incomplete_value": true,
      "site": "0051b344",
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
      "definition_site": "0051b304",
      "incomplete_value": true,
      "site": "0051b304",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051b3cc",
      "incomplete_value": true,
      "site": "0051b3cc",
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
      "definition_site": "0051b38c",
      "incomplete_value": true,
      "site": "0051b38c",
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
      "0051b1d4",
      "READ",
      [
        "storage",
        "002a548f",
        null,
        "string"
      ]
    ],
    [
      "0051b1d8",
      "READ",
      [
        "storage",
        "002a549d",
        null,
        "string"
      ]
    ],
    [
      "0051b2d0",
      "READ",
      [
        "storage",
        "002a548f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051b1d4",
      "READ",
      [
        "storage",
        "002a5433",
        null,
        "string"
      ]
    ],
    [
      "0051b1d8",
      "READ",
      [
        "storage",
        "002a5441",
        null,
        "string"
      ]
    ],
    [
      "0051b2d0",
      "READ",
      [
        "storage",
        "002a5433",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051b180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b11c.md#insn-0051b180) · [`0051b18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b11c.md#insn-0051b18c) · [`0051b1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051b11c.md#insn-0051b1b8)
- 新版 [`0051b1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b15c.md#insn-0051b1c0) · [`0051b1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b15c.md#insn-0051b1cc) · [`0051b1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051b15c.md#insn-0051b1f8)

~~~diff
- 0051b180 ["INT_ADD", "register:40f0:8", ["const:51b180:8", "const:4:8"]]
- 0051b180 ["CALL", null, ["callee:00c59ac0:8"]]
+ 0051b1c0 ["INT_ADD", "register:40f0:8", ["const:51b1c0:8", "const:4:8"]]
+ 0051b1c0 ["CALL", null, ["callee:00c59ac0:8"]]
- 0051b180 bytes 1cfa1c94
+ 0051b1c0 bytes 40fa1c94
- 0051b18c ["COPY", "tmp:0:8", ["const:48f:8"]]
- 0051b18c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 0051b18c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 0051b18c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 0051b1cc ["COPY", "tmp:0:8", ["const:433:8"]]
+ 0051b1cc ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 0051b1cc ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 0051b1cc ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 0051b18c bytes 943e1291
+ 0051b1cc bytes 94ce1091
- 0051b1b8 ["INT_ADD", "register:40f0:8", ["const:51b1b8:8", "const:4:8"]]
- 0051b1b8 ["CALL", null, ["callee:00c59f20:8"]]
+ 0051b1f8 ["INT_ADD", "register:40f0:8", ["const:51b1f8:8", "const:4:8"]]
+ 0051b1f8 ["CALL", null, ["callee:00c59f20:8"]]
- 0051b1b8 bytes 26fb1c94
+ 0051b1f8 bytes 4afb1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc8a074e7f23945e6e3f80f92ae3c376"></a>

### [`0051bae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051bae8.md) → [`0051bb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051bb28.md) _ZNK5Botan14Cert_Extension20Certificate_Policies12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`0054cc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054c/0054cc20.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`0054cc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054c/0054cc60.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.17% / 新版 97.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051bb94",
      "incomplete_value": true,
      "site": "0051bb9c",
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
      "definition_site": "0051bb54",
      "incomplete_value": true,
      "site": "0051bb5c",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051bbb8",
      "incomplete_value": true,
      "site": "0051bbb8",
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
      "definition_site": "0051bb78",
      "incomplete_value": true,
      "site": "0051bb78",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051bcec",
      "incomplete_value": true,
      "site": "0051bcec",
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
      "definition_site": "0051bcac",
      "incomplete_value": true,
      "site": "0051bcac",
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
      "0051bb78",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "0051bb9c",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051bba8",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051bb78",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0051bb9c",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051bba8",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051bb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051bae8.md#insn-0051bb38) · [`0051be84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051bae8.md#insn-0051be84) · [`0051bec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051b/0051bae8.md#insn-0051bec4)
- 新版 [`0051bb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051bb28.md#insn-0051bb78) · [`0051bec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051bb28.md#insn-0051bec4) · [`0051bf04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051b/0051bb28.md#insn-0051bf04)

~~~diff
- 0051bb38 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
- 0051bb38 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051bb78 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
+ 0051bb78 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0051bb38 bytes 29a146f9
+ 0051bb78 bytes 290947f9
- 0051be84 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051be84 ["INT_ADD", "register:40f0:8", ["const:51be84:8", "const:4:8"]]
- 0051be84 ["CALLIND", null, ["register:0:8"]]
+ 0051bec4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051bec4 ["INT_ADD", "register:40f0:8", ["const:51bec4:8", "const:4:8"]]
+ 0051bec4 ["CALLIND", null, ["register:0:8"]]
- 0051be84 bytes 20013fd6
+ 0051bec4 bytes 20013fd6
- 0051bec4 ["INT_ADD", "register:40f0:8", ["const:51bec4:8", "const:4:8"]]
- 0051bec4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0051bf04 ["INT_ADD", "register:40f0:8", ["const:51bf04:8", "const:4:8"]]
+ 0051bf04 ["CALL", null, ["callee:00c57f80:8"]]
- 0051bec4 bytes fbef1c94
+ 0051bf04 bytes 1ff01c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c650aba8af9f12767159731f940b8ec9"></a>

### [`0051c068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c068.md) → [`0051c0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c0a8.md) _ZN5Botan14Cert_Extension20Certificate_Policies12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0053da0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053da0c.md) [`0054b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`0053da4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053da4c.md) [`0054b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b984.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051c130",
      "incomplete_value": true,
      "site": "0051c130",
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
      "definition_site": "0051c0f0",
      "incomplete_value": true,
      "site": "0051c0f0",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051c3c4",
      "incomplete_value": true,
      "site": "0051c3c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051c384",
      "incomplete_value": true,
      "site": "0051c384",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051c408",
      "incomplete_value": true,
      "site": "0051c408",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051c3c8",
      "incomplete_value": true,
      "site": "0051c3c8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051c110",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "0051c130",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051c15c",
      "DATA",
      [
        "storage",
        "00c6a488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051c110",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0051c130",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051c15c",
      "DATA",
      [
        "storage",
        "00c6a558",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051c130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c068.md#insn-0051c130) · [`0051c344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c068.md#insn-0051c344) · [`0051c384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c068.md#insn-0051c384)
- 新版 [`0051c170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c0a8.md#insn-0051c170) · [`0051c384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c0a8.md#insn-0051c384) · [`0051c3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c0a8.md#insn-0051c3c4)

~~~diff
- 0051c130 ["INT_ADD", "register:40f0:8", ["const:51c130:8", "const:4:8"]]
- 0051c130 ["CALL", null, ["callee:00c58760:8"]]
+ 0051c170 ["INT_ADD", "register:40f0:8", ["const:51c170:8", "const:4:8"]]
+ 0051c170 ["CALL", null, ["callee:00c58760:8"]]
- 0051c130 bytes 58f11c94
+ 0051c170 bytes 7cf11c94
- 0051c344 ["INT_ADD", "register:40f0:8", ["const:51c344:8", "const:4:8"]]
- 0051c344 ["CALL", null, ["callee:00c587e0:8"]]
+ 0051c384 ["INT_ADD", "register:40f0:8", ["const:51c384:8", "const:4:8"]]
+ 0051c384 ["CALL", null, ["callee:00c587e0:8"]]
- 0051c344 bytes f3f01c94
+ 0051c384 bytes 17f11c94
- 0051c384 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051c384 ["INT_ADD", "register:40f0:8", ["const:51c384:8", "const:4:8"]]
- 0051c384 ["CALLIND", null, ["register:0:8"]]
+ 0051c3c4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051c3c4 ["INT_ADD", "register:40f0:8", ["const:51c3c4:8", "const:4:8"]]
+ 0051c3c4 ["CALLIND", null, ["register:0:8"]]
- 0051c384 bytes 20013fd6
+ 0051c3c4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-834c6645aebf27b44f0d89f3f8e4fe97"></a>

### [`0051c6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c6bc.md) → [`0051c6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c6fc.md) _ZNK5Botan14Cert_Extension20Certificate_Policies11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58800.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.04% / 新版 91.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051c73c",
      "incomplete_value": true,
      "site": "0051c750",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:78b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051c6fc",
      "incomplete_value": true,
      "site": "0051c710",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:7e7:8"
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
      "definition_site": "0051c738",
      "incomplete_value": true,
      "site": "0051c750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051c6f8",
      "incomplete_value": true,
      "site": "0051c710",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a90:8"
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
      "definition_site": "0051c754",
      "incomplete_value": true,
      "site": "0051c758",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051c714",
      "incomplete_value": true,
      "site": "0051c718",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
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
      "0051c738",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ],
    [
      "0051c73c",
      "READ",
      [
        "storage",
        "002ae7e7",
        null,
        "string"
      ]
    ],
    [
      "0051c754",
      "READ",
      [
        "storage",
        "002ae7f1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051c738",
      "READ",
      [
        "storage",
        "002c2ad0",
        null,
        null
      ]
    ],
    [
      "0051c73c",
      "READ",
      [
        "storage",
        "002ae78b",
        null,
        "string"
      ]
    ],
    [
      "0051c754",
      "READ",
      [
        "storage",
        "002ae795",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051c6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c6bc.md#insn-0051c6f4) · [`0051c6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c6bc.md#insn-0051c6f8) · [`0051c73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051c6bc.md#insn-0051c73c)
- 新版 [`0051c734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c6fc.md#insn-0051c734) · [`0051c738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c6fc.md#insn-0051c738) · [`0051c77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051c6fc.md#insn-0051c77c)

~~~diff
- 0051c6f4 ["COPY", "tmp:0:8", ["const:7e7:8"]]
- 0051c6f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051c6f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051c6f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051c734 ["COPY", "tmp:0:8", ["const:78b:8"]]
+ 0051c734 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051c734 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051c734 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051c6f4 bytes 299d1f91
+ 0051c734 bytes 292d1e91
- 0051c6f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
- 0051c6f8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0051c6f8 ["COPY", "register:5030:8", ["const:0:8"]]
- 0051c6f8 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0051c738 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ad0:8"]]
+ 0051c738 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0051c738 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0051c738 ["COPY", "register:5038:8", ["const:0:8"]]
- 0051c6f8 bytes 01a5c23d
+ 0051c738 bytes 01b5c23d
- 0051c73c ["INT_ADD", "register:40f0:8", ["const:51c73c:8", "const:4:8"]]
- 0051c73c ["CALL", null, ["callee:00c57f60:8"]]
+ 0051c77c ["INT_ADD", "register:40f0:8", ["const:51c77c:8", "const:4:8"]]
+ 0051c77c ["CALL", null, ["callee:00c57f60:8"]]
- 0051c73c bytes d5ed1c94
+ 0051c77c bytes f9ed1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-482eff75f0ab5b820469cee77d1003a7"></a>

### [`0051cab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051cab0.md) → [`0051caf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051caf0.md) _ZNK5Botan14Cert_Extension28Authority_Information_Access12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 0件  · 呼出先 11件 [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051cb70",
      "incomplete_value": true,
      "site": "0051cb70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f9c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051cb30",
      "incomplete_value": true,
      "site": "0051cb30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f5c:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0051cc64",
      "incomplete_value": true,
      "site": "0051cc64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051cc24",
      "incomplete_value": true,
      "site": "0051cc24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
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
      "0051cb60",
      "READ",
      [
        "storage",
        "002b5f5c",
        null,
        "string"
      ]
    ],
    [
      "0051cc54",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051cb60",
      "READ",
      [
        "storage",
        "002b5f9c",
        null,
        "string"
      ]
    ],
    [
      "0051cc54",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051cc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051cab0.md#insn-0051cc24) · [`0051cae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051cab0.md#insn-0051cae4) · [`0051cb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051cab0.md#insn-0051cb00)
- 新版 [`0051cc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051caf0.md#insn-0051cc64) · [`0051cb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051caf0.md#insn-0051cb24) · [`0051cb40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051caf0.md#insn-0051cb40)

~~~diff
- 0051cc24 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051cc24 ["INT_ADD", "register:40f0:8", ["const:51cc24:8", "const:4:8"]]
- 0051cc24 ["CALLIND", null, ["register:0:8"]]
+ 0051cc64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051cc64 ["INT_ADD", "register:40f0:8", ["const:51cc64:8", "const:4:8"]]
+ 0051cc64 ["CALLIND", null, ["register:0:8"]]
- 0051cc24 bytes 20013fd6
+ 0051cc64 bytes 20013fd6
- 0051cae4 ["INT_ADD", "register:40f0:8", ["const:51cae4:8", "const:4:8"]]
- 0051cae4 ["CALL", null, ["callee:00c59a30:8"]]
+ 0051cb24 ["INT_ADD", "register:40f0:8", ["const:51cb24:8", "const:4:8"]]
+ 0051cb24 ["CALL", null, ["callee:00c59a30:8"]]
- 0051cae4 bytes 9ff31c94
+ 0051cb24 bytes c3f31c94
- 0051cb00 ["INT_ADD", "register:40f0:8", ["const:51cb00:8", "const:4:8"]]
- 0051cb00 ["CALL", null, ["callee:00c58780:8"]]
+ 0051cb40 ["INT_ADD", "register:40f0:8", ["const:51cb40:8", "const:4:8"]]
+ 0051cb40 ["CALL", null, ["callee:00c58780:8"]]
- 0051cb00 bytes ecee1c94
+ 0051cb40 bytes 10ef1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8d36919128002d4b20d189644fbac6a"></a>

### [`0051ccdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051ccdc.md) → [`0051cd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051cd1c.md) _ZN5Botan14Cert_Extension28Authority_Information_Access12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.90% / 新版 95.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051cdcc",
      "incomplete_value": true,
      "site": "0051cde8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051cd8c",
      "incomplete_value": true,
      "site": "0051cda8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:780:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0051cda8",
      "incomplete_value": true,
      "site": "0051cda8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051cd68",
      "incomplete_value": true,
      "site": "0051cd68",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051d048",
      "incomplete_value": true,
      "site": "0051d048",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d008",
      "incomplete_value": true,
      "site": "0051d008",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051cd98",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051cdcc",
      "READ",
      [
        "storage",
        "002c2780",
        null,
        null
      ]
    ],
    [
      "0051ce58",
      "READ",
      [
        "storage",
        "002b5f5c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051cd98",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051cdcc",
      "READ",
      [
        "storage",
        "002c27c0",
        null,
        null
      ]
    ],
    [
      "0051ce58",
      "READ",
      [
        "storage",
        "002b5f9c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051cd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051ccdc.md#insn-0051cd28) · [`0051cd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051ccdc.md#insn-0051cd68) · [`0051d008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051c/0051ccdc.md#insn-0051d008)
- 新版 [`0051cd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051cd1c.md#insn-0051cd68) · [`0051cda8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051cd1c.md#insn-0051cda8) · [`0051d048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051c/0051cd1c.md#insn-0051d048)

~~~diff
- 0051cd28 ["INT_ADD", "register:40f0:8", ["const:51cd28:8", "const:4:8"]]
- 0051cd28 ["CALL", null, ["callee:00c587d0:8"]]
+ 0051cd68 ["INT_ADD", "register:40f0:8", ["const:51cd68:8", "const:4:8"]]
+ 0051cd68 ["CALL", null, ["callee:00c587d0:8"]]
- 0051cd28 bytes 76ee1c94
+ 0051cd68 bytes 9aee1c94
- 0051cd68 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051cd68 ["INT_ADD", "register:40f0:8", ["const:51cd68:8", "const:4:8"]]
- 0051cd68 ["CALLIND", null, ["register:0:8"]]
+ 0051cda8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051cda8 ["INT_ADD", "register:40f0:8", ["const:51cda8:8", "const:4:8"]]
+ 0051cda8 ["CALLIND", null, ["register:0:8"]]
- 0051cd68 bytes 20013fd6
+ 0051cda8 bytes 20013fd6
- 0051d008 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051d008 ["INT_ADD", "register:40f0:8", ["const:51d008:8", "const:4:8"]]
- 0051d008 ["CALLIND", null, ["register:0:8"]]
+ 0051d048 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051d048 ["INT_ADD", "register:40f0:8", ["const:51d048:8", "const:4:8"]]
+ 0051d048 ["CALLIND", null, ["register:0:8"]]
- 0051d008 bytes 20013fd6
+ 0051d048 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9987438f3b61e39b75dfe8c155047446"></a>

### [`0051d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d508.md) → [`0051d548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d548.md) _ZNK5Botan14Cert_Extension28Authority_Information_Access11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.14% / 新版 85.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051d5a8",
      "incomplete_value": true,
      "site": "0051d5a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d568",
      "incomplete_value": true,
      "site": "0051d568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a0:8"
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
      "definition_site": "0051d5ac",
      "incomplete_value": true,
      "site": "0051d5ac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0051d56c",
      "incomplete_value": true,
      "site": "0051d56c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0051d5e4",
      "incomplete_value": true,
      "site": "0051d5ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b0d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d5a4",
      "incomplete_value": true,
      "site": "0051d5ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:adc:8"
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
      "0051d598",
      "READ",
      [
        "storage",
        "002c11a0",
        null,
        "string"
      ]
    ],
    [
      "0051d59c",
      "READ",
      [
        "storage",
        "002c11a6",
        null,
        "string"
      ]
    ],
    [
      "0051d5e4",
      "READ",
      [
        "storage",
        "002b1adc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051d598",
      "READ",
      [
        "storage",
        "002c11e0",
        null,
        "string"
      ]
    ],
    [
      "0051d59c",
      "READ",
      [
        "storage",
        "002c11e6",
        null,
        "string"
      ]
    ],
    [
      "0051d5e4",
      "READ",
      [
        "storage",
        "002b1b0d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d508.md#insn-0051d5a8) · [`0051d5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d508.md#insn-0051d5f0) · [`0051d550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d508.md#insn-0051d550)
- 新版 [`0051d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d548.md#insn-0051d5e8) · [`0051d630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d548.md#insn-0051d630) · [`0051d590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d548.md#insn-0051d590)

~~~diff
- 0051d5a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:780:8"]]
- 0051d5a8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0051d5a8 ["COPY", "register:5030:8", ["const:0:8"]]
- 0051d5a8 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0051d5e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7c0:8"]]
+ 0051d5e8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0051d5e8 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0051d5e8 ["COPY", "register:5038:8", ["const:0:8"]]
- 0051d5a8 bytes 01e1c13d
+ 0051d5e8 bytes 01f1c13d
- 0051d5f0 ["INT_ADD", "register:40f0:8", ["const:51d5f0:8", "const:4:8"]]
- 0051d5f0 ["CALL", null, ["callee:004ff1e0:8"]]
+ 0051d630 ["INT_ADD", "register:40f0:8", ["const:51d630:8", "const:4:8"]]
+ 0051d630 ["CALL", null, ["callee:004ff1e0:8"]]
- 0051d5f0 bytes ec86ff97
+ 0051d630 bytes ec86ff97
- 0051d550 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 0051d550 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051d550 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051d550 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051d590 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 0051d590 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051d590 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051d590 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051d550 bytes 29810691
+ 0051d590 bytes 29810791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ddaec411faac1cfc6eeef1ed9bdce8b"></a>

### [`0051d660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d660.md) → [`0051d6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d6a0.md) _ZNK5Botan14Cert_Extension10CRL_Number14get_crl_numberEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59db0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c59e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e80.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0051d704",
      "incomplete_value": false,
      "site": "0051d70c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d6c4",
      "incomplete_value": false,
      "site": "0051d6cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:a8c:8"
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
      "definition_site": "0051d740",
      "incomplete_value": true,
      "site": "0051d74c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d700",
      "incomplete_value": true,
      "site": "0051d70c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
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
      "definition_site": "0051d73c",
      "incomplete_value": false,
      "site": "0051d74c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "0051d6fc",
      "incomplete_value": false,
      "site": "0051d70c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "0051d704",
      "PARAM",
      [
        "storage",
        "002afa8c",
        null,
        "string"
      ]
    ],
    [
      "0051d73c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0051d740",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051d704",
      "PARAM",
      [
        "storage",
        "002afa30",
        null,
        "string"
      ]
    ],
    [
      "0051d73c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0051d740",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051d6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d660.md#insn-0051d6cc) · [`0051d70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d660.md#insn-0051d70c) · [`0051d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d660.md#insn-0051d6b8)
- 新版 [`0051d70c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d6a0.md#insn-0051d70c) · [`0051d74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d6a0.md#insn-0051d74c) · [`0051d6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d6a0.md#insn-0051d6f8)

~~~diff
- 0051d6cc ["INT_ADD", "register:40f0:8", ["const:51d6cc:8", "const:4:8"]]
- 0051d6cc ["CALL", null, ["callee:0043de18:8"]]
+ 0051d70c ["INT_ADD", "register:40f0:8", ["const:51d70c:8", "const:4:8"]]
+ 0051d70c ["CALL", null, ["callee:0043de18:8"]]
- 0051d6cc bytes c381fc97
+ 0051d70c bytes c381fc97
- 0051d70c ["INT_ADD", "register:40f0:8", ["const:51d70c:8", "const:4:8"]]
- 0051d70c ["CALL", null, ["callee:00c57fe0:8"]]
+ 0051d74c ["INT_ADD", "register:40f0:8", ["const:51d74c:8", "const:4:8"]]
+ 0051d74c ["CALL", null, ["callee:00c57fe0:8"]]
- 0051d70c bytes 01ea1c94
+ 0051d74c bytes 25ea1c94
- 0051d6b8 ["INT_ADD", "register:40f0:8", ["const:51d6b8:8", "const:4:8"]]
- 0051d6b8 ["CALL", null, ["callee:00c57fc0:8"]]
+ 0051d6f8 ["INT_ADD", "register:40f0:8", ["const:51d6f8:8", "const:4:8"]]
+ 0051d6f8 ["CALL", null, ["callee:00c57fc0:8"]]
- 0051d6b8 bytes 0eea1c94
+ 0051d6f8 bytes 32ea1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4887f7d89e1cd46a7def23843d8ccbb"></a>

### [`0051d760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d760.md) → [`0051d7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d7a0.md) _ZNK5Botan14Cert_Extension10CRL_Number4copyEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051d7e8",
      "incomplete_value": true,
      "site": "0051d7f0",
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
      "definition_site": "0051d7a8",
      "incomplete_value": true,
      "site": "0051d7b0",
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
      "definition_site": "0051d82c",
      "incomplete_value": false,
      "site": "0051d834",
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
            "const:28d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d7ec",
      "incomplete_value": false,
      "site": "0051d7f4",
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
            "const:24d:8"
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
      "definition_site": "0051d868",
      "incomplete_value": true,
      "site": "0051d874",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d828",
      "incomplete_value": true,
      "site": "0051d834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
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
      "0051d7dc",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "0051d7f0",
      "DATA",
      [
        "storage",
        "00c68cc0",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "0051d82c",
      "PARAM",
      [
        "storage",
        "002b824d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051d7dc",
      "READ",
      [
        "storage",
        "00c9b270",
        null,
        "pointer"
      ]
    ],
    [
      "0051d7f0",
      "DATA",
      [
        "storage",
        "00c68d90",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "0051d82c",
      "PARAM",
      [
        "storage",
        "002b828d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051d7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d760.md#insn-0051d7f4) · [`0051d834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d760.md#insn-0051d834) · [`0051d790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d760.md#insn-0051d790)
- 新版 [`0051d834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d7a0.md#insn-0051d834) · [`0051d874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d7a0.md#insn-0051d874) · [`0051d7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d7a0.md#insn-0051d7d0)

~~~diff
- 0051d7f4 ["INT_ADD", "register:40f0:8", ["const:51d7f4:8", "const:4:8"]]
- 0051d7f4 ["CALL", null, ["callee:0043de18:8"]]
+ 0051d834 ["INT_ADD", "register:40f0:8", ["const:51d834:8", "const:4:8"]]
+ 0051d834 ["CALL", null, ["callee:0043de18:8"]]
- 0051d7f4 bytes 7981fc97
+ 0051d834 bytes 7981fc97
- 0051d834 ["INT_ADD", "register:40f0:8", ["const:51d834:8", "const:4:8"]]
- 0051d834 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0051d874 ["INT_ADD", "register:40f0:8", ["const:51d874:8", "const:4:8"]]
+ 0051d874 ["CALL", null, ["callee:00c57fe0:8"]]
- 0051d834 bytes b7e91c94
+ 0051d874 bytes dbe91c94
- 0051d790 ["INT_ADD", "register:40f0:8", ["const:51d790:8", "const:4:8"]]
- 0051d790 ["CALL", null, ["callee:00c57f60:8"]]
+ 0051d7d0 ["INT_ADD", "register:40f0:8", ["const:51d7d0:8", "const:4:8"]]
+ 0051d7d0 ["CALL", null, ["callee:00c57f60:8"]]
- 0051d790 bytes c0e91c94
+ 0051d7d0 bytes e4e91c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00bcba1967e0b9221021a039d17370fd"></a>

### [`0051d888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d888.md) → [`0051d8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d8c8.md) _ZNK5Botan14Cert_Extension10CRL_Number12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051d940",
      "incomplete_value": true,
      "site": "0051d940",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d900",
      "incomplete_value": true,
      "site": "0051d900",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051d9b8",
      "incomplete_value": true,
      "site": "0051d9b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051d978",
      "incomplete_value": true,
      "site": "0051d978",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051d930",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051d9a8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051d930",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051d9a8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051d900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d888.md#insn-0051d900) · [`0051d940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d888.md#insn-0051d940) · [`0051d978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051d888.md#insn-0051d978)
- 新版 [`0051d940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d8c8.md#insn-0051d940) · [`0051d980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d8c8.md#insn-0051d980) · [`0051d9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051d8c8.md#insn-0051d9b8)

~~~diff
- 0051d900 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051d900 ["INT_ADD", "register:40f0:8", ["const:51d900:8", "const:4:8"]]
- 0051d900 ["CALLIND", null, ["register:0:8"]]
+ 0051d940 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051d940 ["INT_ADD", "register:40f0:8", ["const:51d940:8", "const:4:8"]]
+ 0051d940 ["CALLIND", null, ["register:0:8"]]
- 0051d900 bytes 20013fd6
+ 0051d940 bytes 20013fd6
- 0051d940 ["INT_ADD", "register:40f0:8", ["const:51d940:8", "const:4:8"]]
- 0051d940 ["CALL", null, ["callee:00535bc0:8"]]
+ 0051d980 ["INT_ADD", "register:40f0:8", ["const:51d980:8", "const:4:8"]]
+ 0051d980 ["CALL", null, ["callee:00535bc0:8"]]
- 0051d940 bytes 90600094
+ 0051d980 bytes 90600094
- 0051d978 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051d978 ["INT_ADD", "register:40f0:8", ["const:51d978:8", "const:4:8"]]
- 0051d978 ["CALLIND", null, ["register:0:8"]]
+ 0051d9b8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051d9b8 ["INT_ADD", "register:40f0:8", ["const:51d9b8:8", "const:4:8"]]
+ 0051d9b8 ["CALLIND", null, ["register:0:8"]]
- 0051d978 bytes 20013fd6
+ 0051d9b8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a27c792656c42ca766c2c18d78af52ae"></a>

### [`0051dacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dacc.md) → [`0051db0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051db0c.md) _ZNK5Botan14Cert_Extension10CRL_Number11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58790.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58860.md)

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
      "definition_site": "0051db2c",
      "incomplete_value": true,
      "site": "0051db48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051daec",
      "incomplete_value": true,
      "site": "0051db08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3fc:8"
              ]
            ]
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
      "0051db2c",
      "READ",
      [
        "storage",
        "002ab3fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051db2c",
      "READ",
      [
        "storage",
        "002ab3a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051dae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dacc.md#insn-0051dae4) · [`0051db10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dacc.md#insn-0051db10) · [`0051db20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dacc.md#insn-0051db20)
- 新版 [`0051db24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051db0c.md#insn-0051db24) · [`0051db50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051db0c.md#insn-0051db50) · [`0051db60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051db0c.md#insn-0051db60)

~~~diff
- 0051dae4 ["COPY", "tmp:0:8", ["const:3fc:8"]]
- 0051dae4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051dae4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051dae4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051db24 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 0051db24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051db24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051db24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051dae4 bytes 29f10f91
+ 0051db24 bytes 29810e91
- 0051db10 ["INT_ADD", "register:40f0:8", ["const:51db10:8", "const:4:8"]]
- 0051db10 ["CALL", null, ["callee:00c58860:8"]]
+ 0051db50 ["INT_ADD", "register:40f0:8", ["const:51db50:8", "const:4:8"]]
+ 0051db50 ["CALL", null, ["callee:00c58860:8"]]
- 0051db10 bytes 20eb1c94
+ 0051db50 bytes 44eb1c94
- 0051db20 ["INT_ADD", "register:40f0:8", ["const:51db20:8", "const:4:8"]]
- 0051db20 ["CALL", null, ["callee:004ff1e0:8"]]
+ 0051db60 ["INT_ADD", "register:40f0:8", ["const:51db60:8", "const:4:8"]]
+ 0051db60 ["CALL", null, ["callee:004ff1e0:8"]]
- 0051db20 bytes a085ff97
+ 0051db60 bytes a085ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-466c7f6beb24b62fbefa4adc7f83ea5e"></a>

### [`0051dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dba4.md) → [`0051dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dbe4.md) _ZNK5Botan14Cert_Extension14CRL_ReasonCode12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051dc5c",
      "incomplete_value": true,
      "site": "0051dc5c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051dc1c",
      "incomplete_value": true,
      "site": "0051dc1c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051dcd4",
      "incomplete_value": true,
      "site": "0051dcd4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051dc94",
      "incomplete_value": true,
      "site": "0051dc94",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051dc4c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051dcc4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051dc4c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051dcc4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051dc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dba4.md#insn-0051dc1c) · [`0051dc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dba4.md#insn-0051dc5c) · [`0051dc94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dba4.md#insn-0051dc94)
- 新版 [`0051dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dbe4.md#insn-0051dc5c) · [`0051dc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dbe4.md#insn-0051dc9c) · [`0051dcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dbe4.md#insn-0051dcd4)

~~~diff
- 0051dc1c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051dc1c ["INT_ADD", "register:40f0:8", ["const:51dc1c:8", "const:4:8"]]
- 0051dc1c ["CALLIND", null, ["register:0:8"]]
+ 0051dc5c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051dc5c ["INT_ADD", "register:40f0:8", ["const:51dc5c:8", "const:4:8"]]
+ 0051dc5c ["CALLIND", null, ["register:0:8"]]
- 0051dc1c bytes 20013fd6
+ 0051dc5c bytes 20013fd6
- 0051dc5c ["INT_ADD", "register:40f0:8", ["const:51dc5c:8", "const:4:8"]]
- 0051dc5c ["CALL", null, ["callee:00535bc0:8"]]
+ 0051dc9c ["INT_ADD", "register:40f0:8", ["const:51dc9c:8", "const:4:8"]]
+ 0051dc9c ["CALL", null, ["callee:00535bc0:8"]]
- 0051dc5c bytes c95f0094
+ 0051dc9c bytes c95f0094
- 0051dc94 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051dc94 ["INT_ADD", "register:40f0:8", ["const:51dc94:8", "const:4:8"]]
- 0051dc94 ["CALLIND", null, ["register:0:8"]]
+ 0051dcd4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051dcd4 ["INT_ADD", "register:40f0:8", ["const:51dcd4:8", "const:4:8"]]
+ 0051dcd4 ["CALLIND", null, ["register:0:8"]]
- 0051dc94 bytes 20013fd6
+ 0051dcd4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c710411fbcabd795a675e53d09e11e0"></a>

### [`0051ddec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051ddec.md) → [`0051de2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051de2c.md) _ZNK5Botan14Cert_Extension14CRL_ReasonCode11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58790.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58860.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051de4c",
      "incomplete_value": true,
      "site": "0051de74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051de0c",
      "incomplete_value": true,
      "site": "0051de34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:267:8"
              ]
            ]
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
      "0051de4c",
      "READ",
      [
        "storage",
        "002b8267",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051de4c",
      "READ",
      [
        "storage",
        "002b82a7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051de04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051ddec.md#insn-0051de04) · [`0051de3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051ddec.md#insn-0051de3c) · [`0051de4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051ddec.md#insn-0051de4c)
- 新版 [`0051de44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051de2c.md#insn-0051de44) · [`0051de7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051de2c.md#insn-0051de7c) · [`0051de8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051de2c.md#insn-0051de8c)

~~~diff
- 0051de04 ["COPY", "tmp:0:8", ["const:267:8"]]
- 0051de04 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0051de04 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0051de04 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0051de44 ["COPY", "tmp:0:8", ["const:2a7:8"]]
+ 0051de44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0051de44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0051de44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0051de04 bytes 4a9d0991
+ 0051de44 bytes 4a9d0a91
- 0051de3c ["INT_ADD", "register:40f0:8", ["const:51de3c:8", "const:4:8"]]
- 0051de3c ["CALL", null, ["callee:00c58860:8"]]
+ 0051de7c ["INT_ADD", "register:40f0:8", ["const:51de7c:8", "const:4:8"]]
+ 0051de7c ["CALL", null, ["callee:00c58860:8"]]
- 0051de3c bytes 55ea1c94
+ 0051de7c bytes 79ea1c94
- 0051de4c ["INT_ADD", "register:40f0:8", ["const:51de4c:8", "const:4:8"]]
- 0051de4c ["CALL", null, ["callee:004ff1e0:8"]]
+ 0051de8c ["INT_ADD", "register:40f0:8", ["const:51de8c:8", "const:4:8"]]
+ 0051de8c ["CALL", null, ["callee:004ff1e0:8"]]
- 0051de4c bytes d584ff97
+ 0051de8c bytes d584ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7d81bdaedfb9258e80686ad480e52ab"></a>

### [`0051ded0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051ded0.md) → [`0051df10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051df10.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points12encode_innerEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.58% / 新版 81.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051df54",
      "incomplete_value": true,
      "site": "0051df60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051df14",
      "incomplete_value": true,
      "site": "0051df20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:780:8"
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
      "definition_site": "0051df50",
      "incomplete_value": true,
      "site": "0051df64",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051df10",
      "incomplete_value": true,
      "site": "0051df24",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:54b:8"
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
      "definition_site": "0051df50",
      "incomplete_value": true,
      "site": "0051df64",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051df10",
      "incomplete_value": true,
      "site": "0051df24",
      "value": [
        "LOAD",
        "16",
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
      "0051df50",
      "READ",
      [
        "storage",
        "002ab54b",
        null,
        "string"
      ]
    ],
    [
      "0051df50",
      "READ",
      [
        "storage",
        "002ab55b",
        null,
        "string"
      ]
    ],
    [
      "0051df54",
      "READ",
      [
        "storage",
        "002c2780",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051df50",
      "READ",
      [
        "storage",
        "002ab4ef",
        null,
        "string"
      ]
    ],
    [
      "0051df50",
      "READ",
      [
        "storage",
        "002ab4ff",
        null,
        "string"
      ]
    ],
    [
      "0051df54",
      "READ",
      [
        "storage",
        "002c27c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051df60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051ded0.md#insn-0051df60) · [`0051def4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051ded0.md#insn-0051def4) · [`0051df00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051ded0.md#insn-0051df00)
- 新版 [`0051dfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051df10.md#insn-0051dfa0) · [`0051df34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051df10.md#insn-0051df34) · [`0051df40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051df10.md#insn-0051df40)

~~~diff
- 0051df60 ["INT_ADD", "register:40f0:8", ["const:51df60:8", "const:4:8"]]
- 0051df60 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0051dfa0 ["INT_ADD", "register:40f0:8", ["const:51dfa0:8", "const:4:8"]]
+ 0051dfa0 ["CALL", null, ["callee:00c57fe0:8"]]
- 0051df60 bytes ece71c94
+ 0051dfa0 bytes 10e81c94
- 0051def4 ["INT_ADD", "register:40f0:8", ["const:51def4:8", "const:4:8"]]
- 0051def4 ["CALL", null, ["callee:00c57fc0:8"]]
+ 0051df34 ["INT_ADD", "register:40f0:8", ["const:51df34:8", "const:4:8"]]
+ 0051df34 ["CALL", null, ["callee:00c57fc0:8"]]
- 0051def4 bytes ffe71c94
+ 0051df34 bytes 23e81c94
- 0051df00 ["INT_ADD", "register:40f0:8", ["const:51df00:8", "const:4:8"]]
- 0051df00 ["CALL", null, ["callee:00c57f60:8"]]
+ 0051df40 ["INT_ADD", "register:40f0:8", ["const:51df40:8", "const:4:8"]]
+ 0051df40 ["CALL", null, ["callee:00c57f60:8"]]
- 0051df00 bytes e4e71c94
+ 0051df40 bytes 08e81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a94b74e843517c31136e83c9507eeb7f"></a>

### [`0051dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dfb0.md) → [`0051dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dff0.md) _ZN5Botan14Cert_Extension23CRL_Distribution_Points12decode_innerERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051e2bc",
      "incomplete_value": true,
      "site": "0051e2c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e27c",
      "incomplete_value": true,
      "site": "0051e284",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0051e2cc",
      "incomplete_value": true,
      "site": "0051e2cc",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
      "definition_site": "0051e28c",
      "incomplete_value": true,
      "site": "0051e28c",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051e2cc",
      "incomplete_value": true,
      "site": "0051e2cc",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e28c",
      "incomplete_value": true,
      "site": "0051e28c",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
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
      "0051e06c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051e130",
      "PARAM",
      [
        "storage",
        "002bd76e",
        null,
        null
      ]
    ],
    [
      "0051e15c",
      "PARAM",
      [
        "storage",
        "002a0fc7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051e06c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051e130",
      "PARAM",
      [
        "storage",
        "002bd71a",
        null,
        null
      ]
    ],
    [
      "0051e15c",
      "PARAM",
      [
        "storage",
        "002a0f7a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051dffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dfb0.md#insn-0051dffc) · [`0051e03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dfb0.md#insn-0051e03c) · [`0051dfe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051d/0051dfb0.md#insn-0051dfe4)
- 新版 [`0051e03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dff0.md#insn-0051e03c) · [`0051e07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dff0.md#insn-0051e07c) · [`0051e024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051d/0051dff0.md#insn-0051e024)

~~~diff
- 0051dffc ["INT_ADD", "register:40f0:8", ["const:51dffc:8", "const:4:8"]]
- 0051dffc ["CALL", null, ["callee:00c58af0:8"]]
+ 0051e03c ["INT_ADD", "register:40f0:8", ["const:51e03c:8", "const:4:8"]]
+ 0051e03c ["CALL", null, ["callee:00c58af0:8"]]
- 0051dffc bytes 89ea1c94
+ 0051e03c bytes adea1c94
- 0051e03c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051e03c ["INT_ADD", "register:40f0:8", ["const:51e03c:8", "const:4:8"]]
- 0051e03c ["CALLIND", null, ["register:0:8"]]
+ 0051e07c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051e07c ["INT_ADD", "register:40f0:8", ["const:51e07c:8", "const:4:8"]]
+ 0051e07c ["CALLIND", null, ["register:0:8"]]
- 0051e03c bytes 20013fd6
+ 0051e07c bytes 20013fd6
- 0051dfe4 ["INT_ADD", "register:40f0:8", ["const:51dfe4:8", "const:4:8"]]
- 0051dfe4 ["CALL", null, ["callee:00c58950:8"]]
+ 0051e024 ["INT_ADD", "register:40f0:8", ["const:51e024:8", "const:4:8"]]
+ 0051e024 ["CALL", null, ["callee:00c58950:8"]]
- 0051dfe4 bytes 27ea1c94
+ 0051e024 bytes 4bea1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f13ab95d89b84e90320354c848174918"></a>

### [`0051e398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e398.md) → [`0051e3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e3d8.md) _ZN5Botan11BER_Decoder11decode_listINS_14Cert_Extension23CRL_Distribution_Points18Distribution_PointEEERS0_RNSt6__ndk16vectorIT_NS6_9allocat

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e60.md) · 呼出先 11件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053aaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053aaa4.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`0053ca88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053ca88.md) [`0053d56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d56c.md)
- 新版 呼出元 1件 [`00c59f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f30.md) · 呼出先 11件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053aae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aae4.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`0053cac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053cac8.md) [`0053d5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d5ac.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051e43c",
      "incomplete_value": true,
      "site": "0051e444",
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
      "definition_site": "0051e3fc",
      "incomplete_value": true,
      "site": "0051e404",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051e5f4",
      "incomplete_value": true,
      "site": "0051e5f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e5b4",
      "incomplete_value": true,
      "site": "0051e5b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051e42c",
      "READ",
      [
        "storage",
        "00c9b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "0051e430",
      "READ",
      [
        "storage",
        "00c9b0c8",
        null,
        "pointer"
      ]
    ],
    [
      "0051e444",
      "DATA",
      [
        "storage",
        "00c68e28",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0051e42c",
      "READ",
      [
        "storage",
        "00c9b2b8",
        null,
        "pointer"
      ]
    ],
    [
      "0051e430",
      "READ",
      [
        "storage",
        "00c9b198",
        null,
        "pointer"
      ]
    ],
    [
      "0051e444",
      "DATA",
      [
        "storage",
        "00c68ef8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051e574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e398.md#insn-0051e574) · [`0051e5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e398.md#insn-0051e5b4) · [`0051e3dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e398.md#insn-0051e3dc)
- 新版 [`0051e5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e3d8.md#insn-0051e5b4) · [`0051e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e3d8.md#insn-0051e5f4) · [`0051e41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e3d8.md#insn-0051e41c)

~~~diff
- 0051e574 ["INT_ADD", "register:40f0:8", ["const:51e574:8", "const:4:8"]]
- 0051e574 ["CALL", null, ["callee:00c587e0:8"]]
+ 0051e5b4 ["INT_ADD", "register:40f0:8", ["const:51e5b4:8", "const:4:8"]]
+ 0051e5b4 ["CALL", null, ["callee:00c587e0:8"]]
- 0051e574 bytes 67e81c94
+ 0051e5b4 bytes 8be81c94
- 0051e5b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051e5b4 ["INT_ADD", "register:40f0:8", ["const:51e5b4:8", "const:4:8"]]
- 0051e5b4 ["CALLIND", null, ["register:0:8"]]
+ 0051e5f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051e5f4 ["INT_ADD", "register:40f0:8", ["const:51e5f4:8", "const:4:8"]]
+ 0051e5f4 ["CALLIND", null, ["register:0:8"]]
- 0051e5b4 bytes 20013fd6
+ 0051e5f4 bytes 20013fd6
- 0051e3dc ["INT_ADD", "register:40f0:8", ["const:51e3dc:8", "const:4:8"]]
- 0051e3dc ["CALL", null, ["callee:00c587d0:8"]]
+ 0051e41c ["INT_ADD", "register:40f0:8", ["const:51e41c:8", "const:4:8"]]
+ 0051e41c ["CALL", null, ["callee:00c587d0:8"]]
- 0051e3dc bytes c9e81c94
+ 0051e41c bytes ede81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ebfd6129636678fcf1139428ba03f5f"></a>

### [`0051e674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e674.md) → [`0051e6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e6b4.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points11contents_toERNS_10Data_StoreES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "0051e6f4",
      "incomplete_value": true,
      "site": "0051e708",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:39e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e6b4",
      "incomplete_value": true,
      "site": "0051e6c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3f2:8"
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
      "0051e6f4",
      "READ",
      [
        "storage",
        "002ba3f2",
        null,
        "string"
      ]
    ],
    [
      "0051e6f8",
      "READ",
      [
        "storage",
        "002ba3ff",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051e6f4",
      "READ",
      [
        "storage",
        "002ba39e",
        null,
        "string"
      ]
    ],
    [
      "0051e6f8",
      "READ",
      [
        "storage",
        "002ba3ab",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051e6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e674.md#insn-0051e6ac) · [`0051e6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e674.md#insn-0051e6fc) · [`0051e70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e674.md#insn-0051e70c)
- 新版 [`0051e6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e6b4.md#insn-0051e6ec) · [`0051e73c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e6b4.md#insn-0051e73c) · [`0051e74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e6b4.md#insn-0051e74c)

~~~diff
- 0051e6ac ["COPY", "tmp:0:8", ["const:3f2:8"]]
- 0051e6ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0051e6ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0051e6ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0051e6ec ["COPY", "tmp:0:8", ["const:39e:8"]]
+ 0051e6ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0051e6ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0051e6ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0051e6ac bytes 08c90f91
+ 0051e6ec bytes 08790e91
- 0051e6fc ["INT_ADD", "register:40f0:8", ["const:51e6fc:8", "const:4:8"]]
- 0051e6fc ["CALL", null, ["callee:004ff1e0:8"]]
+ 0051e73c ["INT_ADD", "register:40f0:8", ["const:51e73c:8", "const:4:8"]]
+ 0051e73c ["CALL", null, ["callee:004ff1e0:8"]]
- 0051e6fc bytes a982ff97
+ 0051e73c bytes a982ff97
- 0051e70c ["INT_ADD", "register:40f0:8", ["const:51e70c:8", "const:4:8"]]
- 0051e70c ["CALL", null, ["callee:00c57f80:8"]]
+ 0051e74c ["INT_ADD", "register:40f0:8", ["const:51e74c:8", "const:4:8"]]
+ 0051e74c ["CALL", null, ["callee:00c57f80:8"]]
- 0051e70c bytes e9e51c94
+ 0051e74c bytes 0de61c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca06b1e43a2a14e7982c3a88729f1aef"></a>

### [`0051e770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e770.md) → [`0051e7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e7b0.md) _ZNK5Botan14Cert_Extension23CRL_Distribution_Points18Distribution_Point11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 81.58% / 新版 81.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051e7f4",
      "incomplete_value": true,
      "site": "0051e800",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e7b4",
      "incomplete_value": true,
      "site": "0051e7c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:780:8"
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
      "definition_site": "0051e7f0",
      "incomplete_value": true,
      "site": "0051e804",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4ef:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e7b0",
      "incomplete_value": true,
      "site": "0051e7c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:54b:8"
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
      "definition_site": "0051e7f0",
      "incomplete_value": true,
      "site": "0051e804",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051e7b0",
      "incomplete_value": true,
      "site": "0051e7c4",
      "value": [
        "LOAD",
        "16",
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
      "0051e7f0",
      "READ",
      [
        "storage",
        "002ab54b",
        null,
        "string"
      ]
    ],
    [
      "0051e7f0",
      "READ",
      [
        "storage",
        "002ab55b",
        null,
        "string"
      ]
    ],
    [
      "0051e7f4",
      "READ",
      [
        "storage",
        "002c2780",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051e7f0",
      "READ",
      [
        "storage",
        "002ab4ef",
        null,
        "string"
      ]
    ],
    [
      "0051e7f0",
      "READ",
      [
        "storage",
        "002ab4ff",
        null,
        "string"
      ]
    ],
    [
      "0051e7f4",
      "READ",
      [
        "storage",
        "002c27c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051e800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e770.md#insn-0051e800) · [`0051e794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e770.md#insn-0051e794) · [`0051e7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e770.md#insn-0051e7a0)
- 新版 [`0051e840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e7b0.md#insn-0051e840) · [`0051e7d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e7b0.md#insn-0051e7d4) · [`0051e7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e7b0.md#insn-0051e7e0)

~~~diff
- 0051e800 ["INT_ADD", "register:40f0:8", ["const:51e800:8", "const:4:8"]]
- 0051e800 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0051e840 ["INT_ADD", "register:40f0:8", ["const:51e840:8", "const:4:8"]]
+ 0051e840 ["CALL", null, ["callee:00c57fe0:8"]]
- 0051e800 bytes c4e51c94
+ 0051e840 bytes e8e51c94
- 0051e794 ["INT_ADD", "register:40f0:8", ["const:51e794:8", "const:4:8"]]
- 0051e794 ["CALL", null, ["callee:00c57fc0:8"]]
+ 0051e7d4 ["INT_ADD", "register:40f0:8", ["const:51e7d4:8", "const:4:8"]]
+ 0051e7d4 ["CALL", null, ["callee:00c57fc0:8"]]
- 0051e794 bytes d7e51c94
+ 0051e7d4 bytes fbe51c94
- 0051e7a0 ["INT_ADD", "register:40f0:8", ["const:51e7a0:8", "const:4:8"]]
- 0051e7a0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0051e7e0 ["INT_ADD", "register:40f0:8", ["const:51e7e0:8", "const:4:8"]]
+ 0051e7e0 ["CALL", null, ["callee:00c57f60:8"]]
- 0051e7a0 bytes bce51c94
+ 0051e7e0 bytes e0e51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08232ad46a8aaf1e849edcf2207cbeb9"></a>

### [`0051e850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e850.md) → [`0051e890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e890.md) _ZN5Botan14Cert_Extension23CRL_Distribution_Points18Distribution_Point11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051e9ac",
      "incomplete_value": true,
      "site": "0051e9ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e96c",
      "incomplete_value": true,
      "site": "0051e96c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051e9f0",
      "incomplete_value": true,
      "site": "0051e9f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051e9b0",
      "incomplete_value": true,
      "site": "0051e9b0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
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
      "0051e99c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051e9e0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051e99c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051e9e0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051e92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e850.md#insn-0051e92c) · [`0051e96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e850.md#insn-0051e96c) · [`0051e9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051e850.md#insn-0051e9b0)
- 新版 [`0051e96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e890.md#insn-0051e96c) · [`0051e9ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e890.md#insn-0051e9ac) · [`0051e9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051e890.md#insn-0051e9f0)

~~~diff
- 0051e92c ["INT_ADD", "register:40f0:8", ["const:51e92c:8", "const:4:8"]]
- 0051e92c ["CALL", null, ["callee:00c57f80:8"]]
+ 0051e96c ["INT_ADD", "register:40f0:8", ["const:51e96c:8", "const:4:8"]]
+ 0051e96c ["CALL", null, ["callee:00c57f80:8"]]
- 0051e92c bytes 61e51c94
+ 0051e96c bytes 85e51c94
- 0051e96c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051e96c ["INT_ADD", "register:40f0:8", ["const:51e96c:8", "const:4:8"]]
- 0051e96c ["CALLIND", null, ["register:0:8"]]
+ 0051e9ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051e9ac ["INT_ADD", "register:40f0:8", ["const:51e9ac:8", "const:4:8"]]
+ 0051e9ac ["CALLIND", null, ["register:0:8"]]
- 0051e96c bytes 20013fd6
+ 0051e9ac bytes 20013fd6
- 0051e9b0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051e9b0 ["INT_ADD", "register:40f0:8", ["const:51e9b0:8", "const:4:8"]]
- 0051e9b0 ["CALLIND", null, ["register:0:8"]]
+ 0051e9f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051e9f0 ["INT_ADD", "register:40f0:8", ["const:51e9f0:8", "const:4:8"]]
+ 0051e9f0 ["CALLIND", null, ["register:0:8"]]
- 0051e9b0 bytes 20013fd6
+ 0051e9f0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5a342d611263e9f823bd96df49df011"></a>

### [`0051ec0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051ec0c.md) → [`0051ec4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ec4c.md) FUN_0051ec4c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051ec90",
      "incomplete_value": true,
      "site": "0051eca0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0051ec50",
      "incomplete_value": true,
      "site": "0051ec60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:360:8"
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
      "definition_site": "0051ec8c",
      "incomplete_value": true,
      "site": "0051eca4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:c3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051ec4c",
      "incomplete_value": true,
      "site": "0051ec64",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:c0c:8"
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
      "definition_site": "0051ec8c",
      "incomplete_value": true,
      "site": "0051eca4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051ec4c",
      "incomplete_value": true,
      "site": "0051ec64",
      "value": [
        "LOAD",
        "16",
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
      "0051ec8c",
      "READ",
      [
        "storage",
        "002b2c0c",
        null,
        "string"
      ]
    ],
    [
      "0051ec8c",
      "READ",
      [
        "storage",
        "002b2c1c",
        null,
        "string"
      ]
    ],
    [
      "0051ec90",
      "READ",
      [
        "storage",
        "002c2360",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0051ec8c",
      "READ",
      [
        "storage",
        "002b2c3d",
        null,
        "string"
      ]
    ],
    [
      "0051ec8c",
      "READ",
      [
        "storage",
        "002b2c4d",
        null,
        "string"
      ]
    ],
    [
      "0051ec90",
      "READ",
      [
        "storage",
        "002c23a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051eca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051ec0c.md#insn-0051eca4) · [`0051ec30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051ec0c.md#insn-0051ec30) · [`0051ec3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051ec0c.md#insn-0051ec3c)
- 新版 [`0051ece4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ec4c.md#insn-0051ece4) · [`0051ec70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ec4c.md#insn-0051ec70) · [`0051ec7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ec4c.md#insn-0051ec7c)

~~~diff
- 0051eca4 ["INT_ADD", "register:40f0:8", ["const:51eca4:8", "const:4:8"]]
- 0051eca4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0051ece4 ["INT_ADD", "register:40f0:8", ["const:51ece4:8", "const:4:8"]]
+ 0051ece4 ["CALL", null, ["callee:00c57fe0:8"]]
- 0051eca4 bytes 9be41c94
+ 0051ece4 bytes bfe41c94
- 0051ec30 ["INT_ADD", "register:40f0:8", ["const:51ec30:8", "const:4:8"]]
- 0051ec30 ["CALL", null, ["callee:00c57fc0:8"]]
+ 0051ec70 ["INT_ADD", "register:40f0:8", ["const:51ec70:8", "const:4:8"]]
+ 0051ec70 ["CALL", null, ["callee:00c57fc0:8"]]
- 0051ec30 bytes b0e41c94
+ 0051ec70 bytes d4e41c94
- 0051ec3c ["INT_ADD", "register:40f0:8", ["const:51ec3c:8", "const:4:8"]]
- 0051ec3c ["CALL", null, ["callee:00c57f60:8"]]
+ 0051ec7c ["INT_ADD", "register:40f0:8", ["const:51ec7c:8", "const:4:8"]]
+ 0051ec7c ["CALL", null, ["callee:00c57f60:8"]]
- 0051ec3c bytes 95e41c94
+ 0051ec7c bytes b9e41c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cb335af87928376f26e7712a9a0a0dd"></a>

### [`0051edcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051edcc.md) → [`0051ee0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ee0c.md) FUN_0051ee0c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`004ff1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff1a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`004ff1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff1e0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051ef28",
      "incomplete_value": true,
      "site": "0051ef3c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
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
      "definition_site": "0051eee8",
      "incomplete_value": true,
      "site": "0051eefc",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c3000:8"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051ef24",
      "incomplete_value": true,
      "site": "0051ef40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c54:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051eee4",
      "incomplete_value": true,
      "site": "0051ef00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ca8:8"
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
      "definition_site": "0051ef24",
      "incomplete_value": true,
      "site": "0051ef40",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0051eee4",
      "incomplete_value": true,
      "site": "0051ef00",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051eea8",
      "PARAM",
      [
        "storage",
        "002bd76e",
        null,
        null
      ]
    ],
    [
      "0051eed4",
      "PARAM",
      [
        "storage",
        "002a0fc7",
        null,
        null
      ]
    ],
    [
      "0051ef24",
      "READ",
      [
        "storage",
        "002beca8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0051eea8",
      "PARAM",
      [
        "storage",
        "002bd71a",
        null,
        null
      ]
    ],
    [
      "0051eed4",
      "PARAM",
      [
        "storage",
        "002a0f7a",
        null,
        null
      ]
    ],
    [
      "0051ef24",
      "READ",
      [
        "storage",
        "002bec54",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051ef20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051edcc.md#insn-0051ef20) · [`0051ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051edcc.md#insn-0051ef40) · [`0051ee04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051e/0051edcc.md#insn-0051ee04)
- 新版 [`0051ef60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ee0c.md#insn-0051ef60) · [`0051ef80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ee0c.md#insn-0051ef80) · [`0051ee44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051e/0051ee0c.md#insn-0051ee44)

~~~diff
- 0051ef20 ["INT_ADD", "register:40f0:8", ["const:51ef20:8", "const:4:8"]]
- 0051ef20 ["CALL", null, ["callee:004ff1e0:8"]]
+ 0051ef60 ["INT_ADD", "register:40f0:8", ["const:51ef60:8", "const:4:8"]]
+ 0051ef60 ["CALL", null, ["callee:004ff1e0:8"]]
- 0051ef20 bytes a080ff97
+ 0051ef60 bytes a080ff97
- 0051ef40 ["INT_ADD", "register:40f0:8", ["const:51ef40:8", "const:4:8"]]
- 0051ef40 ["CALL", null, ["callee:00c57f80:8"]]
+ 0051ef80 ["INT_ADD", "register:40f0:8", ["const:51ef80:8", "const:4:8"]]
+ 0051ef80 ["CALL", null, ["callee:00c57f80:8"]]
- 0051ef40 bytes dce31c94
+ 0051ef80 bytes 00e41c94
- 0051ee04 ["INT_ADD", "register:40f0:8", ["const:51ee04:8", "const:4:8"]]
- 0051ee04 ["CALL", null, ["callee:00c59a40:8"]]
+ 0051ee44 ["INT_ADD", "register:40f0:8", ["const:51ee44:8", "const:4:8"]]
+ 0051ee44 ["CALL", null, ["callee:00c59a40:8"]]
- 0051ee04 bytes dbea1c94
+ 0051ee44 bytes ffea1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b812877fa8ed045eac33bbba66f3c961"></a>

### [`0051f1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f1f4.md) → [`0051f234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f234.md) _ZN5Botan11X509_Object11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`004a5980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58710.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004a59c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587d0.md) [`00c587e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587e0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051f304",
      "incomplete_value": true,
      "site": "0051f304",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051f2c4",
      "incomplete_value": true,
      "site": "0051f2c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051f348",
      "incomplete_value": true,
      "site": "0051f348",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051f308",
      "incomplete_value": true,
      "site": "0051f308",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051f2f4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051f338",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0051f2f4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051f338",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051f284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f1f4.md#insn-0051f284) · [`0051f2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f1f4.md#insn-0051f2c4) · [`0051f308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f1f4.md#insn-0051f308)
- 新版 [`0051f2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f234.md#insn-0051f2c4) · [`0051f304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f234.md#insn-0051f304) · [`0051f348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f234.md#insn-0051f348)

~~~diff
- 0051f284 ["INT_ADD", "register:40f0:8", ["const:51f284:8", "const:4:8"]]
- 0051f284 ["CALL", null, ["callee:00c587e0:8"]]
+ 0051f2c4 ["INT_ADD", "register:40f0:8", ["const:51f2c4:8", "const:4:8"]]
+ 0051f2c4 ["CALL", null, ["callee:00c587e0:8"]]
- 0051f284 bytes 23e51c94
+ 0051f2c4 bytes 47e51c94
- 0051f2c4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051f2c4 ["INT_ADD", "register:40f0:8", ["const:51f2c4:8", "const:4:8"]]
- 0051f2c4 ["CALLIND", null, ["register:0:8"]]
+ 0051f304 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051f304 ["INT_ADD", "register:40f0:8", ["const:51f304:8", "const:4:8"]]
+ 0051f304 ["CALLIND", null, ["register:0:8"]]
- 0051f2c4 bytes 20013fd6
+ 0051f304 bytes 20013fd6
- 0051f308 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051f308 ["INT_ADD", "register:40f0:8", ["const:51f308:8", "const:4:8"]]
- 0051f308 ["CALLIND", null, ["register:0:8"]]
+ 0051f348 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051f348 ["INT_ADD", "register:40f0:8", ["const:51f348:8", "const:4:8"]]
+ 0051f348 ["CALLIND", null, ["register:0:8"]]
- 0051f308 bytes 20013fd6
+ 0051f348 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71edacb095a8b89bc10dd824fdae9643"></a>

### [`0051f584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f584.md) → [`0051f5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f5c4.md) _ZNK5Botan11X509_Object23hash_used_for_signatureEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59e90.md) · 呼出先 16件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0051fa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051fa10.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md) [`00547b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b70.md)
- 新版 呼出元 1件 [`00c59f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f60.md) · 呼出先 16件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0051fa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fa50.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00547bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bac.md) [`00547bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0051f600",
      "incomplete_value": false,
      "site": "0051f608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051f5c0",
      "incomplete_value": false,
      "site": "0051f5c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "definition_site": "0051f864",
      "incomplete_value": false,
      "site": "0051f870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:c65:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051f824",
      "incomplete_value": false,
      "site": "0051f830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:c34:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0051f8b8",
      "incomplete_value": true,
      "site": "0051f8c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051f878",
      "incomplete_value": true,
      "site": "0051f884",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
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
      "0051f608",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0051f64c",
      "READ",
      [
        "storage",
        "00c6a6d0",
        null,
        "pointer"
      ]
    ],
    [
      "0051f64c",
      "READ",
      [
        "storage",
        "00c6a6d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0051f608",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ],
    [
      "0051f64c",
      "READ",
      [
        "storage",
        "00c6a7a0",
        null,
        "pointer"
      ]
    ],
    [
      "0051f64c",
      "READ",
      [
        "storage",
        "00c6a7a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051f7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f584.md#insn-0051f7f0) · [`0051f830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f584.md#insn-0051f830) · [`0051f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f584.md#insn-0051f884)
- 新版 [`0051f830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f5c4.md#insn-0051f830) · [`0051f870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f5c4.md#insn-0051f870) · [`0051f8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f5c4.md#insn-0051f8c4)

~~~diff
- 0051f7f0 ["INT_ADD", "register:40f0:8", ["const:51f7f0:8", "const:4:8"]]
- 0051f7f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0051f830 ["INT_ADD", "register:40f0:8", ["const:51f830:8", "const:4:8"]]
+ 0051f830 ["CALL", null, ["callee:00c57f80:8"]]
- 0051f7f0 bytes b0e11c94
+ 0051f830 bytes d4e11c94
- 0051f830 ["INT_ADD", "register:40f0:8", ["const:51f830:8", "const:4:8"]]
- 0051f830 ["CALL", null, ["callee:00c58030:8"]]
+ 0051f870 ["INT_ADD", "register:40f0:8", ["const:51f870:8", "const:4:8"]]
+ 0051f870 ["CALL", null, ["callee:00c58030:8"]]
- 0051f830 bytes cce11c94
+ 0051f870 bytes f0e11c94
- 0051f884 ["INT_ADD", "register:40f0:8", ["const:51f884:8", "const:4:8"]]
- 0051f884 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0051f8c4 ["INT_ADD", "register:40f0:8", ["const:51f8c4:8", "const:4:8"]]
+ 0051f8c4 ["CALL", null, ["callee:00c57fe0:8"]]
- 0051f884 bytes a3e11c94
+ 0051f8c4 bytes c7e11c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02361d5052b0b1e56753b430181bf865"></a>

### [`0051fa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051fa10.md) → [`0051fa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fa50.md) FUN_0051fa50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0051f584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051f584.md) [`00520050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520050.md) · 呼出先 15件 [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`0051f5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051f5c4.md) [`00520090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520090.md) · 呼出先 15件 [`004a57bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a57bc.md) [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.01% / 新版 96.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0051fa90",
      "incomplete_value": true,
      "site": "0051fa90",
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
      "definition_site": "0051fa50",
      "incomplete_value": true,
      "site": "0051fa50",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051fd38",
      "incomplete_value": true,
      "site": "0051fd38",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051fcf8",
      "incomplete_value": true,
      "site": "0051fcf8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0051fdbc",
      "incomplete_value": true,
      "site": "0051fdbc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051fd7c",
      "incomplete_value": true,
      "site": "0051fd7c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0051fa78",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0051fa90",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051fabc",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0051fa78",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0051fa90",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051fabc",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051fa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051fa10.md#insn-0051fa90) · [`0051fcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051fa10.md#insn-0051fcf8) · [`0051fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051fa10.md#insn-0051fd7c)
- 新版 [`0051fad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fa50.md#insn-0051fad0) · [`0051fd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fa50.md#insn-0051fd38) · [`0051fdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fa50.md#insn-0051fdbc)

~~~diff
- 0051fa90 ["INT_ADD", "register:40f0:8", ["const:51fa90:8", "const:4:8"]]
- 0051fa90 ["CALL", null, ["callee:00c58760:8"]]
+ 0051fad0 ["INT_ADD", "register:40f0:8", ["const:51fad0:8", "const:4:8"]]
+ 0051fad0 ["CALL", null, ["callee:00c58760:8"]]
- 0051fa90 bytes 00e31c94
+ 0051fad0 bytes 24e31c94
- 0051fcf8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051fcf8 ["INT_ADD", "register:40f0:8", ["const:51fcf8:8", "const:4:8"]]
- 0051fcf8 ["CALLIND", null, ["register:0:8"]]
+ 0051fd38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051fd38 ["INT_ADD", "register:40f0:8", ["const:51fd38:8", "const:4:8"]]
+ 0051fd38 ["CALLIND", null, ["register:0:8"]]
- 0051fcf8 bytes 20013fd6
+ 0051fd38 bytes 20013fd6
- 0051fd7c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051fd7c ["INT_ADD", "register:40f0:8", ["const:51fd7c:8", "const:4:8"]]
- 0051fd7c ["CALLIND", null, ["register:0:8"]]
+ 0051fdbc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051fdbc ["INT_ADD", "register:40f0:8", ["const:51fdbc:8", "const:4:8"]]
+ 0051fdbc ["CALLIND", null, ["register:0:8"]]
- 0051fd7c bytes 20013fd6
+ 0051fdbc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-395bbe87d497e3583ce701f1e8661875"></a>

### [`00520050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520050.md) → [`00520090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520090.md) _ZNK5Botan11X509_Object16verify_signatureERKNS_10Public_KeyE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cb0.md) · 呼出先 19件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004a6c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6c1c.md) [`004acc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acc24.md) [`0051fa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051f/0051fa10.md) [`00547b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b14.md)
- 新版 呼出元 1件 [`00c59d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d80.md) · 呼出先 19件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004a6c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6c5c.md) [`004acc64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acc64.md) [`0051fa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051f/0051fa50.md) [`00547b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547b54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005200d8",
      "incomplete_value": false,
      "site": "005200d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00520098",
      "incomplete_value": false,
      "site": "00520098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "definition_site": "0052046c",
      "incomplete_value": false,
      "site": "00520474",
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
            "const:b43:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052042c",
      "incomplete_value": false,
      "site": "00520434",
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
            "const:b9f:8"
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
      "definition_site": "00520480",
      "incomplete_value": false,
      "site": "00520488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:295:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00520440",
      "incomplete_value": false,
      "site": "00520448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:2e9:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005200d8",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0052011c",
      "READ",
      [
        "storage",
        "00c6a6d0",
        null,
        "pointer"
      ]
    ],
    [
      "0052011c",
      "READ",
      [
        "storage",
        "00c6a6d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005200d8",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ],
    [
      "0052011c",
      "READ",
      [
        "storage",
        "00c6a7a0",
        null,
        "pointer"
      ]
    ],
    [
      "0052011c",
      "READ",
      [
        "storage",
        "00c6a7a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520050.md#insn-00520434) · [`00520448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520050.md#insn-00520448) · [`00520504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520050.md#insn-00520504)
- 新版 [`00520474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520090.md#insn-00520474) · [`00520488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520090.md#insn-00520488) · [`00520544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520090.md#insn-00520544)

~~~diff
- 00520434 ["INT_ADD", "register:40f0:8", ["const:520434:8", "const:4:8"]]
- 00520434 ["CALL", null, ["callee:004acc64:8"]]
+ 00520474 ["INT_ADD", "register:40f0:8", ["const:520474:8", "const:4:8"]]
+ 00520474 ["CALL", null, ["callee:004acc64:8"]]
- 00520434 bytes fc31fe97
+ 00520474 bytes fc31fe97
- 00520448 ["INT_ADD", "register:40f0:8", ["const:520448:8", "const:4:8"]]
- 00520448 ["CALL", null, ["callee:004acc64:8"]]
+ 00520488 ["INT_ADD", "register:40f0:8", ["const:520488:8", "const:4:8"]]
+ 00520488 ["CALL", null, ["callee:004acc64:8"]]
- 00520448 bytes f731fe97
+ 00520488 bytes f731fe97
- 00520504 ["INT_ADD", "register:40f0:8", ["const:520504:8", "const:4:8"]]
- 00520504 ["CALL", null, ["callee:00c58180:8"]]
+ 00520544 ["INT_ADD", "register:40f0:8", ["const:520544:8", "const:4:8"]]
+ 00520544 ["CALL", null, ["callee:00c58180:8"]]
- 00520504 bytes ebde1c94
+ 00520544 bytes 0fdf1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-768f013a21944dcdc049d447f5a3eed7"></a>

### [`005209e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/005209e4.md) → [`00520a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520a24.md) _ZNK5Botan16X509_Certificate9PEM_labelEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520a48",
      "incomplete_value": true,
      "site": "00520a48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00520a08",
      "incomplete_value": true,
      "site": "00520a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:408:8"
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
      "00520a38",
      "READ",
      [
        "storage",
        "002ba408",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00520a38",
      "READ",
      [
        "storage",
        "002ba3b4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005209ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/005209e4.md#insn-005209ec)
- 新版 [`00520a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520a24.md#insn-00520a2c)

~~~diff
- 005209ec ["COPY", "tmp:0:8", ["const:408:8"]]
- 005209ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005209ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005209ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00520a2c ["COPY", "tmp:0:8", ["const:3b4:8"]]
+ 00520a2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00520a2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00520a2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005209ec bytes 4a211091
+ 00520a2c bytes 4ad10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7f8d0bb924f4e2fd27028c4cb1db751"></a>

### [`00520a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520a10.md) → [`00520a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520a50.md) _ZNK5Botan16X509_Certificate20alternate_PEM_labelsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520a74",
      "incomplete_value": true,
      "site": "00520a84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00520a34",
      "incomplete_value": true,
      "site": "00520a44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d67:8"
              ]
            ]
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
      "00520a74",
      "READ",
      [
        "storage",
        "002b1d67",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00520a74",
      "READ",
      [
        "storage",
        "002b1d98",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520a10.md#insn-00520a28) · [`00520a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520a10.md#insn-00520a54) · [`00520a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520a10.md#insn-00520a64)
- 新版 [`00520a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520a50.md#insn-00520a68) · [`00520a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520a50.md#insn-00520a94) · [`00520aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520a50.md#insn-00520aa4)

~~~diff
- 00520a28 ["COPY", "tmp:0:8", ["const:d67:8"]]
- 00520a28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00520a28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00520a28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00520a68 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00520a68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00520a68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00520a68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00520a28 bytes 299d3591
+ 00520a68 bytes 29613691
- 00520a54 ["INT_ADD", "register:40f0:8", ["const:520a54:8", "const:4:8"]]
- 00520a54 ["CALL", null, ["callee:00473580:8"]]
+ 00520a94 ["INT_ADD", "register:40f0:8", ["const:520a94:8", "const:4:8"]]
+ 00520a94 ["CALL", null, ["callee:00473580:8"]]
- 00520a54 bytes bb4afd97
+ 00520a94 bytes bb4afd97
- 00520a64 ["INT_ADD", "register:40f0:8", ["const:520a64:8", "const:4:8"]]
- 00520a64 ["CALL", null, ["callee:00c57f80:8"]]
+ 00520aa4 ["INT_ADD", "register:40f0:8", ["const:520aa4:8", "const:4:8"]]
+ 00520aa4 ["CALL", null, ["callee:00c57f80:8"]]
- 00520a64 bytes 13dd1c94
+ 00520aa4 bytes 37dd1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec75ad57d7920106027a49810699f2a5"></a>

### [`00520ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520ab8.md) → [`00520af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520af8.md) _ZN5Botan16X509_CertificateC1ERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) [`00c59c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520b38",
      "incomplete_value": true,
      "site": "00520b38",
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
      "definition_site": "00520af8",
      "incomplete_value": true,
      "site": "00520af8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520b38",
      "incomplete_value": true,
      "site": "00520b38",
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
      "definition_site": "00520af8",
      "incomplete_value": true,
      "site": "00520af8",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00520b78",
      "incomplete_value": true,
      "site": "00520b80",
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
      "definition_site": "00520b38",
      "incomplete_value": true,
      "site": "00520b40",
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
      "00520b18",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00520b20",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00520b38",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00520b18",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00520b20",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00520b38",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520ab8.md#insn-00520ad8) · [`00520ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520ab8.md#insn-00520ae0) · [`00520b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520ab8.md#insn-00520b04)
- 新版 [`00520b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520af8.md#insn-00520b18) · [`00520b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520af8.md#insn-00520b20) · [`00520b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520af8.md#insn-00520b44)

~~~diff
- 00520ad8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 00520ad8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00520b18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 00520b18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00520ad8 bytes 08ad40f9
+ 00520b18 bytes 081541f9
- 00520ae0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
- 00520ae0 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00520b20 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e08:8"]]
+ 00520b20 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00520ae0 bytes 4a9d46f9
+ 00520b20 bytes 4a0547f9
- 00520b04 ["INT_ADD", "register:40f0:8", ["const:520b04:8", "const:4:8"]]
- 00520b04 ["CALL", null, ["callee:00c58760:8"]]
+ 00520b44 ["INT_ADD", "register:40f0:8", ["const:520b44:8", "const:4:8"]]
+ 00520b44 ["CALL", null, ["callee:00c58760:8"]]
- 00520b04 bytes e3de1c94
+ 00520b44 bytes 07df1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7c4d333f0268dfa2a871d691deaa85a"></a>

### [`00520c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520c0c.md) → [`00520c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520c4c.md) _ZN5Botan16X509_CertificateC1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59bc0.md) · 呼出先 7件 [`005403c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00c59c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c90.md) · 呼出先 7件 [`00540408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520c8c",
      "incomplete_value": true,
      "site": "00520c8c",
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
      "definition_site": "00520c4c",
      "incomplete_value": true,
      "site": "00520c4c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520c8c",
      "incomplete_value": true,
      "site": "00520c8c",
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
      "definition_site": "00520c4c",
      "incomplete_value": true,
      "site": "00520c4c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00520cd4",
      "incomplete_value": true,
      "site": "00520ce0",
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
      "definition_site": "00520c94",
      "incomplete_value": true,
      "site": "00520ca0",
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
      "00520c6c",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00520c74",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00520c8c",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00520c6c",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00520c74",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00520c8c",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520c0c.md#insn-00520cf8) · [`00520c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520c0c.md#insn-00520c2c) · [`00520c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520c0c.md#insn-00520c34)
- 新版 [`00520d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520c4c.md#insn-00520d38) · [`00520c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520c4c.md#insn-00520c6c) · [`00520c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520c4c.md#insn-00520c74)

~~~diff
- 00520cf8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00520cf8 ["INT_ADD", "register:40f0:8", ["const:520cf8:8", "const:4:8"]]
- 00520cf8 ["CALLIND", null, ["register:0:8"]]
+ 00520d38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00520d38 ["INT_ADD", "register:40f0:8", ["const:520d38:8", "const:4:8"]]
+ 00520d38 ["CALLIND", null, ["register:0:8"]]
- 00520cf8 bytes 20013fd6
+ 00520d38 bytes 20013fd6
- 00520c2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 00520c2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00520c6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 00520c6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00520c2c bytes 08ad40f9
+ 00520c6c bytes 081541f9
- 00520c34 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
- 00520c34 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00520c74 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e08:8"]]
+ 00520c74 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00520c34 bytes 4a9d46f9
+ 00520c74 bytes 4a0547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c04653b1090834d8b28937f91929f7cf"></a>

### [`00520d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520d84.md) → [`00520dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520dc4.md) _ZN5Botan16X509_CertificateC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a60.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) [`00c59660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59660.md) [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md)
- 新版 呼出元 1件 [`00c59b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b30.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59730.md) [`00c59740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59740.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520e04",
      "incomplete_value": true,
      "site": "00520e04",
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
      "definition_site": "00520dc4",
      "incomplete_value": true,
      "site": "00520dc4",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00520e04",
      "incomplete_value": true,
      "site": "00520e04",
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
      "definition_site": "00520dc4",
      "incomplete_value": true,
      "site": "00520dc4",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00520e44",
      "incomplete_value": true,
      "site": "00520e4c",
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
      "definition_site": "00520e04",
      "incomplete_value": true,
      "site": "00520e0c",
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
      "00520de4",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00520dec",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00520e04",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00520de4",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00520dec",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00520e04",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520d84.md#insn-00520da4) · [`00520dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520d84.md#insn-00520dac) · [`00520dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520d84.md#insn-00520dd0)
- 新版 [`00520de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520dc4.md#insn-00520de4) · [`00520dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520dc4.md#insn-00520dec) · [`00520e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520dc4.md#insn-00520e10)

~~~diff
- 00520da4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 00520da4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00520de4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 00520de4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00520da4 bytes 08ad40f9
+ 00520de4 bytes 081541f9
- 00520dac ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
- 00520dac ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00520dec ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e08:8"]]
+ 00520dec ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00520dac bytes 4a9d46f9
+ 00520dec bytes 4a0547f9
- 00520dd0 ["INT_ADD", "register:40f0:8", ["const:520dd0:8", "const:4:8"]]
- 00520dd0 ["CALL", null, ["callee:00c58760:8"]]
+ 00520e10 ["INT_ADD", "register:40f0:8", ["const:520e10:8", "const:4:8"]]
+ 00520e10 ["CALL", null, ["callee:00c58760:8"]]
- 00520dd0 bytes 30de1c94
+ 00520e10 bytes 54de1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7d69dd23535293f5284c2bb07ad0e62"></a>

### [`00520eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md) → [`00520ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md) _ZN5Botan16X509_Certificate12force_decodeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 68件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md)
- 新版 呼出元 0件  · 呼出先 68件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`004a57bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a57bc.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `call_target` 8件, `store_value` 14件

アドレスに依存する影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00521194",
      "incomplete_value": true,
      "site": "00521198",
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
      "definition_site": "00521154",
      "incomplete_value": true,
      "site": "00521158",
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
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00521260",
      "incomplete_value": false,
      "site": "00521260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00521220",
      "incomplete_value": false,
      "site": "00521220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005216a8",
      "incomplete_value": true,
      "site": "005216a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:781:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00521668",
      "incomplete_value": true,
      "site": "00521668",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:7dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 71,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00521068",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052118c",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00521198",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00521068",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052118c",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00521198",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md#insn-00520ff8) · [`00521038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md#insn-00521038) · [`005211bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00520/00520eb0.md#insn-005211bc)
- 新版 [`00521038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md#insn-00521038) · [`00521078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md#insn-00521078) · [`005211fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00520/00520ef0.md#insn-005211fc)

~~~diff
- 00520ff8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00520ff8 ["INT_ADD", "register:40f0:8", ["const:520ff8:8", "const:4:8"]]
- 00520ff8 ["CALLIND", null, ["register:0:8"]]
+ 00521038 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00521038 ["INT_ADD", "register:40f0:8", ["const:521038:8", "const:4:8"]]
+ 00521038 ["CALLIND", null, ["register:0:8"]]
- 00520ff8 bytes 00013fd6
+ 00521038 bytes 00013fd6
- 00521038 ["COPY", "register:0:8", ["register:4048:8"]]
- 00521038 ["INT_ADD", "register:40f0:8", ["const:521038:8", "const:4:8"]]
- 00521038 ["CALLIND", null, ["register:0:8"]]
+ 00521078 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00521078 ["INT_ADD", "register:40f0:8", ["const:521078:8", "const:4:8"]]
+ 00521078 ["CALLIND", null, ["register:0:8"]]
- 00521038 bytes 20013fd6
+ 00521078 bytes 20013fd6
- 005211bc ["COPY", "register:0:8", ["register:4040:8"]]
- 005211bc ["INT_ADD", "register:40f0:8", ["const:5211bc:8", "const:4:8"]]
- 005211bc ["CALLIND", null, ["register:0:8"]]
+ 005211fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 005211fc ["INT_ADD", "register:40f0:8", ["const:5211fc:8", "const:4:8"]]
+ 005211fc ["CALLIND", null, ["register:0:8"]]
- 005211bc bytes 00013fd6
+ 005211fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18b45f5aacec826ec9f79eabbe863df0"></a>

### [`00522864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522864.md) → [`005228a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005228a4.md) _ZNK5Botan16X509_Certificate4dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00522904",
      "incomplete_value": false,
      "site": "0052290c",
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
            "const:c93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005228c4",
      "incomplete_value": false,
      "site": "005228cc",
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
            "const:cef:8"
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
      "definition_site": "00522940",
      "incomplete_value": true,
      "site": "0052294c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00522900",
      "incomplete_value": true,
      "site": "0052290c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
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
      "definition_site": "0052293c",
      "incomplete_value": false,
      "site": "0052294c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "005228fc",
      "incomplete_value": false,
      "site": "0052290c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "00522904",
      "PARAM",
      [
        "storage",
        "002b0cef",
        null,
        "string"
      ]
    ],
    [
      "0052293c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00522940",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00522904",
      "PARAM",
      [
        "storage",
        "002b0c93",
        null,
        "string"
      ]
    ],
    [
      "0052293c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00522940",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005228cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522864.md#insn-005228cc) · [`0052290c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522864.md#insn-0052290c) · [`005228b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522864.md#insn-005228b8)
- 新版 [`0052290c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005228a4.md#insn-0052290c) · [`0052294c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005228a4.md#insn-0052294c) · [`005228f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/005228a4.md#insn-005228f8)

~~~diff
- 005228cc ["INT_ADD", "register:40f0:8", ["const:5228cc:8", "const:4:8"]]
- 005228cc ["CALL", null, ["callee:0043de18:8"]]
+ 0052290c ["INT_ADD", "register:40f0:8", ["const:52290c:8", "const:4:8"]]
+ 0052290c ["CALL", null, ["callee:0043de18:8"]]
- 005228cc bytes 436dfc97
+ 0052290c bytes 436dfc97
- 0052290c ["INT_ADD", "register:40f0:8", ["const:52290c:8", "const:4:8"]]
- 0052290c ["CALL", null, ["callee:00c57fe0:8"]]
+ 0052294c ["INT_ADD", "register:40f0:8", ["const:52294c:8", "const:4:8"]]
+ 0052294c ["CALL", null, ["callee:00c57fe0:8"]]
- 0052290c bytes 81d51c94
+ 0052294c bytes a5d51c94
- 005228b8 ["INT_ADD", "register:40f0:8", ["const:5228b8:8", "const:4:8"]]
- 005228b8 ["CALL", null, ["callee:00c57fc0:8"]]
+ 005228f8 ["INT_ADD", "register:40f0:8", ["const:5228f8:8", "const:4:8"]]
+ 005228f8 ["CALL", null, ["callee:00c57fc0:8"]]
- 005228b8 bytes 8ed51c94
+ 005228f8 bytes b2d51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-866baba5d0198ac705f201add7b4764c"></a>

### [`00522b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522b60.md) → [`00522ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ba0.md) _ZNK5Botan16X509_Certificate13allowed_usageENS_10Usage_TypeE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ea0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md) [`00c59c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c40.md)
- 新版 呼出元 1件 [`00c59f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f70.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md) [`00c59d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d10.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.30% / 新版 90.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00522c2c",
      "incomplete_value": true,
      "site": "00522c38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ceb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00522bec",
      "incomplete_value": true,
      "site": "00522bf8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cba:8"
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
      "definition_site": "00522cd4",
      "incomplete_value": true,
      "site": "00522cd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00522c94",
      "incomplete_value": true,
      "site": "00522c94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c45:8"
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
      "definition_site": "00522cc8",
      "incomplete_value": true,
      "site": "00522cd8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00522c88",
      "incomplete_value": true,
      "site": "00522c98",
      "value": [
        "LOAD",
        "8",
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
      "00522c2c",
      "READ",
      [
        "storage",
        "002b4cba",
        null,
        "string"
      ]
    ],
    [
      "00522cc4",
      "READ",
      [
        "storage",
        "002bec45",
        null,
        "string"
      ]
    ],
    [
      "00522cc8",
      "READ",
      [
        "storage",
        "002bec4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00522c2c",
      "READ",
      [
        "storage",
        "002b4ceb",
        null,
        "string"
      ]
    ],
    [
      "00522cc4",
      "READ",
      [
        "storage",
        "002bebf1",
        null,
        "string"
      ]
    ],
    [
      "00522cc8",
      "READ",
      [
        "storage",
        "002bebf8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00522ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522b60.md#insn-00522ba4) · [`00522bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522b60.md#insn-00522bb4) · [`00522bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00522/00522b60.md#insn-00522bc4)
- 新版 [`00522be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ba0.md#insn-00522be4) · [`00522bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ba0.md#insn-00522bf4) · [`00522c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00522/00522ba0.md#insn-00522c04)

~~~diff
- 00522ba4 ["INT_ADD", "register:40f0:8", ["const:522ba4:8", "const:4:8"]]
- 00522ba4 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522be4 ["INT_ADD", "register:40f0:8", ["const:522be4:8", "const:4:8"]]
+ 00522be4 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522ba4 bytes 93db1c94
+ 00522be4 bytes b7db1c94
- 00522bb4 ["INT_ADD", "register:40f0:8", ["const:522bb4:8", "const:4:8"]]
- 00522bb4 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522bf4 ["INT_ADD", "register:40f0:8", ["const:522bf4:8", "const:4:8"]]
+ 00522bf4 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522bb4 bytes 8fdb1c94
+ 00522bf4 bytes b3db1c94
- 00522bc4 ["INT_ADD", "register:40f0:8", ["const:522bc4:8", "const:4:8"]]
- 00522bc4 ["CALL", null, ["callee:00c59ac0:8"]]
+ 00522c04 ["INT_ADD", "register:40f0:8", ["const:522c04:8", "const:4:8"]]
+ 00522c04 ["CALL", null, ["callee:00c59ac0:8"]]
- 00522bc4 bytes 8bdb1c94
+ 00522c04 bytes afdb1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e062a0f893a91f36cafac4b48653c07"></a>

### [`005230cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/005230cc.md) → [`0052310c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/0052310c.md) _ZNK5Botan16X509_Certificate12subject_infoERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59eb0.md) · 呼出先 16件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c59f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59f80.md) · 呼出先 16件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`005480d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005480d8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00523440",
      "incomplete_value": false,
      "site": "00523448",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00523400",
      "incomplete_value": false,
      "site": "00523408",
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
            "const:56c:8"
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
      "definition_site": "0052347c",
      "incomplete_value": false,
      "site": "00523484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:ed6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052343c",
      "incomplete_value": false,
      "site": "00523444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:ea5:8"
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
      "definition_site": "005234b8",
      "incomplete_value": false,
      "site": "005234c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:1bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00523478",
      "incomplete_value": false,
      "site": "00523480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:209:8"
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
      "00523440",
      "PARAM",
      [
        "storage",
        "002ab56c",
        null,
        "string"
      ]
    ],
    [
      "0052347c",
      "PARAM",
      [
        "storage",
        "002b4ea5",
        null,
        "string"
      ]
    ],
    [
      "005234b8",
      "PARAM",
      [
        "storage",
        "002a1209",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00523440",
      "PARAM",
      [
        "storage",
        "002ab510",
        null,
        "string"
      ]
    ],
    [
      "0052347c",
      "PARAM",
      [
        "storage",
        "002b4ed6",
        null,
        "string"
      ]
    ],
    [
      "005234b8",
      "PARAM",
      [
        "storage",
        "002a11bc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00523408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/005230cc.md#insn-00523408) · [`00523444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/005230cc.md#insn-00523444) · [`00523480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00523/005230cc.md#insn-00523480)
- 新版 [`00523448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/0052310c.md#insn-00523448) · [`00523484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/0052310c.md#insn-00523484) · [`005234c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00523/0052310c.md#insn-005234c0)

~~~diff
- 00523408 ["INT_ADD", "register:40f0:8", ["const:523408:8", "const:4:8"]]
- 00523408 ["CALL", null, ["callee:00441ed4:8"]]
+ 00523448 ["INT_ADD", "register:40f0:8", ["const:523448:8", "const:4:8"]]
+ 00523448 ["CALL", null, ["callee:00441ed4:8"]]
- 00523408 bytes a37afc97
+ 00523448 bytes a37afc97
- 00523444 ["INT_ADD", "register:40f0:8", ["const:523444:8", "const:4:8"]]
- 00523444 ["CALL", null, ["callee:00441ed4:8"]]
+ 00523484 ["INT_ADD", "register:40f0:8", ["const:523484:8", "const:4:8"]]
+ 00523484 ["CALL", null, ["callee:00441ed4:8"]]
- 00523444 bytes 947afc97
+ 00523484 bytes 947afc97
- 00523480 ["INT_ADD", "register:40f0:8", ["const:523480:8", "const:4:8"]]
- 00523480 ["CALL", null, ["callee:00441ed4:8"]]
+ 005234c0 ["INT_ADD", "register:40f0:8", ["const:5234c0:8", "const:4:8"]]
+ 005234c0 ["CALL", null, ["callee:00441ed4:8"]]
- 00523480 bytes 857afc97
+ 005234c0 bytes 857afc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d21458763b5ced7faa9fe7478ec517a9"></a>

### [`005249e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/005249e0.md) → [`00524a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524a20.md) _ZNK5Botan16X509_Certificate9to_stringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 27件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0053ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ee70.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`0053eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053eeb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.84% / 新版 92.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 47件, `store_destination` 2件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00524a64",
      "incomplete_value": true,
      "site": "00524a78",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00524a24",
      "incomplete_value": true,
      "site": "00524a38",
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
            "const:40:8"
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
      "definition_site": "00524a70",
      "incomplete_value": true,
      "site": "00524a7c",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00524a30",
      "incomplete_value": true,
      "site": "00524a3c",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00524a84",
      "incomplete_value": true,
      "site": "00524a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
      "definition_site": "00524a44",
      "incomplete_value": true,
      "site": "00524a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00524a4c",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00524a5c",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00524a70",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00524a4c",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00524a5c",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00524a70",
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00524a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/005249e0.md#insn-00524a7c) · [`00524ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/005249e0.md#insn-00524ab4) · [`00524adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00524/005249e0.md#insn-00524adc)
- 新版 [`00524abc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524a20.md#insn-00524abc) · [`00524af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524a20.md#insn-00524af4) · [`00524b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00524/00524a20.md#insn-00524b1c)

~~~diff
- 00524a7c ["INT_ADD", "register:40f0:8", ["const:524a7c:8", "const:4:8"]]
- 00524a7c ["CALL", null, ["callee:00c582c0:8"]]
+ 00524abc ["INT_ADD", "register:40f0:8", ["const:524abc:8", "const:4:8"]]
+ 00524abc ["CALL", null, ["callee:00c582c0:8"]]
- 00524a7c bytes ddcd1c94
+ 00524abc bytes 01ce1c94
- 00524ab4 ["INT_ADD", "register:40f0:8", ["const:524ab4:8", "const:4:8"]]
- 00524ab4 ["CALL", null, ["callee:00459510:8"]]
+ 00524af4 ["INT_ADD", "register:40f0:8", ["const:524af4:8", "const:4:8"]]
+ 00524af4 ["CALL", null, ["callee:00459510:8"]]
- 00524ab4 bytes 87d2fc97
+ 00524af4 bytes 87d2fc97
- 00524adc ["INT_ADD", "register:40f0:8", ["const:524adc:8", "const:4:8"]]
- 00524adc ["CALL", null, ["callee:00459510:8"]]
+ 00524b1c ["INT_ADD", "register:40f0:8", ["const:524b1c:8", "const:4:8"]]
+ 00524b1c ["CALL", null, ["callee:00459510:8"]]
- 00524adc bytes 7dd2fc97
+ 00524b1c bytes 7dd2fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa6fcf1cb89f5c2912eee4fe47a9b159"></a>

### [`005262e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005262e0.md) → [`00526320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526320.md) _ZN5Botan17X509_Cert_Options17add_ex_constraintERKNS_3OIDE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0054b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`0054b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b984.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526360",
      "incomplete_value": true,
      "site": "00526364",
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
      "definition_site": "00526320",
      "incomplete_value": true,
      "site": "00526324",
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
      "00526354",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00526364",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00526354",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00526364",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00526314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005262e0.md#insn-00526314) · [`00526338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005262e0.md#insn-00526338) · [`00526350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005262e0.md#insn-00526350)
- 新版 [`00526354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526320.md#insn-00526354) · [`00526378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526320.md#insn-00526378) · [`00526390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526320.md#insn-00526390)

~~~diff
- 00526314 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
- 00526314 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00526354 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 00526354 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00526314 bytes 08a146f9
+ 00526354 bytes 080947f9
- 00526338 ["INT_ADD", "register:40f0:8", ["const:526338:8", "const:4:8"]]
- 00526338 ["CALL", null, ["callee:00c57f60:8"]]
+ 00526378 ["INT_ADD", "register:40f0:8", ["const:526378:8", "const:4:8"]]
+ 00526378 ["CALL", null, ["callee:00c57f60:8"]]
- 00526338 bytes d6c61c94
+ 00526378 bytes fac61c94
- 00526350 ["INT_ADD", "register:40f0:8", ["const:526350:8", "const:4:8"]]
- 00526350 ["CALL", null, ["callee:00c580d0:8"]]
+ 00526390 ["INT_ADD", "register:40f0:8", ["const:526390:8", "const:4:8"]]
+ 00526390 ["CALL", null, ["callee:00c580d0:8"]]
- 00526350 bytes 2cc71c94
+ 00526390 bytes 50c71c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d8d5e3aa42bcb9d31d5d573ff661f43"></a>

### [`005263b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005263b0.md) → [`005263f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005263f0.md) _ZN5Botan17X509_Cert_Options17add_ex_constraintERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0054d844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054d/0054d844.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0054d884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054d/0054d884.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526440",
      "incomplete_value": true,
      "site": "00526448",
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
      "definition_site": "00526400",
      "incomplete_value": true,
      "site": "00526408",
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
      "00526438",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00526448",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00526438",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00526448",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005263d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005263b0.md#insn-005263d8) · [`005263f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005263b0.md#insn-005263f8) · [`00526424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005263b0.md#insn-00526424)
- 新版 [`00526418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005263f0.md#insn-00526418) · [`00526438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005263f0.md#insn-00526438) · [`00526464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005263f0.md#insn-00526464)

~~~diff
- 005263d8 ["INT_ADD", "register:40f0:8", ["const:5263d8:8", "const:4:8"]]
- 005263d8 ["CALL", null, ["callee:00c58750:8"]]
+ 00526418 ["INT_ADD", "register:40f0:8", ["const:526418:8", "const:4:8"]]
+ 00526418 ["CALL", null, ["callee:00c58750:8"]]
- 005263d8 bytes aac81c94
+ 00526418 bytes cec81c94
- 005263f8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
- 005263f8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00526438 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
+ 00526438 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005263f8 bytes 29a146f9
+ 00526438 bytes 290947f9
- 00526424 ["INT_ADD", "register:40f0:8", ["const:526424:8", "const:4:8"]]
- 00526424 ["CALL", null, ["callee:0054d884:8"]]
+ 00526464 ["INT_ADD", "register:40f0:8", ["const:526464:8", "const:4:8"]]
+ 00526464 ["CALL", null, ["callee:0054d884:8"]]
- 00526424 bytes 089d0094
+ 00526464 bytes 089d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a5b4195f0ffef7a351c02557486bfb7"></a>

### [`005264ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005264ac.md) → [`005264ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005264ec.md) _ZN5Botan17X509_Cert_OptionsC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md) [`00547b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b70.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00547bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bac.md) [`00547bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bb0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526568",
      "incomplete_value": true,
      "site": "00526568",
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
      "definition_site": "00526528",
      "incomplete_value": true,
      "site": "00526528",
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
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526570",
      "incomplete_value": true,
      "site": "00526570",
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
      "definition_site": "00526530",
      "incomplete_value": true,
      "site": "00526530",
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
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00526598",
      "incomplete_value": true,
      "site": "00526598",
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
      "definition_site": "00526558",
      "incomplete_value": true,
      "site": "00526558",
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
      "00526554",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "00526568",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00526570",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00526554",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "00526568",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00526570",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052657c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005264ac.md#insn-0052657c) · [`00526788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005264ac.md#insn-00526788) · [`005267c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005264ac.md#insn-005267c4)
- 新版 [`005265bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005264ec.md#insn-005265bc) · [`005267c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005264ec.md#insn-005267c8) · [`00526804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/005264ec.md#insn-00526804)

~~~diff
- 0052657c ["INT_ADD", "register:40f0:8", ["const:52657c:8", "const:4:8"]]
- 0052657c ["CALL", null, ["callee:00c58260:8"]]
+ 005265bc ["INT_ADD", "register:40f0:8", ["const:5265bc:8", "const:4:8"]]
+ 005265bc ["CALL", null, ["callee:00c58260:8"]]
- 0052657c bytes 05c71c94
+ 005265bc bytes 29c71c94
- 00526788 ["INT_ADD", "register:40f0:8", ["const:526788:8", "const:4:8"]]
- 00526788 ["CALL", null, ["callee:00c58180:8"]]
+ 005267c8 ["INT_ADD", "register:40f0:8", ["const:5267c8:8", "const:4:8"]]
+ 005267c8 ["CALL", null, ["callee:00c58180:8"]]
- 00526788 bytes 4ac61c94
+ 005267c8 bytes 6ec61c94
- 005267c4 ["INT_ADD", "register:40f0:8", ["const:5267c4:8", "const:4:8"]]
- 005267c4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00526804 ["INT_ADD", "register:40f0:8", ["const:526804:8", "const:4:8"]]
+ 00526804 ["CALL", null, ["callee:00c57fe0:8"]]
- 005267c4 bytes d3c51c94
+ 00526804 bytes f7c51c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ed52004bb8b4beaf8f0977f7542c56c"></a>

### [`005269d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005269d0.md) → [`00526a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md) _ZN5Botan4PKIX11check_chainERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEENS1_6chrono10time_pointINSC_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ee0.md) · 呼出先 29件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00511224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511224.md) [`00527dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)
- 新版 呼出元 1件 [`00c59fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59fb0.md) · 呼出先 29件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00511264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md) [`00527dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527dfc.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.42% / 新版 99.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00526fa8",
      "incomplete_value": true,
      "site": "00526fac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4050:8"
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
      "definition_site": "00526f68",
      "incomplete_value": true,
      "site": "00526f6c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4050:8"
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
    "ordinal": 58,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00527c3c",
      "incomplete_value": false,
      "site": "00527c44",
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
            "const:fbb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00527bfc",
      "incomplete_value": false,
      "site": "00527c04",
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
            "const:f:8"
          ]
        ]
      ]
    },
    "ordinal": 86,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00527c78",
      "incomplete_value": true,
      "site": "00527c84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00527c38",
      "incomplete_value": true,
      "site": "00527c44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 88,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00526f04",
      "READ",
      [
        "storage",
        "00ca53a8",
        null,
        "undefined8"
      ]
    ],
    [
      "005270ac",
      "READ",
      [
        "storage",
        "00ca53a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00527c3c",
      "PARAM",
      [
        "storage",
        "002b900f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00526f04",
      "READ",
      [
        "storage",
        "00ca54a8",
        null,
        "undefined8"
      ]
    ],
    [
      "005270ac",
      "READ",
      [
        "storage",
        "00ca54a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00527c3c",
      "PARAM",
      [
        "storage",
        "002b8fbb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00527c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005269d0.md#insn-00527c04) · [`00527c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005269d0.md#insn-00527c44) · [`00526a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005269d0.md#insn-00526a2c)
- 新版 [`00527c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md#insn-00527c44) · [`00527c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md#insn-00527c84) · [`00526a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md#insn-00526a6c)

~~~diff
- 00527c04 ["INT_ADD", "register:40f0:8", ["const:527c04:8", "const:4:8"]]
- 00527c04 ["CALL", null, ["callee:0043de18:8"]]
+ 00527c44 ["INT_ADD", "register:40f0:8", ["const:527c44:8", "const:4:8"]]
+ 00527c44 ["CALL", null, ["callee:0043de18:8"]]
- 00527c04 bytes 7558fc97
+ 00527c44 bytes 7558fc97
- 00527c44 ["INT_ADD", "register:40f0:8", ["const:527c44:8", "const:4:8"]]
- 00527c44 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00527c84 ["INT_ADD", "register:40f0:8", ["const:527c84:8", "const:4:8"]]
+ 00527c84 ["CALL", null, ["callee:00c57fe0:8"]]
- 00527c44 bytes b3c01c94
+ 00527c84 bytes d7c01c94
- 00526a2c ["INT_ADD", "register:40f0:8", ["const:526a2c:8", "const:4:8"]]
- 00526a2c ["CALL", null, ["callee:00c59b40:8"]]
+ 00526a6c ["INT_ADD", "register:40f0:8", ["const:526a6c:8", "const:4:8"]]
+ 00526a6c ["CALL", null, ["callee:00c59b40:8"]]
- 00526a2c bytes 11cc1c94
+ 00526a6c bytes 35cc1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6f09b51f924ce27f620f3f105050ee5"></a>

### [`00527e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527e28.md) → [`00527e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md) _ZN5Botan4PKIX10check_ocspERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_4OCSP8Respons

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ef0.md) · 呼出先 21件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`005015f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/005015f0.md) [`00527dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527dbc.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)
- 新版 呼出元 1件 [`00c59fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59fc0.md) · 呼出先 21件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00501630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501630.md) [`00527dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527dfc.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.36% / 新版 99.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005282d4",
      "incomplete_value": false,
      "site": "005282dc",
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
            "const:921:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528294",
      "incomplete_value": false,
      "site": "0052829c",
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
            "const:97d:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00528310",
      "incomplete_value": true,
      "site": "0052831c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005282d0",
      "incomplete_value": true,
      "site": "005282dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052830c",
      "incomplete_value": false,
      "site": "0052831c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "005282cc",
      "incomplete_value": false,
      "site": "005282dc",
      "value": [
        "leaf",
        "const:535868:8"
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
      "005282d4",
      "PARAM",
      [
        "storage",
        "002ae97d",
        null,
        "string"
      ]
    ],
    [
      "0052830c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00528310",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005282d4",
      "PARAM",
      [
        "storage",
        "002ae921",
        null,
        "string"
      ]
    ],
    [
      "0052830c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00528310",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052829c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527e28.md#insn-0052829c) · [`005282dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527e28.md#insn-005282dc) · [`00527eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00527/00527e28.md#insn-00527eac)
- 新版 [`005282dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md#insn-005282dc) · [`0052831c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md#insn-0052831c) · [`00527eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00527/00527e68.md#insn-00527eec)

~~~diff
- 0052829c ["INT_ADD", "register:40f0:8", ["const:52829c:8", "const:4:8"]]
- 0052829c ["CALL", null, ["callee:0043de18:8"]]
+ 005282dc ["INT_ADD", "register:40f0:8", ["const:5282dc:8", "const:4:8"]]
+ 005282dc ["CALL", null, ["callee:0043de18:8"]]
- 0052829c bytes cf56fc97
+ 005282dc bytes cf56fc97
- 005282dc ["INT_ADD", "register:40f0:8", ["const:5282dc:8", "const:4:8"]]
- 005282dc ["CALL", null, ["callee:00c57fe0:8"]]
+ 0052831c ["INT_ADD", "register:40f0:8", ["const:52831c:8", "const:4:8"]]
+ 0052831c ["CALL", null, ["callee:00c57fe0:8"]]
- 005282dc bytes 0dbf1c94
+ 0052831c bytes 31bf1c94
- 00527eac ["INT_ADD", "register:40f0:8", ["const:527eac:8", "const:4:8"]]
- 00527eac ["CALL", null, ["callee:00c57f60:8"]]
+ 00527eec ["INT_ADD", "register:40f0:8", ["const:527eec:8", "const:4:8"]]
+ 00527eec ["CALL", null, ["callee:00c57f60:8"]]
- 00527eac bytes f9bf1c94
+ 00527eec bytes 1dc01c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f37eb3c84a49cd5b401e25e85cb152ec"></a>

### [`005283a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00528/005283a4.md) → [`005283e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/005283e4.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_INS3_IKNS_8X509_CRLEEENS7

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f00.md) · 呼出先 29件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`0053f810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f810.md)
- 新版 呼出元 1件 [`00c59fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59fd0.md) · 呼出先 29件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0053f850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.72% / 新版 99.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00528e3c",
      "incomplete_value": false,
      "site": "00528e44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:22a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528dfc",
      "incomplete_value": false,
      "site": "00528e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:277:8"
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00528e78",
      "incomplete_value": true,
      "site": "00528e84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00528e38",
      "incomplete_value": true,
      "site": "00528e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00528e74",
      "incomplete_value": false,
      "site": "00528e84",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "00528e34",
      "incomplete_value": false,
      "site": "00528e44",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "ordinal": 58,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00528e3c",
      "PARAM",
      [
        "storage",
        "002a4277",
        null,
        "string"
      ]
    ],
    [
      "00528e74",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00528e78",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00528e3c",
      "PARAM",
      [
        "storage",
        "002a422a",
        null,
        "string"
      ]
    ],
    [
      "00528e74",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00528e78",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00528e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00528/005283a4.md#insn-00528e04) · [`00528e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00528/005283a4.md#insn-00528e44) · [`00528428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00528/005283a4.md#insn-00528428)
- 新版 [`00528e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/005283e4.md#insn-00528e44) · [`00528e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/005283e4.md#insn-00528e84) · [`00528468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/005283e4.md#insn-00528468)

~~~diff
- 00528e04 ["INT_ADD", "register:40f0:8", ["const:528e04:8", "const:4:8"]]
- 00528e04 ["CALL", null, ["callee:0043de18:8"]]
+ 00528e44 ["INT_ADD", "register:40f0:8", ["const:528e44:8", "const:4:8"]]
+ 00528e44 ["CALL", null, ["callee:0043de18:8"]]
- 00528e04 bytes f553fc97
+ 00528e44 bytes f553fc97
- 00528e44 ["INT_ADD", "register:40f0:8", ["const:528e44:8", "const:4:8"]]
- 00528e44 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00528e84 ["INT_ADD", "register:40f0:8", ["const:528e84:8", "const:4:8"]]
+ 00528e84 ["CALL", null, ["callee:00c57fe0:8"]]
- 00528e44 bytes 33bc1c94
+ 00528e84 bytes 57bc1c94
- 00528428 ["INT_ADD", "register:40f0:8", ["const:528428:8", "const:4:8"]]
- 00528428 ["CALL", null, ["callee:00c57f60:8"]]
+ 00528468 ["INT_ADD", "register:40f0:8", ["const:528468:8", "const:4:8"]]
+ 00528468 ["CALL", null, ["callee:00c57f60:8"]]
- 00528428 bytes 9abe1c94
+ 00528468 bytes bebe1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7cdaf0b9cb577213d2a63cda1af78f2"></a>

### [`00528f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00528/00528f80.md) → [`00528fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/00528fc0.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_IPNS_17Certificate_StoreE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f10.md) · 呼出先 16件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00548d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548d1c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 1件 [`00c59fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59fe0.md) · 呼出先 16件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00548d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548d5c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.44% / 新版 96.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00529208",
      "incomplete_value": false,
      "site": "00529228",
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
            "const:70c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005291c8",
      "incomplete_value": false,
      "site": "005291e8",
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
            "const:768:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00529210",
      "incomplete_value": false,
      "site": "00529228",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005291d0",
      "incomplete_value": false,
      "site": "005291e8",
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
            "const:3ea:8"
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
      "definition_site": "00529218",
      "incomplete_value": false,
      "site": "00529228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:1cb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005291d8",
      "incomplete_value": false,
      "site": "005291e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:18b:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00529208",
      "PARAM",
      [
        "storage",
        "002a6768",
        null,
        "string"
      ]
    ],
    [
      "00529210",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00529218",
      "PARAM",
      [
        "storage",
        "002b618b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00529208",
      "PARAM",
      [
        "storage",
        "002a670c",
        null,
        "string"
      ]
    ],
    [
      "00529210",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00529218",
      "PARAM",
      [
        "storage",
        "002b61cb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005291e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00528/00528f80.md#insn-005291e8) · [`00529204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00528/00528f80.md#insn-00529204) · [`00529240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00528/00528f80.md#insn-00529240)
- 新版 [`00529228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/00528fc0.md#insn-00529228) · [`00529244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/00528fc0.md#insn-00529244) · [`00529280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00528/00528fc0.md#insn-00529280)

~~~diff
- 005291e8 ["INT_ADD", "register:40f0:8", ["const:5291e8:8", "const:4:8"]]
- 005291e8 ["CALL", null, ["callee:00c58720:8"]]
+ 00529228 ["INT_ADD", "register:40f0:8", ["const:529228:8", "const:4:8"]]
+ 00529228 ["CALL", null, ["callee:00c58720:8"]]
- 005291e8 bytes 1abd1c94
+ 00529228 bytes 3ebd1c94
- 00529204 ["INT_ADD", "register:40f0:8", ["const:529204:8", "const:4:8"]]
- 00529204 ["CALL", null, ["callee:0043de18:8"]]
+ 00529244 ["INT_ADD", "register:40f0:8", ["const:529244:8", "const:4:8"]]
+ 00529244 ["CALL", null, ["callee:0043de18:8"]]
- 00529204 bytes f552fc97
+ 00529244 bytes f552fc97
- 00529240 ["INT_ADD", "register:40f0:8", ["const:529240:8", "const:4:8"]]
- 00529240 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00529280 ["INT_ADD", "register:40f0:8", ["const:529280:8", "const:4:8"]]
+ 00529280 ["CALL", null, ["callee:00c57fe0:8"]]
- 00529240 bytes 34bb1c94
+ 00529280 bytes 58bb1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2424b199ebd6505f6e4dd367a47ae7a"></a>

### [`00529334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529334.md) → [`00529374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529374.md) _ZN5Botan4PKIX22build_certificate_pathERNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_IPNS_17Certi

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`005027f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`005408d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408d0.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00502838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00540910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540910.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.43% / 新版 99.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005295dc",
      "incomplete_value": true,
      "site": "005295dc",
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
      "definition_site": "0052959c",
      "incomplete_value": true,
      "site": "0052959c",
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
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005295d0",
      "READ",
      [
        "storage",
        "00c9b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "005295dc",
      "DATA",
      [
        "storage",
        "00c67798",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "005295d0",
      "READ",
      [
        "storage",
        "00c9b1c8",
        null,
        "pointer"
      ]
    ],
    [
      "005295dc",
      "DATA",
      [
        "storage",
        "00c67868",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00529378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529334.md#insn-00529378) · [`005293c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529334.md#insn-005293c4) · [`005293d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529334.md#insn-005293d8)
- 新版 [`005293b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529374.md#insn-005293b8) · [`00529404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529374.md#insn-00529404) · [`00529418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529374.md#insn-00529418)

~~~diff
- 00529378 ["INT_ADD", "register:40f0:8", ["const:529378:8", "const:4:8"]]
- 00529378 ["CALL", null, ["callee:00c59ac0:8"]]
+ 005293b8 ["INT_ADD", "register:40f0:8", ["const:5293b8:8", "const:4:8"]]
+ 005293b8 ["CALL", null, ["callee:00c59ac0:8"]]
- 00529378 bytes 9ec11c94
+ 005293b8 bytes c2c11c94
- 005293c4 ["INT_ADD", "register:40f0:8", ["const:5293c4:8", "const:4:8"]]
- 005293c4 ["CALL", null, ["callee:00c53d70:8"]]
+ 00529404 ["INT_ADD", "register:40f0:8", ["const:529404:8", "const:4:8"]]
+ 00529404 ["CALL", null, ["callee:00c53d70:8"]]
- 005293c4 bytes 43aa1c94
+ 00529404 bytes 5baa1c94
- 005293d8 ["INT_ADD", "register:40f0:8", ["const:5293d8:8", "const:4:8"]]
- 005293d8 ["CALL", null, ["callee:005485d8:8"]]
+ 00529418 ["INT_ADD", "register:40f0:8", ["const:529418:8", "const:4:8"]]
+ 00529418 ["CALL", null, ["callee:005485d8:8"]]
- 005293d8 bytes 707c0094
+ 00529418 bytes 707c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8af36e27e73c6ddc01d64eac1ee730fa"></a>

### [`0052b128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b128.md) → [`0052b168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b168.md) _ZN5Botan4PKIX23merge_revocation_statusERNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f20.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c59ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ff0.md) · 呼出先 8件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.29% / 新版 99.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052b578",
      "incomplete_value": false,
      "site": "0052b580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:24a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052b538",
      "incomplete_value": false,
      "site": "0052b540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:297:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052b5b4",
      "incomplete_value": true,
      "site": "0052b5c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052b574",
      "incomplete_value": true,
      "site": "0052b580",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
      "definition_site": "0052b5b0",
      "incomplete_value": false,
      "site": "0052b5c0",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "0052b570",
      "incomplete_value": false,
      "site": "0052b580",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0052b578",
      "PARAM",
      [
        "storage",
        "002a4297",
        null,
        "string"
      ]
    ],
    [
      "0052b5b0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0052b5b4",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052b578",
      "PARAM",
      [
        "storage",
        "002a424a",
        null,
        "string"
      ]
    ],
    [
      "0052b5b0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0052b5b4",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052b540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b128.md#insn-0052b540) · [`0052b580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b128.md#insn-0052b580) · [`0052b1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b128.md#insn-0052b1d0)
- 新版 [`0052b580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b168.md#insn-0052b580) · [`0052b5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b168.md#insn-0052b5c0) · [`0052b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b168.md#insn-0052b210)

~~~diff
- 0052b540 ["INT_ADD", "register:40f0:8", ["const:52b540:8", "const:4:8"]]
- 0052b540 ["CALL", null, ["callee:0043de18:8"]]
+ 0052b580 ["INT_ADD", "register:40f0:8", ["const:52b580:8", "const:4:8"]]
+ 0052b580 ["CALL", null, ["callee:0043de18:8"]]
- 0052b540 bytes 264afc97
+ 0052b580 bytes 264afc97
- 0052b580 ["INT_ADD", "register:40f0:8", ["const:52b580:8", "const:4:8"]]
- 0052b580 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0052b5c0 ["INT_ADD", "register:40f0:8", ["const:52b5c0:8", "const:4:8"]]
+ 0052b5c0 ["CALL", null, ["callee:00c57fe0:8"]]
- 0052b580 bytes 64b21c94
+ 0052b5c0 bytes 88b21c94
- 0052b1d0 ["INT_ADD", "register:40f0:8", ["const:52b1d0:8", "const:4:8"]]
- 0052b1d0 ["CALL", null, ["callee:0043bbe4:8"]]
+ 0052b210 ["INT_ADD", "register:40f0:8", ["const:52b210:8", "const:4:8"]]
+ 0052b210 ["CALL", null, ["callee:0043bbe4:8"]]
- 0052b1d0 bytes 7542fc97
+ 0052b210 bytes 7542fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6093a86e389df1a229fa947dbb7494d6"></a>

### [`0052b5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b5d4.md) → [`0052b614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b614.md) _ZN5Botan4PKIX14overall_statusERKNSt6__ndk16vectorINS1_3setINS_23Certificate_Status_CodeENS1_4lessIS4_EENS1_9allocatorIS4_EEEENS7_IS9_EEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f30.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c5a000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a000.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052b6dc",
      "incomplete_value": false,
      "site": "0052b6e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:cbe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052b69c",
      "incomplete_value": false,
      "site": "0052b6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:c8d:8"
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
      "definition_site": "0052b718",
      "incomplete_value": true,
      "site": "0052b724",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052b6d8",
      "incomplete_value": true,
      "site": "0052b6e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
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
      "definition_site": "0052b714",
      "incomplete_value": false,
      "site": "0052b724",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "0052b6d4",
      "incomplete_value": false,
      "site": "0052b6e4",
      "value": [
        "leaf",
        "const:535868:8"
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
      "0052b6dc",
      "PARAM",
      [
        "storage",
        "002b2c8d",
        null,
        "string"
      ]
    ],
    [
      "0052b714",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0052b718",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052b6dc",
      "PARAM",
      [
        "storage",
        "002b2cbe",
        null,
        "string"
      ]
    ],
    [
      "0052b714",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0052b718",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052b6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b5d4.md#insn-0052b6a4) · [`0052b6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b5d4.md#insn-0052b6e4) · [`0052b690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b5d4.md#insn-0052b690)
- 新版 [`0052b6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b614.md#insn-0052b6e4) · [`0052b724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b614.md#insn-0052b724) · [`0052b6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b614.md#insn-0052b6d0)

~~~diff
- 0052b6a4 ["INT_ADD", "register:40f0:8", ["const:52b6a4:8", "const:4:8"]]
- 0052b6a4 ["CALL", null, ["callee:0043de18:8"]]
+ 0052b6e4 ["INT_ADD", "register:40f0:8", ["const:52b6e4:8", "const:4:8"]]
+ 0052b6e4 ["CALL", null, ["callee:0043de18:8"]]
- 0052b6a4 bytes cd49fc97
+ 0052b6e4 bytes cd49fc97
- 0052b6e4 ["INT_ADD", "register:40f0:8", ["const:52b6e4:8", "const:4:8"]]
- 0052b6e4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0052b724 ["INT_ADD", "register:40f0:8", ["const:52b724:8", "const:4:8"]]
+ 0052b724 ["CALL", null, ["callee:00c57fe0:8"]]
- 0052b6e4 bytes 0bb21c94
+ 0052b724 bytes 2fb21c94
- 0052b690 ["INT_ADD", "register:40f0:8", ["const:52b690:8", "const:4:8"]]
- 0052b690 ["CALL", null, ["callee:00c57fc0:8"]]
+ 0052b6d0 ["INT_ADD", "register:40f0:8", ["const:52b6d0:8", "const:4:8"]]
+ 0052b6d0 ["CALL", null, ["callee:00c57fc0:8"]]
- 0052b690 bytes 18b21c94
+ 0052b6d0 bytes 3cb21c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f777926ac559b760535d597bf59aff16"></a>

### [`0052b738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md) → [`0052b778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b778.md) _ZN5Botan18x509_path_validateERKNSt6__ndk16vectorINS_16X509_CertificateENS0_9allocatorIS2_EEEERKNS_28Path_Validation_RestrictionsERKNS1_IPNS

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f40.md) · 呼出先 28件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) [`0052c244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c244.md) [`0052c354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052c/0052c354.md)
- 新版 呼出元 1件 [`00c5a010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a010.md) · 呼出先 28件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00529df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529df8.md) [`0052c284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c284.md) [`0052c394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052c/0052c394.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.03% / 新版 99.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052b7f0",
      "incomplete_value": true,
      "site": "0052b7f4",
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
      "definition_site": "0052b7b0",
      "incomplete_value": true,
      "site": "0052b7b4",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052b814",
      "incomplete_value": true,
      "site": "0052b818",
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
      "definition_site": "0052b7d4",
      "incomplete_value": true,
      "site": "0052b7d8",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052b960",
      "value": [
        "leaf",
        "ram:529df8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052b920",
      "value": [
        "leaf",
        "ram:529db8:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0052b7e8",
      "READ",
      [
        "storage",
        "00c9b0d8",
        null,
        "pointer"
      ]
    ],
    [
      "0052b7f4",
      "DATA",
      [
        "storage",
        "00c6a740",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "0052b810",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052b7e8",
      "READ",
      [
        "storage",
        "00c9b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "0052b7f4",
      "DATA",
      [
        "storage",
        "00c6a810",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "0052b810",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052b798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md#insn-0052b798) · [`0052b920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md#insn-0052b920) · [`0052c0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052b/0052b738.md#insn-0052c0a4)
- 新版 [`0052b7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b778.md#insn-0052b7d8) · [`0052b960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b778.md#insn-0052b960) · [`0052c0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052b/0052b778.md#insn-0052c0e4)

~~~diff
- 0052b798 ["INT_ADD", "register:40f0:8", ["const:52b798:8", "const:4:8"]]
- 0052b798 ["CALL", null, ["callee:00c57f60:8"]]
+ 0052b7d8 ["INT_ADD", "register:40f0:8", ["const:52b7d8:8", "const:4:8"]]
+ 0052b7d8 ["CALL", null, ["callee:00c57f60:8"]]
- 0052b798 bytes beb11c94
+ 0052b7d8 bytes e2b11c94
- 0052b920 ["INT_ADD", "register:40f0:8", ["const:52b920:8", "const:4:8"]]
- 0052b920 ["CALL", null, ["ram:529db8:8"]]
+ 0052b960 ["INT_ADD", "register:40f0:8", ["const:52b960:8", "const:4:8"]]
+ 0052b960 ["CALL", null, ["ram:529df8:8"]]
- 0052b920 bytes 26f9ff97
+ 0052b960 bytes 26f9ff97
- 0052c0a4 ["INT_ADD", "register:40f0:8", ["const:52c0a4:8", "const:4:8"]]
- 0052c0a4 ["CALL", null, ["callee:0043de18:8"]]
+ 0052c0e4 ["INT_ADD", "register:40f0:8", ["const:52c0e4:8", "const:4:8"]]
+ 0052c0e4 ["CALL", null, ["callee:0043de18:8"]]
- 0052c0a4 bytes 4d47fc97
+ 0052c0e4 bytes 4d47fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48ef3e1f127583499eb2c09b86941dbf"></a>

### [`0052d114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d114.md) → [`0052d154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d154.md) _ZNK5Botan22Path_Validation_Result10trust_rootEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052d1c4",
      "incomplete_value": false,
      "site": "0052d1cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:de2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052d184",
      "incomplete_value": false,
      "site": "0052d18c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:e36:8"
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
      "definition_site": "0052d200",
      "incomplete_value": true,
      "site": "0052d20c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052d1c0",
      "incomplete_value": true,
      "site": "0052d1cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
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
      "definition_site": "0052d1fc",
      "incomplete_value": false,
      "site": "0052d20c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "0052d1bc",
      "incomplete_value": false,
      "site": "0052d1cc",
      "value": [
        "leaf",
        "const:535868:8"
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
      "0052d1c4",
      "PARAM",
      [
        "storage",
        "002bee36",
        null,
        "string"
      ]
    ],
    [
      "0052d1fc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0052d200",
      "READ",
      [
        "storage",
        "00c9ad88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052d1c4",
      "PARAM",
      [
        "storage",
        "002bede2",
        null,
        "string"
      ]
    ],
    [
      "0052d1fc",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0052d200",
      "READ",
      [
        "storage",
        "00c9ae58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052d18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d114.md#insn-0052d18c) · [`0052d1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d114.md#insn-0052d1cc) · [`0052d1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d114.md#insn-0052d1f0)
- 新版 [`0052d1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d154.md#insn-0052d1cc) · [`0052d20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d154.md#insn-0052d20c) · [`0052d230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d154.md#insn-0052d230)

~~~diff
- 0052d18c ["INT_ADD", "register:40f0:8", ["const:52d18c:8", "const:4:8"]]
- 0052d18c ["CALL", null, ["callee:0043de18:8"]]
+ 0052d1cc ["INT_ADD", "register:40f0:8", ["const:52d1cc:8", "const:4:8"]]
+ 0052d1cc ["CALL", null, ["callee:0043de18:8"]]
- 0052d18c bytes 1343fc97
+ 0052d1cc bytes 1343fc97
- 0052d1cc ["INT_ADD", "register:40f0:8", ["const:52d1cc:8", "const:4:8"]]
- 0052d1cc ["CALL", null, ["callee:00c57fe0:8"]]
+ 0052d20c ["INT_ADD", "register:40f0:8", ["const:52d20c:8", "const:4:8"]]
+ 0052d20c ["CALL", null, ["callee:00c57fe0:8"]]
- 0052d1cc bytes 51ab1c94
+ 0052d20c bytes 75ab1c94
- 0052d1f0 ["INT_ADD", "register:40f0:8", ["const:52d1f0:8", "const:4:8"]]
- 0052d1f0 ["CALL", null, ["callee:0043de18:8"]]
+ 0052d230 ["INT_ADD", "register:40f0:8", ["const:52d230:8", "const:4:8"]]
+ 0052d230 ["CALL", null, ["callee:0043de18:8"]]
- 0052d1f0 bytes fa42fc97
+ 0052d230 bytes fa42fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf9ecc1bf0f883e8d9b7756d8d92764b"></a>

### [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) → [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) _ZN5Botan4X50923create_self_signed_certERKNS_17X509_Cert_OptionsERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9al

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 27件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`004c0a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0a78.md) [`00500f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f0c.md) [`005052d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/005052d4.md) [`00510060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`004c0ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0ab8.md) [`00500f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f4c.md) [`00505314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505314.md) [`005100a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.76% / 新版 95.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052d5a4",
      "incomplete_value": true,
      "site": "0052d5a4",
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
      "definition_site": "0052d564",
      "incomplete_value": true,
      "site": "0052d564",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052d5f0",
      "incomplete_value": true,
      "site": "0052d5f0",
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
      "definition_site": "0052d5b0",
      "incomplete_value": true,
      "site": "0052d5b0",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052d758",
      "incomplete_value": true,
      "site": "0052d760",
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
      "definition_site": "0052d718",
      "incomplete_value": true,
      "site": "0052d720",
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
      "0052d58c",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0052d5a4",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0052d5dc",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052d58c",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0052d5a4",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0052d5dc",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052d614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md#insn-0052d614) · [`0052d808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md#insn-0052d808) · [`0052d878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md#insn-0052d878)
- 新版 [`0052d654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md#insn-0052d654) · [`0052d848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md#insn-0052d848) · [`0052d8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md#insn-0052d8b8)

~~~diff
- 0052d614 ["INT_ADD", "register:40f0:8", ["const:52d614:8", "const:4:8"]]
- 0052d614 ["CALL", null, ["callee:0052dc4c:8"]]
+ 0052d654 ["INT_ADD", "register:40f0:8", ["const:52d654:8", "const:4:8"]]
+ 0052d654 ["CALL", null, ["callee:0052dc4c:8"]]
- 0052d614 bytes 7e010094
+ 0052d654 bytes 7e010094
- 0052d808 ["INT_ADD", "register:40f0:8", ["const:52d808:8", "const:4:8"]]
- 0052d808 ["CALL", null, ["callee:00c59b50:8"]]
+ 0052d848 ["INT_ADD", "register:40f0:8", ["const:52d848:8", "const:4:8"]]
+ 0052d848 ["CALL", null, ["callee:00c59b50:8"]]
- 0052d808 bytes 9eb01c94
+ 0052d848 bytes c2b01c94
- 0052d878 ["INT_ADD", "register:40f0:8", ["const:52d878:8", "const:4:8"]]
- 0052d878 ["CALL", null, ["callee:0053eeb0:8"]]
+ 0052d8b8 ["INT_ADD", "register:40f0:8", ["const:52d8b8:8", "const:4:8"]]
+ 0052d8b8 ["CALL", null, ["callee:0053eeb0:8"]]
- 0052d878 bytes 7e450094
+ 0052d8b8 bytes 7e450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8059c2ca6dd1167046781e7a5e647518"></a>

### [`0052de1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052de1c.md) → [`0052de5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052de5c.md) FUN_0052de5c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 10件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`004ff37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 10件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`004ff3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.54% / 新版 87.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052dea4",
      "incomplete_value": true,
      "site": "0052dea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:522:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052de64",
      "incomplete_value": true,
      "site": "0052de64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:57e:8"
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
      "definition_site": "0052de9c",
      "incomplete_value": true,
      "site": "0052dea8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0052de5c",
      "incomplete_value": true,
      "site": "0052de68",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052df0c",
      "incomplete_value": true,
      "site": "0052df0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052decc",
      "incomplete_value": true,
      "site": "0052decc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:32a:8"
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
      "0052de84",
      "READ",
      [
        "storage",
        "002a657e",
        null,
        "string"
      ]
    ],
    [
      "0052de9c",
      "READ",
      [
        "storage",
        "002a6585",
        null,
        "string"
      ]
    ],
    [
      "0052def8",
      "READ",
      [
        "storage",
        "002bb32a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0052de84",
      "READ",
      [
        "storage",
        "002a6522",
        null,
        "string"
      ]
    ],
    [
      "0052de9c",
      "READ",
      [
        "storage",
        "002a6529",
        null,
        "string"
      ]
    ],
    [
      "0052def8",
      "READ",
      [
        "storage",
        "002bb2d6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052dea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052de1c.md#insn-0052dea8) · [`0052deec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052de1c.md#insn-0052deec) · [`0052df0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052de1c.md#insn-0052df0c)
- 新版 [`0052dee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052de5c.md#insn-0052dee8) · [`0052df2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052de5c.md#insn-0052df2c) · [`0052df4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052de5c.md#insn-0052df4c)

~~~diff
- 0052dea8 ["INT_ADD", "register:40f0:8", ["const:52dea8:8", "const:4:8"]]
- 0052dea8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0052dee8 ["INT_ADD", "register:40f0:8", ["const:52dee8:8", "const:4:8"]]
+ 0052dee8 ["CALL", null, ["callee:00c57f80:8"]]
- 0052dea8 bytes 02a81c94
+ 0052dee8 bytes 26a81c94
- 0052deec ["INT_ADD", "register:40f0:8", ["const:52deec:8", "const:4:8"]]
- 0052deec ["CALL", null, ["callee:00c59bd0:8"]]
+ 0052df2c ["INT_ADD", "register:40f0:8", ["const:52df2c:8", "const:4:8"]]
+ 0052df2c ["CALL", null, ["callee:00c59bd0:8"]]
- 0052deec bytes 05af1c94
+ 0052df2c bytes 29af1c94
- 0052df0c ["INT_ADD", "register:40f0:8", ["const:52df0c:8", "const:4:8"]]
- 0052df0c ["CALL", null, ["callee:00c57f80:8"]]
+ 0052df4c ["INT_ADD", "register:40f0:8", ["const:52df4c:8", "const:4:8"]]
+ 0052df4c ["CALL", null, ["callee:00c57f80:8"]]
- 0052df0c bytes e9a71c94
+ 0052df4c bytes 0da81c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04e99b81903e9d95d05d3f6c22484550"></a>

### [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) → [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) _ZN5Botan4X50915create_cert_reqERKNS_17X509_Cert_OptionsERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9allocatorI

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 42件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`004c0a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0a78.md) [`00500f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f0c.md) [`005052d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/005052d4.md)
- 新版 呼出元 0件  · 呼出先 42件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`004c0ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0ab8.md) [`00500f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f4c.md) [`00505314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505314.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.04% / 新版 94.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 5件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e3c8",
      "incomplete_value": true,
      "site": "0052e3c8",
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
      "definition_site": "0052e388",
      "incomplete_value": true,
      "site": "0052e388",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e414",
      "incomplete_value": true,
      "site": "0052e414",
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
      "definition_site": "0052e3d4",
      "incomplete_value": true,
      "site": "0052e3d4",
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e578",
      "incomplete_value": true,
      "site": "0052e580",
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
      "definition_site": "0052e538",
      "incomplete_value": true,
      "site": "0052e540",
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
      "0052e3b0",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0052e3c8",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0052e400",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052e3b0",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0052e3c8",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0052e400",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052e438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md#insn-0052e438) · [`0052e5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md#insn-0052e5ec) · [`0052e684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md#insn-0052e684)
- 新版 [`0052e478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md#insn-0052e478) · [`0052e62c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md#insn-0052e62c) · [`0052e6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md#insn-0052e6c4)

~~~diff
- 0052e438 ["INT_ADD", "register:40f0:8", ["const:52e438:8", "const:4:8"]]
- 0052e438 ["CALL", null, ["callee:0052dc4c:8"]]
+ 0052e478 ["INT_ADD", "register:40f0:8", ["const:52e478:8", "const:4:8"]]
+ 0052e478 ["CALL", null, ["callee:0052dc4c:8"]]
- 0052e438 bytes f5fdff97
+ 0052e478 bytes f5fdff97
- 0052e5ec ["INT_ADD", "register:40f0:8", ["const:52e5ec:8", "const:4:8"]]
- 0052e5ec ["CALL", null, ["callee:0053eeb0:8"]]
+ 0052e62c ["INT_ADD", "register:40f0:8", ["const:52e62c:8", "const:4:8"]]
+ 0052e62c ["CALL", null, ["callee:0053eeb0:8"]]
- 0052e5ec bytes 21420094
+ 0052e62c bytes 21420094
- 0052e684 ["INT_ADD", "register:40f0:8", ["const:52e684:8", "const:4:8"]]
- 0052e684 ["CALL", null, ["callee:00c59b50:8"]]
+ 0052e6c4 ["INT_ADD", "register:40f0:8", ["const:52e6c4:8", "const:4:8"]]
+ 0052e6c4 ["CALL", null, ["callee:00c59b50:8"]]
- 0052e684 bytes ffac1c94
+ 0052e6c4 bytes 23ad1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39f4e45d4e2d2a84bac3280e0e528f77"></a>

### [`0052efc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052efc0.md) → [`0052f000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f000.md) FUN_0052f000

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f0b4.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0052f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f0f4.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f038",
      "incomplete_value": true,
      "site": "0052f038",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052eff8",
      "incomplete_value": true,
      "site": "0052eff8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f064",
      "incomplete_value": true,
      "site": "0052f064",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f024",
      "incomplete_value": true,
      "site": "0052f024",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f090",
      "incomplete_value": true,
      "site": "0052f090",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f050",
      "incomplete_value": true,
      "site": "0052f050",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
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
      "0052f028",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052f054",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052f080",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052f028",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052f054",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052f080",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052eff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052efc0.md#insn-0052eff8) · [`0052f024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052efc0.md#insn-0052f024) · [`0052f050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052efc0.md#insn-0052f050)
- 新版 [`0052f038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f000.md#insn-0052f038) · [`0052f064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f000.md#insn-0052f064) · [`0052f090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f000.md#insn-0052f090)

~~~diff
- 0052eff8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052eff8 ["INT_ADD", "register:40f0:8", ["const:52eff8:8", "const:4:8"]]
- 0052eff8 ["CALLIND", null, ["register:0:8"]]
+ 0052f038 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f038 ["INT_ADD", "register:40f0:8", ["const:52f038:8", "const:4:8"]]
+ 0052f038 ["CALLIND", null, ["register:0:8"]]
- 0052eff8 bytes 20013fd6
+ 0052f038 bytes 20013fd6
- 0052f024 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f024 ["INT_ADD", "register:40f0:8", ["const:52f024:8", "const:4:8"]]
- 0052f024 ["CALLIND", null, ["register:0:8"]]
+ 0052f064 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f064 ["INT_ADD", "register:40f0:8", ["const:52f064:8", "const:4:8"]]
+ 0052f064 ["CALLIND", null, ["register:0:8"]]
- 0052f024 bytes 20013fd6
+ 0052f064 bytes 20013fd6
- 0052f050 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f050 ["INT_ADD", "register:40f0:8", ["const:52f050:8", "const:4:8"]]
- 0052f050 ["CALLIND", null, ["register:0:8"]]
+ 0052f090 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f090 ["INT_ADD", "register:40f0:8", ["const:52f090:8", "const:4:8"]]
+ 0052f090 ["CALLIND", null, ["register:0:8"]]
- 0052f050 bytes 20013fd6
+ 0052f090 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-692beb48c09da979feade834eac939a5"></a>

### [`0052f268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f268.md) → [`0052f2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2a8.md) FUN_0052f2a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052f2c4",
      "incomplete_value": true,
      "site": "0052f2c8",
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
      "definition_site": "0052f284",
      "incomplete_value": true,
      "site": "0052f288",
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
      "0052f2c0",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0052f2c8",
      "DATA",
      [
        "storage",
        "00c67ad0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0052f2c0",
      "READ",
      [
        "storage",
        "00c9aee0",
        null,
        "pointer"
      ]
    ],
    [
      "0052f2c8",
      "DATA",
      [
        "storage",
        "00c67ba0",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f268.md#insn-0052f274) · [`0052f280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f268.md#insn-0052f280)
- 新版 [`0052f2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2a8.md#insn-0052f2b4) · [`0052f2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2a8.md#insn-0052f2c0)

~~~diff
- 0052f274 ["INT_ADD", "register:40f0:8", ["const:52f274:8", "const:4:8"]]
- 0052f274 ["CALL", null, ["callee:00c57f60:8"]]
+ 0052f2b4 ["INT_ADD", "register:40f0:8", ["const:52f2b4:8", "const:4:8"]]
+ 0052f2b4 ["CALL", null, ["callee:00c57f60:8"]]
- 0052f274 bytes 07a31c94
+ 0052f2b4 bytes 2ba31c94
- 0052f280 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 0052f280 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f2c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
+ 0052f2c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f280 bytes 080947f9
+ 0052f2c0 bytes 087147f9
~~~


<a id="compare-805846398dc720c45bff3dd401b3eb61"></a>

### [`0052f2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f2ac.md) → [`0052f2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2ec.md) FUN_0052f2ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052f3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f3a0.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0052f3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f3e0.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f324",
      "incomplete_value": true,
      "site": "0052f324",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f2e4",
      "incomplete_value": true,
      "site": "0052f2e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f350",
      "incomplete_value": true,
      "site": "0052f350",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f310",
      "incomplete_value": true,
      "site": "0052f310",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f37c",
      "incomplete_value": true,
      "site": "0052f37c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f33c",
      "incomplete_value": true,
      "site": "0052f33c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
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
      "0052f314",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052f340",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052f36c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052f314",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052f340",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052f36c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f2ac.md#insn-0052f2e4) · [`0052f310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f2ac.md#insn-0052f310) · [`0052f33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f2ac.md#insn-0052f33c)
- 新版 [`0052f324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2ec.md#insn-0052f324) · [`0052f350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2ec.md#insn-0052f350) · [`0052f37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f2ec.md#insn-0052f37c)

~~~diff
- 0052f2e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f2e4 ["INT_ADD", "register:40f0:8", ["const:52f2e4:8", "const:4:8"]]
- 0052f2e4 ["CALLIND", null, ["register:0:8"]]
+ 0052f324 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f324 ["INT_ADD", "register:40f0:8", ["const:52f324:8", "const:4:8"]]
+ 0052f324 ["CALLIND", null, ["register:0:8"]]
- 0052f2e4 bytes 20013fd6
+ 0052f324 bytes 20013fd6
- 0052f310 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f310 ["INT_ADD", "register:40f0:8", ["const:52f310:8", "const:4:8"]]
- 0052f310 ["CALLIND", null, ["register:0:8"]]
+ 0052f350 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f350 ["INT_ADD", "register:40f0:8", ["const:52f350:8", "const:4:8"]]
+ 0052f350 ["CALLIND", null, ["register:0:8"]]
- 0052f310 bytes 20013fd6
+ 0052f350 bytes 20013fd6
- 0052f33c ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f33c ["INT_ADD", "register:40f0:8", ["const:52f33c:8", "const:4:8"]]
- 0052f33c ["CALLIND", null, ["register:0:8"]]
+ 0052f37c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f37c ["INT_ADD", "register:40f0:8", ["const:52f37c:8", "const:4:8"]]
+ 0052f37c ["CALLIND", null, ["register:0:8"]]
- 0052f33c bytes 20013fd6
+ 0052f37c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5de6ba32e2c4f175bc1716138bca06f1"></a>

### [`0052f554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f554.md) → [`0052f594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f594.md) FUN_0052f594

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052f5b0",
      "incomplete_value": true,
      "site": "0052f5b4",
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
      "definition_site": "0052f570",
      "incomplete_value": true,
      "site": "0052f574",
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
      "0052f5ac",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0052f5b4",
      "DATA",
      [
        "storage",
        "00c67ba8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0052f5ac",
      "READ",
      [
        "storage",
        "00c9aee8",
        null,
        "pointer"
      ]
    ],
    [
      "0052f5b4",
      "DATA",
      [
        "storage",
        "00c67c78",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f554.md#insn-0052f560) · [`0052f56c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f554.md#insn-0052f56c)
- 新版 [`0052f5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f594.md#insn-0052f5a0) · [`0052f5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f594.md#insn-0052f5ac)

~~~diff
- 0052f560 ["INT_ADD", "register:40f0:8", ["const:52f560:8", "const:4:8"]]
- 0052f560 ["CALL", null, ["callee:00c57f60:8"]]
+ 0052f5a0 ["INT_ADD", "register:40f0:8", ["const:52f5a0:8", "const:4:8"]]
+ 0052f5a0 ["CALL", null, ["callee:00c57f60:8"]]
- 0052f560 bytes 4ca21c94
+ 0052f5a0 bytes 70a21c94
- 0052f56c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e18:8"]]
- 0052f56c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f5ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee8:8"]]
+ 0052f5ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f56c bytes 080d47f9
+ 0052f5ac bytes 087547f9
~~~


<a id="compare-f4aad17425e46b9237d28594d9c42978"></a>

### [`0052f598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f598.md) → [`0052f5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f5d8.md) FUN_0052f5d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0052f68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f68c.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`0052f6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f6cc.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f610",
      "incomplete_value": true,
      "site": "0052f610",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f5d0",
      "incomplete_value": true,
      "site": "0052f5d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f63c",
      "incomplete_value": true,
      "site": "0052f63c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f5fc",
      "incomplete_value": true,
      "site": "0052f5fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f668",
      "incomplete_value": true,
      "site": "0052f668",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f628",
      "incomplete_value": true,
      "site": "0052f628",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
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
      "0052f600",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052f62c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0052f658",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052f600",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052f62c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0052f658",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f598.md#insn-0052f5d0) · [`0052f5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f598.md#insn-0052f5fc) · [`0052f628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f598.md#insn-0052f628)
- 新版 [`0052f610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f5d8.md#insn-0052f610) · [`0052f63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f5d8.md#insn-0052f63c) · [`0052f668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f5d8.md#insn-0052f668)

~~~diff
- 0052f5d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f5d0 ["INT_ADD", "register:40f0:8", ["const:52f5d0:8", "const:4:8"]]
- 0052f5d0 ["CALLIND", null, ["register:0:8"]]
+ 0052f610 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f610 ["INT_ADD", "register:40f0:8", ["const:52f610:8", "const:4:8"]]
+ 0052f610 ["CALLIND", null, ["register:0:8"]]
- 0052f5d0 bytes 20013fd6
+ 0052f610 bytes 20013fd6
- 0052f5fc ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f5fc ["INT_ADD", "register:40f0:8", ["const:52f5fc:8", "const:4:8"]]
- 0052f5fc ["CALLIND", null, ["register:0:8"]]
+ 0052f63c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f63c ["INT_ADD", "register:40f0:8", ["const:52f63c:8", "const:4:8"]]
+ 0052f63c ["CALLIND", null, ["register:0:8"]]
- 0052f5fc bytes 20013fd6
+ 0052f63c bytes 20013fd6
- 0052f628 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f628 ["INT_ADD", "register:40f0:8", ["const:52f628:8", "const:4:8"]]
- 0052f628 ["CALLIND", null, ["register:0:8"]]
+ 0052f668 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f668 ["INT_ADD", "register:40f0:8", ["const:52f668:8", "const:4:8"]]
+ 0052f668 ["CALLIND", null, ["register:0:8"]]
- 0052f628 bytes 20013fd6
+ 0052f668 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cf8d9e9ea8aba2af15431ba24d0aab4"></a>

### [`0052f840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f840.md) → [`0052f880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f880.md) FUN_0052f880

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052f89c",
      "incomplete_value": true,
      "site": "0052f8a0",
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
      "definition_site": "0052f85c",
      "incomplete_value": true,
      "site": "0052f860",
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
      "0052f898",
      "READ",
      [
        "storage",
        "00c9ae20",
        null,
        "pointer"
      ]
    ],
    [
      "0052f8a0",
      "DATA",
      [
        "storage",
        "00c67c58",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "0052f898",
      "READ",
      [
        "storage",
        "00c9aef0",
        null,
        "pointer"
      ]
    ],
    [
      "0052f8a0",
      "DATA",
      [
        "storage",
        "00c67d28",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f840.md#insn-0052f84c) · [`0052f858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f840.md#insn-0052f858)
- 新版 [`0052f88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f880.md#insn-0052f88c) · [`0052f898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f880.md#insn-0052f898)

~~~diff
- 0052f84c ["INT_ADD", "register:40f0:8", ["const:52f84c:8", "const:4:8"]]
- 0052f84c ["CALL", null, ["callee:00c57f60:8"]]
+ 0052f88c ["INT_ADD", "register:40f0:8", ["const:52f88c:8", "const:4:8"]]
+ 0052f88c ["CALL", null, ["callee:00c57f60:8"]]
- 0052f84c bytes 91a11c94
+ 0052f88c bytes b5a11c94
- 0052f858 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e20:8"]]
- 0052f858 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f898 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef0:8"]]
+ 0052f898 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f858 bytes 081147f9
+ 0052f898 bytes 087947f9
~~~


<a id="compare-00d5b803acfd2679dac2dbc06099b520"></a>

### [`0052f89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f89c.md) → [`0052f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f8dc.md) FUN_0052f8dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f910",
      "incomplete_value": true,
      "site": "0052f910",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f8d0",
      "incomplete_value": true,
      "site": "0052f8d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
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
      "0052f900",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052f900",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f89c.md#insn-0052f8d0) · [`0052f8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f89c.md#insn-0052f8c0) · [`0052f8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f89c.md#insn-0052f8d8)
- 新版 [`0052f910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f8dc.md#insn-0052f910) · [`0052f900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f8dc.md#insn-0052f900) · [`0052f918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f8dc.md#insn-0052f918)

~~~diff
- 0052f8d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f8d0 ["INT_ADD", "register:40f0:8", ["const:52f8d0:8", "const:4:8"]]
- 0052f8d0 ["CALLIND", null, ["register:0:8"]]
+ 0052f910 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f910 ["INT_ADD", "register:40f0:8", ["const:52f910:8", "const:4:8"]]
+ 0052f910 ["CALLIND", null, ["register:0:8"]]
- 0052f8d0 bytes 20013fd6
+ 0052f910 bytes 20013fd6
- 0052f8c0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:738:8"]]
- 0052f8c0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f900 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:808:8"]]
+ 0052f900 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f8c0 bytes 299d43f9
+ 0052f900 bytes 290544f9
- 0052f8d8 ["INT_ADD", "register:40f0:8", ["const:52f8d8:8", "const:4:8"]]
- 0052f8d8 ["CALL", null, ["callee:00c58730:8"]]
+ 0052f918 ["INT_ADD", "register:40f0:8", ["const:52f918:8", "const:4:8"]]
+ 0052f918 ["CALL", null, ["callee:00c58730:8"]]
- 0052f8d8 bytes 62a31c94
+ 0052f918 bytes 86a31c94
~~~


<a id="compare-e86580214fd4a333a0070204c23bb5b9"></a>

### [`0052f920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f920.md) → [`0052f960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f960.md) FUN_0052f960

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052f97c",
      "incomplete_value": true,
      "site": "0052f980",
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
      "definition_site": "0052f93c",
      "incomplete_value": true,
      "site": "0052f940",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052f9a4",
      "incomplete_value": true,
      "site": "0052f9a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f964",
      "incomplete_value": true,
      "site": "0052f964",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
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
      "0052f974",
      "READ",
      [
        "storage",
        "00c9ae30",
        null,
        "pointer"
      ]
    ],
    [
      "0052f980",
      "DATA",
      [
        "storage",
        "00c66420",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052f994",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052f974",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "0052f980",
      "DATA",
      [
        "storage",
        "00c664f0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052f994",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f920.md#insn-0052f964) · [`0052f934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f920.md#insn-0052f934) · [`0052f954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f920.md#insn-0052f954)
- 新版 [`0052f9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f960.md#insn-0052f9a4) · [`0052f974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f960.md#insn-0052f974) · [`0052f994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f960.md#insn-0052f994)

~~~diff
- 0052f964 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f964 ["INT_ADD", "register:40f0:8", ["const:52f964:8", "const:4:8"]]
- 0052f964 ["CALLIND", null, ["register:0:8"]]
+ 0052f9a4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052f9a4 ["INT_ADD", "register:40f0:8", ["const:52f9a4:8", "const:4:8"]]
+ 0052f9a4 ["CALLIND", null, ["register:0:8"]]
- 0052f964 bytes 20013fd6
+ 0052f9a4 bytes 20013fd6
- 0052f934 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e30:8"]]
- 0052f934 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f974 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 0052f974 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f934 bytes 081947f9
+ 0052f974 bytes 088147f9
- 0052f954 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:738:8"]]
- 0052f954 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052f994 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:808:8"]]
+ 0052f994 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f954 bytes 299d43f9
+ 0052f994 bytes 290544f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bff6dac727cf6c0654da8d9be021011"></a>

### [`0052f9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f9b4.md) → [`0052f9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f9f4.md) FUN_0052f9f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fa10",
      "incomplete_value": true,
      "site": "0052fa14",
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
      "definition_site": "0052f9d0",
      "incomplete_value": true,
      "site": "0052f9d4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052fa38",
      "incomplete_value": true,
      "site": "0052fa38",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f9f8",
      "incomplete_value": true,
      "site": "0052f9f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
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
      "0052fa08",
      "READ",
      [
        "storage",
        "00c9ae30",
        null,
        "pointer"
      ]
    ],
    [
      "0052fa14",
      "DATA",
      [
        "storage",
        "00c66420",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fa28",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052fa08",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "0052fa14",
      "DATA",
      [
        "storage",
        "00c664f0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fa28",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f9b4.md#insn-0052f9f8) · [`0052f9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f9b4.md#insn-0052f9c8) · [`0052f9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052f9b4.md#insn-0052f9e8)
- 新版 [`0052fa38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f9f4.md#insn-0052fa38) · [`0052fa08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f9f4.md#insn-0052fa08) · [`0052fa28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052f9f4.md#insn-0052fa28)

~~~diff
- 0052f9f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052f9f8 ["INT_ADD", "register:40f0:8", ["const:52f9f8:8", "const:4:8"]]
- 0052f9f8 ["CALLIND", null, ["register:0:8"]]
+ 0052fa38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fa38 ["INT_ADD", "register:40f0:8", ["const:52fa38:8", "const:4:8"]]
+ 0052fa38 ["CALLIND", null, ["register:0:8"]]
- 0052f9f8 bytes 20013fd6
+ 0052fa38 bytes 20013fd6
- 0052f9c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e30:8"]]
- 0052f9c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fa08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 0052fa08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f9c8 bytes 081947f9
+ 0052fa08 bytes 088147f9
- 0052f9e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:738:8"]]
- 0052f9e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fa28 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:808:8"]]
+ 0052fa28 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0052f9e8 bytes 299d43f9
+ 0052fa28 bytes 290544f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9ff17a5ef21c99b38e0952832473f07"></a>

### [`0052fa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fa4c.md) → [`0052fa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fa8c.md) FUN_0052fa8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052faa8",
      "incomplete_value": true,
      "site": "0052faac",
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
      "definition_site": "0052fa68",
      "incomplete_value": true,
      "site": "0052fa6c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052fad0",
      "incomplete_value": true,
      "site": "0052fad0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052fa90",
      "incomplete_value": true,
      "site": "0052fa90",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
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
      "0052faa0",
      "READ",
      [
        "storage",
        "00c9ae30",
        null,
        "pointer"
      ]
    ],
    [
      "0052faac",
      "DATA",
      [
        "storage",
        "00c66420",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fac0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052faa0",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "0052faac",
      "DATA",
      [
        "storage",
        "00c664f0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fac0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052fa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fa4c.md#insn-0052fa90) · [`0052fa60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fa4c.md#insn-0052fa60) · [`0052fa80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fa4c.md#insn-0052fa80)
- 新版 [`0052fad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fa8c.md#insn-0052fad0) · [`0052faa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fa8c.md#insn-0052faa0) · [`0052fac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fa8c.md#insn-0052fac0)

~~~diff
- 0052fa90 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fa90 ["INT_ADD", "register:40f0:8", ["const:52fa90:8", "const:4:8"]]
- 0052fa90 ["CALLIND", null, ["register:0:8"]]
+ 0052fad0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fad0 ["INT_ADD", "register:40f0:8", ["const:52fad0:8", "const:4:8"]]
+ 0052fad0 ["CALLIND", null, ["register:0:8"]]
- 0052fa90 bytes 20013fd6
+ 0052fad0 bytes 20013fd6
- 0052fa60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e30:8"]]
- 0052fa60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052faa0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 0052faa0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052fa60 bytes 081947f9
+ 0052faa0 bytes 088147f9
- 0052fa80 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:738:8"]]
- 0052fa80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fac0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:808:8"]]
+ 0052fac0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0052fa80 bytes 299d43f9
+ 0052fac0 bytes 290544f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ff260209356029cc747f839761c81a1"></a>

### [`0052fae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fae0.md) → [`0052fb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fb20.md) FUN_0052fb20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fb44",
      "incomplete_value": true,
      "site": "0052fb48",
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
      "definition_site": "0052fb04",
      "incomplete_value": true,
      "site": "0052fb08",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fb80",
      "incomplete_value": true,
      "site": "0052fb84",
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
      "definition_site": "0052fb40",
      "incomplete_value": true,
      "site": "0052fb44",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052fb68",
      "incomplete_value": true,
      "site": "0052fb68",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052fb28",
      "incomplete_value": true,
      "site": "0052fb28",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
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
      "0052fb3c",
      "READ",
      [
        "storage",
        "00c9af98",
        null,
        "pointer"
      ]
    ],
    [
      "0052fb48",
      "DATA",
      [
        "storage",
        "00c67f20",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fb58",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052fb3c",
      "READ",
      [
        "storage",
        "00c9b068",
        null,
        "pointer"
      ]
    ],
    [
      "0052fb48",
      "DATA",
      [
        "storage",
        "00c67ff0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fb58",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052fb28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fae0.md#insn-0052fb28) · [`0052fb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fae0.md#insn-0052fb64) · [`0052fb84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fae0.md#insn-0052fb84)
- 新版 [`0052fb68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fb20.md#insn-0052fb68) · [`0052fba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fb20.md#insn-0052fba4) · [`0052fbc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fb20.md#insn-0052fbc4)

~~~diff
- 0052fb28 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fb28 ["INT_ADD", "register:40f0:8", ["const:52fb28:8", "const:4:8"]]
- 0052fb28 ["CALLIND", null, ["register:0:8"]]
+ 0052fb68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fb68 ["INT_ADD", "register:40f0:8", ["const:52fb68:8", "const:4:8"]]
+ 0052fb68 ["CALLIND", null, ["register:0:8"]]
- 0052fb28 bytes 20013fd6
+ 0052fb68 bytes 20013fd6
- 0052fb64 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fb64 ["INT_ADD", "register:40f0:8", ["const:52fb64:8", "const:4:8"]]
- 0052fb64 ["CALLIND", null, ["register:0:8"]]
+ 0052fba4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fba4 ["INT_ADD", "register:40f0:8", ["const:52fba4:8", "const:4:8"]]
+ 0052fba4 ["CALLIND", null, ["register:0:8"]]
- 0052fb64 bytes 20013fd6
+ 0052fba4 bytes 20013fd6
- 0052fb84 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052fb84 ["INT_ADD", "register:40f0:8", ["const:52fb84:8", "const:4:8"]]
- 0052fb84 ["CALLIND", null, ["register:0:8"]]
+ 0052fbc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052fbc4 ["INT_ADD", "register:40f0:8", ["const:52fbc4:8", "const:4:8"]]
+ 0052fbc4 ["CALLIND", null, ["register:0:8"]]
- 0052fb84 bytes 00013fd6
+ 0052fbc4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b38f849e61146f443b545fbe38878be"></a>

### [`0052fbbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fbbc.md) → [`0052fbfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fbfc.md) FUN_0052fbfc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.27% / 新版 87.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fc20",
      "incomplete_value": true,
      "site": "0052fc24",
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
      "definition_site": "0052fbe0",
      "incomplete_value": true,
      "site": "0052fbe4",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fc5c",
      "incomplete_value": true,
      "site": "0052fc60",
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
      "definition_site": "0052fc1c",
      "incomplete_value": true,
      "site": "0052fc20",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052fc44",
      "incomplete_value": true,
      "site": "0052fc44",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052fc04",
      "incomplete_value": true,
      "site": "0052fc04",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
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
      "0052fc18",
      "READ",
      [
        "storage",
        "00c9af98",
        null,
        "pointer"
      ]
    ],
    [
      "0052fc24",
      "DATA",
      [
        "storage",
        "00c67f20",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fc34",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052fc18",
      "READ",
      [
        "storage",
        "00c9b068",
        null,
        "pointer"
      ]
    ],
    [
      "0052fc24",
      "DATA",
      [
        "storage",
        "00c67ff0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fc34",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052fc04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fbbc.md#insn-0052fc04) · [`0052fc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fbbc.md#insn-0052fc40) · [`0052fc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fbbc.md#insn-0052fc60)
- 新版 [`0052fc44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fbfc.md#insn-0052fc44) · [`0052fc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fbfc.md#insn-0052fc80) · [`0052fca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fbfc.md#insn-0052fca0)

~~~diff
- 0052fc04 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fc04 ["INT_ADD", "register:40f0:8", ["const:52fc04:8", "const:4:8"]]
- 0052fc04 ["CALLIND", null, ["register:0:8"]]
+ 0052fc44 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fc44 ["INT_ADD", "register:40f0:8", ["const:52fc44:8", "const:4:8"]]
+ 0052fc44 ["CALLIND", null, ["register:0:8"]]
- 0052fc04 bytes 20013fd6
+ 0052fc44 bytes 20013fd6
- 0052fc40 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fc40 ["INT_ADD", "register:40f0:8", ["const:52fc40:8", "const:4:8"]]
- 0052fc40 ["CALLIND", null, ["register:0:8"]]
+ 0052fc80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fc80 ["INT_ADD", "register:40f0:8", ["const:52fc80:8", "const:4:8"]]
+ 0052fc80 ["CALLIND", null, ["register:0:8"]]
- 0052fc40 bytes 20013fd6
+ 0052fc80 bytes 20013fd6
- 0052fc60 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052fc60 ["INT_ADD", "register:40f0:8", ["const:52fc60:8", "const:4:8"]]
- 0052fc60 ["CALLIND", null, ["register:0:8"]]
+ 0052fca0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052fca0 ["INT_ADD", "register:40f0:8", ["const:52fca0:8", "const:4:8"]]
+ 0052fca0 ["CALLIND", null, ["register:0:8"]]
- 0052fc60 bytes 00013fd6
+ 0052fca0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8c6345186cea0fca50d63e197d85f95"></a>

### [`0052fca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fca0.md) → [`0052fce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fce0.md) FUN_0052fce0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fd04",
      "incomplete_value": true,
      "site": "0052fd08",
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
      "definition_site": "0052fcc4",
      "incomplete_value": true,
      "site": "0052fcc8",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052fd40",
      "incomplete_value": true,
      "site": "0052fd44",
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
      "definition_site": "0052fd00",
      "incomplete_value": true,
      "site": "0052fd04",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052fd28",
      "incomplete_value": true,
      "site": "0052fd28",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052fce8",
      "incomplete_value": true,
      "site": "0052fce8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
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
      "0052fcfc",
      "READ",
      [
        "storage",
        "00c9af98",
        null,
        "pointer"
      ]
    ],
    [
      "0052fd08",
      "DATA",
      [
        "storage",
        "00c67f20",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fd18",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052fcfc",
      "READ",
      [
        "storage",
        "00c9b068",
        null,
        "pointer"
      ]
    ],
    [
      "0052fd08",
      "DATA",
      [
        "storage",
        "00c67ff0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "0052fd18",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052fce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fca0.md#insn-0052fce8) · [`0052fd24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fca0.md#insn-0052fd24) · [`0052fd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fca0.md#insn-0052fd44)
- 新版 [`0052fd28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fce0.md#insn-0052fd28) · [`0052fd64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fce0.md#insn-0052fd64) · [`0052fd84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052fce0.md#insn-0052fd84)

~~~diff
- 0052fce8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fce8 ["INT_ADD", "register:40f0:8", ["const:52fce8:8", "const:4:8"]]
- 0052fce8 ["CALLIND", null, ["register:0:8"]]
+ 0052fd28 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fd28 ["INT_ADD", "register:40f0:8", ["const:52fd28:8", "const:4:8"]]
+ 0052fd28 ["CALLIND", null, ["register:0:8"]]
- 0052fce8 bytes 20013fd6
+ 0052fd28 bytes 20013fd6
- 0052fd24 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052fd24 ["INT_ADD", "register:40f0:8", ["const:52fd24:8", "const:4:8"]]
- 0052fd24 ["CALLIND", null, ["register:0:8"]]
+ 0052fd64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0052fd64 ["INT_ADD", "register:40f0:8", ["const:52fd64:8", "const:4:8"]]
+ 0052fd64 ["CALLIND", null, ["register:0:8"]]
- 0052fd24 bytes 20013fd6
+ 0052fd64 bytes 20013fd6
- 0052fd44 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052fd44 ["INT_ADD", "register:40f0:8", ["const:52fd44:8", "const:4:8"]]
- 0052fd44 ["CALLIND", null, ["register:0:8"]]
+ 0052fd84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052fd84 ["INT_ADD", "register:40f0:8", ["const:52fd84:8", "const:4:8"]]
+ 0052fd84 ["CALLIND", null, ["register:0:8"]]
- 0052fd44 bytes 00013fd6
+ 0052fd84 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6631cfc0ddb14513faf672d047898623"></a>

### [`0052fe74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fe74.md) → [`0052feb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052feb4.md) FUN_0052feb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0052fed4",
      "incomplete_value": true,
      "site": "0052fed8",
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
      "definition_site": "0052fe94",
      "incomplete_value": true,
      "site": "0052fe98",
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
      "0052fec8",
      "READ",
      [
        "storage",
        "00c9ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0052fed8",
      "DATA",
      [
        "storage",
        "00c664d8",
        null,
        "undefined1[160]"
      ]
    ]
  ],
  "added": [
    [
      "0052fec8",
      "READ",
      [
        "storage",
        "00c9af18",
        null,
        "pointer"
      ]
    ],
    [
      "0052fed8",
      "DATA",
      [
        "storage",
        "00c665a8",
        null,
        "undefined1[160]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052fe88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fe74.md#insn-0052fe88) · [`0052fea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fe74.md#insn-0052fea8) · [`0052fec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fe74.md#insn-0052fec0)
- 新版 [`0052fec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052feb4.md#insn-0052fec8) · [`0052fee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052feb4.md#insn-0052fee8) · [`0052ff00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052feb4.md#insn-0052ff00)

~~~diff
- 0052fe88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e48:8"]]
- 0052fe88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052fec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f18:8"]]
+ 0052fec8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052fe88 bytes 082547f9
+ 0052fec8 bytes 088d47f9
- 0052fea8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052fea8 ["INT_ADD", "register:40f0:8", ["const:52fea8:8", "const:4:8"]]
- 0052fea8 ["CALLIND", null, ["register:0:8"]]
+ 0052fee8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052fee8 ["INT_ADD", "register:40f0:8", ["const:52fee8:8", "const:4:8"]]
+ 0052fee8 ["CALLIND", null, ["register:0:8"]]
- 0052fea8 bytes 00013fd6
+ 0052fee8 bytes 00013fd6
- 0052fec0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052fec0 ["INT_ADD", "register:40f0:8", ["const:52fec0:8", "const:4:8"]]
- 0052fec0 ["CALLIND", null, ["register:0:8"]]
+ 0052ff00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052ff00 ["INT_ADD", "register:40f0:8", ["const:52ff00:8", "const:4:8"]]
+ 0052ff00 ["CALLIND", null, ["register:0:8"]]
- 0052fec0 bytes 00013fd6
+ 0052ff00 bytes 00013fd6
~~~


<a id="compare-5cf7385ee0e807501cd8fde5be4b4d01"></a>

### [`0052fed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fed4.md) → [`0052ff14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff14.md) FUN_0052ff14

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0052ff34",
      "incomplete_value": true,
      "site": "0052ff38",
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
      "definition_site": "0052fef4",
      "incomplete_value": true,
      "site": "0052fef8",
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
      "0052ff28",
      "READ",
      [
        "storage",
        "00c9ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0052ff38",
      "DATA",
      [
        "storage",
        "00c664d8",
        null,
        "undefined1[160]"
      ]
    ]
  ],
  "added": [
    [
      "0052ff28",
      "READ",
      [
        "storage",
        "00c9af18",
        null,
        "pointer"
      ]
    ],
    [
      "0052ff38",
      "DATA",
      [
        "storage",
        "00c665a8",
        null,
        "undefined1[160]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052fee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fed4.md#insn-0052fee8) · [`0052ff08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052fed4.md#insn-0052ff08)
- 新版 [`0052ff28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff14.md#insn-0052ff28) · [`0052ff48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff14.md#insn-0052ff48)

~~~diff
- 0052fee8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e48:8"]]
- 0052fee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052ff28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f18:8"]]
+ 0052ff28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052fee8 bytes 082547f9
+ 0052ff28 bytes 088d47f9
- 0052ff08 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052ff08 ["INT_ADD", "register:40f0:8", ["const:52ff08:8", "const:4:8"]]
- 0052ff08 ["CALLIND", null, ["register:0:8"]]
+ 0052ff48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052ff48 ["INT_ADD", "register:40f0:8", ["const:52ff48:8", "const:4:8"]]
+ 0052ff48 ["CALLIND", null, ["register:0:8"]]
- 0052ff08 bytes 00013fd6
+ 0052ff48 bytes 00013fd6
~~~


<a id="compare-0de310d98f8e2608d4a8b4e89bfe3850"></a>

### [`0052ff38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052ff38.md) → [`0052ff78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff78.md) FUN_0052ff78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0052ff98",
      "incomplete_value": true,
      "site": "0052ff9c",
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
      "definition_site": "0052ff58",
      "incomplete_value": true,
      "site": "0052ff5c",
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
      "0052ff8c",
      "READ",
      [
        "storage",
        "00c9ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0052ff9c",
      "DATA",
      [
        "storage",
        "00c664d8",
        null,
        "undefined1[160]"
      ]
    ]
  ],
  "added": [
    [
      "0052ff8c",
      "READ",
      [
        "storage",
        "00c9af18",
        null,
        "pointer"
      ]
    ],
    [
      "0052ff9c",
      "DATA",
      [
        "storage",
        "00c665a8",
        null,
        "undefined1[160]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052ff4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052ff38.md#insn-0052ff4c) · [`0052ff6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052ff38.md#insn-0052ff6c) · [`0052ff84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052f/0052ff38.md#insn-0052ff84)
- 新版 [`0052ff8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff78.md#insn-0052ff8c) · [`0052ffac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff78.md#insn-0052ffac) · [`0052ffc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052f/0052ff78.md#insn-0052ffc4)

~~~diff
- 0052ff4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e48:8"]]
- 0052ff4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052ff8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f18:8"]]
+ 0052ff8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052ff4c bytes 082547f9
+ 0052ff8c bytes 088d47f9
- 0052ff6c ["COPY", "register:0:8", ["register:4040:8"]]
- 0052ff6c ["INT_ADD", "register:40f0:8", ["const:52ff6c:8", "const:4:8"]]
- 0052ff6c ["CALLIND", null, ["register:0:8"]]
+ 0052ffac ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052ffac ["INT_ADD", "register:40f0:8", ["const:52ffac:8", "const:4:8"]]
+ 0052ffac ["CALLIND", null, ["register:0:8"]]
- 0052ff6c bytes 00013fd6
+ 0052ffac bytes 00013fd6
- 0052ff84 ["COPY", "register:0:8", ["register:4040:8"]]
- 0052ff84 ["INT_ADD", "register:40f0:8", ["const:52ff84:8", "const:4:8"]]
- 0052ff84 ["CALLIND", null, ["register:0:8"]]
+ 0052ffc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0052ffc4 ["INT_ADD", "register:40f0:8", ["const:52ffc4:8", "const:4:8"]]
+ 0052ffc4 ["CALLIND", null, ["register:0:8"]]
- 0052ff84 bytes 00013fd6
+ 0052ffc4 bytes 00013fd6
~~~


<a id="compare-dd0b525968fbbeff581608c581a47128"></a>

### [`005302e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005302e8.md) → [`00530328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530328.md) FUN_00530328

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005303bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303bc.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`005303fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005303fc.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005303a4",
      "incomplete_value": true,
      "site": "005303a8",
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
      "definition_site": "00530364",
      "incomplete_value": true,
      "site": "00530368",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530360",
      "incomplete_value": true,
      "site": "00530360",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530320",
      "incomplete_value": true,
      "site": "00530320",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0053038c",
      "incomplete_value": true,
      "site": "0053038c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053034c",
      "incomplete_value": true,
      "site": "0053034c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00530350",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0053037c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0053039c",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00530350",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0053037c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0053039c",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005302e8.md#insn-00530320) · [`00530328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005302e8.md#insn-00530328) · [`0053034c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005302e8.md#insn-0053034c)
- 新版 [`00530360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530328.md#insn-00530360) · [`00530368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530328.md#insn-00530368) · [`0053038c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530328.md#insn-0053038c)

~~~diff
- 00530320 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530320 ["INT_ADD", "register:40f0:8", ["const:530320:8", "const:4:8"]]
- 00530320 ["CALLIND", null, ["register:0:8"]]
+ 00530360 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530360 ["INT_ADD", "register:40f0:8", ["const:530360:8", "const:4:8"]]
+ 00530360 ["CALLIND", null, ["register:0:8"]]
- 00530320 bytes 20013fd6
+ 00530360 bytes 20013fd6
- 00530328 ["INT_ADD", "register:40f0:8", ["const:530328:8", "const:4:8"]]
- 00530328 ["CALL", null, ["callee:00c58730:8"]]
+ 00530368 ["INT_ADD", "register:40f0:8", ["const:530368:8", "const:4:8"]]
+ 00530368 ["CALL", null, ["callee:00c58730:8"]]
- 00530328 bytes cea01c94
+ 00530368 bytes f2a01c94
- 0053034c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053034c ["INT_ADD", "register:40f0:8", ["const:53034c:8", "const:4:8"]]
- 0053034c ["CALLIND", null, ["register:0:8"]]
+ 0053038c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053038c ["INT_ADD", "register:40f0:8", ["const:53038c:8", "const:4:8"]]
+ 0053038c ["CALLIND", null, ["register:0:8"]]
- 0053034c bytes 20013fd6
+ 0053038c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d51c139f625ae7d991e7e4b284762206"></a>

### [`00530478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530478.md) → [`005304b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005304b8.md) FUN_005304b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005304fc",
      "incomplete_value": true,
      "site": "005304fc",
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
      "definition_site": "005304bc",
      "incomplete_value": true,
      "site": "005304bc",
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
      "005304f4",
      "READ",
      [
        "storage",
        "00c9afc8",
        null,
        "pointer"
      ]
    ],
    [
      "005304fc",
      "DATA",
      [
        "storage",
        "00c68530",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "005304f4",
      "READ",
      [
        "storage",
        "00c9b098",
        null,
        "pointer"
      ]
    ],
    [
      "005304fc",
      "DATA",
      [
        "storage",
        "00c68600",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053048c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530478.md#insn-0053048c) · [`005304a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530478.md#insn-005304a4) · [`005304a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530478.md#insn-005304a8)
- 新版 [`005304cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005304b8.md#insn-005304cc) · [`005304e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005304b8.md#insn-005304e4) · [`005304e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005304b8.md#insn-005304e8)

~~~diff
- 0053048c ["INT_ADD", "register:40f0:8", ["const:53048c:8", "const:4:8"]]
- 0053048c ["CALL", null, ["callee:00c57f60:8"]]
+ 005304cc ["INT_ADD", "register:40f0:8", ["const:5304cc:8", "const:4:8"]]
+ 005304cc ["CALL", null, ["callee:00c57f60:8"]]
- 0053048c bytes 819e1c94
+ 005304cc bytes a59e1c94
- 005304a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005304a4 ["INT_ADD", "register:40f0:8", ["const:5304a4:8", "const:4:8"]]
- 005304a4 ["CALLIND", null, ["register:0:8"]]
+ 005304e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005304e4 ["INT_ADD", "register:40f0:8", ["const:5304e4:8", "const:4:8"]]
+ 005304e4 ["CALLIND", null, ["register:0:8"]]
- 005304a4 bytes 20013fd6
+ 005304e4 bytes 20013fd6
- 005304a8 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 005304e8 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 005304a8 bytes 493b00d0
+ 005304e8 bytes 493b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecddbd8587796b509d32dfa672800faa"></a>

### [`005304e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005304e0.md) → [`00530520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530520.md) FUN_00530520

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00530558",
      "incomplete_value": false,
      "site": "00530564",
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
            "const:c1e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530518",
      "incomplete_value": false,
      "site": "00530524",
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
            "const:c7a:8"
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
      "definition_site": "00530584",
      "incomplete_value": false,
      "site": "0053058c",
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
            "const:2d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530544",
      "incomplete_value": false,
      "site": "0053054c",
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
            "const:332:8"
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
      "00530558",
      "PARAM",
      [
        "storage",
        "002a8c7a",
        null,
        "string"
      ]
    ],
    [
      "00530584",
      "PARAM",
      [
        "storage",
        "002ab332",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00530558",
      "PARAM",
      [
        "storage",
        "002a8c1e",
        null,
        "string"
      ]
    ],
    [
      "00530584",
      "PARAM",
      [
        "storage",
        "002ab2d6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005304e0.md#insn-00530524) · [`0053054c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005304e0.md#insn-0053054c) · [`00530510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005304e0.md#insn-00530510)
- 新版 [`00530564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530520.md#insn-00530564) · [`0053058c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530520.md#insn-0053058c) · [`00530550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530520.md#insn-00530550)

~~~diff
- 00530524 ["INT_ADD", "register:40f0:8", ["const:530524:8", "const:4:8"]]
- 00530524 ["CALL", null, ["callee:00c58030:8"]]
+ 00530564 ["INT_ADD", "register:40f0:8", ["const:530564:8", "const:4:8"]]
+ 00530564 ["CALL", null, ["callee:00c58030:8"]]
- 00530524 bytes 8f9e1c94
+ 00530564 bytes b39e1c94
- 0053054c ["INT_ADD", "register:40f0:8", ["const:53054c:8", "const:4:8"]]
- 0053054c ["CALL", null, ["callee:00c58040:8"]]
+ 0053058c ["INT_ADD", "register:40f0:8", ["const:53058c:8", "const:4:8"]]
+ 0053058c ["CALL", null, ["callee:00c58040:8"]]
- 0053054c bytes 899e1c94
+ 0053058c bytes ad9e1c94
- 00530510 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530510 ["INT_ADD", "register:40f0:8", ["const:530510:8", "const:4:8"]]
- 00530510 ["CALLIND", null, ["register:0:8"]]
+ 00530550 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530550 ["INT_ADD", "register:40f0:8", ["const:530550:8", "const:4:8"]]
+ 00530550 ["CALLIND", null, ["register:0:8"]]
- 00530510 bytes 20013fd6
+ 00530550 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da15ba017932132332a75630db6bfc89"></a>

### [`00530664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530664.md) → [`005306a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005306a4.md) FUN_005306a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005306c8",
      "incomplete_value": true,
      "site": "005306cc",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530688",
      "incomplete_value": true,
      "site": "0053068c",
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
            "const:80:8"
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
      "definition_site": "005306ec",
      "incomplete_value": true,
      "site": "005306ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005306ac",
      "incomplete_value": true,
      "site": "005306ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530718",
      "incomplete_value": true,
      "site": "00530718",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005306d8",
      "incomplete_value": true,
      "site": "005306d8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005306c0",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "005306cc",
      "DATA",
      [
        "storage",
        "00c670a8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "005306dc",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005306c0",
      "READ",
      [
        "storage",
        "00c9b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "005306cc",
      "DATA",
      [
        "storage",
        "00c67178",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "005306dc",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005306ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530664.md#insn-005306ac) · [`005306d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530664.md#insn-005306d8) · [`00530674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530664.md#insn-00530674)
- 新版 [`005306ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005306a4.md#insn-005306ec) · [`00530718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005306a4.md#insn-00530718) · [`005306b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005306a4.md#insn-005306b4)

~~~diff
- 005306ac ["COPY", "register:0:8", ["register:4048:8"]]
- 005306ac ["INT_ADD", "register:40f0:8", ["const:5306ac:8", "const:4:8"]]
- 005306ac ["CALLIND", null, ["register:0:8"]]
+ 005306ec ["COPY", "register:0:8", ["register:4048:8"]]
+ 005306ec ["INT_ADD", "register:40f0:8", ["const:5306ec:8", "const:4:8"]]
+ 005306ec ["CALLIND", null, ["register:0:8"]]
- 005306ac bytes 20013fd6
+ 005306ec bytes 20013fd6
- 005306d8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005306d8 ["INT_ADD", "register:40f0:8", ["const:5306d8:8", "const:4:8"]]
- 005306d8 ["CALLIND", null, ["register:0:8"]]
+ 00530718 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530718 ["INT_ADD", "register:40f0:8", ["const:530718:8", "const:4:8"]]
+ 00530718 ["CALLIND", null, ["register:0:8"]]
- 005306d8 bytes 20013fd6
+ 00530718 bytes 20013fd6
- 00530674 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005306b4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00530674 bytes 483b00d0
+ 005306b4 bytes 483b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b30ae16e8b19f936b382761cc277780"></a>

### [`00530708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530708.md) → [`00530748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530748.md) FUN_00530748

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053076c",
      "incomplete_value": true,
      "site": "00530770",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053072c",
      "incomplete_value": true,
      "site": "00530730",
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
            "const:80:8"
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
      "definition_site": "00530790",
      "incomplete_value": true,
      "site": "00530790",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530750",
      "incomplete_value": true,
      "site": "00530750",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005307bc",
      "incomplete_value": true,
      "site": "005307bc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053077c",
      "incomplete_value": true,
      "site": "0053077c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00530764",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "00530770",
      "DATA",
      [
        "storage",
        "00c670a8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00530780",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00530764",
      "READ",
      [
        "storage",
        "00c9b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "00530770",
      "DATA",
      [
        "storage",
        "00c67178",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "00530780",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530708.md#insn-00530750) · [`0053077c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530708.md#insn-0053077c) · [`00530718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530708.md#insn-00530718)
- 新版 [`00530790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530748.md#insn-00530790) · [`005307bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530748.md#insn-005307bc) · [`00530758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530748.md#insn-00530758)

~~~diff
- 00530750 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530750 ["INT_ADD", "register:40f0:8", ["const:530750:8", "const:4:8"]]
- 00530750 ["CALLIND", null, ["register:0:8"]]
+ 00530790 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530790 ["INT_ADD", "register:40f0:8", ["const:530790:8", "const:4:8"]]
+ 00530790 ["CALLIND", null, ["register:0:8"]]
- 00530750 bytes 20013fd6
+ 00530790 bytes 20013fd6
- 0053077c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053077c ["INT_ADD", "register:40f0:8", ["const:53077c:8", "const:4:8"]]
- 0053077c ["CALLIND", null, ["register:0:8"]]
+ 005307bc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005307bc ["INT_ADD", "register:40f0:8", ["const:5307bc:8", "const:4:8"]]
+ 005307bc ["CALLIND", null, ["register:0:8"]]
- 0053077c bytes 20013fd6
+ 005307bc bytes 20013fd6
- 00530718 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00530758 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00530718 bytes 483b00d0
+ 00530758 bytes 483b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9b950b6b2f74ab3169087b81f62c5bf"></a>

### [`005307cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307cc.md) → [`0053080c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md) FUN_0053080c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`004c7c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7c24.md) [`004c7c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7c60.md) [`005308b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005308b8.md) [`00530944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530944.md) [`0053094c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/0053094c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 6件 [`004c7c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7c64.md) [`004c7ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7ca0.md) [`005308f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005308f8.md) [`00530984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530984.md) [`0053098c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053098c.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.98% / 新版 92.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530844",
      "incomplete_value": true,
      "site": "00530848",
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
      "definition_site": "00530804",
      "incomplete_value": true,
      "site": "00530808",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530878",
      "incomplete_value": true,
      "site": "00530878",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530838",
      "incomplete_value": true,
      "site": "00530838",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "005308cc",
      "incomplete_value": true,
      "site": "005308cc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053088c",
      "incomplete_value": true,
      "site": "0053088c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00530838",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "00530848",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00530868",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00530838",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "00530848",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00530868",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005307f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307cc.md#insn-005307f8) · [`00530838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307cc.md#insn-00530838) · [`0053088c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005307cc.md#insn-0053088c)
- 新版 [`00530838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md#insn-00530838) · [`00530878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md#insn-00530878) · [`005308cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/0053080c.md#insn-005308cc)

~~~diff
- 005307f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 005307f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530838 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 00530838 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005307f8 bytes 083947f9
+ 00530838 bytes 08a147f9
- 00530838 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530838 ["INT_ADD", "register:40f0:8", ["const:530838:8", "const:4:8"]]
- 00530838 ["CALLIND", null, ["register:0:8"]]
+ 00530878 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530878 ["INT_ADD", "register:40f0:8", ["const:530878:8", "const:4:8"]]
+ 00530878 ["CALLIND", null, ["register:0:8"]]
- 00530838 bytes 20013fd6
+ 00530878 bytes 20013fd6
- 0053088c ["COPY", "register:0:8", ["register:4048:8"]]
- 0053088c ["INT_ADD", "register:40f0:8", ["const:53088c:8", "const:4:8"]]
- 0053088c ["CALLIND", null, ["register:0:8"]]
+ 005308cc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005308cc ["INT_ADD", "register:40f0:8", ["const:5308cc:8", "const:4:8"]]
+ 005308cc ["CALLIND", null, ["register:0:8"]]
- 0053088c bytes 20013fd6
+ 005308cc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a64a4c0d188e0a48284e78b10e24748"></a>

### [`00530974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530974.md) → [`005309b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005309b4.md) FUN_005309b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00530a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a48.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00530a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530a88.md) · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530a30",
      "incomplete_value": true,
      "site": "00530a34",
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
      "definition_site": "005309f0",
      "incomplete_value": true,
      "site": "005309f4",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005309ec",
      "incomplete_value": true,
      "site": "005309ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005309ac",
      "incomplete_value": true,
      "site": "005309ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530a18",
      "incomplete_value": true,
      "site": "00530a18",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005309d8",
      "incomplete_value": true,
      "site": "005309d8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005309dc",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00530a08",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00530a28",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005309dc",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00530a08",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00530a28",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005309ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530974.md#insn-005309ac) · [`005309b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530974.md#insn-005309b4) · [`005309d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530974.md#insn-005309d8)
- 新版 [`005309ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005309b4.md#insn-005309ec) · [`005309f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005309b4.md#insn-005309f4) · [`00530a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/005309b4.md#insn-00530a18)

~~~diff
- 005309ac ["COPY", "register:0:8", ["register:4048:8"]]
- 005309ac ["INT_ADD", "register:40f0:8", ["const:5309ac:8", "const:4:8"]]
- 005309ac ["CALLIND", null, ["register:0:8"]]
+ 005309ec ["COPY", "register:0:8", ["register:4048:8"]]
+ 005309ec ["INT_ADD", "register:40f0:8", ["const:5309ec:8", "const:4:8"]]
+ 005309ec ["CALLIND", null, ["register:0:8"]]
- 005309ac bytes 20013fd6
+ 005309ec bytes 20013fd6
- 005309b4 ["INT_ADD", "register:40f0:8", ["const:5309b4:8", "const:4:8"]]
- 005309b4 ["CALL", null, ["callee:00c58730:8"]]
+ 005309f4 ["INT_ADD", "register:40f0:8", ["const:5309f4:8", "const:4:8"]]
+ 005309f4 ["CALL", null, ["callee:00c58730:8"]]
- 005309b4 bytes 2b9f1c94
+ 005309f4 bytes 4f9f1c94
- 005309d8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005309d8 ["INT_ADD", "register:40f0:8", ["const:5309d8:8", "const:4:8"]]
- 005309d8 ["CALLIND", null, ["register:0:8"]]
+ 00530a18 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530a18 ["INT_ADD", "register:40f0:8", ["const:530a18:8", "const:4:8"]]
+ 00530a18 ["CALLIND", null, ["register:0:8"]]
- 005309d8 bytes 20013fd6
+ 00530a18 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb3e0b42bd6ce67084633846691b4614"></a>

### [`00530ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530ad4.md) → [`00530b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530b14.md) FUN_00530b14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530b64",
      "incomplete_value": true,
      "site": "00530b68",
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
      "definition_site": "00530b24",
      "incomplete_value": true,
      "site": "00530b28",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530b4c",
      "incomplete_value": true,
      "site": "00530b4c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530b0c",
      "incomplete_value": true,
      "site": "00530b0c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530b88",
      "incomplete_value": true,
      "site": "00530b88",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530b48",
      "incomplete_value": true,
      "site": "00530b48",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00530b3c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00530b5c",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "00530b68",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530b3c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00530b5c",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ],
    [
      "00530b68",
      "DATA",
      [
        "storage",
        "00c66da8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530ad4.md#insn-00530b0c) · [`00530b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530ad4.md#insn-00530b48) · [`00530afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530ad4.md#insn-00530afc)
- 新版 [`00530b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530b14.md#insn-00530b4c) · [`00530b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530b14.md#insn-00530b88) · [`00530b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530b14.md#insn-00530b3c)

~~~diff
- 00530b0c ["COPY", "register:0:8", ["register:4048:8"]]
- 00530b0c ["INT_ADD", "register:40f0:8", ["const:530b0c:8", "const:4:8"]]
- 00530b0c ["CALLIND", null, ["register:0:8"]]
+ 00530b4c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530b4c ["INT_ADD", "register:40f0:8", ["const:530b4c:8", "const:4:8"]]
+ 00530b4c ["CALLIND", null, ["register:0:8"]]
- 00530b0c bytes 20013fd6
+ 00530b4c bytes 20013fd6
- 00530b48 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530b48 ["INT_ADD", "register:40f0:8", ["const:530b48:8", "const:4:8"]]
- 00530b48 ["CALLIND", null, ["register:0:8"]]
+ 00530b88 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530b88 ["INT_ADD", "register:40f0:8", ["const:530b88:8", "const:4:8"]]
+ 00530b88 ["CALLIND", null, ["register:0:8"]]
- 00530b48 bytes 20013fd6
+ 00530b88 bytes 20013fd6
- 00530afc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
- 00530afc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530b3c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00530b3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00530afc bytes a99e43f9
+ 00530b3c bytes a90644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-875392490ae4dcbd5911bc63eef0dc8d"></a>

### [`00530b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530b78.md) → [`00530bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530bb8.md) FUN_00530bb8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530c08",
      "incomplete_value": true,
      "site": "00530c0c",
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
      "definition_site": "00530bc8",
      "incomplete_value": true,
      "site": "00530bcc",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530bf0",
      "incomplete_value": true,
      "site": "00530bf0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530bb0",
      "incomplete_value": true,
      "site": "00530bb0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530c2c",
      "incomplete_value": true,
      "site": "00530c2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530bec",
      "incomplete_value": true,
      "site": "00530bec",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00530be0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00530c00",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "00530c0c",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530be0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00530c00",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ],
    [
      "00530c0c",
      "DATA",
      [
        "storage",
        "00c66da8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530b78.md#insn-00530bb0) · [`00530bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530b78.md#insn-00530bec) · [`00530ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530b78.md#insn-00530ba0)
- 新版 [`00530bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530bb8.md#insn-00530bf0) · [`00530c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530bb8.md#insn-00530c2c) · [`00530be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530bb8.md#insn-00530be0)

~~~diff
- 00530bb0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530bb0 ["INT_ADD", "register:40f0:8", ["const:530bb0:8", "const:4:8"]]
- 00530bb0 ["CALLIND", null, ["register:0:8"]]
+ 00530bf0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530bf0 ["INT_ADD", "register:40f0:8", ["const:530bf0:8", "const:4:8"]]
+ 00530bf0 ["CALLIND", null, ["register:0:8"]]
- 00530bb0 bytes 20013fd6
+ 00530bf0 bytes 20013fd6
- 00530bec ["COPY", "register:0:8", ["register:4048:8"]]
- 00530bec ["INT_ADD", "register:40f0:8", ["const:530bec:8", "const:4:8"]]
- 00530bec ["CALLIND", null, ["register:0:8"]]
+ 00530c2c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530c2c ["INT_ADD", "register:40f0:8", ["const:530c2c:8", "const:4:8"]]
+ 00530c2c ["CALLIND", null, ["register:0:8"]]
- 00530bec bytes 20013fd6
+ 00530c2c bytes 20013fd6
- 00530ba0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
- 00530ba0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530be0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00530be0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00530ba0 bytes a99e43f9
+ 00530be0 bytes a90644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0a0465d7be93ad2207478b606e8311e"></a>

### [`00530c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530c7c.md) → [`00530cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530cbc.md) FUN_00530cbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00530d0c",
      "incomplete_value": true,
      "site": "00530d10",
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
      "definition_site": "00530ccc",
      "incomplete_value": true,
      "site": "00530cd0",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530cf4",
      "incomplete_value": true,
      "site": "00530cf4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530cb4",
      "incomplete_value": true,
      "site": "00530cb4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00530d30",
      "incomplete_value": true,
      "site": "00530d30",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530cf0",
      "incomplete_value": true,
      "site": "00530cf0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00530ce4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00530d04",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "00530d10",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00530ce4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00530d04",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ],
    [
      "00530d10",
      "DATA",
      [
        "storage",
        "00c66da8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530c7c.md#insn-00530cb4) · [`00530cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530c7c.md#insn-00530cf0) · [`00530ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530c7c.md#insn-00530ca4)
- 新版 [`00530cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530cbc.md#insn-00530cf4) · [`00530d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530cbc.md#insn-00530d30) · [`00530ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00530/00530cbc.md#insn-00530ce4)

~~~diff
- 00530cb4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530cb4 ["INT_ADD", "register:40f0:8", ["const:530cb4:8", "const:4:8"]]
- 00530cb4 ["CALLIND", null, ["register:0:8"]]
+ 00530cf4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530cf4 ["INT_ADD", "register:40f0:8", ["const:530cf4:8", "const:4:8"]]
+ 00530cf4 ["CALLIND", null, ["register:0:8"]]
- 00530cb4 bytes 20013fd6
+ 00530cf4 bytes 20013fd6
- 00530cf0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00530cf0 ["INT_ADD", "register:40f0:8", ["const:530cf0:8", "const:4:8"]]
- 00530cf0 ["CALLIND", null, ["register:0:8"]]
+ 00530d30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00530d30 ["INT_ADD", "register:40f0:8", ["const:530d30:8", "const:4:8"]]
+ 00530d30 ["CALLIND", null, ["register:0:8"]]
- 00530cf0 bytes 20013fd6
+ 00530d30 bytes 20013fd6
- 00530ca4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
- 00530ca4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00530ce4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 00530ce4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00530ca4 bytes a99e43f9
+ 00530ce4 bytes a90644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

