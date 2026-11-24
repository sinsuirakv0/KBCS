# v16.0.1 → v16.0.2 · 最優先の変更候補 (23)

[一覧の目次](README.md)

<a id="compare-52afefe34132013a7fc90cc3ff6c60f4"></a>

### [`005b51e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b51e4.md) → [`005b5224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5224.md) FUN_005b5224

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
      "definition_site": "005b5234",
      "incomplete_value": false,
      "site": "005b523c",
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
      "definition_site": "005b51f4",
      "incomplete_value": false,
      "site": "005b51fc",
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
      "005b523c",
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
      "005b523c",
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

- 旧版 [`005b51f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b51e4.md#insn-005b51f4) · [`005b5200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b51e4.md#insn-005b5200)
- 新版 [`005b5234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5224.md#insn-005b5234) · [`005b5240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5224.md#insn-005b5240)

~~~diff
- 005b51f4 ["COPY", "tmp:0:8", ["const:660:8"]]
- 005b51f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b51f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b51f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5234 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 005b5234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b51f4 bytes 08811991
+ 005b5234 bytes 08c11c91
- 005b5200 ["INT_ADD", "register:40f0:8", ["const:5b5200:8", "const:4:8"]]
- 005b5200 ["CALL", null, ["callee:00c57f70:8"]]
+ 005b5240 ["INT_ADD", "register:40f0:8", ["const:5b5240:8", "const:4:8"]]
+ 005b5240 ["CALL", null, ["callee:00c57f70:8"]]
- 005b5200 bytes 288b1a94
+ 005b5240 bytes 4c8b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30f398867e546a196434fc453ac093b0"></a>

### [`005b5304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5304.md) → [`005b5344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5344.md) FUN_005b5344

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5368",
      "incomplete_value": false,
      "site": "005b5368",
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
      "definition_site": "005b5328",
      "incomplete_value": false,
      "site": "005b5328",
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
      "005b5368",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5368",
      "DATA",
      [
        "storage",
        "00c6f780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5304.md#insn-005b5318) · [`005b5324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5304.md#insn-005b5324)
- 新版 [`005b5358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5344.md#insn-005b5358) · [`005b5364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5344.md#insn-005b5364)

~~~diff
- 005b5318 ["INT_ADD", "register:40f0:8", ["const:5b5318:8", "const:4:8"]]
- 005b5318 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b5358 ["INT_ADD", "register:40f0:8", ["const:5b5358:8", "const:4:8"]]
+ 005b5358 ["CALL", null, ["callee:00c57f60:8"]]
- 005b5318 bytes de8a1a94
+ 005b5358 bytes 028b1a94
- 005b5324 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 005b5324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5364 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 005b5364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5324 bytes 08c11a91
+ 005b5364 bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbcce81cd929b453c4e0c5f466e5cf84"></a>

### [`005b5338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5338.md) → [`005b5378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5378.md) FUN_005b5378

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5384",
      "incomplete_value": false,
      "site": "005b5384",
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
      "definition_site": "005b5344",
      "incomplete_value": false,
      "site": "005b5344",
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
      "005b5384",
      "DATA",
      [
        "storage",
        "00c6f6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5384",
      "DATA",
      [
        "storage",
        "00c6f780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5338.md#insn-005b5340)
- 新版 [`005b5380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5378.md#insn-005b5380)

~~~diff
- 005b5340 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 005b5340 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5340 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5340 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5380 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 005b5380 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5380 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5380 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5340 bytes 29c11a91
+ 005b5380 bytes 29011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89a279fe09f00fd007a04c2919ee880e"></a>

### [`005b5388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5388.md) → [`005b53c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b53c8.md) FUN_005b53c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b53ec",
      "incomplete_value": true,
      "site": "005b53ec",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b53ac",
      "incomplete_value": true,
      "site": "005b53ac",
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
      "005b53ec",
      "DATA",
      [
        "storage",
        "00c6f740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b53ec",
      "DATA",
      [
        "storage",
        "00c6f810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b539c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5388.md#insn-005b539c) · [`005b53a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5388.md#insn-005b53a8)
- 新版 [`005b53dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b53c8.md#insn-005b53dc) · [`005b53e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b53c8.md#insn-005b53e8)

~~~diff
- 005b539c ["INT_ADD", "register:40f0:8", ["const:5b539c:8", "const:4:8"]]
- 005b539c ["CALL", null, ["callee:00c57f60:8"]]
+ 005b53dc ["INT_ADD", "register:40f0:8", ["const:5b53dc:8", "const:4:8"]]
+ 005b53dc ["CALL", null, ["callee:00c57f60:8"]]
- 005b539c bytes bd8a1a94
+ 005b53dc bytes e18a1a94
- 005b53a8 ["COPY", "tmp:0:8", ["const:740:8"]]
- 005b53a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b53a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b53a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b53e8 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 005b53e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b53e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b53e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b53a8 bytes 08011d91
+ 005b53e8 bytes 08412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c28e4a3bf107293c61333d55dbfa3a56"></a>

### [`005b53bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b53bc.md) → [`005b53fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b53fc.md) FUN_005b53fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5408",
      "incomplete_value": false,
      "site": "005b5408",
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
      "definition_site": "005b53c8",
      "incomplete_value": false,
      "site": "005b53c8",
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
      "005b5408",
      "DATA",
      [
        "storage",
        "00c6f740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5408",
      "DATA",
      [
        "storage",
        "00c6f810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b53c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b53bc.md#insn-005b53c4)
- 新版 [`005b5404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b53fc.md#insn-005b5404)

~~~diff
- 005b53c4 ["COPY", "tmp:0:8", ["const:740:8"]]
- 005b53c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b53c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b53c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5404 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 005b5404 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5404 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5404 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b53c4 bytes 29011d91
+ 005b5404 bytes 29412091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cfd67f08cc77f5f639c5b635a6b82ef"></a>

### [`005b5454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5454.md) → [`005b5494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5494.md) FUN_005b5494

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
      "definition_site": "005b549c",
      "incomplete_value": false,
      "site": "005b54a0",
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
      "definition_site": "005b545c",
      "incomplete_value": false,
      "site": "005b5460",
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
      "005b54a0",
      "DATA",
      [
        "storage",
        "00c6f7d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b54a0",
      "DATA",
      [
        "storage",
        "00c6f8a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b545c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5454.md#insn-005b545c) · [`005b5480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5454.md#insn-005b5480)
- 新版 [`005b549c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5494.md#insn-005b549c) · [`005b54c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5494.md#insn-005b54c0)

~~~diff
- 005b545c ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 005b545c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b545c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b545c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b549c ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 005b549c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b549c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b549c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b545c bytes 29411f91
+ 005b549c bytes 29812291
- 005b5480 ["INT_ADD", "register:40f0:8", ["const:5b5480:8", "const:4:8"]]
- 005b5480 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b54c0 ["INT_ADD", "register:40f0:8", ["const:5b54c0:8", "const:4:8"]]
+ 005b54c0 ["CALL", null, ["callee:00c57f80:8"]]
- 005b5480 bytes 8c8a1a94
+ 005b54c0 bytes b08a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f1c605162e4427bf3512ec445eb774d"></a>

### [`005b5510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5510.md) → [`005b5550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5550.md) FUN_005b5550

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b555c",
      "incomplete_value": false,
      "site": "005b555c",
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
      "definition_site": "005b551c",
      "incomplete_value": false,
      "site": "005b551c",
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
      "005b555c",
      "DATA",
      [
        "storage",
        "00c6f7d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b555c",
      "DATA",
      [
        "storage",
        "00c6f8a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5510.md#insn-005b5518)
- 新版 [`005b5558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5550.md#insn-005b5558)

~~~diff
- 005b5518 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 005b5518 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5518 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5518 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5558 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 005b5558 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5558 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5558 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5518 bytes 29411f91
+ 005b5558 bytes 29812291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d0422e0f9eb0a2cb46315e147e14748"></a>

### [`005b55d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b55d4.md) → [`005b5614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5614.md) FUN_005b5614

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5638",
      "incomplete_value": false,
      "site": "005b5638",
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
      "definition_site": "005b55f8",
      "incomplete_value": false,
      "site": "005b55f8",
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
      "005b5638",
      "DATA",
      [
        "storage",
        "00c6f860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5638",
      "DATA",
      [
        "storage",
        "00c6f930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b55e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b55d4.md#insn-005b55e8) · [`005b55f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b55d4.md#insn-005b55f4)
- 新版 [`005b5628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5614.md#insn-005b5628) · [`005b5634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5614.md#insn-005b5634)

~~~diff
- 005b55e8 ["INT_ADD", "register:40f0:8", ["const:5b55e8:8", "const:4:8"]]
- 005b55e8 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b5628 ["INT_ADD", "register:40f0:8", ["const:5b5628:8", "const:4:8"]]
+ 005b5628 ["CALL", null, ["callee:00c57f60:8"]]
- 005b55e8 bytes 2a8a1a94
+ 005b5628 bytes 4e8a1a94
- 005b55f4 ["COPY", "tmp:0:8", ["const:860:8"]]
- 005b55f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b55f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b55f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5634 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 005b5634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b55f4 bytes 08812191
+ 005b5634 bytes 08c12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc27f401ee691d6995c27ba31060aaae"></a>

### [`005b5608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5608.md) → [`005b5648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5648.md) FUN_005b5648

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5654",
      "incomplete_value": false,
      "site": "005b5654",
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
      "definition_site": "005b5614",
      "incomplete_value": false,
      "site": "005b5614",
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
      "005b5654",
      "DATA",
      [
        "storage",
        "00c6f860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5654",
      "DATA",
      [
        "storage",
        "00c6f930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5608.md#insn-005b5610)
- 新版 [`005b5650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5648.md#insn-005b5650)

~~~diff
- 005b5610 ["COPY", "tmp:0:8", ["const:860:8"]]
- 005b5610 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5610 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5610 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5650 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 005b5650 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5650 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5650 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5610 bytes 29812191
+ 005b5650 bytes 29c12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c872399e17b940c74e4a06abdce83b0"></a>

### [`005b56c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b56c0.md) → [`005b5700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5700.md) FUN_005b5700

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b570c",
      "incomplete_value": false,
      "site": "005b570c",
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
      "definition_site": "005b56cc",
      "incomplete_value": false,
      "site": "005b56cc",
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
      "005b570c",
      "DATA",
      [
        "storage",
        "00c6f8e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b570c",
      "DATA",
      [
        "storage",
        "00c6f9b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b56c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b56c0.md#insn-005b56c8)
- 新版 [`005b5708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5700.md#insn-005b5708)

~~~diff
- 005b56c8 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 005b56c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b56c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b56c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5708 ["COPY", "tmp:0:8", ["const:9b0:8"]]
+ 005b5708 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5708 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5708 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b56c8 bytes 29812391
+ 005b5708 bytes 29c12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4678d32e70c2c7e0a3b68515e0b165fc"></a>

### [`005b5710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5710.md) → [`005b5750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5750.md) FUN_005b5750

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5774",
      "incomplete_value": false,
      "site": "005b5774",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5734",
      "incomplete_value": false,
      "site": "005b5734",
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
            "const:960:8"
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
      "005b5774",
      "DATA",
      [
        "storage",
        "00c6f960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5774",
      "DATA",
      [
        "storage",
        "00c6fa30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5710.md#insn-005b5724) · [`005b5730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5710.md#insn-005b5730)
- 新版 [`005b5764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5750.md#insn-005b5764) · [`005b5770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5750.md#insn-005b5770)

~~~diff
- 005b5724 ["INT_ADD", "register:40f0:8", ["const:5b5724:8", "const:4:8"]]
- 005b5724 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b5764 ["INT_ADD", "register:40f0:8", ["const:5b5764:8", "const:4:8"]]
+ 005b5764 ["CALL", null, ["callee:00c57f60:8"]]
- 005b5724 bytes db891a94
+ 005b5764 bytes ff891a94
- 005b5730 ["COPY", "tmp:0:8", ["const:960:8"]]
- 005b5730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5770 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 005b5770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5730 bytes 08812591
+ 005b5770 bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6869351f4ffba25b62868077653bc876"></a>

### [`005b5744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5744.md) → [`005b5784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5784.md) FUN_005b5784

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5790",
      "incomplete_value": false,
      "site": "005b5790",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5750",
      "incomplete_value": false,
      "site": "005b5750",
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
            "const:960:8"
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
      "005b5790",
      "DATA",
      [
        "storage",
        "00c6f960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5790",
      "DATA",
      [
        "storage",
        "00c6fa30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b574c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5744.md#insn-005b574c)
- 新版 [`005b578c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5784.md#insn-005b578c)

~~~diff
- 005b574c ["COPY", "tmp:0:8", ["const:960:8"]]
- 005b574c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b574c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b574c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b578c ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 005b578c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b578c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b578c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b574c bytes 29812591
+ 005b578c bytes 29c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a4a560959b193b47caa0515e94780e7"></a>

### [`005b5814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5814.md) → [`005b5854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5854.md) FUN_005b5854

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`005b5a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a74.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`005b5ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ab4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.60% / 新版 95.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b58d0",
      "incomplete_value": false,
      "site": "005b58d8",
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
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5890",
      "incomplete_value": false,
      "site": "005b5898",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b5880",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b5840",
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
      "005b5880",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "005b58d8",
      "DATA",
      [
        "storage",
        "00c6fa50",
        null,
        "pointer"
      ]
    ],
    [
      "005b5970",
      "READ",
      [
        "storage",
        "00c6fa60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5880",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "005b58d8",
      "DATA",
      [
        "storage",
        "00c6fb20",
        null,
        "pointer"
      ]
    ],
    [
      "005b5970",
      "READ",
      [
        "storage",
        "00c6fb30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5814.md#insn-005b5840) · [`005b5844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5814.md#insn-005b5844) · [`005b5888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5814.md#insn-005b5888)
- 新版 [`005b5880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5854.md#insn-005b5880) · [`005b5884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5854.md#insn-005b5884) · [`005b58c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5854.md#insn-005b58c8)

~~~diff
- 005b5840 ["INT_ADD", "register:40f0:8", ["const:5b5840:8", "const:4:8"]]
- 005b5840 ["CALL", null, ["ram:48ccf8:8"]]
+ 005b5880 ["INT_ADD", "register:40f0:8", ["const:5b5880:8", "const:4:8"]]
+ 005b5880 ["CALL", null, ["ram:48cd38:8"]]
- 005b5840 bytes 2e5dfb97
+ 005b5880 bytes 2e5dfb97
- 005b5844 ["INT_ADD", "register:40f0:8", ["const:5b5844:8", "const:4:8"]]
- 005b5844 ["CALL", null, ["callee:0048e820:8"]]
+ 005b5884 ["INT_ADD", "register:40f0:8", ["const:5b5884:8", "const:4:8"]]
+ 005b5884 ["CALL", null, ["callee:0048e820:8"]]
- 005b5844 bytes e763fb97
+ 005b5884 bytes e763fb97
- 005b5888 ["INT_ADD", "register:40f0:8", ["const:5b5888:8", "const:4:8"]]
- 005b5888 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b58c8 ["INT_ADD", "register:40f0:8", ["const:5b58c8:8", "const:4:8"]]
+ 005b58c8 ["CALL", null, ["callee:00c57f60:8"]]
- 005b5888 bytes 82891a94
+ 005b58c8 bytes a6891a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fdec7664f03b8c5f1861faad742e4e8"></a>

### [`005b5a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a34.md) → [`005b5a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5a74.md) FUN_005b5a74

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
      "definition_site": "005b5a78",
      "incomplete_value": false,
      "site": "005b5a7c",
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
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5a38",
      "incomplete_value": false,
      "site": "005b5a3c",
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
      "005b5a7c",
      "DATA",
      [
        "storage",
        "00c6fa50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b5a7c",
      "DATA",
      [
        "storage",
        "00c6fb20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a34.md#insn-005b5a38)
- 新版 [`005b5a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5a74.md#insn-005b5a78)

~~~diff
- 005b5a38 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 005b5a38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5a38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5a38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5a78 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 005b5a78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5a78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5a78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5a38 bytes 08412991
+ 005b5a78 bytes 08812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a85b963a01f6573896192bb1277b4b31"></a>

### [`005b5a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a44.md) → [`005b5a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5a84.md) FUN_005b5a84

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
      "definition_site": "005b5a94",
      "incomplete_value": false,
      "site": "005b5a9c",
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
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5a54",
      "incomplete_value": false,
      "site": "005b5a5c",
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
      "005b5a9c",
      "DATA",
      [
        "storage",
        "00c6fa50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b5a9c",
      "DATA",
      [
        "storage",
        "00c6fb20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a44.md#insn-005b5a54) · [`005b5a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a44.md#insn-005b5a60)
- 新版 [`005b5a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5a84.md#insn-005b5a94) · [`005b5aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5a84.md#insn-005b5aa0)

~~~diff
- 005b5a54 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 005b5a54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5a54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5a54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5a94 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 005b5a94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5a94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5a94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5a54 bytes 08412991
+ 005b5a94 bytes 08812c91
- 005b5a60 ["INT_ADD", "register:40f0:8", ["const:5b5a60:8", "const:4:8"]]
- 005b5a60 ["CALL", null, ["callee:00c57f70:8"]]
+ 005b5aa0 ["INT_ADD", "register:40f0:8", ["const:5b5aa0:8", "const:4:8"]]
+ 005b5aa0 ["CALL", null, ["callee:00c57f70:8"]]
- 005b5a60 bytes 10891a94
+ 005b5aa0 bytes 34891a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1693d5bd9e8323622bc32f160f10ea9"></a>

### [`005b5a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a90.md) → [`005b5ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ad0.md) FUN_005b5ad0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5af4",
      "incomplete_value": false,
      "site": "005b5af4",
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
      "definition_site": "005b5ab4",
      "incomplete_value": false,
      "site": "005b5ab4",
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
      "005b5af4",
      "DATA",
      [
        "storage",
        "00c6fab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5af4",
      "DATA",
      [
        "storage",
        "00c6fb80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a90.md#insn-005b5aa4) · [`005b5ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5a90.md#insn-005b5ab0)
- 新版 [`005b5ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ad0.md#insn-005b5ae4) · [`005b5af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ad0.md#insn-005b5af0)

~~~diff
- 005b5aa4 ["INT_ADD", "register:40f0:8", ["const:5b5aa4:8", "const:4:8"]]
- 005b5aa4 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b5ae4 ["INT_ADD", "register:40f0:8", ["const:5b5ae4:8", "const:4:8"]]
+ 005b5ae4 ["CALL", null, ["callee:00c57f60:8"]]
- 005b5aa4 bytes fb881a94
+ 005b5ae4 bytes 1f891a94
- 005b5ab0 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 005b5ab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5ab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5ab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5af0 ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 005b5af0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5af0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5af0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5ab0 bytes 08c12a91
+ 005b5af0 bytes 08012e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c68c2e873a518183a9655a91a554d09"></a>

### [`005b5ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ae0.md) → [`005b5b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b20.md) FUN_005b5b20

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`005b22f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b22f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`005b2330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b2330.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

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
      "site": "005b5b3c",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b5afc",
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
      "005b5b3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "005b5b3c",
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

- 旧版 [`005b5afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ae0.md#insn-005b5afc) · [`005b5b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ae0.md#insn-005b5b00)
- 新版 [`005b5b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b20.md#insn-005b5b3c) · [`005b5b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b20.md#insn-005b5b40)

~~~diff
- 005b5afc ["INT_ADD", "register:40f0:8", ["const:5b5afc:8", "const:4:8"]]
- 005b5afc ["CALL", null, ["ram:48ccf8:8"]]
+ 005b5b3c ["INT_ADD", "register:40f0:8", ["const:5b5b3c:8", "const:4:8"]]
+ 005b5b3c ["CALL", null, ["ram:48cd38:8"]]
- 005b5afc bytes 7f5cfb97
+ 005b5b3c bytes 7f5cfb97
- 005b5b00 ["INT_ADD", "register:40f0:8", ["const:5b5b00:8", "const:4:8"]]
- 005b5b00 ["CALL", null, ["callee:0048e820:8"]]
+ 005b5b40 ["INT_ADD", "register:40f0:8", ["const:5b5b40:8", "const:4:8"]]
+ 005b5b40 ["CALL", null, ["callee:0048e820:8"]]
- 005b5b00 bytes 3863fb97
+ 005b5b40 bytes 3863fb97
~~~


<a id="compare-1d5a2e6e3711f7cbbcf1677f1a836dbb"></a>

### [`005b5b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5b54.md) → [`005b5b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b94.md) FUN_005b5b94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5bb4",
      "incomplete_value": false,
      "site": "005b5bb8",
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
      "definition_site": "005b5b74",
      "incomplete_value": false,
      "site": "005b5b78",
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
      "005b5bb8",
      "DATA",
      [
        "storage",
        "00c6fb40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5bb8",
      "DATA",
      [
        "storage",
        "00c6fc10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5b54.md#insn-005b5b68) · [`005b5b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5b54.md#insn-005b5b74)
- 新版 [`005b5ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b94.md#insn-005b5ba8) · [`005b5bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5b94.md#insn-005b5bb4)

~~~diff
- 005b5b68 ["INT_ADD", "register:40f0:8", ["const:5b5b68:8", "const:4:8"]]
- 005b5b68 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b5ba8 ["INT_ADD", "register:40f0:8", ["const:5b5ba8:8", "const:4:8"]]
+ 005b5ba8 ["CALL", null, ["callee:00c57f60:8"]]
- 005b5b68 bytes ca881a94
+ 005b5ba8 bytes ee881a94
- 005b5b74 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 005b5b74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5b74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5b74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5bb4 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 005b5bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5b74 bytes 08012d91
+ 005b5bb4 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-850d20b6cd7bb52e3424d1ebd3bd9e92"></a>

### [`005b5b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5b8c.md) → [`005b5bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5bcc.md) FUN_005b5bcc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5bd0",
      "incomplete_value": false,
      "site": "005b5bd4",
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
      "definition_site": "005b5b90",
      "incomplete_value": false,
      "site": "005b5b94",
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
      "005b5bd4",
      "DATA",
      [
        "storage",
        "00c6fb40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5bd4",
      "DATA",
      [
        "storage",
        "00c6fc10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5b8c.md#insn-005b5b90)
- 新版 [`005b5bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5bcc.md#insn-005b5bd0)

~~~diff
- 005b5b90 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 005b5b90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5b90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5b90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5bd0 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 005b5bd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5bd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5bd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5b90 bytes 08012d91
+ 005b5bd0 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83f49bf75a3a6ab3521aad302aefd015"></a>

### [`005b5bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5bfc.md) → [`005b5c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c3c.md) FUN_005b5c3c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5c60",
      "incomplete_value": false,
      "site": "005b5c60",
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
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5c20",
      "incomplete_value": false,
      "site": "005b5c20",
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
      "005b5c60",
      "DATA",
      [
        "storage",
        "00c6fbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5c60",
      "DATA",
      [
        "storage",
        "00c6fc90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5bfc.md#insn-005b5c10) · [`005b5c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5bfc.md#insn-005b5c1c)
- 新版 [`005b5c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c3c.md#insn-005b5c50) · [`005b5c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c3c.md#insn-005b5c5c)

~~~diff
- 005b5c10 ["INT_ADD", "register:40f0:8", ["const:5b5c10:8", "const:4:8"]]
- 005b5c10 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b5c50 ["INT_ADD", "register:40f0:8", ["const:5b5c50:8", "const:4:8"]]
+ 005b5c50 ["CALL", null, ["callee:00c57f60:8"]]
- 005b5c10 bytes a0881a94
+ 005b5c50 bytes c4881a94
- 005b5c1c ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 005b5c1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5c1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5c1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5c5c ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 005b5c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5c1c bytes 08012f91
+ 005b5c5c bytes 08413291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-716fd141e08d2dae0934560842d7ad6c"></a>

### [`005b5c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c30.md) → [`005b5c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c70.md) FUN_005b5c70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5c7c",
      "incomplete_value": false,
      "site": "005b5c7c",
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
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5c3c",
      "incomplete_value": false,
      "site": "005b5c3c",
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
      "005b5c7c",
      "DATA",
      [
        "storage",
        "00c6fbc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5c7c",
      "DATA",
      [
        "storage",
        "00c6fc90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c30.md#insn-005b5c38)
- 新版 [`005b5c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5c70.md#insn-005b5c78)

~~~diff
- 005b5c38 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 005b5c38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5c38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5c38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5c78 ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 005b5c78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5c78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5c78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5c38 bytes 29012f91
+ 005b5c78 bytes 29413291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc974dba5e724993b7ba700d6c26d642"></a>

### [`005b5c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c90.md) → [`005b5cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5cd0.md) FUN_005b5cd0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5cf4",
      "incomplete_value": false,
      "site": "005b5cf4",
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
      "definition_site": "005b5cb4",
      "incomplete_value": false,
      "site": "005b5cb4",
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
      "005b5cf4",
      "DATA",
      [
        "storage",
        "00c6fc40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5cf4",
      "DATA",
      [
        "storage",
        "00c6fd10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c90.md#insn-005b5ca4) · [`005b5cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5c90.md#insn-005b5cb0)
- 新版 [`005b5ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5cd0.md#insn-005b5ce4) · [`005b5cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5cd0.md#insn-005b5cf0)

~~~diff
- 005b5ca4 ["INT_ADD", "register:40f0:8", ["const:5b5ca4:8", "const:4:8"]]
- 005b5ca4 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b5ce4 ["INT_ADD", "register:40f0:8", ["const:5b5ce4:8", "const:4:8"]]
+ 005b5ce4 ["CALL", null, ["callee:00c57f60:8"]]
- 005b5ca4 bytes 7b881a94
+ 005b5ce4 bytes 9f881a94
- 005b5cb0 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 005b5cb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5cb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5cb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5cf0 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 005b5cf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5cf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5cf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5cb0 bytes 08013191
+ 005b5cf0 bytes 08413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f06146240784e754810827e8b82b732d"></a>

### [`005b5cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5cc4.md) → [`005b5d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5d04.md) FUN_005b5d04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5d10",
      "incomplete_value": false,
      "site": "005b5d10",
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
      "definition_site": "005b5cd0",
      "incomplete_value": false,
      "site": "005b5cd0",
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
      "005b5d10",
      "DATA",
      [
        "storage",
        "00c6fc40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5d10",
      "DATA",
      [
        "storage",
        "00c6fd10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5cc4.md#insn-005b5ccc)
- 新版 [`005b5d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5d04.md#insn-005b5d0c)

~~~diff
- 005b5ccc ["COPY", "tmp:0:8", ["const:c40:8"]]
- 005b5ccc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5ccc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5ccc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5d0c ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 005b5d0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5d0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5d0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5ccc bytes 29013191
+ 005b5d0c bytes 29413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd2575fc82d70cb4c6cd95291d5524e2"></a>

### [`005b5db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5db8.md) → [`005b5df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5df8.md) FUN_005b5df8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5e1c",
      "incomplete_value": false,
      "site": "005b5e1c",
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
      "definition_site": "005b5ddc",
      "incomplete_value": false,
      "site": "005b5ddc",
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
      "005b5e1c",
      "DATA",
      [
        "storage",
        "00c6fcc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5e1c",
      "DATA",
      [
        "storage",
        "00c6fd90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5db8.md#insn-005b5dcc) · [`005b5dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5db8.md#insn-005b5dd8)
- 新版 [`005b5e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5df8.md#insn-005b5e0c) · [`005b5e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5df8.md#insn-005b5e18)

~~~diff
- 005b5dcc ["INT_ADD", "register:40f0:8", ["const:5b5dcc:8", "const:4:8"]]
- 005b5dcc ["CALL", null, ["callee:00c57f60:8"]]
+ 005b5e0c ["INT_ADD", "register:40f0:8", ["const:5b5e0c:8", "const:4:8"]]
+ 005b5e0c ["CALL", null, ["callee:00c57f60:8"]]
- 005b5dcc bytes 31881a94
+ 005b5e0c bytes 55881a94
- 005b5dd8 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 005b5dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5e18 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 005b5e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5dd8 bytes 08013391
+ 005b5e18 bytes 08413691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-193114ed312748f8a58c91533b79cac6"></a>

### [`005b5dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5dec.md) → [`005b5e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5e2c.md) FUN_005b5e2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5e38",
      "incomplete_value": false,
      "site": "005b5e38",
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
      "definition_site": "005b5df8",
      "incomplete_value": false,
      "site": "005b5df8",
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
      "005b5e38",
      "DATA",
      [
        "storage",
        "00c6fcc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5e38",
      "DATA",
      [
        "storage",
        "00c6fd90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5dec.md#insn-005b5df4)
- 新版 [`005b5e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5e2c.md#insn-005b5e34)

~~~diff
- 005b5df4 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 005b5df4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b5df4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b5df4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b5e34 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 005b5e34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5e34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b5e34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b5df4 bytes 29013391
+ 005b5e34 bytes 29413691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de9652e2b4c7fb8771b66152f9b41f00"></a>

### [`005b5e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e50.md) → [`005b5e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5e90.md) FUN_005b5e90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5eb0",
      "incomplete_value": false,
      "site": "005b5eb4",
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
      "definition_site": "005b5e70",
      "incomplete_value": false,
      "site": "005b5e74",
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
      "005b5eb4",
      "DATA",
      [
        "storage",
        "00c6fd40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5eb4",
      "DATA",
      [
        "storage",
        "00c6fe10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e50.md#insn-005b5e64) · [`005b5e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e50.md#insn-005b5e70)
- 新版 [`005b5ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5e90.md#insn-005b5ea4) · [`005b5eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5e90.md#insn-005b5eb0)

~~~diff
- 005b5e64 ["INT_ADD", "register:40f0:8", ["const:5b5e64:8", "const:4:8"]]
- 005b5e64 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b5ea4 ["INT_ADD", "register:40f0:8", ["const:5b5ea4:8", "const:4:8"]]
+ 005b5ea4 ["CALL", null, ["callee:00c57f60:8"]]
- 005b5e64 bytes 0b881a94
+ 005b5ea4 bytes 2f881a94
- 005b5e70 ["COPY", "tmp:0:8", ["const:d40:8"]]
- 005b5e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5eb0 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 005b5eb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5eb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5eb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5e70 bytes 08013591
+ 005b5eb0 bytes 08413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9850b440e51b6f3e7420784065d51908"></a>

### [`005b5e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e88.md) → [`005b5ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ec8.md) FUN_005b5ec8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b5ecc",
      "incomplete_value": false,
      "site": "005b5ed0",
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
      "definition_site": "005b5e8c",
      "incomplete_value": false,
      "site": "005b5e90",
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
      "005b5ed0",
      "DATA",
      [
        "storage",
        "00c6fd40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b5ed0",
      "DATA",
      [
        "storage",
        "00c6fe10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5e88.md#insn-005b5e8c)
- 新版 [`005b5ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ec8.md#insn-005b5ecc)

~~~diff
- 005b5e8c ["COPY", "tmp:0:8", ["const:d40:8"]]
- 005b5e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b5ecc ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 005b5ecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5ecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b5ecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5e8c bytes 08013591
+ 005b5ecc bytes 08413891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c62b84fc394a9836d7eb84a75cc8b13f"></a>

### [`005b5ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ea8.md) → [`005b5ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ee8.md) FUN_005b5ee8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005b3140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3140.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005b3180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3180.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.50% / 新版 97.50%

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
      "site": "005b5f4c",
      "value": [
        "leaf",
        "ram:5b3180:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005b5f0c",
      "value": [
        "leaf",
        "ram:5b3140:8"
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
      "005b5f4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005b3140"
      ]
    ]
  ],
  "added": [
    [
      "005b5f4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005b3180"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ea8.md#insn-005b5f0c) · [`005b5efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ea8.md#insn-005b5efc) · [`005b5f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5ea8.md#insn-005b5f1c)
- 新版 [`005b5f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ee8.md#insn-005b5f4c) · [`005b5f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ee8.md#insn-005b5f3c) · [`005b5f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5ee8.md#insn-005b5f5c)

~~~diff
- 005b5f0c ["INT_ADD", "register:40f0:8", ["const:5b5f0c:8", "const:4:8"]]
- 005b5f0c ["CALL", null, ["ram:5b3140:8"]]
+ 005b5f4c ["INT_ADD", "register:40f0:8", ["const:5b5f4c:8", "const:4:8"]]
+ 005b5f4c ["CALL", null, ["ram:5b3180:8"]]
- 005b5f0c bytes 8df4ff97
+ 005b5f4c bytes 8df4ff97
- 005b5efc ["INT_ADD", "register:40f0:8", ["const:5b5efc:8", "const:4:8"]]
- 005b5efc ["CALL", null, ["callee:0043bb60:8"]]
+ 005b5f3c ["INT_ADD", "register:40f0:8", ["const:5b5f3c:8", "const:4:8"]]
+ 005b5f3c ["CALL", null, ["callee:0043bb60:8"]]
- 005b5efc bytes 0917fa97
+ 005b5f3c bytes 0917fa97
- 005b5f1c ["INT_ADD", "register:40f0:8", ["const:5b5f1c:8", "const:4:8"]]
- 005b5f1c ["CALL", null, ["callee:00c57f80:8"]]
+ 005b5f5c ["INT_ADD", "register:40f0:8", ["const:5b5f5c:8", "const:4:8"]]
+ 005b5f5c ["CALL", null, ["callee:00c57f80:8"]]
- 005b5f1c bytes e5871a94
+ 005b5f5c bytes 09881a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-311a6670a7966c6d6817beaf6ff14a76"></a>

### [`005b5fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5fa4.md) → [`005b5fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5fe4.md) FUN_005b5fe4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6004",
      "incomplete_value": false,
      "site": "005b6008",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b5fc4",
      "incomplete_value": false,
      "site": "005b5fc8",
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
            "const:dd0:8"
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
      "005b6008",
      "DATA",
      [
        "storage",
        "00c6fdd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6008",
      "DATA",
      [
        "storage",
        "00c6fea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b5fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5fa4.md#insn-005b5fb8) · [`005b5fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5fa4.md#insn-005b5fc4)
- 新版 [`005b5ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5fe4.md#insn-005b5ff8) · [`005b6004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5fe4.md#insn-005b6004)

~~~diff
- 005b5fb8 ["INT_ADD", "register:40f0:8", ["const:5b5fb8:8", "const:4:8"]]
- 005b5fb8 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b5ff8 ["INT_ADD", "register:40f0:8", ["const:5b5ff8:8", "const:4:8"]]
+ 005b5ff8 ["CALL", null, ["callee:00c57f60:8"]]
- 005b5fb8 bytes b6871a94
+ 005b5ff8 bytes da871a94
- 005b5fc4 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 005b5fc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b5fc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b5fc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6004 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 005b6004 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6004 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6004 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b5fc4 bytes 08413791
+ 005b6004 bytes 08813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34b57556b203af1da012804383084e73"></a>

### [`005b610c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b610c.md) → [`005b614c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b614c.md) FUN_005b614c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b616c",
      "incomplete_value": false,
      "site": "005b6170",
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
      "definition_site": "005b612c",
      "incomplete_value": false,
      "site": "005b6130",
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
      "005b6170",
      "DATA",
      [
        "storage",
        "00c6fe60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6170",
      "DATA",
      [
        "storage",
        "00c6ff30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b610c.md#insn-005b6120) · [`005b612c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b610c.md#insn-005b612c)
- 新版 [`005b6160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b614c.md#insn-005b6160) · [`005b616c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b614c.md#insn-005b616c)

~~~diff
- 005b6120 ["INT_ADD", "register:40f0:8", ["const:5b6120:8", "const:4:8"]]
- 005b6120 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b6160 ["INT_ADD", "register:40f0:8", ["const:5b6160:8", "const:4:8"]]
+ 005b6160 ["CALL", null, ["callee:00c57f60:8"]]
- 005b6120 bytes 5c871a94
+ 005b6160 bytes 80871a94
- 005b612c ["COPY", "tmp:0:8", ["const:e60:8"]]
- 005b612c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b612c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b612c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b616c ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 005b616c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b616c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b616c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b612c bytes 08813991
+ 005b616c bytes 08c13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94f6902eb9475f882d64c36b691fa04b"></a>

### [`005b6144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6144.md) → [`005b6184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6184.md) FUN_005b6184

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6188",
      "incomplete_value": false,
      "site": "005b618c",
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
      "definition_site": "005b6148",
      "incomplete_value": false,
      "site": "005b614c",
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
      "005b618c",
      "DATA",
      [
        "storage",
        "00c6fe60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b618c",
      "DATA",
      [
        "storage",
        "00c6ff30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6144.md#insn-005b6148)
- 新版 [`005b6188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6184.md#insn-005b6188)

~~~diff
- 005b6148 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 005b6148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6188 ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 005b6188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6148 bytes 08813991
+ 005b6188 bytes 08c13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d49d5a2ded22d880c79581fb9499aa4"></a>

### [`005b61a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b61a4.md) → [`005b61e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b61e4.md) FUN_005b61e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6208",
      "incomplete_value": false,
      "site": "005b6208",
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
      "definition_site": "005b61c8",
      "incomplete_value": false,
      "site": "005b61c8",
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
      "005b6208",
      "DATA",
      [
        "storage",
        "00c6fee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6208",
      "DATA",
      [
        "storage",
        "00c6ffb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b61b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b61a4.md#insn-005b61b8) · [`005b61c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b61a4.md#insn-005b61c4)
- 新版 [`005b61f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b61e4.md#insn-005b61f8) · [`005b6204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b61e4.md#insn-005b6204)

~~~diff
- 005b61b8 ["INT_ADD", "register:40f0:8", ["const:5b61b8:8", "const:4:8"]]
- 005b61b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b61f8 ["INT_ADD", "register:40f0:8", ["const:5b61f8:8", "const:4:8"]]
+ 005b61f8 ["CALL", null, ["callee:00c57f60:8"]]
- 005b61b8 bytes 36871a94
+ 005b61f8 bytes 5a871a94
- 005b61c4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 005b61c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b61c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b61c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6204 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 005b6204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b61c4 bytes 08813b91
+ 005b6204 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e50ced2103d03253b93458fdb18215ad"></a>

### [`005b61d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b61d8.md) → [`005b6218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6218.md) FUN_005b6218

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6224",
      "incomplete_value": false,
      "site": "005b6224",
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
      "definition_site": "005b61e4",
      "incomplete_value": false,
      "site": "005b61e4",
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
      "005b6224",
      "DATA",
      [
        "storage",
        "00c6fee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6224",
      "DATA",
      [
        "storage",
        "00c6ffb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b61e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b61d8.md#insn-005b61e0)
- 新版 [`005b6220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6218.md#insn-005b6220)

~~~diff
- 005b61e0 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 005b61e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b61e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b61e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6220 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 005b6220 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6220 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6220 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b61e0 bytes 29813b91
+ 005b6220 bytes 29c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaf3b655abf8c21b8dc542c7e31ce094"></a>

### [`005b6258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6258.md) → [`005b6298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6298.md) FUN_005b6298

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b62bc",
      "incomplete_value": false,
      "site": "005b62bc",
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
      "definition_site": "005b627c",
      "incomplete_value": false,
      "site": "005b627c",
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
      "005b62bc",
      "DATA",
      [
        "storage",
        "00c6ff60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b62bc",
      "DATA",
      [
        "storage",
        "00c70030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b626c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6258.md#insn-005b626c) · [`005b6274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6258.md#insn-005b6274) · [`005b6278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6258.md#insn-005b6278)
- 新版 [`005b62ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6298.md#insn-005b62ac) · [`005b62b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6298.md#insn-005b62b4) · [`005b62b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6298.md#insn-005b62b8)

~~~diff
- 005b626c ["INT_ADD", "register:40f0:8", ["const:5b626c:8", "const:4:8"]]
- 005b626c ["CALL", null, ["callee:00c57f60:8"]]
+ 005b62ac ["INT_ADD", "register:40f0:8", ["const:5b62ac:8", "const:4:8"]]
+ 005b62ac ["CALL", null, ["callee:00c57f60:8"]]
- 005b626c bytes 09871a94
+ 005b62ac bytes 2d871a94
- 005b6274 ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b62b4 ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b6274 bytes c83500b0
+ 005b62b4 bytes c83500d0
- 005b6278 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 005b6278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b62b8 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 005b62b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b62b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b62b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6278 bytes 08813d91
+ 005b62b8 bytes 08c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36f58aa9a53b1dbd6221fb76e44e89d8"></a>

### [`005b628c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b628c.md) → [`005b62cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b62cc.md) FUN_005b62cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b62d8",
      "incomplete_value": false,
      "site": "005b62d8",
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
      "definition_site": "005b6298",
      "incomplete_value": false,
      "site": "005b6298",
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
      "005b62d8",
      "DATA",
      [
        "storage",
        "00c6ff60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b62d8",
      "DATA",
      [
        "storage",
        "00c70030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b628c.md#insn-005b6290) · [`005b6294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b628c.md#insn-005b6294)
- 新版 [`005b62d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b62cc.md#insn-005b62d0) · [`005b62d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b62cc.md#insn-005b62d4)

~~~diff
- 005b6290 ["COPY", "register:4048:8", ["const:c6f000:8"]]
+ 005b62d0 ["COPY", "register:4048:8", ["const:c70000:8"]]
- 005b6290 bytes c93500b0
+ 005b62d0 bytes c93500d0
- 005b6294 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 005b6294 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6294 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6294 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b62d4 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 005b62d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b62d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b62d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6294 bytes 29813d91
+ 005b62d4 bytes 29c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fadd6a08fda3a55efe06157f88033316"></a>

### [`005b6380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6380.md) → [`005b63c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63c0.md) FUN_005b63c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b63e4",
      "incomplete_value": false,
      "site": "005b63e4",
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
      "definition_site": "005b63a4",
      "incomplete_value": false,
      "site": "005b63a4",
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
      "005b63e4",
      "DATA",
      [
        "storage",
        "00c6ffe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b63e4",
      "DATA",
      [
        "storage",
        "00c700b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6380.md#insn-005b6394) · [`005b639c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6380.md#insn-005b639c) · [`005b63a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6380.md#insn-005b63a0)
- 新版 [`005b63d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63c0.md#insn-005b63d4) · [`005b63dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63c0.md#insn-005b63dc) · [`005b63e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63c0.md#insn-005b63e0)

~~~diff
- 005b6394 ["INT_ADD", "register:40f0:8", ["const:5b6394:8", "const:4:8"]]
- 005b6394 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b63d4 ["INT_ADD", "register:40f0:8", ["const:5b63d4:8", "const:4:8"]]
+ 005b63d4 ["CALL", null, ["callee:00c57f60:8"]]
- 005b6394 bytes bf861a94
+ 005b63d4 bytes e3861a94
- 005b639c ["COPY", "register:4040:8", ["const:c6f000:8"]]
+ 005b63dc ["COPY", "register:4040:8", ["const:c70000:8"]]
- 005b639c bytes c83500b0
+ 005b63dc bytes c83500d0
- 005b63a0 ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 005b63a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b63a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b63a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b63e0 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 005b63e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b63e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b63e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b63a0 bytes 08813f91
+ 005b63e0 bytes 08c10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b26e82a46ebfb9b442fdec66e5ad573"></a>

### [`005b63b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b63b4.md) → [`005b63f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63f4.md) FUN_005b63f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6400",
      "incomplete_value": false,
      "site": "005b6400",
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
      "definition_site": "005b63c0",
      "incomplete_value": false,
      "site": "005b63c0",
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
      "005b6400",
      "DATA",
      [
        "storage",
        "00c6ffe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6400",
      "DATA",
      [
        "storage",
        "00c700b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b63b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b63b4.md#insn-005b63b8) · [`005b63bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b63b4.md#insn-005b63bc)
- 新版 [`005b63f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63f4.md#insn-005b63f8) · [`005b63fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b63f4.md#insn-005b63fc)

~~~diff
- 005b63b8 ["COPY", "register:4048:8", ["const:c6f000:8"]]
+ 005b63f8 ["COPY", "register:4048:8", ["const:c70000:8"]]
- 005b63b8 bytes c93500b0
+ 005b63f8 bytes c93500d0
- 005b63bc ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 005b63bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b63bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b63bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b63fc ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 005b63fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b63fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b63fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b63bc bytes 29813f91
+ 005b63fc bytes 29c10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-852d73084d2a0beb0c61c84a2c384b3a"></a>

### [`005b6418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6418.md) → [`005b6458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6458.md) FUN_005b6458

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b647c",
      "incomplete_value": false,
      "site": "005b647c",
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
      "definition_site": "005b643c",
      "incomplete_value": false,
      "site": "005b643c",
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
      "005b647c",
      "DATA",
      [
        "storage",
        "00c70060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b647c",
      "DATA",
      [
        "storage",
        "00c70130",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b642c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6418.md#insn-005b642c) · [`005b6438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6418.md#insn-005b6438)
- 新版 [`005b646c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6458.md#insn-005b646c) · [`005b6478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6458.md#insn-005b6478)

~~~diff
- 005b642c ["INT_ADD", "register:40f0:8", ["const:5b642c:8", "const:4:8"]]
- 005b642c ["CALL", null, ["callee:00c57f60:8"]]
+ 005b646c ["INT_ADD", "register:40f0:8", ["const:5b646c:8", "const:4:8"]]
+ 005b646c ["CALL", null, ["callee:00c57f60:8"]]
- 005b642c bytes 99861a94
+ 005b646c bytes bd861a94
- 005b6438 ["COPY", "tmp:0:8", ["const:60:8"]]
- 005b6438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6478 ["COPY", "tmp:0:8", ["const:130:8"]]
+ 005b6478 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6478 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6478 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6438 bytes 08810191
+ 005b6478 bytes 08c10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daf161a1ec1dad9b0a5a72b644305e52"></a>

### [`005b644c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b644c.md) → [`005b648c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b648c.md) FUN_005b648c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6498",
      "incomplete_value": false,
      "site": "005b6498",
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
      "definition_site": "005b6458",
      "incomplete_value": false,
      "site": "005b6458",
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
      "005b6498",
      "DATA",
      [
        "storage",
        "00c70060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6498",
      "DATA",
      [
        "storage",
        "00c70130",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b644c.md#insn-005b6454)
- 新版 [`005b6494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b648c.md#insn-005b6494)

~~~diff
- 005b6454 ["COPY", "tmp:0:8", ["const:60:8"]]
- 005b6454 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6454 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6454 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6494 ["COPY", "tmp:0:8", ["const:130:8"]]
+ 005b6494 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6494 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6494 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6454 bytes 29810191
+ 005b6494 bytes 29c10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-511ba7e0cfeffd390c94f748c989877f"></a>

### [`005b6468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6468.md) → [`005b64a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b64a8.md) FUN_005b64a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0053f018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f018.md) [`005b668c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b668c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0053f058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f058.md) [`005b66cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b66cc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b6524",
      "incomplete_value": false,
      "site": "005b653c",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b64e4",
      "incomplete_value": false,
      "site": "005b64fc",
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
            "const:e0:8"
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
      "005b653c",
      "DATA",
      [
        "storage",
        "00c700e0",
        null,
        "pointer"
      ]
    ],
    [
      "005b65a0",
      "READ",
      [
        "storage",
        "00c700f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b653c",
      "DATA",
      [
        "storage",
        "00c701b0",
        null,
        "pointer"
      ]
    ],
    [
      "005b65a0",
      "READ",
      [
        "storage",
        "00c701c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b64d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6468.md#insn-005b64d0) · [`005b64e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6468.md#insn-005b64e4) · [`005b6528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6468.md#insn-005b6528)
- 新版 [`005b6510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b64a8.md#insn-005b6510) · [`005b6524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b64a8.md#insn-005b6524) · [`005b6568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b64a8.md#insn-005b6568)

~~~diff
- 005b64d0 ["INT_ADD", "register:40f0:8", ["const:5b64d0:8", "const:4:8"]]
- 005b64d0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b6510 ["INT_ADD", "register:40f0:8", ["const:5b6510:8", "const:4:8"]]
+ 005b6510 ["CALL", null, ["callee:00c57f60:8"]]
- 005b64d0 bytes 70861a94
+ 005b6510 bytes 94861a94
- 005b64e4 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 005b64e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b64e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b64e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6524 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 005b6524 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6524 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6524 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b64e4 bytes 29810391
+ 005b6524 bytes 29c10691
- 005b6528 ["INT_ADD", "register:40f0:8", ["const:5b6528:8", "const:4:8"]]
- 005b6528 ["CALL", null, ["callee:0053f058:8"]]
+ 005b6568 ["INT_ADD", "register:40f0:8", ["const:5b6568:8", "const:4:8"]]
+ 005b6568 ["CALL", null, ["callee:0053f058:8"]]
- 005b6528 bytes bc22fe97
+ 005b6568 bytes bc22fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-485a394b649c7e664f065d8aac0f1678"></a>

### [`005b664c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b664c.md) → [`005b668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b668c.md) FUN_005b668c

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
      "definition_site": "005b6690",
      "incomplete_value": false,
      "site": "005b6694",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6650",
      "incomplete_value": false,
      "site": "005b6654",
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
            "const:e0:8"
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
      "005b6694",
      "DATA",
      [
        "storage",
        "00c700e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b6694",
      "DATA",
      [
        "storage",
        "00c701b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b664c.md#insn-005b6650)
- 新版 [`005b6690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b668c.md#insn-005b6690)

~~~diff
- 005b6650 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 005b6650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6690 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 005b6690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6650 bytes 08810391
+ 005b6690 bytes 08c10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f55840bd9876b728ae91a377b8801655"></a>

### [`005b665c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b665c.md) → [`005b669c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b669c.md) FUN_005b669c

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
      "definition_site": "005b66ac",
      "incomplete_value": false,
      "site": "005b66b4",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b666c",
      "incomplete_value": false,
      "site": "005b6674",
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
            "const:e0:8"
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
      "005b66b4",
      "DATA",
      [
        "storage",
        "00c700e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b66b4",
      "DATA",
      [
        "storage",
        "00c701b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b666c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b665c.md#insn-005b666c) · [`005b6678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b665c.md#insn-005b6678)
- 新版 [`005b66ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b669c.md#insn-005b66ac) · [`005b66b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b669c.md#insn-005b66b8)

~~~diff
- 005b666c ["COPY", "tmp:0:8", ["const:e0:8"]]
- 005b666c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b666c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b666c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b66ac ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 005b66ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b66ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b66ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b666c bytes 08810391
+ 005b66ac bytes 08c10691
- 005b6678 ["INT_ADD", "register:40f0:8", ["const:5b6678:8", "const:4:8"]]
- 005b6678 ["CALL", null, ["callee:00c57f70:8"]]
+ 005b66b8 ["INT_ADD", "register:40f0:8", ["const:5b66b8:8", "const:4:8"]]
+ 005b66b8 ["CALL", null, ["callee:00c57f70:8"]]
- 005b6678 bytes 0a861a94
+ 005b66b8 bytes 2e861a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a32735ea9e46c1176cb86719f99a5b1"></a>

### [`005b6710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6710.md) → [`005b6750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6750.md) FUN_005b6750

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6774",
      "incomplete_value": false,
      "site": "005b6774",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6734",
      "incomplete_value": false,
      "site": "005b6734",
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
            "const:140:8"
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
      "005b6774",
      "DATA",
      [
        "storage",
        "00c70140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6774",
      "DATA",
      [
        "storage",
        "00c70210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6710.md#insn-005b6724) · [`005b6730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6710.md#insn-005b6730)
- 新版 [`005b6764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6750.md#insn-005b6764) · [`005b6770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6750.md#insn-005b6770)

~~~diff
- 005b6724 ["INT_ADD", "register:40f0:8", ["const:5b6724:8", "const:4:8"]]
- 005b6724 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b6764 ["INT_ADD", "register:40f0:8", ["const:5b6764:8", "const:4:8"]]
+ 005b6764 ["CALL", null, ["callee:00c57f60:8"]]
- 005b6724 bytes db851a94
+ 005b6764 bytes ff851a94
- 005b6730 ["COPY", "tmp:0:8", ["const:140:8"]]
- 005b6730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6770 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 005b6770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6730 bytes 08010591
+ 005b6770 bytes 08410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f320c419bdd83f6f2c44c03d99ea48bf"></a>

### [`005b6744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6744.md) → [`005b6784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6784.md) FUN_005b6784

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6790",
      "incomplete_value": false,
      "site": "005b6790",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6750",
      "incomplete_value": false,
      "site": "005b6750",
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
            "const:140:8"
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
      "005b6790",
      "DATA",
      [
        "storage",
        "00c70140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6790",
      "DATA",
      [
        "storage",
        "00c70210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6744.md#insn-005b674c)
- 新版 [`005b678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6784.md#insn-005b678c)

~~~diff
- 005b674c ["COPY", "tmp:0:8", ["const:140:8"]]
- 005b674c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b674c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b674c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b678c ["COPY", "tmp:0:8", ["const:210:8"]]
+ 005b678c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b678c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b678c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b674c bytes 29010591
+ 005b678c bytes 29410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a08659f146ed49f87de8ee6720e816ea"></a>

### [`005b67a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67a8.md) → [`005b67e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b67e8.md) FUN_005b67e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b680c",
      "incomplete_value": false,
      "site": "005b680c",
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
      "definition_site": "005b67cc",
      "incomplete_value": false,
      "site": "005b67cc",
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
      "005b680c",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b680c",
      "DATA",
      [
        "storage",
        "00c70290",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b67bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67a8.md#insn-005b67bc) · [`005b67c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67a8.md#insn-005b67c8)
- 新版 [`005b67fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b67e8.md#insn-005b67fc) · [`005b6808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b67e8.md#insn-005b6808)

~~~diff
- 005b67bc ["INT_ADD", "register:40f0:8", ["const:5b67bc:8", "const:4:8"]]
- 005b67bc ["CALL", null, ["callee:00c57f60:8"]]
+ 005b67fc ["INT_ADD", "register:40f0:8", ["const:5b67fc:8", "const:4:8"]]
+ 005b67fc ["CALL", null, ["callee:00c57f60:8"]]
- 005b67bc bytes b5851a94
+ 005b67fc bytes d9851a94
- 005b67c8 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 005b67c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b67c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b67c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6808 ["COPY", "tmp:0:8", ["const:290:8"]]
+ 005b6808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b67c8 bytes 08010791
+ 005b6808 bytes 08410a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3949321e570269e76c726ab16c9da3c"></a>

### [`005b67dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67dc.md) → [`005b681c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b681c.md) FUN_005b681c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6828",
      "incomplete_value": false,
      "site": "005b6828",
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
      "definition_site": "005b67e8",
      "incomplete_value": false,
      "site": "005b67e8",
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
      "005b6828",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6828",
      "DATA",
      [
        "storage",
        "00c70290",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b67e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b67dc.md#insn-005b67e4)
- 新版 [`005b6824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b681c.md#insn-005b6824)

~~~diff
- 005b67e4 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 005b67e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b67e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b67e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6824 ["COPY", "tmp:0:8", ["const:290:8"]]
+ 005b6824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b67e4 bytes 29010791
+ 005b6824 bytes 29410a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f21bf67cd3bf5c273895b9a4a1bde396"></a>

### [`005b6830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6830.md) → [`005b6870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6870.md) FUN_005b6870

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6894",
      "incomplete_value": false,
      "site": "005b6894",
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
      "definition_site": "005b6854",
      "incomplete_value": false,
      "site": "005b6854",
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
      "005b6894",
      "DATA",
      [
        "storage",
        "00c70250",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6894",
      "DATA",
      [
        "storage",
        "00c70320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6830.md#insn-005b6844) · [`005b6850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6830.md#insn-005b6850)
- 新版 [`005b6884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6870.md#insn-005b6884) · [`005b6890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6870.md#insn-005b6890)

~~~diff
- 005b6844 ["INT_ADD", "register:40f0:8", ["const:5b6844:8", "const:4:8"]]
- 005b6844 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b6884 ["INT_ADD", "register:40f0:8", ["const:5b6884:8", "const:4:8"]]
+ 005b6884 ["CALL", null, ["callee:00c57f60:8"]]
- 005b6844 bytes 93851a94
+ 005b6884 bytes b7851a94
- 005b6850 ["COPY", "tmp:0:8", ["const:250:8"]]
- 005b6850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6890 ["COPY", "tmp:0:8", ["const:320:8"]]
+ 005b6890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6850 bytes 08410991
+ 005b6890 bytes 08810c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a5557f734a57c430ac6f30d4783c484"></a>

### [`005b6864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6864.md) → [`005b68a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b68a4.md) FUN_005b68a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b68b0",
      "incomplete_value": false,
      "site": "005b68b0",
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
      "definition_site": "005b6870",
      "incomplete_value": false,
      "site": "005b6870",
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
      "005b68b0",
      "DATA",
      [
        "storage",
        "00c70250",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b68b0",
      "DATA",
      [
        "storage",
        "00c70320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b686c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6864.md#insn-005b686c)
- 新版 [`005b68ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b68a4.md#insn-005b68ac)

~~~diff
- 005b686c ["COPY", "tmp:0:8", ["const:250:8"]]
- 005b686c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b686c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b686c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b68ac ["COPY", "tmp:0:8", ["const:320:8"]]
+ 005b68ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b68ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b68ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b686c bytes 29410991
+ 005b68ac bytes 29810c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e38622a449d8a837728d844e4eea90b3"></a>

### [`005b68c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b68c8.md) → [`005b6908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6908.md) FUN_005b6908

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b692c",
      "incomplete_value": false,
      "site": "005b692c",
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
      "definition_site": "005b68ec",
      "incomplete_value": false,
      "site": "005b68ec",
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
      "005b692c",
      "DATA",
      [
        "storage",
        "00c702d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b692c",
      "DATA",
      [
        "storage",
        "00c703a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b68dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b68c8.md#insn-005b68dc) · [`005b68e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b68c8.md#insn-005b68e8)
- 新版 [`005b691c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6908.md#insn-005b691c) · [`005b6928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6908.md#insn-005b6928)

~~~diff
- 005b68dc ["INT_ADD", "register:40f0:8", ["const:5b68dc:8", "const:4:8"]]
- 005b68dc ["CALL", null, ["callee:00c57f60:8"]]
+ 005b691c ["INT_ADD", "register:40f0:8", ["const:5b691c:8", "const:4:8"]]
+ 005b691c ["CALL", null, ["callee:00c57f60:8"]]
- 005b68dc bytes 6d851a94
+ 005b691c bytes 91851a94
- 005b68e8 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 005b68e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b68e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b68e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6928 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 005b6928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b68e8 bytes 08410b91
+ 005b6928 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74386568084c166dc3a63c47aa09fd6f"></a>

### [`005b68fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b68fc.md) → [`005b693c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b693c.md) FUN_005b693c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6948",
      "incomplete_value": false,
      "site": "005b6948",
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
      "definition_site": "005b6908",
      "incomplete_value": false,
      "site": "005b6908",
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
      "005b6948",
      "DATA",
      [
        "storage",
        "00c702d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6948",
      "DATA",
      [
        "storage",
        "00c703a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b68fc.md#insn-005b6904)
- 新版 [`005b6944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b693c.md#insn-005b6944)

~~~diff
- 005b6904 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 005b6904 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6904 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6904 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6944 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 005b6944 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6944 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6944 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6904 bytes 29410b91
+ 005b6944 bytes 29810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51adade5d066d9bf625f242392fa0b97"></a>

### [`005b6918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6918.md) → [`005b6958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6958.md) FUN_005b6958

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005b0bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b0/005b0bdc.md) [`005b5214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b5/005b5214.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`005b0c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b0/005b0c1c.md) [`005b5254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b5/005b5254.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.95% / 新版 87.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b69a4",
      "incomplete_value": true,
      "site": "005b69b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6964",
      "incomplete_value": true,
      "site": "005b6970",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec0:8"
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
      "definition_site": "005b69a0",
      "incomplete_value": true,
      "site": "005b69b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dee:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6960",
      "incomplete_value": true,
      "site": "005b6974",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dbf:8"
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
      "definition_site": "005b69a0",
      "incomplete_value": true,
      "site": "005b69b4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "005b6960",
      "incomplete_value": true,
      "site": "005b6974",
      "value": [
        "LOAD",
        "16",
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
      "005b69a0",
      "READ",
      [
        "storage",
        "002a8dbf",
        null,
        null
      ]
    ],
    [
      "005b69a0",
      "READ",
      [
        "storage",
        "002a8dcf",
        null,
        null
      ]
    ],
    [
      "005b69a4",
      "READ",
      [
        "storage",
        "002c2ec0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005b69a0",
      "READ",
      [
        "storage",
        "002a8dee",
        null,
        null
      ]
    ],
    [
      "005b69a0",
      "READ",
      [
        "storage",
        "002a8dfe",
        null,
        null
      ]
    ],
    [
      "005b69a4",
      "READ",
      [
        "storage",
        "002c2f00",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6918.md#insn-005b6964) · [`005b69b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6918.md#insn-005b69b8) · [`005b6950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6918.md#insn-005b6950)
- 新版 [`005b69a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6958.md#insn-005b69a4) · [`005b69f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6958.md#insn-005b69f8) · [`005b6990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6958.md#insn-005b6990)

~~~diff
- 005b6964 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ec0:8"]]
- 005b6964 ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
- 005b6964 ["COPY", "register:5050:8", ["const:0:8"]]
- 005b6964 ["COPY", "register:5058:8", ["const:0:8"]]
+ 005b69a4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f00:8"]]
+ 005b69a4 ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
+ 005b69a4 ["COPY", "register:5050:8", ["const:0:8"]]
+ 005b69a4 ["COPY", "register:5058:8", ["const:0:8"]]
- 005b6964 bytes 22b1c33d
+ 005b69a4 bytes 22c1c33d
- 005b69b8 ["INT_ADD", "register:40f0:8", ["const:5b69b8:8", "const:4:8"]]
- 005b69b8 ["CALL", null, ["callee:005b0c1c:8"]]
+ 005b69f8 ["INT_ADD", "register:40f0:8", ["const:5b69f8:8", "const:4:8"]]
+ 005b69f8 ["CALL", null, ["callee:005b0c1c:8"]]
- 005b69b8 bytes 89e8ff97
+ 005b69f8 bytes 89e8ff97
- 005b6950 ["INT_ADD", "register:40f0:8", ["const:5b6950:8", "const:4:8"]]
- 005b6950 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b6990 ["INT_ADD", "register:40f0:8", ["const:5b6990:8", "const:4:8"]]
+ 005b6990 ["CALL", null, ["callee:00c57f60:8"]]
- 005b6950 bytes 50851a94
+ 005b6990 bytes 74851a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34526b699774027fed3ed9bcae1d498f"></a>

### [`005b6ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6ae8.md) → [`005b6b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b28.md) FUN_005b6b28

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6b4c",
      "incomplete_value": false,
      "site": "005b6b4c",
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
      "definition_site": "005b6b0c",
      "incomplete_value": false,
      "site": "005b6b0c",
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
      "005b6b4c",
      "DATA",
      [
        "storage",
        "00c70360",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6b4c",
      "DATA",
      [
        "storage",
        "00c70430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6ae8.md#insn-005b6afc) · [`005b6b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6ae8.md#insn-005b6b08)
- 新版 [`005b6b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b28.md#insn-005b6b3c) · [`005b6b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b28.md#insn-005b6b48)

~~~diff
- 005b6afc ["INT_ADD", "register:40f0:8", ["const:5b6afc:8", "const:4:8"]]
- 005b6afc ["CALL", null, ["callee:00c57f60:8"]]
+ 005b6b3c ["INT_ADD", "register:40f0:8", ["const:5b6b3c:8", "const:4:8"]]
+ 005b6b3c ["CALL", null, ["callee:00c57f60:8"]]
- 005b6afc bytes e5841a94
+ 005b6b3c bytes 09851a94
- 005b6b08 ["COPY", "tmp:0:8", ["const:360:8"]]
- 005b6b08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6b08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6b08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6b48 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 005b6b48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6b48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6b48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6b08 bytes 08810d91
+ 005b6b48 bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-328200b4bee9e7f83e3ef93db7f943e9"></a>

### [`005b6b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6b1c.md) → [`005b6b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b5c.md) FUN_005b6b5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6b68",
      "incomplete_value": false,
      "site": "005b6b68",
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
      "definition_site": "005b6b28",
      "incomplete_value": false,
      "site": "005b6b28",
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
      "005b6b68",
      "DATA",
      [
        "storage",
        "00c70360",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6b68",
      "DATA",
      [
        "storage",
        "00c70430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6b1c.md#insn-005b6b24)
- 新版 [`005b6b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b5c.md#insn-005b6b64)

~~~diff
- 005b6b24 ["COPY", "tmp:0:8", ["const:360:8"]]
- 005b6b24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6b24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6b24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6b64 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 005b6b64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6b64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6b64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6b24 bytes 29810d91
+ 005b6b64 bytes 29c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50b3c8d0b1f0747d41ab02004c1759e2"></a>

### [`005b6b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6b38.md) → [`005b6b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b78.md) FUN_005b6b78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005b6dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6dec.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`005b6e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6e2c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b6bfc",
      "incomplete_value": false,
      "site": "005b6c04",
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
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6bbc",
      "incomplete_value": false,
      "site": "005b6bc4",
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
            "const:3e0:8"
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
      "005b6c04",
      "DATA",
      [
        "storage",
        "00c703e0",
        null,
        "pointer"
      ]
    ],
    [
      "005b6cfc",
      "READ",
      [
        "storage",
        "00c703f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b6c04",
      "DATA",
      [
        "storage",
        "00c704b0",
        null,
        "pointer"
      ]
    ],
    [
      "005b6cfc",
      "READ",
      [
        "storage",
        "00c704c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6b38.md#insn-005b6bac) · [`005b6bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6b38.md#insn-005b6bbc) · [`005b6bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6b38.md#insn-005b6bc0)
- 新版 [`005b6bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b78.md#insn-005b6bec) · [`005b6bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6b78.md#insn-005b6bfc)

~~~diff
- 005b6bac ["INT_ADD", "register:40f0:8", ["const:5b6bac:8", "const:4:8"]]
- 005b6bac ["CALL", null, ["callee:00c57f60:8"]]
+ 005b6bec ["INT_ADD", "register:40f0:8", ["const:5b6bec:8", "const:4:8"]]
+ 005b6bec ["CALL", null, ["callee:00c57f60:8"]]
- 005b6bac bytes b9841a94
+ 005b6bec bytes dd841a94
- 005b6bbc ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 005b6bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6bfc ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 005b6bfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6bfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6bfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6bbc bytes 08810f91
+ 005b6bfc bytes 08c11291
- 005b6bc0 ["COPY", "register:40b0:8", ["register:4000:8"]]
- 005b6bc0 bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee490acc220ba76dcfaeb9e4e30d3b40"></a>

### [`005b6dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6dac.md) → [`005b6dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6dec.md) FUN_005b6dec

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
      "definition_site": "005b6df0",
      "incomplete_value": false,
      "site": "005b6df4",
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
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6db0",
      "incomplete_value": false,
      "site": "005b6db4",
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
            "const:3e0:8"
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
      "005b6df4",
      "DATA",
      [
        "storage",
        "00c703e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b6df4",
      "DATA",
      [
        "storage",
        "00c704b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6dac.md#insn-005b6db0)
- 新版 [`005b6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6dec.md#insn-005b6df0)

~~~diff
- 005b6db0 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 005b6db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6df0 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 005b6df0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6df0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6df0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6db0 bytes 08810f91
+ 005b6df0 bytes 08c11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a22b66e93b929dcb769245f7fab9d76"></a>

### [`005b6dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6dbc.md) → [`005b6dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6dfc.md) FUN_005b6dfc

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
      "definition_site": "005b6e0c",
      "incomplete_value": false,
      "site": "005b6e14",
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
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b6dcc",
      "incomplete_value": false,
      "site": "005b6dd4",
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
            "const:3e0:8"
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
      "005b6e14",
      "DATA",
      [
        "storage",
        "00c703e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b6e14",
      "DATA",
      [
        "storage",
        "00c704b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6dbc.md#insn-005b6dcc) · [`005b6dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6dbc.md#insn-005b6dd8)
- 新版 [`005b6e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6dfc.md#insn-005b6e0c) · [`005b6e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6dfc.md#insn-005b6e18)

~~~diff
- 005b6dcc ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 005b6dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6e0c ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 005b6e0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6e0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6e0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6dcc bytes 08810f91
+ 005b6e0c bytes 08c11291
- 005b6dd8 ["INT_ADD", "register:40f0:8", ["const:5b6dd8:8", "const:4:8"]]
- 005b6dd8 ["CALL", null, ["callee:00c57f70:8"]]
+ 005b6e18 ["INT_ADD", "register:40f0:8", ["const:5b6e18:8", "const:4:8"]]
+ 005b6e18 ["CALL", null, ["callee:00c57f70:8"]]
- 005b6dd8 bytes 32841a94
+ 005b6e18 bytes 56841a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bfbdef0f08acf5d0f7687bf1227ba71"></a>

### [`005b6e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6e7c.md) → [`005b6ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6ebc.md) FUN_005b6ebc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6ee0",
      "incomplete_value": false,
      "site": "005b6ee0",
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
      "definition_site": "005b6ea0",
      "incomplete_value": false,
      "site": "005b6ea0",
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
      "005b6ee0",
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
      "005b6ee0",
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

- 旧版 [`005b6e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6e7c.md#insn-005b6e90) · [`005b6e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6e7c.md#insn-005b6e9c)
- 新版 [`005b6ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6ebc.md#insn-005b6ed0) · [`005b6edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6ebc.md#insn-005b6edc)

~~~diff
- 005b6e90 ["INT_ADD", "register:40f0:8", ["const:5b6e90:8", "const:4:8"]]
- 005b6e90 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b6ed0 ["INT_ADD", "register:40f0:8", ["const:5b6ed0:8", "const:4:8"]]
+ 005b6ed0 ["CALL", null, ["callee:00c57f60:8"]]
- 005b6e90 bytes 00841a94
+ 005b6ed0 bytes 24841a94
- 005b6e9c ["COPY", "tmp:0:8", ["const:440:8"]]
- 005b6e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b6edc ["COPY", "tmp:0:8", ["const:510:8"]]
+ 005b6edc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6edc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b6edc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6e9c bytes 08011191
+ 005b6edc bytes 08411491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2518bbc98d7132a30d2e6e5bd239a9c4"></a>

### [`005b6eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6eb0.md) → [`005b6ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6ef0.md) FUN_005b6ef0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b6efc",
      "incomplete_value": false,
      "site": "005b6efc",
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
      "definition_site": "005b6ebc",
      "incomplete_value": false,
      "site": "005b6ebc",
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
      "005b6efc",
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
      "005b6efc",
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

- 旧版 [`005b6eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6eb0.md#insn-005b6eb8)
- 新版 [`005b6ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b6/005b6ef0.md#insn-005b6ef8)

~~~diff
- 005b6eb8 ["COPY", "tmp:0:8", ["const:440:8"]]
- 005b6eb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b6eb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b6eb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b6ef8 ["COPY", "tmp:0:8", ["const:510:8"]]
+ 005b6ef8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6ef8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b6ef8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b6eb8 bytes 29011191
+ 005b6ef8 bytes 29411491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9bf19759e319ecf4a1bf560c06238a8"></a>

### [`005b6fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6fc8.md) → [`005b7008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7008.md) FUN_005b7008

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b702c",
      "incomplete_value": false,
      "site": "005b702c",
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
      "definition_site": "005b6fec",
      "incomplete_value": false,
      "site": "005b6fec",
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
      "005b702c",
      "DATA",
      [
        "storage",
        "00c704c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b702c",
      "DATA",
      [
        "storage",
        "00c70590",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b6fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6fc8.md#insn-005b6fdc) · [`005b6fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6fc8.md#insn-005b6fe8)
- 新版 [`005b701c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7008.md#insn-005b701c) · [`005b7028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7008.md#insn-005b7028)

~~~diff
- 005b6fdc ["INT_ADD", "register:40f0:8", ["const:5b6fdc:8", "const:4:8"]]
- 005b6fdc ["CALL", null, ["callee:00c57f60:8"]]
+ 005b701c ["INT_ADD", "register:40f0:8", ["const:5b701c:8", "const:4:8"]]
+ 005b701c ["CALL", null, ["callee:00c57f60:8"]]
- 005b6fdc bytes ad831a94
+ 005b701c bytes d1831a94
- 005b6fe8 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 005b6fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b6fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b6fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7028 ["COPY", "tmp:0:8", ["const:590:8"]]
+ 005b7028 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7028 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7028 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b6fe8 bytes 08011391
+ 005b7028 bytes 08411691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3921509e0418ee594cdba5b0cf7d07f7"></a>

### [`005b6ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6ffc.md) → [`005b703c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b703c.md) FUN_005b703c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b7048",
      "incomplete_value": false,
      "site": "005b7048",
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
      "definition_site": "005b7008",
      "incomplete_value": false,
      "site": "005b7008",
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
      "005b7048",
      "DATA",
      [
        "storage",
        "00c704c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7048",
      "DATA",
      [
        "storage",
        "00c70590",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b6/005b6ffc.md#insn-005b7004)
- 新版 [`005b7044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b703c.md#insn-005b7044)

~~~diff
- 005b7004 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 005b7004 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b7004 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b7004 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b7044 ["COPY", "tmp:0:8", ["const:590:8"]]
+ 005b7044 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7044 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7044 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b7004 bytes 29011391
+ 005b7044 bytes 29411691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87a96618445f6d1d7929daec009dac79"></a>

### [`005b70f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b70f4.md) → [`005b7134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7134.md) FUN_005b7134

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b7158",
      "incomplete_value": false,
      "site": "005b7158",
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
      "definition_site": "005b7118",
      "incomplete_value": false,
      "site": "005b7118",
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
      "005b7158",
      "DATA",
      [
        "storage",
        "00c70540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7158",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b70f4.md#insn-005b7108) · [`005b7114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b70f4.md#insn-005b7114)
- 新版 [`005b7148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7134.md#insn-005b7148) · [`005b7154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7134.md#insn-005b7154)

~~~diff
- 005b7108 ["INT_ADD", "register:40f0:8", ["const:5b7108:8", "const:4:8"]]
- 005b7108 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b7148 ["INT_ADD", "register:40f0:8", ["const:5b7148:8", "const:4:8"]]
+ 005b7148 ["CALL", null, ["callee:00c57f60:8"]]
- 005b7108 bytes 62831a94
+ 005b7148 bytes 86831a94
- 005b7114 ["COPY", "tmp:0:8", ["const:540:8"]]
- 005b7114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7154 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 005b7154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7114 bytes 08011591
+ 005b7154 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9febbac60e7bd55af7c3eae7f666fd07"></a>

### [`005b7128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7128.md) → [`005b7168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7168.md) FUN_005b7168

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "005b7174",
      "incomplete_value": false,
      "site": "005b7174",
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
      "definition_site": "005b7134",
      "incomplete_value": false,
      "site": "005b7134",
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
      "005b7174",
      "DATA",
      [
        "storage",
        "00c70540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7174",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7128.md#insn-005b7130)
- 新版 [`005b7170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7168.md#insn-005b7170)

~~~diff
- 005b7130 ["COPY", "tmp:0:8", ["const:540:8"]]
- 005b7130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b7130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b7130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b7170 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 005b7170 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7170 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7170 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b7130 bytes 29011591
+ 005b7170 bytes 29411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b793d8131f3feec77af462a227f3799"></a>

### [`005b7184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7184.md) → [`005b71c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b71c4.md) FUN_005b71c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b3b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b3b74.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`005b3bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3bb4.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b71fc",
      "incomplete_value": false,
      "site": "005b7204",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b71bc",
      "incomplete_value": false,
      "site": "005b71c4",
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
            "const:5c0:8"
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
      "005b7204",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b72bc",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7204",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "005b72bc",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7184.md#insn-005b7204) · [`005b71b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7184.md#insn-005b71b4) · [`005b71bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7184.md#insn-005b71bc)
- 新版 [`005b7244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b71c4.md#insn-005b7244) · [`005b71f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b71c4.md#insn-005b71f4) · [`005b71fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b71c4.md#insn-005b71fc)

~~~diff
- 005b7204 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7204 ["INT_ADD", "register:40f0:8", ["const:5b7204:8", "const:4:8"]]
- 005b7204 ["CALLIND", null, ["register:0:8"]]
+ 005b7244 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7244 ["INT_ADD", "register:40f0:8", ["const:5b7244:8", "const:4:8"]]
+ 005b7244 ["CALLIND", null, ["register:0:8"]]
- 005b7204 bytes 00013fd6
+ 005b7244 bytes 00013fd6
- 005b71b4 ["INT_ADD", "register:40f0:8", ["const:5b71b4:8", "const:4:8"]]
- 005b71b4 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b71f4 ["INT_ADD", "register:40f0:8", ["const:5b71f4:8", "const:4:8"]]
+ 005b71f4 ["CALL", null, ["callee:00c57f60:8"]]
- 005b71b4 bytes 37831a94
+ 005b71f4 bytes 5b831a94
- 005b71bc ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 005b71bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b71bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b71bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b71fc ["COPY", "tmp:0:8", ["const:690:8"]]
+ 005b71fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b71fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b71fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b71bc bytes 08011791
+ 005b71fc bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c76843cd2a0d65d4a60f03272e04065"></a>

### [`005b72fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b72fc.md) → [`005b733c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b733c.md) FUN_005b733c

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
      "definition_site": "005b7340",
      "incomplete_value": false,
      "site": "005b7344",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7300",
      "incomplete_value": false,
      "site": "005b7304",
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
            "const:5c0:8"
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
      "005b7344",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b7344",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b72fc.md#insn-005b7300)
- 新版 [`005b7340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b733c.md#insn-005b7340)

~~~diff
- 005b7300 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 005b7300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7340 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 005b7340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7300 bytes 08011791
+ 005b7340 bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-699690b35020a018aee681b0568fabbf"></a>

### [`005b730c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b730c.md) → [`005b734c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b734c.md) FUN_005b734c

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
      "definition_site": "005b735c",
      "incomplete_value": false,
      "site": "005b7364",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b731c",
      "incomplete_value": false,
      "site": "005b7324",
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
            "const:5c0:8"
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
      "005b7364",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b7364",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b731c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b730c.md#insn-005b731c) · [`005b7328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b730c.md#insn-005b7328)
- 新版 [`005b735c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b734c.md#insn-005b735c) · [`005b7368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b734c.md#insn-005b7368)

~~~diff
- 005b731c ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 005b731c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b731c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b731c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b735c ["COPY", "tmp:0:8", ["const:690:8"]]
+ 005b735c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b735c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b735c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b731c bytes 08011791
+ 005b735c bytes 08411a91
- 005b7328 ["INT_ADD", "register:40f0:8", ["const:5b7328:8", "const:4:8"]]
- 005b7328 ["CALL", null, ["callee:00c57f70:8"]]
+ 005b7368 ["INT_ADD", "register:40f0:8", ["const:5b7368:8", "const:4:8"]]
+ 005b7368 ["CALL", null, ["callee:00c57f70:8"]]
- 005b7328 bytes de821a94
+ 005b7368 bytes 02831a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4330873f0742a863adcdc902886a68d"></a>

### [`005b734c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b734c.md) → [`005b738c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b738c.md) FUN_005b738c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b7398",
      "incomplete_value": false,
      "site": "005b73a4",
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
      "definition_site": "005b7358",
      "incomplete_value": false,
      "site": "005b7364",
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
      "005b73a4",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b73a4",
      "DATA",
      [
        "storage",
        "00c706e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b734c.md#insn-005b7358)
- 新版 [`005b7398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b738c.md#insn-005b7398)

~~~diff
- 005b7358 ["COPY", "tmp:0:8", ["const:610:8"]]
- 005b7358 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b7358 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b7358 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b7398 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 005b7398 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b7398 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b7398 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b7358 bytes 4a411891
+ 005b7398 bytes 4a811b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d21a25ab76c76e2a4ac38ab8fed5776"></a>

### [`005b7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7390.md) → [`005b73d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b73d0.md) FUN_005b73d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b73e8",
      "incomplete_value": false,
      "site": "005b73f4",
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
      "definition_site": "005b73a8",
      "incomplete_value": false,
      "site": "005b73b4",
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
      "005b73f4",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b73f4",
      "DATA",
      [
        "storage",
        "00c706e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b73a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7390.md#insn-005b73a8) · [`005b73d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7390.md#insn-005b73d8)
- 新版 [`005b73e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b73d0.md#insn-005b73e8) · [`005b7418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b73d0.md#insn-005b7418)

~~~diff
- 005b73a8 ["COPY", "tmp:0:8", ["const:610:8"]]
- 005b73a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b73a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b73a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b73e8 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 005b73e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b73e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b73e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b73a8 bytes 08411891
+ 005b73e8 bytes 08811b91
- 005b73d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b73d8 ["INT_ADD", "register:40f0:8", ["const:5b73d8:8", "const:4:8"]]
- 005b73d8 ["CALLIND", null, ["register:0:8"]]
+ 005b7418 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7418 ["INT_ADD", "register:40f0:8", ["const:5b7418:8", "const:4:8"]]
+ 005b7418 ["CALLIND", null, ["register:0:8"]]
- 005b73d8 bytes 00013fd6
+ 005b7418 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e1413767f04d3d74d84aa3414581e34"></a>

### [`005b73ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b73ec.md) → [`005b742c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b742c.md) FUN_005b742c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b7458",
      "incomplete_value": false,
      "site": "005b7458",
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
      "definition_site": "005b7418",
      "incomplete_value": false,
      "site": "005b7418",
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
      "005b7458",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7458",
      "DATA",
      [
        "storage",
        "00c706e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b73ec.md#insn-005b7400) · [`005b7410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b73ec.md#insn-005b7410) · [`005b7434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b73ec.md#insn-005b7434)
- 新版 [`005b7440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b742c.md#insn-005b7440) · [`005b7450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b742c.md#insn-005b7450) · [`005b7474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b742c.md#insn-005b7474)

~~~diff
- 005b7400 ["INT_ADD", "register:40f0:8", ["const:5b7400:8", "const:4:8"]]
- 005b7400 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b7440 ["INT_ADD", "register:40f0:8", ["const:5b7440:8", "const:4:8"]]
+ 005b7440 ["CALL", null, ["callee:00c57f60:8"]]
- 005b7400 bytes a4821a94
+ 005b7440 bytes c8821a94
- 005b7410 ["COPY", "tmp:0:8", ["const:610:8"]]
- 005b7410 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7410 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7410 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7450 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 005b7450 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7450 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7450 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7410 bytes 08411891
+ 005b7450 bytes 08811b91
- 005b7434 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7434 ["INT_ADD", "register:40f0:8", ["const:5b7434:8", "const:4:8"]]
- 005b7434 ["CALLIND", null, ["register:0:8"]]
+ 005b7474 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7474 ["INT_ADD", "register:40f0:8", ["const:5b7474:8", "const:4:8"]]
+ 005b7474 ["CALLIND", null, ["register:0:8"]]
- 005b7434 bytes 00013fd6
+ 005b7474 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-319ee6bed394db05cb880632f90a29ac"></a>

### [`005b7474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7474.md) → [`005b74b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b74b4.md) FUN_005b74b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b74d0",
      "incomplete_value": false,
      "site": "005b74d0",
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
      "definition_site": "005b7490",
      "incomplete_value": false,
      "site": "005b7490",
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
      "005b74d0",
      "DATA",
      [
        "storage",
        "00c70610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b74d0",
      "DATA",
      [
        "storage",
        "00c706e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b748c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7474.md#insn-005b748c) · [`005b74b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7474.md#insn-005b74b0)
- 新版 [`005b74cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b74b4.md#insn-005b74cc) · [`005b74f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b74b4.md#insn-005b74f0)

~~~diff
- 005b748c ["COPY", "tmp:0:8", ["const:610:8"]]
- 005b748c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b748c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b748c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b74cc ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 005b74cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b74cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b74cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b748c bytes 29411891
+ 005b74cc bytes 29811b91
- 005b74b0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b74b0 ["INT_ADD", "register:40f0:8", ["const:5b74b0:8", "const:4:8"]]
- 005b74b0 ["CALLIND", null, ["register:0:8"]]
+ 005b74f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b74f0 ["INT_ADD", "register:40f0:8", ["const:5b74f0:8", "const:4:8"]]
+ 005b74f0 ["CALLIND", null, ["register:0:8"]]
- 005b74b0 bytes 20013fd6
+ 005b74f0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ba88c1810ec126356f8fb06231d3adc"></a>

### [`005b7734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7734.md) → [`005b7774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7774.md) FUN_005b7774

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005b1e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1e64.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "005b77b4",
      "incomplete_value": false,
      "site": "005b77b8",
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
      "definition_site": "005b7774",
      "incomplete_value": false,
      "site": "005b7778",
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
      "005b77b8",
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
      "005b77b8",
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

- 旧版 [`005b7754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7734.md#insn-005b7754) · [`005b7764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7734.md#insn-005b7764) · [`005b776c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7734.md#insn-005b776c)
- 新版 [`005b7794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7774.md#insn-005b7794) · [`005b77a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7774.md#insn-005b77a4) · [`005b77ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7774.md#insn-005b77ac)

~~~diff
- 005b7754 ["INT_ADD", "register:40f0:8", ["const:5b7754:8", "const:4:8"]]
- 005b7754 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b7794 ["INT_ADD", "register:40f0:8", ["const:5b7794:8", "const:4:8"]]
+ 005b7794 ["CALL", null, ["callee:00c57f80:8"]]
- 005b7754 bytes d7811a94
+ 005b7794 bytes fb811a94
- 005b7764 ["INT_ADD", "register:40f0:8", ["const:5b7764:8", "const:4:8"]]
- 005b7764 ["CALL", null, ["callee:00c57f80:8"]]
+ 005b77a4 ["INT_ADD", "register:40f0:8", ["const:5b77a4:8", "const:4:8"]]
+ 005b77a4 ["CALL", null, ["callee:00c57f80:8"]]
- 005b7764 bytes d3811a94
+ 005b77a4 bytes f7811a94
- 005b776c ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005b776c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b776c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b776c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b77ac ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 005b77ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b77ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b77ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b776c bytes 08412891
+ 005b77ac bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-800769efc3b9713dd707b20629a4b8aa"></a>

### [`005b77ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b77ac.md) → [`005b77ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b77ec.md) FUN_005b77ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`005b1e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1e64.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "005b7824",
      "incomplete_value": false,
      "site": "005b782c",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b77e4",
      "incomplete_value": false,
      "site": "005b77ec",
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
            "const:5c0:8"
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
      "005b782c",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b78e4",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b782c",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "005b78e4",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b782c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b77ac.md#insn-005b782c) · [`005b77dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b77ac.md#insn-005b77dc) · [`005b77e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b77ac.md#insn-005b77e4)
- 新版 [`005b786c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b77ec.md#insn-005b786c) · [`005b781c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b77ec.md#insn-005b781c) · [`005b7824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b77ec.md#insn-005b7824)

~~~diff
- 005b782c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b782c ["INT_ADD", "register:40f0:8", ["const:5b782c:8", "const:4:8"]]
- 005b782c ["CALLIND", null, ["register:0:8"]]
+ 005b786c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b786c ["INT_ADD", "register:40f0:8", ["const:5b786c:8", "const:4:8"]]
+ 005b786c ["CALLIND", null, ["register:0:8"]]
- 005b782c bytes 00013fd6
+ 005b786c bytes 00013fd6
- 005b77dc ["INT_ADD", "register:40f0:8", ["const:5b77dc:8", "const:4:8"]]
- 005b77dc ["CALL", null, ["callee:00c57f60:8"]]
+ 005b781c ["INT_ADD", "register:40f0:8", ["const:5b781c:8", "const:4:8"]]
+ 005b781c ["CALL", null, ["callee:00c57f60:8"]]
- 005b77dc bytes ad811a94
+ 005b781c bytes d1811a94
- 005b77e4 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 005b77e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b77e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b77e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7824 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 005b7824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b77e4 bytes 08011791
+ 005b7824 bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-388633e1025cf4e218e208da93f324f2"></a>

### [`005b7924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7924.md) → [`005b7964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7964.md) FUN_005b7964

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b7970",
      "incomplete_value": false,
      "site": "005b797c",
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
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7930",
      "incomplete_value": false,
      "site": "005b793c",
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
            "const:6a0:8"
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
      "005b797c",
      "DATA",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b797c",
      "DATA",
      [
        "storage",
        "00c70770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7924.md#insn-005b7930)
- 新版 [`005b7970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7964.md#insn-005b7970)

~~~diff
- 005b7930 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 005b7930 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b7930 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b7930 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b7970 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 005b7970 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b7970 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b7970 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b7930 bytes 4a811a91
+ 005b7970 bytes 4ac11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60e97e61fe055dfdb8c5e139c854081e"></a>

### [`005b7968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7968.md) → [`005b79a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b79a8.md) FUN_005b79a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b79c0",
      "incomplete_value": false,
      "site": "005b79cc",
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
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7980",
      "incomplete_value": false,
      "site": "005b798c",
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
            "const:6a0:8"
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
      "005b79cc",
      "DATA",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b79cc",
      "DATA",
      [
        "storage",
        "00c70770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7968.md#insn-005b7980) · [`005b79b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7968.md#insn-005b79b0)
- 新版 [`005b79c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b79a8.md#insn-005b79c0) · [`005b79f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b79a8.md#insn-005b79f0)

~~~diff
- 005b7980 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 005b7980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b79c0 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 005b79c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b79c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b79c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7980 bytes 08811a91
+ 005b79c0 bytes 08c11d91
- 005b79b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b79b0 ["INT_ADD", "register:40f0:8", ["const:5b79b0:8", "const:4:8"]]
- 005b79b0 ["CALLIND", null, ["register:0:8"]]
+ 005b79f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b79f0 ["INT_ADD", "register:40f0:8", ["const:5b79f0:8", "const:4:8"]]
+ 005b79f0 ["CALLIND", null, ["register:0:8"]]
- 005b79b0 bytes 00013fd6
+ 005b79f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62f69122097ace8d5919b3c66ed243e9"></a>

### [`005b79c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b79c4.md) → [`005b7a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a04.md) FUN_005b7a04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b7a30",
      "incomplete_value": false,
      "site": "005b7a30",
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
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b79f0",
      "incomplete_value": false,
      "site": "005b79f0",
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
            "const:6a0:8"
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
      "005b7a30",
      "DATA",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7a30",
      "DATA",
      [
        "storage",
        "00c70770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b79d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b79c4.md#insn-005b79d8) · [`005b79e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b79c4.md#insn-005b79e8) · [`005b7a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b79c4.md#insn-005b7a0c)
- 新版 [`005b7a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a04.md#insn-005b7a18) · [`005b7a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a04.md#insn-005b7a28) · [`005b7a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a04.md#insn-005b7a4c)

~~~diff
- 005b79d8 ["INT_ADD", "register:40f0:8", ["const:5b79d8:8", "const:4:8"]]
- 005b79d8 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b7a18 ["INT_ADD", "register:40f0:8", ["const:5b7a18:8", "const:4:8"]]
+ 005b7a18 ["CALL", null, ["callee:00c57f60:8"]]
- 005b79d8 bytes 2e811a94
+ 005b7a18 bytes 52811a94
- 005b79e8 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 005b79e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b79e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b79e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7a28 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 005b7a28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7a28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7a28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b79e8 bytes 08811a91
+ 005b7a28 bytes 08c11d91
- 005b7a0c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7a0c ["INT_ADD", "register:40f0:8", ["const:5b7a0c:8", "const:4:8"]]
- 005b7a0c ["CALLIND", null, ["register:0:8"]]
+ 005b7a4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7a4c ["INT_ADD", "register:40f0:8", ["const:5b7a4c:8", "const:4:8"]]
+ 005b7a4c ["CALLIND", null, ["register:0:8"]]
- 005b7a0c bytes 00013fd6
+ 005b7a4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06eae1d19604603bb26e81b8a94b225e"></a>

### [`005b7a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7a4c.md) → [`005b7a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a8c.md) FUN_005b7a8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b7aa8",
      "incomplete_value": false,
      "site": "005b7aa8",
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
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7a68",
      "incomplete_value": false,
      "site": "005b7a68",
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
            "const:6a0:8"
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
      "005b7aa8",
      "DATA",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7aa8",
      "DATA",
      [
        "storage",
        "00c70770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7a4c.md#insn-005b7a64) · [`005b7a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7a4c.md#insn-005b7a88)
- 新版 [`005b7aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a8c.md#insn-005b7aa4) · [`005b7ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7a8c.md#insn-005b7ac8)

~~~diff
- 005b7a64 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 005b7a64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b7a64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b7a64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b7aa4 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 005b7aa4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7aa4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7aa4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b7a64 bytes 29811a91
+ 005b7aa4 bytes 29c11d91
- 005b7a88 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b7a88 ["INT_ADD", "register:40f0:8", ["const:5b7a88:8", "const:4:8"]]
- 005b7a88 ["CALLIND", null, ["register:0:8"]]
+ 005b7ac8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b7ac8 ["INT_ADD", "register:40f0:8", ["const:5b7ac8:8", "const:4:8"]]
+ 005b7ac8 ["CALLIND", null, ["register:0:8"]]
- 005b7a88 bytes 20013fd6
+ 005b7ac8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f9db224c63f052efde216dc168e1812"></a>

### [`005b7cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7cf8.md) → [`005b7d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7d38.md) FUN_005b7d38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b35f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b3/005b35f8.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`005b3638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3638.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "005b7d70",
      "incomplete_value": false,
      "site": "005b7d78",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b7d30",
      "incomplete_value": false,
      "site": "005b7d38",
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
            "const:5c0:8"
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
      "005b7d78",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b7e30",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7d78",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "005b7e30",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7cf8.md#insn-005b7d78) · [`005b7d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7cf8.md#insn-005b7d28) · [`005b7d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7cf8.md#insn-005b7d30)
- 新版 [`005b7db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7d38.md#insn-005b7db8) · [`005b7d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7d38.md#insn-005b7d68) · [`005b7d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7d38.md#insn-005b7d70)

~~~diff
- 005b7d78 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7d78 ["INT_ADD", "register:40f0:8", ["const:5b7d78:8", "const:4:8"]]
- 005b7d78 ["CALLIND", null, ["register:0:8"]]
+ 005b7db8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7db8 ["INT_ADD", "register:40f0:8", ["const:5b7db8:8", "const:4:8"]]
+ 005b7db8 ["CALLIND", null, ["register:0:8"]]
- 005b7d78 bytes 00013fd6
+ 005b7db8 bytes 00013fd6
- 005b7d28 ["INT_ADD", "register:40f0:8", ["const:5b7d28:8", "const:4:8"]]
- 005b7d28 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b7d68 ["INT_ADD", "register:40f0:8", ["const:5b7d68:8", "const:4:8"]]
+ 005b7d68 ["CALL", null, ["callee:00c57f60:8"]]
- 005b7d28 bytes 5a801a94
+ 005b7d68 bytes 7e801a94
- 005b7d30 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 005b7d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7d70 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 005b7d70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7d70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7d70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7d30 bytes 08011791
+ 005b7d70 bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccd5ae9d3377d7dbebc6c5a0d0aa5f8c"></a>

### [`005b7eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7eb4.md) → [`005b7ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7ef4.md) FUN_005b7ef4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b7f0c",
      "incomplete_value": false,
      "site": "005b7f18",
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
      "definition_site": "005b7ecc",
      "incomplete_value": false,
      "site": "005b7ed8",
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
      "005b7f18",
      "DATA",
      [
        "storage",
        "00c70720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7f18",
      "DATA",
      [
        "storage",
        "00c707f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7eb4.md#insn-005b7ecc) · [`005b7efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7eb4.md#insn-005b7efc)
- 新版 [`005b7f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7ef4.md#insn-005b7f0c) · [`005b7f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7ef4.md#insn-005b7f3c)

~~~diff
- 005b7ecc ["COPY", "tmp:0:8", ["const:720:8"]]
- 005b7ecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7ecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7ecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7f0c ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 005b7f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7ecc bytes 08811c91
+ 005b7f0c bytes 08c11f91
- 005b7efc ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7efc ["INT_ADD", "register:40f0:8", ["const:5b7efc:8", "const:4:8"]]
- 005b7efc ["CALLIND", null, ["register:0:8"]]
+ 005b7f3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7f3c ["INT_ADD", "register:40f0:8", ["const:5b7f3c:8", "const:4:8"]]
+ 005b7f3c ["CALLIND", null, ["register:0:8"]]
- 005b7efc bytes 00013fd6
+ 005b7f3c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-534c426830babfc5a73b4952f8243336"></a>

### [`005b7f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7f10.md) → [`005b7f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7f50.md) FUN_005b7f50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b7f7c",
      "incomplete_value": false,
      "site": "005b7f7c",
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
      "definition_site": "005b7f3c",
      "incomplete_value": false,
      "site": "005b7f3c",
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
      "005b7f7c",
      "DATA",
      [
        "storage",
        "00c70720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7f7c",
      "DATA",
      [
        "storage",
        "00c707f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7f10.md#insn-005b7f24) · [`005b7f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7f10.md#insn-005b7f34) · [`005b7f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7f10.md#insn-005b7f58)
- 新版 [`005b7f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7f50.md#insn-005b7f64) · [`005b7f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7f50.md#insn-005b7f74) · [`005b7f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7f50.md#insn-005b7f98)

~~~diff
- 005b7f24 ["INT_ADD", "register:40f0:8", ["const:5b7f24:8", "const:4:8"]]
- 005b7f24 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b7f64 ["INT_ADD", "register:40f0:8", ["const:5b7f64:8", "const:4:8"]]
+ 005b7f64 ["CALL", null, ["callee:00c57f60:8"]]
- 005b7f24 bytes db7f1a94
+ 005b7f64 bytes ff7f1a94
- 005b7f34 ["COPY", "tmp:0:8", ["const:720:8"]]
- 005b7f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b7f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b7f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b7f74 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 005b7f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b7f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b7f34 bytes 08811c91
+ 005b7f74 bytes 08c11f91
- 005b7f58 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b7f58 ["INT_ADD", "register:40f0:8", ["const:5b7f58:8", "const:4:8"]]
- 005b7f58 ["CALLIND", null, ["register:0:8"]]
+ 005b7f98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7f98 ["INT_ADD", "register:40f0:8", ["const:5b7f98:8", "const:4:8"]]
+ 005b7f98 ["CALLIND", null, ["register:0:8"]]
- 005b7f58 bytes 00013fd6
+ 005b7f98 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b3087c3654a165e4fcb22fb166fcb3e"></a>

### [`005b7f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7f98.md) → [`005b7fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7fd8.md) FUN_005b7fd8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b7ff4",
      "incomplete_value": false,
      "site": "005b7ff4",
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
      "definition_site": "005b7fb4",
      "incomplete_value": false,
      "site": "005b7fb4",
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
      "005b7ff4",
      "DATA",
      [
        "storage",
        "00c70720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b7ff4",
      "DATA",
      [
        "storage",
        "00c707f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7f98.md#insn-005b7fb0) · [`005b7fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b7f98.md#insn-005b7fd4)
- 新版 [`005b7ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7fd8.md#insn-005b7ff0) · [`005b8014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b7fd8.md#insn-005b8014)

~~~diff
- 005b7fb0 ["COPY", "tmp:0:8", ["const:720:8"]]
- 005b7fb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b7fb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b7fb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b7ff0 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 005b7ff0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7ff0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b7ff0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b7fb0 bytes 29811c91
+ 005b7ff0 bytes 29c11f91
- 005b7fd4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b7fd4 ["INT_ADD", "register:40f0:8", ["const:5b7fd4:8", "const:4:8"]]
- 005b7fd4 ["CALLIND", null, ["register:0:8"]]
+ 005b8014 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b8014 ["INT_ADD", "register:40f0:8", ["const:5b8014:8", "const:4:8"]]
+ 005b8014 ["CALLIND", null, ["register:0:8"]]
- 005b7fd4 bytes 20013fd6
+ 005b8014 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6d3de2bdd37275889d0da392ae41d78"></a>

### [`005b80dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b80dc.md) → [`005b811c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b811c.md) FUN_005b811c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b275c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b2/005b275c.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`005b279c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b279c.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005b8154",
      "incomplete_value": false,
      "site": "005b815c",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8114",
      "incomplete_value": false,
      "site": "005b811c",
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
            "const:5c0:8"
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
      "005b815c",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b8214",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b815c",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "005b8214",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b815c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b80dc.md#insn-005b815c) · [`005b810c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b80dc.md#insn-005b810c) · [`005b8114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b80dc.md#insn-005b8114)
- 新版 [`005b819c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b811c.md#insn-005b819c) · [`005b814c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b811c.md#insn-005b814c) · [`005b8154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b811c.md#insn-005b8154)

~~~diff
- 005b815c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b815c ["INT_ADD", "register:40f0:8", ["const:5b815c:8", "const:4:8"]]
- 005b815c ["CALLIND", null, ["register:0:8"]]
+ 005b819c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b819c ["INT_ADD", "register:40f0:8", ["const:5b819c:8", "const:4:8"]]
+ 005b819c ["CALLIND", null, ["register:0:8"]]
- 005b815c bytes 00013fd6
+ 005b819c bytes 00013fd6
- 005b810c ["INT_ADD", "register:40f0:8", ["const:5b810c:8", "const:4:8"]]
- 005b810c ["CALL", null, ["callee:00c57f60:8"]]
+ 005b814c ["INT_ADD", "register:40f0:8", ["const:5b814c:8", "const:4:8"]]
+ 005b814c ["CALL", null, ["callee:00c57f60:8"]]
- 005b810c bytes 617f1a94
+ 005b814c bytes 857f1a94
- 005b8114 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 005b8114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8154 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 005b8154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8114 bytes 08011791
+ 005b8154 bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91baed49e1361a7a66785a7bb225b788"></a>

### [`005b8254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8254.md) → [`005b8294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8294.md) FUN_005b8294

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b82a0",
      "incomplete_value": false,
      "site": "005b82ac",
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
      "definition_site": "005b8260",
      "incomplete_value": false,
      "site": "005b826c",
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
      "005b82ac",
      "DATA",
      [
        "storage",
        "00c707a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b82ac",
      "DATA",
      [
        "storage",
        "00c70870",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8254.md#insn-005b8260)
- 新版 [`005b82a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8294.md#insn-005b82a0)

~~~diff
- 005b8260 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 005b8260 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b8260 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b8260 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b82a0 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 005b82a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b82a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b82a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b8260 bytes 4a811e91
+ 005b82a0 bytes 4ac12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3464c78a114253a317dcd577faae6ae2"></a>

### [`005b8298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8298.md) → [`005b82d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b82d8.md) FUN_005b82d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b82f0",
      "incomplete_value": false,
      "site": "005b82fc",
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
      "definition_site": "005b82b0",
      "incomplete_value": false,
      "site": "005b82bc",
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
      "005b82fc",
      "DATA",
      [
        "storage",
        "00c707a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b82fc",
      "DATA",
      [
        "storage",
        "00c70870",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b82b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8298.md#insn-005b82b0) · [`005b82e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8298.md#insn-005b82e0)
- 新版 [`005b82f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b82d8.md#insn-005b82f0) · [`005b8320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b82d8.md#insn-005b8320)

~~~diff
- 005b82b0 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 005b82b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b82b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b82b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b82f0 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 005b82f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b82f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b82f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b82b0 bytes 08811e91
+ 005b82f0 bytes 08c12191
- 005b82e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b82e0 ["INT_ADD", "register:40f0:8", ["const:5b82e0:8", "const:4:8"]]
- 005b82e0 ["CALLIND", null, ["register:0:8"]]
+ 005b8320 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8320 ["INT_ADD", "register:40f0:8", ["const:5b8320:8", "const:4:8"]]
+ 005b8320 ["CALLIND", null, ["register:0:8"]]
- 005b82e0 bytes 00013fd6
+ 005b8320 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6074fe315d8f49b5283a90f0e8d7e19"></a>

### [`005b82f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b82f4.md) → [`005b8334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8334.md) FUN_005b8334

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b8360",
      "incomplete_value": false,
      "site": "005b8360",
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
      "definition_site": "005b8320",
      "incomplete_value": false,
      "site": "005b8320",
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
      "005b8360",
      "DATA",
      [
        "storage",
        "00c707a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8360",
      "DATA",
      [
        "storage",
        "00c70870",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b82f4.md#insn-005b8308) · [`005b8318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b82f4.md#insn-005b8318) · [`005b833c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b82f4.md#insn-005b833c)
- 新版 [`005b8348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8334.md#insn-005b8348) · [`005b8358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8334.md#insn-005b8358) · [`005b837c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8334.md#insn-005b837c)

~~~diff
- 005b8308 ["INT_ADD", "register:40f0:8", ["const:5b8308:8", "const:4:8"]]
- 005b8308 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b8348 ["INT_ADD", "register:40f0:8", ["const:5b8348:8", "const:4:8"]]
+ 005b8348 ["CALL", null, ["callee:00c57f60:8"]]
- 005b8308 bytes e27e1a94
+ 005b8348 bytes 067f1a94
- 005b8318 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 005b8318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8358 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 005b8358 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8358 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8358 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8318 bytes 08811e91
+ 005b8358 bytes 08c12191
- 005b833c ["COPY", "register:0:8", ["register:4040:8"]]
- 005b833c ["INT_ADD", "register:40f0:8", ["const:5b833c:8", "const:4:8"]]
- 005b833c ["CALLIND", null, ["register:0:8"]]
+ 005b837c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b837c ["INT_ADD", "register:40f0:8", ["const:5b837c:8", "const:4:8"]]
+ 005b837c ["CALLIND", null, ["register:0:8"]]
- 005b833c bytes 00013fd6
+ 005b837c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16c8eef83f75d75b70772e5f9f258ab3"></a>

### [`005b837c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b837c.md) → [`005b83bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b83bc.md) FUN_005b83bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b83d8",
      "incomplete_value": false,
      "site": "005b83d8",
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
      "definition_site": "005b8398",
      "incomplete_value": false,
      "site": "005b8398",
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
      "005b83d8",
      "DATA",
      [
        "storage",
        "00c707a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b83d8",
      "DATA",
      [
        "storage",
        "00c70870",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b837c.md#insn-005b8394) · [`005b83b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b837c.md#insn-005b83b8)
- 新版 [`005b83d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b83bc.md#insn-005b83d4) · [`005b83f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b83bc.md#insn-005b83f8)

~~~diff
- 005b8394 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 005b8394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b8394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b8394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b83d4 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 005b83d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b83d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b83d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b8394 bytes 29811e91
+ 005b83d4 bytes 29c12191
- 005b83b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b83b8 ["INT_ADD", "register:40f0:8", ["const:5b83b8:8", "const:4:8"]]
- 005b83b8 ["CALLIND", null, ["register:0:8"]]
+ 005b83f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b83f8 ["INT_ADD", "register:40f0:8", ["const:5b83f8:8", "const:4:8"]]
+ 005b83f8 ["CALLIND", null, ["register:0:8"]]
- 005b83b8 bytes 20013fd6
+ 005b83f8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a01bc04f93aacd08c94e45089e54375a"></a>

### [`005b84c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b84c0.md) → [`005b8500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8500.md) FUN_005b8500

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005b4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4020.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`005b4060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4060.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005b8538",
      "incomplete_value": true,
      "site": "005b8540",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b84f8",
      "incomplete_value": true,
      "site": "005b8500",
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
            "const:5c0:8"
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
      "005b8540",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b85f8",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8540",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "005b85f8",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b84c0.md#insn-005b8540) · [`005b84f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b84c0.md#insn-005b84f0) · [`005b84f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b84c0.md#insn-005b84f8)
- 新版 [`005b8580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8500.md#insn-005b8580) · [`005b8530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8500.md#insn-005b8530) · [`005b8538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8500.md#insn-005b8538)

~~~diff
- 005b8540 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8540 ["INT_ADD", "register:40f0:8", ["const:5b8540:8", "const:4:8"]]
- 005b8540 ["CALLIND", null, ["register:0:8"]]
+ 005b8580 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8580 ["INT_ADD", "register:40f0:8", ["const:5b8580:8", "const:4:8"]]
+ 005b8580 ["CALLIND", null, ["register:0:8"]]
- 005b8540 bytes 00013fd6
+ 005b8580 bytes 00013fd6
- 005b84f0 ["INT_ADD", "register:40f0:8", ["const:5b84f0:8", "const:4:8"]]
- 005b84f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b8530 ["INT_ADD", "register:40f0:8", ["const:5b8530:8", "const:4:8"]]
+ 005b8530 ["CALL", null, ["callee:00c57f60:8"]]
- 005b84f0 bytes 687e1a94
+ 005b8530 bytes 8c7e1a94
- 005b84f8 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 005b84f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b84f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b84f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8538 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 005b8538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b84f8 bytes 08011791
+ 005b8538 bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3545de035a9b6244526fa849d3c4e8d6"></a>

### [`005b867c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b867c.md) → [`005b86bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b86bc.md) FUN_005b86bc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b86d4",
      "incomplete_value": false,
      "site": "005b86e0",
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
    "old": {
      "definition_site": "005b8694",
      "incomplete_value": false,
      "site": "005b86a0",
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
            "const:820:8"
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
      "005b86e0",
      "DATA",
      [
        "storage",
        "00c70820",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b86e0",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b867c.md#insn-005b8694) · [`005b86c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b867c.md#insn-005b86c4)
- 新版 [`005b86d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b86bc.md#insn-005b86d4) · [`005b8704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b86bc.md#insn-005b8704)

~~~diff
- 005b8694 ["COPY", "tmp:0:8", ["const:820:8"]]
- 005b8694 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8694 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8694 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b86d4 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 005b86d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b86d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b86d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8694 bytes 08812091
+ 005b86d4 bytes 08c12391
- 005b86c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b86c4 ["INT_ADD", "register:40f0:8", ["const:5b86c4:8", "const:4:8"]]
- 005b86c4 ["CALLIND", null, ["register:0:8"]]
+ 005b8704 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8704 ["INT_ADD", "register:40f0:8", ["const:5b8704:8", "const:4:8"]]
+ 005b8704 ["CALLIND", null, ["register:0:8"]]
- 005b86c4 bytes 00013fd6
+ 005b8704 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12d8ce7834495a0f9ae22c252afcbd60"></a>

### [`005b86d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b86d8.md) → [`005b8718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8718.md) FUN_005b8718

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b8744",
      "incomplete_value": false,
      "site": "005b8744",
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
    "old": {
      "definition_site": "005b8704",
      "incomplete_value": false,
      "site": "005b8704",
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
            "const:820:8"
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
      "005b8744",
      "DATA",
      [
        "storage",
        "00c70820",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8744",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b86ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b86d8.md#insn-005b86ec) · [`005b86fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b86d8.md#insn-005b86fc) · [`005b8720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b86d8.md#insn-005b8720)
- 新版 [`005b872c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8718.md#insn-005b872c) · [`005b873c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8718.md#insn-005b873c) · [`005b8760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8718.md#insn-005b8760)

~~~diff
- 005b86ec ["INT_ADD", "register:40f0:8", ["const:5b86ec:8", "const:4:8"]]
- 005b86ec ["CALL", null, ["callee:00c57f60:8"]]
+ 005b872c ["INT_ADD", "register:40f0:8", ["const:5b872c:8", "const:4:8"]]
+ 005b872c ["CALL", null, ["callee:00c57f60:8"]]
- 005b86ec bytes e97d1a94
+ 005b872c bytes 0d7e1a94
- 005b86fc ["COPY", "tmp:0:8", ["const:820:8"]]
- 005b86fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b86fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b86fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b873c ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 005b873c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b873c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b873c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b86fc bytes 08812091
+ 005b873c bytes 08c12391
- 005b8720 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8720 ["INT_ADD", "register:40f0:8", ["const:5b8720:8", "const:4:8"]]
- 005b8720 ["CALLIND", null, ["register:0:8"]]
+ 005b8760 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8760 ["INT_ADD", "register:40f0:8", ["const:5b8760:8", "const:4:8"]]
+ 005b8760 ["CALLIND", null, ["register:0:8"]]
- 005b8720 bytes 00013fd6
+ 005b8760 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cc24d172b5ac49a050aea46d057cba1"></a>

### [`005b8760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8760.md) → [`005b87a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b87a0.md) FUN_005b87a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b87bc",
      "incomplete_value": false,
      "site": "005b87bc",
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
    "old": {
      "definition_site": "005b877c",
      "incomplete_value": false,
      "site": "005b877c",
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
            "const:820:8"
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
      "005b87bc",
      "DATA",
      [
        "storage",
        "00c70820",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b87bc",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8760.md#insn-005b8778) · [`005b879c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8760.md#insn-005b879c)
- 新版 [`005b87b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b87a0.md#insn-005b87b8) · [`005b87dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b87a0.md#insn-005b87dc)

~~~diff
- 005b8778 ["COPY", "tmp:0:8", ["const:820:8"]]
- 005b8778 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b8778 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b8778 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b87b8 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 005b87b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b87b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b87b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b8778 bytes 29812091
+ 005b87b8 bytes 29c12391
- 005b879c ["COPY", "register:0:8", ["register:4048:8"]]
- 005b879c ["INT_ADD", "register:40f0:8", ["const:5b879c:8", "const:4:8"]]
- 005b879c ["CALLIND", null, ["register:0:8"]]
+ 005b87dc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b87dc ["INT_ADD", "register:40f0:8", ["const:5b87dc:8", "const:4:8"]]
+ 005b87dc ["CALLIND", null, ["register:0:8"]]
- 005b879c bytes 20013fd6
+ 005b87dc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e8fa73cb452007aa65e936f9b8c7e14"></a>

### [`005b8a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8a64.md) → [`005b8aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8aa4.md) FUN_005b8aa4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b4590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4590.md) · 呼出先 7件 [`005aca10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ac/005aca10.md) [`005b8c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8c1c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`005b45d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b45d0.md) · 呼出先 7件 [`005aca50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005aca50.md) [`005b8c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c5c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "005b8adc",
      "incomplete_value": false,
      "site": "005b8ae4",
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
    "old": {
      "definition_site": "005b8a9c",
      "incomplete_value": false,
      "site": "005b8aa4",
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
            "const:8a0:8"
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
      "005b8ae4",
      "DATA",
      [
        "storage",
        "00c708a0",
        null,
        "pointer"
      ]
    ],
    [
      "005b8b9c",
      "READ",
      [
        "storage",
        "00c708b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8ae4",
      "DATA",
      [
        "storage",
        "00c70970",
        null,
        "pointer"
      ]
    ],
    [
      "005b8b9c",
      "READ",
      [
        "storage",
        "00c70980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8a64.md#insn-005b8ae4) · [`005b8a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8a64.md#insn-005b8a94) · [`005b8a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8a64.md#insn-005b8a9c)
- 新版 [`005b8b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8aa4.md#insn-005b8b24) · [`005b8ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8aa4.md#insn-005b8ad4) · [`005b8adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8aa4.md#insn-005b8adc)

~~~diff
- 005b8ae4 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8ae4 ["INT_ADD", "register:40f0:8", ["const:5b8ae4:8", "const:4:8"]]
- 005b8ae4 ["CALLIND", null, ["register:0:8"]]
+ 005b8b24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8b24 ["INT_ADD", "register:40f0:8", ["const:5b8b24:8", "const:4:8"]]
+ 005b8b24 ["CALLIND", null, ["register:0:8"]]
- 005b8ae4 bytes 00013fd6
+ 005b8b24 bytes 00013fd6
- 005b8a94 ["INT_ADD", "register:40f0:8", ["const:5b8a94:8", "const:4:8"]]
- 005b8a94 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b8ad4 ["INT_ADD", "register:40f0:8", ["const:5b8ad4:8", "const:4:8"]]
+ 005b8ad4 ["CALL", null, ["callee:00c57f60:8"]]
- 005b8a94 bytes ff7c1a94
+ 005b8ad4 bytes 237d1a94
- 005b8a9c ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 005b8a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8adc ["COPY", "tmp:0:8", ["const:970:8"]]
+ 005b8adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8a9c bytes 08812291
+ 005b8adc bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f02341796f83aeb4e7cac65566a95dd"></a>

### [`005b8bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8bdc.md) → [`005b8c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c1c.md) FUN_005b8c1c

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
      "definition_site": "005b8c20",
      "incomplete_value": false,
      "site": "005b8c24",
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
    "old": {
      "definition_site": "005b8be0",
      "incomplete_value": false,
      "site": "005b8be4",
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
            "const:8a0:8"
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
      "005b8c24",
      "DATA",
      [
        "storage",
        "00c708a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b8c24",
      "DATA",
      [
        "storage",
        "00c70970",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8bdc.md#insn-005b8be0)
- 新版 [`005b8c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c1c.md#insn-005b8c20)

~~~diff
- 005b8be0 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 005b8be0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8be0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8be0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8c20 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 005b8c20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8c20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8c20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8be0 bytes 08812291
+ 005b8c20 bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e752dd0f8b8208cb2ab70d4993f6b74"></a>

### [`005b8bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8bec.md) → [`005b8c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c2c.md) FUN_005b8c2c

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
      "definition_site": "005b8c3c",
      "incomplete_value": false,
      "site": "005b8c44",
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
    "old": {
      "definition_site": "005b8bfc",
      "incomplete_value": false,
      "site": "005b8c04",
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
            "const:8a0:8"
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
      "005b8c44",
      "DATA",
      [
        "storage",
        "00c708a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005b8c44",
      "DATA",
      [
        "storage",
        "00c70970",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8bec.md#insn-005b8bfc) · [`005b8c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8bec.md#insn-005b8c08)
- 新版 [`005b8c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c2c.md#insn-005b8c3c) · [`005b8c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c2c.md#insn-005b8c48)

~~~diff
- 005b8bfc ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 005b8bfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8bfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8bfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8c3c ["COPY", "tmp:0:8", ["const:970:8"]]
+ 005b8c3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8c3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8c3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8bfc bytes 08812291
+ 005b8c3c bytes 08c12591
- 005b8c08 ["INT_ADD", "register:40f0:8", ["const:5b8c08:8", "const:4:8"]]
- 005b8c08 ["CALL", null, ["callee:00c57f70:8"]]
+ 005b8c48 ["INT_ADD", "register:40f0:8", ["const:5b8c48:8", "const:4:8"]]
+ 005b8c48 ["CALL", null, ["callee:00c57f70:8"]]
- 005b8c08 bytes a67c1a94
+ 005b8c48 bytes ca7c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7e6200a2b41e3844eec2cf22db8ee2e"></a>

### [`005b8c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8c2c.md) → [`005b8c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c6c.md) FUN_005b8c6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b8c78",
      "incomplete_value": false,
      "site": "005b8c84",
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
      "definition_site": "005b8c38",
      "incomplete_value": false,
      "site": "005b8c44",
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
      "005b8c84",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8c84",
      "DATA",
      [
        "storage",
        "00c709c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8c2c.md#insn-005b8c38)
- 新版 [`005b8c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8c6c.md#insn-005b8c78)

~~~diff
- 005b8c38 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 005b8c38 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b8c38 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b8c38 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b8c78 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 005b8c78 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b8c78 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b8c78 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b8c38 bytes 4ac12391
+ 005b8c78 bytes 4a012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-479c9f444933766c4e77325f6f71a663"></a>

### [`005b8c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8c70.md) → [`005b8cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8cb0.md) FUN_005b8cb0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b8cc8",
      "incomplete_value": false,
      "site": "005b8cd4",
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
      "definition_site": "005b8c88",
      "incomplete_value": false,
      "site": "005b8c94",
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
      "005b8cd4",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8cd4",
      "DATA",
      [
        "storage",
        "00c709c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8c70.md#insn-005b8c88) · [`005b8cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8c70.md#insn-005b8cb8)
- 新版 [`005b8cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8cb0.md#insn-005b8cc8) · [`005b8cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8cb0.md#insn-005b8cf8)

~~~diff
- 005b8c88 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 005b8c88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8c88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8c88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8cc8 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 005b8cc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8cc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8cc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8c88 bytes 08c12391
+ 005b8cc8 bytes 08012791
- 005b8cb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8cb8 ["INT_ADD", "register:40f0:8", ["const:5b8cb8:8", "const:4:8"]]
- 005b8cb8 ["CALLIND", null, ["register:0:8"]]
+ 005b8cf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8cf8 ["INT_ADD", "register:40f0:8", ["const:5b8cf8:8", "const:4:8"]]
+ 005b8cf8 ["CALLIND", null, ["register:0:8"]]
- 005b8cb8 bytes 00013fd6
+ 005b8cf8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-840f574dd6505d6b19592ef3ff693f3b"></a>

### [`005b8ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8ccc.md) → [`005b8d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d0c.md) FUN_005b8d0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b8d38",
      "incomplete_value": false,
      "site": "005b8d38",
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
      "definition_site": "005b8cf8",
      "incomplete_value": false,
      "site": "005b8cf8",
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
      "005b8d38",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8d38",
      "DATA",
      [
        "storage",
        "00c709c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8ccc.md#insn-005b8ce0) · [`005b8cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8ccc.md#insn-005b8cf0) · [`005b8d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8ccc.md#insn-005b8d14)
- 新版 [`005b8d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d0c.md#insn-005b8d20) · [`005b8d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d0c.md#insn-005b8d30) · [`005b8d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d0c.md#insn-005b8d54)

~~~diff
- 005b8ce0 ["INT_ADD", "register:40f0:8", ["const:5b8ce0:8", "const:4:8"]]
- 005b8ce0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b8d20 ["INT_ADD", "register:40f0:8", ["const:5b8d20:8", "const:4:8"]]
+ 005b8d20 ["CALL", null, ["callee:00c57f60:8"]]
- 005b8ce0 bytes 6c7c1a94
+ 005b8d20 bytes 907c1a94
- 005b8cf0 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 005b8cf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8cf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8cf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b8d30 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 005b8d30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8d30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b8d30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8cf0 bytes 08c12391
+ 005b8d30 bytes 08012791
- 005b8d14 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b8d14 ["INT_ADD", "register:40f0:8", ["const:5b8d14:8", "const:4:8"]]
- 005b8d14 ["CALLIND", null, ["register:0:8"]]
+ 005b8d54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8d54 ["INT_ADD", "register:40f0:8", ["const:5b8d54:8", "const:4:8"]]
+ 005b8d54 ["CALLIND", null, ["register:0:8"]]
- 005b8d14 bytes 00013fd6
+ 005b8d54 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d154229b8eac1df33c749501df19dd6d"></a>

### [`005b8d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8d54.md) → [`005b8d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d94.md) FUN_005b8d94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b8db0",
      "incomplete_value": false,
      "site": "005b8db0",
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
      "definition_site": "005b8d70",
      "incomplete_value": false,
      "site": "005b8d70",
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
      "005b8db0",
      "DATA",
      [
        "storage",
        "00c708f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b8db0",
      "DATA",
      [
        "storage",
        "00c709c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b8d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8d54.md#insn-005b8d6c) · [`005b8d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8d54.md#insn-005b8d90)
- 新版 [`005b8dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d94.md#insn-005b8dac) · [`005b8dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8d94.md#insn-005b8dd0)

~~~diff
- 005b8d6c ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 005b8d6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b8d6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b8d6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b8dac ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 005b8dac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b8dac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b8dac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b8d6c bytes 29c12391
+ 005b8dac bytes 29012791
- 005b8d90 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b8d90 ["INT_ADD", "register:40f0:8", ["const:5b8d90:8", "const:4:8"]]
- 005b8d90 ["CALLIND", null, ["register:0:8"]]
+ 005b8dd0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b8dd0 ["INT_ADD", "register:40f0:8", ["const:5b8dd0:8", "const:4:8"]]
+ 005b8dd0 ["CALLIND", null, ["register:0:8"]]
- 005b8d90 bytes 20013fd6
+ 005b8dd0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-177b78fde432cff61e641f8ad91b8eb2"></a>

### [`005b8fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8fb4.md) → [`005b8ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8ff4.md) FUN_005b8ff4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005b4a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b4/005b4a98.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`005b4ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4ad8.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "005b902c",
      "incomplete_value": false,
      "site": "005b9034",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005b8fec",
      "incomplete_value": false,
      "site": "005b8ff4",
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
            "const:5c0:8"
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
      "005b9034",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "005b90ec",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005b9034",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "005b90ec",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b9034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8fb4.md#insn-005b9034) · [`005b8fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8fb4.md#insn-005b8fe4) · [`005b8fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b8/005b8fb4.md#insn-005b8fec)
- 新版 [`005b9074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8ff4.md#insn-005b9074) · [`005b9024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8ff4.md#insn-005b9024) · [`005b902c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b8/005b8ff4.md#insn-005b902c)

~~~diff
- 005b9034 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b9034 ["INT_ADD", "register:40f0:8", ["const:5b9034:8", "const:4:8"]]
- 005b9034 ["CALLIND", null, ["register:0:8"]]
+ 005b9074 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b9074 ["INT_ADD", "register:40f0:8", ["const:5b9074:8", "const:4:8"]]
+ 005b9074 ["CALLIND", null, ["register:0:8"]]
- 005b9034 bytes 00013fd6
+ 005b9074 bytes 00013fd6
- 005b8fe4 ["INT_ADD", "register:40f0:8", ["const:5b8fe4:8", "const:4:8"]]
- 005b8fe4 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b9024 ["INT_ADD", "register:40f0:8", ["const:5b9024:8", "const:4:8"]]
+ 005b9024 ["CALL", null, ["callee:00c57f60:8"]]
- 005b8fe4 bytes ab7b1a94
+ 005b9024 bytes cf7b1a94
- 005b8fec ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 005b8fec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b8fec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b8fec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b902c ["COPY", "tmp:0:8", ["const:690:8"]]
+ 005b902c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b902c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b902c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b8fec bytes 08011791
+ 005b902c bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3208297bd448a35b4e9f74a066475844"></a>

### [`005b912c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b912c.md) → [`005b916c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b916c.md) FUN_005b916c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b9178",
      "incomplete_value": false,
      "site": "005b9184",
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
      "definition_site": "005b9138",
      "incomplete_value": false,
      "site": "005b9144",
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
      "005b9184",
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
      "005b9184",
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

- 旧版 [`005b9138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b912c.md#insn-005b9138)
- 新版 [`005b9178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b916c.md#insn-005b9178)

~~~diff
- 005b9138 ["COPY", "tmp:0:8", ["const:970:8"]]
- 005b9138 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005b9138 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005b9138 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005b9178 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 005b9178 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9178 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005b9178 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005b9138 bytes 4ac12591
+ 005b9178 bytes 4a012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc19fa0ae3ca18f0cfc951a8515584cb"></a>

### [`005b9170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9170.md) → [`005b91b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b91b0.md) FUN_005b91b0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b91c8",
      "incomplete_value": false,
      "site": "005b91d4",
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
      "definition_site": "005b9188",
      "incomplete_value": false,
      "site": "005b9194",
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
      "005b91d4",
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
      "005b91d4",
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

- 旧版 [`005b9188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9170.md#insn-005b9188) · [`005b91b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9170.md#insn-005b91b8)
- 新版 [`005b91c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b91b0.md#insn-005b91c8) · [`005b91f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b91b0.md#insn-005b91f8)

~~~diff
- 005b9188 ["COPY", "tmp:0:8", ["const:970:8"]]
- 005b9188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b9188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b9188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b91c8 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 005b91c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b91c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b91c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b9188 bytes 08c12591
+ 005b91c8 bytes 08012991
- 005b91b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b91b8 ["INT_ADD", "register:40f0:8", ["const:5b91b8:8", "const:4:8"]]
- 005b91b8 ["CALLIND", null, ["register:0:8"]]
+ 005b91f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b91f8 ["INT_ADD", "register:40f0:8", ["const:5b91f8:8", "const:4:8"]]
+ 005b91f8 ["CALLIND", null, ["register:0:8"]]
- 005b91b8 bytes 00013fd6
+ 005b91f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ba09cf3c8917e93f7c2a75b2e6a1679"></a>

### [`005b91cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b91cc.md) → [`005b920c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b920c.md) FUN_005b920c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b9238",
      "incomplete_value": false,
      "site": "005b9238",
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
      "definition_site": "005b91f8",
      "incomplete_value": false,
      "site": "005b91f8",
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
      "005b9238",
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
      "005b9238",
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

- 旧版 [`005b91e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b91cc.md#insn-005b91e0) · [`005b91f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b91cc.md#insn-005b91f0) · [`005b9214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b91cc.md#insn-005b9214)
- 新版 [`005b9220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b920c.md#insn-005b9220) · [`005b9230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b920c.md#insn-005b9230) · [`005b9254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b920c.md#insn-005b9254)

~~~diff
- 005b91e0 ["INT_ADD", "register:40f0:8", ["const:5b91e0:8", "const:4:8"]]
- 005b91e0 ["CALL", null, ["callee:00c57f60:8"]]
+ 005b9220 ["INT_ADD", "register:40f0:8", ["const:5b9220:8", "const:4:8"]]
+ 005b9220 ["CALL", null, ["callee:00c57f60:8"]]
- 005b91e0 bytes 2c7b1a94
+ 005b9220 bytes 507b1a94
- 005b91f0 ["COPY", "tmp:0:8", ["const:970:8"]]
- 005b91f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005b91f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005b91f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005b9230 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 005b9230 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005b9230 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005b9230 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005b91f0 bytes 08c12591
+ 005b9230 bytes 08012991
- 005b9214 ["COPY", "register:0:8", ["register:4040:8"]]
- 005b9214 ["INT_ADD", "register:40f0:8", ["const:5b9214:8", "const:4:8"]]
- 005b9214 ["CALLIND", null, ["register:0:8"]]
+ 005b9254 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b9254 ["INT_ADD", "register:40f0:8", ["const:5b9254:8", "const:4:8"]]
+ 005b9254 ["CALLIND", null, ["register:0:8"]]
- 005b9214 bytes 00013fd6
+ 005b9254 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dfd087c9d043de106464ba80e53fade"></a>

### [`005b9254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9254.md) → [`005b9294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9294.md) FUN_005b9294

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005b92b0",
      "incomplete_value": false,
      "site": "005b92b0",
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
      "definition_site": "005b9270",
      "incomplete_value": false,
      "site": "005b9270",
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
      "005b92b0",
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
      "005b92b0",
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

- 旧版 [`005b926c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9254.md#insn-005b926c) · [`005b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b9/005b9254.md#insn-005b9290)
- 新版 [`005b92ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9294.md#insn-005b92ac) · [`005b92d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b9/005b9294.md#insn-005b92d0)

~~~diff
- 005b926c ["COPY", "tmp:0:8", ["const:970:8"]]
- 005b926c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005b926c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005b926c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005b92ac ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 005b92ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005b92ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005b92ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005b926c bytes 29c12591
+ 005b92ac bytes 29012991
- 005b9290 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b9290 ["INT_ADD", "register:40f0:8", ["const:5b9290:8", "const:4:8"]]
- 005b9290 ["CALLIND", null, ["register:0:8"]]
+ 005b92d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005b92d0 ["INT_ADD", "register:40f0:8", ["const:5b92d0:8", "const:4:8"]]
+ 005b92d0 ["CALLIND", null, ["register:0:8"]]
- 005b9290 bytes 20013fd6
+ 005b92d0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

