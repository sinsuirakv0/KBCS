# v16.0.0 → v16.0.1 · 最優先の変更候補 (4)

[一覧の目次](README.md)

<a id="compare-20024fed07be54bb0a28b92f0ccbad8e"></a>

### [`00462dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462dc0.md) → [`00462e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462e00.md) FUN_00462e00

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
      "definition_site": "00462e18",
      "incomplete_value": false,
      "site": "00462e24",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462dd8",
      "incomplete_value": false,
      "site": "00462de4",
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
            "const:98:8"
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
      "00462e24",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462e24",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462dc0.md#insn-00462dd8) · [`00462e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462dc0.md#insn-00462e08)
- 新版 `00462e18`（命令位置の公開資料なし） · `00462e48`（命令位置の公開資料なし）

~~~diff
- 00462dd8 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00462dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462e18 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 00462e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462dd8 bytes 08610291
+ 00462e18 bytes 08611291
- 00462e08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462e08 ["INT_ADD", "register:40f0:8", ["const:462e08:8", "const:4:8"]]
- 00462e08 ["CALLIND", null, ["register:0:8"]]
+ 00462e48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462e48 ["INT_ADD", "register:40f0:8", ["const:462e48:8", "const:4:8"]]
+ 00462e48 ["CALLIND", null, ["register:0:8"]]
- 00462e08 bytes 00013fd6
+ 00462e48 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24c1bb73d8c5af675f87c7c1b79ea770"></a>

### [`00462e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462e1c.md) → [`00462e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462e5c.md) FUN_00462e5c

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
      "definition_site": "00462e88",
      "incomplete_value": false,
      "site": "00462e88",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462e48",
      "incomplete_value": false,
      "site": "00462e48",
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
            "const:98:8"
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
      "00462e88",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462e88",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462e1c.md#insn-00462e30) · [`00462e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462e1c.md#insn-00462e40) · [`00462e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462e1c.md#insn-00462e64)
- 新版 `00462e70`（命令位置の公開資料なし） · `00462e80`（命令位置の公開資料なし） · `00462ea4`（命令位置の公開資料なし）

~~~diff
- 00462e30 ["INT_ADD", "register:40f0:8", ["const:462e30:8", "const:4:8"]]
- 00462e30 ["CALL", null, ["callee:00c57e90:8"]]
+ 00462e70 ["INT_ADD", "register:40f0:8", ["const:462e70:8", "const:4:8"]]
+ 00462e70 ["CALL", null, ["callee:00c57e90:8"]]
- 00462e30 bytes 18d31f94
+ 00462e70 bytes 08d41f94
- 00462e40 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00462e40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462e40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462e40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462e80 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 00462e80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462e80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462e80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462e40 bytes 08610291
+ 00462e80 bytes 08611291
- 00462e64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462e64 ["INT_ADD", "register:40f0:8", ["const:462e64:8", "const:4:8"]]
- 00462e64 ["CALLIND", null, ["register:0:8"]]
+ 00462ea4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462ea4 ["INT_ADD", "register:40f0:8", ["const:462ea4:8", "const:4:8"]]
+ 00462ea4 ["CALLIND", null, ["register:0:8"]]
- 00462e64 bytes 00013fd6
+ 00462ea4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8b4e7918439fa2bb9aa63fc211be927"></a>

### [`00462ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462ea4.md) → [`00462ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462ee4.md) FUN_00462ee4

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
      "definition_site": "00462f00",
      "incomplete_value": false,
      "site": "00462f00",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462ec0",
      "incomplete_value": false,
      "site": "00462ec0",
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
            "const:98:8"
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
      "00462f00",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462f00",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462ea4.md#insn-00462ebc) · [`00462ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00462/00462ea4.md#insn-00462ee0)
- 新版 `00462efc`（命令位置の公開資料なし） · `00462f20`（命令位置の公開資料なし）

~~~diff
- 00462ebc ["COPY", "tmp:0:8", ["const:98:8"]]
- 00462ebc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00462ebc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00462ebc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462efc ["COPY", "tmp:0:8", ["const:498:8"]]
+ 00462efc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462efc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462efc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00462ebc bytes 29610291
+ 00462efc bytes 29611291
- 00462ee0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00462ee0 ["INT_ADD", "register:40f0:8", ["const:462ee0:8", "const:4:8"]]
- 00462ee0 ["CALLIND", null, ["register:0:8"]]
+ 00462f20 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462f20 ["INT_ADD", "register:40f0:8", ["const:462f20:8", "const:4:8"]]
+ 00462f20 ["CALLIND", null, ["register:0:8"]]
- 00462ee0 bytes 20013fd6
+ 00462f20 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d42cecb574e6f8a27c345875ed4f36c"></a>

### [`00463044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463044.md) → [`00463084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463084.md) FUN_00463084

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
      "definition_site": "00463090",
      "incomplete_value": false,
      "site": "0046309c",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463050",
      "incomplete_value": false,
      "site": "0046305c",
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
            "const:118:8"
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
      "0046309c",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046309c",
      "DATA",
      [
        "storage",
        "00c64518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463044.md#insn-00463050)
- 新版 `00463090`（命令位置の公開資料なし）

~~~diff
- 00463050 ["COPY", "tmp:0:8", ["const:118:8"]]
- 00463050 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00463050 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00463050 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463090 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00463090 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463090 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463090 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00463050 bytes 4a610491
+ 00463090 bytes 4a611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7e0bdd8830573ab1a20dd8549f6fb14"></a>

### [`00463088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463088.md) → [`004630c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004630c8.md) FUN_004630c8

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
      "definition_site": "004630e0",
      "incomplete_value": false,
      "site": "004630ec",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004630a0",
      "incomplete_value": false,
      "site": "004630ac",
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
            "const:118:8"
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
      "004630ec",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004630ec",
      "DATA",
      [
        "storage",
        "00c64518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004630a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463088.md#insn-004630a0) · [`004630d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463088.md#insn-004630d0)
- 新版 `004630e0`（命令位置の公開資料なし） · `00463110`（命令位置の公開資料なし）

~~~diff
- 004630a0 ["COPY", "tmp:0:8", ["const:118:8"]]
- 004630a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004630a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004630a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004630e0 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 004630e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004630e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004630e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004630a0 bytes 08610491
+ 004630e0 bytes 08611491
- 004630d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004630d0 ["INT_ADD", "register:40f0:8", ["const:4630d0:8", "const:4:8"]]
- 004630d0 ["CALLIND", null, ["register:0:8"]]
+ 00463110 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463110 ["INT_ADD", "register:40f0:8", ["const:463110:8", "const:4:8"]]
+ 00463110 ["CALLIND", null, ["register:0:8"]]
- 004630d0 bytes 00013fd6
+ 00463110 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53e6bcd4314a1faef5961c09c5c263ca"></a>

### [`004630e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004630e4.md) → [`00463124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463124.md) FUN_00463124

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
      "definition_site": "00463150",
      "incomplete_value": false,
      "site": "00463150",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463110",
      "incomplete_value": false,
      "site": "00463110",
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
            "const:118:8"
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
      "00463150",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463150",
      "DATA",
      [
        "storage",
        "00c64518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004630f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004630e4.md#insn-004630f8) · [`00463108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004630e4.md#insn-00463108) · [`0046312c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004630e4.md#insn-0046312c)
- 新版 `00463138`（命令位置の公開資料なし） · `00463148`（命令位置の公開資料なし） · `0046316c`（命令位置の公開資料なし）

~~~diff
- 004630f8 ["INT_ADD", "register:40f0:8", ["const:4630f8:8", "const:4:8"]]
- 004630f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00463138 ["INT_ADD", "register:40f0:8", ["const:463138:8", "const:4:8"]]
+ 00463138 ["CALL", null, ["callee:00c57e90:8"]]
- 004630f8 bytes 66d21f94
+ 00463138 bytes 56d31f94
- 00463108 ["COPY", "tmp:0:8", ["const:118:8"]]
- 00463108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463148 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00463148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463108 bytes 08610491
+ 00463148 bytes 08611491
- 0046312c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046312c ["INT_ADD", "register:40f0:8", ["const:46312c:8", "const:4:8"]]
- 0046312c ["CALLIND", null, ["register:0:8"]]
+ 0046316c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046316c ["INT_ADD", "register:40f0:8", ["const:46316c:8", "const:4:8"]]
+ 0046316c ["CALLIND", null, ["register:0:8"]]
- 0046312c bytes 00013fd6
+ 0046316c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f3ac2fee2a4a801f5274ec2bbf462e3"></a>

### [`0046316c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046316c.md) → [`004631ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004631ac.md) FUN_004631ac

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
      "definition_site": "004631c8",
      "incomplete_value": false,
      "site": "004631c8",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463188",
      "incomplete_value": false,
      "site": "00463188",
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
            "const:118:8"
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
      "004631c8",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004631c8",
      "DATA",
      [
        "storage",
        "00c64518",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046316c.md#insn-00463184) · [`004631a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046316c.md#insn-004631a8)
- 新版 `004631c4`（命令位置の公開資料なし） · `004631e8`（命令位置の公開資料なし）

~~~diff
- 00463184 ["COPY", "tmp:0:8", ["const:118:8"]]
- 00463184 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00463184 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00463184 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004631c4 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 004631c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004631c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004631c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00463184 bytes 29610491
+ 004631c4 bytes 29611491
- 004631a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004631a8 ["INT_ADD", "register:40f0:8", ["const:4631a8:8", "const:4:8"]]
- 004631a8 ["CALLIND", null, ["register:0:8"]]
+ 004631e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004631e8 ["INT_ADD", "register:40f0:8", ["const:4631e8:8", "const:4:8"]]
+ 004631e8 ["CALLIND", null, ["register:0:8"]]
- 004631a8 bytes 20013fd6
+ 004631e8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3643c86ad49d4c26a07a61d63469ee7"></a>

### [`00463268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463268.md) → [`004632a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004632a8.md) FUN_004632a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.79% / 新版 97.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046334c",
      "incomplete_value": true,
      "site": "0046334c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f9b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046330c",
      "incomplete_value": true,
      "site": "0046330c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ece:8"
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
      "0046333c",
      "READ",
      [
        "storage",
        "002a0ece",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0046333c",
      "READ",
      [
        "storage",
        "002a0f9b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046334c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463268.md#insn-0046334c) · [`004632bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463268.md#insn-004632bc) · [`004632e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463268.md#insn-004632e8)
- 新版 `0046338c`（命令位置の公開資料なし） · `004632fc`（命令位置の公開資料なし） · `00463328`（命令位置の公開資料なし）

~~~diff
- 0046334c ["INT_ADD", "register:40f0:8", ["const:46334c:8", "const:4:8"]]
- 0046334c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0046338c ["INT_ADD", "register:40f0:8", ["const:46338c:8", "const:4:8"]]
+ 0046338c ["CALL", null, ["callee:00c57eb0:8"]]
- 0046334c bytes d9d11f94
+ 0046338c bytes c9d21f94
- 004632bc ["INT_ADD", "register:40f0:8", ["const:4632bc:8", "const:4:8"]]
- 004632bc ["CALL", null, ["callee:0044108c:8"]]
+ 004632fc ["INT_ADD", "register:40f0:8", ["const:4632fc:8", "const:4:8"]]
+ 004632fc ["CALL", null, ["callee:0044108c:8"]]
- 004632bc bytes 6477ff97
+ 004632fc bytes 6477ff97
- 004632e8 ["INT_ADD", "register:40f0:8", ["const:4632e8:8", "const:4:8"]]
- 004632e8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00463328 ["INT_ADD", "register:40f0:8", ["const:463328:8", "const:4:8"]]
+ 00463328 ["CALL", null, ["callee:00c57eb0:8"]]
- 004632e8 bytes f2d11f94
+ 00463328 bytes e2d21f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6988a4de7353ab5f1dc854f7deb85daa"></a>

### [`0046352c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046352c.md) → [`0046356c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/0046356c.md) FUN_0046356c

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
      "definition_site": "00463578",
      "incomplete_value": false,
      "site": "00463584",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463538",
      "incomplete_value": false,
      "site": "00463544",
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
            "const:198:8"
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
      "00463584",
      "DATA",
      [
        "storage",
        "00c64198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463584",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046352c.md#insn-00463538)
- 新版 `00463578`（命令位置の公開資料なし）

~~~diff
- 00463538 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00463538 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00463538 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00463538 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463578 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00463578 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463578 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463578 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00463538 bytes 4a610691
+ 00463578 bytes 4a611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3699aa4cd9ae461082243fa6018734d"></a>

### [`00463570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463570.md) → [`004635b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004635b0.md) FUN_004635b0

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
      "definition_site": "004635c8",
      "incomplete_value": false,
      "site": "004635d4",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463588",
      "incomplete_value": false,
      "site": "00463594",
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
            "const:198:8"
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
      "004635d4",
      "DATA",
      [
        "storage",
        "00c64198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004635d4",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463570.md#insn-00463588) · [`004635b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463570.md#insn-004635b8)
- 新版 `004635c8`（命令位置の公開資料なし） · `004635f8`（命令位置の公開資料なし）

~~~diff
- 00463588 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00463588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004635c8 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 004635c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004635c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004635c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463588 bytes 08610691
+ 004635c8 bytes 08611691
- 004635b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004635b8 ["INT_ADD", "register:40f0:8", ["const:4635b8:8", "const:4:8"]]
- 004635b8 ["CALLIND", null, ["register:0:8"]]
+ 004635f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004635f8 ["INT_ADD", "register:40f0:8", ["const:4635f8:8", "const:4:8"]]
+ 004635f8 ["CALLIND", null, ["register:0:8"]]
- 004635b8 bytes 00013fd6
+ 004635f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be3c626456c7c5e9d816d632a308dd6c"></a>

### [`004635cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004635cc.md) → [`0046360c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/0046360c.md) FUN_0046360c

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
      "definition_site": "00463638",
      "incomplete_value": false,
      "site": "00463638",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004635f8",
      "incomplete_value": false,
      "site": "004635f8",
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
            "const:198:8"
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
      "00463638",
      "DATA",
      [
        "storage",
        "00c64198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463638",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004635e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004635cc.md#insn-004635e0) · [`004635f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004635cc.md#insn-004635f0) · [`00463614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004635cc.md#insn-00463614)
- 新版 `00463620`（命令位置の公開資料なし） · `00463630`（命令位置の公開資料なし） · `00463654`（命令位置の公開資料なし）

~~~diff
- 004635e0 ["INT_ADD", "register:40f0:8", ["const:4635e0:8", "const:4:8"]]
- 004635e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00463620 ["INT_ADD", "register:40f0:8", ["const:463620:8", "const:4:8"]]
+ 00463620 ["CALL", null, ["callee:00c57e90:8"]]
- 004635e0 bytes 2cd11f94
+ 00463620 bytes 1cd21f94
- 004635f0 ["COPY", "tmp:0:8", ["const:198:8"]]
- 004635f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004635f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004635f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463630 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00463630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004635f0 bytes 08610691
+ 00463630 bytes 08611691
- 00463614 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463614 ["INT_ADD", "register:40f0:8", ["const:463614:8", "const:4:8"]]
- 00463614 ["CALLIND", null, ["register:0:8"]]
+ 00463654 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463654 ["INT_ADD", "register:40f0:8", ["const:463654:8", "const:4:8"]]
+ 00463654 ["CALLIND", null, ["register:0:8"]]
- 00463614 bytes 00013fd6
+ 00463654 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-223bac674cd670bdb79b38a763908ac5"></a>

### [`00463654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463654.md) → [`00463694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463694.md) FUN_00463694

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
      "definition_site": "004636b0",
      "incomplete_value": false,
      "site": "004636b0",
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
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463670",
      "incomplete_value": false,
      "site": "00463670",
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
            "const:198:8"
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
      "004636b0",
      "DATA",
      [
        "storage",
        "00c64198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004636b0",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046366c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463654.md#insn-0046366c) · [`00463690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463654.md#insn-00463690)
- 新版 `004636ac`（命令位置の公開資料なし） · `004636d0`（命令位置の公開資料なし）

~~~diff
- 0046366c ["COPY", "tmp:0:8", ["const:198:8"]]
- 0046366c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0046366c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0046366c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004636ac ["COPY", "tmp:0:8", ["const:598:8"]]
+ 004636ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004636ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004636ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0046366c bytes 29610691
+ 004636ac bytes 29611691
- 00463690 ["COPY", "register:0:8", ["register:4048:8"]]
- 00463690 ["INT_ADD", "register:40f0:8", ["const:463690:8", "const:4:8"]]
- 00463690 ["CALLIND", null, ["register:0:8"]]
+ 004636d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004636d0 ["INT_ADD", "register:40f0:8", ["const:4636d0:8", "const:4:8"]]
+ 004636d0 ["CALLIND", null, ["register:0:8"]]
- 00463690 bytes 20013fd6
+ 004636d0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0935aa3d036cdb4bd15bd2f6572948e4"></a>

### [`00463844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463844.md) → [`00463884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463884.md) FUN_00463884

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
      "definition_site": "00463890",
      "incomplete_value": false,
      "site": "0046389c",
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
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463850",
      "incomplete_value": false,
      "site": "0046385c",
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
            "const:218:8"
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
      "0046389c",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046389c",
      "DATA",
      [
        "storage",
        "00c64618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463844.md#insn-00463850)
- 新版 `00463890`（命令位置の公開資料なし）

~~~diff
- 00463850 ["COPY", "tmp:0:8", ["const:218:8"]]
- 00463850 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00463850 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00463850 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463890 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 00463890 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463890 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463890 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00463850 bytes 4a610891
+ 00463890 bytes 4a611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee70470a2044a16541bdf10dd803a6ff"></a>

### [`00463888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463888.md) → [`004638c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004638c8.md) FUN_004638c8

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
      "definition_site": "004638e0",
      "incomplete_value": false,
      "site": "004638ec",
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
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004638a0",
      "incomplete_value": false,
      "site": "004638ac",
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
            "const:218:8"
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
      "004638ec",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004638ec",
      "DATA",
      [
        "storage",
        "00c64618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004638a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463888.md#insn-004638a0) · [`004638d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463888.md#insn-004638d0)
- 新版 `004638e0`（命令位置の公開資料なし） · `00463910`（命令位置の公開資料なし）

~~~diff
- 004638a0 ["COPY", "tmp:0:8", ["const:218:8"]]
- 004638a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004638a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004638a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004638e0 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 004638e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004638e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004638e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004638a0 bytes 08610891
+ 004638e0 bytes 08611891
- 004638d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004638d0 ["INT_ADD", "register:40f0:8", ["const:4638d0:8", "const:4:8"]]
- 004638d0 ["CALLIND", null, ["register:0:8"]]
+ 00463910 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463910 ["INT_ADD", "register:40f0:8", ["const:463910:8", "const:4:8"]]
+ 00463910 ["CALLIND", null, ["register:0:8"]]
- 004638d0 bytes 00013fd6
+ 00463910 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39a1fdc3e7577d4c979b16b4c123f8c1"></a>

### [`004638e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004638e4.md) → [`00463924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463924.md) FUN_00463924

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
      "definition_site": "00463950",
      "incomplete_value": false,
      "site": "00463950",
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
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463910",
      "incomplete_value": false,
      "site": "00463910",
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
            "const:218:8"
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
      "00463950",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463950",
      "DATA",
      [
        "storage",
        "00c64618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004638f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004638e4.md#insn-004638f8) · [`00463908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004638e4.md#insn-00463908) · [`0046392c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/004638e4.md#insn-0046392c)
- 新版 `00463938`（命令位置の公開資料なし） · `00463948`（命令位置の公開資料なし） · `0046396c`（命令位置の公開資料なし）

~~~diff
- 004638f8 ["INT_ADD", "register:40f0:8", ["const:4638f8:8", "const:4:8"]]
- 004638f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00463938 ["INT_ADD", "register:40f0:8", ["const:463938:8", "const:4:8"]]
+ 00463938 ["CALL", null, ["callee:00c57e90:8"]]
- 004638f8 bytes 66d01f94
+ 00463938 bytes 56d11f94
- 00463908 ["COPY", "tmp:0:8", ["const:218:8"]]
- 00463908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463948 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 00463948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463908 bytes 08610891
+ 00463948 bytes 08611891
- 0046392c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046392c ["INT_ADD", "register:40f0:8", ["const:46392c:8", "const:4:8"]]
- 0046392c ["CALLIND", null, ["register:0:8"]]
+ 0046396c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046396c ["INT_ADD", "register:40f0:8", ["const:46396c:8", "const:4:8"]]
+ 0046396c ["CALLIND", null, ["register:0:8"]]
- 0046392c bytes 00013fd6
+ 0046396c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f078e875783fe8349ea45bea297a6170"></a>

### [`0046396c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046396c.md) → [`004639ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004639ac.md) FUN_004639ac

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
      "definition_site": "004639c8",
      "incomplete_value": false,
      "site": "004639c8",
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
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463988",
      "incomplete_value": false,
      "site": "00463988",
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
            "const:218:8"
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
      "004639c8",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004639c8",
      "DATA",
      [
        "storage",
        "00c64618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046396c.md#insn-00463984) · [`004639a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/0046396c.md#insn-004639a8)
- 新版 `004639c4`（命令位置の公開資料なし） · `004639e8`（命令位置の公開資料なし）

~~~diff
- 00463984 ["COPY", "tmp:0:8", ["const:218:8"]]
- 00463984 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00463984 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00463984 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004639c4 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 004639c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004639c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004639c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00463984 bytes 29610891
+ 004639c4 bytes 29611891
- 004639a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004639a8 ["INT_ADD", "register:40f0:8", ["const:4639a8:8", "const:4:8"]]
- 004639a8 ["CALLIND", null, ["register:0:8"]]
+ 004639e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004639e8 ["INT_ADD", "register:40f0:8", ["const:4639e8:8", "const:4:8"]]
+ 004639e8 ["CALLIND", null, ["register:0:8"]]
- 004639a8 bytes 20013fd6
+ 004639e8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-869101e79195f22cf3af143a60504c87"></a>

### [`00463b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463b04.md) → [`00463b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463b44.md) FUN_00463b44

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
      "definition_site": "00463b50",
      "incomplete_value": false,
      "site": "00463b5c",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463b10",
      "incomplete_value": false,
      "site": "00463b1c",
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
            "const:298:8"
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
      "00463b5c",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463b5c",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463b04.md#insn-00463b10)
- 新版 `00463b50`（命令位置の公開資料なし）

~~~diff
- 00463b10 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00463b10 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00463b10 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00463b10 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463b50 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 00463b50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463b50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463b50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00463b10 bytes 4a610a91
+ 00463b50 bytes 4a611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25ad7a6a398434ba6e91e9c035c07bd8"></a>

### [`00463b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463b48.md) → [`00463b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463b88.md) FUN_00463b88

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
      "definition_site": "00463ba0",
      "incomplete_value": false,
      "site": "00463bac",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463b60",
      "incomplete_value": false,
      "site": "00463b6c",
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
            "const:298:8"
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
      "00463bac",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463bac",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463b48.md#insn-00463b60) · [`00463b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463b48.md#insn-00463b90)
- 新版 `00463ba0`（命令位置の公開資料なし） · `00463bd0`（命令位置の公開資料なし）

~~~diff
- 00463b60 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00463b60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463b60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463b60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463ba0 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 00463ba0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463ba0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463ba0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463b60 bytes 08610a91
+ 00463ba0 bytes 08611a91
- 00463b90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463b90 ["INT_ADD", "register:40f0:8", ["const:463b90:8", "const:4:8"]]
- 00463b90 ["CALLIND", null, ["register:0:8"]]
+ 00463bd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463bd0 ["INT_ADD", "register:40f0:8", ["const:463bd0:8", "const:4:8"]]
+ 00463bd0 ["CALLIND", null, ["register:0:8"]]
- 00463b90 bytes 00013fd6
+ 00463bd0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a37fab805bdfecc71d10c2ca5dbfebb6"></a>

### [`00463ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463ba4.md) → [`00463be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463be4.md) FUN_00463be4

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
      "definition_site": "00463c10",
      "incomplete_value": false,
      "site": "00463c10",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463bd0",
      "incomplete_value": false,
      "site": "00463bd0",
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
            "const:298:8"
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
      "00463c10",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463c10",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463ba4.md#insn-00463bb8) · [`00463bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463ba4.md#insn-00463bc8) · [`00463bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463ba4.md#insn-00463bec)
- 新版 `00463bf8`（命令位置の公開資料なし） · `00463c08`（命令位置の公開資料なし） · `00463c2c`（命令位置の公開資料なし）

~~~diff
- 00463bb8 ["INT_ADD", "register:40f0:8", ["const:463bb8:8", "const:4:8"]]
- 00463bb8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00463bf8 ["INT_ADD", "register:40f0:8", ["const:463bf8:8", "const:4:8"]]
+ 00463bf8 ["CALL", null, ["callee:00c57e90:8"]]
- 00463bb8 bytes b6cf1f94
+ 00463bf8 bytes a6d01f94
- 00463bc8 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00463bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463c08 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 00463c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463bc8 bytes 08610a91
+ 00463c08 bytes 08611a91
- 00463bec ["COPY", "register:0:8", ["register:4040:8"]]
- 00463bec ["INT_ADD", "register:40f0:8", ["const:463bec:8", "const:4:8"]]
- 00463bec ["CALLIND", null, ["register:0:8"]]
+ 00463c2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463c2c ["INT_ADD", "register:40f0:8", ["const:463c2c:8", "const:4:8"]]
+ 00463c2c ["CALLIND", null, ["register:0:8"]]
- 00463bec bytes 00013fd6
+ 00463c2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3636733a902e0e5945ea64f1ab9e7d3"></a>

### [`00463c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463c2c.md) → [`00463c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463c6c.md) FUN_00463c6c

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
      "definition_site": "00463c88",
      "incomplete_value": false,
      "site": "00463c88",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463c48",
      "incomplete_value": false,
      "site": "00463c48",
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
            "const:298:8"
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
      "00463c88",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463c88",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463c2c.md#insn-00463c44) · [`00463c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463c2c.md#insn-00463c68)
- 新版 `00463c84`（命令位置の公開資料なし） · `00463ca8`（命令位置の公開資料なし）

~~~diff
- 00463c44 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00463c44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00463c44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00463c44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00463c84 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 00463c84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00463c84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00463c84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00463c44 bytes 29610a91
+ 00463c84 bytes 29611a91
- 00463c68 ["COPY", "register:0:8", ["register:4048:8"]]
- 00463c68 ["INT_ADD", "register:40f0:8", ["const:463c68:8", "const:4:8"]]
- 00463c68 ["CALLIND", null, ["register:0:8"]]
+ 00463ca8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00463ca8 ["INT_ADD", "register:40f0:8", ["const:463ca8:8", "const:4:8"]]
+ 00463ca8 ["CALLIND", null, ["register:0:8"]]
- 00463c68 bytes 20013fd6
+ 00463ca8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bd41b11817108ef1b481d3cf10410bf"></a>

### [`00463dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463dc4.md) → [`00463e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463e04.md) FUN_00463e04

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
      "definition_site": "00463e10",
      "incomplete_value": false,
      "site": "00463e1c",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463dd0",
      "incomplete_value": false,
      "site": "00463ddc",
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
            "const:318:8"
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
      "00463e1c",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463e1c",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463dc4.md#insn-00463dd0)
- 新版 `00463e10`（命令位置の公開資料なし）

~~~diff
- 00463dd0 ["COPY", "tmp:0:8", ["const:318:8"]]
- 00463dd0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00463dd0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00463dd0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463e10 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00463e10 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463e10 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463e10 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00463dd0 bytes 4a610c91
+ 00463e10 bytes 4a611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8a4ac6c2a40a4dc71aef7764cdcf2ca"></a>

### [`00463e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e08.md) → [`00463e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463e48.md) FUN_00463e48

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
      "definition_site": "00463e60",
      "incomplete_value": false,
      "site": "00463e6c",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463e20",
      "incomplete_value": false,
      "site": "00463e2c",
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
            "const:318:8"
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
      "00463e6c",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463e6c",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e08.md#insn-00463e20) · [`00463e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e08.md#insn-00463e50)
- 新版 `00463e60`（命令位置の公開資料なし） · `00463e90`（命令位置の公開資料なし）

~~~diff
- 00463e20 ["COPY", "tmp:0:8", ["const:318:8"]]
- 00463e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463e60 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00463e60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463e60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463e60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463e20 bytes 08610c91
+ 00463e60 bytes 08611c91
- 00463e50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463e50 ["INT_ADD", "register:40f0:8", ["const:463e50:8", "const:4:8"]]
- 00463e50 ["CALLIND", null, ["register:0:8"]]
+ 00463e90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463e90 ["INT_ADD", "register:40f0:8", ["const:463e90:8", "const:4:8"]]
+ 00463e90 ["CALLIND", null, ["register:0:8"]]
- 00463e50 bytes 00013fd6
+ 00463e90 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59d5461ce8d9ea972bcacc94cb33d992"></a>

### [`00463e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e64.md) → [`00463ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463ea4.md) FUN_00463ea4

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
      "definition_site": "00463ed0",
      "incomplete_value": false,
      "site": "00463ed0",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463e90",
      "incomplete_value": false,
      "site": "00463e90",
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
            "const:318:8"
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
      "00463ed0",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463ed0",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e64.md#insn-00463e78) · [`00463e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e64.md#insn-00463e88) · [`00463eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463e64.md#insn-00463eac)
- 新版 `00463eb8`（命令位置の公開資料なし） · `00463ec8`（命令位置の公開資料なし） · `00463eec`（命令位置の公開資料なし）

~~~diff
- 00463e78 ["INT_ADD", "register:40f0:8", ["const:463e78:8", "const:4:8"]]
- 00463e78 ["CALL", null, ["callee:00c57e90:8"]]
+ 00463eb8 ["INT_ADD", "register:40f0:8", ["const:463eb8:8", "const:4:8"]]
+ 00463eb8 ["CALL", null, ["callee:00c57e90:8"]]
- 00463e78 bytes 06cf1f94
+ 00463eb8 bytes f6cf1f94
- 00463e88 ["COPY", "tmp:0:8", ["const:318:8"]]
- 00463e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463ec8 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00463ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463e88 bytes 08610c91
+ 00463ec8 bytes 08611c91
- 00463eac ["COPY", "register:0:8", ["register:4040:8"]]
- 00463eac ["INT_ADD", "register:40f0:8", ["const:463eac:8", "const:4:8"]]
- 00463eac ["CALLIND", null, ["register:0:8"]]
+ 00463eec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463eec ["INT_ADD", "register:40f0:8", ["const:463eec:8", "const:4:8"]]
+ 00463eec ["CALLIND", null, ["register:0:8"]]
- 00463eac bytes 00013fd6
+ 00463eec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69b50b51f0ddb83373627e2804bc2c4b"></a>

### [`00463eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463eec.md) → [`00463f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463f2c.md) FUN_00463f2c

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
      "definition_site": "00463f48",
      "incomplete_value": false,
      "site": "00463f48",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463f08",
      "incomplete_value": false,
      "site": "00463f08",
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
            "const:318:8"
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
      "00463f48",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463f48",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463eec.md#insn-00463f04) · [`00463f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463eec.md#insn-00463f28)
- 新版 `00463f44`（命令位置の公開資料なし） · `00463f68`（命令位置の公開資料なし）

~~~diff
- 00463f04 ["COPY", "tmp:0:8", ["const:318:8"]]
- 00463f04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00463f04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00463f04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00463f44 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 00463f44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00463f44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00463f44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00463f04 bytes 29610c91
+ 00463f44 bytes 29611c91
- 00463f28 ["COPY", "register:0:8", ["register:4048:8"]]
- 00463f28 ["INT_ADD", "register:40f0:8", ["const:463f28:8", "const:4:8"]]
- 00463f28 ["CALLIND", null, ["register:0:8"]]
+ 00463f68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00463f68 ["INT_ADD", "register:40f0:8", ["const:463f68:8", "const:4:8"]]
+ 00463f68 ["CALLIND", null, ["register:0:8"]]
- 00463f28 bytes 20013fd6
+ 00463f68 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee08ce7f3c469b08d305df0e8022ae10"></a>

### [`00463fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463fe8.md) → [`00464028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464028.md) FUN_00464028

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00461a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461a40.md) [`0046475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/0046475c.md) [`00464838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464838.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md) [`00464878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464878.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.54% / 新版 95.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00464300",
      "incomplete_value": true,
      "site": "00464300",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004642c0",
      "incomplete_value": true,
      "site": "004642c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 60,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004642f4",
      "incomplete_value": true,
      "site": "00464304",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004642b4",
      "incomplete_value": true,
      "site": "004642c4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 61,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046438c",
      "incomplete_value": true,
      "site": "00464398",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:65f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046434c",
      "incomplete_value": true,
      "site": "00464358",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:583:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 70,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004642f0",
      "READ",
      [
        "storage",
        "002a89e7",
        null,
        "string"
      ]
    ],
    [
      "004642f4",
      "READ",
      [
        "storage",
        "002a89ee",
        null,
        "string"
      ]
    ],
    [
      "0046438c",
      "READ",
      [
        "storage",
        "002a7583",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004642f0",
      "READ",
      [
        "storage",
        "002a8ab4",
        null,
        "string"
      ]
    ],
    [
      "004642f4",
      "READ",
      [
        "storage",
        "002a8abb",
        null,
        "string"
      ]
    ],
    [
      "0046438c",
      "READ",
      [
        "storage",
        "002a765f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463fe8.md#insn-00464318) · [`00464050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463fe8.md#insn-00464050) · [`0046407c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00463/00463fe8.md#insn-0046407c)
- 新版 `00464358`（命令位置の公開資料なし） · `00464090`（命令位置の公開資料なし） · `004640bc`（命令位置の公開資料なし）

~~~diff
- 00464318 ["INT_ADD", "register:40f0:8", ["const:464318:8", "const:4:8"]]
- 00464318 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00464358 ["INT_ADD", "register:40f0:8", ["const:464358:8", "const:4:8"]]
+ 00464358 ["CALL", null, ["callee:00c57eb0:8"]]
- 00464318 bytes e6cd1f94
+ 00464358 bytes d6ce1f94
- 00464050 ["INT_ADD", "register:40f0:8", ["const:464050:8", "const:4:8"]]
- 00464050 ["CALL", null, ["callee:0044108c:8"]]
+ 00464090 ["INT_ADD", "register:40f0:8", ["const:464090:8", "const:4:8"]]
+ 00464090 ["CALL", null, ["callee:0044108c:8"]]
- 00464050 bytes ff73ff97
+ 00464090 bytes ff73ff97
- 0046407c ["INT_ADD", "register:40f0:8", ["const:46407c:8", "const:4:8"]]
- 0046407c ["CALL", null, ["callee:00c57eb0:8"]]
+ 004640bc ["INT_ADD", "register:40f0:8", ["const:4640bc:8", "const:4:8"]]
+ 004640bc ["CALL", null, ["callee:00c57eb0:8"]]
- 0046407c bytes 8dce1f94
+ 004640bc bytes 7dcf1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61e4d789cd80a4a518b5725e05eaa735"></a>

### [`00464ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ac8.md) → [`00464b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464b08.md) FUN_00464b08

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
      "definition_site": "00464b14",
      "incomplete_value": false,
      "site": "00464b20",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464ad4",
      "incomplete_value": false,
      "site": "00464ae0",
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
            "const:398:8"
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
      "00464b20",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464b20",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ac8.md#insn-00464ad4)
- 新版 `00464b14`（命令位置の公開資料なし）

~~~diff
- 00464ad4 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00464ad4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00464ad4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00464ad4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00464b14 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00464b14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00464b14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00464b14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00464ad4 bytes 4a610e91
+ 00464b14 bytes 4a611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eac2706b83d669575cbe0a0358d710be"></a>

### [`00464b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b0c.md) → [`00464b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464b4c.md) FUN_00464b4c

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
      "definition_site": "00464b64",
      "incomplete_value": false,
      "site": "00464b70",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464b24",
      "incomplete_value": false,
      "site": "00464b30",
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
            "const:398:8"
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
      "00464b70",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464b70",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b0c.md#insn-00464b24) · [`00464b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b0c.md#insn-00464b54)
- 新版 `00464b64`（命令位置の公開資料なし） · `00464b94`（命令位置の公開資料なし）

~~~diff
- 00464b24 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00464b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00464b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00464b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00464b64 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00464b64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00464b64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00464b64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00464b24 bytes 08610e91
+ 00464b64 bytes 08611e91
- 00464b54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00464b54 ["INT_ADD", "register:40f0:8", ["const:464b54:8", "const:4:8"]]
- 00464b54 ["CALLIND", null, ["register:0:8"]]
+ 00464b94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464b94 ["INT_ADD", "register:40f0:8", ["const:464b94:8", "const:4:8"]]
+ 00464b94 ["CALLIND", null, ["register:0:8"]]
- 00464b54 bytes 00013fd6
+ 00464b94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-118893d95ee1328ffe73d52fe2adeb50"></a>

### [`00464b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b68.md) → [`00464ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464ba8.md) FUN_00464ba8

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
      "definition_site": "00464bd4",
      "incomplete_value": false,
      "site": "00464bd4",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464b94",
      "incomplete_value": false,
      "site": "00464b94",
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
            "const:398:8"
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
      "00464bd4",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464bd4",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b68.md#insn-00464b7c) · [`00464b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b68.md#insn-00464b8c) · [`00464bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464b68.md#insn-00464bb0)
- 新版 `00464bbc`（命令位置の公開資料なし） · `00464bcc`（命令位置の公開資料なし） · `00464bf0`（命令位置の公開資料なし）

~~~diff
- 00464b7c ["INT_ADD", "register:40f0:8", ["const:464b7c:8", "const:4:8"]]
- 00464b7c ["CALL", null, ["callee:00c57e90:8"]]
+ 00464bbc ["INT_ADD", "register:40f0:8", ["const:464bbc:8", "const:4:8"]]
+ 00464bbc ["CALL", null, ["callee:00c57e90:8"]]
- 00464b7c bytes c5cb1f94
+ 00464bbc bytes b5cc1f94
- 00464b8c ["COPY", "tmp:0:8", ["const:398:8"]]
- 00464b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00464b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00464b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00464bcc ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00464bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00464bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00464bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00464b8c bytes 08610e91
+ 00464bcc bytes 08611e91
- 00464bb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00464bb0 ["INT_ADD", "register:40f0:8", ["const:464bb0:8", "const:4:8"]]
- 00464bb0 ["CALLIND", null, ["register:0:8"]]
+ 00464bf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464bf0 ["INT_ADD", "register:40f0:8", ["const:464bf0:8", "const:4:8"]]
+ 00464bf0 ["CALLIND", null, ["register:0:8"]]
- 00464bb0 bytes 00013fd6
+ 00464bf0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2551ce4fc8822a5c6c3fe5aba78bc6b"></a>

### [`00464bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464bf0.md) → [`00464c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464c30.md) FUN_00464c30

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
      "definition_site": "00464c4c",
      "incomplete_value": false,
      "site": "00464c4c",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464c0c",
      "incomplete_value": false,
      "site": "00464c0c",
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
            "const:398:8"
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
      "00464c4c",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464c4c",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464bf0.md#insn-00464c08) · [`00464c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464bf0.md#insn-00464c2c)
- 新版 `00464c48`（命令位置の公開資料なし） · `00464c6c`（命令位置の公開資料なし）

~~~diff
- 00464c08 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00464c08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00464c08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00464c08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00464c48 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00464c48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00464c48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00464c48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00464c08 bytes 29610e91
+ 00464c48 bytes 29611e91
- 00464c2c ["COPY", "register:0:8", ["register:4048:8"]]
- 00464c2c ["INT_ADD", "register:40f0:8", ["const:464c2c:8", "const:4:8"]]
- 00464c2c ["CALLIND", null, ["register:0:8"]]
+ 00464c6c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00464c6c ["INT_ADD", "register:40f0:8", ["const:464c6c:8", "const:4:8"]]
+ 00464c6c ["CALLIND", null, ["register:0:8"]]
- 00464c2c bytes 20013fd6
+ 00464c6c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24cd831a58da611f77e1b982f9b6ea16"></a>

### [`00464dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464dd0.md) → [`00464e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464e10.md) FUN_00464e10

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
      "definition_site": "00464e1c",
      "incomplete_value": false,
      "site": "00464e28",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464ddc",
      "incomplete_value": false,
      "site": "00464de8",
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
            "const:418:8"
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
      "00464e28",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464e28",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464dd0.md#insn-00464ddc)
- 新版 `00464e1c`（命令位置の公開資料なし）

~~~diff
- 00464ddc ["COPY", "tmp:0:8", ["const:418:8"]]
- 00464ddc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00464ddc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00464ddc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00464e1c ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00464e1c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00464e1c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00464e1c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00464ddc bytes 4a611091
+ 00464e1c bytes 4a612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17164edcdff754b18bed7f494bbc8df6"></a>

### [`00464e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e14.md) → [`00464e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464e54.md) FUN_00464e54

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
      "definition_site": "00464e6c",
      "incomplete_value": false,
      "site": "00464e78",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464e2c",
      "incomplete_value": false,
      "site": "00464e38",
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
            "const:418:8"
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
      "00464e78",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464e78",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e14.md#insn-00464e2c) · [`00464e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e14.md#insn-00464e5c)
- 新版 `00464e6c`（命令位置の公開資料なし） · `00464e9c`（命令位置の公開資料なし）

~~~diff
- 00464e2c ["COPY", "tmp:0:8", ["const:418:8"]]
- 00464e2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00464e2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00464e2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00464e6c ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00464e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00464e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00464e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00464e2c bytes 08611091
+ 00464e6c bytes 08612091
- 00464e5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00464e5c ["INT_ADD", "register:40f0:8", ["const:464e5c:8", "const:4:8"]]
- 00464e5c ["CALLIND", null, ["register:0:8"]]
+ 00464e9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464e9c ["INT_ADD", "register:40f0:8", ["const:464e9c:8", "const:4:8"]]
+ 00464e9c ["CALLIND", null, ["register:0:8"]]
- 00464e5c bytes 00013fd6
+ 00464e9c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9314cb8f151257993526665868f2ddc4"></a>

### [`00464e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e70.md) → [`00464eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464eb0.md) FUN_00464eb0

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
      "definition_site": "00464edc",
      "incomplete_value": false,
      "site": "00464edc",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464e9c",
      "incomplete_value": false,
      "site": "00464e9c",
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
            "const:418:8"
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
      "00464edc",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464edc",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e70.md#insn-00464e84) · [`00464e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e70.md#insn-00464e94) · [`00464eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464e70.md#insn-00464eb8)
- 新版 `00464ec4`（命令位置の公開資料なし） · `00464ed4`（命令位置の公開資料なし） · `00464ef8`（命令位置の公開資料なし）

~~~diff
- 00464e84 ["INT_ADD", "register:40f0:8", ["const:464e84:8", "const:4:8"]]
- 00464e84 ["CALL", null, ["callee:00c57e90:8"]]
+ 00464ec4 ["INT_ADD", "register:40f0:8", ["const:464ec4:8", "const:4:8"]]
+ 00464ec4 ["CALL", null, ["callee:00c57e90:8"]]
- 00464e84 bytes 03cb1f94
+ 00464ec4 bytes f3cb1f94
- 00464e94 ["COPY", "tmp:0:8", ["const:418:8"]]
- 00464e94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00464e94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00464e94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00464ed4 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00464ed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00464ed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00464ed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00464e94 bytes 08611091
+ 00464ed4 bytes 08612091
- 00464eb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00464eb8 ["INT_ADD", "register:40f0:8", ["const:464eb8:8", "const:4:8"]]
- 00464eb8 ["CALLIND", null, ["register:0:8"]]
+ 00464ef8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464ef8 ["INT_ADD", "register:40f0:8", ["const:464ef8:8", "const:4:8"]]
+ 00464ef8 ["CALLIND", null, ["register:0:8"]]
- 00464eb8 bytes 00013fd6
+ 00464ef8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bb27e4e734335870431d6d5e14ffeaa"></a>

### [`00464ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ef8.md) → [`00464f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464f38.md) FUN_00464f38

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
      "definition_site": "00464f54",
      "incomplete_value": false,
      "site": "00464f54",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464f14",
      "incomplete_value": false,
      "site": "00464f14",
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
            "const:418:8"
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
      "00464f54",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464f54",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ef8.md#insn-00464f10) · [`00464f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00464/00464ef8.md#insn-00464f34)
- 新版 `00464f50`（命令位置の公開資料なし） · `00464f74`（命令位置の公開資料なし）

~~~diff
- 00464f10 ["COPY", "tmp:0:8", ["const:418:8"]]
- 00464f10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00464f10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00464f10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00464f50 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00464f50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00464f50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00464f50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00464f10 bytes 29611091
+ 00464f50 bytes 29612091
- 00464f34 ["COPY", "register:0:8", ["register:4048:8"]]
- 00464f34 ["INT_ADD", "register:40f0:8", ["const:464f34:8", "const:4:8"]]
- 00464f34 ["CALLIND", null, ["register:0:8"]]
+ 00464f74 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00464f74 ["INT_ADD", "register:40f0:8", ["const:464f74:8", "const:4:8"]]
+ 00464f74 ["CALLIND", null, ["register:0:8"]]
- 00464f34 bytes 20013fd6
+ 00464f74 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d70ef86229893a9d6b1b938928da8495"></a>

### [`004650d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004650d0.md) → [`00465110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465110.md) FUN_00465110

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
      "definition_site": "00465124",
      "incomplete_value": false,
      "site": "00465128",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004650e4",
      "incomplete_value": false,
      "site": "004650e8",
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
            "const:498:8"
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
      "00465128",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465128",
      "DATA",
      [
        "storage",
        "00c64898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004650dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004650d0.md#insn-004650dc) · [`004650e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004650d0.md#insn-004650e4)
- 新版 `0046511c`（命令位置の公開資料なし） · `00465124`（命令位置の公開資料なし）

~~~diff
- 004650dc ["INT_ADD", "register:40f0:8", ["const:4650dc:8", "const:4:8"]]
- 004650dc ["CALL", null, ["callee:00c57e90:8"]]
+ 0046511c ["INT_ADD", "register:40f0:8", ["const:46511c:8", "const:4:8"]]
+ 0046511c ["CALL", null, ["callee:00c57e90:8"]]
- 004650dc bytes 6dca1f94
+ 0046511c bytes 5dcb1f94
- 004650e4 ["COPY", "tmp:0:8", ["const:498:8"]]
- 004650e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004650e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004650e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465124 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00465124 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465124 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465124 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004650e4 bytes 08611291
+ 00465124 bytes 08612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a7165c0a09cd81779c0dffe7750464d"></a>

### [`004650f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004650f4.md) → [`00465134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465134.md) FUN_00465134

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
      "definition_site": "00465138",
      "incomplete_value": false,
      "site": "0046513c",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004650f8",
      "incomplete_value": false,
      "site": "004650fc",
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
            "const:498:8"
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
      "0046513c",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046513c",
      "DATA",
      [
        "storage",
        "00c64898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004650f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004650f4.md#insn-004650f8)
- 新版 `00465138`（命令位置の公開資料なし）

~~~diff
- 004650f8 ["COPY", "tmp:0:8", ["const:498:8"]]
- 004650f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004650f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004650f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465138 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00465138 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465138 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465138 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004650f8 bytes 08611291
+ 00465138 bytes 08612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f632d637728171b9c1cffdbcd7f980d4"></a>

### [`0046510c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046510c.md) → [`0046514c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046514c.md) FUN_0046514c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00465180",
      "incomplete_value": false,
      "site": "00465184",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465140",
      "incomplete_value": false,
      "site": "00465144",
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
            "const:6a0:8"
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
      "definition_site": "00465190",
      "incomplete_value": false,
      "site": "00465194",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465150",
      "incomplete_value": false,
      "site": "00465154",
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
            "const:6a0:8"
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
      "0046515c",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465168",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "00465180",
      "PARAM",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046515c",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465168",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00465180",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046510c.md#insn-00465144) · [`00465154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046510c.md#insn-00465154) · [`00465118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046510c.md#insn-00465118)
- 新版 `00465184`（命令位置の公開資料なし） · `00465194`（命令位置の公開資料なし） · `00465158`（命令位置の公開資料なし）

~~~diff
- 00465144 ["INT_ADD", "register:40f0:8", ["const:465144:8", "const:4:8"]]
- 00465144 ["CALL", null, ["callee:00c57e50:8"]]
+ 00465184 ["INT_ADD", "register:40f0:8", ["const:465184:8", "const:4:8"]]
+ 00465184 ["CALL", null, ["callee:00c57e50:8"]]
- 00465144 bytes 43ca1f94
+ 00465184 bytes 33cb1f94
- 00465154 ["INT_ADD", "register:40f0:8", ["const:465154:8", "const:4:8"]]
- 00465154 ["CALL", null, ["callee:00c57e70:8"]]
+ 00465194 ["INT_ADD", "register:40f0:8", ["const:465194:8", "const:4:8"]]
+ 00465194 ["CALL", null, ["callee:00c57e70:8"]]
- 00465154 bytes 47ca1f94
+ 00465194 bytes 37cb1f94
- 00465118 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00465118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00465118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00465118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465158 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 00465158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00465118 bytes 08811a91
+ 00465158 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a423820dc8a1587c4daf3cc94d3b1096"></a>

### [`00465188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465188.md) → [`004651c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004651c8.md) FUN_004651c8

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
      "definition_site": "004651dc",
      "incomplete_value": false,
      "site": "004651e0",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046519c",
      "incomplete_value": false,
      "site": "004651a0",
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
            "const:518:8"
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
      "004651e0",
      "DATA",
      [
        "storage",
        "00c64518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004651e0",
      "DATA",
      [
        "storage",
        "00c64918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465188.md#insn-00465194) · [`0046519c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465188.md#insn-0046519c)
- 新版 `004651d4`（命令位置の公開資料なし） · `004651dc`（命令位置の公開資料なし）

~~~diff
- 00465194 ["INT_ADD", "register:40f0:8", ["const:465194:8", "const:4:8"]]
- 00465194 ["CALL", null, ["callee:00c57e90:8"]]
+ 004651d4 ["INT_ADD", "register:40f0:8", ["const:4651d4:8", "const:4:8"]]
+ 004651d4 ["CALL", null, ["callee:00c57e90:8"]]
- 00465194 bytes 3fca1f94
+ 004651d4 bytes 2fcb1f94
- 0046519c ["COPY", "tmp:0:8", ["const:518:8"]]
- 0046519c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046519c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046519c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004651dc ["COPY", "tmp:0:8", ["const:918:8"]]
+ 004651dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004651dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004651dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046519c bytes 08611491
+ 004651dc bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a51bda5cbcd2d5e37d216e134ed60019"></a>

### [`004651ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651ac.md) → [`004651ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004651ec.md) FUN_004651ec

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
      "definition_site": "004651f0",
      "incomplete_value": false,
      "site": "004651f4",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004651b0",
      "incomplete_value": false,
      "site": "004651b4",
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
            "const:518:8"
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
      "004651f4",
      "DATA",
      [
        "storage",
        "00c64518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004651f4",
      "DATA",
      [
        "storage",
        "00c64918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004651b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651ac.md#insn-004651b0)
- 新版 `004651f0`（命令位置の公開資料なし）

~~~diff
- 004651b0 ["COPY", "tmp:0:8", ["const:518:8"]]
- 004651b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004651b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004651b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004651f0 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 004651f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004651f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004651f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004651b0 bytes 08611491
+ 004651f0 bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df2a9a8ea483ba3d668a12677ffb783b"></a>

### [`004651c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651c4.md) → [`00465204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465204.md) FUN_00465204

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00465244",
      "incomplete_value": false,
      "site": "0046524c",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465204",
      "incomplete_value": false,
      "site": "0046520c",
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
            "const:6a0:8"
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
      "definition_site": "0046525c",
      "incomplete_value": false,
      "site": "00465260",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046521c",
      "incomplete_value": false,
      "site": "00465220",
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
            "const:6a0:8"
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
      "0046521c",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465228",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "00465244",
      "PARAM",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046521c",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465228",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00465244",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046520c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651c4.md#insn-0046520c) · [`00465220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651c4.md#insn-00465220) · [`004651d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004651c4.md#insn-004651d4)
- 新版 `0046524c`（命令位置の公開資料なし） · `00465260`（命令位置の公開資料なし） · `00465214`（命令位置の公開資料なし）

~~~diff
- 0046520c ["INT_ADD", "register:40f0:8", ["const:46520c:8", "const:4:8"]]
- 0046520c ["CALL", null, ["callee:00c57e50:8"]]
+ 0046524c ["INT_ADD", "register:40f0:8", ["const:46524c:8", "const:4:8"]]
+ 0046524c ["CALL", null, ["callee:00c57e50:8"]]
- 0046520c bytes 11ca1f94
+ 0046524c bytes 01cb1f94
- 00465220 ["INT_ADD", "register:40f0:8", ["const:465220:8", "const:4:8"]]
- 00465220 ["CALL", null, ["callee:00c57e70:8"]]
+ 00465260 ["INT_ADD", "register:40f0:8", ["const:465260:8", "const:4:8"]]
+ 00465260 ["CALL", null, ["callee:00c57e70:8"]]
- 00465220 bytes 14ca1f94
+ 00465260 bytes 04cb1f94
- 004651d4 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 004651d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004651d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004651d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465214 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 00465214 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465214 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465214 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004651d4 bytes 08811a91
+ 00465214 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bd72371928120396e74d84d1db974dc"></a>

### [`00465258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465258.md) → [`00465298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465298.md) FUN_00465298

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
      "definition_site": "004652ac",
      "incomplete_value": false,
      "site": "004652b0",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046526c",
      "incomplete_value": false,
      "site": "00465270",
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
            "const:598:8"
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
      "004652b0",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004652b0",
      "DATA",
      [
        "storage",
        "00c64998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465258.md#insn-00465264) · [`0046526c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465258.md#insn-0046526c)
- 新版 `004652a4`（命令位置の公開資料なし） · `004652ac`（命令位置の公開資料なし）

~~~diff
- 00465264 ["INT_ADD", "register:40f0:8", ["const:465264:8", "const:4:8"]]
- 00465264 ["CALL", null, ["callee:00c57e90:8"]]
+ 004652a4 ["INT_ADD", "register:40f0:8", ["const:4652a4:8", "const:4:8"]]
+ 004652a4 ["CALL", null, ["callee:00c57e90:8"]]
- 00465264 bytes 0bca1f94
+ 004652a4 bytes fbca1f94
- 0046526c ["COPY", "tmp:0:8", ["const:598:8"]]
- 0046526c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046526c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046526c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004652ac ["COPY", "tmp:0:8", ["const:998:8"]]
+ 004652ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004652ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004652ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046526c bytes 08611691
+ 004652ac bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0b170f4d1b458cad86025901af8adee"></a>

### [`0046527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046527c.md) → [`004652bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004652bc.md) FUN_004652bc

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
      "definition_site": "004652c0",
      "incomplete_value": false,
      "site": "004652c4",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465280",
      "incomplete_value": false,
      "site": "00465284",
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
      "004652c4",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004652c4",
      "DATA",
      [
        "storage",
        "00c64998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046527c.md#insn-00465280)
- 新版 `004652c0`（命令位置の公開資料なし）

~~~diff
- 00465280 ["COPY", "tmp:0:8", ["const:598:8"]]
- 00465280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00465280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00465280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004652c0 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 004652c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004652c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004652c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00465280 bytes 08611691
+ 004652c0 bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-553598c1c15f2e6dee51b2bdbd52f21b"></a>

### [`00465294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465294.md) → [`004652d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004652d4.md) FUN_004652d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.73% / 新版 89.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00465378",
      "incomplete_value": true,
      "site": "00465378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465338",
      "incomplete_value": true,
      "site": "00465338",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ac:8"
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
      "definition_site": "00465464",
      "incomplete_value": true,
      "site": "00465464",
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
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465424",
      "incomplete_value": true,
      "site": "00465424",
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
              "LOAD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046544c",
      "incomplete_value": true,
      "site": "00465464",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:a98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046540c",
      "incomplete_value": true,
      "site": "00465424",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
                "const:698:8"
              ]
            ]
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
      "00465364",
      "READ",
      [
        "storage",
        "002bc3ac",
        null,
        "string"
      ]
    ],
    [
      "00465440",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046544c",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00465364",
      "READ",
      [
        "storage",
        "002bc3ec",
        null,
        "string"
      ]
    ],
    [
      "00465440",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046544c",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465294.md#insn-00465378) · [`00465424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465294.md#insn-00465424) · [`00465450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465294.md#insn-00465450)
- 新版 `004653b8`（命令位置の公開資料なし） · `00465464`（命令位置の公開資料なし） · `00465490`（命令位置の公開資料なし）

~~~diff
- 00465378 ["INT_ADD", "register:40f0:8", ["const:465378:8", "const:4:8"]]
- 00465378 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004653b8 ["INT_ADD", "register:40f0:8", ["const:4653b8:8", "const:4:8"]]
+ 004653b8 ["CALL", null, ["callee:00c57eb0:8"]]
- 00465378 bytes cec91f94
+ 004653b8 bytes beca1f94
- 00465424 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465424 ["INT_ADD", "register:40f0:8", ["const:465424:8", "const:4:8"]]
- 00465424 ["CALLIND", null, ["register:0:8"]]
+ 00465464 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465464 ["INT_ADD", "register:40f0:8", ["const:465464:8", "const:4:8"]]
+ 00465464 ["CALLIND", null, ["register:0:8"]]
- 00465424 bytes 00013fd6
+ 00465464 bytes 00013fd6
- 00465450 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465450 ["INT_ADD", "register:40f0:8", ["const:465450:8", "const:4:8"]]
- 00465450 ["CALLIND", null, ["register:0:8"]]
+ 00465490 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465490 ["INT_ADD", "register:40f0:8", ["const:465490:8", "const:4:8"]]
+ 00465490 ["CALLIND", null, ["register:0:8"]]
- 00465450 bytes 00013fd6
+ 00465490 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73c9c984cb6b6ec8fcd13826509459a5"></a>

### [`00465618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465618.md) → [`00465658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465658.md) FUN_00465658

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
      "definition_site": "0046566c",
      "incomplete_value": false,
      "site": "00465670",
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
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046562c",
      "incomplete_value": false,
      "site": "00465630",
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
            "const:618:8"
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
      "00465670",
      "DATA",
      [
        "storage",
        "00c64618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465670",
      "DATA",
      [
        "storage",
        "00c64a18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465618.md#insn-00465624) · [`0046562c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465618.md#insn-0046562c)
- 新版 `00465664`（命令位置の公開資料なし） · `0046566c`（命令位置の公開資料なし）

~~~diff
- 00465624 ["INT_ADD", "register:40f0:8", ["const:465624:8", "const:4:8"]]
- 00465624 ["CALL", null, ["callee:00c57e90:8"]]
+ 00465664 ["INT_ADD", "register:40f0:8", ["const:465664:8", "const:4:8"]]
+ 00465664 ["CALL", null, ["callee:00c57e90:8"]]
- 00465624 bytes 1bc91f94
+ 00465664 bytes 0bca1f94
- 0046562c ["COPY", "tmp:0:8", ["const:618:8"]]
- 0046562c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046562c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046562c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046566c ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 0046566c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046566c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046566c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046562c bytes 08611891
+ 0046566c bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0119c58f4311dd5b8a083da879e2b6e4"></a>

### [`0046563c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046563c.md) → [`0046567c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046567c.md) FUN_0046567c

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
      "definition_site": "00465680",
      "incomplete_value": false,
      "site": "00465684",
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
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465640",
      "incomplete_value": false,
      "site": "00465644",
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
      "00465684",
      "DATA",
      [
        "storage",
        "00c64618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465684",
      "DATA",
      [
        "storage",
        "00c64a18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/0046563c.md#insn-00465640)
- 新版 `00465680`（命令位置の公開資料なし）

~~~diff
- 00465640 ["COPY", "tmp:0:8", ["const:618:8"]]
- 00465640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00465640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00465640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465680 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 00465680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00465640 bytes 08611891
+ 00465680 bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f66a30368f3fe5ea05b90109235edaea"></a>

### [`00465654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465654.md) → [`00465694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465694.md) FUN_00465694

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004656d4",
      "incomplete_value": false,
      "site": "004656dc",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465694",
      "incomplete_value": false,
      "site": "0046569c",
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
            "const:6a0:8"
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
      "definition_site": "004656ec",
      "incomplete_value": false,
      "site": "004656f0",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004656ac",
      "incomplete_value": false,
      "site": "004656b0",
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
            "const:6a0:8"
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
      "004656ac",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "004656b8",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "004656d4",
      "PARAM",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004656ac",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "004656b8",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "004656d4",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046569c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465654.md#insn-0046569c) · [`004656b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465654.md#insn-004656b0) · [`00465664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465654.md#insn-00465664)
- 新版 `004656dc`（命令位置の公開資料なし） · `004656f0`（命令位置の公開資料なし） · `004656a4`（命令位置の公開資料なし）

~~~diff
- 0046569c ["INT_ADD", "register:40f0:8", ["const:46569c:8", "const:4:8"]]
- 0046569c ["CALL", null, ["callee:00c57e50:8"]]
+ 004656dc ["INT_ADD", "register:40f0:8", ["const:4656dc:8", "const:4:8"]]
+ 004656dc ["CALL", null, ["callee:00c57e50:8"]]
- 0046569c bytes edc81f94
+ 004656dc bytes ddc91f94
- 004656b0 ["INT_ADD", "register:40f0:8", ["const:4656b0:8", "const:4:8"]]
- 004656b0 ["CALL", null, ["callee:00c57e70:8"]]
+ 004656f0 ["INT_ADD", "register:40f0:8", ["const:4656f0:8", "const:4:8"]]
+ 004656f0 ["CALL", null, ["callee:00c57e70:8"]]
- 004656b0 bytes f0c81f94
+ 004656f0 bytes e0c91f94
- 00465664 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00465664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00465664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00465664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004656a4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 004656a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004656a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004656a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00465664 bytes 08811a91
+ 004656a4 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dae9d21c9331e07650f29410ca6ebade"></a>

### [`004656e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004656e4.md) → [`00465724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465724.md) FUN_00465724

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0046573c",
      "incomplete_value": false,
      "site": "00465740",
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
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004656fc",
      "incomplete_value": false,
      "site": "00465700",
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
      "00465740",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465740",
      "DATA",
      [
        "storage",
        "00c64a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004656fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004656e4.md#insn-004656fc) · [`00465728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004656e4.md#insn-00465728) · [`00465738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004656e4.md#insn-00465738)
- 新版 `0046573c`（命令位置の公開資料なし） · `00465768`（命令位置の公開資料なし） · `00465778`（命令位置の公開資料なし）

~~~diff
- 004656fc ["COPY", "tmp:0:8", ["const:698:8"]]
- 004656fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004656fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004656fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0046573c ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 0046573c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0046573c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0046573c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004656fc bytes 29611a91
+ 0046573c bytes 29612a91
- 00465728 ["INT_ADD", "register:40f0:8", ["const:465728:8", "const:4:8"]]
- 00465728 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00465768 ["INT_ADD", "register:40f0:8", ["const:465768:8", "const:4:8"]]
+ 00465768 ["CALL", null, ["callee:00c57eb0:8"]]
- 00465728 bytes e2c81f94
+ 00465768 bytes d2c91f94
- 00465738 ["INT_ADD", "register:40f0:8", ["const:465738:8", "const:4:8"]]
- 00465738 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00465778 ["INT_ADD", "register:40f0:8", ["const:465778:8", "const:4:8"]]
+ 00465778 ["CALL", null, ["callee:00c57eb0:8"]]
- 00465738 bytes dec81f94
+ 00465778 bytes cec91f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdcfbf51f1a6b4e3e148fb60e6651963"></a>

### [`00465754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465754.md) → [`00465794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465794.md) FUN_00465794

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "004657ac",
      "incomplete_value": false,
      "site": "004657b0",
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
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046576c",
      "incomplete_value": false,
      "site": "00465770",
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
      "004657b0",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004657b0",
      "DATA",
      [
        "storage",
        "00c64a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046576c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465754.md#insn-0046576c) · [`0046578c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465754.md#insn-0046578c) · [`004657a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465754.md#insn-004657a4)
- 新版 `004657ac`（命令位置の公開資料なし） · `004657cc`（命令位置の公開資料なし） · `004657e4`（命令位置の公開資料なし）

~~~diff
- 0046576c ["COPY", "tmp:0:8", ["const:698:8"]]
- 0046576c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0046576c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0046576c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004657ac ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 004657ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004657ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004657ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0046576c bytes 29611a91
+ 004657ac bytes 29612a91
- 0046578c ["INT_ADD", "register:40f0:8", ["const:46578c:8", "const:4:8"]]
- 0046578c ["CALL", null, ["callee:00c57eb0:8"]]
+ 004657cc ["INT_ADD", "register:40f0:8", ["const:4657cc:8", "const:4:8"]]
+ 004657cc ["CALL", null, ["callee:00c57eb0:8"]]
- 0046578c bytes c9c81f94
+ 004657cc bytes b9c91f94
- 004657a4 ["INT_ADD", "register:40f0:8", ["const:4657a4:8", "const:4:8"]]
- 004657a4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004657e4 ["INT_ADD", "register:40f0:8", ["const:4657e4:8", "const:4:8"]]
+ 004657e4 ["CALL", null, ["callee:00c57eb0:8"]]
- 004657a4 bytes c3c81f94
+ 004657e4 bytes b3c91f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-310db39b1ea0652c08a3e29b4567b2cc"></a>

### [`004657c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004657c4.md) → [`00465804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465804.md) FUN_00465804

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0046688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/0046688c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004668cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004668cc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00465828",
      "incomplete_value": false,
      "site": "00465828",
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
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004657e8",
      "incomplete_value": false,
      "site": "004657e8",
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
      "00465828",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465828",
      "DATA",
      [
        "storage",
        "00c64a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004657d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004657c4.md#insn-004657d8) · [`004657e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004657c4.md#insn-004657e4) · [`004657f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004657c4.md#insn-004657f0)
- 新版 `00465818`（命令位置の公開資料なし） · `00465824`（命令位置の公開資料なし） · `00465830`（命令位置の公開資料なし）

~~~diff
- 004657d8 ["INT_ADD", "register:40f0:8", ["const:4657d8:8", "const:4:8"]]
- 004657d8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00465818 ["INT_ADD", "register:40f0:8", ["const:465818:8", "const:4:8"]]
+ 00465818 ["CALL", null, ["callee:00c57e90:8"]]
- 004657d8 bytes aec81f94
+ 00465818 bytes 9ec91f94
- 004657e4 ["COPY", "tmp:0:8", ["const:698:8"]]
- 004657e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004657e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004657e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465824 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 00465824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004657e4 bytes 08611a91
+ 00465824 bytes 08612a91
- 004657f0 ["INT_ADD", "register:40f0:8", ["const:4657f0:8", "const:4:8"]]
- 004657f0 ["CALL", null, ["callee:004668cc:8"]]
+ 00465830 ["INT_ADD", "register:40f0:8", ["const:465830:8", "const:4:8"]]
+ 00465830 ["CALL", null, ["callee:004668cc:8"]]
- 004657f0 bytes 27040094
+ 00465830 bytes 27040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe81d149011dc4d043764fc9c457ec6f"></a>

### [`00465818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465818.md) → [`00465858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465858.md) FUN_00465858

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0046688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/0046688c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004668cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004668cc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00465864",
      "incomplete_value": false,
      "site": "00465864",
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
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465824",
      "incomplete_value": false,
      "site": "00465824",
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
      "00465864",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465864",
      "DATA",
      [
        "storage",
        "00c64a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/00465818.md#insn-00465820)
- 新版 `00465860`（命令位置の公開資料なし）

~~~diff
- 00465820 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00465820 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00465820 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00465820 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00465860 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 00465860 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00465860 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00465860 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00465820 bytes 29611a91
+ 00465860 bytes 29612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7f684024be9f1a89f99ee2775688611"></a>

### [`004658fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md) → [`0046593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md) FUN_0046593c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 22件 [`0043db14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db14.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`00450140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450140.md) [`00450710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450710.md) [`0055e834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e834.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0043db54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043db54.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) [`00450750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md) [`0055e874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e874.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 91.58% / 新版 91.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `call_target` 5件, `store_value` 9件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004659bc",
      "incomplete_value": true,
      "site": "004659bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0046597c",
      "incomplete_value": true,
      "site": "0046597c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8ce:8"
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
      "definition_site": "00465b90",
      "incomplete_value": true,
      "site": "00465b90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00465b50",
      "incomplete_value": true,
      "site": "00465b50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:953:8"
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
      "definition_site": "00465d90",
      "incomplete_value": true,
      "site": "00465da0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:960:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465d50",
      "incomplete_value": true,
      "site": "00465d60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:920:8"
              ]
            ]
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
      "004659a0",
      "READ",
      [
        "storage",
        "002b38ce",
        null,
        "string"
      ]
    ],
    [
      "00465a5c",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465a68",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004659a0",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ],
    [
      "00465a5c",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465a68",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md#insn-00465c58) · [`00465cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md#insn-00465cc4) · [`00465d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00465/004658fc.md#insn-00465d00)
- 新版 `00465c98`（命令位置の公開資料なし） · `00465d04`（命令位置の公開資料なし） · `00465d40`（命令位置の公開資料なし）

~~~diff
- 00465c58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465c58 ["INT_ADD", "register:40f0:8", ["const:465c58:8", "const:4:8"]]
- 00465c58 ["CALLIND", null, ["register:0:8"]]
+ 00465c98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465c98 ["INT_ADD", "register:40f0:8", ["const:465c98:8", "const:4:8"]]
+ 00465c98 ["CALLIND", null, ["register:0:8"]]
- 00465c58 bytes 00013fd6
+ 00465c98 bytes 00013fd6
- 00465cc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465cc4 ["INT_ADD", "register:40f0:8", ["const:465cc4:8", "const:4:8"]]
- 00465cc4 ["CALLIND", null, ["register:0:8"]]
+ 00465d04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465d04 ["INT_ADD", "register:40f0:8", ["const:465d04:8", "const:4:8"]]
+ 00465d04 ["CALLIND", null, ["register:0:8"]]
- 00465cc4 bytes 00013fd6
+ 00465d04 bytes 00013fd6
- 00465d00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465d00 ["INT_ADD", "register:40f0:8", ["const:465d00:8", "const:4:8"]]
- 00465d00 ["CALLIND", null, ["register:0:8"]]
+ 00465d40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465d40 ["INT_ADD", "register:40f0:8", ["const:465d40:8", "const:4:8"]]
+ 00465d40 ["CALLIND", null, ["register:0:8"]]
- 00465d00 bytes 00013fd6
+ 00465d40 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-325a8b1105b81b992d6f4279ea99a4c5"></a>

### [`00466980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466980.md) → [`004669c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004669c0.md) FUN_004669c0

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
      "definition_site": "004669d4",
      "incomplete_value": false,
      "site": "004669d8",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466994",
      "incomplete_value": false,
      "site": "00466998",
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
            "const:718:8"
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
      "004669d8",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004669d8",
      "DATA",
      [
        "storage",
        "00c64b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046698c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466980.md#insn-0046698c) · [`00466994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466980.md#insn-00466994)
- 新版 `004669cc`（命令位置の公開資料なし） · `004669d4`（命令位置の公開資料なし）

~~~diff
- 0046698c ["INT_ADD", "register:40f0:8", ["const:46698c:8", "const:4:8"]]
- 0046698c ["CALL", null, ["callee:00c57e90:8"]]
+ 004669cc ["INT_ADD", "register:40f0:8", ["const:4669cc:8", "const:4:8"]]
+ 004669cc ["CALL", null, ["callee:00c57e90:8"]]
- 0046698c bytes 41c41f94
+ 004669cc bytes 31c51f94
- 00466994 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00466994 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466994 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466994 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004669d4 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 004669d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004669d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004669d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466994 bytes 08611c91
+ 004669d4 bytes 08612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3e121132fba60c0709786b95f95dfd6"></a>

### [`004669a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669a4.md) → [`004669e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004669e4.md) FUN_004669e4

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
      "definition_site": "004669e8",
      "incomplete_value": false,
      "site": "004669ec",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004669a8",
      "incomplete_value": false,
      "site": "004669ac",
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
      "004669ec",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004669ec",
      "DATA",
      [
        "storage",
        "00c64b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004669a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669a4.md#insn-004669a8)
- 新版 `004669e8`（命令位置の公開資料なし）

~~~diff
- 004669a8 ["COPY", "tmp:0:8", ["const:718:8"]]
- 004669a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004669a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004669a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004669e8 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 004669e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004669e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004669e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004669a8 bytes 08611c91
+ 004669e8 bytes 08612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93052fdbc40574030576cd5d60a0abc3"></a>

### [`004669bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669bc.md) → [`004669fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004669fc.md) FUN_004669fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00466a34",
      "incomplete_value": false,
      "site": "00466a38",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004669f4",
      "incomplete_value": false,
      "site": "004669f8",
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
            "const:6a0:8"
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
      "definition_site": "00466a44",
      "incomplete_value": false,
      "site": "00466a48",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466a04",
      "incomplete_value": false,
      "site": "00466a08",
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
            "const:6a0:8"
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
      "00466a0c",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00466a18",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "00466a34",
      "PARAM",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00466a0c",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00466a18",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00466a34",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004669c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669bc.md#insn-004669c8) · [`004669f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669bc.md#insn-004669f8) · [`00466a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/004669bc.md#insn-00466a08)
- 新版 `00466a08`（命令位置の公開資料なし） · `00466a38`（命令位置の公開資料なし） · `00466a48`（命令位置の公開資料なし）

~~~diff
- 004669c8 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 004669c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004669c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004669c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466a08 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 00466a08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004669c8 bytes 08811a91
+ 00466a08 bytes 08812a91
- 004669f8 ["INT_ADD", "register:40f0:8", ["const:4669f8:8", "const:4:8"]]
- 004669f8 ["CALL", null, ["callee:00c57e50:8"]]
+ 00466a38 ["INT_ADD", "register:40f0:8", ["const:466a38:8", "const:4:8"]]
+ 00466a38 ["CALL", null, ["callee:00c57e50:8"]]
- 004669f8 bytes 16c41f94
+ 00466a38 bytes 06c51f94
- 00466a08 ["INT_ADD", "register:40f0:8", ["const:466a08:8", "const:4:8"]]
- 00466a08 ["CALL", null, ["callee:00c57e70:8"]]
+ 00466a48 ["INT_ADD", "register:40f0:8", ["const:466a48:8", "const:4:8"]]
+ 00466a48 ["CALL", null, ["callee:00c57e70:8"]]
- 00466a08 bytes 1ac41f94
+ 00466a48 bytes 0ac51f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35f8c3e44c6dc8642c4c660594982260"></a>

### [`00466a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a40.md) → [`00466a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466a80.md) FUN_00466a80

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
      "definition_site": "00466a94",
      "incomplete_value": false,
      "site": "00466a98",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466a54",
      "incomplete_value": false,
      "site": "00466a58",
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
            "const:798:8"
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
      "00466a98",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466a98",
      "DATA",
      [
        "storage",
        "00c64b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a40.md#insn-00466a4c) · [`00466a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a40.md#insn-00466a54)
- 新版 `00466a8c`（命令位置の公開資料なし） · `00466a94`（命令位置の公開資料なし）

~~~diff
- 00466a4c ["INT_ADD", "register:40f0:8", ["const:466a4c:8", "const:4:8"]]
- 00466a4c ["CALL", null, ["callee:00c57e90:8"]]
+ 00466a8c ["INT_ADD", "register:40f0:8", ["const:466a8c:8", "const:4:8"]]
+ 00466a8c ["CALL", null, ["callee:00c57e90:8"]]
- 00466a4c bytes 11c41f94
+ 00466a8c bytes 01c51f94
- 00466a54 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00466a54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466a54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466a54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466a94 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 00466a94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466a54 bytes 08611e91
+ 00466a94 bytes 08612e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0215f3e380559368cb16343bc7b8485"></a>

### [`00466a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a64.md) → [`00466aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466aa4.md) FUN_00466aa4

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
      "definition_site": "00466aa8",
      "incomplete_value": false,
      "site": "00466aac",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466a68",
      "incomplete_value": false,
      "site": "00466a6c",
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
            "const:798:8"
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
      "00466aac",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466aac",
      "DATA",
      [
        "storage",
        "00c64b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a64.md#insn-00466a68)
- 新版 `00466aa8`（命令位置の公開資料なし）

~~~diff
- 00466a68 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00466a68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466a68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466a68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466aa8 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 00466aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466a68 bytes 08611e91
+ 00466aa8 bytes 08612e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8dfb553389c643d9b355470557eebc1"></a>

### [`00466a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a7c.md) → [`00466abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466abc.md) FUN_00466abc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00466af4",
      "incomplete_value": false,
      "site": "00466af8",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466ab4",
      "incomplete_value": false,
      "site": "00466ab8",
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
            "const:6a0:8"
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
      "definition_site": "00466b04",
      "incomplete_value": false,
      "site": "00466b08",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466ac4",
      "incomplete_value": false,
      "site": "00466ac8",
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
            "const:6a0:8"
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
      "00466acc",
      "READ",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00466ad8",
      "READ",
      [
        "storage",
        "00ca4698",
        null,
        "undefined8"
      ]
    ],
    [
      "00466af4",
      "PARAM",
      [
        "storage",
        "00ca46a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00466acc",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00466ad8",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00466af4",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a7c.md#insn-00466a88) · [`00466ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a7c.md#insn-00466ab8) · [`00466ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466a7c.md#insn-00466ac8)
- 新版 `00466ac8`（命令位置の公開資料なし） · `00466af8`（命令位置の公開資料なし） · `00466b08`（命令位置の公開資料なし）

~~~diff
- 00466a88 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00466a88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466a88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466a88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466ac8 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 00466ac8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466ac8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466ac8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466a88 bytes 08811a91
+ 00466ac8 bytes 08812a91
- 00466ab8 ["INT_ADD", "register:40f0:8", ["const:466ab8:8", "const:4:8"]]
- 00466ab8 ["CALL", null, ["callee:00c57e50:8"]]
+ 00466af8 ["INT_ADD", "register:40f0:8", ["const:466af8:8", "const:4:8"]]
+ 00466af8 ["CALL", null, ["callee:00c57e50:8"]]
- 00466ab8 bytes e6c31f94
+ 00466af8 bytes d6c41f94
- 00466ac8 ["INT_ADD", "register:40f0:8", ["const:466ac8:8", "const:4:8"]]
- 00466ac8 ["CALL", null, ["callee:00c57e70:8"]]
+ 00466b08 ["INT_ADD", "register:40f0:8", ["const:466b08:8", "const:4:8"]]
+ 00466b08 ["CALL", null, ["callee:00c57e70:8"]]
- 00466ac8 bytes eac31f94
+ 00466b08 bytes dac41f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc80a57e37c4b2a28ab0ece473770a3f"></a>

### [`00466af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466af8.md) → [`00466b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466b38.md) FUN_00466b38

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
      "definition_site": "00466b44",
      "incomplete_value": false,
      "site": "00466b50",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466b04",
      "incomplete_value": false,
      "site": "00466b10",
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
            "const:818:8"
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
      "00466b50",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466b50",
      "DATA",
      [
        "storage",
        "00c64c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466af8.md#insn-00466b04)
- 新版 `00466b44`（命令位置の公開資料なし）

~~~diff
- 00466b04 ["COPY", "tmp:0:8", ["const:818:8"]]
- 00466b04 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00466b04 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00466b04 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00466b44 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 00466b44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00466b44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00466b44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00466b04 bytes 4a612091
+ 00466b44 bytes 4a613091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f19554265040957412e917087d065875"></a>

### [`00466b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b3c.md) → [`00466b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466b7c.md) FUN_00466b7c

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
      "definition_site": "00466b94",
      "incomplete_value": false,
      "site": "00466ba0",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466b54",
      "incomplete_value": false,
      "site": "00466b60",
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
            "const:818:8"
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
      "00466ba0",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466ba0",
      "DATA",
      [
        "storage",
        "00c64c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b3c.md#insn-00466b54) · [`00466b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b3c.md#insn-00466b84)
- 新版 `00466b94`（命令位置の公開資料なし） · `00466bc4`（命令位置の公開資料なし）

~~~diff
- 00466b54 ["COPY", "tmp:0:8", ["const:818:8"]]
- 00466b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466b94 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 00466b94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466b94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466b94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466b54 bytes 08612091
+ 00466b94 bytes 08613091
- 00466b84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00466b84 ["INT_ADD", "register:40f0:8", ["const:466b84:8", "const:4:8"]]
- 00466b84 ["CALLIND", null, ["register:0:8"]]
+ 00466bc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00466bc4 ["INT_ADD", "register:40f0:8", ["const:466bc4:8", "const:4:8"]]
+ 00466bc4 ["CALLIND", null, ["register:0:8"]]
- 00466b84 bytes 00013fd6
+ 00466bc4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fc8fa9713c73b93fb2eb63060d53c1b"></a>

### [`00466b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b98.md) → [`00466bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466bd8.md) FUN_00466bd8

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
      "definition_site": "00466c04",
      "incomplete_value": false,
      "site": "00466c04",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466bc4",
      "incomplete_value": false,
      "site": "00466bc4",
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
            "const:818:8"
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
      "00466c04",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466c04",
      "DATA",
      [
        "storage",
        "00c64c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b98.md#insn-00466bac) · [`00466bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b98.md#insn-00466bbc) · [`00466be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466b98.md#insn-00466be0)
- 新版 `00466bec`（命令位置の公開資料なし） · `00466bfc`（命令位置の公開資料なし） · `00466c20`（命令位置の公開資料なし）

~~~diff
- 00466bac ["INT_ADD", "register:40f0:8", ["const:466bac:8", "const:4:8"]]
- 00466bac ["CALL", null, ["callee:00c57e90:8"]]
+ 00466bec ["INT_ADD", "register:40f0:8", ["const:466bec:8", "const:4:8"]]
+ 00466bec ["CALL", null, ["callee:00c57e90:8"]]
- 00466bac bytes b9c31f94
+ 00466bec bytes a9c41f94
- 00466bbc ["COPY", "tmp:0:8", ["const:818:8"]]
- 00466bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466bfc ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 00466bfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466bfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466bfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466bbc bytes 08612091
+ 00466bfc bytes 08613091
- 00466be0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00466be0 ["INT_ADD", "register:40f0:8", ["const:466be0:8", "const:4:8"]]
- 00466be0 ["CALLIND", null, ["register:0:8"]]
+ 00466c20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00466c20 ["INT_ADD", "register:40f0:8", ["const:466c20:8", "const:4:8"]]
+ 00466c20 ["CALLIND", null, ["register:0:8"]]
- 00466be0 bytes 00013fd6
+ 00466c20 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe0d219c0fd0523bb25693ab223e3dbd"></a>

### [`00466c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466c20.md) → [`00466c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466c60.md) FUN_00466c60

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
      "definition_site": "00466c7c",
      "incomplete_value": false,
      "site": "00466c7c",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466c3c",
      "incomplete_value": false,
      "site": "00466c3c",
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
            "const:818:8"
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
      "00466c7c",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466c7c",
      "DATA",
      [
        "storage",
        "00c64c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466c20.md#insn-00466c38) · [`00466c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466c20.md#insn-00466c5c)
- 新版 `00466c78`（命令位置の公開資料なし） · `00466c9c`（命令位置の公開資料なし）

~~~diff
- 00466c38 ["COPY", "tmp:0:8", ["const:818:8"]]
- 00466c38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00466c38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00466c38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00466c78 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 00466c78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00466c78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00466c78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00466c38 bytes 29612091
+ 00466c78 bytes 29613091
- 00466c5c ["COPY", "register:0:8", ["register:4048:8"]]
- 00466c5c ["INT_ADD", "register:40f0:8", ["const:466c5c:8", "const:4:8"]]
- 00466c5c ["CALLIND", null, ["register:0:8"]]
+ 00466c9c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00466c9c ["INT_ADD", "register:40f0:8", ["const:466c9c:8", "const:4:8"]]
+ 00466c9c ["CALLIND", null, ["register:0:8"]]
- 00466c5c bytes 20013fd6
+ 00466c9c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e1e4e257a193cb15d834d9c9ea2e6c0"></a>

### [`00466ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ecc.md) → [`00466f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f0c.md) FUN_00466f0c

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
      "definition_site": "00466f20",
      "incomplete_value": false,
      "site": "00466f24",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466ee0",
      "incomplete_value": false,
      "site": "00466ee4",
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
            "const:898:8"
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
      "00466f24",
      "DATA",
      [
        "storage",
        "00c64898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466f24",
      "DATA",
      [
        "storage",
        "00c64c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ecc.md#insn-00466ed8) · [`00466ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ecc.md#insn-00466ee0)
- 新版 `00466f18`（命令位置の公開資料なし） · `00466f20`（命令位置の公開資料なし）

~~~diff
- 00466ed8 ["INT_ADD", "register:40f0:8", ["const:466ed8:8", "const:4:8"]]
- 00466ed8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00466f18 ["INT_ADD", "register:40f0:8", ["const:466f18:8", "const:4:8"]]
+ 00466f18 ["CALL", null, ["callee:00c57e90:8"]]
- 00466ed8 bytes eec21f94
+ 00466f18 bytes dec31f94
- 00466ee0 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00466ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466f20 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00466f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466ee0 bytes 08612291
+ 00466f20 bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18f13f97d097e78efbae1edf9baa3c0c"></a>

### [`00466ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ef0.md) → [`00466f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f30.md) FUN_00466f30

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
      "definition_site": "00466f34",
      "incomplete_value": false,
      "site": "00466f38",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466ef4",
      "incomplete_value": false,
      "site": "00466ef8",
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
            "const:898:8"
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
      "00466f38",
      "DATA",
      [
        "storage",
        "00c64898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466f38",
      "DATA",
      [
        "storage",
        "00c64c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466ef0.md#insn-00466ef4)
- 新版 `00466f34`（命令位置の公開資料なし）

~~~diff
- 00466ef4 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00466ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466f34 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00466f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466ef4 bytes 08612291
+ 00466f34 bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b7f77a1350ec15a4c93c74d9056e330"></a>

### [`00466f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466f08.md) → [`00466f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f48.md) FUN_00466f48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.63% / 新版 89.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00466ffc",
      "incomplete_value": true,
      "site": "00466ffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:723:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466fbc",
      "incomplete_value": true,
      "site": "00466fbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e3:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00466fa8",
      "incomplete_value": true,
      "site": "00466fac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466f68",
      "incomplete_value": true,
      "site": "00466f6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:870:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "00467064",
      "incomplete_value": true,
      "site": "00467064",
      "value": [
        "LOAD",
        "8",
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467024",
      "incomplete_value": true,
      "site": "00467024",
      "value": [
        "LOAD",
        "8",
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
                "const:80:8"
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
      "00466fa8",
      "READ",
      [
        "storage",
        "00c9a870",
        null,
        "pointer"
      ]
    ],
    [
      "00466fa8",
      "PARAM",
      [
        "storage",
        "01127100",
        "_ZNSt6__ndk14coutE",
        "undefined8"
      ]
    ],
    [
      "00466fec",
      "READ",
      [
        "storage",
        "002bd6e3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00466fa8",
      "READ",
      [
        "storage",
        "00c9ac70",
        null,
        "pointer"
      ]
    ],
    [
      "00466fa8",
      "PARAM",
      [
        "storage",
        "01127500",
        "_ZNSt6__ndk14coutE",
        "undefined8"
      ]
    ],
    [
      "00466fec",
      "READ",
      [
        "storage",
        "002bd723",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466f08.md#insn-00466f6c) · [`00466f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466f08.md#insn-00466f7c) · [`00466fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00466/00466f08.md#insn-00466fe4)
- 新版 `00466fac`（命令位置の公開資料なし） · `00466fbc`（命令位置の公開資料なし） · `00467024`（命令位置の公開資料なし）

~~~diff
- 00466f6c ["INT_ADD", "register:40f0:8", ["const:466f6c:8", "const:4:8"]]
- 00466f6c ["CALL", null, ["callee:004594d0:8"]]
+ 00466fac ["INT_ADD", "register:40f0:8", ["const:466fac:8", "const:4:8"]]
+ 00466fac ["CALL", null, ["callee:004594d0:8"]]
- 00466f6c bytes 49c9ff97
+ 00466fac bytes 49c9ff97
- 00466f7c ["INT_ADD", "register:40f0:8", ["const:466f7c:8", "const:4:8"]]
- 00466f7c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00466fbc ["INT_ADD", "register:40f0:8", ["const:466fbc:8", "const:4:8"]]
+ 00466fbc ["CALL", null, ["callee:00c57eb0:8"]]
- 00466f7c bytes cdc21f94
+ 00466fbc bytes bdc31f94
- 00466fe4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00466fe4 ["INT_ADD", "register:40f0:8", ["const:466fe4:8", "const:4:8"]]
- 00466fe4 ["CALLIND", null, ["register:0:8"]]
+ 00467024 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00467024 ["INT_ADD", "register:40f0:8", ["const:467024:8", "const:4:8"]]
+ 00467024 ["CALLIND", null, ["register:0:8"]]
- 00466fe4 bytes 00013fd6
+ 00467024 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96f946632723cc623d35ae39ec4da3c0"></a>

### [`00467218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467218.md) → [`00467258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467258.md) _INIT_11

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00467294",
      "incomplete_value": true,
      "site": "004672b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00467254",
      "incomplete_value": true,
      "site": "00467270",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "004672b8",
      "incomplete_value": true,
      "site": "004672d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00467278",
      "incomplete_value": true,
      "site": "00467294",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "004672d8",
      "incomplete_value": true,
      "site": "004672f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00467298",
      "incomplete_value": true,
      "site": "004672b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00467294",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "004672b8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "004672d8",
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
      "00467294",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "004672b8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "004672d8",
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

- 旧版 [`00467290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467218.md#insn-00467290) · [`004672b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467218.md#insn-004672b0) · [`00467378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467218.md#insn-00467378)
- 新版 `004672d0`（命令位置の公開資料なし） · `004672f0`（命令位置の公開資料なし） · `004673b8`（命令位置の公開資料なし）

~~~diff
- 00467290 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00467290 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00467290 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00467290 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004672d0 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 004672d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004672d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004672d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00467290 bytes 4a093691
+ 004672d0 bytes 4a093791
- 004672b0 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 004672b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004672b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004672b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004672f0 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 004672f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004672f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004672f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004672b0 bytes 4a553a91
+ 004672f0 bytes 4a893d91
- 00467378 ["INT_ADD", "register:40f0:8", ["const:467378:8", "const:4:8"]]
- 00467378 ["CALL", null, ["callee:0043b7f8:8"]]
+ 004673b8 ["INT_ADD", "register:40f0:8", ["const:4673b8:8", "const:4:8"]]
+ 004673b8 ["CALL", null, ["callee:0043b7f8:8"]]
- 00467378 bytes 1051ff97
+ 004673b8 bytes 1051ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fd13d9a2eaa8a1b63c4a7485171e6fd"></a>

### [`00467610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467610.md) → [`00467650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467650.md) FUN_00467650

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0046dde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dde4.md) [`005fc360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fc/005fc360.md) · 呼出先 0件 
- 新版 呼出元 2件 [`0046de24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046de24.md) [`005fc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fc/005fc3a0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046765c",
      "incomplete_value": true,
      "site": "00467668",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046761c",
      "incomplete_value": true,
      "site": "00467628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00467664",
      "incomplete_value": true,
      "site": "0046766c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467624",
      "incomplete_value": true,
      "site": "0046762c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
              ]
            ]
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
      "0046765c",
      "READ",
      [
        "storage",
        "002c3d58",
        null,
        "undefined8"
      ]
    ],
    [
      "00467664",
      "READ",
      [
        "storage",
        "002c3d60",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046765c",
      "READ",
      [
        "storage",
        "002c3d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00467664",
      "READ",
      [
        "storage",
        "002c3da0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467610.md#insn-0046761c) · [`00467620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467610.md#insn-00467620) · [`00467624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467610.md#insn-00467624)
- 新版 `0046765c`（命令位置の公開資料なし） · `00467664`（命令位置の公開資料なし）

~~~diff
- 0046761c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 0046761c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 0046761c ["COPY", "register:5008:8", ["const:0:8"]]
- 0046761c ["COPY", "register:5010:8", ["const:0:8"]]
+ 0046765c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
+ 0046765c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046765c ["COPY", "register:5008:8", ["const:0:8"]]
+ 0046765c ["COPY", "register:5010:8", ["const:0:8"]]
- 0046761c bytes 00ad46fd
+ 0046765c bytes 00cd46fd
- 00467620 ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 00467620 bytes e8f2ff90
- 00467624 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d60:8"]]
- 00467624 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
- 00467624 ["COPY", "register:5048:8", ["const:0:8"]]
- 00467624 ["COPY", "register:5050:8", ["const:0:8"]]
+ 00467664 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
+ 00467664 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00467664 ["COPY", "register:5048:8", ["const:0:8"]]
+ 00467664 ["COPY", "register:5050:8", ["const:0:8"]]
- 00467624 bytes 02b146fd
+ 00467664 bytes 02d146fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a661d60917ba8e847e21ba2121707bf"></a>

### [`0046763c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046763c.md) → [`0046767c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046767c.md) FUN_0046767c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00a46f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46f0c.md) [`00a4743c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a4743c.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00a47104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47104.md) [`00a47634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47634.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00467688",
      "incomplete_value": true,
      "site": "00467694",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467648",
      "incomplete_value": true,
      "site": "00467654",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
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
      "definition_site": "0046768c",
      "incomplete_value": true,
      "site": "00467698",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046764c",
      "incomplete_value": true,
      "site": "00467658",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
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
      "00467688",
      "READ",
      [
        "storage",
        "002c3d58",
        null,
        "undefined8"
      ]
    ],
    [
      "0046768c",
      "READ",
      [
        "storage",
        "002c3d60",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00467688",
      "READ",
      [
        "storage",
        "002c3d98",
        null,
        "undefined8"
      ]
    ],
    [
      "0046768c",
      "READ",
      [
        "storage",
        "002c3da0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00467648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046763c.md#insn-00467648) · [`0046764c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046763c.md#insn-0046764c)
- 新版 `00467688`（命令位置の公開資料なし） · `0046768c`（命令位置の公開資料なし）

~~~diff
- 00467648 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 00467648 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
- 00467648 ["COPY", "register:5048:8", ["const:0:8"]]
- 00467648 ["COPY", "register:5050:8", ["const:0:8"]]
+ 00467688 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
+ 00467688 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00467688 ["COPY", "register:5048:8", ["const:0:8"]]
+ 00467688 ["COPY", "register:5050:8", ["const:0:8"]]
- 00467648 bytes 02ad46fd
+ 00467688 bytes 02cd46fd
- 0046764c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d60:8"]]
- 0046764c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 0046764c ["COPY", "register:5008:8", ["const:0:8"]]
- 0046764c ["COPY", "register:5010:8", ["const:0:8"]]
+ 0046768c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:da0:8"]]
+ 0046768c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046768c ["COPY", "register:5008:8", ["const:0:8"]]
+ 0046768c ["COPY", "register:5010:8", ["const:0:8"]]
- 0046764c bytes 20b146fd
+ 0046768c bytes 20d146fd
~~~


<a id="compare-9a72b5047ec7cb9b9c6760ef8a2b2eb5"></a>

### [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) → [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) FUN_00467860

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 154件 [`005c4918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c4/005c4918.md) [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) [`005e03e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e03e4.md) [`005e4034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4034.md) [`005ed234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005ed234.md) · 呼出先 5件 [`004678b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004678b0.md) [`004678dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004678dc.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 154件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) [`005e0424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0424.md) [`005e4074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4074.md) [`005ed274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005ed274.md) · 呼出先 5件 [`004678f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004678f0.md) [`0046791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046791c.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 63.33% / 新版 63.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00467894",
      "incomplete_value": false,
      "site": "00467898",
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
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467854",
      "incomplete_value": false,
      "site": "00467858",
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
            "const:810:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004678a8",
      "value": [
        "leaf",
        "ram:4678f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00467868",
      "value": [
        "leaf",
        "ram:4678b0:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004678a4",
      "incomplete_value": false,
      "site": "004678a8",
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
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467864",
      "incomplete_value": false,
      "site": "00467868",
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
            "const:7a8:8"
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
      "00467874",
      "READ",
      [
        "storage",
        "00ca4810",
        null,
        "undefined1"
      ]
    ],
    [
      "00467880",
      "DATA",
      [
        "storage",
        "00ca47a8",
        null,
        null
      ]
    ],
    [
      "00467894",
      "PARAM",
      [
        "storage",
        "00ca4810",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00467874",
      "READ",
      [
        "storage",
        "00ca4c10",
        null,
        "undefined1"
      ]
    ],
    [
      "00467880",
      "DATA",
      [
        "storage",
        "00ca4ba8",
        null,
        null
      ]
    ],
    [
      "00467894",
      "PARAM",
      [
        "storage",
        "00ca4c10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00467858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md#insn-00467858) · [`00467868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md#insn-00467868) · [`00467884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md#insn-00467884)
- 新版 `00467898`（命令位置の公開資料なし） · `004678a8`（命令位置の公開資料なし） · `004678c4`（命令位置の公開資料なし）

~~~diff
- 00467858 ["INT_ADD", "register:40f0:8", ["const:467858:8", "const:4:8"]]
- 00467858 ["CALL", null, ["callee:00c57e50:8"]]
+ 00467898 ["INT_ADD", "register:40f0:8", ["const:467898:8", "const:4:8"]]
+ 00467898 ["CALL", null, ["callee:00c57e50:8"]]
- 00467858 bytes 7ec01f94
+ 00467898 bytes 6ec11f94
- 00467868 ["INT_ADD", "register:40f0:8", ["const:467868:8", "const:4:8"]]
- 00467868 ["CALL", null, ["ram:4678b0:8"]]
+ 004678a8 ["INT_ADD", "register:40f0:8", ["const:4678a8:8", "const:4:8"]]
+ 004678a8 ["CALL", null, ["ram:4678f0:8"]]
- 00467868 bytes 12000094
+ 004678a8 bytes 12000094
- 00467884 ["INT_ADD", "register:40f0:8", ["const:467884:8", "const:4:8"]]
- 00467884 ["CALL", null, ["callee:00c57e30:8"]]
+ 004678c4 ["INT_ADD", "register:40f0:8", ["const:4678c4:8", "const:4:8"]]
+ 004678c4 ["CALL", null, ["callee:00c57e30:8"]]
- 00467884 bytes 6bc01f94
+ 004678c4 bytes 5bc11f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84b2700174faf05ba40b8c728dbcabbe"></a>

### [`0046792c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md) → [`0046796c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046796c.md) FUN_0046796c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b2bdd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bdd8.md) · 呼出先 11件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0046ca14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca14.md) [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md) [`0055a5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5e4.md) [`0055a664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a664.md)
- 新版 呼出元 1件 [`00b2c200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md) · 呼出先 11件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0046ca54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca54.md) [`0046cb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md) [`0055a624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a624.md) [`0055a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6a4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.96% / 新版 92.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00467a24",
      "incomplete_value": true,
      "site": "00467a2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004679e4",
      "incomplete_value": true,
      "site": "004679ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8d0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004679c0",
      "incomplete_value": false,
      "site": "004679c4",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467980",
      "incomplete_value": false,
      "site": "00467984",
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
            "const:870:8"
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
      "definition_site": "004679e4",
      "incomplete_value": false,
      "site": "004679e8",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004679a4",
      "incomplete_value": false,
      "site": "004679a8",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004679c0",
      "PARAM",
      [
        "storage",
        "00ca4870",
        null,
        "undefined8"
      ]
    ],
    [
      "004679e4",
      "PARAM",
      [
        "storage",
        "00ca4870",
        null,
        "undefined8"
      ]
    ],
    [
      "00467a08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a664"
      ]
    ]
  ],
  "added": [
    [
      "004679c0",
      "PARAM",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ],
    [
      "004679e4",
      "PARAM",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ],
    [
      "00467a08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a6a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00467984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md#insn-00467984) · [`004679a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md#insn-004679a8) · [`004679c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md#insn-004679c4)
- 新版 `004679c4`（命令位置の公開資料なし） · `004679e8`（命令位置の公開資料なし） · `00467a04`（命令位置の公開資料なし）

~~~diff
- 00467984 ["INT_ADD", "register:40f0:8", ["const:467984:8", "const:4:8"]]
- 00467984 ["CALL", null, ["callee:0046ca54:8"]]
+ 004679c4 ["INT_ADD", "register:40f0:8", ["const:4679c4:8", "const:4:8"]]
+ 004679c4 ["CALL", null, ["callee:0046ca54:8"]]
- 00467984 bytes 24140094
+ 004679c4 bytes 24140094
- 004679a8 ["INT_ADD", "register:40f0:8", ["const:4679a8:8", "const:4:8"]]
- 004679a8 ["CALL", null, ["callee:0046cb0c:8"]]
+ 004679e8 ["INT_ADD", "register:40f0:8", ["const:4679e8:8", "const:4:8"]]
+ 004679e8 ["CALL", null, ["callee:0046cb0c:8"]]
- 004679a8 bytes 49140094
+ 004679e8 bytes 49140094
- 004679c4 ["INT_ADD", "register:40f0:8", ["const:4679c4:8", "const:4:8"]]
- 004679c4 ["CALL", null, ["callee:00467dbc:8"]]
+ 00467a04 ["INT_ADD", "register:40f0:8", ["const:467a04:8", "const:4:8"]]
+ 00467a04 ["CALL", null, ["callee:00467dbc:8"]]
- 004679c4 bytes ee000094
+ 00467a04 bytes ee000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70c0bcede0ac220bd9c4229a5cc5a0bf"></a>

### [`00467a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md) → [`00467a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md) FUN_00467a88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 11件 [`005f466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f4/005f466c.md) [`005f4d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f4/005f4d2c.md) [`0065cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md) [`0065d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065d5f0.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 4件 [`0046ca14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca14.md) [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0085ad18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085a/0085ad18.md)
- 新版 呼出元 11件 [`005f46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f46ac.md) [`005f4d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f4d6c.md) [`0065cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065c/0065cccc.md) [`0065d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065d/0065d630.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 4件 [`0046ca54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca54.md) [`0046cb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085ad58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085a/0085ad58.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00467aa4",
      "incomplete_value": true,
      "site": "00467aac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467a64",
      "incomplete_value": true,
      "site": "00467a6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:768:8"
              ]
            ]
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
      "definition_site": "00467ac4",
      "incomplete_value": false,
      "site": "00467ac8",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467a84",
      "incomplete_value": false,
      "site": "00467a88",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00467aa4",
      "READ",
      [
        "storage",
        "00c9a768",
        null,
        "pointer"
      ]
    ],
    [
      "00467aa4",
      "PARAM",
      [
        "storage",
        "00ca4870",
        null,
        "undefined8"
      ]
    ],
    [
      "00467ac4",
      "PARAM",
      [
        "storage",
        "00ca4870",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00467aa4",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      "00467aa4",
      "PARAM",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ],
    [
      "00467ac4",
      "PARAM",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00467a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md#insn-00467a6c) · [`00467a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md#insn-00467a88) · [`00467a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md#insn-00467a64)
- 新版 `00467aac`（命令位置の公開資料なし） · `00467ac8`（命令位置の公開資料なし） · `00467aa4`（命令位置の公開資料なし）

~~~diff
- 00467a6c ["INT_ADD", "register:40f0:8", ["const:467a6c:8", "const:4:8"]]
- 00467a6c ["CALL", null, ["callee:0046ca54:8"]]
+ 00467aac ["INT_ADD", "register:40f0:8", ["const:467aac:8", "const:4:8"]]
+ 00467aac ["CALL", null, ["callee:0046ca54:8"]]
- 00467a6c bytes ea130094
+ 00467aac bytes ea130094
- 00467a88 ["INT_ADD", "register:40f0:8", ["const:467a88:8", "const:4:8"]]
- 00467a88 ["CALL", null, ["callee:0046cb0c:8"]]
+ 00467ac8 ["INT_ADD", "register:40f0:8", ["const:467ac8:8", "const:4:8"]]
+ 00467ac8 ["CALL", null, ["callee:0046cb0c:8"]]
- 00467a88 bytes 11140094
+ 00467ac8 bytes 11140094
- 00467a64 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:768:8"]]
- 00467a64 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00467aa4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b68:8"]]
+ 00467aa4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00467a64 bytes 00b443f9
+ 00467aa4 bytes 00b445f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c32ef915502bcf72a4168d0a756ce647"></a>

### [`00467abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md) → [`00467afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467afc.md) FUN_00467afc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`006bf84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bf/006bf84c.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 3件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0055a664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a664.md) [`0055a668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a668.md)
- 新版 呼出元 4件 [`006bf88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bf/006bf88c.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 3件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0055a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6a4.md) [`0055a6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6a8.md)

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
      "site": "00467b14",
      "value": [
        "leaf",
        "ram:55a6a4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00467ad4",
      "value": [
        "leaf",
        "ram:55a664:8"
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
      "00467b14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a664"
      ]
    ]
  ],
  "added": [
    [
      "00467b14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a6a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00467ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md#insn-00467ad4) · [`00467ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md#insn-00467ad0)
- 新版 `00467b14`（命令位置の公開資料なし） · `00467b10`（命令位置の公開資料なし）

~~~diff
- 00467ad4 ["INT_ADD", "register:40f0:8", ["const:467ad4:8", "const:4:8"]]
- 00467ad4 ["CALL", null, ["ram:55a664:8"]]
+ 00467b14 ["INT_ADD", "register:40f0:8", ["const:467b14:8", "const:4:8"]]
+ 00467b14 ["CALL", null, ["ram:55a6a4:8"]]
- 00467ad4 bytes e4ca0394
+ 00467b14 bytes e4ca0394
- 00467ad0 ["INT_ADD", "register:40f0:8", ["const:467ad0:8", "const:4:8"]]
- 00467ad0 ["CALL", null, ["callee:00467dbc:8"]]
+ 00467b10 ["INT_ADD", "register:40f0:8", ["const:467b10:8", "const:4:8"]]
+ 00467b10 ["CALL", null, ["callee:00467dbc:8"]]
- 00467ad0 bytes ab000094
+ 00467b10 bytes ab000094
~~~


<a id="compare-7dfa177997d13db856a5c4bfbd826755"></a>

### [`00467e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e6c.md) → [`00467eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467eac.md) FUN_00467eac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005ed234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005ed234.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) · 呼出先 5件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`0055a664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a664.md) [`0055a668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a668.md) [`0055a66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a66c.md) [`0055a670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a670.md)
- 新版 呼出元 3件 [`005ed274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005ed274.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) · 呼出先 5件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0055a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6a4.md) [`0055a6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6a8.md) [`0055a6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6ac.md) [`0055a6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6b0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

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
      "site": "00467ecc",
      "value": [
        "leaf",
        "ram:55a6a4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00467e8c",
      "value": [
        "leaf",
        "ram:55a664:8"
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
      "00467ecc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a664"
      ]
    ]
  ],
  "added": [
    [
      "00467ecc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a6a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00467e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e6c.md#insn-00467e8c) · [`00467e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e6c.md#insn-00467e88) · [`00467e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e6c.md#insn-00467e98)
- 新版 `00467ecc`（命令位置の公開資料なし） · `00467ec8`（命令位置の公開資料なし） · `00467ed8`（命令位置の公開資料なし）

~~~diff
- 00467e8c ["INT_ADD", "register:40f0:8", ["const:467e8c:8", "const:4:8"]]
- 00467e8c ["CALL", null, ["ram:55a664:8"]]
+ 00467ecc ["INT_ADD", "register:40f0:8", ["const:467ecc:8", "const:4:8"]]
+ 00467ecc ["CALL", null, ["ram:55a6a4:8"]]
- 00467e8c bytes f6c90394
+ 00467ecc bytes f6c90394
- 00467e88 ["INT_ADD", "register:40f0:8", ["const:467e88:8", "const:4:8"]]
- 00467e88 ["CALL", null, ["callee:00467dbc:8"]]
+ 00467ec8 ["INT_ADD", "register:40f0:8", ["const:467ec8:8", "const:4:8"]]
+ 00467ec8 ["CALL", null, ["callee:00467dbc:8"]]
- 00467e88 bytes bdffff97
+ 00467ec8 bytes bdffff97
- 00467e98 ["INT_ADD", "register:40f0:8", ["const:467e98:8", "const:4:8"]]
- 00467e98 ["CALL", null, ["callee:0055a6a8:8"]]
+ 00467ed8 ["INT_ADD", "register:40f0:8", ["const:467ed8:8", "const:4:8"]]
+ 00467ed8 ["CALL", null, ["callee:0055a6a8:8"]]
- 00467e98 bytes f4c90394
+ 00467ed8 bytes f4c90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c6cb1d7800bd23af2abb171251fa929"></a>

### [`00468180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md) → [`004681c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004681c0.md) FUN_004681c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`005ed234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005ed234.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) [`006b6184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b6/006b6184.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`00925834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00925/00925834.md) · 呼出先 12件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`004684a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684a8.md) [`004684c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684c0.md) [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md)
- 新版 呼出元 5件 [`005ed274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005ed274.md) [`005ef5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005ef5ac.md) [`006b61c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b6/006b61c4.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`009259d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00925/009259d0.md) · 呼出先 12件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`004684e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004684e8.md) [`00468500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468500.md) [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.60% / 新版 89.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 4件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046827c",
      "incomplete_value": true,
      "site": "0046827c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046823c",
      "incomplete_value": true,
      "site": "0046823c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00468374",
      "incomplete_value": false,
      "site": "00468374",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00468334",
      "incomplete_value": false,
      "site": "00468334",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00468374",
      "incomplete_value": false,
      "site": "00468374",
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
                "const:c18:8"
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
      "definition_site": "00468334",
      "incomplete_value": false,
      "site": "00468334",
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
                "const:818:8"
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
    "ordinal": 36,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004681fc",
      "READ",
      [
        "storage",
        "00ca4830",
        null,
        "undefined1"
      ]
    ],
    [
      "00468218",
      "READ",
      [
        "storage",
        "00ca4818",
        null,
        "undefined8"
      ]
    ],
    [
      "00468220",
      "WRITE",
      [
        "storage",
        "00ca4820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004681fc",
      "READ",
      [
        "storage",
        "00ca4c30",
        null,
        "undefined1"
      ]
    ],
    [
      "00468218",
      "READ",
      [
        "storage",
        "00ca4c18",
        null,
        "undefined8"
      ]
    ],
    [
      "00468220",
      "WRITE",
      [
        "storage",
        "00ca4c20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046823c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md#insn-0046823c) · [`00468374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md#insn-00468374) · [`00468394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md#insn-00468394)
- 新版 `0046827c`（命令位置の公開資料なし） · `004683b4`（命令位置の公開資料なし） · `004683d4`（命令位置の公開資料なし）

~~~diff
- 0046823c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:820:8"]]
- 0046823c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
+ 0046827c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:c20:8"]]
+ 0046827c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 0046823c bytes 5c1104f9
+ 0046827c bytes 5c1106f9
- 00468374 ["COPY", "tmp:0:8", ["const:838:8"]]
- 00468374 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00468374 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00468374 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 004683b4 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 004683b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 004683b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 004683b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00468374 bytes 73e22091
+ 004683b4 bytes 73e23091
- 00468394 ["INT_ADD", "register:40f0:8", ["const:468394:8", "const:4:8"]]
- 00468394 ["CALL", null, ["callee:00468500:8"]]
+ 004683d4 ["INT_ADD", "register:40f0:8", ["const:4683d4:8", "const:4:8"]]
+ 004683d4 ["CALL", null, ["callee:00468500:8"]]
- 00468394 bytes 4b000094
+ 004683d4 bytes 4b000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfd87b3a5e1a0d1c75ba9bb928eb74ca"></a>

### [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) → [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) FUN_0046c44c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`00468180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468180.md) [`004684c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684c0.md) [`00555438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md) [`00555dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md) [`00559bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559bd0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 10件 [`004681c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004681c0.md) [`00468500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468500.md) [`00555478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555478.md) [`00555e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555e0c.md) [`00559c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559c10.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0046c458",
      "incomplete_value": false,
      "site": "0046c45c",
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
      "definition_site": "0046c418",
      "incomplete_value": false,
      "site": "0046c41c",
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
      "0046c458",
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
      "0046c458",
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

- 旧版 [`0046c41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md#insn-0046c41c) · [`0046c418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md#insn-0046c418)
- 新版 `0046c45c`（命令位置の公開資料なし） · `0046c458`（命令位置の公開資料なし）

~~~diff
- 0046c41c ["INT_ADD", "register:40f0:8", ["const:46c41c:8", "const:4:8"]]
- 0046c41c ["CALL", null, ["callee:0043b778:8"]]
+ 0046c45c ["INT_ADD", "register:40f0:8", ["const:46c45c:8", "const:4:8"]]
+ 0046c45c ["CALL", null, ["callee:0043b778:8"]]
- 0046c41c bytes c73cff97
+ 0046c45c bytes c73cff97
- 0046c418 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0046c418 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046c418 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046c418 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046c458 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0046c458 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c458 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c458 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046c418 bytes 00303c91
+ 0046c458 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-def2ace4c87fa421e33a4db7979c9446"></a>

### [`0046c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md) → [`0046c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c460.md) FUN_0046c460

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`00467fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md) [`00559924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md) [`005de640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005de640.md) [`00812e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00812/00812e8c.md) [`00813e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00813/00813e10.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 7件 [`00467ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md) [`00559964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559964.md) [`005de680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005de/005de680.md) [`00812ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00812/00812ecc.md) [`00813e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813e50.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0046c46c",
      "incomplete_value": false,
      "site": "0046c470",
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
      "definition_site": "0046c42c",
      "incomplete_value": false,
      "site": "0046c430",
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
      "0046c46c",
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
      "0046c46c",
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

- 旧版 [`0046c430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md#insn-0046c430) · [`0046c42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md#insn-0046c42c)
- 新版 `0046c470`（命令位置の公開資料なし） · `0046c46c`（命令位置の公開資料なし）

~~~diff
- 0046c430 ["INT_ADD", "register:40f0:8", ["const:46c430:8", "const:4:8"]]
- 0046c430 ["CALL", null, ["callee:0043b778:8"]]
+ 0046c470 ["INT_ADD", "register:40f0:8", ["const:46c470:8", "const:4:8"]]
+ 0046c470 ["CALL", null, ["callee:0043b778:8"]]
- 0046c430 bytes c23cff97
+ 0046c470 bytes c23cff97
- 0046c42c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0046c42c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046c42c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046c42c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046c46c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0046c46c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c46c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c46c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046c42c bytes 00303c91
+ 0046c46c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6e4e2e7d1116ec95d5ff5c67dbf5f42"></a>

### [`0046c5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5d4.md) → [`0046c614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c614.md) FUN_0046c614

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0046c434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c434.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0046c474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c474.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0046c620",
      "incomplete_value": false,
      "site": "0046c624",
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
      "definition_site": "0046c5e0",
      "incomplete_value": false,
      "site": "0046c5e4",
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
      "0046c620",
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
      "0046c620",
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

- 旧版 [`0046c5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5d4.md#insn-0046c5e4) · [`0046c5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5d4.md#insn-0046c5e0)
- 新版 `0046c624`（命令位置の公開資料なし） · `0046c620`（命令位置の公開資料なし）

~~~diff
- 0046c5e4 ["INT_ADD", "register:40f0:8", ["const:46c5e4:8", "const:4:8"]]
- 0046c5e4 ["CALL", null, ["callee:0043b778:8"]]
+ 0046c624 ["INT_ADD", "register:40f0:8", ["const:46c624:8", "const:4:8"]]
+ 0046c624 ["CALL", null, ["callee:0043b778:8"]]
- 0046c5e4 bytes 553cff97
+ 0046c624 bytes 553cff97
- 0046c5e0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0046c5e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046c5e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046c5e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046c620 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0046c620 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c620 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c620 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046c5e0 bytes 00303c91
+ 0046c620 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-062b44af48ed229570d2c266279247d5"></a>

### [`0046c5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5e8.md) → [`0046c628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c628.md) _INIT_12

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046c664",
      "incomplete_value": true,
      "site": "0046c680",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0046c624",
      "incomplete_value": true,
      "site": "0046c640",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "0046c688",
      "incomplete_value": true,
      "site": "0046c6a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0046c648",
      "incomplete_value": true,
      "site": "0046c664",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "0046c6a8",
      "incomplete_value": true,
      "site": "0046c6c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0046c668",
      "incomplete_value": true,
      "site": "0046c684",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046c664",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0046c688",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0046c6a8",
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
      "0046c664",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0046c688",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0046c6a8",
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

- 旧版 [`0046c660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5e8.md#insn-0046c660) · [`0046c680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5e8.md#insn-0046c680) · [`0046c748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c5e8.md#insn-0046c748)
- 新版 `0046c6a0`（命令位置の公開資料なし） · `0046c6c0`（命令位置の公開資料なし） · `0046c788`（命令位置の公開資料なし）

~~~diff
- 0046c660 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0046c660 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046c660 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046c660 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046c6a0 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0046c6a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046c6a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046c6a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046c660 bytes 4a093691
+ 0046c6a0 bytes 4a093791
- 0046c680 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0046c680 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046c680 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046c680 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046c6c0 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0046c6c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046c6c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046c6c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046c680 bytes 4a553a91
+ 0046c6c0 bytes 4a893d91
- 0046c748 ["INT_ADD", "register:40f0:8", ["const:46c748:8", "const:4:8"]]
- 0046c748 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0046c788 ["INT_ADD", "register:40f0:8", ["const:46c788:8", "const:4:8"]]
+ 0046c788 ["CALL", null, ["callee:0043b7f8:8"]]
- 0046c748 bytes 1c3cff97
+ 0046c788 bytes 1c3cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e88a17a2461dab20511d4ab9b2c4f19"></a>

### [`0046ca64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca64.md) → [`0046caa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046caa4.md) FUN_0046caa4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2b7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b2bbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bbcc.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046caac",
      "incomplete_value": false,
      "site": "0046caac",
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
            "const:cb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046ca6c",
      "incomplete_value": false,
      "site": "0046ca6c",
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
            "const:8b4:8"
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
      "0046caac",
      "WRITE",
      [
        "storage",
        "00ca48b4",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046caac",
      "WRITE",
      [
        "storage",
        "00ca4cb4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046ca6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca64.md#insn-0046ca6c)
- 新版 `0046caac`（命令位置の公開資料なし）

~~~diff
- 0046ca6c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0046ca6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:8b4:8"]]
- 0046ca6c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0046caac ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0046caac ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:cb4:8"]]
+ 0046caac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0046ca6c bytes 09d12239
+ 0046caac bytes 09d13239
~~~


<a id="compare-f22be43dc71e1ab7d80d07955a4e7876"></a>

### [`0046cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md) → [`0046cb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md) FUN_0046cb0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 26件 [`0046792c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md) [`00467a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md) [`00490af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00490/00490af4.md) [`004920e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md) [`0049252c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049252c.md) · 呼出先 0件 
- 新版 呼出元 26件 [`0046796c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046796c.md) [`00467a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md) [`00490b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490b34.md) [`00492120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492120.md) [`0049256c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/0049256c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0046cb4c",
      "incomplete_value": true,
      "site": "0046cb50",
      "value": [
        "TRUNC",
        "4",
        [
          [
            "FLOAT_DIV",
            "4",
            [
              "FLOAT_MULT",
              "INT2FLOAT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046cb0c",
      "incomplete_value": true,
      "site": "0046cb10",
      "value": [
        "TRUNC",
        "4",
        [
          [
            "FLOAT_DIV",
            "4",
            [
              "FLOAT_MULT",
              "INT2FLOAT"
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
      "0046cb30",
      "READ",
      [
        "storage",
        "00ca48a4",
        null,
        "undefined4"
      ]
    ],
    [
      "0046cb34",
      "READ",
      [
        "storage",
        "00ca4878",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0046cb30",
      "READ",
      [
        "storage",
        "00ca4ca4",
        null,
        "undefined4"
      ]
    ],
    [
      "0046cb34",
      "READ",
      [
        "storage",
        "00ca4c78",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046cae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cacc.md#insn-0046cae8)
- 新版 `0046cb28`（命令位置の公開資料なし）

~~~diff
- 0046cae8 ["COPY", "tmp:0:8", ["const:878:8"]]
- 0046cae8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046cae8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046cae8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046cb28 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 0046cb28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046cb28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046cb28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046cae8 bytes 08e12191
+ 0046cb28 bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75bb0bce0f355234d78a4dc211fb39db"></a>

### [`0046cbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cbdc.md) → [`0046cc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cc1c.md) FUN_0046cc1c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005f6c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f6/005f6c14.md) [`005f70f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f7/005f70f0.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) [`00a4f100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f100.md) · 呼出先 0件 
- 新版 呼出元 5件 [`005f6c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f6/005f6c54.md) [`005f7130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f7/005f7130.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) [`00a4f2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f2f8.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 59.09% / 新版 59.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0046cc64",
      "incomplete_value": true,
      "site": "0046cc68",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_SUB",
            "4",
            [
              [
                "live",
                "register:4048:4"
              ],
              "TRUNC"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046cc24",
      "incomplete_value": true,
      "site": "0046cc28",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_SUB",
            "4",
            [
              [
                "live",
                "register:4048:4"
              ],
              "TRUNC"
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
      "0046cc40",
      "READ",
      [
        "storage",
        "00ca48a8",
        null,
        null
      ]
    ],
    [
      "0046cc44",
      "READ",
      [
        "storage",
        "00ca487c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0046cc40",
      "READ",
      [
        "storage",
        "00ca4ca8",
        null,
        "undefined4"
      ]
    ],
    [
      "0046cc44",
      "READ",
      [
        "storage",
        "00ca4c7c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046cbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046cbdc.md#insn-0046cbf8)
- 新版 `0046cc38`（命令位置の公開資料なし）

~~~diff
- 0046cbf8 ["COPY", "tmp:0:8", ["const:87c:8"]]
- 0046cbf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046cbf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046cbf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046cc38 ["COPY", "tmp:0:8", ["const:c7c:8"]]
+ 0046cc38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046cc38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046cc38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046cbf8 bytes 08f12191
+ 0046cc38 bytes 08f13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3e8c8681902069730e29fc05f6f7ba9"></a>

### [`0046ccb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ccb4.md) → [`0046ccf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ccf4.md) _INIT_13

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 80.54% / 新版 80.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 8件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046cd30",
      "incomplete_value": true,
      "site": "0046cd4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0046ccf0",
      "incomplete_value": true,
      "site": "0046cd0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "0046cd54",
      "incomplete_value": true,
      "site": "0046cd70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0046cd14",
      "incomplete_value": true,
      "site": "0046cd30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "0046cd74",
      "incomplete_value": true,
      "site": "0046cd90",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0046cd34",
      "incomplete_value": true,
      "site": "0046cd50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046cd30",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0046cd54",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0046cd74",
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
      "0046cd30",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0046cd54",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0046cd74",
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

- 旧版 [`0046cd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ccb4.md#insn-0046cd2c) · [`0046cd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ccb4.md#insn-0046cd4c) · [`0046ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ccb4.md#insn-0046ce14)
- 新版 `0046cd6c`（命令位置の公開資料なし） · `0046cd8c`（命令位置の公開資料なし） · `0046ce54`（命令位置の公開資料なし）

~~~diff
- 0046cd2c ["COPY", "tmp:0:8", ["const:d82:8"]]
- 0046cd2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046cd2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046cd2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046cd6c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0046cd6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046cd6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046cd6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046cd2c bytes 4a093691
+ 0046cd6c bytes 4a093791
- 0046cd4c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0046cd4c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046cd4c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046cd4c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046cd8c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0046cd8c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046cd8c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046cd8c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046cd4c bytes 4a553a91
+ 0046cd8c bytes 4a893d91
- 0046ce14 ["INT_ADD", "register:40f0:8", ["const:46ce14:8", "const:4:8"]]
- 0046ce14 ["CALL", null, ["callee:0043b7f8:8"]]
+ 0046ce54 ["INT_ADD", "register:40f0:8", ["const:46ce54:8", "const:4:8"]]
+ 0046ce54 ["CALL", null, ["callee:0043b7f8:8"]]
- 0046ce14 bytes 693aff97
+ 0046ce54 bytes 693aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77732f4654b8d32ad20ba746e97cb433"></a>

### [`0046d064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d064.md) → [`0046d0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d0a4.md) FUN_0046d0a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 4件 [`0046d0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0d8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 2件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 4件 [`0046d118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d118.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination, store_value

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `store_destination` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046d0f8",
      "incomplete_value": false,
      "site": "0046d0f8",
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
                "const:cb8:8"
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
      "definition_site": "0046d0b8",
      "incomplete_value": false,
      "site": "0046d0b8",
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
                "const:8b8:8"
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046d0fc",
      "incomplete_value": false,
      "site": "0046d0fc",
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
                "const:cb8:8"
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
      "definition_site": "0046d0bc",
      "incomplete_value": false,
      "site": "0046d0bc",
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
                "const:8b8:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046d100",
      "incomplete_value": false,
      "site": "0046d100",
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
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046d0c0",
      "incomplete_value": false,
      "site": "0046d0c0",
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
            "const:8b8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046d0b4",
      "READ",
      [
        "storage",
        "00ca48d0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046d0c0",
      "DATA",
      [
        "storage",
        "00ca48b8",
        null,
        "undefined8"
      ]
    ],
    [
      "0046d0d0",
      "PARAM",
      [
        "storage",
        "00ca48d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046d0b4",
      "READ",
      [
        "storage",
        "00ca4cd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046d0c0",
      "DATA",
      [
        "storage",
        "00ca4cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "0046d0d0",
      "PARAM",
      [
        "storage",
        "00ca4cd0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046d080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d064.md#insn-0046d080) · [`0046d090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d064.md#insn-0046d090) · [`0046d094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d064.md#insn-0046d094)
- 新版 `0046d0c0`（命令位置の公開資料なし） · `0046d0d0`（命令位置の公開資料なし） · `0046d0d4`（命令位置の公開資料なし）

~~~diff
- 0046d080 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 0046d080 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046d080 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046d080 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046d0c0 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 0046d0c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046d0c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046d0c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046d080 bytes 00e02291
+ 0046d0c0 bytes 00e03291
- 0046d090 ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 0046d090 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046d090 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046d090 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046d0d0 ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 0046d0d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046d0d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046d0d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046d090 bytes 00402391
+ 0046d0d0 bytes 00403391
- 0046d094 ["INT_ADD", "register:40f0:8", ["const:46d094:8", "const:4:8"]]
- 0046d094 ["CALL", null, ["callee:00c57e50:8"]]
+ 0046d0d4 ["INT_ADD", "register:40f0:8", ["const:46d0d4:8", "const:4:8"]]
+ 0046d0d4 ["CALL", null, ["callee:00c57e50:8"]]
- 0046d094 bytes 6faa1f94
+ 0046d0d4 bytes 5fab1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62f9bc767d2023a6abb403137bfa65de"></a>

### [`0046d0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md) → [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) FUN_0046d120

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 15件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 15件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.10% / 新版 89.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046d16c",
      "incomplete_value": false,
      "site": "0046d178",
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
      "definition_site": "0046d12c",
      "incomplete_value": false,
      "site": "0046d138",
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
      "definition_site": "0046d190",
      "incomplete_value": true,
      "site": "0046d190",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:37f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046d150",
      "incomplete_value": true,
      "site": "0046d150",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2a3:8"
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
      "definition_site": "0046d188",
      "incomplete_value": true,
      "site": "0046d194",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0046d148",
      "incomplete_value": true,
      "site": "0046d154",
      "value": [
        "LOAD",
        "8",
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
      "0046d178",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0046d180",
      "READ",
      [
        "storage",
        "002a52a3",
        null,
        "string"
      ]
    ],
    [
      "0046d188",
      "READ",
      [
        "storage",
        "002a52aa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0046d178",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0046d180",
      "READ",
      [
        "storage",
        "002a537f",
        null,
        "string"
      ]
    ],
    [
      "0046d188",
      "READ",
      [
        "storage",
        "002a5386",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046d110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md#insn-0046d110) · [`0046d194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md#insn-0046d194) · [`0046d274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d0e0.md#insn-0046d274)
- 新版 `0046d150`（命令位置の公開資料なし） · `0046d1d4`（命令位置の公開資料なし） · `0046d2b4`（命令位置の公開資料なし）

~~~diff
- 0046d110 ["INT_ADD", "register:40f0:8", ["const:46d110:8", "const:4:8"]]
- 0046d110 ["CALL", null, ["callee:0046d490:8"]]
+ 0046d150 ["INT_ADD", "register:40f0:8", ["const:46d150:8", "const:4:8"]]
+ 0046d150 ["CALL", null, ["callee:0046d490:8"]]
- 0046d110 bytes d0000094
+ 0046d150 bytes d0000094
- 0046d194 ["INT_ADD", "register:40f0:8", ["const:46d194:8", "const:4:8"]]
- 0046d194 ["CALL", null, ["callee:00488558:8"]]
+ 0046d1d4 ["INT_ADD", "register:40f0:8", ["const:46d1d4:8", "const:4:8"]]
+ 0046d1d4 ["CALL", null, ["callee:00488558:8"]]
- 0046d194 bytes e16c0094
+ 0046d1d4 bytes e16c0094
- 0046d274 ["INT_ADD", "register:40f0:8", ["const:46d274:8", "const:4:8"]]
- 0046d274 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0046d2b4 ["INT_ADD", "register:40f0:8", ["const:46d2b4:8", "const:4:8"]]
+ 0046d2b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0046d274 bytes 0faa1f94
+ 0046d2b4 bytes ffaa1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cff51bf8f5de981c8d32249166151c23"></a>

### [`0046d4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d4b0.md) → [`0046d4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d4f0.md) FUN_0046d4f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 73.91% / 新版 73.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046d520",
      "incomplete_value": true,
      "site": "0046d528",
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
      "definition_site": "0046d4e0",
      "incomplete_value": true,
      "site": "0046d4e8",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0046d52c",
      "incomplete_value": true,
      "site": "0046d52c",
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
      "definition_site": "0046d4ec",
      "incomplete_value": true,
      "site": "0046d4ec",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046d53c",
      "incomplete_value": true,
      "site": "0046d53c",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "definition_site": "0046d4fc",
      "incomplete_value": true,
      "site": "0046d4fc",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "0046d50c",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      "0046d510",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "0046d51c",
      "READ",
      [
        "storage",
        "00c92e00",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0046d50c",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "0046d510",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "0046d51c",
      "READ",
      [
        "storage",
        "00c93200",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046d528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d4b0.md#insn-0046d528) · [`0046d4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d4b0.md#insn-0046d4cc) · [`0046d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d4b0.md#insn-0046d4d0)
- 新版 `0046d568`（命令位置の公開資料なし） · `0046d50c`（命令位置の公開資料なし） · `0046d510`（命令位置の公開資料なし）

~~~diff
- 0046d528 ["INT_ADD", "register:40f0:8", ["const:46d528:8", "const:4:8"]]
- 0046d528 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0046d568 ["INT_ADD", "register:40f0:8", ["const:46d568:8", "const:4:8"]]
+ 0046d568 ["CALL", null, ["callee:00c57fb0:8"]]
- 0046d528 bytes a2a91f94
+ 0046d568 bytes 92aa1f94
- 0046d4cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7b0:8"]]
- 0046d4cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046d50c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
+ 0046d50c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0046d4cc bytes 08d943f9
+ 0046d50c bytes 08d945f9
- 0046d4d0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:7b8:8"]]
- 0046d4d0 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046d510 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:bb8:8"]]
+ 0046d510 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 0046d4d0 bytes d6de43f9
+ 0046d510 bytes d6de45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a649ed455f9dc3b7c30aa145a5273a7"></a>

### [`0046d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d780.md) → [`0046d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7c0.md) FUN_0046d7c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`009dbf88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbf88.md) [`009dbf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbf94.md) [`009dbfa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009db/009dbfa0.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 7件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)
- 新版 呼出元 5件 [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`009dc124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dc124.md) [`009dc130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dc130.md) [`009dc13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dc13c.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 7件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence

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
      "site": "0046d8ac",
      "value": [
        "leaf",
        "ram:46db00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0046d86c",
      "value": [
        "leaf",
        "ram:46dac0:8"
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
      "0046d818",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "0046d81c",
      "READ",
      [
        "storage",
        "002c4108",
        null,
        "undefined8"
      ]
    ],
    [
      "0046d8ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ],
  "added": [
    [
      "0046d818",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "0046d81c",
      "READ",
      [
        "storage",
        "002c4148",
        null,
        "undefined8"
      ]
    ],
    [
      "0046d8ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046db00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046d82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d780.md#insn-0046d82c) · [`0046d86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d780.md#insn-0046d86c) · [`0046d7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d780.md#insn-0046d7cc)
- 新版 `0046d86c`（命令位置の公開資料なし） · `0046d8ac`（命令位置の公開資料なし） · `0046d80c`（命令位置の公開資料なし）

~~~diff
- 0046d82c ["INT_ADD", "register:40f0:8", ["const:46d82c:8", "const:4:8"]]
- 0046d82c ["CALL", null, ["callee:00c583b0:8"]]
+ 0046d86c ["INT_ADD", "register:40f0:8", ["const:46d86c:8", "const:4:8"]]
+ 0046d86c ["CALL", null, ["callee:00c583b0:8"]]
- 0046d82c bytes e1a91f94
+ 0046d86c bytes d1aa1f94
- 0046d86c ["INT_ADD", "register:40f0:8", ["const:46d86c:8", "const:4:8"]]
- 0046d86c ["CALL", null, ["ram:46dac0:8"]]
+ 0046d8ac ["INT_ADD", "register:40f0:8", ["const:46d8ac:8", "const:4:8"]]
+ 0046d8ac ["CALL", null, ["ram:46db00:8"]]
- 0046d86c bytes 95000094
+ 0046d8ac bytes 95000094
- 0046d7cc ["COPY", "tmp:0:8", ["const:ddd:8"]]
- 0046d7cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046d7cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046d7cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046d80c ["COPY", "tmp:0:8", ["const:e1d:8"]]
+ 0046d80c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046d80c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046d80c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046d7cc bytes 08753791
+ 0046d80c bytes 08753891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f39b39308f739edac4d1eced4f76f828"></a>

### [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) → [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) FUN_0046e7c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 25件 [`005df690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df690.md) [`005e4f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4f34.md) [`00682424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682424.md) [`0078c1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078c/0078c1dc.md) [`007bbddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md) · 呼出先 1件 [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 25件 [`005df6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005df/005df6d0.md) [`005e4f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4f74.md) [`00682464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682464.md) [`0078c21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078c/0078c21c.md) [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) · 呼出先 1件 [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046e7f0",
      "incomplete_value": false,
      "site": "0046e7f8",
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
    "old": {
      "definition_site": "0046e7b0",
      "incomplete_value": false,
      "site": "0046e7b8",
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
            "const:30e:8"
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
      "0046e7f0",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046e7f0",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md#insn-0046e7b8) · [`0046e7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md#insn-0046e7b0)
- 新版 `0046e7f8`（命令位置の公開資料なし） · `0046e7f0`（命令位置の公開資料なし）

~~~diff
- 0046e7b8 ["INT_ADD", "register:40f0:8", ["const:46e7b8:8", "const:4:8"]]
- 0046e7b8 ["CALL", null, ["callee:00c58190:8"]]
+ 0046e7f8 ["INT_ADD", "register:40f0:8", ["const:46e7f8:8", "const:4:8"]]
+ 0046e7f8 ["CALL", null, ["callee:00c58190:8"]]
- 0046e7b8 bytes 76a51f94
+ 0046e7f8 bytes 66a61f94
- 0046e7b0 ["COPY", "tmp:0:8", ["const:30e:8"]]
- 0046e7b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0046e7b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0046e7b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046e7f0 ["COPY", "tmp:0:8", ["const:3ea:8"]]
+ 0046e7f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046e7f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046e7f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0046e7b0 bytes 21380c91
+ 0046e7f0 bytes 21a80f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14dd69a92ecf36a2c19379801c21ebec"></a>

### [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) → [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) FUN_0046e8a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 38件 [`005df738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df738.md) [`005e5078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e5/005e5078.md) [`006821d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006821d8.md) [`0078dd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dd8c.md) [`0078de14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078de14.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 38件 [`005df778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005df/005df778.md) [`005e50b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e5/005e50b8.md) [`00682218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682218.md) [`0078ddcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078ddcc.md) [`0078de54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078de54.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046e8ec",
      "incomplete_value": false,
      "site": "0046e8f4",
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
    "old": {
      "definition_site": "0046e8ac",
      "incomplete_value": false,
      "site": "0046e8b4",
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
            "const:30e:8"
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
      "0046e8ec",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046e8ec",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046e8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md#insn-0046e8b4) · [`0046e898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md#insn-0046e898) · [`0046e8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md#insn-0046e8ac)
- 新版 `0046e8f4`（命令位置の公開資料なし） · `0046e8d8`（命令位置の公開資料なし） · `0046e8ec`（命令位置の公開資料なし）

~~~diff
- 0046e8b4 ["INT_ADD", "register:40f0:8", ["const:46e8b4:8", "const:4:8"]]
- 0046e8b4 ["CALL", null, ["callee:00c58190:8"]]
+ 0046e8f4 ["INT_ADD", "register:40f0:8", ["const:46e8f4:8", "const:4:8"]]
+ 0046e8f4 ["CALL", null, ["callee:00c58190:8"]]
- 0046e8b4 bytes 37a51f94
+ 0046e8f4 bytes 27a61f94
- 0046e898 ["INT_ADD", "register:40f0:8", ["const:46e898:8", "const:4:8"]]
- 0046e898 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0046e8d8 ["INT_ADD", "register:40f0:8", ["const:46e8d8:8", "const:4:8"]]
+ 0046e8d8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0046e898 bytes 86a41f94
+ 0046e8d8 bytes 76a51f94
- 0046e8ac ["COPY", "tmp:0:8", ["const:30e:8"]]
- 0046e8ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0046e8ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0046e8ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046e8ec ["COPY", "tmp:0:8", ["const:3ea:8"]]
+ 0046e8ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046e8ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046e8ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0046e8ac bytes 21380c91
+ 0046e8ec bytes 21a80f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdc182aeb591e7a592f4f88c0cfc0601"></a>

### [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) → [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) FUN_0046e970

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 36件 [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md) [`0063a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a764.md) · 呼出先 15件 [`00470124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470124.md) [`00470328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470328.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 36件 [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) [`006312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00631/006312f4.md) [`0063a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a7a4.md) · 呼出先 15件 [`00470164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470164.md) [`00470368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470368.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.20% / 新版 95.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046e9b4",
      "incomplete_value": false,
      "site": "0046e9b8",
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
      "definition_site": "0046e974",
      "incomplete_value": false,
      "site": "0046e978",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046ecac",
      "incomplete_value": true,
      "site": "0046ecb0",
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
      "definition_site": "0046ec6c",
      "incomplete_value": true,
      "site": "0046ec70",
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
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046eca8",
      "incomplete_value": true,
      "site": "0046ecb4",
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
      "definition_site": "0046ec68",
      "incomplete_value": true,
      "site": "0046ec74",
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
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046e9b8",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0046e9d0",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "0046ec9c",
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
      "0046e9b8",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0046e9d0",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "0046ec9c",
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

- 旧版 [`0046e998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md#insn-0046e998) · [`0046e9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md#insn-0046e9b8) · [`0046e9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md#insn-0046e9d8)
- 新版 `0046e9d8`（命令位置の公開資料なし） · `0046e9f8`（命令位置の公開資料なし） · `0046ea18`（命令位置の公開資料なし）

~~~diff
- 0046e998 ["INT_ADD", "register:40f0:8", ["const:46e998:8", "const:4:8"]]
- 0046e998 ["CALL", null, ["callee:00c58190:8"]]
+ 0046e9d8 ["INT_ADD", "register:40f0:8", ["const:46e9d8:8", "const:4:8"]]
+ 0046e9d8 ["CALL", null, ["callee:00c58190:8"]]
- 0046e998 bytes fea41f94
+ 0046e9d8 bytes eea51f94
- 0046e9b8 ["INT_ADD", "register:40f0:8", ["const:46e9b8:8", "const:4:8"]]
- 0046e9b8 ["CALL", null, ["callee:00b110ec:8"]]
+ 0046e9f8 ["INT_ADD", "register:40f0:8", ["const:46e9f8:8", "const:4:8"]]
+ 0046e9f8 ["CALL", null, ["callee:00b110ec:8"]]
- 0046e9b8 bytes c3881a94
+ 0046e9f8 bytes bd891a94
- 0046e9d8 ["INT_ADD", "register:40f0:8", ["const:46e9d8:8", "const:4:8"]]
- 0046e9d8 ["CALL", null, ["callee:0048791c:8"]]
+ 0046ea18 ["INT_ADD", "register:40f0:8", ["const:46ea18:8", "const:4:8"]]
+ 0046ea18 ["CALL", null, ["callee:0048791c:8"]]
- 0046e9d8 bytes c1630094
+ 0046ea18 bytes c1630094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd19beba806aa2ed375e3c67a6b2440b"></a>

### [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md) → [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) FUN_0046eef8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 26件 [`005f0e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0e14.md) [`0067e370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e370.md) [`0070dfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070dfc4.md) [`0078c1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078c/0078c1dc.md) [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) · 呼出先 1件 [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 26件 [`005f0e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0e54.md) [`0067e3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e3b0.md) [`0070e004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e004.md) [`0078c21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078c/0078c21c.md) [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) · 呼出先 1件 [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046ef38",
      "incomplete_value": false,
      "site": "0046ef40",
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
    "old": {
      "definition_site": "0046eef8",
      "incomplete_value": false,
      "site": "0046ef00",
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
            "const:30e:8"
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
      "0046ef38",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046ef38",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046ef00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md#insn-0046ef00) · [`0046eef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md#insn-0046eef8)
- 新版 `0046ef40`（命令位置の公開資料なし） · `0046ef38`（命令位置の公開資料なし）

~~~diff
- 0046ef00 ["INT_ADD", "register:40f0:8", ["const:46ef00:8", "const:4:8"]]
- 0046ef00 ["CALL", null, ["callee:00c58190:8"]]
+ 0046ef40 ["INT_ADD", "register:40f0:8", ["const:46ef40:8", "const:4:8"]]
+ 0046ef40 ["CALL", null, ["callee:00c58190:8"]]
- 0046ef00 bytes a4a31f94
+ 0046ef40 bytes 94a41f94
- 0046eef8 ["COPY", "tmp:0:8", ["const:30e:8"]]
- 0046eef8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0046eef8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0046eef8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046ef38 ["COPY", "tmp:0:8", ["const:3ea:8"]]
+ 0046ef38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046ef38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046ef38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0046eef8 bytes 21380c91
+ 0046ef38 bytes 21a80f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46750839bdf35bffa5f5e1d1b5cdd4d4"></a>

### [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) → [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) FUN_0046efdc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 31件 [`005f0ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0ebc.md) [`0067e4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e4cc.md) [`00681fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00681/00681fb8.md) [`0070e108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e108.md) [`0078dd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dd8c.md) · 呼出先 4件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d90.md)
- 新版 呼出元 31件 [`005f0efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0efc.md) [`0067e50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e50c.md) [`00681ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00681/00681ff8.md) [`0070e148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e148.md) [`0078ddcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078ddcc.md) · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046f010",
      "incomplete_value": false,
      "site": "0046f018",
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
    "old": {
      "definition_site": "0046efd0",
      "incomplete_value": false,
      "site": "0046efd8",
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
            "const:30e:8"
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
      "0046f010",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046f010",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046efd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md#insn-0046efd8) · [`0046f018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md#insn-0046f018) · [`0046efd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md#insn-0046efd0)
- 新版 `0046f018`（命令位置の公開資料なし） · `0046f058`（命令位置の公開資料なし） · `0046f010`（命令位置の公開資料なし）

~~~diff
- 0046efd8 ["INT_ADD", "register:40f0:8", ["const:46efd8:8", "const:4:8"]]
- 0046efd8 ["CALL", null, ["callee:00c58190:8"]]
+ 0046f018 ["INT_ADD", "register:40f0:8", ["const:46f018:8", "const:4:8"]]
+ 0046f018 ["CALL", null, ["callee:00c58190:8"]]
- 0046efd8 bytes 6ea31f94
+ 0046f018 bytes 5ea41f94
- 0046f018 ["INT_ADD", "register:40f0:8", ["const:46f018:8", "const:4:8"]]
- 0046f018 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0046f058 ["INT_ADD", "register:40f0:8", ["const:46f058:8", "const:4:8"]]
+ 0046f058 ["CALL", null, ["callee:00c57eb0:8"]]
- 0046f018 bytes a6a21f94
+ 0046f058 bytes 96a31f94
- 0046efd0 ["COPY", "tmp:0:8", ["const:30e:8"]]
- 0046efd0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0046efd0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0046efd0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046f010 ["COPY", "tmp:0:8", ["const:3ea:8"]]
+ 0046f010 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046f010 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046f010 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0046efd0 bytes 21380c91
+ 0046f010 bytes 21a80f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4703cda24519287cc666637392a4b15e"></a>

### [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) → [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) FUN_0046f0b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 36件 [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) [`006312b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006312b4.md) [`0063a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a764.md) · 呼出先 16件 [`00470468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470468.md) [`004706d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706d4.md) [`00470814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470814.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)
- 新版 呼出元 36件 [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) [`006312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00631/006312f4.md) [`0063a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a7a4.md) · 呼出先 16件 [`004704a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004704a8.md) [`00470714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md) [`00470854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470854.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.60% / 新版 96.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046f0f4",
      "incomplete_value": false,
      "site": "0046f0fc",
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
      "definition_site": "0046f0b4",
      "incomplete_value": false,
      "site": "0046f0bc",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046f474",
      "incomplete_value": true,
      "site": "0046f480",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:3f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046f434",
      "incomplete_value": true,
      "site": "0046f440",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046f58c",
      "incomplete_value": true,
      "site": "0046f590",
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
      "definition_site": "0046f54c",
      "incomplete_value": true,
      "site": "0046f550",
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
      "0046f0fc",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0046f130",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "0046f474",
      "READ",
      [
        "storage",
        "002c43b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046f0fc",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0046f130",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "0046f474",
      "READ",
      [
        "storage",
        "002c43f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046f0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md#insn-0046f0f8) · [`0046f400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md#insn-0046f400) · [`0046f594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md#insn-0046f594)
- 新版 `0046f138`（命令位置の公開資料なし） · `0046f440`（命令位置の公開資料なし） · `0046f5d4`（命令位置の公開資料なし）

~~~diff
- 0046f0f8 ["INT_ADD", "register:40f0:8", ["const:46f0f8:8", "const:4:8"]]
- 0046f0f8 ["CALL", null, ["callee:00c58190:8"]]
+ 0046f138 ["INT_ADD", "register:40f0:8", ["const:46f138:8", "const:4:8"]]
+ 0046f138 ["CALL", null, ["callee:00c58190:8"]]
- 0046f0f8 bytes 26a31f94
+ 0046f138 bytes 16a41f94
- 0046f400 ["INT_ADD", "register:40f0:8", ["const:46f400:8", "const:4:8"]]
- 0046f400 ["CALL", null, ["callee:0048793c:8"]]
+ 0046f440 ["INT_ADD", "register:40f0:8", ["const:46f440:8", "const:4:8"]]
+ 0046f440 ["CALL", null, ["callee:0048793c:8"]]
- 0046f400 bytes 3f610094
+ 0046f440 bytes 3f610094
- 0046f594 ["INT_ADD", "register:40f0:8", ["const:46f594:8", "const:4:8"]]
- 0046f594 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0046f5d4 ["INT_ADD", "register:40f0:8", ["const:46f5d4:8", "const:4:8"]]
+ 0046f5d4 ["CALL", null, ["callee:00c57fb0:8"]]
- 0046f594 bytes 87a11f94
+ 0046f5d4 bytes 77a21f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a6c320dc852225ac1535242eda84244"></a>

### [`00470314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470314.md) → [`00470354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470354.md) FUN_00470354

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00470124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470124.md) [`007bbddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbddc.md) [`007f1a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1a78.md) [`008ff730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ff/008ff730.md) [`00a3f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3f/00a3f154.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 5件 [`00470164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470164.md) [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) [`007f1ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md) [`008ff8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff8cc.md) [`00a3f34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3f/00a3f34c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00470360",
      "incomplete_value": false,
      "site": "00470364",
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
      "definition_site": "00470320",
      "incomplete_value": false,
      "site": "00470324",
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
      "00470360",
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
      "00470360",
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

- 旧版 [`00470324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470314.md#insn-00470324) · [`00470320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470314.md#insn-00470320)
- 新版 `00470364`（命令位置の公開資料なし） · `00470360`（命令位置の公開資料なし）

~~~diff
- 00470324 ["INT_ADD", "register:40f0:8", ["const:470324:8", "const:4:8"]]
- 00470324 ["CALL", null, ["callee:0043b778:8"]]
+ 00470364 ["INT_ADD", "register:40f0:8", ["const:470364:8", "const:4:8"]]
+ 00470364 ["CALL", null, ["callee:0043b778:8"]]
- 00470324 bytes 052dff97
+ 00470364 bytes 052dff97
- 00470320 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00470320 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00470320 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00470320 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00470360 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00470360 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00470360 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00470360 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00470320 bytes 00303c91
+ 00470360 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6768453951d0992be2fa54fa1bfd8a45"></a>

### [`00470454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470454.md) → [`00470494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470494.md) FUN_00470494

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00470328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470328.md) [`007f1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1c70.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`00470368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470368.md) [`007f1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1cb0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "004704a0",
      "incomplete_value": false,
      "site": "004704a4",
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
      "definition_site": "00470460",
      "incomplete_value": false,
      "site": "00470464",
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
      "004704a0",
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
      "004704a0",
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

- 旧版 [`00470464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470454.md#insn-00470464) · [`00470460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470454.md#insn-00470460)
- 新版 `004704a4`（命令位置の公開資料なし） · `004704a0`（命令位置の公開資料なし）

~~~diff
- 00470464 ["INT_ADD", "register:40f0:8", ["const:470464:8", "const:4:8"]]
- 00470464 ["CALL", null, ["callee:0043b778:8"]]
+ 004704a4 ["INT_ADD", "register:40f0:8", ["const:4704a4:8", "const:4:8"]]
+ 004704a4 ["CALL", null, ["callee:0043b778:8"]]
- 00470464 bytes b52cff97
+ 004704a4 bytes b52cff97
- 00470460 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00470460 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00470460 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00470460 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004704a0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 004704a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004704a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004704a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00470460 bytes 00303c91
+ 004704a0 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-972b4ded989b29b98fb40e2336d5a6c3"></a>

### [`00470468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470468.md) → [`004704a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004704a8.md) FUN_004704a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004675a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004675a8.md) [`004706c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706c0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`004675e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004675e8.md) [`00470700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470700.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.55% / 新版 98.55%

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
      "site": "004705a4",
      "value": [
        "leaf",
        "ram:4675e8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00470564",
      "value": [
        "leaf",
        "ram:4675a8:8"
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
      "site": "0047062c",
      "value": [
        "leaf",
        "ram:4675e8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004705ec",
      "value": [
        "leaf",
        "ram:4675a8:8"
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
      "004705a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004675a8"
      ]
    ],
    [
      "0047062c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004675a8"
      ]
    ]
  ],
  "added": [
    [
      "004705a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004675e8"
      ]
    ],
    [
      "0047062c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004675e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00470564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470468.md#insn-00470564) · [`004705ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470468.md#insn-004705ec) · [`00470520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470468.md#insn-00470520)
- 新版 `004705a4`（命令位置の公開資料なし） · `0047062c`（命令位置の公開資料なし） · `00470560`（命令位置の公開資料なし）

~~~diff
- 00470564 ["INT_ADD", "register:40f0:8", ["const:470564:8", "const:4:8"]]
- 00470564 ["CALL", null, ["ram:4675a8:8"]]
+ 004705a4 ["INT_ADD", "register:40f0:8", ["const:4705a4:8", "const:4:8"]]
+ 004705a4 ["CALL", null, ["ram:4675e8:8"]]
- 00470564 bytes 11dcff97
+ 004705a4 bytes 11dcff97
- 004705ec ["INT_ADD", "register:40f0:8", ["const:4705ec:8", "const:4:8"]]
- 004705ec ["CALL", null, ["ram:4675a8:8"]]
+ 0047062c ["INT_ADD", "register:40f0:8", ["const:47062c:8", "const:4:8"]]
+ 0047062c ["CALL", null, ["ram:4675e8:8"]]
- 004705ec bytes efdbff97
+ 0047062c bytes efdbff97
- 00470520 ["INT_ADD", "register:40f0:8", ["const:470520:8", "const:4:8"]]
- 00470520 ["CALL", null, ["callee:00c57e90:8"]]
+ 00470560 ["INT_ADD", "register:40f0:8", ["const:470560:8", "const:4:8"]]
+ 00470560 ["CALL", null, ["callee:00c57e90:8"]]
- 00470520 bytes 5c9d1f94
+ 00470560 bytes 4c9e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5878251ad185b2a1f5fe2e5c58f8a8b3"></a>

### [`004706c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706c0.md) → [`00470700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470700.md) FUN_00470700

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00470468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470468.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`004704a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004704a8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0047070c",
      "incomplete_value": false,
      "site": "00470710",
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
      "definition_site": "004706cc",
      "incomplete_value": false,
      "site": "004706d0",
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
      "0047070c",
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
      "0047070c",
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

- 旧版 [`004706d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706c0.md#insn-004706d0) · [`004706cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706c0.md#insn-004706cc)
- 新版 `00470710`（命令位置の公開資料なし） · `0047070c`（命令位置の公開資料なし）

~~~diff
- 004706d0 ["INT_ADD", "register:40f0:8", ["const:4706d0:8", "const:4:8"]]
- 004706d0 ["CALL", null, ["callee:0043b778:8"]]
+ 00470710 ["INT_ADD", "register:40f0:8", ["const:470710:8", "const:4:8"]]
+ 00470710 ["CALL", null, ["callee:0043b778:8"]]
- 004706d0 bytes 1a2cff97
+ 00470710 bytes 1a2cff97
- 004706cc ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 004706cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004706cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004706cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047070c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0047070c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047070c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047070c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004706cc bytes 00303c91
+ 0047070c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b212e690084b4ec9b71b11ef0e6b18b"></a>

### [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) → [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) FUN_00470840

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 261件 [`0046f71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f71c.md) [`004706d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004706d4.md) [`00470954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`0047aed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047aed0.md) [`0049e484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049e/0049e484.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 262件 [`0046f75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f75c.md) [`00470714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md) [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) [`0049e4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e4c4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0047084c",
      "incomplete_value": false,
      "site": "00470850",
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
      "definition_site": "0047080c",
      "incomplete_value": false,
      "site": "00470810",
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
      "0047084c",
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
      "0047084c",
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

- 旧版 [`00470810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md#insn-00470810) · [`0047080c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md#insn-0047080c)
- 新版 `00470850`（命令位置の公開資料なし） · `0047084c`（命令位置の公開資料なし）

~~~diff
- 00470810 ["INT_ADD", "register:40f0:8", ["const:470810:8", "const:4:8"]]
- 00470810 ["CALL", null, ["callee:0043b778:8"]]
+ 00470850 ["INT_ADD", "register:40f0:8", ["const:470850:8", "const:4:8"]]
+ 00470850 ["CALL", null, ["callee:0043b778:8"]]
- 00470810 bytes ca2bff97
+ 00470850 bytes ca2bff97
- 0047080c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0047080c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047080c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047080c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047084c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0047084c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047084c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047084c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047080c bytes 00303c91
+ 0047084c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51be44c505d5bf1d733d8e50f3183b12"></a>

### [`00470940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470940.md) → [`00470980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470980.md) FUN_00470980

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00470814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470814.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00470854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470854.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0047098c",
      "incomplete_value": false,
      "site": "00470990",
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
      "definition_site": "0047094c",
      "incomplete_value": false,
      "site": "00470950",
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
      "0047098c",
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
      "0047098c",
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

- 旧版 [`00470950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470940.md#insn-00470950) · [`0047094c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470940.md#insn-0047094c)
- 新版 `00470990`（命令位置の公開資料なし） · `0047098c`（命令位置の公開資料なし）

~~~diff
- 00470950 ["INT_ADD", "register:40f0:8", ["const:470950:8", "const:4:8"]]
- 00470950 ["CALL", null, ["callee:0043b778:8"]]
+ 00470990 ["INT_ADD", "register:40f0:8", ["const:470990:8", "const:4:8"]]
+ 00470990 ["CALL", null, ["callee:0043b778:8"]]
- 00470950 bytes 7a2bff97
+ 00470990 bytes 7a2bff97
- 0047094c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0047094c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047094c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047094c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047098c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0047098c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047098c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047098c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047094c bytes 00303c91
+ 0047098c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4e45a02362bb0dbd36f883bc0dd792b"></a>

### [`00470a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470a84.md) → [`00470ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ac4.md) _INIT_14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00470b00",
      "incomplete_value": true,
      "site": "00470b1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00470ac0",
      "incomplete_value": true,
      "site": "00470adc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "00470b24",
      "incomplete_value": true,
      "site": "00470b40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00470ae4",
      "incomplete_value": true,
      "site": "00470b00",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "00470b44",
      "incomplete_value": true,
      "site": "00470b60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00470b04",
      "incomplete_value": true,
      "site": "00470b20",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00470b00",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00470b24",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00470b44",
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
      "00470b00",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00470b24",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00470b44",
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

- 旧版 [`00470afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470a84.md#insn-00470afc) · [`00470b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470a84.md#insn-00470b1c) · [`00470be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470a84.md#insn-00470be4)
- 新版 `00470b3c`（命令位置の公開資料なし） · `00470b5c`（命令位置の公開資料なし） · `00470c24`（命令位置の公開資料なし）

~~~diff
- 00470afc ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00470afc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00470afc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00470afc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00470b3c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00470b3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00470b3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00470b3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00470afc bytes 4a093691
+ 00470b3c bytes 4a093791
- 00470b1c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00470b1c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00470b1c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00470b1c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00470b5c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00470b5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00470b5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00470b5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00470b1c bytes 4a553a91
+ 00470b5c bytes 4a893d91
- 00470be4 ["INT_ADD", "register:40f0:8", ["const:470be4:8", "const:4:8"]]
- 00470be4 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00470c24 ["INT_ADD", "register:40f0:8", ["const:470c24:8", "const:4:8"]]
+ 00470c24 ["CALL", null, ["callee:0043b7f8:8"]]
- 00470be4 bytes f52aff97
+ 00470c24 bytes f52aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef8f9dc536c84bdedab21140b04898a4"></a>

### [`00470ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md) → [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) FUN_00470f34

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008519cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008519cc.md) [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) [`00b11858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b11858.md) · 呼出先 32件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00471cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471cdc.md) [`00471f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471f74.md) [`00472078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472078.md)
- 新版 呼出元 3件 [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`00876f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md) [`00b11c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11c80.md) · 呼出先 32件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00471d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471d1c.md) [`00471fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471fb4.md) [`004720b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.28% / 新版 97.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047133c",
      "incomplete_value": true,
      "site": "00471340",
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
      "definition_site": "004712fc",
      "incomplete_value": true,
      "site": "00471300",
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
      "definition_site": "00471338",
      "incomplete_value": true,
      "site": "00471344",
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
      "definition_site": "004712f8",
      "incomplete_value": true,
      "site": "00471304",
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
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00471350",
      "incomplete_value": true,
      "site": "00471350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:48:8"
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
      "definition_site": "00471310",
      "incomplete_value": true,
      "site": "00471310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:48:8"
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
      "0047127c",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ],
    [
      "0047132c",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ],
    [
      "00471330",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047127c",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "0047132c",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "00471330",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md#insn-00471240) · [`00471344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md#insn-00471344) · [`004713c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470ef4.md#insn-004713c0)
- 新版 `00471280`（命令位置の公開資料なし） · `00471384`（命令位置の公開資料なし） · `00471400`（命令位置の公開資料なし）

~~~diff
- 00471240 ["INT_ADD", "register:40f0:8", ["const:471240:8", "const:4:8"]]
- 00471240 ["CALL", null, ["callee:00471d1c:8"]]
+ 00471280 ["INT_ADD", "register:40f0:8", ["const:471280:8", "const:4:8"]]
+ 00471280 ["CALL", null, ["callee:00471d1c:8"]]
- 00471240 bytes a7020094
+ 00471280 bytes a7020094
- 00471344 ["INT_ADD", "register:40f0:8", ["const:471344:8", "const:4:8"]]
- 00471344 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00471384 ["INT_ADD", "register:40f0:8", ["const:471384:8", "const:4:8"]]
+ 00471384 ["CALL", null, ["callee:00c57fb0:8"]]
- 00471344 bytes 1b9a1f94
+ 00471384 bytes 0b9b1f94
- 004713c0 ["INT_ADD", "register:40f0:8", ["const:4713c0:8", "const:4:8"]]
- 004713c0 ["CALL", null, ["callee:00550ba4:8"]]
+ 00471400 ["INT_ADD", "register:40f0:8", ["const:471400:8", "const:4:8"]]
+ 00471400 ["CALL", null, ["callee:00550ba4:8"]]
- 004713c0 bytes e97d0394
+ 00471400 bytes e97d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-527289374c99edb6f5639ff21da9c9f7"></a>

### [`004718f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md) → [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) FUN_00471930

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00484780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md) [`00488750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488750.md) [`0048965c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/0048965c.md) [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`00471f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/00471f74.md) [`00472078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472078.md) [`00472324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472324.md)
- 新版 呼出元 4件 [`004847c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md) [`00488790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md) [`0048969c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/0048969c.md) [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00471fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471fb4.md) [`004720b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md) [`00472364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472364.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.32% / 新版 99.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00471a7c",
      "incomplete_value": false,
      "site": "00471a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471a3c",
      "incomplete_value": false,
      "site": "00471a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00471a7c",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00471a7c",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md#insn-00471a50) · [`00471a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md#insn-00471a90) · [`00471928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00471/004718f0.md#insn-00471928)
- 新版 `00471a90`（命令位置の公開資料なし） · `00471ad0`（命令位置の公開資料なし） · `00471968`（命令位置の公開資料なし）

~~~diff
- 00471a50 ["INT_ADD", "register:40f0:8", ["const:471a50:8", "const:4:8"]]
- 00471a50 ["CALL", null, ["callee:004720b8:8"]]
+ 00471a90 ["INT_ADD", "register:40f0:8", ["const:471a90:8", "const:4:8"]]
+ 00471a90 ["CALL", null, ["callee:004720b8:8"]]
- 00471a50 bytes 8a010094
+ 00471a90 bytes 8a010094
- 00471a90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00471a90 ["INT_ADD", "register:40f0:8", ["const:471a90:8", "const:4:8"]]
- 00471a90 ["CALLIND", null, ["register:0:8"]]
+ 00471ad0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00471ad0 ["INT_ADD", "register:40f0:8", ["const:471ad0:8", "const:4:8"]]
+ 00471ad0 ["CALLIND", null, ["register:0:8"]]
- 00471a90 bytes 00013fd6
+ 00471ad0 bytes 00013fd6
- 00471928 ["INT_ADD", "register:40f0:8", ["const:471928:8", "const:4:8"]]
- 00471928 ["CALL", null, ["callee:00c580e0:8"]]
+ 00471968 ["INT_ADD", "register:40f0:8", ["const:471968:8", "const:4:8"]]
+ 00471968 ["CALL", null, ["callee:00c580e0:8"]]
- 00471928 bytes ee981f94
+ 00471968 bytes de991f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc16ef2f3543ce3b2e530ade7f69264e"></a>

### [`00472630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472630.md) → [`00472670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472670.md) _INIT_15

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004726ac",
      "incomplete_value": true,
      "site": "004726c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0047266c",
      "incomplete_value": true,
      "site": "00472688",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee6:8"
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
      "definition_site": "004726d0",
      "incomplete_value": true,
      "site": "004726ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00472690",
      "incomplete_value": true,
      "site": "004726ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ef9:8"
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
      "definition_site": "004726f0",
      "incomplete_value": true,
      "site": "0047270c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "004726b0",
      "incomplete_value": true,
      "site": "004726cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004726ac",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "004726d0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "004726f0",
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
      "004726ac",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "004726d0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "004726f0",
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

- 旧版 [`004726a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472630.md#insn-004726a8) · [`004726c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472630.md#insn-004726c8) · [`00472790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00472/00472630.md#insn-00472790)
- 新版 `004726e8`（命令位置の公開資料なし） · `00472708`（命令位置の公開資料なし） · `004727d0`（命令位置の公開資料なし）

~~~diff
- 004726a8 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 004726a8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004726a8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004726a8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004726e8 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 004726e8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004726e8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004726e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004726a8 bytes 4a093691
+ 004726e8 bytes 4a093791
- 004726c8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 004726c8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004726c8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004726c8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00472708 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00472708 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00472708 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00472708 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004726c8 bytes 4a553a91
+ 00472708 bytes 4a893d91
- 00472790 ["INT_ADD", "register:40f0:8", ["const:472790:8", "const:4:8"]]
- 00472790 ["CALL", null, ["callee:0043b7f8:8"]]
+ 004727d0 ["INT_ADD", "register:40f0:8", ["const:4727d0:8", "const:4:8"]]
+ 004727d0 ["CALL", null, ["callee:0043b7f8:8"]]
- 00472790 bytes 0a24ff97
+ 004727d0 bytes 0a24ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

