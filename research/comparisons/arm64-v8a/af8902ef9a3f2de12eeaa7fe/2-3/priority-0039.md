# v16.0.0 → v16.0.1 · 最優先の変更候補 (39)

[一覧の目次](README.md)

<a id="compare-dd5dfc7d8d5881e19e4a276d0844cc6f"></a>

### [`007af68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af68c.md) → [`007af6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af6cc.md) FUN_007af6cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "007af6f8",
      "incomplete_value": false,
      "site": "007af6f8",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af6b8",
      "incomplete_value": false,
      "site": "007af6b8",
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
      "007af6f8",
      "DATA",
      [
        "storage",
        "00c7a518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af6f8",
      "DATA",
      [
        "storage",
        "00c7a918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af68c.md#insn-007af6a0) · [`007af6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af68c.md#insn-007af6b0) · [`007af6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af68c.md#insn-007af6d4)
- 新版 `007af6e0`（命令位置の公開資料なし） · `007af6f0`（命令位置の公開資料なし） · `007af714`（命令位置の公開資料なし）

~~~diff
- 007af6a0 ["INT_ADD", "register:40f0:8", ["const:7af6a0:8", "const:4:8"]]
- 007af6a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007af6e0 ["INT_ADD", "register:40f0:8", ["const:7af6e0:8", "const:4:8"]]
+ 007af6e0 ["CALL", null, ["callee:00c57e90:8"]]
- 007af6a0 bytes fca01294
+ 007af6e0 bytes eca11294
- 007af6b0 ["COPY", "tmp:0:8", ["const:518:8"]]
- 007af6b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007af6b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007af6b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af6f0 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 007af6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007af6b0 bytes 08611491
+ 007af6f0 bytes 08612491
- 007af6d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af6d4 ["INT_ADD", "register:40f0:8", ["const:7af6d4:8", "const:4:8"]]
- 007af6d4 ["CALLIND", null, ["register:0:8"]]
+ 007af714 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af714 ["INT_ADD", "register:40f0:8", ["const:7af714:8", "const:4:8"]]
+ 007af714 ["CALLIND", null, ["register:0:8"]]
- 007af6d4 bytes 00013fd6
+ 007af714 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd488c7d4b588ef746972f848f393bf1"></a>

### [`007af714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af714.md) → [`007af754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af754.md) FUN_007af754

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
      "definition_site": "007af770",
      "incomplete_value": false,
      "site": "007af770",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af730",
      "incomplete_value": false,
      "site": "007af730",
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
      "007af770",
      "DATA",
      [
        "storage",
        "00c7a518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af770",
      "DATA",
      [
        "storage",
        "00c7a918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af714.md#insn-007af72c) · [`007af750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af714.md#insn-007af750)
- 新版 `007af76c`（命令位置の公開資料なし） · `007af790`（命令位置の公開資料なし）

~~~diff
- 007af72c ["COPY", "tmp:0:8", ["const:518:8"]]
- 007af72c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007af72c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007af72c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007af76c ["COPY", "tmp:0:8", ["const:918:8"]]
+ 007af76c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007af76c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007af76c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007af72c bytes 29611491
+ 007af76c bytes 29612491
- 007af750 ["COPY", "register:0:8", ["register:4048:8"]]
- 007af750 ["INT_ADD", "register:40f0:8", ["const:7af750:8", "const:4:8"]]
- 007af750 ["CALLIND", null, ["register:0:8"]]
+ 007af790 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007af790 ["INT_ADD", "register:40f0:8", ["const:7af790:8", "const:4:8"]]
+ 007af790 ["CALLIND", null, ["register:0:8"]]
- 007af750 bytes 20013fd6
+ 007af790 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc24450f47acc187418ef770ccbd930b"></a>

### [`007af858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af858.md) → [`007af898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007af898.md) FUN_007af898

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007ad2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad2e4.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`007ad324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad324.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "007af8d0",
      "incomplete_value": false,
      "site": "007af8d8",
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
    "old": {
      "definition_site": "007af890",
      "incomplete_value": false,
      "site": "007af898",
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
      "007af8d8",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ],
    [
      "007af990",
      "READ",
      [
        "storage",
        "00c701d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007af8d8",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "007af990",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af858.md#insn-007af8d8) · [`007af888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af858.md#insn-007af888) · [`007af890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af858.md#insn-007af890)
- 新版 `007af918`（命令位置の公開資料なし） · `007af8c8`（命令位置の公開資料なし） · `007af8d0`（命令位置の公開資料なし）

~~~diff
- 007af8d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007af8d8 ["INT_ADD", "register:40f0:8", ["const:7af8d8:8", "const:4:8"]]
- 007af8d8 ["CALLIND", null, ["register:0:8"]]
+ 007af918 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007af918 ["INT_ADD", "register:40f0:8", ["const:7af918:8", "const:4:8"]]
+ 007af918 ["CALLIND", null, ["register:0:8"]]
- 007af8d8 bytes 00013fd6
+ 007af918 bytes 00013fd6
- 007af888 ["INT_ADD", "register:40f0:8", ["const:7af888:8", "const:4:8"]]
- 007af888 ["CALL", null, ["callee:00c57e90:8"]]
+ 007af8c8 ["INT_ADD", "register:40f0:8", ["const:7af8c8:8", "const:4:8"]]
+ 007af8c8 ["CALL", null, ["callee:00c57e90:8"]]
- 007af888 bytes 82a01294
+ 007af8c8 bytes 72a11294
- 007af890 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 007af890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007af890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007af890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007af8d0 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 007af8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007af8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007af8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007af890 bytes 08010791
+ 007af8d0 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8396e97d5e3a2aec7ac3de44e0d940be"></a>

### [`007af9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af9d0.md) → [`007afa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afa10.md) FUN_007afa10

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
      "definition_site": "007afa1c",
      "incomplete_value": false,
      "site": "007afa28",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007af9dc",
      "incomplete_value": false,
      "site": "007af9e8",
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
            "const:598:8"
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
      "007afa28",
      "DATA",
      [
        "storage",
        "00c7a598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afa28",
      "DATA",
      [
        "storage",
        "00c7a998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007af9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007af9d0.md#insn-007af9dc)
- 新版 `007afa1c`（命令位置の公開資料なし）

~~~diff
- 007af9dc ["COPY", "tmp:0:8", ["const:598:8"]]
- 007af9dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007af9dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007af9dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007afa1c ["COPY", "tmp:0:8", ["const:998:8"]]
+ 007afa1c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007afa1c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007afa1c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007af9dc bytes 4a611691
+ 007afa1c bytes 4a612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98b2dbede66509b20b9b9a46721db19e"></a>

### [`007afa14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afa14.md) → [`007afa54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afa54.md) FUN_007afa54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "007afa6c",
      "incomplete_value": false,
      "site": "007afa78",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afa2c",
      "incomplete_value": false,
      "site": "007afa38",
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
            "const:598:8"
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
      "007afa78",
      "DATA",
      [
        "storage",
        "00c7a598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afa78",
      "DATA",
      [
        "storage",
        "00c7a998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afa2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afa14.md#insn-007afa2c) · [`007afa5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afa14.md#insn-007afa5c)
- 新版 `007afa6c`（命令位置の公開資料なし） · `007afa9c`（命令位置の公開資料なし）

~~~diff
- 007afa2c ["COPY", "tmp:0:8", ["const:598:8"]]
- 007afa2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007afa2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007afa2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007afa6c ["COPY", "tmp:0:8", ["const:998:8"]]
+ 007afa6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007afa6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007afa6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007afa2c bytes 08611691
+ 007afa6c bytes 08612691
- 007afa5c ["COPY", "register:0:8", ["register:4040:8"]]
- 007afa5c ["INT_ADD", "register:40f0:8", ["const:7afa5c:8", "const:4:8"]]
- 007afa5c ["CALLIND", null, ["register:0:8"]]
+ 007afa9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afa9c ["INT_ADD", "register:40f0:8", ["const:7afa9c:8", "const:4:8"]]
+ 007afa9c ["CALLIND", null, ["register:0:8"]]
- 007afa5c bytes 00013fd6
+ 007afa9c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b8a6eaf8bc76c02197d5800e4fa8c72"></a>

### [`007afa70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afa70.md) → [`007afab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afab0.md) FUN_007afab0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "007afadc",
      "incomplete_value": false,
      "site": "007afadc",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afa9c",
      "incomplete_value": false,
      "site": "007afa9c",
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
            "const:598:8"
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
      "007afadc",
      "DATA",
      [
        "storage",
        "00c7a598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afadc",
      "DATA",
      [
        "storage",
        "00c7a998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afa84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afa70.md#insn-007afa84) · [`007afa94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afa70.md#insn-007afa94) · [`007afab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afa70.md#insn-007afab8)
- 新版 `007afac4`（命令位置の公開資料なし） · `007afad4`（命令位置の公開資料なし） · `007afaf8`（命令位置の公開資料なし）

~~~diff
- 007afa84 ["INT_ADD", "register:40f0:8", ["const:7afa84:8", "const:4:8"]]
- 007afa84 ["CALL", null, ["callee:00c57e90:8"]]
+ 007afac4 ["INT_ADD", "register:40f0:8", ["const:7afac4:8", "const:4:8"]]
+ 007afac4 ["CALL", null, ["callee:00c57e90:8"]]
- 007afa84 bytes 03a01294
+ 007afac4 bytes f3a01294
- 007afa94 ["COPY", "tmp:0:8", ["const:598:8"]]
- 007afa94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007afa94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007afa94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007afad4 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 007afad4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007afad4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007afad4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007afa94 bytes 08611691
+ 007afad4 bytes 08612691
- 007afab8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007afab8 ["INT_ADD", "register:40f0:8", ["const:7afab8:8", "const:4:8"]]
- 007afab8 ["CALLIND", null, ["register:0:8"]]
+ 007afaf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afaf8 ["INT_ADD", "register:40f0:8", ["const:7afaf8:8", "const:4:8"]]
+ 007afaf8 ["CALLIND", null, ["register:0:8"]]
- 007afab8 bytes 00013fd6
+ 007afaf8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55098f92d710a295b6ab695a735830cf"></a>

### [`007afaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afaf8.md) → [`007afb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afb38.md) FUN_007afb38

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
      "definition_site": "007afb54",
      "incomplete_value": false,
      "site": "007afb54",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afb14",
      "incomplete_value": false,
      "site": "007afb14",
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
            "const:598:8"
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
      "007afb54",
      "DATA",
      [
        "storage",
        "00c7a598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afb54",
      "DATA",
      [
        "storage",
        "00c7a998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afaf8.md#insn-007afb10) · [`007afb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afaf8.md#insn-007afb34)
- 新版 `007afb50`（命令位置の公開資料なし） · `007afb74`（命令位置の公開資料なし）

~~~diff
- 007afb10 ["COPY", "tmp:0:8", ["const:598:8"]]
- 007afb10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007afb10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007afb10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007afb50 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 007afb50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007afb50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007afb50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007afb10 bytes 29611691
+ 007afb50 bytes 29612691
- 007afb34 ["COPY", "register:0:8", ["register:4048:8"]]
- 007afb34 ["INT_ADD", "register:40f0:8", ["const:7afb34:8", "const:4:8"]]
- 007afb34 ["CALLIND", null, ["register:0:8"]]
+ 007afb74 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007afb74 ["INT_ADD", "register:40f0:8", ["const:7afb74:8", "const:4:8"]]
+ 007afb74 ["CALLIND", null, ["register:0:8"]]
- 007afb34 bytes 20013fd6
+ 007afb74 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69c0e8c887b9971f5df3efa5a60c1298"></a>

### [`007afc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afc3c.md) → [`007afc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afc7c.md) FUN_007afc7c

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
      "definition_site": "007afc88",
      "incomplete_value": false,
      "site": "007afc94",
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
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afc48",
      "incomplete_value": false,
      "site": "007afc54",
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
      "007afc94",
      "DATA",
      [
        "storage",
        "00c7a618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afc94",
      "DATA",
      [
        "storage",
        "00c7aa18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afc3c.md#insn-007afc48)
- 新版 `007afc88`（命令位置の公開資料なし）

~~~diff
- 007afc48 ["COPY", "tmp:0:8", ["const:618:8"]]
- 007afc48 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007afc48 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007afc48 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007afc88 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 007afc88 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007afc88 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007afc88 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007afc48 bytes 4a611891
+ 007afc88 bytes 4a612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fe08558598ed52e5a8886d15f6abed8"></a>

### [`007afc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afc80.md) → [`007afcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afcc0.md) FUN_007afcc0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "007afcd8",
      "incomplete_value": false,
      "site": "007afce4",
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
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afc98",
      "incomplete_value": false,
      "site": "007afca4",
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
      "007afce4",
      "DATA",
      [
        "storage",
        "00c7a618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afce4",
      "DATA",
      [
        "storage",
        "00c7aa18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afc80.md#insn-007afc98) · [`007afcc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afc80.md#insn-007afcc8)
- 新版 `007afcd8`（命令位置の公開資料なし） · `007afd08`（命令位置の公開資料なし）

~~~diff
- 007afc98 ["COPY", "tmp:0:8", ["const:618:8"]]
- 007afc98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007afc98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007afc98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007afcd8 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 007afcd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007afcd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007afcd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007afc98 bytes 08611891
+ 007afcd8 bytes 08612891
- 007afcc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007afcc8 ["INT_ADD", "register:40f0:8", ["const:7afcc8:8", "const:4:8"]]
- 007afcc8 ["CALLIND", null, ["register:0:8"]]
+ 007afd08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afd08 ["INT_ADD", "register:40f0:8", ["const:7afd08:8", "const:4:8"]]
+ 007afd08 ["CALLIND", null, ["register:0:8"]]
- 007afcc8 bytes 00013fd6
+ 007afd08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b5dbac88624ca8876ea7c8f2d2728ad"></a>

### [`007afcdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afcdc.md) → [`007afd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afd1c.md) FUN_007afd1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "007afd48",
      "incomplete_value": false,
      "site": "007afd48",
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
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afd08",
      "incomplete_value": false,
      "site": "007afd08",
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
            "const:618:8"
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
      "007afd48",
      "DATA",
      [
        "storage",
        "00c7a618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afd48",
      "DATA",
      [
        "storage",
        "00c7aa18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afcdc.md#insn-007afcf0) · [`007afd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afcdc.md#insn-007afd00) · [`007afd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afcdc.md#insn-007afd24)
- 新版 `007afd30`（命令位置の公開資料なし） · `007afd40`（命令位置の公開資料なし） · `007afd64`（命令位置の公開資料なし）

~~~diff
- 007afcf0 ["INT_ADD", "register:40f0:8", ["const:7afcf0:8", "const:4:8"]]
- 007afcf0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007afd30 ["INT_ADD", "register:40f0:8", ["const:7afd30:8", "const:4:8"]]
+ 007afd30 ["CALL", null, ["callee:00c57e90:8"]]
- 007afcf0 bytes 689f1294
+ 007afd30 bytes 58a01294
- 007afd00 ["COPY", "tmp:0:8", ["const:618:8"]]
- 007afd00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007afd00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007afd00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007afd40 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 007afd40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007afd40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007afd40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007afd00 bytes 08611891
+ 007afd40 bytes 08612891
- 007afd24 ["COPY", "register:0:8", ["register:4040:8"]]
- 007afd24 ["INT_ADD", "register:40f0:8", ["const:7afd24:8", "const:4:8"]]
- 007afd24 ["CALLIND", null, ["register:0:8"]]
+ 007afd64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007afd64 ["INT_ADD", "register:40f0:8", ["const:7afd64:8", "const:4:8"]]
+ 007afd64 ["CALLIND", null, ["register:0:8"]]
- 007afd24 bytes 00013fd6
+ 007afd64 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7471d145d57939cabff40936eceeeb52"></a>

### [`007afd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afd64.md) → [`007afda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007afda4.md) FUN_007afda4

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
      "definition_site": "007afdc0",
      "incomplete_value": false,
      "site": "007afdc0",
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
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007afd80",
      "incomplete_value": false,
      "site": "007afd80",
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
      "007afdc0",
      "DATA",
      [
        "storage",
        "00c7a618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007afdc0",
      "DATA",
      [
        "storage",
        "00c7aa18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007afd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afd64.md#insn-007afd7c) · [`007afda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afd64.md#insn-007afda0)
- 新版 `007afdbc`（命令位置の公開資料なし） · `007afde0`（命令位置の公開資料なし）

~~~diff
- 007afd7c ["COPY", "tmp:0:8", ["const:618:8"]]
- 007afd7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007afd7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007afd7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007afdbc ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 007afdbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007afdbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007afdbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007afd7c bytes 29611891
+ 007afdbc bytes 29612891
- 007afda0 ["COPY", "register:0:8", ["register:4048:8"]]
- 007afda0 ["INT_ADD", "register:40f0:8", ["const:7afda0:8", "const:4:8"]]
- 007afda0 ["CALLIND", null, ["register:0:8"]]
+ 007afde0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007afde0 ["INT_ADD", "register:40f0:8", ["const:7afde0:8", "const:4:8"]]
+ 007afde0 ["CALLIND", null, ["register:0:8"]]
- 007afda0 bytes 20013fd6
+ 007afde0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8a1b64f7a7cea5bd4a73c4b4fd376b8"></a>

### [`007afefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afefc.md) → [`007aff3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007af/007aff3c.md) FUN_007aff3c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007adedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007adedc.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`007adf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007adf1c.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "007aff74",
      "incomplete_value": false,
      "site": "007aff7c",
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
    "old": {
      "definition_site": "007aff34",
      "incomplete_value": false,
      "site": "007aff3c",
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
      "007aff7c",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ],
    [
      "007b0034",
      "READ",
      [
        "storage",
        "00c701d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007aff7c",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "007b0034",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007aff7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afefc.md#insn-007aff7c) · [`007aff2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afefc.md#insn-007aff2c) · [`007aff34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007af/007afefc.md#insn-007aff34)
- 新版 `007affbc`（命令位置の公開資料なし） · `007aff6c`（命令位置の公開資料なし） · `007aff74`（命令位置の公開資料なし）

~~~diff
- 007aff7c ["COPY", "register:0:8", ["register:4040:8"]]
- 007aff7c ["INT_ADD", "register:40f0:8", ["const:7aff7c:8", "const:4:8"]]
- 007aff7c ["CALLIND", null, ["register:0:8"]]
+ 007affbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 007affbc ["INT_ADD", "register:40f0:8", ["const:7affbc:8", "const:4:8"]]
+ 007affbc ["CALLIND", null, ["register:0:8"]]
- 007aff7c bytes 00013fd6
+ 007affbc bytes 00013fd6
- 007aff2c ["INT_ADD", "register:40f0:8", ["const:7aff2c:8", "const:4:8"]]
- 007aff2c ["CALL", null, ["callee:00c57e90:8"]]
+ 007aff6c ["INT_ADD", "register:40f0:8", ["const:7aff6c:8", "const:4:8"]]
+ 007aff6c ["CALL", null, ["callee:00c57e90:8"]]
- 007aff2c bytes d99e1294
+ 007aff6c bytes c99f1294
- 007aff34 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 007aff34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007aff34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007aff34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007aff74 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 007aff74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007aff74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007aff74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007aff34 bytes 08010791
+ 007aff74 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e314914713913fd2c250135256d1df0"></a>

### [`007b0074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0074.md) → [`007b00b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b00b4.md) FUN_007b00b4

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
      "definition_site": "007b00c0",
      "incomplete_value": false,
      "site": "007b00cc",
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
    "old": {
      "definition_site": "007b0080",
      "incomplete_value": false,
      "site": "007b008c",
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
            "const:698:8"
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
      "007b00cc",
      "DATA",
      [
        "storage",
        "00c7a698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b00cc",
      "DATA",
      [
        "storage",
        "00c7aa98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b0080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0074.md#insn-007b0080)
- 新版 `007b00c0`（命令位置の公開資料なし）

~~~diff
- 007b0080 ["COPY", "tmp:0:8", ["const:698:8"]]
- 007b0080 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007b0080 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007b0080 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007b00c0 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 007b00c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007b00c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007b00c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007b0080 bytes 4a611a91
+ 007b00c0 bytes 4a612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc68a9147352be6bba5af0c1b9711ab1"></a>

### [`007b00b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b00b8.md) → [`007b00f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b00f8.md) FUN_007b00f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "007b00d0",
      "incomplete_value": false,
      "site": "007b00dc",
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
            "const:698:8"
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
      "007b011c",
      "DATA",
      [
        "storage",
        "00c7a698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b011c",
      "DATA",
      [
        "storage",
        "00c7aa98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b00d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b00b8.md#insn-007b00d0) · [`007b0100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b00b8.md#insn-007b0100)
- 新版 `007b0110`（命令位置の公開資料なし） · `007b0140`（命令位置の公開資料なし）

~~~diff
- 007b00d0 ["COPY", "tmp:0:8", ["const:698:8"]]
- 007b00d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007b00d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007b00d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007b0110 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 007b0110 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007b0110 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007b0110 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007b00d0 bytes 08611a91
+ 007b0110 bytes 08612a91
- 007b0100 ["COPY", "register:0:8", ["register:4040:8"]]
- 007b0100 ["INT_ADD", "register:40f0:8", ["const:7b0100:8", "const:4:8"]]
- 007b0100 ["CALLIND", null, ["register:0:8"]]
+ 007b0140 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007b0140 ["INT_ADD", "register:40f0:8", ["const:7b0140:8", "const:4:8"]]
+ 007b0140 ["CALLIND", null, ["register:0:8"]]
- 007b0100 bytes 00013fd6
+ 007b0140 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9984bd84c1d968deeb49405a617c7cc3"></a>

### [`007b0114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0114.md) → [`007b0154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0154.md) FUN_007b0154

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007b0140",
      "incomplete_value": false,
      "site": "007b0140",
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
            "const:698:8"
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
      "007b0180",
      "DATA",
      [
        "storage",
        "00c7a698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b0180",
      "DATA",
      [
        "storage",
        "00c7aa98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b0128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0114.md#insn-007b0128) · [`007b0138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0114.md#insn-007b0138) · [`007b015c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0114.md#insn-007b015c)
- 新版 `007b0168`（命令位置の公開資料なし） · `007b0178`（命令位置の公開資料なし） · `007b019c`（命令位置の公開資料なし）

~~~diff
- 007b0128 ["INT_ADD", "register:40f0:8", ["const:7b0128:8", "const:4:8"]]
- 007b0128 ["CALL", null, ["callee:00c57e90:8"]]
+ 007b0168 ["INT_ADD", "register:40f0:8", ["const:7b0168:8", "const:4:8"]]
+ 007b0168 ["CALL", null, ["callee:00c57e90:8"]]
- 007b0128 bytes 5a9e1294
+ 007b0168 bytes 4a9f1294
- 007b0138 ["COPY", "tmp:0:8", ["const:698:8"]]
- 007b0138 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007b0138 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007b0138 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007b0178 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 007b0178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007b0178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007b0178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007b0138 bytes 08611a91
+ 007b0178 bytes 08612a91
- 007b015c ["COPY", "register:0:8", ["register:4040:8"]]
- 007b015c ["INT_ADD", "register:40f0:8", ["const:7b015c:8", "const:4:8"]]
- 007b015c ["CALLIND", null, ["register:0:8"]]
+ 007b019c ["COPY", "register:0:8", ["register:4040:8"]]
+ 007b019c ["INT_ADD", "register:40f0:8", ["const:7b019c:8", "const:4:8"]]
+ 007b019c ["CALLIND", null, ["register:0:8"]]
- 007b015c bytes 00013fd6
+ 007b019c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0d74ce3b00325ffb98ef1a0f19ff3b2"></a>

### [`007b019c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b019c.md) → [`007b01dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b01dc.md) FUN_007b01dc

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
    "old": {
      "definition_site": "007b01b8",
      "incomplete_value": false,
      "site": "007b01b8",
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
            "const:698:8"
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
      "007b01f8",
      "DATA",
      [
        "storage",
        "00c7a698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b01f8",
      "DATA",
      [
        "storage",
        "00c7aa98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b01b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b019c.md#insn-007b01b4) · [`007b01d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b019c.md#insn-007b01d8)
- 新版 `007b01f4`（命令位置の公開資料なし） · `007b0218`（命令位置の公開資料なし）

~~~diff
- 007b01b4 ["COPY", "tmp:0:8", ["const:698:8"]]
- 007b01b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007b01b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007b01b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007b01f4 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 007b01f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007b01f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007b01f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007b01b4 bytes 29611a91
+ 007b01f4 bytes 29612a91
- 007b01d8 ["COPY", "register:0:8", ["register:4048:8"]]
- 007b01d8 ["INT_ADD", "register:40f0:8", ["const:7b01d8:8", "const:4:8"]]
- 007b01d8 ["CALLIND", null, ["register:0:8"]]
+ 007b0218 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007b0218 ["INT_ADD", "register:40f0:8", ["const:7b0218:8", "const:4:8"]]
+ 007b0218 ["CALLIND", null, ["register:0:8"]]
- 007b01d8 bytes 20013fd6
+ 007b0218 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-871ee377f457de3cc6c394722d42c0a3"></a>

### [`007b02e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b02e0.md) → [`007b0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0320.md) FUN_007b0320

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
    "old": {
      "definition_site": "007b02ec",
      "incomplete_value": false,
      "site": "007b02f8",
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
            "const:718:8"
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
      "007b0338",
      "DATA",
      [
        "storage",
        "00c7a718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b0338",
      "DATA",
      [
        "storage",
        "00c7ab18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b02ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b02e0.md#insn-007b02ec)
- 新版 `007b032c`（命令位置の公開資料なし）

~~~diff
- 007b02ec ["COPY", "tmp:0:8", ["const:718:8"]]
- 007b02ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007b02ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007b02ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007b032c ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 007b032c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007b032c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007b032c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007b02ec bytes 4a611c91
+ 007b032c bytes 4a612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0941c834773099ae591d44a96a218de3"></a>

### [`007b0380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0380.md) → [`007b03c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b03c0.md) FUN_007b03c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007b03ac",
      "incomplete_value": false,
      "site": "007b03ac",
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
            "const:718:8"
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
      "007b03ec",
      "DATA",
      [
        "storage",
        "00c7a718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b03ec",
      "DATA",
      [
        "storage",
        "00c7ab18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b0394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0380.md#insn-007b0394) · [`007b03a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0380.md#insn-007b03a4) · [`007b03c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0380.md#insn-007b03c8)
- 新版 `007b03d4`（命令位置の公開資料なし） · `007b03e4`（命令位置の公開資料なし） · `007b0408`（命令位置の公開資料なし）

~~~diff
- 007b0394 ["INT_ADD", "register:40f0:8", ["const:7b0394:8", "const:4:8"]]
- 007b0394 ["CALL", null, ["callee:00c57e90:8"]]
+ 007b03d4 ["INT_ADD", "register:40f0:8", ["const:7b03d4:8", "const:4:8"]]
+ 007b03d4 ["CALL", null, ["callee:00c57e90:8"]]
- 007b0394 bytes bf9d1294
+ 007b03d4 bytes af9e1294
- 007b03a4 ["COPY", "tmp:0:8", ["const:718:8"]]
- 007b03a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007b03a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007b03a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007b03e4 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 007b03e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007b03e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007b03e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007b03a4 bytes 08611c91
+ 007b03e4 bytes 08612c91
- 007b03c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 007b03c8 ["INT_ADD", "register:40f0:8", ["const:7b03c8:8", "const:4:8"]]
- 007b03c8 ["CALLIND", null, ["register:0:8"]]
+ 007b0408 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007b0408 ["INT_ADD", "register:40f0:8", ["const:7b0408:8", "const:4:8"]]
+ 007b0408 ["CALLIND", null, ["register:0:8"]]
- 007b03c8 bytes 00013fd6
+ 007b0408 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dde33dfa14ac7eeeadd4acabb6ef3970"></a>

### [`007b0408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0408.md) → [`007b0448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0448.md) FUN_007b0448

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
    "old": {
      "definition_site": "007b0424",
      "incomplete_value": false,
      "site": "007b0424",
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
            "const:718:8"
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
      "007b0464",
      "DATA",
      [
        "storage",
        "00c7a718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007b0464",
      "DATA",
      [
        "storage",
        "00c7ab18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b0420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0408.md#insn-007b0420) · [`007b0444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b0408.md#insn-007b0444)
- 新版 `007b0460`（命令位置の公開資料なし） · `007b0484`（命令位置の公開資料なし）

~~~diff
- 007b0420 ["COPY", "tmp:0:8", ["const:718:8"]]
- 007b0420 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007b0420 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007b0420 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007b0460 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 007b0460 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007b0460 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007b0460 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007b0420 bytes 29611c91
+ 007b0460 bytes 29612c91
- 007b0444 ["COPY", "register:0:8", ["register:4048:8"]]
- 007b0444 ["INT_ADD", "register:40f0:8", ["const:7b0444:8", "const:4:8"]]
- 007b0444 ["CALLIND", null, ["register:0:8"]]
+ 007b0484 ["COPY", "register:0:8", ["register:4048:8"]]
+ 007b0484 ["INT_ADD", "register:40f0:8", ["const:7b0484:8", "const:4:8"]]
+ 007b0484 ["CALLIND", null, ["register:0:8"]]
- 007b0444 bytes 20013fd6
+ 007b0484 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b2eb8934867e729cd4ed8cd2f93d0ee"></a>

### [`007b054c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b054c.md) → [`007b058c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b058c.md) _INIT_145

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "007b05cc",
      "incomplete_value": true,
      "site": "007b05e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d82:8"
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
    "old": {
      "definition_site": "007b05ec",
      "incomplete_value": true,
      "site": "007b0604",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e95:8"
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
    "old": {
      "definition_site": "007b0608",
      "incomplete_value": true,
      "site": "007b0624",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:592:8"
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
      "007b05c8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "007b05ec",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "007b060c",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007b05c8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "007b05ec",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "007b060c",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b05c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b054c.md#insn-007b05c4) · [`007b05e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b054c.md#insn-007b05e4) · [`007b0780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b054c.md#insn-007b0780)
- 新版 `007b0604`（命令位置の公開資料なし） · `007b0624`（命令位置の公開資料なし） · `007b07c0`（命令位置の公開資料なし）

~~~diff
- 007b05c4 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 007b05c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007b05c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007b05c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007b0604 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 007b0604 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007b0604 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007b0604 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007b05c4 bytes 4a093691
+ 007b0604 bytes 4a093791
- 007b05e4 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 007b05e4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007b05e4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007b05e4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007b0624 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 007b0624 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007b0624 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007b0624 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007b05e4 bytes 4a553a91
+ 007b0624 bytes 4a893d91
- 007b0780 ["INT_ADD", "register:40f0:8", ["const:7b0780:8", "const:4:8"]]
- 007b0780 ["CALL", null, ["callee:00c57e30:8"]]
+ 007b07c0 ["INT_ADD", "register:40f0:8", ["const:7b07c0:8", "const:4:8"]]
+ 007b07c0 ["CALL", null, ["callee:00c57e30:8"]]
- 007b0780 bytes ac9c1294
+ 007b07c0 bytes 9c9d1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afbf55bcdd78d7b29eef04e7b950bcd1"></a>

### [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) → [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) FUN_007b0a18

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 51件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046e4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e4f8.md)
- 新版 呼出元 1件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 51件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046e538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e538.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.86% / 新版 83.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 422件, `call_target` 12件, `store_destination` 144件, `store_value` 271件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007b0a54",
      "incomplete_value": false,
      "site": "007b0a5c",
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
    "old": {
      "definition_site": "007b0a14",
      "incomplete_value": false,
      "site": "007b0a1c",
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
            "const:798:8"
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
      "definition_site": "007b0c44",
      "incomplete_value": true,
      "site": "007b0c44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:38e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007b0c04",
      "incomplete_value": true,
      "site": "007b0c04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:34e:8"
              ]
            ]
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
      "definition_site": "007b0c60",
      "incomplete_value": true,
      "site": "007b0c60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f16:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007b0c20",
      "incomplete_value": true,
      "site": "007b0c20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007b0a5c",
      "DATA",
      [
        "storage",
        "00c7a798",
        null,
        "pointer"
      ]
    ],
    [
      "007b0af8",
      "DATA",
      [
        "storage",
        "0039aab0",
        "fde_0039aab0",
        "dword"
      ]
    ],
    [
      "007b0ba8",
      "DATA",
      [
        "storage",
        "0039aab0",
        "fde_0039aab0",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "007b0a5c",
      "DATA",
      [
        "storage",
        "00c7ab98",
        null,
        "pointer"
      ]
    ],
    [
      "007b0af8",
      "DATA",
      [
        "storage",
        "0039aab0",
        null,
        "byte[23]"
      ]
    ],
    [
      "007b0ba8",
      "DATA",
      [
        "storage",
        "0039aab0",
        null,
        "byte[23]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007b0c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/assembly/007b0/007b09d8-007b09d8-007bb9c8.md#insn-007b0c44) · [`007b0cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/assembly/007b0/007b09d8-007b09d8-007bb9c8.md#insn-007b0cac) · [`007b0ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/assembly/007b0/007b09d8-007b09d8-007bb9c8.md#insn-007b0ebc)
- 新版 `007b0c84`（命令位置の公開資料なし） · `007b0cec`（命令位置の公開資料なし） · `007b0efc`（命令位置の公開資料なし）

~~~diff
- 007b0c44 ["INT_ADD", "register:40f0:8", ["const:7b0c44:8", "const:4:8"]]
- 007b0c44 ["CALL", null, ["callee:0047e60c:8"]]
+ 007b0c84 ["INT_ADD", "register:40f0:8", ["const:7b0c84:8", "const:4:8"]]
+ 007b0c84 ["CALL", null, ["callee:0047e60c:8"]]
- 007b0c44 bytes 6236f397
+ 007b0c84 bytes 6236f397
- 007b0cac ["COPY", "tmp:0:8", ["const:b38:8"]]
- 007b0cac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007b0cac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007b0cac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007b0cec ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 007b0cec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007b0cec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007b0cec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007b0cac bytes 08e12c91
+ 007b0cec bytes 08e13c91
- 007b0ebc ["INT_ADD", "register:40f0:8", ["const:7b0ebc:8", "const:4:8"]]
- 007b0ebc ["CALL", null, ["callee:00c53d00:8"]]
+ 007b0efc ["INT_ADD", "register:40f0:8", ["const:7b0efc:8", "const:4:8"]]
+ 007b0efc ["CALL", null, ["callee:00c53d00:8"]]
- 007b0ebc bytes 898a1294
+ 007b0efc bytes 818b1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b57d812df4770f6e4f682adc9be5ab02"></a>

### [`007bbd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbd08.md) → [`007bbd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbd48.md) FUN_007bbd48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 13件 [`006bed1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006be/006bed1c.md) [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007cb5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb5a0.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 7件 [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b4c.md) [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md) [`00805fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805fa4.md)
- 新版 呼出元 13件 [`006bed5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006be/006bed5c.md) [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 7件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`00805fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805fe4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

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
      "site": "007bbd74",
      "value": [
        "leaf",
        "ram:802b8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007bbd34",
      "value": [
        "leaf",
        "ram:802b4c:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007bbdcc",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007bbd8c",
      "value": [
        "leaf",
        "ram:a65bf4:8"
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
      "007bbd74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ],
    [
      "007bbdcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ],
  "added": [
    [
      "007bbd74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ],
    [
      "007bbdcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bbd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbd08.md#insn-007bbd34) · [`007bbd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbd08.md#insn-007bbd8c) · [`007bbd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbd08.md#insn-007bbd20)
- 新版 `007bbd74`（命令位置の公開資料なし） · `007bbdcc`（命令位置の公開資料なし） · `007bbd60`（命令位置の公開資料なし）

~~~diff
- 007bbd34 ["INT_ADD", "register:40f0:8", ["const:7bbd34:8", "const:4:8"]]
- 007bbd34 ["CALL", null, ["ram:802b4c:8"]]
+ 007bbd74 ["INT_ADD", "register:40f0:8", ["const:7bbd74:8", "const:4:8"]]
+ 007bbd74 ["CALL", null, ["ram:802b8c:8"]]
- 007bbd34 bytes 861b0194
+ 007bbd74 bytes 861b0194
- 007bbd8c ["INT_ADD", "register:40f0:8", ["const:7bbd8c:8", "const:4:8"]]
- 007bbd8c ["CALL", null, ["ram:a65bf4:8"]]
+ 007bbdcc ["INT_ADD", "register:40f0:8", ["const:7bbdcc:8", "const:4:8"]]
+ 007bbdcc ["CALL", null, ["ram:a65dec:8"]]
- 007bbd8c bytes 9aa70a94
+ 007bbdcc bytes 08a80a94
- 007bbd20 ["INT_ADD", "register:40f0:8", ["const:7bbd20:8", "const:4:8"]]
- 007bbd20 ["CALL", null, ["callee:008026b8:8"]]
+ 007bbd60 ["INT_ADD", "register:40f0:8", ["const:7bbd60:8", "const:4:8"]]
+ 007bbd60 ["CALL", null, ["callee:008026b8:8"]]
- 007bbd20 bytes 561a0194
+ 007bbd60 bytes 561a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77603e53f6024d0e370076e143ae3d2f"></a>

### [`007bbddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md) → [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) FUN_007bbe1c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) · 呼出先 30件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md)
- 新版 呼出元 1件 [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) · 呼出先 30件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

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
    "old": {
      "definition_site": "007bcc48",
      "incomplete_value": true,
      "site": "007bcc60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d6:8"
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
    "old": {
      "definition_site": "007bcd94",
      "incomplete_value": true,
      "site": "007bcda8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a2f:8"
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
    "old": {
      "definition_site": "007bcdac",
      "incomplete_value": true,
      "site": "007bcdac",
      "value": [
        "LOAD",
        "8",
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
      "007bcc74",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "007bcc88",
      "READ",
      [
        "storage",
        "002bf0d6",
        null,
        "string"
      ]
    ],
    [
      "007bcce4",
      "READ",
      [
        "storage",
        "002a8fbd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007bcc74",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "007bcc88",
      "READ",
      [
        "storage",
        "002bf116",
        null,
        "string"
      ]
    ],
    [
      "007bcce4",
      "READ",
      [
        "storage",
        "002a908a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007bcca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md#insn-007bcca0) · [`007bcd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md#insn-007bcd0c) · [`007bcdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md#insn-007bcdec)
- 新版 `007bcce0`（命令位置の公開資料なし） · `007bcd4c`（命令位置の公開資料なし） · `007bce2c`（命令位置の公開資料なし）

~~~diff
- 007bcca0 ["COPY", "tmp:0:8", ["const:fbd:8"]]
- 007bcca0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007bcca0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007bcca0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007bcce0 ["COPY", "tmp:0:8", ["const:8a:8"]]
+ 007bcce0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007bcce0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007bcce0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007bcca0 bytes 29f53e91
+ 007bcce0 bytes 29290291
- 007bcd0c ["INT_ADD", "register:40f0:8", ["const:7bcd0c:8", "const:4:8"]]
- 007bcd0c ["CALL", null, ["callee:0047e60c:8"]]
+ 007bcd4c ["INT_ADD", "register:40f0:8", ["const:7bcd4c:8", "const:4:8"]]
+ 007bcd4c ["CALL", null, ["callee:0047e60c:8"]]
- 007bcd0c bytes 3006f397
+ 007bcd4c bytes 3006f397
- 007bcdec ["INT_ADD", "register:40f0:8", ["const:7bcdec:8", "const:4:8"]]
- 007bcdec ["CALL", null, ["callee:0046f0b4:8"]]
+ 007bce2c ["INT_ADD", "register:40f0:8", ["const:7bce2c:8", "const:4:8"]]
+ 007bce2c ["CALL", null, ["callee:0046f0b4:8"]]
- 007bcdec bytes a2c8f297
+ 007bce2c bytes a2c8f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1760d8936dbefe7b421eebdbb89c2e8"></a>

### [`007c7938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7938.md) → [`007c7978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7978.md) FUN_007c7978

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047b/0047b4cc.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008005ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008005ec.md) [`00804f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00804/00804f94.md)
- 新版 呼出元 2件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0047b50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`0080062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/0080062c.md) [`00804fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00804/00804fd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

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
      "site": "007c7b50",
      "value": [
        "leaf",
        "ram:804fd4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007c7b10",
      "value": [
        "leaf",
        "ram:804f94:8"
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
      "007c79c8",
      "DATA",
      [
        "storage",
        "0038e0f0",
        null,
        "byte[27]"
      ]
    ],
    [
      "007c79c8",
      "DATA",
      [
        "storage",
        "0038e0f4",
        null,
        "byte[27]"
      ]
    ],
    [
      "007c7b50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00804f94"
      ]
    ]
  ],
  "added": [
    [
      "007c79c8",
      "DATA",
      [
        "storage",
        "0038e0f0",
        null,
        "byte[31]"
      ]
    ],
    [
      "007c79c8",
      "DATA",
      [
        "storage",
        "0038e0f4",
        null,
        "byte[31]"
      ]
    ],
    [
      "007c7b50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00804fd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c7b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7938.md#insn-007c7b10) · [`007c7990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7938.md#insn-007c7990) · [`007c79a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7938.md#insn-007c79a0)
- 新版 `007c7b50`（命令位置の公開資料なし） · `007c79d0`（命令位置の公開資料なし） · `007c79e0`（命令位置の公開資料なし）

~~~diff
- 007c7b10 ["INT_ADD", "register:40f0:8", ["const:7c7b10:8", "const:4:8"]]
- 007c7b10 ["CALL", null, ["ram:804f94:8"]]
+ 007c7b50 ["INT_ADD", "register:40f0:8", ["const:7c7b50:8", "const:4:8"]]
+ 007c7b50 ["CALL", null, ["ram:804fd4:8"]]
- 007c7b10 bytes 21f50094
+ 007c7b50 bytes 21f50094
- 007c7990 ["INT_ADD", "register:40f0:8", ["const:7c7990:8", "const:4:8"]]
- 007c7990 ["CALL", null, ["callee:00800378:8"]]
+ 007c79d0 ["INT_ADD", "register:40f0:8", ["const:7c79d0:8", "const:4:8"]]
+ 007c79d0 ["CALL", null, ["callee:00800378:8"]]
- 007c7990 bytes 6ae20094
+ 007c79d0 bytes 6ae20094
- 007c79a0 ["INT_ADD", "register:40f0:8", ["const:7c79a0:8", "const:4:8"]]
- 007c79a0 ["CALL", null, ["callee:0080062c:8"]]
+ 007c79e0 ["INT_ADD", "register:40f0:8", ["const:7c79e0:8", "const:4:8"]]
+ 007c79e0 ["CALL", null, ["callee:0080062c:8"]]
- 007c79a0 bytes 13e30094
+ 007c79e0 bytes 13e30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bb69b9bc797c4909b6bde85c23eb9eb"></a>

### [`007c7b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7b80.md) → [`007c7bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7bc0.md) FUN_007c7bc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 15件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488138.md)
- 新版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 15件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488178.md)

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
    "old": {
      "definition_site": "007c7bb8",
      "incomplete_value": false,
      "site": "007c7bc4",
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
            "const:938:8"
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
    "old": {
      "definition_site": "007c7d64",
      "incomplete_value": true,
      "site": "007c7d68",
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
      "007c7c04",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "007c7c0c",
      "READ",
      [
        "storage",
        "002a6a61",
        null,
        "string"
      ]
    ],
    [
      "007c7d70",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007c7c04",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "007c7c0c",
      "READ",
      [
        "storage",
        "002a6b3d",
        null,
        "string"
      ]
    ],
    [
      "007c7d70",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c7c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7b80.md#insn-007c7c04) · [`007c7bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7b80.md#insn-007c7bb0) · [`007c7bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7b80.md#insn-007c7bb8)
- 新版 `007c7c44`（命令位置の公開資料なし） · `007c7bf0`（命令位置の公開資料なし） · `007c7bf8`（命令位置の公開資料なし）

~~~diff
- 007c7c04 ["INT_ADD", "register:40f0:8", ["const:7c7c04:8", "const:4:8"]]
- 007c7c04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007c7c44 ["INT_ADD", "register:40f0:8", ["const:7c7c44:8", "const:4:8"]]
+ 007c7c44 ["CALL", null, ["callee:00c57eb0:8"]]
- 007c7c04 bytes ab3f1294
+ 007c7c44 bytes 9b401294
- 007c7bb0 ["INT_ADD", "register:40f0:8", ["const:7c7bb0:8", "const:4:8"]]
- 007c7bb0 ["CALL", null, ["callee:00487e20:8"]]
+ 007c7bf0 ["INT_ADD", "register:40f0:8", ["const:7c7bf0:8", "const:4:8"]]
+ 007c7bf0 ["CALL", null, ["callee:00487e20:8"]]
- 007c7bb0 bytes 8c00f397
+ 007c7bf0 bytes 8c00f397
- 007c7bb8 ["COPY", "tmp:0:8", ["const:938:8"]]
- 007c7bb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007c7bb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007c7bb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007c7bf8 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 007c7bf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7bf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007c7bf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007c7bb8 bytes 08e12491
+ 007c7bf8 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7970b8412026652c84554d9ee154dd5"></a>

### [`007c8cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c8/007c8cb0.md) → [`007c8cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c8/007c8cf0.md) FUN_007c8cf0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 24件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab00.md) [`0048ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab08.md)
- 新版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 24件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ab40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab40.md) [`0048ab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab48.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

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
    "old": {
      "definition_site": "007c8ffc",
      "incomplete_value": false,
      "site": "007c8ffc",
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
                "const:b00:8"
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
    "old": {
      "definition_site": "007c9000",
      "incomplete_value": false,
      "site": "007c9000",
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
            "const:b00:8"
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
    "old": {
      "definition_site": "007c8ffc",
      "incomplete_value": false,
      "site": "007c9000",
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
                "const:b00:8"
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
      "007c8d4c",
      "DATA",
      [
        "storage",
        "0039badc",
        "fde_0039badc",
        "dword"
      ]
    ],
    [
      "007c8d6c",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[15]"
      ]
    ],
    [
      "007c8d78",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "007c8d4c",
      "DATA",
      [
        "storage",
        "0039badc",
        null,
        "uleb128"
      ]
    ],
    [
      "007c8d6c",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ],
    [
      "007c8d78",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c8d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c8/007c8cb0.md#insn-007c8d90) · [`007c8dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c8/007c8cb0.md#insn-007c8dd0) · [`007c8f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c8/007c8cb0.md#insn-007c8f18)
- 新版 `007c8dd0`（命令位置の公開資料なし） · `007c8e10`（命令位置の公開資料なし） · `007c8f58`（命令位置の公開資料なし）

~~~diff
- 007c8d90 ["INT_ADD", "register:40f0:8", ["const:7c8d90:8", "const:4:8"]]
- 007c8d90 ["CALL", null, ["callee:0048ce54:8"]]
+ 007c8dd0 ["INT_ADD", "register:40f0:8", ["const:7c8dd0:8", "const:4:8"]]
+ 007c8dd0 ["CALL", null, ["callee:0048ce54:8"]]
- 007c8d90 bytes 2110f397
+ 007c8dd0 bytes 2110f397
- 007c8dd0 ["INT_ADD", "register:40f0:8", ["const:7c8dd0:8", "const:4:8"]]
- 007c8dd0 ["CALL", null, ["callee:0047e8dc:8"]]
+ 007c8e10 ["INT_ADD", "register:40f0:8", ["const:7c8e10:8", "const:4:8"]]
+ 007c8e10 ["CALL", null, ["callee:0047e8dc:8"]]
- 007c8dd0 bytes b3d6f297
+ 007c8e10 bytes b3d6f297
- 007c8f18 ["INT_ADD", "register:40f0:8", ["const:7c8f18:8", "const:4:8"]]
- 007c8f18 ["CALL", null, ["callee:0047e8dc:8"]]
+ 007c8f58 ["INT_ADD", "register:40f0:8", ["const:7c8f58:8", "const:4:8"]]
+ 007c8f58 ["CALL", null, ["callee:0047e8dc:8"]]
- 007c8f18 bytes 61d6f297
+ 007c8f58 bytes 61d6f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6242c41ecd1b6b5ff24950f0f9c757e"></a>

### [`007c90dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c9/007c90dc.md) → [`007c911c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c911c.md) FUN_007c911c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 22件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`007ff154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff154.md)
- 新版 呼出元 1件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 22件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`007ff194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff194.md)

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
    "old": {
      "definition_site": "007c9470",
      "incomplete_value": false,
      "site": "007c9470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
    "old": {
      "definition_site": "007c952c",
      "incomplete_value": false,
      "site": "007c9530",
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
                "const:3a0:8"
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
    "old": {
      "definition_site": "007c9124",
      "incomplete_value": true,
      "site": "007c9124",
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
      "007c9158",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007c916c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c9174",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c9158",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007c916c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c9174",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c913c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c9/007c90dc.md#insn-007c913c) · [`007c94f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c9/007c90dc.md#insn-007c94f0) · [`007c9118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c9/007c90dc.md#insn-007c9118)
- 新版 `007c917c`（命令位置の公開資料なし） · `007c9530`（命令位置の公開資料なし） · `007c9158`（命令位置の公開資料なし）

~~~diff
- 007c913c ["INT_ADD", "register:40f0:8", ["const:7c913c:8", "const:4:8"]]
- 007c913c ["CALL", null, ["callee:00c58610:8"]]
+ 007c917c ["INT_ADD", "register:40f0:8", ["const:7c917c:8", "const:4:8"]]
+ 007c917c ["CALL", null, ["callee:00c58610:8"]]
- 007c913c bytes 353c1294
+ 007c917c bytes 253d1294
- 007c94f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f68:8"]]
- 007c94f0 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c9530 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:368:8"]]
+ 007c9530 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 007c94f0 bytes b5b647f9
+ 007c9530 bytes b5b641f9
- 007c9118 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
- 007c9118 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 007c9158 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
+ 007c9158 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 007c9118 bytes 00bd42f9
+ 007c9158 bytes 00bd44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-587a5b6ba0a9649eee28a8abdf6e45ed"></a>

### [`007c970c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c9/007c970c.md) → [`007c974c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c9/007c974c.md) FUN_007c974c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) · 呼出先 30件 [`0046da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da1c.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 30件 [`0046da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da5c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

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
    "old": {
      "definition_site": "007c99d0",
      "incomplete_value": true,
      "site": "007c99d0",
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
    "old": {
      "definition_site": "007c9a3c",
      "incomplete_value": true,
      "site": "007c9a3c",
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
    "old": {
      "definition_site": "007c9b88",
      "incomplete_value": true,
      "site": "007c9b88",
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
      "007c979c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007c97a8",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c97b0",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007c979c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007c97a8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007c97b0",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007c9778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c9/007c970c.md#insn-007c9778) · [`007c9aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c9/007c970c.md#insn-007c9aa0) · [`007c9b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c9/007c970c.md#insn-007c9b78)
- 新版 `007c97b8`（命令位置の公開資料なし） · `007c9ae0`（命令位置の公開資料なし） · `007c9bb8`（命令位置の公開資料なし）

~~~diff
- 007c9778 ["INT_ADD", "register:40f0:8", ["const:7c9778:8", "const:4:8"]]
- 007c9778 ["CALL", null, ["callee:00c58610:8"]]
+ 007c97b8 ["INT_ADD", "register:40f0:8", ["const:7c97b8:8", "const:4:8"]]
+ 007c97b8 ["CALL", null, ["callee:00c58610:8"]]
- 007c9778 bytes a63a1294
+ 007c97b8 bytes 963b1294
- 007c9aa0 ["INT_ADD", "register:40f0:8", ["const:7c9aa0:8", "const:4:8"]]
- 007c9aa0 ["CALL", null, ["ram:71be98:8"]]
+ 007c9ae0 ["INT_ADD", "register:40f0:8", ["const:7c9ae0:8", "const:4:8"]]
+ 007c9ae0 ["CALL", null, ["ram:71bed8:8"]]
- 007c9aa0 bytes fe48fd97
+ 007c9ae0 bytes fe48fd97
- 007c9b78 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 007c9bb8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 007c9b78 bytes 882600b0
+ 007c9bb8 bytes 882600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2f94d860df97879ace8a93da60490dd"></a>

### [`007ca02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca02c.md) → [`007ca06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca06c.md) FUN_007ca06c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) · 呼出先 22件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md)
- 新版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 22件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

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
    "old": {
      "definition_site": "007ca2d4",
      "incomplete_value": false,
      "site": "007ca2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
    "old": {
      "definition_site": "007ca414",
      "incomplete_value": false,
      "site": "007ca414",
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
                "const:b00:8"
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
    "old": {
      "definition_site": "007ca418",
      "incomplete_value": false,
      "site": "007ca418",
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
            "const:b00:8"
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
      "007ca0ac",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007ca0b8",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ca0c0",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007ca0ac",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007ca0b8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ca0c0",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca02c.md#insn-007ca088) · [`007ca120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca02c.md#insn-007ca120) · [`007ca160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca02c.md#insn-007ca160)
- 新版 `007ca0c8`（命令位置の公開資料なし） · `007ca160`（命令位置の公開資料なし） · `007ca1a0`（命令位置の公開資料なし）

~~~diff
- 007ca088 ["INT_ADD", "register:40f0:8", ["const:7ca088:8", "const:4:8"]]
- 007ca088 ["CALL", null, ["callee:00c58610:8"]]
+ 007ca0c8 ["INT_ADD", "register:40f0:8", ["const:7ca0c8:8", "const:4:8"]]
+ 007ca0c8 ["CALL", null, ["callee:00c58610:8"]]
- 007ca088 bytes 62381294
+ 007ca0c8 bytes 52391294
- 007ca120 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 007ca120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007ca120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007ca120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007ca160 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 007ca160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007ca160 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007ca120 bytes 08e12c91
+ 007ca160 bytes 08e13c91
- 007ca160 ["INT_ADD", "register:40f0:8", ["const:7ca160:8", "const:4:8"]]
- 007ca160 ["CALL", null, ["callee:0047e8dc:8"]]
+ 007ca1a0 ["INT_ADD", "register:40f0:8", ["const:7ca1a0:8", "const:4:8"]]
+ 007ca1a0 ["CALL", null, ["callee:0047e8dc:8"]]
- 007ca160 bytes cfd1f297
+ 007ca1a0 bytes cfd1f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-386c6a6c6a4eef6df6d02f067fc05323"></a>

### [`007ca4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca4e8.md) → [`007ca528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca528.md) FUN_007ca528

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) · 呼出先 20件 [`0046da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da1c.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`007ff91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff91c.md) [`007ff920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ff/007ff920.md)
- 新版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 20件 [`0046da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da5c.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`007ff95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff95c.md) [`007ff960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ff960.md)

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
    "old": {
      "definition_site": "007ca820",
      "incomplete_value": true,
      "site": "007ca820",
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
    "old": {
      "definition_site": "007ca890",
      "incomplete_value": false,
      "site": "007ca890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7d000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
    "old": {
      "definition_site": "007ca910",
      "incomplete_value": true,
      "site": "007ca910",
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
      "007ca56c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007ca578",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ca580",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007ca56c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007ca578",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007ca580",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ca548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca4e8.md#insn-007ca548) · [`007ca684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca4e8.md#insn-007ca684) · [`007ca850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca4e8.md#insn-007ca850)
- 新版 `007ca588`（命令位置の公開資料なし） · `007ca6c4`（命令位置の公開資料なし） · `007ca890`（命令位置の公開資料なし）

~~~diff
- 007ca548 ["INT_ADD", "register:40f0:8", ["const:7ca548:8", "const:4:8"]]
- 007ca548 ["CALL", null, ["callee:00c58610:8"]]
+ 007ca588 ["INT_ADD", "register:40f0:8", ["const:7ca588:8", "const:4:8"]]
+ 007ca588 ["CALL", null, ["callee:00c58610:8"]]
- 007ca548 bytes 32371294
+ 007ca588 bytes 22381294
- 007ca684 ["COPY", "register:0:8", ["register:4040:8"]]
- 007ca684 ["INT_ADD", "register:40f0:8", ["const:7ca684:8", "const:4:8"]]
- 007ca684 ["CALLIND", null, ["register:0:8"]]
+ 007ca6c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 007ca6c4 ["INT_ADD", "register:40f0:8", ["const:7ca6c4:8", "const:4:8"]]
+ 007ca6c4 ["CALLIND", null, ["register:0:8"]]
- 007ca684 bytes 00013fd6
+ 007ca6c4 bytes 00013fd6
- 007ca850 ["INT_ADD", "register:40f0:8", ["const:7ca850:8", "const:4:8"]]
- 007ca850 ["CALL", null, ["callee:00c53d00:8"]]
+ 007ca890 ["INT_ADD", "register:40f0:8", ["const:7ca890:8", "const:4:8"]]
+ 007ca890 ["CALL", null, ["callee:00c53d00:8"]]
- 007ca850 bytes 24241294
+ 007ca890 bytes 1c251294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b48e6e4bbc48bdbd3a8e7ed7603fecaa"></a>

### [`007caa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007caa88.md) → [`007caac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md) FUN_007caac8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) · 呼出先 30件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00727cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727cdc.md)
- 新版 呼出元 2件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 30件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00727d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727d1c.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "007cace8",
      "incomplete_value": false,
      "site": "007cacec",
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
                "const:3a0:8"
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
    "old": {
      "definition_site": "007cb0cc",
      "incomplete_value": false,
      "site": "007cb0d0",
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
                "const:3a0:8"
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
    "old": {
      "definition_site": "007cb150",
      "incomplete_value": false,
      "site": "007cb154",
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
                "const:3a0:8"
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
      "007cab30",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007cab3c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007cab44",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007cab30",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007cab3c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007cab44",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cab0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007caa88.md#insn-007cab0c) · [`007cab4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007caa88.md#insn-007cab4c) · [`007cab9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007caa88.md#insn-007cab9c)
- 新版 `007cab4c`（命令位置の公開資料なし） · `007cab8c`（命令位置の公開資料なし） · `007cabdc`（命令位置の公開資料なし）

~~~diff
- 007cab0c ["INT_ADD", "register:40f0:8", ["const:7cab0c:8", "const:4:8"]]
- 007cab0c ["CALL", null, ["callee:00c58610:8"]]
+ 007cab4c ["INT_ADD", "register:40f0:8", ["const:7cab4c:8", "const:4:8"]]
+ 007cab4c ["CALL", null, ["callee:00c58610:8"]]
- 007cab0c bytes c1351294
+ 007cab4c bytes b1361294
- 007cab4c ["INT_ADD", "register:40f0:8", ["const:7cab4c:8", "const:4:8"]]
- 007cab4c ["CALL", null, ["callee:00489f4c:8"]]
+ 007cab8c ["INT_ADD", "register:40f0:8", ["const:7cab8c:8", "const:4:8"]]
+ 007cab8c ["CALL", null, ["callee:00489f4c:8"]]
- 007cab4c bytes f0fcf297
+ 007cab8c bytes f0fcf297
- 007cab9c ["INT_ADD", "register:40f0:8", ["const:7cab9c:8", "const:4:8"]]
- 007cab9c ["CALL", null, ["ram:46c984:8"]]
+ 007cabdc ["INT_ADD", "register:40f0:8", ["const:7cabdc:8", "const:4:8"]]
+ 007cabdc ["CALL", null, ["ram:46c9c4:8"]]
- 007cab9c bytes 7a87f297
+ 007cabdc bytes 7a87f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de2926a0ad271e387f3beaf319a2ae0a"></a>

### [`007cb5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb5a0.md) → [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) FUN_007cb5e0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`009fb2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fb/009fb2b0.md) · 呼出先 67件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md)
- 新版 呼出元 3件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`009fb44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md) · 呼出先 67件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.70% / 新版 91.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 12件, `call_target` 23件, `store_value` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "007cb5f8",
      "incomplete_value": true,
      "site": "007cb604",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:76d:8"
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
    "old": {
      "definition_site": "007cba84",
      "incomplete_value": true,
      "site": "007cba98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7e3:8"
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
    "old": {
      "definition_site": "007cbbc8",
      "incomplete_value": true,
      "site": "007cbbe4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4e4:8"
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
      "007cb638",
      "READ",
      [
        "storage",
        "002b776d",
        null,
        "string"
      ]
    ],
    [
      "007cb658",
      "PARAM",
      [
        "storage",
        "002a144e",
        null,
        "string"
      ]
    ],
    [
      "007cb6c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007ef644"
      ]
    ]
  ],
  "added": [
    [
      "007cb638",
      "READ",
      [
        "storage",
        "002b77ad",
        null,
        "string"
      ]
    ],
    [
      "007cb658",
      "PARAM",
      [
        "storage",
        "002a151b",
        null,
        "string"
      ]
    ],
    [
      "007cb6c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007ef684"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007cb620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb5a0.md#insn-007cb620) · [`007cb684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb5a0.md#insn-007cb684) · [`007cb6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cb/007cb5a0.md#insn-007cb6c4)
- 新版 `007cb660`（命令位置の公開資料なし） · `007cb6c4`（命令位置の公開資料なし） · `007cb704`（命令位置の公開資料なし）

~~~diff
- 007cb620 ["INT_ADD", "register:40f0:8", ["const:7cb620:8", "const:4:8"]]
- 007cb620 ["CALL", null, ["callee:00c57f70:8"]]
+ 007cb660 ["INT_ADD", "register:40f0:8", ["const:7cb660:8", "const:4:8"]]
+ 007cb660 ["CALL", null, ["callee:00c57f70:8"]]
- 007cb620 bytes 54311294
+ 007cb660 bytes 44321294
- 007cb684 ["INT_ADD", "register:40f0:8", ["const:7cb684:8", "const:4:8"]]
- 007cb684 ["CALL", null, ["ram:7ef644:8"]]
+ 007cb6c4 ["INT_ADD", "register:40f0:8", ["const:7cb6c4:8", "const:4:8"]]
+ 007cb6c4 ["CALL", null, ["ram:7ef684:8"]]
- 007cb684 bytes f08f0094
+ 007cb6c4 bytes f08f0094
- 007cb6c4 ["INT_ADD", "register:40f0:8", ["const:7cb6c4:8", "const:4:8"]]
- 007cb6c4 ["CALL", null, ["callee:007bbd48:8"]]
+ 007cb704 ["INT_ADD", "register:40f0:8", ["const:7cb704:8", "const:4:8"]]
+ 007cb704 ["CALL", null, ["callee:007bbd48:8"]]
- 007cb6c4 bytes 91c1ff97
+ 007cb704 bytes 91c1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faaf36bf4f65f9ddfee72fe18200b361"></a>

### [`007dd760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd760.md) → [`007dd7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd7a0.md) FUN_007dd7a0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 31件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 31件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

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
    "old": {
      "definition_site": "007dd898",
      "incomplete_value": true,
      "site": "007dd8a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:35b:8"
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
    "old": {
      "definition_site": "007dd89c",
      "incomplete_value": true,
      "site": "007dd8ac",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "007dd8a0",
      "incomplete_value": true,
      "site": "007dd8b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:260:8"
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
      "007dd7f0",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007dd7fc",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007dd804",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007dd7f0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007dd7fc",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007dd804",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007dd7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd760.md#insn-007dd7cc) · [`007dd86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd760.md#insn-007dd86c) · [`007dd8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd760.md#insn-007dd8f0)
- 新版 `007dd80c`（命令位置の公開資料なし） · `007dd8ac`（命令位置の公開資料なし） · `007dd930`（命令位置の公開資料なし）

~~~diff
- 007dd7cc ["INT_ADD", "register:40f0:8", ["const:7dd7cc:8", "const:4:8"]]
- 007dd7cc ["CALL", null, ["callee:00c58610:8"]]
+ 007dd80c ["INT_ADD", "register:40f0:8", ["const:7dd80c:8", "const:4:8"]]
+ 007dd80c ["CALL", null, ["callee:00c58610:8"]]
- 007dd7cc bytes 91ea1194
+ 007dd80c bytes 81eb1194
- 007dd86c ["INT_ADD", "register:40f0:8", ["const:7dd86c:8", "const:4:8"]]
- 007dd86c ["CALL", null, ["callee:00a65860:8"]]
+ 007dd8ac ["INT_ADD", "register:40f0:8", ["const:7dd8ac:8", "const:4:8"]]
+ 007dd8ac ["CALL", null, ["callee:00a65860:8"]]
- 007dd86c bytes 7f1f0a94
+ 007dd8ac bytes ed1f0a94
- 007dd8f0 ["INT_ADD", "register:40f0:8", ["const:7dd8f0:8", "const:4:8"]]
- 007dd8f0 ["CALL", null, ["callee:0047e8dc:8"]]
+ 007dd930 ["INT_ADD", "register:40f0:8", ["const:7dd930:8", "const:4:8"]]
+ 007dd930 ["CALL", null, ["callee:0047e8dc:8"]]
- 007dd8f0 bytes eb83f297
+ 007dd930 bytes eb83f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-058d698cfa8b77d42ed5016fc7fcabf5"></a>

### [`007defe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007defe4.md) → [`007df024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df024.md) FUN_007df024

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007f292c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f292c.md) · 呼出先 5件 [`00a42f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a42f40.md) [`00a83068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a83/00a83068.md) [`00a83254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a83/00a83254.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007f296c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f296c.md) · 呼出先 5件 [`00a43138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a43/00a43138.md) [`00a83260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a83260.md) [`00a8344c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a8344c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "site": "007df068",
      "value": [
        "leaf",
        "ram:a43138:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007df028",
      "value": [
        "leaf",
        "ram:a42f40:8"
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
      "007df068",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a42f40"
      ]
    ]
  ],
  "added": [
    [
      "007df068",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a43138"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007df028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007defe4.md#insn-007df028) · [`007df014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007defe4.md#insn-007df014) · [`007df040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007defe4.md#insn-007df040)
- 新版 `007df068`（命令位置の公開資料なし） · `007df054`（命令位置の公開資料なし） · `007df080`（命令位置の公開資料なし）

~~~diff
- 007df028 ["INT_ADD", "register:40f0:8", ["const:7df028:8", "const:4:8"]]
- 007df028 ["CALL", null, ["ram:a42f40:8"]]
+ 007df068 ["INT_ADD", "register:40f0:8", ["const:7df068:8", "const:4:8"]]
+ 007df068 ["CALL", null, ["ram:a43138:8"]]
- 007df028 bytes c68f0994
+ 007df068 bytes 34900994
- 007df014 ["INT_ADD", "register:40f0:8", ["const:7df014:8", "const:4:8"]]
- 007df014 ["CALL", null, ["callee:00a83260:8"]]
+ 007df054 ["INT_ADD", "register:40f0:8", ["const:7df054:8", "const:4:8"]]
+ 007df054 ["CALL", null, ["callee:00a83260:8"]]
- 007df014 bytes 15900a94
+ 007df054 bytes 83900a94
- 007df040 ["INT_ADD", "register:40f0:8", ["const:7df040:8", "const:4:8"]]
- 007df040 ["CALL", null, ["callee:00a8344c:8"]]
+ 007df080 ["INT_ADD", "register:40f0:8", ["const:7df080:8", "const:4:8"]]
+ 007df080 ["CALL", null, ["callee:00a8344c:8"]]
- 007df040 bytes 85900a94
+ 007df080 bytes f3900a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b4e0b0aae6cf664772a9829d9a84c27"></a>

### [`007ef2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef2e0.md) → [`007ef320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef320.md) FUN_007ef320

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 8件 [`005e4e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4e34.md) [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b4c.md) [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md) [`00a064d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a064d8.md)
- 新版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 8件 [`005e4e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4e74.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00a06674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06674.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

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
      "site": "007ef344",
      "value": [
        "leaf",
        "ram:802b8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ef304",
      "value": [
        "leaf",
        "ram:802b4c:8"
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
      "007ef344",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ]
  ],
  "added": [
    [
      "007ef344",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ef304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef2e0.md#insn-007ef304) · [`007ef344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef2e0.md#insn-007ef344) · [`007ef2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef2e0.md#insn-007ef2f8)
- 新版 `007ef344`（命令位置の公開資料なし） · `007ef384`（命令位置の公開資料なし） · `007ef338`（命令位置の公開資料なし）

~~~diff
- 007ef304 ["INT_ADD", "register:40f0:8", ["const:7ef304:8", "const:4:8"]]
- 007ef304 ["CALL", null, ["ram:802b4c:8"]]
+ 007ef344 ["INT_ADD", "register:40f0:8", ["const:7ef344:8", "const:4:8"]]
+ 007ef344 ["CALL", null, ["ram:802b8c:8"]]
- 007ef304 bytes 124e0094
+ 007ef344 bytes 124e0094
- 007ef344 ["INT_ADD", "register:40f0:8", ["const:7ef344:8", "const:4:8"]]
- 007ef344 ["CALL", null, ["callee:00a06674:8"]]
+ 007ef384 ["INT_ADD", "register:40f0:8", ["const:7ef384:8", "const:4:8"]]
+ 007ef384 ["CALL", null, ["callee:00a06674:8"]]
- 007ef344 bytes 655c0894
+ 007ef384 bytes bc5c0894
- 007ef2f8 ["INT_ADD", "register:40f0:8", ["const:7ef2f8:8", "const:4:8"]]
- 007ef2f8 ["CALL", null, ["callee:008026b8:8"]]
+ 007ef338 ["INT_ADD", "register:40f0:8", ["const:7ef338:8", "const:4:8"]]
+ 007ef338 ["CALL", null, ["callee:008026b8:8"]]
- 007ef2f8 bytes e04c0094
+ 007ef338 bytes e04c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5d8e4553c373931cb5bb95c7c652280"></a>

### [`007ef4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef4d8.md) → [`007ef518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef518.md) FUN_007ef518

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 1件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 1件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.96% / 新版 97.96%

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
      "site": "007ef538",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007ef4f8",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "007ef538",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "007ef538",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007ef4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007ef4d8.md#insn-007ef4f8)
- 新版 `007ef538`（命令位置の公開資料なし）

~~~diff
- 007ef4f8 ["INT_ADD", "register:40f0:8", ["const:7ef4f8:8", "const:4:8"]]
- 007ef4f8 ["CALL", null, ["ram:46c984:8"]]
+ 007ef538 ["INT_ADD", "register:40f0:8", ["const:7ef538:8", "const:4:8"]]
+ 007ef538 ["CALL", null, ["ram:46c9c4:8"]]
- 007ef4f8 bytes 23f5f197
+ 007ef538 bytes 23f5f197
~~~


<a id="compare-955d7998770a1bf361e065528ece34bf"></a>

### [`007efb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efb3c.md) → [`007efb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efb7c.md) FUN_007efb7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00933edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00933/00933edc.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) [`00afdfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afd/00afdfe4.md) [`00aff204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00aff204.md) · 呼出先 2件 [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b4c.md)
- 新版 呼出元 4件 [`00934078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/00934078.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) [`00afe40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afe40c.md) [`00aff62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00aff62c.md) · 呼出先 2件 [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "site": "007efb9c",
      "value": [
        "leaf",
        "ram:802b8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007efb5c",
      "value": [
        "leaf",
        "ram:802b4c:8"
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
      "007efb9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ]
  ],
  "added": [
    [
      "007efb9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007efb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efb3c.md#insn-007efb5c) · [`007efb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efb3c.md#insn-007efb48)
- 新版 `007efb9c`（命令位置の公開資料なし） · `007efb88`（命令位置の公開資料なし）

~~~diff
- 007efb5c ["INT_ADD", "register:40f0:8", ["const:7efb5c:8", "const:4:8"]]
- 007efb5c ["CALL", null, ["ram:802b4c:8"]]
+ 007efb9c ["INT_ADD", "register:40f0:8", ["const:7efb9c:8", "const:4:8"]]
+ 007efb9c ["CALL", null, ["ram:802b8c:8"]]
- 007efb5c bytes fc4b0094
+ 007efb9c bytes fc4b0094
- 007efb48 ["INT_ADD", "register:40f0:8", ["const:7efb48:8", "const:4:8"]]
- 007efb48 ["CALL", null, ["callee:008026b8:8"]]
+ 007efb88 ["INT_ADD", "register:40f0:8", ["const:7efb88:8", "const:4:8"]]
+ 007efb88 ["CALL", null, ["callee:008026b8:8"]]
- 007efb48 bytes cc4a0094
+ 007efb88 bytes cc4a0094
~~~


<a id="compare-5f0db8d1003b4b9cdb39079d8765eb2b"></a>

### [`007efb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efb70.md) → [`007efbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efbb0.md) FUN_007efbb0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 7件 [`0067687c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067687c.md) [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b4c.md) [`00a32c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a32/00a32c10.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 7件 [`006768bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/006768bc.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b8c.md) [`00a32e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32e08.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

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
      "site": "007efbe8",
      "value": [
        "leaf",
        "ram:802b8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007efba8",
      "value": [
        "leaf",
        "ram:802b4c:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007efc58",
      "value": [
        "leaf",
        "ram:802b8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007efc18",
      "value": [
        "leaf",
        "ram:802b4c:8"
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
      "007efbe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ],
    [
      "007efc58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ]
  ],
  "added": [
    [
      "007efbe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ],
    [
      "007efc58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007efba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efb70.md#insn-007efba8) · [`007efc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efb70.md#insn-007efc18) · [`007efb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efb70.md#insn-007efb98)
- 新版 `007efbe8`（命令位置の公開資料なし） · `007efc58`（命令位置の公開資料なし） · `007efbd8`（命令位置の公開資料なし）

~~~diff
- 007efba8 ["INT_ADD", "register:40f0:8", ["const:7efba8:8", "const:4:8"]]
- 007efba8 ["CALL", null, ["ram:802b4c:8"]]
+ 007efbe8 ["INT_ADD", "register:40f0:8", ["const:7efbe8:8", "const:4:8"]]
+ 007efbe8 ["CALL", null, ["ram:802b8c:8"]]
- 007efba8 bytes e94b0094
+ 007efbe8 bytes e94b0094
- 007efc18 ["INT_ADD", "register:40f0:8", ["const:7efc18:8", "const:4:8"]]
- 007efc18 ["CALL", null, ["ram:802b4c:8"]]
+ 007efc58 ["INT_ADD", "register:40f0:8", ["const:7efc58:8", "const:4:8"]]
+ 007efc58 ["CALL", null, ["ram:802b8c:8"]]
- 007efc18 bytes cd4b0094
+ 007efc58 bytes cd4b0094
- 007efb98 ["INT_ADD", "register:40f0:8", ["const:7efb98:8", "const:4:8"]]
- 007efb98 ["CALL", null, ["callee:008026b8:8"]]
+ 007efbd8 ["INT_ADD", "register:40f0:8", ["const:7efbd8:8", "const:4:8"]]
+ 007efbd8 ["CALL", null, ["callee:008026b8:8"]]
- 007efb98 bytes b84a0094
+ 007efbd8 bytes b84a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb28b496fbe6907a0bc7df706dd4c2f9"></a>

### [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) → [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) FUN_007efca8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`007fceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fceac.md) [`007fcf9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcf9c.md) · 呼出先 33件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`005e486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e486c.md) [`005e4b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4b48.md) [`005e4ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4ea4.md) [`005e8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8158.md)
- 新版 呼出元 2件 [`007fceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fceec.md) [`007fcfdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcfdc.md) · 呼出先 33件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`005e48ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e48ac.md) [`005e4b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4b88.md) [`005e4ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4ee4.md) [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.25% / 新版 91.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "007efd3c",
      "incomplete_value": false,
      "site": "007efd44",
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
            "const:ab4:8"
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
    "old": {
      "definition_site": "007efd64",
      "incomplete_value": false,
      "site": "007efd70",
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
            "const:52e:8"
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
    "old": {
      "definition_site": "007efd9c",
      "incomplete_value": false,
      "site": "007efda0",
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
            "const:e08:8"
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
      "007efcf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007dd324"
      ]
    ],
    [
      "007efd10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b4c"
      ]
    ],
    [
      "007efd18",
      "DATA",
      [
        "storage",
        "003870a0",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "007efcf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007dd364"
      ]
    ],
    [
      "007efd10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802b8c"
      ]
    ],
    [
      "007efd18",
      "DATA",
      [
        "storage",
        "003870a0",
        null,
        "byte[23]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007efcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md#insn-007efcb0) · [`007efcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md#insn-007efcd0) · [`007efd04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md#insn-007efd04)
- 新版 `007efcf0`（命令位置の公開資料なし） · `007efd10`（命令位置の公開資料なし） · `007efd44`（命令位置の公開資料なし）

~~~diff
- 007efcb0 ["INT_ADD", "register:40f0:8", ["const:7efcb0:8", "const:4:8"]]
- 007efcb0 ["CALL", null, ["ram:7dd324:8"]]
+ 007efcf0 ["INT_ADD", "register:40f0:8", ["const:7efcf0:8", "const:4:8"]]
+ 007efcf0 ["CALL", null, ["ram:7dd364:8"]]
- 007efcb0 bytes 9db5ff97
+ 007efcf0 bytes 9db5ff97
- 007efcd0 ["INT_ADD", "register:40f0:8", ["const:7efcd0:8", "const:4:8"]]
- 007efcd0 ["CALL", null, ["ram:802b4c:8"]]
+ 007efd10 ["INT_ADD", "register:40f0:8", ["const:7efd10:8", "const:4:8"]]
+ 007efd10 ["CALL", null, ["ram:802b8c:8"]]
- 007efcd0 bytes 9f4b0094
+ 007efd10 bytes 9f4b0094
- 007efd04 ["INT_ADD", "register:40f0:8", ["const:7efd04:8", "const:4:8"]]
- 007efd04 ["CALL", null, ["ram:802b4c:8"]]
+ 007efd44 ["INT_ADD", "register:40f0:8", ["const:7efd44:8", "const:4:8"]]
+ 007efd44 ["CALL", null, ["ram:802b8c:8"]]
- 007efd04 bytes 924b0094
+ 007efd44 bytes 924b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a231e611358698eaf8a41bb32b18eec4"></a>

### [`007f0534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0534.md) → [`007f0574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0574.md) FUN_007f0574

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007caa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007caa88.md) · 呼出先 7件 [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00a4658c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4658c.md) [`00a46ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46ad0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`007caac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007caac8.md) · 呼出先 7件 [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00a46784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46784.md) [`00a46cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46cc8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
    "old": {
      "definition_site": "007f05e8",
      "incomplete_value": false,
      "site": "007f05ec",
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
                "const:3a0:8"
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
      "007f05ec",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "007f0600",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ],
    [
      "007f062c",
      "DATA",
      [
        "storage",
        "00c8b3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f05ec",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "007f0600",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ],
    [
      "007f062c",
      "DATA",
      [
        "storage",
        "00c8b7b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f05ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0534.md#insn-007f05ac) · [`007f0588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0534.md#insn-007f0588) · [`007f059c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0534.md#insn-007f059c)
- 新版 `007f05ec`（命令位置の公開資料なし） · `007f05c8`（命令位置の公開資料なし） · `007f05dc`（命令位置の公開資料なし）

~~~diff
- 007f05ac ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:f68:8"]]
- 007f05ac ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f05ec ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:368:8"]]
+ 007f05ec ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 007f05ac bytes 18b747f9
+ 007f05ec bytes 18b741f9
- 007f0588 ["INT_ADD", "register:40f0:8", ["const:7f0588:8", "const:4:8"]]
- 007f0588 ["CALL", null, ["callee:00a46cc8:8"]]
+ 007f05c8 ["INT_ADD", "register:40f0:8", ["const:7f05c8:8", "const:4:8"]]
+ 007f05c8 ["CALL", null, ["callee:00a46cc8:8"]]
- 007f0588 bytes 52590994
+ 007f05c8 bytes c0590994
- 007f059c ["INT_ADD", "register:40f0:8", ["const:7f059c:8", "const:4:8"]]
- 007f059c ["CALL", null, ["callee:00a46784:8"]]
+ 007f05dc ["INT_ADD", "register:40f0:8", ["const:7f05dc:8", "const:4:8"]]
+ 007f05dc ["CALL", null, ["callee:00a46784:8"]]
- 007f059c bytes fc570994
+ 007f05dc bytes 6a580994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cb360f745f03da23be9cb69632f4b78"></a>

### [`007f06b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f06b4.md) → [`007f06f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f06f4.md) FUN_007f06f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007f0c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0c34.md) · 呼出先 10件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md)
- 新版 呼出元 1件 [`007f0c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c74.md) · 呼出先 10件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00672748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00672/00672748.md) [`0067e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e5e8.md) [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md)

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
    "old": {
      "definition_site": "007f06d0",
      "incomplete_value": false,
      "site": "007f06d4",
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
            "const:798:8"
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
    "old": {
      "definition_site": "007f0bb0",
      "incomplete_value": false,
      "site": "007f0bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
    "old": {
      "definition_site": "007f0bec",
      "incomplete_value": false,
      "site": "007f0bf0",
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
            "const:410:8"
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
      "007f0714",
      "DATA",
      [
        "storage",
        "00c7a798",
        null,
        "pointer"
      ]
    ],
    [
      "007f0bf4",
      "DATA",
      [
        "storage",
        "00c77f30",
        null,
        "pointer"
      ]
    ],
    [
      "007f0c30",
      "DATA",
      [
        "storage",
        "00c74410",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007f0714",
      "DATA",
      [
        "storage",
        "00c7ab98",
        null,
        "pointer"
      ]
    ],
    [
      "007f0bf4",
      "DATA",
      [
        "storage",
        "00c78330",
        null,
        "pointer"
      ]
    ],
    [
      "007f0c30",
      "DATA",
      [
        "storage",
        "00c74810",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f0714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f06b4.md#insn-007f0714) · [`007f0b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f06b4.md#insn-007f0b74) · [`007f0bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f06b4.md#insn-007f0bb0)
- 新版 `007f0754`（命令位置の公開資料なし） · `007f0bb4`（命令位置の公開資料なし） · `007f0bf0`（命令位置の公開資料なし）

~~~diff
- 007f0714 ["INT_ADD", "register:40f0:8", ["const:7f0714:8", "const:4:8"]]
- 007f0714 ["CALL", null, ["callee:00c53d00:8"]]
+ 007f0754 ["INT_ADD", "register:40f0:8", ["const:7f0754:8", "const:4:8"]]
+ 007f0754 ["CALL", null, ["callee:00c53d00:8"]]
- 007f0714 bytes 738c1194
+ 007f0754 bytes 6b8d1194
- 007f0b74 ["INT_ADD", "register:40f0:8", ["const:7f0b74:8", "const:4:8"]]
- 007f0b74 ["CALL", null, ["callee:00c57e80:8"]]
+ 007f0bb4 ["INT_ADD", "register:40f0:8", ["const:7f0bb4:8", "const:4:8"]]
+ 007f0bb4 ["CALL", null, ["callee:00c57e80:8"]]
- 007f0b74 bytes c39b1194
+ 007f0bb4 bytes b39c1194
- 007f0bb0 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 007f0bb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f0bb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f0bb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f0bf0 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 007f0bf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f0bf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f0bf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f0bb0 bytes 08c13c91
+ 007f0bf0 bytes 08c10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95f02fc7e2052df15e6cd658ac8c952a"></a>

### [`007f0d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0d94.md) → [`007f0dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0dd4.md) FUN_007f0dd4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007f0c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0c58.md) [`007f0d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0d94.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`007f0c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0c98.md) [`007f0dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0dd4.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

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
    "old": {
      "definition_site": "007f0ef8",
      "incomplete_value": false,
      "site": "007f0f00",
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
            "const:f13:8"
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
    "old": {
      "definition_site": "007f0f1c",
      "incomplete_value": false,
      "site": "007f0f28",
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
            "const:ea9:8"
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
    "old": {
      "definition_site": "007f1050",
      "incomplete_value": false,
      "site": "007f1058",
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
            "const:da7:8"
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
      "007f0f38",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "007f0f5c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "007f1090",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007f0f38",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "007f0f5c",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "007f1090",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f0f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0d94.md#insn-007f0f00) · [`007f0f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0d94.md#insn-007f0f28) · [`007f1058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f0/007f0d94.md#insn-007f1058)
- 新版 `007f0f40`（命令位置の公開資料なし） · `007f0f68`（命令位置の公開資料なし） · `007f1098`（命令位置の公開資料なし）

~~~diff
- 007f0f00 ["INT_ADD", "register:40f0:8", ["const:7f0f00:8", "const:4:8"]]
- 007f0f00 ["CALL", null, ["callee:00441e94:8"]]
+ 007f0f40 ["INT_ADD", "register:40f0:8", ["const:7f0f40:8", "const:4:8"]]
+ 007f0f40 ["CALL", null, ["callee:00441e94:8"]]
- 007f0f00 bytes d543f197
+ 007f0f40 bytes d543f197
- 007f0f28 ["INT_ADD", "register:40f0:8", ["const:7f0f28:8", "const:4:8"]]
- 007f0f28 ["CALL", null, ["callee:004427f4:8"]]
+ 007f0f68 ["INT_ADD", "register:40f0:8", ["const:7f0f68:8", "const:4:8"]]
+ 007f0f68 ["CALL", null, ["callee:004427f4:8"]]
- 007f0f28 bytes 2346f197
+ 007f0f68 bytes 2346f197
- 007f1058 ["INT_ADD", "register:40f0:8", ["const:7f1058:8", "const:4:8"]]
- 007f1058 ["CALL", null, ["callee:00441e94:8"]]
+ 007f1098 ["INT_ADD", "register:40f0:8", ["const:7f1098:8", "const:4:8"]]
+ 007f1098 ["CALL", null, ["callee:00441e94:8"]]
- 007f1058 bytes 7f43f197
+ 007f1098 bytes 7f43f197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-974de522809b6475ac565b13146d6038"></a>

### [`007f1e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e50.md) → [`007f1e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1e90.md) FUN_007f1e90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007f1854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1854.md) [`0090113c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00901/0090113c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`007f1894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1894.md) [`009012d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00901/009012d8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
    "old": {
      "definition_site": "007f1e5c",
      "incomplete_value": false,
      "site": "007f1e60",
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
            "const:f0c:8"
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
      "007f1e9c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f1e9c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f1e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e50.md#insn-007f1e60) · [`007f1e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e50.md#insn-007f1e5c)
- 新版 `007f1ea0`（命令位置の公開資料なし） · `007f1e9c`（命令位置の公開資料なし）

~~~diff
- 007f1e60 ["INT_ADD", "register:40f0:8", ["const:7f1e60:8", "const:4:8"]]
- 007f1e60 ["CALL", null, ["callee:0043b778:8"]]
+ 007f1ea0 ["INT_ADD", "register:40f0:8", ["const:7f1ea0:8", "const:4:8"]]
+ 007f1ea0 ["CALL", null, ["callee:0043b778:8"]]
- 007f1e60 bytes 3626f197
+ 007f1ea0 bytes 3626f197
- 007f1e5c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 007f1e5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007f1e5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007f1e5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007f1e9c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 007f1e9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007f1e9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007f1e9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007f1e5c bytes 00303c91
+ 007f1e9c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56da419c2c8572f9f4f0fc12610e9799"></a>

### [`007f1e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e64.md) → [`007f1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ea4.md) FUN_007f1ea4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`0080eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080e/0080eeb0.md) [`00810848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00810/00810848.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`0080eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080e/0080eef0.md) [`00810888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00810/00810888.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
    "old": {
      "definition_site": "007f1e70",
      "incomplete_value": false,
      "site": "007f1e74",
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
            "const:f0c:8"
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
      "007f1eb0",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f1eb0",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f1e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e64.md#insn-007f1e74) · [`007f1e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e64.md#insn-007f1e70)
- 新版 `007f1eb4`（命令位置の公開資料なし） · `007f1eb0`（命令位置の公開資料なし）

~~~diff
- 007f1e74 ["INT_ADD", "register:40f0:8", ["const:7f1e74:8", "const:4:8"]]
- 007f1e74 ["CALL", null, ["callee:0043b778:8"]]
+ 007f1eb4 ["INT_ADD", "register:40f0:8", ["const:7f1eb4:8", "const:4:8"]]
+ 007f1eb4 ["CALL", null, ["callee:0043b778:8"]]
- 007f1e74 bytes 3126f197
+ 007f1eb4 bytes 3126f197
- 007f1e70 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 007f1e70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007f1e70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007f1e70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007f1eb0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 007f1eb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007f1eb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007f1eb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007f1e70 bytes 00303c91
+ 007f1eb0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5efdcc1ab373610400920c3f2c5b4260"></a>

### [`007f1e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e90.md) → [`007f1ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ed0.md) FUN_007f1ed0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f1ea4",
      "incomplete_value": false,
      "site": "007f1ea8",
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
            "const:7b8:8"
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
      "007f1ee8",
      "DATA",
      [
        "storage",
        "00c7a7b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f1ee8",
      "DATA",
      [
        "storage",
        "00c7abb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f1e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e90.md#insn-007f1e9c) · [`007f1ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1e90.md#insn-007f1ea4)
- 新版 `007f1edc`（命令位置の公開資料なし） · `007f1ee4`（命令位置の公開資料なし）

~~~diff
- 007f1e9c ["INT_ADD", "register:40f0:8", ["const:7f1e9c:8", "const:4:8"]]
- 007f1e9c ["CALL", null, ["callee:00c57e90:8"]]
+ 007f1edc ["INT_ADD", "register:40f0:8", ["const:7f1edc:8", "const:4:8"]]
+ 007f1edc ["CALL", null, ["callee:00c57e90:8"]]
- 007f1e9c bytes fd961194
+ 007f1edc bytes ed971194
- 007f1ea4 ["COPY", "tmp:0:8", ["const:7b8:8"]]
- 007f1ea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f1ea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f1ea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f1ee4 ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 007f1ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f1ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f1ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f1ea4 bytes 08e11e91
+ 007f1ee4 bytes 08e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d41869aeaf30349add39a01f90c67b4"></a>

### [`007f1ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1ecc.md) → [`007f1f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1f0c.md) FUN_007f1f0c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

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
    "old": {
      "definition_site": "007f1fb8",
      "incomplete_value": true,
      "site": "007f1fcc",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:e5e:8"
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
    "old": {
      "definition_site": "007f1fd0",
      "incomplete_value": true,
      "site": "007f1fd0",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "007f2098",
      "incomplete_value": false,
      "site": "007f2098",
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
            "const:828:8"
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
      "007f1f44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f1f60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f1fa8",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[15]"
      ]
    ]
  ],
  "added": [
    [
      "007f1f44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f1f60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f1fa8",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f1f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1ecc.md#insn-007f1f04) · [`007f1f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1ecc.md#insn-007f1f20) · [`007f1f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1ecc.md#insn-007f1f90)
- 新版 `007f1f44`（命令位置の公開資料なし） · `007f1f60`（命令位置の公開資料なし） · `007f1fd0`（命令位置の公開資料なし）

~~~diff
- 007f1f04 ["INT_ADD", "register:40f0:8", ["const:7f1f04:8", "const:4:8"]]
- 007f1f04 ["CALL", null, ["ram:47acb4:8"]]
+ 007f1f44 ["INT_ADD", "register:40f0:8", ["const:7f1f44:8", "const:4:8"]]
+ 007f1f44 ["CALL", null, ["ram:47acf4:8"]]
- 007f1f04 bytes 6c23f297
+ 007f1f44 bytes 6c23f297
- 007f1f20 ["INT_ADD", "register:40f0:8", ["const:7f1f20:8", "const:4:8"]]
- 007f1f20 ["CALL", null, ["ram:47acb4:8"]]
+ 007f1f60 ["INT_ADD", "register:40f0:8", ["const:7f1f60:8", "const:4:8"]]
+ 007f1f60 ["CALL", null, ["ram:47acf4:8"]]
- 007f1f20 bytes 6523f297
+ 007f1f60 bytes 6523f297
- 007f1f90 ["INT_ADD", "register:40f0:8", ["const:7f1f90:8", "const:4:8"]]
- 007f1f90 ["CALL", null, ["callee:008514f8:8"]]
+ 007f1fd0 ["INT_ADD", "register:40f0:8", ["const:7f1fd0:8", "const:4:8"]]
+ 007f1fd0 ["CALL", null, ["callee:008514f8:8"]]
- 007f1f90 bytes 4a7d0194
+ 007f1fd0 bytes 4a7d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e7806401cb9317708745f9cf8774768"></a>

### [`007f22f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f22f8.md) → [`007f2338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2338.md) FUN_007f2338

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f230c",
      "incomplete_value": false,
      "site": "007f2310",
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
      "007f2350",
      "DATA",
      [
        "storage",
        "00c7a828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f2350",
      "DATA",
      [
        "storage",
        "00c7ac28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f22f8.md#insn-007f2304) · [`007f230c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f22f8.md#insn-007f230c)
- 新版 `007f2344`（命令位置の公開資料なし） · `007f234c`（命令位置の公開資料なし）

~~~diff
- 007f2304 ["INT_ADD", "register:40f0:8", ["const:7f2304:8", "const:4:8"]]
- 007f2304 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f2344 ["INT_ADD", "register:40f0:8", ["const:7f2344:8", "const:4:8"]]
+ 007f2344 ["CALL", null, ["callee:00c57e90:8"]]
- 007f2304 bytes e3951194
+ 007f2344 bytes d3961194
- 007f230c ["COPY", "tmp:0:8", ["const:828:8"]]
- 007f230c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f230c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f230c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f234c ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 007f234c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f234c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f234c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f230c bytes 08a12091
+ 007f234c bytes 08a13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac07645f0592e9c6b36559bf088c70b0"></a>

### [`007f231c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f231c.md) → [`007f235c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f235c.md) FUN_007f235c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "007f2320",
      "incomplete_value": false,
      "site": "007f2324",
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
      "007f2364",
      "DATA",
      [
        "storage",
        "00c7a828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f2364",
      "DATA",
      [
        "storage",
        "00c7ac28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f231c.md#insn-007f2320)
- 新版 `007f2360`（命令位置の公開資料なし）

~~~diff
- 007f2320 ["COPY", "tmp:0:8", ["const:828:8"]]
- 007f2320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2360 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 007f2360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2320 bytes 08a12091
+ 007f2360 bytes 08a13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ded23485cbbbfb0832d19f000fef1ca"></a>

### [`007f2334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2334.md) → [`007f2374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2374.md) FUN_007f2374

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

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
    "old": {
      "definition_site": "007f23fc",
      "incomplete_value": true,
      "site": "007f240c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:303:8"
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
    "old": {
      "definition_site": "007f2410",
      "incomplete_value": true,
      "site": "007f2410",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "007f247c",
      "incomplete_value": true,
      "site": "007f248c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:303:8"
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
      "007f23c0",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[15]"
      ]
    ],
    [
      "007f23d8",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "qword"
      ]
    ],
    [
      "007f241c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007f23c0",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ],
    [
      "007f23d8",
      "DATA",
      [
        "storage",
        "00344440",
        null,
        "dword"
      ]
    ],
    [
      "007f241c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f23dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2334.md#insn-007f23dc) · [`007f24e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2334.md#insn-007f24e0) · [`007f2508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2334.md#insn-007f2508)
- 新版 `007f241c`（命令位置の公開資料なし） · `007f2520`（命令位置の公開資料なし） · `007f2548`（命令位置の公開資料なし）

~~~diff
- 007f23dc ["INT_ADD", "register:40f0:8", ["const:7f23dc:8", "const:4:8"]]
- 007f23dc ["CALL", null, ["ram:47acb4:8"]]
+ 007f241c ["INT_ADD", "register:40f0:8", ["const:7f241c:8", "const:4:8"]]
+ 007f241c ["CALL", null, ["ram:47acf4:8"]]
- 007f23dc bytes 3622f297
+ 007f241c bytes 3622f297
- 007f24e0 ["INT_ADD", "register:40f0:8", ["const:7f24e0:8", "const:4:8"]]
- 007f24e0 ["CALL", null, ["ram:48ccb8:8"]]
+ 007f2520 ["INT_ADD", "register:40f0:8", ["const:7f2520:8", "const:4:8"]]
+ 007f2520 ["CALL", null, ["ram:48ccf8:8"]]
- 007f24e0 bytes f669f297
+ 007f2520 bytes f669f297
- 007f2508 ["INT_ADD", "register:40f0:8", ["const:7f2508:8", "const:4:8"]]
- 007f2508 ["CALL", null, ["callee:00c57f60:8"]]
+ 007f2548 ["INT_ADD", "register:40f0:8", ["const:7f2548:8", "const:4:8"]]
+ 007f2548 ["CALL", null, ["callee:00c57f60:8"]]
- 007f2508 bytes 96951194
+ 007f2548 bytes 86961194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4106edfe0a2fd852e4233f6b82d6fe40"></a>

### [`007f28f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f28f0.md) → [`007f2930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2930.md) FUN_007f2930

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f2904",
      "incomplete_value": false,
      "site": "007f2908",
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
            "const:8b8:8"
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
      "007f2948",
      "DATA",
      [
        "storage",
        "00c7a8b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f2948",
      "DATA",
      [
        "storage",
        "00c7acb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f28fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f28f0.md#insn-007f28fc) · [`007f2904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f28f0.md#insn-007f2904)
- 新版 `007f293c`（命令位置の公開資料なし） · `007f2944`（命令位置の公開資料なし）

~~~diff
- 007f28fc ["INT_ADD", "register:40f0:8", ["const:7f28fc:8", "const:4:8"]]
- 007f28fc ["CALL", null, ["callee:00c57e90:8"]]
+ 007f293c ["INT_ADD", "register:40f0:8", ["const:7f293c:8", "const:4:8"]]
+ 007f293c ["CALL", null, ["callee:00c57e90:8"]]
- 007f28fc bytes 65941194
+ 007f293c bytes 55951194
- 007f2904 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 007f2904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2944 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 007f2944 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2944 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2944 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2904 bytes 08e12291
+ 007f2944 bytes 08e13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8025dc67f06cf2a35c33b04132b5cbd4"></a>

### [`007f292c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f292c.md) → [`007f296c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f296c.md) FUN_007f296c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`007defe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007defe4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`007df024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df024.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

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
      "site": "007f298c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f294c",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "007f2998",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2958",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f298c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f2998",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007f298c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f2998",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f294c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f292c.md#insn-007f294c) · [`007f2958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f292c.md#insn-007f2958) · [`007f296c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f292c.md#insn-007f296c)
- 新版 `007f298c`（命令位置の公開資料なし） · `007f2998`（命令位置の公開資料なし） · `007f29ac`（命令位置の公開資料なし）

~~~diff
- 007f294c ["INT_ADD", "register:40f0:8", ["const:7f294c:8", "const:4:8"]]
- 007f294c ["CALL", null, ["ram:47acb4:8"]]
+ 007f298c ["INT_ADD", "register:40f0:8", ["const:7f298c:8", "const:4:8"]]
+ 007f298c ["CALL", null, ["ram:47acf4:8"]]
- 007f294c bytes da20f297
+ 007f298c bytes da20f297
- 007f2958 ["INT_ADD", "register:40f0:8", ["const:7f2958:8", "const:4:8"]]
- 007f2958 ["CALL", null, ["ram:47acb4:8"]]
+ 007f2998 ["INT_ADD", "register:40f0:8", ["const:7f2998:8", "const:4:8"]]
+ 007f2998 ["CALL", null, ["ram:47acf4:8"]]
- 007f2958 bytes d720f297
+ 007f2998 bytes d720f297
- 007f296c ["INT_ADD", "register:40f0:8", ["const:7f296c:8", "const:4:8"]]
- 007f296c ["CALL", null, ["callee:008514f8:8"]]
+ 007f29ac ["INT_ADD", "register:40f0:8", ["const:7f29ac:8", "const:4:8"]]
+ 007f29ac ["CALL", null, ["callee:008514f8:8"]]
- 007f296c bytes d37a0194
+ 007f29ac bytes d37a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7bb883aef83a4da048108a587b226b4"></a>

### [`007f29d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f29d0.md) → [`007f2a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2a10.md) FUN_007f2a10

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f29f4",
      "incomplete_value": false,
      "site": "007f29f4",
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
            "const:938:8"
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
      "007f2a34",
      "DATA",
      [
        "storage",
        "00c7a938",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f2a34",
      "DATA",
      [
        "storage",
        "00c7ad38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f29e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f29d0.md#insn-007f29e4) · [`007f29f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f29d0.md#insn-007f29f0)
- 新版 `007f2a24`（命令位置の公開資料なし） · `007f2a30`（命令位置の公開資料なし）

~~~diff
- 007f29e4 ["INT_ADD", "register:40f0:8", ["const:7f29e4:8", "const:4:8"]]
- 007f29e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f2a24 ["INT_ADD", "register:40f0:8", ["const:7f2a24:8", "const:4:8"]]
+ 007f2a24 ["CALL", null, ["callee:00c57e90:8"]]
- 007f29e4 bytes 2b941194
+ 007f2a24 bytes 1b951194
- 007f29f0 ["COPY", "tmp:0:8", ["const:938:8"]]
- 007f29f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f29f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f29f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2a30 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 007f2a30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2a30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2a30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f29f0 bytes 08e12491
+ 007f2a30 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c3c992e2e3f2ec7fe97be52f3f6b3bd"></a>

### [`007f2a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2a20.md) → [`007f2a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2a60.md) FUN_007f2a60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

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
    "old": {
      "definition_site": "007f2b24",
      "incomplete_value": false,
      "site": "007f2b24",
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
            "const:9a8:8"
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
      "site": "007f2a98",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2a58",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "007f2ab4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2a74",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f2a98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f2ab4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f2af0",
      "READ",
      [
        "storage",
        "002a7c25",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f2a98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f2ab4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f2af0",
      "READ",
      [
        "storage",
        "002a7d01",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2a20.md#insn-007f2a58) · [`007f2a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2a20.md#insn-007f2a74) · [`007f2c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2a20.md#insn-007f2c04)
- 新版 `007f2a98`（命令位置の公開資料なし） · `007f2ab4`（命令位置の公開資料なし） · `007f2c44`（命令位置の公開資料なし）

~~~diff
- 007f2a58 ["INT_ADD", "register:40f0:8", ["const:7f2a58:8", "const:4:8"]]
- 007f2a58 ["CALL", null, ["ram:47acb4:8"]]
+ 007f2a98 ["INT_ADD", "register:40f0:8", ["const:7f2a98:8", "const:4:8"]]
+ 007f2a98 ["CALL", null, ["ram:47acf4:8"]]
- 007f2a58 bytes 9720f297
+ 007f2a98 bytes 9720f297
- 007f2a74 ["INT_ADD", "register:40f0:8", ["const:7f2a74:8", "const:4:8"]]
- 007f2a74 ["CALL", null, ["ram:47acb4:8"]]
+ 007f2ab4 ["INT_ADD", "register:40f0:8", ["const:7f2ab4:8", "const:4:8"]]
+ 007f2ab4 ["CALL", null, ["ram:47acf4:8"]]
- 007f2a74 bytes 9020f297
+ 007f2ab4 bytes 9020f297
- 007f2c04 ["INT_ADD", "register:40f0:8", ["const:7f2c04:8", "const:4:8"]]
- 007f2c04 ["CALL", null, ["callee:00442930:8"]]
+ 007f2c44 ["INT_ADD", "register:40f0:8", ["const:7f2c44:8", "const:4:8"]]
+ 007f2c44 ["CALL", null, ["callee:00442930:8"]]
- 007f2c04 bytes 3b3ff197
+ 007f2c44 bytes 3b3ff197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a2ded4ef054cde42d5809642d9bc751"></a>

### [`007f2cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2cf0.md) → [`007f2d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2d30.md) FUN_007f2d30

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f2d04",
      "incomplete_value": false,
      "site": "007f2d08",
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
            "const:9a8:8"
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
      "007f2d48",
      "DATA",
      [
        "storage",
        "00c7a9a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f2d48",
      "DATA",
      [
        "storage",
        "00c7ada8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2cf0.md#insn-007f2cfc) · [`007f2d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2cf0.md#insn-007f2d04)
- 新版 `007f2d3c`（命令位置の公開資料なし） · `007f2d44`（命令位置の公開資料なし）

~~~diff
- 007f2cfc ["INT_ADD", "register:40f0:8", ["const:7f2cfc:8", "const:4:8"]]
- 007f2cfc ["CALL", null, ["callee:00c57e90:8"]]
+ 007f2d3c ["INT_ADD", "register:40f0:8", ["const:7f2d3c:8", "const:4:8"]]
+ 007f2d3c ["CALL", null, ["callee:00c57e90:8"]]
- 007f2cfc bytes 65931194
+ 007f2d3c bytes 55941194
- 007f2d04 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 007f2d04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2d04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2d04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2d44 ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 007f2d44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2d44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2d04 bytes 08a12691
+ 007f2d44 bytes 08a13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30a3dc79633a340261e68391abd635ba"></a>

### [`007f2d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2d14.md) → [`007f2d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2d54.md) FUN_007f2d54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "007f2d18",
      "incomplete_value": false,
      "site": "007f2d1c",
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
            "const:9a8:8"
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
      "007f2d5c",
      "DATA",
      [
        "storage",
        "00c7a9a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f2d5c",
      "DATA",
      [
        "storage",
        "00c7ada8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2d14.md#insn-007f2d18)
- 新版 `007f2d58`（命令位置の公開資料なし）

~~~diff
- 007f2d18 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 007f2d18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2d18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2d18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2d58 ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 007f2d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2d18 bytes 08a12691
+ 007f2d58 bytes 08a13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f3b0cf22719fdc7b75efc3669306eac"></a>

### [`007f2d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2d2c.md) → [`007f2d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2d6c.md) FUN_007f2d6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "007f2d90",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2d50",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f2d90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007f2d90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2d2c.md#insn-007f2d50) · [`007f2d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2d2c.md#insn-007f2d5c)
- 新版 `007f2d90`（命令位置の公開資料なし） · `007f2d9c`（命令位置の公開資料なし）

~~~diff
- 007f2d50 ["INT_ADD", "register:40f0:8", ["const:7f2d50:8", "const:4:8"]]
- 007f2d50 ["CALL", null, ["ram:47acb4:8"]]
+ 007f2d90 ["INT_ADD", "register:40f0:8", ["const:7f2d90:8", "const:4:8"]]
+ 007f2d90 ["CALL", null, ["ram:47acf4:8"]]
- 007f2d50 bytes d91ff297
+ 007f2d90 bytes d91ff297
- 007f2d5c ["INT_ADD", "register:40f0:8", ["const:7f2d5c:8", "const:4:8"]]
- 007f2d5c ["CALL", null, ["callee:0047cdd4:8"]]
+ 007f2d9c ["INT_ADD", "register:40f0:8", ["const:7f2d9c:8", "const:4:8"]]
+ 007f2d9c ["CALL", null, ["callee:0047cdd4:8"]]
- 007f2d5c bytes 0e28f297
+ 007f2d9c bytes 0e28f297
~~~


<a id="compare-c476630133bc6068a007059c1456b2a4"></a>

### [`007f2da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2da0.md) → [`007f2de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2de0.md) FUN_007f2de0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f2dc4",
      "incomplete_value": false,
      "site": "007f2dc4",
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
            "const:a38:8"
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
      "007f2e04",
      "DATA",
      [
        "storage",
        "00c7aa38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f2e04",
      "DATA",
      [
        "storage",
        "00c7ae38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2da0.md#insn-007f2db4) · [`007f2dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2da0.md#insn-007f2dc0)
- 新版 `007f2df4`（命令位置の公開資料なし） · `007f2e00`（命令位置の公開資料なし）

~~~diff
- 007f2db4 ["INT_ADD", "register:40f0:8", ["const:7f2db4:8", "const:4:8"]]
- 007f2db4 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f2df4 ["INT_ADD", "register:40f0:8", ["const:7f2df4:8", "const:4:8"]]
+ 007f2df4 ["CALL", null, ["callee:00c57e90:8"]]
- 007f2db4 bytes 37931194
+ 007f2df4 bytes 27941194
- 007f2dc0 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 007f2dc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2dc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2dc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f2e00 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 007f2e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f2e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2dc0 bytes 08e12891
+ 007f2e00 bytes 08e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f0508579a52213eec83ce1854fa354a"></a>

### [`007f2df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2df0.md) → [`007f2e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f2/007f2e30.md) FUN_007f2e30

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`008b6f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f0c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`008b6f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f50.md)

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
      "site": "007f2ef4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2eb4",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "007f2f10",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f2ed0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f2ef4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f2f10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f2f50",
      "DATA",
      [
        "storage",
        "003c7698",
        null,
        "uleb128"
      ]
    ]
  ],
  "added": [
    [
      "007f2ef4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f2f10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f2f50",
      "DATA",
      [
        "storage",
        "003c7698",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2df0.md#insn-007f2eb4) · [`007f2ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2df0.md#insn-007f2ed0) · [`007f2e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2df0.md#insn-007f2e10)
- 新版 `007f2ef4`（命令位置の公開資料なし） · `007f2f10`（命令位置の公開資料なし） · `007f2e50`（命令位置の公開資料なし）

~~~diff
- 007f2eb4 ["INT_ADD", "register:40f0:8", ["const:7f2eb4:8", "const:4:8"]]
- 007f2eb4 ["CALL", null, ["ram:47acb4:8"]]
+ 007f2ef4 ["INT_ADD", "register:40f0:8", ["const:7f2ef4:8", "const:4:8"]]
+ 007f2ef4 ["CALL", null, ["ram:47acf4:8"]]
- 007f2eb4 bytes 801ff297
+ 007f2ef4 bytes 801ff297
- 007f2ed0 ["INT_ADD", "register:40f0:8", ["const:7f2ed0:8", "const:4:8"]]
- 007f2ed0 ["CALL", null, ["ram:47acb4:8"]]
+ 007f2f10 ["INT_ADD", "register:40f0:8", ["const:7f2f10:8", "const:4:8"]]
+ 007f2f10 ["CALL", null, ["ram:47acf4:8"]]
- 007f2ed0 bytes 791ff297
+ 007f2f10 bytes 791ff297
- 007f2e10 ["INT_ADD", "register:40f0:8", ["const:7f2e10:8", "const:4:8"]]
- 007f2e10 ["CALL", null, ["callee:008b6f50:8"]]
+ 007f2e50 ["INT_ADD", "register:40f0:8", ["const:7f2e50:8", "const:4:8"]]
+ 007f2e50 ["CALL", null, ["callee:008b6f50:8"]]
- 007f2e10 bytes 3f100394
+ 007f2e50 bytes 40100394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69f0eee0d06cfc975e53f14ae67dd171"></a>

### [`007f2fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2fc0.md) → [`007f3000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3000.md) FUN_007f3000

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f2fe4",
      "incomplete_value": false,
      "site": "007f2fe4",
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
            "const:ab8:8"
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
      "007f3024",
      "DATA",
      [
        "storage",
        "00c7aab8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3024",
      "DATA",
      [
        "storage",
        "00c7aeb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f2fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2fc0.md#insn-007f2fd4) · [`007f2fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2fc0.md#insn-007f2fe0)
- 新版 `007f3014`（命令位置の公開資料なし） · `007f3020`（命令位置の公開資料なし）

~~~diff
- 007f2fd4 ["INT_ADD", "register:40f0:8", ["const:7f2fd4:8", "const:4:8"]]
- 007f2fd4 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f3014 ["INT_ADD", "register:40f0:8", ["const:7f3014:8", "const:4:8"]]
+ 007f3014 ["CALL", null, ["callee:00c57e90:8"]]
- 007f2fd4 bytes af921194
+ 007f3014 bytes 9f931194
- 007f2fe0 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 007f2fe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f2fe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f2fe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3020 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 007f3020 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3020 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3020 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f2fe0 bytes 08e12a91
+ 007f3020 bytes 08e13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d32a2b687ef6864e45f01cb6da2969a"></a>

### [`007f3010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3010.md) → [`007f3050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3050.md) FUN_007f3050

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`006746e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00674/006746e4.md) [`00675b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675b00.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00674724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00674/00674724.md) [`00675b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00675/00675b40.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md)

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
      "site": "007f3090",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3050",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "007f30ac",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f306c",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f3090",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f30ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007f3090",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f30ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3010.md#insn-007f3050) · [`007f306c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3010.md#insn-007f306c) · [`007f30cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3010.md#insn-007f30cc)
- 新版 `007f3090`（命令位置の公開資料なし） · `007f30ac`（命令位置の公開資料なし） · `007f310c`（命令位置の公開資料なし）

~~~diff
- 007f3050 ["INT_ADD", "register:40f0:8", ["const:7f3050:8", "const:4:8"]]
- 007f3050 ["CALL", null, ["ram:47acb4:8"]]
+ 007f3090 ["INT_ADD", "register:40f0:8", ["const:7f3090:8", "const:4:8"]]
+ 007f3090 ["CALL", null, ["ram:47acf4:8"]]
- 007f3050 bytes 191ff297
+ 007f3090 bytes 191ff297
- 007f306c ["INT_ADD", "register:40f0:8", ["const:7f306c:8", "const:4:8"]]
- 007f306c ["CALL", null, ["ram:47acb4:8"]]
+ 007f30ac ["INT_ADD", "register:40f0:8", ["const:7f30ac:8", "const:4:8"]]
+ 007f30ac ["CALL", null, ["ram:47acf4:8"]]
- 007f306c bytes 121ff297
+ 007f30ac bytes 121ff297
- 007f30cc ["INT_ADD", "register:40f0:8", ["const:7f30cc:8", "const:4:8"]]
- 007f30cc ["CALL", null, ["callee:00675b40:8"]]
+ 007f310c ["INT_ADD", "register:40f0:8", ["const:7f310c:8", "const:4:8"]]
+ 007f310c ["CALL", null, ["callee:00675b40:8"]]
- 007f30cc bytes 8d0afa97
+ 007f310c bytes 8d0afa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab01d7be0d8e129cb5e8cf6f13798a9d"></a>

### [`007f3204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3204.md) → [`007f3244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3244.md) FUN_007f3244

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f3228",
      "incomplete_value": false,
      "site": "007f3228",
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
            "const:b38:8"
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
      "007f3268",
      "DATA",
      [
        "storage",
        "00c7ab38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3268",
      "DATA",
      [
        "storage",
        "00c7af38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3204.md#insn-007f3218) · [`007f3224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3204.md#insn-007f3224)
- 新版 `007f3258`（命令位置の公開資料なし） · `007f3264`（命令位置の公開資料なし）

~~~diff
- 007f3218 ["INT_ADD", "register:40f0:8", ["const:7f3218:8", "const:4:8"]]
- 007f3218 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f3258 ["INT_ADD", "register:40f0:8", ["const:7f3258:8", "const:4:8"]]
+ 007f3258 ["CALL", null, ["callee:00c57e90:8"]]
- 007f3218 bytes 1e921194
+ 007f3258 bytes 0e931194
- 007f3224 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 007f3224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3264 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 007f3264 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3264 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3264 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3224 bytes 08e12c91
+ 007f3264 bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58a5d8d49bcf82cf5dbbd39c571ae26e"></a>

### [`007f3254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3254.md) → [`007f3294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3294.md) FUN_007f3294

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`007f34d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f34d8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007f3518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3518.md)

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
    "old": {
      "definition_site": "007f3344",
      "incomplete_value": false,
      "site": "007f334c",
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
            "const:ba8:8"
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
      "site": "007f32c8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3288",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f32c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f3318",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "007f3358",
      "READ",
      [
        "storage",
        "002b4b6a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f32c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f3318",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "007f3358",
      "READ",
      [
        "storage",
        "002b4baa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3254.md#insn-007f3288) · [`007f32bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3254.md#insn-007f32bc) · [`007f3310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3254.md#insn-007f3310)
- 新版 `007f32c8`（命令位置の公開資料なし） · `007f32fc`（命令位置の公開資料なし） · `007f3350`（命令位置の公開資料なし）

~~~diff
- 007f3288 ["INT_ADD", "register:40f0:8", ["const:7f3288:8", "const:4:8"]]
- 007f3288 ["CALL", null, ["ram:47acb4:8"]]
+ 007f32c8 ["INT_ADD", "register:40f0:8", ["const:7f32c8:8", "const:4:8"]]
+ 007f32c8 ["CALL", null, ["ram:47acf4:8"]]
- 007f3288 bytes 8b1ef297
+ 007f32c8 bytes 8b1ef297
- 007f32bc ["INT_ADD", "register:40f0:8", ["const:7f32bc:8", "const:4:8"]]
- 007f32bc ["CALL", null, ["callee:0048ce50:8"]]
+ 007f32fc ["INT_ADD", "register:40f0:8", ["const:7f32fc:8", "const:4:8"]]
+ 007f32fc ["CALL", null, ["callee:0048ce50:8"]]
- 007f32bc bytes d566f297
+ 007f32fc bytes d566f297
- 007f3310 ["COPY", "tmp:0:8", ["const:b6a:8"]]
- 007f3310 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007f3310 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007f3310 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007f3350 ["COPY", "tmp:0:8", ["const:baa:8"]]
+ 007f3350 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007f3350 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007f3350 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007f3310 bytes 29a92d91
+ 007f3350 bytes 29a92e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac37ddafa5fdde3943a4a58d261afcd6"></a>

### [`007f34a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f34a4.md) → [`007f34e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f34e4.md) FUN_007f34e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f34b8",
      "incomplete_value": false,
      "site": "007f34bc",
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
            "const:ba8:8"
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
      "007f34fc",
      "DATA",
      [
        "storage",
        "00c7aba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f34fc",
      "DATA",
      [
        "storage",
        "00c7afa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f34b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f34a4.md#insn-007f34b0) · [`007f34b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f34a4.md#insn-007f34b8)
- 新版 `007f34f0`（命令位置の公開資料なし） · `007f34f8`（命令位置の公開資料なし）

~~~diff
- 007f34b0 ["INT_ADD", "register:40f0:8", ["const:7f34b0:8", "const:4:8"]]
- 007f34b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f34f0 ["INT_ADD", "register:40f0:8", ["const:7f34f0:8", "const:4:8"]]
+ 007f34f0 ["CALL", null, ["callee:00c57e90:8"]]
- 007f34b0 bytes 78911194
+ 007f34f0 bytes 68921194
- 007f34b8 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 007f34b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f34b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f34b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f34f8 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 007f34f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f34f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f34f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f34b8 bytes 08a12e91
+ 007f34f8 bytes 08a13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbb0a2c2b2a3fb69cd140071e533ed3f"></a>

### [`007f34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f34c8.md) → [`007f3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3508.md) FUN_007f3508

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "007f34cc",
      "incomplete_value": false,
      "site": "007f34d0",
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
      "007f3510",
      "DATA",
      [
        "storage",
        "00c7aba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3510",
      "DATA",
      [
        "storage",
        "00c7afa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f34cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f34c8.md#insn-007f34cc)
- 新版 `007f350c`（命令位置の公開資料なし）

~~~diff
- 007f34cc ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 007f34cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f34cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f34cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f350c ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 007f350c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f350c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f350c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f34cc bytes 08a12e91
+ 007f350c bytes 08a13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a0ed77599939b2e1acd8dc11bbdd300"></a>

### [`007f3524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3524.md) → [`007f3564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3564.md) FUN_007f3564

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f3548",
      "incomplete_value": false,
      "site": "007f3548",
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
            "const:c38:8"
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
      "007f3588",
      "DATA",
      [
        "storage",
        "00c7ac38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3588",
      "DATA",
      [
        "storage",
        "00c7b038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3524.md#insn-007f3538) · [`007f3540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3524.md#insn-007f3540) · [`007f3544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3524.md#insn-007f3544)
- 新版 `007f3578`（命令位置の公開資料なし） · `007f3580`（命令位置の公開資料なし） · `007f3584`（命令位置の公開資料なし）

~~~diff
- 007f3538 ["INT_ADD", "register:40f0:8", ["const:7f3538:8", "const:4:8"]]
- 007f3538 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f3578 ["INT_ADD", "register:40f0:8", ["const:7f3578:8", "const:4:8"]]
+ 007f3578 ["CALL", null, ["callee:00c57e90:8"]]
- 007f3538 bytes 56911194
+ 007f3578 bytes 46921194
- 007f3540 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 007f3580 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 007f3540 bytes 282400f0
+ 007f3580 bytes 48240090
- 007f3544 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 007f3544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3584 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 007f3584 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3584 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3584 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3544 bytes 08e13091
+ 007f3584 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff62e9ea009685a67d14c985a9552566"></a>

### [`007f3618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3618.md) → [`007f3658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3658.md) FUN_007f3658

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f363c",
      "incomplete_value": false,
      "site": "007f363c",
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
      "007f367c",
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
      "007f367c",
      "DATA",
      [
        "storage",
        "00c7b0b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f362c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3618.md#insn-007f362c) · [`007f3634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3618.md#insn-007f3634) · [`007f3638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3618.md#insn-007f3638)
- 新版 `007f366c`（命令位置の公開資料なし） · `007f3674`（命令位置の公開資料なし） · `007f3678`（命令位置の公開資料なし）

~~~diff
- 007f362c ["INT_ADD", "register:40f0:8", ["const:7f362c:8", "const:4:8"]]
- 007f362c ["CALL", null, ["callee:00c57e90:8"]]
+ 007f366c ["INT_ADD", "register:40f0:8", ["const:7f366c:8", "const:4:8"]]
+ 007f366c ["CALL", null, ["callee:00c57e90:8"]]
- 007f362c bytes 19911194
+ 007f366c bytes 09921194
- 007f3634 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 007f3674 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 007f3634 bytes 282400f0
+ 007f3674 bytes 48240090
- 007f3638 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 007f3638 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3638 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3638 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3678 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 007f3678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3638 bytes 08e13291
+ 007f3678 bytes 08e10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c82f934e1526c8923084827783b3452"></a>

### [`007f3668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3668.md) → [`007f36a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f36a8.md) FUN_007f36a8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`007f3998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3998.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007f39d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f39d8.md)

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
    "old": {
      "definition_site": "007f3798",
      "incomplete_value": false,
      "site": "007f37a0",
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
            "const:d28:8"
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
      "site": "007f36e0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f36a0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "007f36fc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f36bc",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f36e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f36fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f3788",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "007f36e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f36fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f3788",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f36a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3668.md#insn-007f36a0) · [`007f36bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3668.md#insn-007f36bc) · [`007f36fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3668.md#insn-007f36fc)
- 新版 `007f36e0`（命令位置の公開資料なし） · `007f36fc`（命令位置の公開資料なし） · `007f373c`（命令位置の公開資料なし）

~~~diff
- 007f36a0 ["INT_ADD", "register:40f0:8", ["const:7f36a0:8", "const:4:8"]]
- 007f36a0 ["CALL", null, ["ram:47acb4:8"]]
+ 007f36e0 ["INT_ADD", "register:40f0:8", ["const:7f36e0:8", "const:4:8"]]
+ 007f36e0 ["CALL", null, ["ram:47acf4:8"]]
- 007f36a0 bytes 851df297
+ 007f36e0 bytes 851df297
- 007f36bc ["INT_ADD", "register:40f0:8", ["const:7f36bc:8", "const:4:8"]]
- 007f36bc ["CALL", null, ["ram:47acb4:8"]]
+ 007f36fc ["INT_ADD", "register:40f0:8", ["const:7f36fc:8", "const:4:8"]]
+ 007f36fc ["CALL", null, ["ram:47acf4:8"]]
- 007f36bc bytes 7e1df297
+ 007f36fc bytes 7e1df297
- 007f36fc ["INT_ADD", "register:40f0:8", ["const:7f36fc:8", "const:4:8"]]
- 007f36fc ["CALL", null, ["callee:009e0fc0:8"]]
+ 007f373c ["INT_ADD", "register:40f0:8", ["const:7f373c:8", "const:4:8"]]
+ 007f373c ["CALL", null, ["callee:009e0fc0:8"]]
- 007f36fc bytes cab50794
+ 007f373c bytes 21b60794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b6372e30073377d6fe246deb308e037"></a>

### [`007f3964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3964.md) → [`007f39a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f39a4.md) FUN_007f39a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f3978",
      "incomplete_value": false,
      "site": "007f397c",
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
            "const:d28:8"
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
      "007f39bc",
      "DATA",
      [
        "storage",
        "00c7ad28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f39bc",
      "DATA",
      [
        "storage",
        "00c7b128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3964.md#insn-007f3970) · [`007f3974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3964.md#insn-007f3974) · [`007f3978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3964.md#insn-007f3978)
- 新版 `007f39b0`（命令位置の公開資料なし） · `007f39b4`（命令位置の公開資料なし） · `007f39b8`（命令位置の公開資料なし）

~~~diff
- 007f3970 ["INT_ADD", "register:40f0:8", ["const:7f3970:8", "const:4:8"]]
- 007f3970 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f39b0 ["INT_ADD", "register:40f0:8", ["const:7f39b0:8", "const:4:8"]]
+ 007f39b0 ["CALL", null, ["callee:00c57e90:8"]]
- 007f3970 bytes 48901194
+ 007f39b0 bytes 38911194
- 007f3974 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 007f39b4 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 007f3974 bytes 282400f0
+ 007f39b4 bytes 48240090
- 007f3978 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007f3978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f39b8 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 007f39b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f39b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f39b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3978 bytes 08a13491
+ 007f39b8 bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09656703a79c53ae59d6ac2fab4a807f"></a>

### [`007f3988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3988.md) → [`007f39c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f39c8.md) FUN_007f39c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
    "old": {
      "definition_site": "007f398c",
      "incomplete_value": false,
      "site": "007f3990",
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
            "const:d28:8"
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
      "007f39d0",
      "DATA",
      [
        "storage",
        "00c7ad28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f39d0",
      "DATA",
      [
        "storage",
        "00c7b128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3988.md#insn-007f3988) · [`007f398c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3988.md#insn-007f398c)
- 新版 `007f39c8`（命令位置の公開資料なし） · `007f39cc`（命令位置の公開資料なし）

~~~diff
- 007f3988 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 007f39c8 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 007f3988 bytes 282400f0
+ 007f39c8 bytes 48240090
- 007f398c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 007f398c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f398c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f398c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f39cc ["COPY", "tmp:0:8", ["const:128:8"]]
+ 007f39cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f39cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f39cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f398c bytes 08a13491
+ 007f39cc bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25049e67212a6605f149e5d699b6df1c"></a>

### [`007f39e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f39e4.md) → [`007f3a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3a24.md) FUN_007f3a24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f3a08",
      "incomplete_value": false,
      "site": "007f3a08",
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
            "const:db8:8"
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
      "007f3a48",
      "DATA",
      [
        "storage",
        "00c7adb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3a48",
      "DATA",
      [
        "storage",
        "00c7b1b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f39f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f39e4.md#insn-007f39f8) · [`007f3a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f39e4.md#insn-007f3a00) · [`007f3a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f39e4.md#insn-007f3a04)
- 新版 `007f3a38`（命令位置の公開資料なし） · `007f3a40`（命令位置の公開資料なし） · `007f3a44`（命令位置の公開資料なし）

~~~diff
- 007f39f8 ["INT_ADD", "register:40f0:8", ["const:7f39f8:8", "const:4:8"]]
- 007f39f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f3a38 ["INT_ADD", "register:40f0:8", ["const:7f3a38:8", "const:4:8"]]
+ 007f3a38 ["CALL", null, ["callee:00c57e90:8"]]
- 007f39f8 bytes 26901194
+ 007f3a38 bytes 16911194
- 007f3a00 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 007f3a40 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 007f3a00 bytes 282400f0
+ 007f3a40 bytes 48240090
- 007f3a04 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 007f3a04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3a04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3a04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3a44 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 007f3a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3a04 bytes 08e13691
+ 007f3a44 bytes 08e10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8e238882a2399ee991fb86bc6de47f8"></a>

### [`007f3d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3d7c.md) → [`007f3dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3dbc.md) FUN_007f3dbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f3d90",
      "incomplete_value": false,
      "site": "007f3d94",
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
            "const:e28:8"
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
      "007f3dd4",
      "DATA",
      [
        "storage",
        "00c7ae28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f3dd4",
      "DATA",
      [
        "storage",
        "00c7b228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3d7c.md#insn-007f3d88) · [`007f3d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3d7c.md#insn-007f3d8c) · [`007f3d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3d7c.md#insn-007f3d90)
- 新版 `007f3dc8`（命令位置の公開資料なし） · `007f3dcc`（命令位置の公開資料なし） · `007f3dd0`（命令位置の公開資料なし）

~~~diff
- 007f3d88 ["INT_ADD", "register:40f0:8", ["const:7f3d88:8", "const:4:8"]]
- 007f3d88 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f3dc8 ["INT_ADD", "register:40f0:8", ["const:7f3dc8:8", "const:4:8"]]
+ 007f3dc8 ["CALL", null, ["callee:00c57e90:8"]]
- 007f3d88 bytes 428f1194
+ 007f3dc8 bytes 32901194
- 007f3d8c ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 007f3dcc ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 007f3d8c bytes 282400f0
+ 007f3dcc bytes 48240090
- 007f3d90 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 007f3d90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f3d90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f3d90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f3dd0 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 007f3dd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3dd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f3dd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f3d90 bytes 08a13891
+ 007f3dd0 bytes 08a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88ed20dfe89ce3aae1811ec5eeab1de3"></a>

### [`007f3db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3db8.md) → [`007f3df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3df8.md) FUN_007f3df8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "007f3e1c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f3ddc",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f3e1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007f3e1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f3ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3db8.md#insn-007f3ddc) · [`007f3de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3db8.md#insn-007f3de8)
- 新版 `007f3e1c`（命令位置の公開資料なし） · `007f3e28`（命令位置の公開資料なし）

~~~diff
- 007f3ddc ["INT_ADD", "register:40f0:8", ["const:7f3ddc:8", "const:4:8"]]
- 007f3ddc ["CALL", null, ["ram:47acb4:8"]]
+ 007f3e1c ["INT_ADD", "register:40f0:8", ["const:7f3e1c:8", "const:4:8"]]
+ 007f3e1c ["CALL", null, ["ram:47acf4:8"]]
- 007f3ddc bytes b61bf297
+ 007f3e1c bytes b61bf297
- 007f3de8 ["INT_ADD", "register:40f0:8", ["const:7f3de8:8", "const:4:8"]]
- 007f3de8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007f3e28 ["INT_ADD", "register:40f0:8", ["const:7f3e28:8", "const:4:8"]]
+ 007f3e28 ["CALL", null, ["callee:0047cdd4:8"]]
- 007f3de8 bytes eb23f297
+ 007f3e28 bytes eb23f297
~~~


<a id="compare-20d820c8959f040aa338d13b0934e257"></a>

### [`007f3e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3e4c.md) → [`007f3e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f3/007f3e8c.md) FUN_007f3e8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 10件 [`006d734c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d734c.md) [`006d7610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7610.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`006d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d76a4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 10件 [`006d738c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d738c.md) [`006d7650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7650.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`006d76e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76e4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

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
    "old": {
      "definition_site": "007f410c",
      "incomplete_value": false,
      "site": "007f4110",
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
            "const:f04:8"
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
      "007f414c",
      "PARAM",
      [
        "storage",
        "002a9f04",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f414c",
      "PARAM",
      [
        "storage",
        "002a9fd1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f4110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3e4c.md#insn-007f4110) · [`007f3ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3e4c.md#insn-007f3ecc) · [`007f3eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3e4c.md#insn-007f3eec)
- 新版 `007f4150`（命令位置の公開資料なし） · `007f3f0c`（命令位置の公開資料なし） · `007f3f2c`（命令位置の公開資料なし）

~~~diff
- 007f4110 ["INT_ADD", "register:40f0:8", ["const:7f4110:8", "const:4:8"]]
- 007f4110 ["CALL", null, ["callee:006d7650:8"]]
+ 007f4150 ["INT_ADD", "register:40f0:8", ["const:7f4150:8", "const:4:8"]]
+ 007f4150 ["CALL", null, ["callee:006d7650:8"]]
- 007f4110 bytes 408dfb97
+ 007f4150 bytes 408dfb97
- 007f3ecc ["INT_ADD", "register:40f0:8", ["const:7f3ecc:8", "const:4:8"]]
- 007f3ecc ["CALL", null, ["callee:00c57e90:8"]]
+ 007f3f0c ["INT_ADD", "register:40f0:8", ["const:7f3f0c:8", "const:4:8"]]
+ 007f3f0c ["CALL", null, ["callee:00c57e90:8"]]
- 007f3ecc bytes f18e1194
+ 007f3f0c bytes e18f1194
- 007f3eec ["INT_ADD", "register:40f0:8", ["const:7f3eec:8", "const:4:8"]]
- 007f3eec ["CALL", null, ["callee:00c58090:8"]]
+ 007f3f2c ["INT_ADD", "register:40f0:8", ["const:7f3f2c:8", "const:4:8"]]
+ 007f3f2c ["CALL", null, ["callee:00c58090:8"]]
- 007f3eec bytes 698f1194
+ 007f3f2c bytes 59901194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3faa67fb3aa4ca00cb0d6e92510e42d"></a>

### [`007f4150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4150.md) → [`007f4190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4190.md) FUN_007f4190

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`006d7610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7610.md) [`006d7b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7b50.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`006d7650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7650.md) [`006d7b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d7b90.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f44f8",
      "incomplete_value": false,
      "site": "007f44fc",
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
            "const:afb:8"
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
      "007f4538",
      "PARAM",
      [
        "storage",
        "002a7afb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f4538",
      "PARAM",
      [
        "storage",
        "002a7bd7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f44fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4150.md#insn-007f44fc) · [`007f41e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4150.md#insn-007f41e0) · [`007f4200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4150.md#insn-007f4200)
- 新版 `007f453c`（命令位置の公開資料なし） · `007f4220`（命令位置の公開資料なし） · `007f4240`（命令位置の公開資料なし）

~~~diff
- 007f44fc ["INT_ADD", "register:40f0:8", ["const:7f44fc:8", "const:4:8"]]
- 007f44fc ["CALL", null, ["callee:006d7650:8"]]
+ 007f453c ["INT_ADD", "register:40f0:8", ["const:7f453c:8", "const:4:8"]]
+ 007f453c ["CALL", null, ["callee:006d7650:8"]]
- 007f44fc bytes 458cfb97
+ 007f453c bytes 458cfb97
- 007f41e0 ["INT_ADD", "register:40f0:8", ["const:7f41e0:8", "const:4:8"]]
- 007f41e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f4220 ["INT_ADD", "register:40f0:8", ["const:7f4220:8", "const:4:8"]]
+ 007f4220 ["CALL", null, ["callee:00c57e90:8"]]
- 007f41e0 bytes 2c8e1194
+ 007f4220 bytes 1c8f1194
- 007f4200 ["INT_ADD", "register:40f0:8", ["const:7f4200:8", "const:4:8"]]
- 007f4200 ["CALL", null, ["callee:00c58090:8"]]
+ 007f4240 ["INT_ADD", "register:40f0:8", ["const:7f4240:8", "const:4:8"]]
+ 007f4240 ["CALL", null, ["callee:00c58090:8"]]
- 007f4200 bytes a48e1194
+ 007f4240 bytes 948f1194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8556f1b23d15020467ad6acdf7d13d7"></a>

### [`007f4568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4568.md) → [`007f45a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f45a8.md) FUN_007f45a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f458c",
      "incomplete_value": false,
      "site": "007f458c",
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
            "const:f30:8"
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
      "007f45cc",
      "DATA",
      [
        "storage",
        "00c7af30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f45cc",
      "DATA",
      [
        "storage",
        "00c7b330",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f457c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4568.md#insn-007f457c) · [`007f4584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4568.md#insn-007f4584) · [`007f4588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4568.md#insn-007f4588)
- 新版 `007f45bc`（命令位置の公開資料なし） · `007f45c4`（命令位置の公開資料なし） · `007f45c8`（命令位置の公開資料なし）

~~~diff
- 007f457c ["INT_ADD", "register:40f0:8", ["const:7f457c:8", "const:4:8"]]
- 007f457c ["CALL", null, ["callee:00c57e90:8"]]
+ 007f45bc ["INT_ADD", "register:40f0:8", ["const:7f45bc:8", "const:4:8"]]
+ 007f45bc ["CALL", null, ["callee:00c57e90:8"]]
- 007f457c bytes 458d1194
+ 007f45bc bytes 358e1194
- 007f4584 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 007f45c4 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 007f4584 bytes 282400d0
+ 007f45c4 bytes 282400f0
- 007f4588 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 007f4588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f4588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f4588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f45c8 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 007f45c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f45c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f45c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f4588 bytes 08c13c91
+ 007f45c8 bytes 08c10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bad696e3e6504fbadf1e9556c3eb988"></a>

### [`007f4668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4668.md) → [`007f46a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f46a8.md) FUN_007f46a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f468c",
      "incomplete_value": false,
      "site": "007f468c",
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
            "const:fb0:8"
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
      "007f46cc",
      "DATA",
      [
        "storage",
        "00c7afb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f46cc",
      "DATA",
      [
        "storage",
        "00c7b3b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f467c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4668.md#insn-007f467c) · [`007f4684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4668.md#insn-007f4684) · [`007f4688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4668.md#insn-007f4688)
- 新版 `007f46bc`（命令位置の公開資料なし） · `007f46c4`（命令位置の公開資料なし） · `007f46c8`（命令位置の公開資料なし）

~~~diff
- 007f467c ["INT_ADD", "register:40f0:8", ["const:7f467c:8", "const:4:8"]]
- 007f467c ["CALL", null, ["callee:00c57e90:8"]]
+ 007f46bc ["INT_ADD", "register:40f0:8", ["const:7f46bc:8", "const:4:8"]]
+ 007f46bc ["CALL", null, ["callee:00c57e90:8"]]
- 007f467c bytes 058d1194
+ 007f46bc bytes f58d1194
- 007f4684 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 007f46c4 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 007f4684 bytes 282400d0
+ 007f46c4 bytes 282400f0
- 007f4688 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 007f4688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f4688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f4688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f46c8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 007f46c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f46c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f46c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f4688 bytes 08c13e91
+ 007f46c8 bytes 08c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56a5ce597d7de63197d9483d6e6fc444"></a>

### [`007f4750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4750.md) → [`007f4790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4790.md) FUN_007f4790

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f4774",
      "incomplete_value": false,
      "site": "007f4774",
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
            "const:30:8"
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
      "007f47b4",
      "DATA",
      [
        "storage",
        "00c7b030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f47b4",
      "DATA",
      [
        "storage",
        "00c7b430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f4764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4750.md#insn-007f4764) · [`007f4770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4750.md#insn-007f4770)
- 新版 `007f47a4`（命令位置の公開資料なし） · `007f47b0`（命令位置の公開資料なし）

~~~diff
- 007f4764 ["INT_ADD", "register:40f0:8", ["const:7f4764:8", "const:4:8"]]
- 007f4764 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f47a4 ["INT_ADD", "register:40f0:8", ["const:7f47a4:8", "const:4:8"]]
+ 007f47a4 ["CALL", null, ["callee:00c57e90:8"]]
- 007f4764 bytes cb8c1194
+ 007f47a4 bytes bb8d1194
- 007f4770 ["COPY", "tmp:0:8", ["const:30:8"]]
- 007f4770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f4770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f4770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f47b0 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 007f47b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f47b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f47b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f4770 bytes 08c10091
+ 007f47b0 bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4ee39872fad5ff1d47741d1cc4c3b63"></a>

### [`007f4858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4858.md) → [`007f4898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4898.md) FUN_007f4898

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f487c",
      "incomplete_value": false,
      "site": "007f487c",
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
            "const:b0:8"
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
      "007f48bc",
      "DATA",
      [
        "storage",
        "00c7b0b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f48bc",
      "DATA",
      [
        "storage",
        "00c7b4b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4858.md#insn-007f486c) · [`007f4878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4858.md#insn-007f4878)
- 新版 `007f48ac`（命令位置の公開資料なし） · `007f48b8`（命令位置の公開資料なし）

~~~diff
- 007f486c ["INT_ADD", "register:40f0:8", ["const:7f486c:8", "const:4:8"]]
- 007f486c ["CALL", null, ["callee:00c57e90:8"]]
+ 007f48ac ["INT_ADD", "register:40f0:8", ["const:7f48ac:8", "const:4:8"]]
+ 007f48ac ["CALL", null, ["callee:00c57e90:8"]]
- 007f486c bytes 898c1194
+ 007f48ac bytes 798d1194
- 007f4878 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 007f4878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f4878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f4878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f48b8 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 007f48b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f48b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f48b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f4878 bytes 08c10291
+ 007f48b8 bytes 08c11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-711eb9dca2510de79666e0f4670b9674"></a>

### [`007f49c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f49c4.md) → [`007f4a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4a04.md) FUN_007f4a04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f49e8",
      "incomplete_value": false,
      "site": "007f49e8",
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
            "const:130:8"
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
      "007f4a28",
      "DATA",
      [
        "storage",
        "00c7b130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f4a28",
      "DATA",
      [
        "storage",
        "00c7b530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f49d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f49c4.md#insn-007f49d8) · [`007f49e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f49c4.md#insn-007f49e4)
- 新版 `007f4a18`（命令位置の公開資料なし） · `007f4a24`（命令位置の公開資料なし）

~~~diff
- 007f49d8 ["INT_ADD", "register:40f0:8", ["const:7f49d8:8", "const:4:8"]]
- 007f49d8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f4a18 ["INT_ADD", "register:40f0:8", ["const:7f4a18:8", "const:4:8"]]
+ 007f4a18 ["CALL", null, ["callee:00c57e90:8"]]
- 007f49d8 bytes 2e8c1194
+ 007f4a18 bytes 1e8d1194
- 007f49e4 ["COPY", "tmp:0:8", ["const:130:8"]]
- 007f49e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f49e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f49e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f4a24 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 007f4a24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4a24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4a24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f49e4 bytes 08c10491
+ 007f4a24 bytes 08c11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-062e8173b7d5a9e5ee76d96203cc2388"></a>

### [`007f4a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4a8c.md) → [`007f4acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4acc.md) FUN_007f4acc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f4ab0",
      "incomplete_value": false,
      "site": "007f4ab4",
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
            "const:1b0:8"
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
      "007f4af4",
      "DATA",
      [
        "storage",
        "00c7b1b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f4af4",
      "DATA",
      [
        "storage",
        "00c7b5b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f4aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4a8c.md#insn-007f4aa0) · [`007f4ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4a8c.md#insn-007f4ab0)
- 新版 `007f4ae0`（命令位置の公開資料なし） · `007f4af0`（命令位置の公開資料なし）

~~~diff
- 007f4aa0 ["INT_ADD", "register:40f0:8", ["const:7f4aa0:8", "const:4:8"]]
- 007f4aa0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f4ae0 ["INT_ADD", "register:40f0:8", ["const:7f4ae0:8", "const:4:8"]]
+ 007f4ae0 ["CALL", null, ["callee:00c57e90:8"]]
- 007f4aa0 bytes fc8b1194
+ 007f4ae0 bytes ec8c1194
- 007f4ab0 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 007f4ab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f4ab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f4ab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f4af0 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 007f4af0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4af0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f4af0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f4ab0 bytes 08c10691
+ 007f4af0 bytes 08c11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a1a88922d0668a7fb72834d3255726c"></a>

### [`007f4af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4af4.md) → [`007f4b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f4b34.md) FUN_007f4b34

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

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
    "old": {
      "definition_site": "007f4bf8",
      "incomplete_value": true,
      "site": "007f4c08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:94b:8"
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
    "old": {
      "definition_site": "007f4bfc",
      "incomplete_value": true,
      "site": "007f4c0c",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "007f4e04",
      "incomplete_value": true,
      "site": "007f4e04",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:27d:8"
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
      "007f4b8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f4b9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "007f4c38",
      "READ",
      [
        "storage",
        "002ab94b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007f4b8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f4b9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "007f4c38",
      "READ",
      [
        "storage",
        "002ab98b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f4b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4af4.md#insn-007f4b4c) · [`007f4b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4af4.md#insn-007f4b5c) · [`007f4bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4af4.md#insn-007f4bcc)
- 新版 `007f4b8c`（命令位置の公開資料なし） · `007f4b9c`（命令位置の公開資料なし） · `007f4c0c`（命令位置の公開資料なし）

~~~diff
- 007f4b4c ["INT_ADD", "register:40f0:8", ["const:7f4b4c:8", "const:4:8"]]
- 007f4b4c ["CALL", null, ["ram:47acb4:8"]]
+ 007f4b8c ["INT_ADD", "register:40f0:8", ["const:7f4b8c:8", "const:4:8"]]
+ 007f4b8c ["CALL", null, ["ram:47acf4:8"]]
- 007f4b4c bytes 5a18f297
+ 007f4b8c bytes 5a18f297
- 007f4b5c ["INT_ADD", "register:40f0:8", ["const:7f4b5c:8", "const:4:8"]]
- 007f4b5c ["CALL", null, ["ram:71be98:8"]]
+ 007f4b9c ["INT_ADD", "register:40f0:8", ["const:7f4b9c:8", "const:4:8"]]
+ 007f4b9c ["CALL", null, ["ram:71bed8:8"]]
- 007f4b5c bytes cf9cfc97
+ 007f4b9c bytes cf9cfc97
- 007f4bcc ["INT_ADD", "register:40f0:8", ["const:7f4bcc:8", "const:4:8"]]
- 007f4bcc ["CALL", null, ["callee:008514f8:8"]]
+ 007f4c0c ["INT_ADD", "register:40f0:8", ["const:7f4c0c:8", "const:4:8"]]
+ 007f4c0c ["CALL", null, ["callee:008514f8:8"]]
- 007f4bcc bytes 3b720194
+ 007f4c0c bytes 3b720194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea38c14e60c5357234c67840dfd6a79"></a>

### [`007f51d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f51d4.md) → [`007f5214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5214.md) FUN_007f5214

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f51f4",
      "incomplete_value": true,
      "site": "007f51f8",
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
            "const:220:8"
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
      "007f5238",
      "DATA",
      [
        "storage",
        "00c7b220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5238",
      "DATA",
      [
        "storage",
        "00c7b620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f51e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f51d4.md#insn-007f51e8) · [`007f51f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f51d4.md#insn-007f51f4)
- 新版 `007f5228`（命令位置の公開資料なし） · `007f5234`（命令位置の公開資料なし）

~~~diff
- 007f51e8 ["INT_ADD", "register:40f0:8", ["const:7f51e8:8", "const:4:8"]]
- 007f51e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f5228 ["INT_ADD", "register:40f0:8", ["const:7f5228:8", "const:4:8"]]
+ 007f5228 ["CALL", null, ["callee:00c57e90:8"]]
- 007f51e8 bytes 2a8a1194
+ 007f5228 bytes 1a8b1194
- 007f51f4 ["COPY", "tmp:0:8", ["const:220:8"]]
- 007f51f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f51f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f51f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f5234 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 007f5234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f51f4 bytes 08810891
+ 007f5234 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3443a8f96976c146af786061152fad11"></a>

### [`007f520c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f520c.md) → [`007f524c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f524c.md) FUN_007f524c

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
    "old": {
      "definition_site": "007f5210",
      "incomplete_value": false,
      "site": "007f5214",
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
            "const:220:8"
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
      "007f5254",
      "DATA",
      [
        "storage",
        "00c7b220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f5254",
      "DATA",
      [
        "storage",
        "00c7b620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f520c.md#insn-007f5210)
- 新版 `007f5250`（命令位置の公開資料なし）

~~~diff
- 007f5210 ["COPY", "tmp:0:8", ["const:220:8"]]
- 007f5210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f5210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f5210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f5250 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 007f5250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f5210 bytes 08810891
+ 007f5250 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de8ff8545e21152befd56e99f5b27c69"></a>

### [`007f565c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f565c.md) → [`007f569c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f569c.md) FUN_007f569c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f5670",
      "incomplete_value": false,
      "site": "007f5674",
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
            "const:2b0:8"
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
      "007f56b4",
      "DATA",
      [
        "storage",
        "00c7b2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f56b4",
      "DATA",
      [
        "storage",
        "00c7b6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f565c.md#insn-007f5668) · [`007f5670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f565c.md#insn-007f5670)
- 新版 `007f56a8`（命令位置の公開資料なし） · `007f56b0`（命令位置の公開資料なし）

~~~diff
- 007f5668 ["INT_ADD", "register:40f0:8", ["const:7f5668:8", "const:4:8"]]
- 007f5668 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f56a8 ["INT_ADD", "register:40f0:8", ["const:7f56a8:8", "const:4:8"]]
+ 007f56a8 ["CALL", null, ["callee:00c57e90:8"]]
- 007f5668 bytes 0a891194
+ 007f56a8 bytes fa891194
- 007f5670 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 007f5670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f5670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f5670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f56b0 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 007f56b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f56b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f56b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f5670 bytes 08c10a91
+ 007f56b0 bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bb00d6d5c57bab99b47b94b3632aaab"></a>

### [`007f5698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5698.md) → [`007f56d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f56d8.md) FUN_007f56d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`008b924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b924c.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md)

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
    "old": {
      "definition_site": "007f56e0",
      "incomplete_value": true,
      "site": "007f56e0",
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
    "old": {
      "definition_site": "007f56e8",
      "incomplete_value": false,
      "site": "007f56f8",
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
            "const:a58:8"
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
    "old": {
      "definition_site": "007f56f0",
      "incomplete_value": false,
      "site": "007f56f8",
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
            "const:590:8"
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
      "007f571c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5728",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5730",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f571c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5728",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5730",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f56f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5698.md#insn-007f56f8) · [`007f5804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5698.md#insn-007f5804) · [`007f56d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5698.md#insn-007f56d0)
- 新版 `007f5738`（命令位置の公開資料なし） · `007f5844`（命令位置の公開資料なし） · `007f5710`（命令位置の公開資料なし）

~~~diff
- 007f56f8 ["INT_ADD", "register:40f0:8", ["const:7f56f8:8", "const:4:8"]]
- 007f56f8 ["CALL", null, ["callee:00c58610:8"]]
+ 007f5738 ["INT_ADD", "register:40f0:8", ["const:7f5738:8", "const:4:8"]]
+ 007f5738 ["CALL", null, ["callee:00c58610:8"]]
- 007f56f8 bytes c68a1194
+ 007f5738 bytes b68b1194
- 007f5804 ["INT_ADD", "register:40f0:8", ["const:7f5804:8", "const:4:8"]]
- 007f5804 ["CALL", null, ["ram:71be98:8"]]
+ 007f5844 ["INT_ADD", "register:40f0:8", ["const:7f5844:8", "const:4:8"]]
+ 007f5844 ["CALL", null, ["ram:71bed8:8"]]
- 007f5804 bytes a599fc97
+ 007f5844 bytes a599fc97
- 007f56d0 ["INT_ADD", "register:40f0:8", ["const:7f56d0:8", "const:4:8"]]
- 007f56d0 ["CALL", null, ["callee:008b9290:8"]]
+ 007f5710 ["INT_ADD", "register:40f0:8", ["const:7f5710:8", "const:4:8"]]
+ 007f5710 ["CALL", null, ["callee:008b9290:8"]]
- 007f56d0 bytes df0e0394
+ 007f5710 bytes e00e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aa035393e9570189602f189ea6a0bb1"></a>

### [`007f589c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f589c.md) → [`007f58dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f58dc.md) FUN_007f58dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f58c0",
      "incomplete_value": false,
      "site": "007f58c0",
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
      "007f5900",
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
      "007f5900",
      "DATA",
      [
        "storage",
        "00c7b730",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f58b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f589c.md#insn-007f58b0) · [`007f58bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f589c.md#insn-007f58bc)
- 新版 `007f58f0`（命令位置の公開資料なし） · `007f58fc`（命令位置の公開資料なし）

~~~diff
- 007f58b0 ["INT_ADD", "register:40f0:8", ["const:7f58b0:8", "const:4:8"]]
- 007f58b0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f58f0 ["INT_ADD", "register:40f0:8", ["const:7f58f0:8", "const:4:8"]]
+ 007f58f0 ["CALL", null, ["callee:00c57e90:8"]]
- 007f58b0 bytes 78881194
+ 007f58f0 bytes 68891194
- 007f58bc ["COPY", "tmp:0:8", ["const:330:8"]]
- 007f58bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f58bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f58bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f58fc ["COPY", "tmp:0:8", ["const:730:8"]]
+ 007f58fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f58fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f58fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f58bc bytes 08c10c91
+ 007f58fc bytes 08c11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25e02eb0fd27e483bf7a96b9d8c3235b"></a>

### [`007f58ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f58ec.md) → [`007f592c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f592c.md) FUN_007f592c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "007f5988",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f5948",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f5988",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007f5988",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f58ec.md#insn-007f5948) · [`007f5954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f58ec.md#insn-007f5954)
- 新版 `007f5988`（命令位置の公開資料なし） · `007f5994`（命令位置の公開資料なし）

~~~diff
- 007f5948 ["INT_ADD", "register:40f0:8", ["const:7f5948:8", "const:4:8"]]
- 007f5948 ["CALL", null, ["ram:47acb4:8"]]
+ 007f5988 ["INT_ADD", "register:40f0:8", ["const:7f5988:8", "const:4:8"]]
+ 007f5988 ["CALL", null, ["ram:47acf4:8"]]
- 007f5948 bytes db14f297
+ 007f5988 bytes db14f297
- 007f5954 ["INT_ADD", "register:40f0:8", ["const:7f5954:8", "const:4:8"]]
- 007f5954 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007f5994 ["INT_ADD", "register:40f0:8", ["const:7f5994:8", "const:4:8"]]
+ 007f5994 ["CALL", null, ["callee:0047cdd4:8"]]
- 007f5954 bytes 101df297
+ 007f5994 bytes 101df297
~~~


<a id="compare-40113b6db9b172eea10688be14fdcd72"></a>

### [`007f59a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f59a0.md) → [`007f59e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f59e0.md) FUN_007f59e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f59b4",
      "incomplete_value": false,
      "site": "007f59b8",
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
      "007f59f8",
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
      "007f59f8",
      "DATA",
      [
        "storage",
        "00c7b7b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f59ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f59a0.md#insn-007f59ac) · [`007f59b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f59a0.md#insn-007f59b4)
- 新版 `007f59ec`（命令位置の公開資料なし） · `007f59f4`（命令位置の公開資料なし）

~~~diff
- 007f59ac ["INT_ADD", "register:40f0:8", ["const:7f59ac:8", "const:4:8"]]
- 007f59ac ["CALL", null, ["callee:00c57e90:8"]]
+ 007f59ec ["INT_ADD", "register:40f0:8", ["const:7f59ec:8", "const:4:8"]]
+ 007f59ec ["CALL", null, ["callee:00c57e90:8"]]
- 007f59ac bytes 39881194
+ 007f59ec bytes 29891194
- 007f59b4 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 007f59b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f59b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f59b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f59f4 ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 007f59f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f59f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f59f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f59b4 bytes 08c10e91
+ 007f59f4 bytes 08c11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-634a7b2f7f31629c257b21e74b82cfe4"></a>

### [`007f59dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f59dc.md) → [`007f5a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5a1c.md) FUN_007f5a1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "007f5a40",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f5a00",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f5a40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007f5a40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f59dc.md#insn-007f5a00) · [`007f5a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f59dc.md#insn-007f5a0c)
- 新版 `007f5a40`（命令位置の公開資料なし） · `007f5a4c`（命令位置の公開資料なし）

~~~diff
- 007f5a00 ["INT_ADD", "register:40f0:8", ["const:7f5a00:8", "const:4:8"]]
- 007f5a00 ["CALL", null, ["ram:47acb4:8"]]
+ 007f5a40 ["INT_ADD", "register:40f0:8", ["const:7f5a40:8", "const:4:8"]]
+ 007f5a40 ["CALL", null, ["ram:47acf4:8"]]
- 007f5a00 bytes ad14f297
+ 007f5a40 bytes ad14f297
- 007f5a0c ["INT_ADD", "register:40f0:8", ["const:7f5a0c:8", "const:4:8"]]
- 007f5a0c ["CALL", null, ["callee:0047cdd4:8"]]
+ 007f5a4c ["INT_ADD", "register:40f0:8", ["const:7f5a4c:8", "const:4:8"]]
+ 007f5a4c ["CALL", null, ["callee:0047cdd4:8"]]
- 007f5a0c bytes e21cf297
+ 007f5a4c bytes e21cf297
~~~


<a id="compare-9f554bde3c75d76ad189e2914a655544"></a>

### [`007f5a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5a50.md) → [`007f5a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5a90.md) FUN_007f5a90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f5a74",
      "incomplete_value": false,
      "site": "007f5a74",
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
      "007f5ab4",
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
      "007f5ab4",
      "DATA",
      [
        "storage",
        "00c7b830",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5a50.md#insn-007f5a64) · [`007f5a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5a50.md#insn-007f5a70)
- 新版 `007f5aa4`（命令位置の公開資料なし） · `007f5ab0`（命令位置の公開資料なし）

~~~diff
- 007f5a64 ["INT_ADD", "register:40f0:8", ["const:7f5a64:8", "const:4:8"]]
- 007f5a64 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f5aa4 ["INT_ADD", "register:40f0:8", ["const:7f5aa4:8", "const:4:8"]]
+ 007f5aa4 ["CALL", null, ["callee:00c57e90:8"]]
- 007f5a64 bytes 0b881194
+ 007f5aa4 bytes fb881194
- 007f5a70 ["COPY", "tmp:0:8", ["const:430:8"]]
- 007f5a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f5a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f5a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f5ab0 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 007f5ab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5ab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5ab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f5a70 bytes 08c11091
+ 007f5ab0 bytes 08c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df9b695a3a1836a5a346368da6a6d09e"></a>

### [`007f5aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5aa0.md) → [`007f5ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5ae0.md) FUN_007f5ae0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.39% / 新版 94.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "007f5ae4",
      "incomplete_value": true,
      "site": "007f5ae4",
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
    "old": {
      "definition_site": "007f5aec",
      "incomplete_value": false,
      "site": "007f5afc",
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
            "const:a58:8"
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
    "old": {
      "definition_site": "007f5af4",
      "incomplete_value": false,
      "site": "007f5afc",
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
            "const:590:8"
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
      "007f5b18",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5b2c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5b34",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f5b18",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5b2c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5b34",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5aa0.md#insn-007f5afc) · [`007f5b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5aa0.md#insn-007f5b44) · [`007f5b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5aa0.md#insn-007f5b74)
- 新版 `007f5b3c`（命令位置の公開資料なし） · `007f5b84`（命令位置の公開資料なし） · `007f5bb4`（命令位置の公開資料なし）

~~~diff
- 007f5afc ["INT_ADD", "register:40f0:8", ["const:7f5afc:8", "const:4:8"]]
- 007f5afc ["CALL", null, ["callee:00c58610:8"]]
+ 007f5b3c ["INT_ADD", "register:40f0:8", ["const:7f5b3c:8", "const:4:8"]]
+ 007f5b3c ["CALL", null, ["callee:00c58610:8"]]
- 007f5afc bytes c5891194
+ 007f5b3c bytes b58a1194
- 007f5b44 ["INT_ADD", "register:40f0:8", ["const:7f5b44:8", "const:4:8"]]
- 007f5b44 ["CALL", null, ["ram:46c984:8"]]
+ 007f5b84 ["INT_ADD", "register:40f0:8", ["const:7f5b84:8", "const:4:8"]]
+ 007f5b84 ["CALL", null, ["ram:46c9c4:8"]]
- 007f5b44 bytes 90dbf197
+ 007f5b84 bytes 90dbf197
- 007f5b74 ["INT_ADD", "register:40f0:8", ["const:7f5b74:8", "const:4:8"]]
- 007f5b74 ["CALL", null, ["ram:46c984:8"]]
+ 007f5bb4 ["INT_ADD", "register:40f0:8", ["const:7f5bb4:8", "const:4:8"]]
+ 007f5bb4 ["CALL", null, ["ram:46c9c4:8"]]
- 007f5b74 bytes 84dbf197
+ 007f5bb4 bytes 84dbf197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37bdf285fb7d3126948d4325667098f6"></a>

### [`007f5e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5e24.md) → [`007f5e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5e64.md) FUN_007f5e64

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f5e48",
      "incomplete_value": false,
      "site": "007f5e48",
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
      "007f5e88",
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
      "007f5e88",
      "DATA",
      [
        "storage",
        "00c7b8b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5e24.md#insn-007f5e38) · [`007f5e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5e24.md#insn-007f5e44)
- 新版 `007f5e78`（命令位置の公開資料なし） · `007f5e84`（命令位置の公開資料なし）

~~~diff
- 007f5e38 ["INT_ADD", "register:40f0:8", ["const:7f5e38:8", "const:4:8"]]
- 007f5e38 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f5e78 ["INT_ADD", "register:40f0:8", ["const:7f5e78:8", "const:4:8"]]
+ 007f5e78 ["CALL", null, ["callee:00c57e90:8"]]
- 007f5e38 bytes 16871194
+ 007f5e78 bytes 06881194
- 007f5e44 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 007f5e44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f5e44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f5e44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f5e84 ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 007f5e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f5e44 bytes 08c11291
+ 007f5e84 bytes 08c12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cf02dd52846dd7ae797a55aa0f48321"></a>

### [`007f5e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5e74.md) → [`007f5eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5eb4.md) FUN_007f5eb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "007f5efc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f5ebc",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f5efc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007f5efc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5e74.md#insn-007f5ebc) · [`007f5ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5e74.md#insn-007f5ec8)
- 新版 `007f5efc`（命令位置の公開資料なし） · `007f5f08`（命令位置の公開資料なし）

~~~diff
- 007f5ebc ["INT_ADD", "register:40f0:8", ["const:7f5ebc:8", "const:4:8"]]
- 007f5ebc ["CALL", null, ["ram:47acb4:8"]]
+ 007f5efc ["INT_ADD", "register:40f0:8", ["const:7f5efc:8", "const:4:8"]]
+ 007f5efc ["CALL", null, ["ram:47acf4:8"]]
- 007f5ebc bytes 7e13f297
+ 007f5efc bytes 7e13f297
- 007f5ec8 ["INT_ADD", "register:40f0:8", ["const:7f5ec8:8", "const:4:8"]]
- 007f5ec8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007f5f08 ["INT_ADD", "register:40f0:8", ["const:7f5f08:8", "const:4:8"]]
+ 007f5f08 ["CALL", null, ["callee:0047cdd4:8"]]
- 007f5ec8 bytes b31bf297
+ 007f5f08 bytes b31bf297
~~~


<a id="compare-660ef2d5a62cf22d672d4280eabd60f4"></a>

### [`007f5f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5f08.md) → [`007f5f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5f48.md) FUN_007f5f48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f5f2c",
      "incomplete_value": false,
      "site": "007f5f2c",
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
      "007f5f6c",
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
      "007f5f6c",
      "DATA",
      [
        "storage",
        "00c7b930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5f08.md#insn-007f5f1c) · [`007f5f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5f08.md#insn-007f5f28)
- 新版 `007f5f5c`（命令位置の公開資料なし） · `007f5f68`（命令位置の公開資料なし）

~~~diff
- 007f5f1c ["INT_ADD", "register:40f0:8", ["const:7f5f1c:8", "const:4:8"]]
- 007f5f1c ["CALL", null, ["callee:00c57e90:8"]]
+ 007f5f5c ["INT_ADD", "register:40f0:8", ["const:7f5f5c:8", "const:4:8"]]
+ 007f5f5c ["CALL", null, ["callee:00c57e90:8"]]
- 007f5f1c bytes dd861194
+ 007f5f5c bytes cd871194
- 007f5f28 ["COPY", "tmp:0:8", ["const:530:8"]]
- 007f5f28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f5f28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f5f28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f5f68 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 007f5f68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5f68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f5f68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f5f28 bytes 08c11491
+ 007f5f68 bytes 08c12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a3ddb17f276f40523b10a94affbf74c"></a>

### [`007f5f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5f58.md) → [`007f5f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f5/007f5f98.md) FUN_007f5f98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)

変更の種類 branch_value, call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 87.67% / 新版 87.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "007f5f7c",
      "incomplete_value": true,
      "site": "007f5f7c",
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f5fec",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f5fac",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f6050",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f6010",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "007f5fb4",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5fc4",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5fcc",
      "PARAM",
      [
        "storage",
        "00c71590",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007f5fb4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007f5fc4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007f5fcc",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f5fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5f58.md#insn-007f5fac) · [`007f6010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5f58.md#insn-007f6010) · [`007f6048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f5/007f5f58.md#insn-007f6048)
- 新版 `007f5fec`（命令位置の公開資料なし） · `007f6050`（命令位置の公開資料なし） · `007f6088`（命令位置の公開資料なし）

~~~diff
- 007f5fac ["INT_ADD", "register:40f0:8", ["const:7f5fac:8", "const:4:8"]]
- 007f5fac ["CALL", null, ["ram:46c984:8"]]
+ 007f5fec ["INT_ADD", "register:40f0:8", ["const:7f5fec:8", "const:4:8"]]
+ 007f5fec ["CALL", null, ["ram:46c9c4:8"]]
- 007f5fac bytes 76daf197
+ 007f5fec bytes 76daf197
- 007f6010 ["INT_ADD", "register:40f0:8", ["const:7f6010:8", "const:4:8"]]
- 007f6010 ["CALL", null, ["ram:46c984:8"]]
+ 007f6050 ["INT_ADD", "register:40f0:8", ["const:7f6050:8", "const:4:8"]]
+ 007f6050 ["CALL", null, ["ram:46c9c4:8"]]
- 007f6010 bytes 5ddaf197
+ 007f6050 bytes 5ddaf197
- 007f6048 ["INT_ADD", "register:40f0:8", ["const:7f6048:8", "const:4:8"]]
- 007f6048 ["CALL", null, ["ram:46c984:8"]]
+ 007f6088 ["INT_ADD", "register:40f0:8", ["const:7f6088:8", "const:4:8"]]
+ 007f6088 ["CALL", null, ["ram:46c9c4:8"]]
- 007f6048 bytes 4fdaf197
+ 007f6088 bytes 4fdaf197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bb3dd4b795cac83e3da0eb35c33a375"></a>

### [`007f60a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f60a8.md) → [`007f60e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f60e8.md) FUN_007f60e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f60bc",
      "incomplete_value": false,
      "site": "007f60c0",
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
      "007f6100",
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
      "007f6100",
      "DATA",
      [
        "storage",
        "00c7b9b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f60b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f60a8.md#insn-007f60b4) · [`007f60bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f60a8.md#insn-007f60bc)
- 新版 `007f60f4`（命令位置の公開資料なし） · `007f60fc`（命令位置の公開資料なし）

~~~diff
- 007f60b4 ["INT_ADD", "register:40f0:8", ["const:7f60b4:8", "const:4:8"]]
- 007f60b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f60f4 ["INT_ADD", "register:40f0:8", ["const:7f60f4:8", "const:4:8"]]
+ 007f60f4 ["CALL", null, ["callee:00c57e90:8"]]
- 007f60b4 bytes 77861194
+ 007f60f4 bytes 67871194
- 007f60bc ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 007f60bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f60bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f60bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f60fc ["COPY", "tmp:0:8", ["const:9b0:8"]]
+ 007f60fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f60fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f60fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f60bc bytes 08c11691
+ 007f60fc bytes 08c12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac5baebe58548d42d5ac3a90b4f65774"></a>

### [`007f60e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f60e4.md) → [`007f6124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6124.md) FUN_007f6124

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "007f6140",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f6100",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f6140",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007f6140",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f60e4.md#insn-007f6100) · [`007f610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f60e4.md#insn-007f610c)
- 新版 `007f6140`（命令位置の公開資料なし） · `007f614c`（命令位置の公開資料なし）

~~~diff
- 007f6100 ["INT_ADD", "register:40f0:8", ["const:7f6100:8", "const:4:8"]]
- 007f6100 ["CALL", null, ["ram:47acb4:8"]]
+ 007f6140 ["INT_ADD", "register:40f0:8", ["const:7f6140:8", "const:4:8"]]
+ 007f6140 ["CALL", null, ["ram:47acf4:8"]]
- 007f6100 bytes ed12f297
+ 007f6140 bytes ed12f297
- 007f610c ["INT_ADD", "register:40f0:8", ["const:7f610c:8", "const:4:8"]]
- 007f610c ["CALL", null, ["callee:0047cdd4:8"]]
+ 007f614c ["INT_ADD", "register:40f0:8", ["const:7f614c:8", "const:4:8"]]
+ 007f614c ["CALL", null, ["callee:0047cdd4:8"]]
- 007f610c bytes 221bf297
+ 007f614c bytes 221bf297
~~~


<a id="compare-d23cf071b3e4decc7bb46619607f34d6"></a>

### [`007f6150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f6150.md) → [`007f6190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f6190.md) FUN_007f6190

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f6174",
      "incomplete_value": false,
      "site": "007f6174",
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
            "const:630:8"
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
      "007f61b4",
      "DATA",
      [
        "storage",
        "00c7b630",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f61b4",
      "DATA",
      [
        "storage",
        "00c7ba30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f6150.md#insn-007f6164) · [`007f6170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f6150.md#insn-007f6170)
- 新版 `007f61a4`（命令位置の公開資料なし） · `007f61b0`（命令位置の公開資料なし）

~~~diff
- 007f6164 ["INT_ADD", "register:40f0:8", ["const:7f6164:8", "const:4:8"]]
- 007f6164 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f61a4 ["INT_ADD", "register:40f0:8", ["const:7f61a4:8", "const:4:8"]]
+ 007f61a4 ["CALL", null, ["callee:00c57e90:8"]]
- 007f6164 bytes 4b861194
+ 007f61a4 bytes 3b871194
- 007f6170 ["COPY", "tmp:0:8", ["const:630:8"]]
- 007f6170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f6170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f6170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f61b0 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 007f61b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f61b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f61b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f6170 bytes 08c11891
+ 007f61b0 bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4b1eb04c3c33c777043c3f79039e9fc"></a>

### [`007f61a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f61a0.md) → [`007f61e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f61e0.md) FUN_007f61e0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0046dab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dab4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`007f64bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f64bc.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`007f64fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f64fc.md)

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
    "old": {
      "definition_site": "007f62b4",
      "incomplete_value": true,
      "site": "007f62c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4b6:8"
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
    "old": {
      "definition_site": "007f62e8",
      "incomplete_value": false,
      "site": "007f62e8",
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
            "const:6a0:8"
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
      "site": "007f6220",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007f61e0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007f6220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007f623c",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "007f6254",
      "READ",
      [
        "storage",
        "00ca3d8c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "007f6220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007f623c",
      "READ",
      [
        "storage",
        "00c9b4d0",
        null,
        "pointer"
      ]
    ],
    [
      "007f6254",
      "READ",
      [
        "storage",
        "00ca418c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f61e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f61a0.md#insn-007f61e0) · [`007f61ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f61a0.md#insn-007f61ec) · [`007f61fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f61a0.md#insn-007f61fc)
- 新版 `007f6220`（命令位置の公開資料なし） · `007f622c`（命令位置の公開資料なし） · `007f623c`（命令位置の公開資料なし）

~~~diff
- 007f61e0 ["INT_ADD", "register:40f0:8", ["const:7f61e0:8", "const:4:8"]]
- 007f61e0 ["CALL", null, ["ram:47acb4:8"]]
+ 007f6220 ["INT_ADD", "register:40f0:8", ["const:7f6220:8", "const:4:8"]]
+ 007f6220 ["CALL", null, ["ram:47acf4:8"]]
- 007f61e0 bytes b512f297
+ 007f6220 bytes b512f297
- 007f61ec ["INT_ADD", "register:40f0:8", ["const:7f61ec:8", "const:4:8"]]
- 007f61ec ["CALL", null, ["callee:0047cdd4:8"]]
+ 007f622c ["INT_ADD", "register:40f0:8", ["const:7f622c:8", "const:4:8"]]
+ 007f622c ["CALL", null, ["callee:0047cdd4:8"]]
- 007f61ec bytes ea1af297
+ 007f622c bytes ea1af297
- 007f61fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d0:8"]]
- 007f61fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 007f623c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4d0:8"]]
+ 007f623c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 007f61fc bytes 296940f9
+ 007f623c bytes 296942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62a927ff341b6f4fa367855c11ff64e8"></a>

### [`007f6474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f6474.md) → [`007f64b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f6/007f64b4.md) FUN_007f64b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "007f6498",
      "incomplete_value": false,
      "site": "007f6498",
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
      "007f64d8",
      "DATA",
      [
        "storage",
        "00c7b6a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007f64d8",
      "DATA",
      [
        "storage",
        "00c7baa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007f6488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f6474.md#insn-007f6488) · [`007f6494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f6/007f6474.md#insn-007f6494)
- 新版 `007f64c8`（命令位置の公開資料なし） · `007f64d4`（命令位置の公開資料なし）

~~~diff
- 007f6488 ["INT_ADD", "register:40f0:8", ["const:7f6488:8", "const:4:8"]]
- 007f6488 ["CALL", null, ["callee:00c57e90:8"]]
+ 007f64c8 ["INT_ADD", "register:40f0:8", ["const:7f64c8:8", "const:4:8"]]
+ 007f64c8 ["CALL", null, ["callee:00c57e90:8"]]
- 007f6488 bytes 82851194
+ 007f64c8 bytes 72861194
- 007f6494 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 007f6494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007f6494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007f6494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007f64d4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 007f64d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007f64d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007f64d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007f6494 bytes 08811a91
+ 007f64d4 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

